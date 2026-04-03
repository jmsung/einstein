"""Optimizer for the Second Autocorrelation Inequality (Problem 3).

Strategy: maximize C = ||f★f||₂² / (||f★f||₁ · ||f★f||∞)

Key insight: C→1 when autoconvolution is flat. Optimal solutions are sparse
with ~500 blocks whose non-uniform values create a flat autoconvolution plateau.

Approach:
  Phase A: Direct element-wise optimization at small n (2k-5k)
  Phase B: Scale up to medium n (20k-50k) and refine
  Phase C: Scale to large n (100k+) for final submission
"""

import sys

sys.path.insert(0, "src")

import json
import time
from pathlib import Path

import numpy as np
from scipy.signal import fftconvolve

from einstein.autocorrelation.fast import diagnose, fast_evaluate

RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)


def save_result(f, score, tag=""):
    """Save a result to disk."""
    result = {
        "problem": "second-autocorrelation-inequality",
        "n_points": len(f),
        "score": score,
        "values": f.tolist() if isinstance(f, np.ndarray) else f,
        "tag": tag,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    fname = RESULTS_DIR / f"c2_n{len(f)}_{score:.8f}_{tag}.json"
    with open(fname, "w") as fh:
        json.dump(result, fh)
    print(f"  Saved to {fname}")


# -------------------------------------------------------------------------
# Element-wise coordinate ascent (works at small-medium n)
# -------------------------------------------------------------------------
def elementwise_ascent(f, max_iters=200, verbose=True):
    """Optimize every element of f via coordinate ascent.

    At each iteration, for each element, try a set of modifications
    and accept the first improvement found.
    """
    f = f.copy().astype(np.float64)
    n = len(f)
    best_score = fast_evaluate(f)
    rng = np.random.default_rng(0)
    improved_total = 0

    if verbose:
        print(f"  Element-wise ascent: n={n}, initial C={best_score:.8f}")

    for iteration in range(max_iters):
        improved = False
        order = rng.permutation(n)

        for i in order:
            old_val = f[i]

            # Additive and multiplicative deltas
            deltas = []
            if old_val > 0:
                deltas.extend([
                    old_val * 1.5, old_val * 0.67, old_val * 2.0, old_val * 0.5,
                    old_val * 1.1, old_val * 0.9, old_val * 1.02, old_val * 0.98,
                    old_val + 0.1, max(0, old_val - 0.1),
                    old_val + 0.01, max(0, old_val - 0.01),
                    0.0,  # try removing this element
                ])
            else:
                # Try activating this zero element
                deltas.extend([0.01, 0.1, 0.5, 1.0])

            for new_val in deltas:
                f[i] = max(0, new_val)
                s = fast_evaluate(f)
                if s > best_score + 1e-14:
                    best_score = s
                    improved = True
                    improved_total += 1
                    break
                f[i] = old_val

        if not improved:
            break
        if verbose and (iteration + 1) % 5 == 0:
            nnz = np.count_nonzero(f)
            print(f"    iter {iteration+1}: C={best_score:.8f} (nnz={nnz}, {improved_total} impr)")

    if verbose:
        print(f"    Final: C={best_score:.8f} ({improved_total} impr, {iteration+1} iters)")
    return f, best_score


# -------------------------------------------------------------------------
# Multi-element perturbation search
# -------------------------------------------------------------------------
def perturb_search(f, n_trials=2000, sigma=0.1, verbose=True):
    """Random perturbation of multiple elements simultaneously."""
    f = f.copy()
    n = len(f)
    support = np.where(f > 0)[0]
    best_score = fast_evaluate(f)
    rng = np.random.default_rng(42)
    improved = 0

    if verbose:
        print(f"  Perturbation: {n_trials} trials, sigma={sigma}, support={len(support)}")

    for t in range(n_trials):
        trial = f.copy()

        # Mix of perturbation strategies
        strategy = rng.integers(4)

        if strategy == 0 and len(support) > 0:
            # Perturb existing support values
            n_perturb = rng.integers(1, min(20, len(support) + 1))
            idx = rng.choice(support, n_perturb, replace=False)
            for i in idx:
                trial[i] = max(0, trial[i] * (1 + rng.normal() * sigma))

        elif strategy == 1:
            # Swap: move mass from one support position to a new position
            if len(support) > 0:
                src = rng.choice(support)
                dst = rng.integers(n)
                trial[dst] = trial[src]
                trial[src] = 0

        elif strategy == 2:
            # Add new random positions
            n_new = rng.integers(1, 6)
            new_pos = rng.choice(n, n_new, replace=False)
            for p in new_pos:
                trial[p] = rng.exponential(0.5)

        elif strategy == 3 and len(support) > 0:
            # Remove some support elements
            n_remove = rng.integers(1, min(5, len(support) + 1))
            idx = rng.choice(support, n_remove, replace=False)
            trial[idx] = 0

        s = fast_evaluate(trial)
        if s > best_score + 1e-14:
            best_score = s
            f = trial
            support = np.where(f > 0)[0]
            improved += 1

    if verbose:
        print(f"    {improved}/{n_trials} impr, C={best_score:.8f}, nnz={len(support)}")
    return f, best_score


# -------------------------------------------------------------------------
# Upscaling
# -------------------------------------------------------------------------
def upscale(f, new_n):
    """Upscale: map each nonzero position to its proportional position in new_n."""
    old_n = len(f)
    if new_n == old_n:
        return f.copy()

    f_new = np.zeros(new_n)
    nonzero = np.where(f > 0)[0]

    for idx in nonzero:
        new_idx = int(round(idx * (new_n - 1) / (old_n - 1)))
        new_idx = min(new_idx, new_n - 1)
        f_new[new_idx] = f[idx]

    old_score = fast_evaluate(f)
    new_score = fast_evaluate(f_new)
    print(f"  Upscale: n={old_n}→{new_n}, C={old_score:.8f}→{new_score:.8f}")
    return f_new


# -------------------------------------------------------------------------
# Multi-start initialization
# -------------------------------------------------------------------------
def run_start(name, f0, n_ascent_iters=30, n_perturb=500):
    """Quick optimization from a starting point."""
    s0 = fast_evaluate(f0)
    print(f"\n  [{name}] init C={s0:.6f}, nnz={np.count_nonzero(f0)}")

    f, s = elementwise_ascent(f0, max_iters=n_ascent_iters, verbose=False)
    print(f"    After ascent: C={s:.8f}, nnz={np.count_nonzero(f)}")

    f, s = perturb_search(f, n_trials=n_perturb, sigma=0.2, verbose=False)
    print(f"    After perturb: C={s:.8f}, nnz={np.count_nonzero(f)}")

    f, s = elementwise_ascent(f, max_iters=n_ascent_iters, verbose=False)
    print(f"    Final: C={s:.8f}, nnz={np.count_nonzero(f)}")
    return f, s


def generate_starts(n):
    """Generate diverse starting functions at resolution n."""
    starts = {}
    x = np.linspace(-3, 3, n)

    starts["gaussian"] = np.exp(-x**2)
    starts["narrow_gauss"] = np.exp(-10 * x**2)
    starts["uniform"] = np.ones(n)
    starts["cosine"] = np.maximum(0, np.cos(np.pi * x / 6))

    # Sparse random
    rng = np.random.default_rng(42)
    f = np.zeros(n)
    f[rng.choice(n, size=n // 10, replace=False)] = rng.random(n // 10)
    starts["sparse_random"] = f

    # Multi-peak
    starts["multi_peak"] = np.exp(-2 * x**2) + 0.5 * np.exp(-2 * (x - 2)**2) + 0.5 * np.exp(-2 * (x + 2)**2)

    return starts


# -------------------------------------------------------------------------
# Main
# -------------------------------------------------------------------------
def main():
    print("=" * 60)
    print("Second Autocorrelation Inequality — Optimizer v3")
    print("Target: maximize C")
    print("=" * 60)

    # Phase A: Small n, multi-start → find best structure
    n_a = 2000
    print(f"\n=== Phase A: Multi-start at n={n_a} ===")
    starts = generate_starts(n_a)

    best_f = None
    best_score = 0
    best_name = ""

    for name, f0 in starts.items():
        f, s = run_start(name, f0)
        if s > best_score:
            best_score = s
            best_f = f
            best_name = name

    print(f"\n  >>> Best: {best_name} C={best_score:.8f}")
    save_result(best_f, best_score, f"phaseA_{best_name}")

    # Deep optimization on the winner
    print(f"\n=== Phase A deep: intensive optimization on {best_name} ===")
    for rnd in range(5):
        best_f, best_score = elementwise_ascent(best_f, max_iters=50)
        for sigma in [0.3, 0.1, 0.03]:
            best_f, best_score = perturb_search(best_f, n_trials=1000, sigma=sigma)
        print(f"  Round {rnd+1}: C={best_score:.8f}, nnz={np.count_nonzero(best_f)}")

    save_result(best_f, best_score, "phaseA_deep")

    # Phase B: Scale up
    for target_n in [5_000, 10_000, 20_000]:
        print(f"\n=== Phase B: Scale to n={target_n} ===")
        f_up = upscale(best_f, target_n)

        for rnd in range(3):
            f_up, score = elementwise_ascent(f_up, max_iters=30)
            for sigma in [0.2, 0.05]:
                f_up, score = perturb_search(f_up, n_trials=500, sigma=sigma)
            print(f"  Round {rnd+1}: C={score:.8f}, nnz={np.count_nonzero(f_up)}")

        best_f = f_up
        best_score = score
        save_result(best_f, best_score, f"phaseB_n{target_n}")

    # Phase C: Large scale
    for target_n in [50_000, 100_000]:
        print(f"\n=== Phase C: Scale to n={target_n} ===")
        f_up = upscale(best_f, target_n)

        # At large n, only optimize nonzero elements + nearby
        support = np.where(f_up > 0)[0]
        print(f"  Support: {len(support)} nonzero elements")

        for rnd in range(2):
            f_up, score = elementwise_ascent(f_up, max_iters=20)
            f_up, score = perturb_search(f_up, n_trials=300, sigma=0.1)
            print(f"  Round {rnd+1}: C={score:.8f}")

        best_f = f_up
        best_score = score
        save_result(best_f, best_score, f"phaseC_n{target_n}")

    # Final verification
    from einstein.autocorrelation import evaluate
    arena_score = evaluate({"values": best_f.tolist()})

    print("\n" + "=" * 60)
    print(f"FINAL RESULT")
    print(f"  Fast score:  C={best_score:.10f}")
    print(f"  Arena score: C={arena_score:.10f}")
    print(f"  n={len(best_f)}, nonzero={np.count_nonzero(best_f)}")
    d = diagnose(best_f)
    print(f"  Blocks: {d['n_blocks']}, mean width: {d['mean_block_width']:.1f}")
    print(f"  Flatness (0.1%): {d['flatness_0.1pct']}, (1%): {d['flatness_1pct']}")
    print(f"  Target: 0.962086")
    print(f"  {'BEATS SOTA!' if arena_score > 0.962086 else 'Below target'}")
    print("=" * 60)

    save_result(best_f, arena_score, "final")


if __name__ == "__main__":
    main()
