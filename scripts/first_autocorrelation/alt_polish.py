"""Alternate smooth-max cascade and exact-max subgradient polish.

Use the softmax-weighted gradient across the top-K active peaks to step
in the direction that reduces all near-active conv values simultaneously.
"""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np
import torch

from einstein.first_autocorrelation.evaluator import verify_and_compute
from einstein.first_autocorrelation.optimizer import (
    exact_score_f,
    surrogate_v,
    to_v,
)


def cascade(v_np, betas, iters):
    v = torch.tensor(v_np.copy(), dtype=torch.float64, requires_grad=True)
    for beta in betas:
        opt = torch.optim.LBFGS(
            [v], lr=1.0, max_iter=iters, tolerance_grad=1e-15,
            tolerance_change=1e-20, history_size=200,
            line_search_fn="strong_wolfe",
        )
        def closure():
            opt.zero_grad()
            loss = surrogate_v(v, beta, fft=True)
            loss.backward()
            return loss
        opt.step(closure)
    f = np.exp(v.detach().cpu().numpy()).astype(np.float64)
    return f, exact_score_f(f)


def multi_peak_polish(f: np.ndarray, iters: int, topk: int = 200,
                     lr0: float = 1e-4) -> tuple[np.ndarray, float]:
    """Simultaneous subgradient on top-K peaks of f★f."""
    f = f.astype(np.float64).copy()
    n = len(f)
    dx = 0.5 / n
    best_c = exact_score_f(f)
    best_f = f.copy()
    lr = lr0
    no_improve = 0

    for it in range(iters):
        s = f.sum()
        # FFT conv
        m = 2 * n - 1
        m_pad = 1 << (m - 1).bit_length()
        F = np.fft.rfft(f, n=m_pad)
        conv = np.fft.irfft(F * F, n=m_pad)[:m]
        ratios = conv * dx / (s * dx) ** 2

        # Top K peaks
        top_idx = np.argpartition(ratios, -topk)[-topk:]
        top_vals = ratios[top_idx]
        max_val = top_vals.max()

        # Softmax weights across top K (emphasize the true max)
        beta = 1e6
        z = beta * (top_vals - max_val)
        w = np.exp(z)
        w /= w.sum()

        # Build weighted mirror-vector gradient:
        # For each peak t*, grad_t* = 2*mirror(f, t*)/(s^2*dx) - 2*C/s
        # Weighted sum over top peaks.
        mirror_sum = np.zeros(n, dtype=np.float64)
        c_sum = 0.0
        for wi, ti in zip(w, top_idx):
            lo = max(0, ti - (n - 1))
            hi = min(n - 1, ti)
            j_idx = ti - np.arange(lo, hi + 1)
            mirror_sum[lo:hi+1] += wi * f[j_idx]
            c_sum += wi * ratios[ti]
        grad = (2.0 * mirror_sum) / (s * s * dx) - (2.0 * c_sum) / s

        # Project: zero components where f=0 and grad >= 0 (inactive)
        active = (f > 1e-30) | (grad < 0)
        step = np.where(active, -grad, 0.0)
        gnorm = np.linalg.norm(step)
        if gnorm < 1e-30:
            break
        d = step / gnorm

        accepted = False
        for _ in range(50):
            f_try = np.maximum(f + lr * d, 0.0)
            if f_try.sum() <= 0:
                lr *= 0.5
                continue
            c_try = exact_score_f(f_try)
            if c_try < best_c:
                f = f_try
                best_c = c_try
                best_f = f.copy()
                lr = min(lr * 1.3, lr0 * 10)
                accepted = True
                no_improve = 0
                break
            lr *= 0.5
        if not accepted:
            no_improve += 1
            lr = lr0
            if no_improve >= 6:
                break

        if it % 20 == 0:
            print(f"    polish iter={it:>4} C={best_c:.18f} lr={lr:.2e} "
                  f"gnorm={gnorm:.2e}", flush=True)

    return best_f, best_c


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--warmstart", type=Path, required=True)
    p.add_argument("--n", type=int, required=True)
    p.add_argument("--rounds", type=int, default=6)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()

    with open(args.warmstart) as fh:
        data = json.load(fh)
    f = np.array(data["values"], dtype=np.float64)
    if len(f) != args.n:
        from einstein.first_autocorrelation.optimizer import upsample
        f = upsample(f, args.n)
    c = exact_score_f(f)
    print(f"Initial: n={args.n} C={c:.18f}")

    best_c = c
    best_f = f.copy()
    t0 = time.time()

    for r in range(args.rounds):
        # Round: cascade → polish
        print(f"--- round {r}: cascade ---")
        v0 = to_v(f, floor=1e-25)
        f, c_cas = cascade(v0, [1e9, 1e10, 1e11, 1e12], iters=2000)
        print(f"  after cascade: C={c_cas:.18f}")
        if c_cas < best_c:
            best_c = c_cas
            best_f = f.copy()
            print(f"  * NEW BEST")

        print(f"--- round {r}: multi-peak polish ---")
        f, c_pol = multi_peak_polish(f, iters=100, topk=200, lr0=1e-5)
        print(f"  after polish:  C={c_pol:.18f}")
        if c_pol < best_c:
            best_c = c_pol
            best_f = f.copy()
            print(f"  * NEW BEST")

    print(f"\nBest C = {best_c:.18f}  ({time.time()-t0:.1f}s)")
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w") as fh:
        json.dump({"values": best_f.tolist(), "score": best_c, "n": args.n},
                  fh)
    print(f"Saved: {args.out}")


if __name__ == "__main__":
    main()
