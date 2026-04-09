"""Bandlimit-Fourier parameterized L-BFGS for a log-positive scalar field.

Restrict the log-parameter ``v`` to a low-frequency Fourier subspace of
bandwidth ``T`` (``T`` real + ``T`` imaginary rfft coefficients) and run
L-BFGS on the real parameters. The rest of ``v``'s rfft spectrum is zeroed
out. Acts as a smoothness regularizer on the underlying field.

Usage:
    uv run python scripts/first_autocorrelation/fourier_lbfgs.py \\
        --warmstart PATH --T 500 --betas 1e6,1e7,1e8,1e9,1e10 --out OUT
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np
import torch

from einstein.first_autocorrelation.evaluator import verify_and_compute


# ----------------------------------------------------------------------------
# Fourier basis: v parameterized by T complex rfft coefficients
# ----------------------------------------------------------------------------

def v_from_coefs(c_re: torch.Tensor, c_im: torch.Tensor, n: int) -> torch.Tensor:
    """Reconstruct v (real length n) from its first T rfft coefficients.

    Higher-frequency coefficients are zero (strict bandlimit).
    Uses torch.fft.irfft for efficiency.
    """
    T = c_re.shape[0]
    half = n // 2 + 1
    # Pad to full rfft length with zeros
    c_complex = torch.complex(c_re, c_im)
    pad_len = half - T
    if pad_len > 0:
        padding = torch.zeros(pad_len, dtype=torch.complex128, device=c_re.device)
        c_padded = torch.cat([c_complex, padding])
    else:
        c_padded = c_complex[:half]
    return torch.fft.irfft(c_padded, n=n)


def coefs_from_v(v: np.ndarray, T: int):
    """Extract first T complex rfft coefficients of v."""
    V = np.fft.rfft(v)
    c = V[:T]
    return c.real.copy(), c.imag.copy()


# ----------------------------------------------------------------------------
# Objective: smooth surrogate C(f) with f = exp(v)
# ----------------------------------------------------------------------------

def autoconv_fft(f: torch.Tensor) -> torch.Tensor:
    n = f.shape[-1]
    m = 2 * n - 1
    m_pad = 1 << (m - 1).bit_length()
    F = torch.fft.rfft(f, n=m_pad)
    return torch.fft.irfft(F * F, n=m_pad)[:m]


def smooth_max(x: torch.Tensor, beta: float) -> torch.Tensor:
    return (1.0 / beta) * torch.logsumexp(beta * x, dim=-1)


def surrogate_from_coefs(
    c_re: torch.Tensor,
    c_im: torch.Tensor,
    n: int,
    beta: float,
) -> torch.Tensor:
    """Smooth surrogate of C evaluated through the Fourier parameterization."""
    v = v_from_coefs(c_re, c_im, n)
    f = torch.exp(v)
    dx = 0.5 / n
    conv = autoconv_fft(f)
    integral_sum = f.sum()
    ratios = conv / (integral_sum * integral_sum * dx)
    return smooth_max(ratios, beta)


def exact_C_from_coefs(c_re: torch.Tensor, c_im: torch.Tensor, n: int) -> float:
    v = v_from_coefs(c_re, c_im, n).detach().cpu().numpy()
    f = np.exp(v).astype(np.float64)
    return float(verify_and_compute(f.tolist()))


# ----------------------------------------------------------------------------
# Main optimization
# ----------------------------------------------------------------------------

def optimize_fourier(
    warmstart: Path,
    T: int,
    betas: list[float],
    iters: int,
    lr: float,
    seed: int,
    noise: float,
    floor: float,
):
    rng = np.random.default_rng(seed)
    torch.manual_seed(seed)

    with open(warmstart) as fh:
        d = json.load(fh)
    f_warm = np.array(d["values"], dtype=np.float64)
    n = len(f_warm)
    print(f"Warmstart: {warmstart}  n={n}  T={T}  (DoF = {2*T})", flush=True)

    v_warm = np.log(np.maximum(f_warm, floor))
    C_initial = float(verify_and_compute(f_warm.tolist()))
    print(f"Initial C (full-DoF) = {C_initial:.16f}", flush=True)

    # Truncate to first T Fourier coefficients
    c_re_np, c_im_np = coefs_from_v(v_warm, T)
    if noise > 0:
        c_re_np = c_re_np + rng.normal(scale=noise, size=c_re_np.shape)
        c_im_np = c_im_np + rng.normal(scale=noise, size=c_im_np.shape)

    c_re = torch.tensor(c_re_np, dtype=torch.float64, requires_grad=True)
    c_im = torch.tensor(c_im_np, dtype=torch.float64, requires_grad=True)

    # Check: after truncation and reconstruction, what is C?
    C_truncated = exact_C_from_coefs(c_re, c_im, n)
    print(f"After FFT-truncate to T={T}: C = {C_truncated:.16f}", flush=True)

    best_C = C_truncated
    best_c_re = c_re.detach().cpu().numpy().copy()
    best_c_im = c_im.detach().cpu().numpy().copy()

    for beta in betas:
        opt = torch.optim.LBFGS(
            [c_re, c_im], lr=lr, max_iter=iters,
            tolerance_grad=1e-14, tolerance_change=1e-18,
            history_size=100, line_search_fn="strong_wolfe",
        )

        def closure():
            opt.zero_grad()
            loss = surrogate_from_coefs(c_re, c_im, n, beta)
            loss.backward()
            return loss

        t0 = time.time()
        opt.step(closure)
        c_now = exact_C_from_coefs(c_re, c_im, n)
        print(
            f"  beta={beta:.0e}  C={c_now:.16f}  "
            f"delta_best={best_C - c_now:+.3e}  ({time.time()-t0:.1f}s)",
            flush=True,
        )
        if c_now < best_C:
            best_C = c_now
            best_c_re = c_re.detach().cpu().numpy().copy()
            best_c_im = c_im.detach().cpu().numpy().copy()

    # Reconstruct best f
    with torch.no_grad():
        best_v = v_from_coefs(
            torch.tensor(best_c_re, dtype=torch.float64),
            torch.tensor(best_c_im, dtype=torch.float64),
            n,
        ).cpu().numpy()
    best_f = np.exp(best_v).astype(np.float64)
    return best_f, best_C


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--warmstart", type=Path, required=True)
    p.add_argument("--T", type=int, default=500,
                   help="Fourier bandwidth (first T rfft coefficients)")
    p.add_argument("--betas", type=str, default="1e6,1e7,1e8,1e9,1e10,1e11")
    p.add_argument("--iters", type=int, default=1500)
    p.add_argument("--lr", type=float, default=1.0)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--noise", type=float, default=0.0)
    p.add_argument("--floor", type=float, default=1e-30)
    p.add_argument("--out", type=Path, default=None)
    args = p.parse_args()

    betas = [float(b) for b in args.betas.split(",")]
    best_f, best_C = optimize_fourier(
        args.warmstart, args.T, betas, args.iters, args.lr,
        args.seed, args.noise, args.floor,
    )

    print(f"\n=== FINAL ===", flush=True)
    print(f"Best C = {best_C:.16f}")

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with open(args.out, "w") as fh:
            json.dump({
                "values": best_f.tolist(),
                "score": best_C,
                "n": len(best_f),
                "T": args.T,
                "warmstart": str(args.warmstart),
            }, fh)
        print(f"Saved: {args.out}")


if __name__ == "__main__":
    main()
