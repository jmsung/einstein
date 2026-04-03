"""MTS-based optimizer for Problem 12 — Flat Polynomials.

Uses Memetic Tabu Search at N=4096 (fast) with diverse warm-starts,
then verifies best candidates at N=1M.

Usage:
    uv run python scripts/optimize_flat_poly.py              # full MTS campaign (~30 min)
    uv run python scripts/optimize_flat_poly.py --quick      # quick test (~3 min)
    uv run python scripts/optimize_flat_poly.py --hours 4    # extended campaign
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np

from einstein.flat_poly import (
    compute_score,
    fast_score,
    kloosterman_sign,
    memetic_tabu_search,
    period3_base,
    rudin_shapiro,
    tabu_search,
    turyn,
)

RESULTS_DIR = Path("results/problem-12-flat-polynomials")
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Known solutions from the arena leaderboard (descending order)
# ---------------------------------------------------------------------------
SOTA_DESC = [
    -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1,
    1, 1, -1, 1, 1, 1, 1, 1, -1, -1, 1, 1, 1, -1, 1, 1, -1, 1, -1, 1,
    -1, -1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 1, -1,
    1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1,
]

THIRD_DESC = [
    1, 1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, -1,
    1, -1, 1, 1, 1, 1, -1, 1, 1, 1, -1, 1, 1, -1, -1, -1, -1, -1, -1,
    1, -1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, -1, 1, -1,
    -1, 1, -1, -1, 1, 1, -1, 1, 1, 1, -1, 1, -1, 1, -1,
]

SOTA_ASC = SOTA_DESC[::-1]
THIRD_ASC = THIRD_DESC[::-1]


def log(msg: str) -> None:
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def save_result(coeffs_asc: list[int], score_fast: float, tag: str) -> float:
    """Save solution to results directory. Returns exact score."""
    desc = coeffs_asc[::-1]
    exact_score = compute_score(desc)
    result = {
        "tag": tag,
        "score_fast": score_fast,
        "score_exact_1m": exact_score,
        "coefficients_descending": desc,
        "coefficients_ascending": coeffs_asc,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    fname = RESULTS_DIR / f"best_{tag}_{exact_score:.8f}.json"
    with open(fname, "w") as f:
        json.dump(result, f, indent=2)
    log(f"Saved: {fname} (exact={exact_score:.10f})")
    return exact_score


def collect_warm_starts() -> list[list[int]]:
    """Gather diverse warm-start solutions."""
    starts = [
        SOTA_ASC,
        THIRD_ASC,
        turyn(shift=22),
        turyn(shift=21),
        turyn(shift=16),
        rudin_shapiro(),
        kloosterman_sign(),
        period3_base(),
    ]
    # Add some random seeds
    rng = np.random.default_rng(42)
    for _ in range(12):
        starts.append(rng.choice([-1, 1], size=70).tolist())
    return starts


def main() -> None:
    parser = argparse.ArgumentParser(description="MTS optimizer for flat polynomials")
    parser.add_argument("--quick", action="store_true", help="Quick test (~3 min)")
    parser.add_argument("--hours", type=float, default=0.5, help="Time budget in hours")
    args = parser.parse_args()

    if args.quick:
        pop_size, n_rounds, tabu_iters = 30, 30, 500
    else:
        # Scale rounds to fill time budget
        # Each round: ~500 tabu iters × 0.08ms = 40ms, plus crossover overhead
        # ~20 rounds/sec → hours * 3600 * 20 rounds
        target_rounds = int(args.hours * 3600 * 10)  # conservative estimate
        pop_size, n_rounds, tabu_iters = 50, target_rounds, 1000

    log("=" * 60)
    log("Flat Polynomials MTS Optimizer — Problem 12")
    log(f"Mode: {'quick' if args.quick else 'full'}")
    log(f"Pop: {pop_size}, Rounds: {n_rounds:,}, Tabu iters/round: {tabu_iters}")
    log(f"Time budget: {args.hours:.1f} hours")

    sota_exact = compute_score(SOTA_DESC)
    log(f"SOTA (arena): 1.2809320527987977")
    log(f"SOTA (ours):  {sota_exact:.16f}")
    log("=" * 60)

    warm_starts = collect_warm_starts()
    log(f"Warm starts: {len(warm_starts)} diverse solutions")

    # Phase 1: MTS campaign
    log("Phase 1: Memetic Tabu Search (N=4096)")
    t0 = time.time()

    best_coeffs, best_score = memetic_tabu_search(
        pop_size=pop_size,
        n_rounds=n_rounds,
        max_iter_per_round=tabu_iters,
        n_eval_points=4096,
        warm_start=warm_starts,
        seed=42,
    )

    elapsed = time.time() - t0
    log(f"MTS completed in {elapsed:.1f}s ({elapsed/60:.1f} min)")
    log(f"MTS best (N=4096): {best_score:.10f}")

    # Phase 2: Verify at N=100K
    log("Phase 2: Verify top candidate at N=100K")
    score_100k = fast_score(best_coeffs, n_points=100_000)
    log(f"Score at N=100K: {score_100k:.10f}")

    # Phase 3: Refine at N=100K with tabu search
    log("Phase 3: Refine at N=100K")
    refined, refined_score = tabu_search(
        best_coeffs,
        max_iter=2000,
        n_eval_points=100_000,
        seed=99,
    )
    log(f"Refined (N=100K): {refined_score:.10f}")

    # Phase 4: Exact verification at N=1M
    log("=" * 60)
    exact = save_result(refined, refined_score, "mts_campaign")

    log("")
    log(f"GLOBAL BEST (exact): {exact:.10f}")
    log(f"ARENA SOTA:          1.2809320527987977")
    log(f"Gap to SOTA:         {exact - 1.2809320527987977:+.10f}")

    if exact < 1.2809320527987977 - 1e-5:
        log(">>> BEATS SOTA! Ready for submission (pending user approval).")
    elif exact < 1.3409252794557085 - 1e-5:
        log(f">>> Beats #3 (1.3409)! Rank ~#3. Gap to #1: {exact - 1.2809:.4f}")
    else:
        log(f">>> Score: {exact:.6f}. Gap to #3: {exact - 1.3409:.4f}")


if __name__ == "__main__":
    main()
