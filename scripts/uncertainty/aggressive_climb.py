"""Aggressive k-climbing pipeline: insert root + CMA-ES at each level.

Strategy: Start from the best optimized solution at base_k, then for each k:
1. Insert a root at the best position (quick scan)
2. CMA-ES optimize with moderate budget
3. Use optimized result as base for k+1

This should push the score monotonically lower as k increases.

Usage:
  uv run python -u scripts/uncertainty/aggressive_climb.py --start-k 23 --end-k 50 --fevals 1500
"""
import argparse
import json
import glob
import sys
import time
from pathlib import Path

sys.path.insert(0, "src")

import numpy as np
import cma

from einstein.uncertainty.poly_eval import poly_evaluate

RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def load_best_k(k):
    best_score = float("inf")
    best_roots = None
    for p in RESULTS_DIR.glob(f"up_k{k}_*.json"):
        with open(p) as f:
            d = json.load(f)
        if d.get("verified") and d["score"] < best_score:
            best_score = d["score"]
            best_roots = d["laguerre_double_roots"]
    if best_roots is None:
        return None, float("inf")
    return [float(r) for r in best_roots], best_score


def insert_best_root(base_roots, dps=80):
    """Find the best position to insert one additional root."""
    positions = np.concatenate([
        np.linspace(0.5, 15, 30),
        np.linspace(16, 80, 80),
        np.linspace(85, 280, 50),
    ])

    best_score = float("inf")
    best_cand = None

    for pos in positions:
        cand = sorted(base_roots + [float(pos)])
        if any(cand[i + 1] - cand[i] < 0.2 for i in range(len(cand) - 1)):
            continue
        if cand[0] <= 0 or cand[-1] > 300:
            continue
        s = poly_evaluate(cand, dps=dps)
        if s < best_score:
            best_score = s
            best_cand = cand

    return best_cand, best_score


def roots_to_gaps(roots):
    roots = sorted(roots)
    return [roots[0]] + [roots[i] - roots[i - 1] for i in range(1, len(roots))]


def gaps_to_roots(gaps):
    return list(np.cumsum(gaps))


def cma_optimize(roots, sigma, fevals, seed, dps=80):
    """Run CMA-ES optimization on root positions."""
    gaps = roots_to_gaps(roots)
    best_score = [float("inf")]
    eval_count = [0]

    def obj(gaps):
        eval_count[0] += 1
        gaps = np.asarray(gaps, dtype=float)
        repaired = np.maximum(gaps, 0.05)
        roots = list(np.cumsum(repaired))
        if roots[-1] > 300 or roots[0] <= 0:
            return 100.0
        s = poly_evaluate(roots, dps=dps)
        if not np.isfinite(s):
            return 100.0
        penalty = float(np.sum(np.maximum(0.05 - gaps, 0)))
        result = s + 10.0 * penalty
        if result < best_score[0]:
            best_score[0] = result
            log(f"    CMA eval #{eval_count[0]}: {result:.14f}")
        return result

    try:
        es = cma.CMAEvolutionStrategy(
            gaps, sigma,
            {"maxfevals": fevals, "verbose": -9, "tolx": 1e-14, "seed": seed, "popsize": 14},
        )
        es.optimize(obj)
    except Exception as e:
        log(f"  CMA error: {e}")
        return roots, float("inf")

    best_gaps = list(es.result.xbest) if es.result.xbest is not None else gaps
    final_roots = gaps_to_roots(best_gaps)
    final_score = float(es.result.fbest)

    return final_roots, final_score


def save_result(roots, score, tag):
    result = {
        "problem": "uncertainty-principle",
        "k": len(roots),
        "score": score,
        "laguerre_double_roots": list(roots),
        "tag": tag,
        "verified": True,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    fname = RESULTS_DIR / f"up_k{len(roots)}_{score:.10f}.json"
    with open(fname, "w") as f:
        json.dump(result, f, indent=2)
    log(f"  SAVED: {fname.name}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-k", type=int, default=23)
    parser.add_argument("--end-k", type=int, default=50)
    parser.add_argument("--fevals", type=int, default=1500, help="CMA-ES fevals per k level")
    parser.add_argument("--sigma", type=float, default=0.3)
    parser.add_argument("--dps", type=int, default=80)
    parser.add_argument("--seed", type=int, default=2026)
    args = parser.parse_args()

    # Load best available at start_k
    current_roots, current_score = load_best_k(args.start_k)
    if current_roots is None:
        log(f"No solution found for k={args.start_k}")
        return

    log("=" * 70)
    log(f"AGGRESSIVE K-CLIMBING: k={args.start_k}→{args.end_k}")
    log(f"Base: k={args.start_k}, score={current_score:.14f}")
    log(f"CMA fevals/level: {args.fevals}, sigma: {args.sigma}")
    log("=" * 70)

    rng = np.random.default_rng(args.seed)
    global_best_score = current_score
    global_best_roots = list(current_roots)

    for target_k in range(args.start_k + 1, args.end_k + 1):
        t0 = time.time()
        log(f"\n--- k={target_k} ---")

        # Step 1: Insert a root
        insert_roots, insert_score = insert_best_root(current_roots, dps=args.dps)
        if insert_roots is None:
            log(f"  No valid insertion found. Stopping.")
            break
        log(f"  Insert: {insert_score:.14f}")

        # Step 2: CMA-ES optimize (use smaller sigma since base is already optimized)
        seed = int(rng.integers(1, 2**31))
        opt_sigma = min(args.sigma, 0.15)  # smaller sigma for incremental optimization
        opt_roots, opt_score = cma_optimize(
            insert_roots, opt_sigma, args.fevals, seed, args.dps
        )

        # Validate
        if not all(0 < r <= 300 for r in opt_roots):
            log(f"  CMA result invalid. Using insertion only.")
            opt_roots = insert_roots
            opt_score = insert_score

        # Verify with higher precision
        h = poly_evaluate(opt_roots, dps=120)
        if not np.isfinite(h):
            log(f"  Verification failed. Using insertion.")
            h = insert_score
            opt_roots = insert_roots

        log(f"  CMA optimized: {h:.14f} (took {time.time()-t0:.0f}s)")

        # Save and update
        save_result(opt_roots, h, f"aggressive_climb_k{target_k}")
        current_roots = [float(r) for r in opt_roots]
        current_score = h

        if h < global_best_score:
            global_best_score = h
            global_best_roots = list(current_roots)
            log(f"  *** GLOBAL BEST: {global_best_score:.14f} ***")

        # Also check if a better solution exists on disk
        disk_roots, disk_score = load_best_k(target_k)
        if disk_roots is not None and disk_score < current_score:
            current_roots = disk_roots
            current_score = disk_score
            log(f"  Loaded better from disk: {current_score:.14f}")

    log("\n" + "=" * 70)
    log(f"FINAL GLOBAL BEST: k={len(global_best_roots)}, score={global_best_score:.14f}")
    log("=" * 70)


if __name__ == "__main__":
    main()
