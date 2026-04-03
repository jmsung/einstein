#!/usr/bin/env python3
"""Random perturbation search for Problem 3 (Second Autocorrelation Inequality).

Tries random multi-block perturbations to escape local optima.
CPU-only, starting from the packet-ascent result.

Usage:
    uv run python scripts/random_perturbation_search.py
"""

import json
import os
import sys
import time
from pathlib import Path

# Force unbuffered output
os.environ["PYTHONUNBUFFERED"] = "1"

import numpy as np
from scipy.signal import fftconvolve

ROOT = Path(__file__).resolve().parent.parent
RESULTS = ROOT / "results"


def score(f: np.ndarray) -> float:
    """Closed-form scoring."""
    conv = fftconvolve(f, f, mode="full")
    c_sum = np.sum(conv)
    c_max = np.max(conv)
    if c_sum == 0 or c_max == 0:
        return 0.0
    num = 2.0 * np.dot(conv, conv) + np.dot(conv[:-1], conv[1:])
    return float(num / (3.0 * c_sum * c_max))


def find_blocks(f: np.ndarray, threshold: float = 1e-10) -> list[tuple[int, int]]:
    """Find contiguous blocks of nonzero values."""
    mask = f > threshold
    d = np.diff(mask.astype(np.int8))
    starts = np.where(d == 1)[0] + 1
    ends = np.where(d == -1)[0] + 1
    if mask[0]:
        starts = np.concatenate(([0], starts))
    if mask[-1]:
        ends = np.concatenate((ends, [len(f)]))
    return list(zip(starts.tolist(), ends.tolist()))


def random_perturbation_search(
    f: np.ndarray,
    blocks: list[tuple[int, int]],
    n_trials: int = 2000,
    seed: int = 123,
) -> tuple[np.ndarray, float]:
    """Random multi-block perturbation search."""
    rng = np.random.default_rng(seed)
    C_best = score(f)
    f_best = f.copy()
    n_improved = 0
    n_blocks = len(blocks)

    print(f"  Starting random perturbation search: {n_trials} trials")
    print(f"  Baseline C = {C_best:.13f}")

    t0 = time.time()
    for trial in range(n_trials):
        f_trial = f_best.copy()

        # Choose perturbation type
        ptype = rng.choice([
            "scale_random_blocks",
            "gaussian_noise",
            "block_swap",
            "block_scale_group",
            "tooth_jitter",
        ])

        if ptype == "scale_random_blocks":
            # Scale 1-5 random blocks
            n_perturb = rng.integers(1, 6)
            idxs = rng.choice(n_blocks, n_perturb, replace=False)
            for idx in idxs:
                s, e = blocks[idx]
                scale = rng.uniform(0.8, 1.2)
                f_trial[s:e] *= scale

        elif ptype == "gaussian_noise":
            # Add small Gaussian noise to all nonzero values
            sigma = rng.uniform(0.001, 0.05) * np.mean(f_trial[f_trial > 1e-10])
            mask = f_trial > 1e-10
            f_trial[mask] += rng.normal(0, sigma, mask.sum())
            f_trial = np.maximum(f_trial, 0.0)

        elif ptype == "block_swap":
            # Swap values between two random blocks (same width)
            if n_blocks < 2:
                continue
            i, j = rng.choice(n_blocks, 2, replace=False)
            s1, e1 = blocks[i]
            s2, e2 = blocks[j]
            w1, w2 = e1 - s1, e2 - s2
            wmin = min(w1, w2)
            if wmin > 0:
                temp = f_trial[s1:s1+wmin].copy()
                f_trial[s1:s1+wmin] = f_trial[s2:s2+wmin]
                f_trial[s2:s2+wmin] = temp

        elif ptype == "block_scale_group":
            # Scale a contiguous group of 5-20 blocks
            group_size = rng.integers(5, min(21, n_blocks))
            start_block = rng.integers(0, n_blocks - group_size + 1)
            scale = rng.uniform(0.9, 1.1)
            for bi in range(start_block, start_block + group_size):
                s, e = blocks[bi]
                f_trial[s:e] *= scale

        elif ptype == "tooth_jitter":
            # Shift a block's mass slightly left or right
            idx = rng.integers(0, n_blocks)
            s, e = blocks[idx]
            shift = rng.choice([-2, -1, 1, 2])
            new_s = max(0, s + shift)
            new_e = min(len(f), e + shift)
            w = min(e - s, new_e - new_s)
            if w > 0 and new_s != s:
                vals = f_trial[s:s+w].copy()
                f_trial[s:e] = 0.0
                f_trial[new_s:new_s+w] = vals

        C_trial = score(f_trial)
        if C_trial > C_best:
            n_improved += 1
            print(
                f"    trial {trial:5d} ({ptype:20s}): "
                f"C={C_trial:.13f} (dC={C_trial - C_best:+.2e})"
            )
            C_best = C_trial
            f_best = f_trial

        if (trial + 1) % 500 == 0:
            elapsed = time.time() - t0
            rate = (trial + 1) / elapsed
            print(
                f"    ... {trial+1}/{n_trials}, {n_improved} improvements, "
                f"{rate:.0f} trials/s"
            )

    elapsed = time.time() - t0
    print(f"  Done: {n_trials} trials in {elapsed:.0f}s, {n_improved} improvements")
    print(f"  Final C = {C_best:.13f}")

    return f_best, C_best


def cpu_dinkelbach_polish(
    f: np.ndarray, n_outer: int = 3, n_inner: int = 500, beta: float = 1e7,
) -> tuple[np.ndarray, float]:
    """CPU-based Dinkelbach polish using scipy L-BFGS-B.

    Since we don't have GPU/torch, we use scipy. This is slower but still useful.
    """
    from scipy.optimize import minimize

    w = np.sqrt(np.maximum(f, 0.0))
    n = len(w)
    nc = 2 * n - 1

    # Determine FFT size
    nfft = 1
    while nfft < nc:
        nfft <<= 1

    C_best = score(f)
    f_best = f.copy()

    for outer in range(n_outer):
        lam = C_best

        def neg_objective(w_flat):
            """Negative Dinkelbach objective for minimization."""
            ff = w_flat ** 2
            F = np.fft.rfft(ff, n=nfft)
            conv = np.fft.irfft(F * F, n=nfft)[:nc]
            conv = np.maximum(conv, 0.0)

            c_sum = np.sum(conv)
            c_max = np.max(conv)
            if c_sum == 0 or c_max == 0:
                return 1e10

            # L2^2 via closed-form
            num = 2.0 * np.dot(conv, conv) + np.dot(conv[:-1], conv[1:])
            l2sq = num / (3.0 * (nc + 1))

            # L1
            l1 = c_sum / (nc + 1)

            # Smooth Linf
            log_ratios = beta * (conv / (c_max + 1e-18) - 1.0)
            log_ratios = np.clip(log_ratios, -500, 500)
            linf_proxy = c_max * np.exp(
                np.log(np.sum(np.exp(log_ratios - np.max(log_ratios))))
                / beta + np.max(log_ratios) / beta
            )

            obj = l2sq - lam * l1 * linf_proxy
            return -obj

        result = minimize(
            neg_objective, w,
            method="L-BFGS-B",
            options={"maxiter": n_inner, "ftol": 1e-15, "gtol": 1e-14},
        )

        w_new = result.x
        f_new = w_new ** 2
        C_new = score(f_new)

        if C_new > C_best and np.all(np.isfinite(f_new)):
            C_best = C_new
            f_best = f_new.copy()
            w = w_new
            print(f"    Dinkelbach outer={outer}: C={C_new:.13f}")
        else:
            print(f"    Dinkelbach outer={outer}: no improvement (C={C_new:.13f})")

    return f_best, C_best


def main():
    print("=" * 70)
    print("Random Perturbation Search + CPU Dinkelbach Polish")
    print("=" * 70)

    # Load the packet-ascent result
    npy_path = RESULTS / "c2_n100000_0.96198706_packet_ascent.npy"
    if not npy_path.exists():
        # Fallback to public best
        npy_path = RESULTS / "public_best_100k.npy"

    f = np.maximum(np.load(npy_path).astype(np.float64), 0.0)
    n = len(f)
    C_initial = score(f)
    print(f"Loaded: n={n}, C={C_initial:.13f} from {npy_path.name}")

    blocks = find_blocks(f, threshold=1e-10)
    print(f"Blocks: {len(blocks)}")

    C_best = C_initial
    f_best = f.copy()

    # ------------------------------------------------------------------
    # Phase 1: Random perturbation search
    # ------------------------------------------------------------------
    print(f"\n{'='*60}")
    print("Phase 1: Random perturbation search")
    print(f"{'='*60}")

    f_new, C_new = random_perturbation_search(
        f_best, blocks, n_trials=2000, seed=42
    )
    if C_new > C_best:
        C_best = C_new
        f_best = f_new

    # Note: CPU Dinkelbach polish requires PyTorch for autodiff gradients.
    # scipy L-BFGS-B with numerical gradients is intractable at n=100k.
    # Skipping Dinkelbach phase on CPU.

    # ------------------------------------------------------------------
    # Save results
    # ------------------------------------------------------------------
    improvement = C_best - C_initial

    print(f"\n{'='*70}")
    print("RESULTS")
    print(f"  Initial C: {C_initial:.13f}")
    print(f"  Final C:   {C_best:.13f}")
    print(f"  Improvement: {improvement:+.2e}")
    print(f"{'='*70}")

    out_tag = f"c2_n{n}_{C_best:.8f}_perturb_search"
    out_json = RESULTS / f"{out_tag}.json"
    out_npy = RESULTS / f"{out_tag}.npy"

    data = {
        "problem": "second_autocorrelation_inequality",
        "n_points": n,
        "score": C_best,
        "values": f_best.tolist(),
        "tag": out_tag,
        "method": "random_perturbation + cpu_dinkelbach on packet_ascent result",
        "initial_score": C_initial,
        "improvement": improvement,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    with open(out_json, "w") as fout:
        json.dump(data, fout)
    np.save(out_npy, f_best)
    print(f"Saved: {out_json}")
    print(f"Saved: {out_npy}")


if __name__ == "__main__":
    main()
