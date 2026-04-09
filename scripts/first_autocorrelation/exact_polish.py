"""Direct exact-max gradient polish for First Autocorrelation.

After the smooth-surrogate cascade has concentrated the autocorrelation to a
single strict peak t*, C(f) is locally differentiable:

    C(f) = conv[t*] * dx / (sum(f) * dx)^2
         = conv[t*] / (sum(f)^2 * dx)
    dC/df_i = (2/sum(f)^2 / dx) * f_{t*-i}  -  (2 * C / sum(f))

Project this onto the non-negative orthant (zero the partial where f_i ≈ 0
and dC/df_i >= 0 — that's a KKT-consistent active set), then take a cautious
line-search step. Re-check the argmax each iteration: if a different t claims
the peak, update.

Usage:
    uv run python scripts/first_autocorrelation/exact_polish.py \\
        --warmstart PATH --iters 2000 --out OUTPUT
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np

from einstein.first_autocorrelation.evaluator import verify_and_compute


def exact_score(f: np.ndarray) -> float:
    return float(verify_and_compute(f.tolist()))


def conv_full(f: np.ndarray) -> np.ndarray:
    """Full autoconvolution via real FFT, length 2n-1."""
    n = len(f)
    m = 2 * n - 1
    m_pad = 1 << (m - 1).bit_length()
    F = np.fft.rfft(f, n=m_pad)
    return np.fft.irfft(F * F, n=m_pad)[:m]


def gradient_at_peak(f: np.ndarray, t_star: int) -> np.ndarray:
    """Exact dC/df at the unique-peak basin.

    C = conv[t*] / (sum(f)^2 * dx),  conv[t*] = sum_k f_k f_{t*-k}.
    dC/df_i = 2 f_{t*-i} / (sum(f)^2 * dx) - 2 C / sum(f).
    """
    n = len(f)
    dx = 0.5 / n
    s = f.sum()
    conv_t = 0.0
    # 2 f_{t*-i} / (s^2 dx)
    lo = max(0, t_star - (n - 1))
    hi = min(n - 1, t_star)
    # Build the "mirror" vector g where g[i] = f[t_star - i] if valid, else 0
    g = np.zeros(n, dtype=np.float64)
    for i in range(lo, hi + 1):
        g[i] = f[t_star - i]
        conv_t += f[i] * f[t_star - i]
    C = conv_t * dx / (s * dx) ** 2
    grad = (2.0 * g) / (s * s * dx) - (2.0 * C) / s
    return grad, C


def gradient_at_peak_fast(f: np.ndarray, t_star: int) -> tuple[np.ndarray, float]:
    """Vectorized mirror-vector construction."""
    n = len(f)
    dx = 0.5 / n
    s = f.sum()
    g = np.zeros(n, dtype=np.float64)
    lo = max(0, t_star - (n - 1))
    hi = min(n - 1, t_star)
    i_idx = np.arange(lo, hi + 1)
    j_idx = t_star - i_idx
    g[i_idx] = f[j_idx]
    conv_t = float(np.dot(f[i_idx], f[j_idx]))
    C = conv_t * dx / (s * dx) ** 2
    grad = (2.0 * g) / (s * s * dx) - (2.0 * C) / s
    return grad, C


def polish(f: np.ndarray, iters: int, lr0: float, verbose: bool = True) -> tuple[np.ndarray, float]:
    f = f.astype(np.float64).copy()
    n = len(f)
    best_c = exact_score(f)
    best_f = f.copy()
    lr = lr0
    no_improve = 0
    t_star_prev = -1

    for it in range(iters):
        # exact hard max position
        conv = conv_full(f)
        t_star = int(np.argmax(conv))
        grad, C_at_peak = gradient_at_peak_fast(f, t_star)

        # KKT: for cells where f_i <= 0 (effectively zero), only subtract
        # gradient if grad < 0 (i.e., increasing f_i helps).
        active_or_increasing = (f > 1e-30) | (grad < 0)

        step_dir = np.where(active_or_increasing, -grad, 0.0)
        # normalize step for stability
        gnorm = np.linalg.norm(step_dir)
        if gnorm < 1e-30:
            if verbose:
                print(f"  iter={it}  gnorm tiny, stopping")
            break
        d = step_dir / gnorm

        # backtracking line search on the EXACT C
        accepted = False
        for _ in range(60):
            f_try = f + lr * d
            # enforce non-negativity by clipping (the projection)
            f_try = np.maximum(f_try, 0.0)
            if f_try.sum() <= 0:
                lr *= 0.5
                continue
            c_try = exact_score(f_try)
            if c_try < best_c:
                f = f_try
                if c_try < best_c:
                    best_c = c_try
                    best_f = f.copy()
                lr = min(lr * 1.5, lr0)
                accepted = True
                no_improve = 0
                break
            lr *= 0.5
        if not accepted:
            no_improve += 1
            lr = lr0  # reset for a fresh direction next iter
            if no_improve >= 5:
                if verbose:
                    print(f"  iter={it}  stuck (5 failed line searches)")
                break

        if verbose and (it < 20 or it % 50 == 0):
            print(f"  iter={it:>5}  C={best_c:.18f}  lr={lr:.2e}  "
                  f"t*={t_star}  gnorm={gnorm:.2e}  "
                  f"{'* new peak' if t_star != t_star_prev else ''}",
                  flush=True)
        t_star_prev = t_star

    return best_f, best_c


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--warmstart", type=Path, required=True)
    p.add_argument("--iters", type=int, default=2000)
    p.add_argument("--lr", type=float, default=1e-6)
    p.add_argument("--out", type=Path, default=None)
    args = p.parse_args()

    with open(args.warmstart) as fh:
        data = json.load(fh)
    f0 = np.array(data["values"], dtype=np.float64)
    print(f"Warmstart: {args.warmstart}  n={len(f0)}")
    print(f"Initial C = {exact_score(f0):.18f}")

    t0 = time.time()
    f_best, c_best = polish(f0, args.iters, args.lr, verbose=True)
    print(f"\nFinal C = {c_best:.18f}  ({time.time()-t0:.1f}s)")

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with open(args.out, "w") as fh:
            json.dump(
                {"values": f_best.tolist(), "score": c_best, "n": len(f_best)}, fh
            )
        print(f"Saved: {args.out}")


if __name__ == "__main__":
    main()
