"""Warm-start optimizer for Erdős Minimum Overlap (Problem 1).

Loads a SOTA solution and polishes with mass transport (multi-point) +
dyadic mass transport. Adam refinement on float64 CPU is included as
an optional first stage.

Usage:
    uv run python scripts/erdos/optimize_warmstart.py \
        --warm-start results/problem-1-erdos-overlap/sota_together_ai_n600.json
"""

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, "src")
from einstein.erdos.evaluator import evaluate as exact_evaluate
from einstein.erdos.fast import fast_evaluate

RESULTS_DIR = Path("results/problem-1-erdos-overlap")
RESULTS_DIR.mkdir(parents=True, exist_ok=True)


def mass_transport(h: np.ndarray, n_iters: int, n_points_choices=(2, 2, 2, 3, 4),
                   delta_scale: float = 1e-7, seed: int = 12345) -> tuple[np.ndarray, float]:
    """Multi-point mass transport: random small zero-sum perturbations to k indices."""
    rng = np.random.default_rng(seed)
    h = np.clip(h.copy(), 0, 1)
    n = len(h)
    best = fast_evaluate(h)
    improved = 0
    t0 = time.time()
    print(f"  Mass transport: n={n}, iters={n_iters}, start C={best:.13f}")

    for trial in range(n_iters):
        n_pts = rng.choice(n_points_choices)
        idx = rng.choice(n, size=n_pts, replace=False)
        delta = rng.standard_normal(n_pts) * delta_scale
        delta -= delta.mean()  # zero-sum

        old = h[idx].copy()
        new = old + delta
        if np.any(new < 0) or np.any(new > 1):
            continue

        h[idx] = new
        score = fast_evaluate(h)
        if score < best:
            best = score
            improved += 1
        else:
            h[idx] = old

        if (trial + 1) % 500_000 == 0:
            print(f"    iter {trial+1}: C={best:.13f}, improved={improved}, "
                  f"time={time.time()-t0:.0f}s")

    return h, best


def dyadic_mass_transport(h: np.ndarray, n_iters: int, seed: int = 7) -> tuple[np.ndarray, float]:
    """Pairwise mass transport at dyadic offsets."""
    rng = np.random.default_rng(seed)
    h = np.clip(h.copy(), 0, 1)
    n = len(h)
    best = fast_evaluate(h)
    improved = 0
    print(f"  Dyadic MT: n={n}, iters={n_iters}, start C={best:.13f}")

    log2n = int(np.log2(n))
    for trial in range(n_iters):
        i = rng.integers(n)
        k = 2 ** rng.integers(0, log2n)
        j = (i + k) % n
        delta = rng.uniform(1e-12, 1e-7)
        old_i, old_j = h[i], h[j]
        new_i = old_i - delta
        new_j = old_j + delta
        if new_i < 0 or new_j > 1:
            continue
        h[i], h[j] = new_i, new_j
        score = fast_evaluate(h)
        if score < best:
            best = score
            improved += 1
        else:
            h[i], h[j] = old_i, old_j

        if (trial + 1) % 100_000 == 0:
            print(f"    iter {trial+1}: C={best:.13f}, improved={improved}")

    return h, best


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--warm-start", type=str, required=True)
    parser.add_argument("--mt-iters", type=int, default=2_000_000)
    parser.add_argument("--dmt-iters", type=int, default=500_000)
    args = parser.parse_args()

    print("=" * 60)
    print("Erdős Minimum Overlap — Warm-Start Optimizer")
    print("=" * 60)

    with open(args.warm_start) as f:
        data = json.load(f)
    h = np.array(data["values"], dtype=np.float64)
    source = data.get("source", "unknown")
    start = fast_evaluate(h)
    print(f"Source: {source}, n={len(h)}, start C={start:.13f}")

    t0 = time.time()

    print("\n--- Stage 1: Multi-point mass transport ---")
    h, score_mt = mass_transport(h, n_iters=args.mt_iters)

    print("\n--- Stage 2: Dyadic mass transport ---")
    h, score_dmt = dyadic_mass_transport(h, n_iters=args.dmt_iters)

    # Final triple-verification
    print("\n--- Final Verification ---")
    exact = exact_evaluate({"values": h.tolist()})
    fast = fast_evaluate(h)
    print(f"Fast:  {fast:.13f}")
    print(f"Exact: {exact:.13f}")
    print(f"Match: {abs(fast - exact) < 1e-10}")

    result = {
        "problem": "erdos-minimum-overlap",
        "n_points": len(h),
        "score": float(exact),
        "values": h.tolist(),
        "source": f"warm-start from {source}",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    fname = RESULTS_DIR / "erdos_n600_best.json"
    with open(fname, "w") as f:
        json.dump(result, f)
    print(f"\nSaved: {fname}")

    elapsed = time.time() - t0
    print(f"\n{'=' * 60}")
    print(f"DONE: C={exact:.13f} (start: {start:.13f})")
    print(f"Improvement: {start - exact:.2e}")
    print(f"Time: {elapsed:.0f}s")
    print(f"{'=' * 60}")

    print("\nLeaderboard comparison:")
    print(f"  #1 Together-AI:   0.3808703105862")
    print(f"  #2 GaussAgent:    0.3808721886444")
    print(f"  #3 TTT-Discover:  0.3808753232177")
    print(f"  Our result:       {exact:.13f}")
    if exact < 0.3808753232177:
        print(f"  -> Beats #3!")
    if exact < 0.3808703105862:
        print(f"  -> Beats #1!")


if __name__ == "__main__":
    main()
