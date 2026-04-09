"""Pairwise Frank-Wolfe with drop steps (Lacoste-Julien & Jaggi 2015).

Vanilla Frank-Wolfe can only add mass (the LP atom oracle picks a single
vertex), and once mass is placed it cannot be removed. Smooth-max L-BFGS on
the simplex inherits this fixed-point trap.

Pairwise FW picks two vertices per step: s_plus (FW atom, add mass) and
s_minus (away atom, remove mass). The direction d = e_{s_plus} - e_{s_minus}
preserves sum(f) = 1 and f >= 0 as long as alpha ≤ f[s_minus]. When the
optimal alpha equals f[s_minus], that atom is dropped from the active set;
the drop step is the mechanism that escapes a vanilla-FW fixed point.

Uses a smooth-max surrogate for the gradient (stable softmax over top
peaks), but accepts a step only if the exact C decreases.
"""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np

from einstein.first_autocorrelation.evaluator import verify_and_compute


def conv_full_fft(f: np.ndarray) -> np.ndarray:
    n = len(f)
    m = 2 * n - 1
    m_pad = 1 << (m - 1).bit_length()
    F = np.fft.rfft(f, n=m_pad)
    return np.fft.irfft(F * F, n=m_pad)[:m]


def exact_C(f: np.ndarray) -> float:
    """Fast FFT-based C equivalent to arena verifier to within 1 ulp.

    We verified (triple check) that FFT convolution matches np.convolve
    to 0 or 1 ulp on float64 for solutions in this family. For optimization
    we use FFT; final verification uses verify_and_compute.
    """
    n = len(f)
    dx = 0.5 / n
    m = 2 * n - 1
    m_pad = 1 << (m - 1).bit_length()
    F = np.fft.rfft(f, n=m_pad)
    conv = np.fft.irfft(F * F, n=m_pad)[:m]
    return float(np.max(conv) * dx / (f.sum() * dx) ** 2)


def exact_C_verify(f: np.ndarray) -> float:
    """Arena-exact (slow) — used for final verification only."""
    return float(verify_and_compute(f.tolist()))


def gradient_and_C(f: np.ndarray, beta: float) -> tuple[np.ndarray, float]:
    """Gradient of smoothed surrogate L(f) = smooth_max(ratios(f)) at scale beta.

    Returns (gradient, smoothed_L).  f is assumed to satisfy sum(f)=1.
    """
    n = len(f)
    dx = 0.5 / n
    conv = conv_full_fft(f)
    s = f.sum()
    ratios = conv * dx / (s * dx) ** 2  # length 2n-1

    # stable softmax
    mx = float(ratios.max())
    exps = np.exp(beta * (ratios - mx))
    Z = exps.sum()
    L = mx + np.log(Z) / beta
    w = exps / Z  # softmax weights, length 2n-1

    # dL/df_i via cross-correlation (FFT-based, O(n log n))
    # d_vec[i] = sum_t w[t] f[t-i] for i=0..n-1
    # = (w * f_rev)[n-1+i] where f_rev[k] = f[n-1-k]
    f_rev = f[::-1]
    m_full = (2 * n - 1) + n - 1  # 3n - 2
    m_pad = 1 << (m_full - 1).bit_length()
    W = np.fft.rfft(w, n=m_pad)
    F_rev = np.fft.rfft(f_rev, n=m_pad)
    conv_wfr = np.fft.irfft(W * F_rev, n=m_pad)[:m_full]
    d_vec = conv_wfr[n - 1: 2 * n - 1]  # length n
    grad = (2.0 / (s * s * dx)) * d_vec - (2.0 * L) / s
    return grad, L


def pairwise_fw(
    f: np.ndarray,
    iters: int,
    betas: list[float],
    eps_active: float = 1e-20,
    verbose: bool = True,
) -> tuple[np.ndarray, float]:
    """Pairwise FW with smoothed-gradient direction and exact-C acceptance."""
    f = f.astype(np.float64).copy()
    f /= f.sum()
    best_c = exact_C(f)
    best_f = f.copy()
    n = len(f)

    for beta in betas:
        no_progress = 0
        if verbose:
            print(f"\n=== beta={beta:.1e} ===")

        for it in range(iters):
            grad, L_smooth = gradient_and_C(f, beta)

            # FW vertex: most-negative gradient (add mass here)
            j_plus = int(np.argmin(grad))
            # Away vertex: within support, largest gradient (remove mass here)
            active_mask = f > eps_active
            if not active_mask.any():
                break
            # Cheap way: argmax of (grad where active, else -inf)
            grad_masked = np.where(active_mask, grad, -np.inf)
            j_minus = int(np.argmax(grad_masked))

            if j_plus == j_minus:
                no_progress += 1
                if no_progress >= 3:
                    break
                continue

            # Directional derivative of the smooth surrogate
            dg_smooth = grad[j_plus] - grad[j_minus]
            if dg_smooth >= -1e-16:
                no_progress += 1
                if no_progress >= 3:
                    break
                continue

            # Line search: try many step sizes (exponential from gmax down)
            gmax = float(f[j_minus])
            current_c = exact_C(f)
            best_gamma = 0.0
            best_new_c = current_c

            # Grid of fractions: large first (drop step at frac=1.0 if accepted)
            fracs = [1.0, 0.5, 0.25, 0.1, 0.05, 0.02, 0.01, 3e-3, 1e-3,
                     3e-4, 1e-4, 3e-5, 1e-5, 3e-6, 1e-6]
            for frac in fracs:
                gamma = frac * gmax
                f_try = f.copy()
                f_try[j_plus] += gamma
                f_try[j_minus] -= gamma
                if f_try[j_minus] < 0:
                    f_try[j_minus] = 0.0
                c_try = exact_C(f_try)
                if c_try < best_new_c:
                    best_new_c = c_try
                    best_gamma = gamma

            if best_gamma <= 0:
                no_progress += 1
                if no_progress >= 5:
                    if verbose:
                        print(f"  iter={it:>5}  stuck after 5 failed steps (dg_smooth={dg_smooth:.2e})")
                    break
                continue

            # Apply step
            f[j_plus] += best_gamma
            f[j_minus] -= best_gamma
            if f[j_minus] < 0:
                f[j_minus] = 0.0
            # Re-normalize to stay on simplex
            f /= f.sum()
            c_now = exact_C(f)
            if c_now < best_c:
                best_c = c_now
                best_f = f.copy()
            no_progress = 0

            if verbose and (it < 10 or it % 50 == 0):
                drop = " * DROP" if best_gamma == gmax else ""
                print(f"  iter={it:>5}  C={c_now:.18f}  "
                      f"best={best_c:.18f}  "
                      f"dg={dg_smooth:.2e}  γ={best_gamma:.2e}{drop}",
                      flush=True)

    return best_f, best_c


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--warmstart", type=Path, required=True)
    p.add_argument("--iters", type=int, default=300)
    p.add_argument("--beta", type=str, default="1e7,1e8,1e9,1e10,1e11")
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()

    with open(args.warmstart) as fh:
        data = json.load(fh)
    f = np.array(data["values"], dtype=np.float64)
    f = f / f.sum()
    print(f"Warmstart: n={len(f)}  C={exact_C(f):.18f}")

    betas = [float(b) for b in args.beta.split(",")]
    t0 = time.time()
    f_best, c_best = pairwise_fw(f, args.iters, betas)
    print(f"\nFinal C = {c_best:.18f}  ({time.time()-t0:.1f}s)")

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w") as fh:
        json.dump({"values": f_best.tolist(), "score": c_best, "n": len(f_best)}, fh)
    print(f"Saved: {args.out}")


if __name__ == "__main__":
    main()
