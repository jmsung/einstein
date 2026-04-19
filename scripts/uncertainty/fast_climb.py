"""Fast k-climbing with L-BFGS-B polishing at each level.

Much faster than CMA-ES for polishing: ~200 evals vs 800+ per k level.
Uses CMA-ES for the initial exploration (optional), then L-BFGS-B for refinement.

Usage:
  uv run python -u scripts/uncertainty/fast_climb.py --start-k 25 --end-k 60
"""
import argparse
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, "src")

import numpy as np
from scipy.optimize import minimize

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


def roots_to_gaps(roots):
    roots = sorted(roots)
    return np.array([roots[0]] + [roots[i] - roots[i - 1] for i in range(1, len(roots))])


def gaps_to_roots(gaps):
    return list(np.cumsum(gaps))


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


def lbfgsb_optimize(roots, maxfun=500, dps=80):
    """L-BFGS-B optimization on gap representation."""
    gaps = roots_to_gaps(roots)
    bounds = [(0.05, 250)] * len(gaps)
    best = [float("inf")]
    count = [0]

    def obj(gaps):
        count[0] += 1
        gaps = np.asarray(gaps)
        roots = list(np.cumsum(np.maximum(gaps, 0.05)))
        if roots[-1] > 300 or roots[0] <= 0:
            return 100.0
        s = poly_evaluate(roots, dps=dps)
        if not np.isfinite(s):
            return 100.0
        penalty = float(np.sum(np.maximum(0.05 - gaps, 0)))
        result = s + 10.0 * penalty
        if result < best[0]:
            best[0] = result
        return result

    result = minimize(obj, gaps, method="L-BFGS-B", bounds=bounds,
                      options={"maxfun": maxfun, "maxiter": 200, "ftol": 1e-15, "gtol": 1e-12})
    final_roots = gaps_to_roots(result.x)
    return final_roots, float(result.fun), count[0]


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
    parser.add_argument("--start-k", type=int, default=25)
    parser.add_argument("--end-k", type=int, default=60)
    parser.add_argument("--maxfun", type=int, default=500, help="L-BFGS-B max function evals")
    parser.add_argument("--dps", type=int, default=80)
    args = parser.parse_args()

    current_roots, current_score = load_best_k(args.start_k)
    if current_roots is None:
        log(f"No solution found for k={args.start_k}")
        return

    log("=" * 70)
    log(f"FAST K-CLIMBING (L-BFGS-B): k={args.start_k}→{args.end_k}")
    log(f"Base: k={args.start_k}, score={current_score:.14f}")
    log(f"L-BFGS-B maxfun: {args.maxfun}")
    log("=" * 70)

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

        # Step 2: L-BFGS-B polish
        opt_roots, opt_score, nfev = lbfgsb_optimize(
            insert_roots, maxfun=args.maxfun, dps=args.dps
        )
        log(f"  L-BFGS-B: {opt_score:.14f} ({nfev} evals, {time.time()-t0:.0f}s)")

        # Validate
        if not all(0 < r <= 300 for r in opt_roots):
            opt_roots = insert_roots
            opt_score = insert_score

        # Verify
        h = poly_evaluate(opt_roots, dps=120)
        if not np.isfinite(h):
            h = insert_score
            opt_roots = insert_roots

        # Save
        save_result(opt_roots, h, f"fast_climb_k{target_k}")
        current_roots = [float(r) for r in opt_roots]
        current_score = h

        if h < global_best_score:
            global_best_score = h
            global_best_roots = list(current_roots)
            log(f"  *** GLOBAL BEST: {global_best_score:.14f} ***")

        # Check disk for better
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
