"""Third Autocorrelation (P4) — FFT-based smooth-max gradient optimizer.

Same as optimize_torch.py but uses torch.fft for O(n log n) convolution,
enabling much larger n.
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np
import torch

from einstein.third_autocorrelation.evaluator import verify_and_compute

MB_SOLUTIONS = Path.home() / "projects/workbench/memory-bank/einstein/docs/problem-4-third-autocorrelation/solutions"


def load_sota_n400() -> np.ndarray:
    with open(MB_SOLUTIONS / "rank01_DarwinAgent8427_n400.json") as fh:
        return np.array(json.load(fh)["values"], dtype=np.float64)


def upsample_block(v: np.ndarray, n_target: int) -> np.ndarray:
    n_src = len(v)
    if n_target == n_src:
        return v.copy()
    if n_target % n_src == 0:
        k = n_target // n_src
        return np.repeat(v, k)
    # Generic: sample via piecewise-constant indexing
    out = np.empty(n_target, dtype=np.float64)
    for i in range(n_target):
        src_i = int(i * n_src / n_target)
        out[i] = v[src_i]
    return out


def smooth_max(x: torch.Tensor, beta: float) -> torch.Tensor:
    return (1.0 / beta) * torch.logsumexp(beta * x, dim=-1)


def fft_autoconv(f: torch.Tensor) -> torch.Tensor:
    """Compute full autoconvolution via FFT (length 2n-1)."""
    n = f.shape[-1]
    m = 2 * n - 1
    # Use next power of 2 for efficiency
    m_pad = 1 << (m - 1).bit_length()
    F = torch.fft.rfft(f, n=m_pad)
    # Autoconvolution = F * F (Fourier of f*f, NOT correlation)
    conv = torch.fft.irfft(F * F, n=m_pad)[:m]
    return conv


def compute_score_torch(f: torch.Tensor, beta: float) -> torch.Tensor:
    n = f.shape[-1]
    dx = 0.5 / n
    conv = fft_autoconv(f) * dx
    peak = smooth_max(conv, beta)
    integral = f.sum() * dx
    return peak / (integral ** 2)


def exact_score(f: torch.Tensor) -> float:
    return float(verify_and_compute(f.detach().cpu().numpy().tolist()))


def optimize(n: int, start: str, beta_cascade, iters: int, lr: float,
             seed: int = 0, device: str = "cpu"):
    rng = np.random.default_rng(seed)
    torch.manual_seed(seed)

    if start == "sota":
        v0 = load_sota_n400()
        if n != 400:
            v0 = upsample_block(v0, n)
            v0 = v0 + rng.normal(scale=1e-6 * np.std(v0), size=v0.shape)
    elif start.endswith(".json"):
        with open(start) as fh:
            d = json.load(fh)
        v0 = np.array(d["values"], dtype=np.float64)
        if len(v0) != n:
            v0 = upsample_block(v0, n)
            v0 = v0 + rng.normal(scale=1e-7 * np.std(v0), size=v0.shape)
    else:
        raise ValueError(f"Unknown start: {start}")

    f = torch.tensor(v0, dtype=torch.float64, device=device, requires_grad=True)
    print(f"\nStart: {start}  n={n}")
    print(f"Initial exact C = {exact_score(f):.13f}")

    best_c = exact_score(f)
    best_v = f.detach().cpu().numpy().copy()

    for beta in beta_cascade:
        print(f"\n--- beta = {beta:.0e} ---", flush=True)
        opt = torch.optim.LBFGS(
            [f], lr=lr, max_iter=iters, tolerance_grad=1e-14,
            tolerance_change=1e-16, history_size=100,
            line_search_fn="strong_wolfe"
        )

        def closure():
            opt.zero_grad()
            c = compute_score_torch(f, beta)
            c.backward()
            return c

        t0 = time.time()
        opt.step(closure)
        dt = time.time() - t0
        c_smooth = float(compute_score_torch(f, beta).detach())
        c_exact = exact_score(f)
        print(f"  smooth={c_smooth:.13f}  exact={c_exact:.13f}  ({dt:.1f}s)",
              flush=True)
        if c_exact < best_c:
            best_c = c_exact
            best_v = f.detach().cpu().numpy().copy()
            print(f"  NEW BEST: {best_c:.13f}", flush=True)

    return best_v, best_c


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--n", type=int, default=12800)
    p.add_argument("--start", type=str, default="sota")
    p.add_argument("--beta-cascade", type=str, default="1e4,3e4,1e5,3e5,1e6,3e6,1e7,3e7")
    p.add_argument("--iters", type=int, default=1500)
    p.add_argument("--lr", type=float, default=1.0)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--device", type=str, default="cpu")
    p.add_argument("--out", type=str, default=None)
    args = p.parse_args()

    betas = [float(b) for b in args.beta_cascade.split(",")]
    best_v, best_c = optimize(args.n, args.start, betas, args.iters,
                              args.lr, args.seed, args.device)

    print(f"\n=== Final: C = {best_c:.13f}  (n={args.n}) ===")
    print(f"SOTA ref: 1.4540379299619")
    print(f"Delta vs SOTA: {best_c - 1.4540379299619:.6e}")

    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        with open(args.out, "w") as fh:
            json.dump({"values": best_v.tolist(), "score": best_c, "n": args.n}, fh)
        print(f"Saved: {args.out}")


if __name__ == "__main__":
    main()
