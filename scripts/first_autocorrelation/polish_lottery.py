"""Fast ulp-scale polish lottery on f directly (not via log param).

Inspired by the prior branch's long_polish.py — random perturbations at
several scales with greedy accept. For basin-floor residual improvement.
"""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np

from einstein.first_autocorrelation.evaluator import verify_and_compute


def exact_c(f: np.ndarray) -> float:
    return float(verify_and_compute(f.tolist()))


def conv_fft_c(f: np.ndarray) -> float:
    n = len(f)
    dx = 0.5 / n
    m = 2 * n - 1
    m_pad = 1 << (m - 1).bit_length()
    F = np.fft.rfft(f, n=m_pad)
    conv = np.fft.irfft(F * F, n=m_pad)[:m]
    return float(np.max(conv) * dx / (f.sum() * dx) ** 2)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--warmstart", type=Path, required=True)
    p.add_argument("--duration-sec", type=float, default=300)
    p.add_argument("--scales", type=str,
                   default="1e-16,1e-15,1e-14,1e-13,1e-12,1e-11,1e-10,1e-9,1e-8")
    p.add_argument("--perturb-cells", type=int, nargs=2, default=[1, 100])
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()

    with open(args.warmstart) as fh:
        data = json.load(fh)
    f = np.array(data["values"], dtype=np.float64)
    n = len(f)
    rng = np.random.default_rng(args.seed)

    # Warm: use np.convolve to match arena exactly
    best_c = exact_c(f)
    print(f"n={n}  initial C = {best_c:.18f}")

    scales = [float(x) for x in args.scales.split(",")]
    k_lo, k_hi = args.perturb_cells

    t0 = time.time()
    n_trials = 0
    n_accepted = 0
    last_report = t0
    max_amp = float(f.max())

    while time.time() - t0 < args.duration_sec:
        scale = scales[n_trials % len(scales)]
        k = rng.integers(k_lo, k_hi + 1)
        idx = rng.integers(0, n, size=k)
        sign = rng.choice([-1.0, 1.0], size=k)
        delta_vec = scale * sign * max_amp
        f_try = f.copy()
        f_try[idx] += delta_vec
        if np.any(f_try < 0):
            f_try = np.maximum(f_try, 0.0)
        c_try = exact_c(f_try)
        n_trials += 1
        if c_try < best_c:
            f = f_try
            best_c = c_try
            n_accepted += 1

        if time.time() - last_report > 10:
            rate = n_trials / (time.time() - t0)
            print(f"  t={time.time()-t0:.0f}s  trials={n_trials}  "
                  f"accepted={n_accepted}  C={best_c:.18f}  "
                  f"rate={rate:.0f}/s", flush=True)
            last_report = time.time()

    print(f"\nFinal C = {best_c:.18f}  ({time.time()-t0:.0f}s, "
          f"{n_trials} trials, {n_accepted} accepted)")
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w") as fh:
        json.dump({"values": f.tolist(), "score": best_c, "n": n}, fh)
    print(f"Saved: {args.out}")


if __name__ == "__main__":
    main()
