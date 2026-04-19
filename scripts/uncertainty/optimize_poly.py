"""CMA-ES optimizer using the polynomial evaluator (correct for all k).

Optimizes root positions continuously from a grid-based starting solution.
Uses poly_evaluate (~0.3s/eval) which is correct for k>=15 unlike fast_evaluate.

Usage:
  uv run python -u scripts/uncertainty/optimize_poly.py --base-k 19
  uv run python -u scripts/uncertainty/optimize_poly.py --base-k 19 --sigma 0.5 --fevals 8000
  uv run python -u scripts/uncertainty/optimize_poly.py --base-k 19 --insert  # try k+1
"""
import argparse
import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, "src")

import numpy as np

from einstein.uncertainty.poly_eval import poly_evaluate

RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)


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
        raise FileNotFoundError(f"No verified k={k} result in results/")
    return list(best_roots), best_score


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def roots_to_gaps(roots):
    roots = sorted(roots)
    return [roots[0]] + [roots[i] - roots[i - 1] for i in range(1, len(roots))]


def gaps_to_roots(gaps):
    return list(np.cumsum(gaps))


def make_obj(dps=100):
    call_count = [0]
    best_seen = [float("inf")]

    def obj(gaps):
        call_count[0] += 1
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
        if result < best_seen[0]:
            prev = best_seen[0]
            best_seen[0] = result
            if call_count[0] % 10 == 0 or result < prev - 1e-6:
                log(f"  eval #{call_count[0]}: {result:.14f}")
        return result

    return obj, call_count, best_seen


def cma_optimize(start_roots, sigma, fevals, seed, tag, dps=100):
    import cma

    obj, call_count, best_seen = make_obj(dps)
    gaps = roots_to_gaps(start_roots)

    log(f"[{tag}] Starting CMA-ES: k={len(start_roots)}, sigma={sigma}, fevals={fevals}")

    try:
        es = cma.CMAEvolutionStrategy(
            gaps, sigma,
            {"maxfevals": fevals, "verbose": -9, "tolx": 1e-14, "seed": seed, "popsize": 14},
        )
        es.optimize(obj)
    except Exception as e:
        log(f"  CMA-ES error: {e}")
        return float("inf"), gaps, tag

    best_gaps = list(es.result.xbest) if es.result.xbest is not None else gaps
    best_score = float(es.result.fbest)
    log(f"  [{tag}] CMA-ES done: {best_score:.14f} ({call_count[0]} evals)")
    return best_score, best_gaps, tag


def verify_and_save(roots, fast_score, tag):
    """Verify with higher precision and save."""
    log(f"  Verifying [{tag}]...")
    h = poly_evaluate(roots, dps=150)
    diff = abs(fast_score - h)
    log(f"  Verified: {h:.16f} (diff={diff:.2e})")
    if diff > 1e-4:
        log("  REJECTED — verification mismatch")
        return None

    result = {
        "problem": "uncertainty-principle",
        "k": len(roots),
        "score": h,
        "score_fast": fast_score,
        "laguerre_double_roots": list(roots),
        "tag": tag,
        "verified": True,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    fname = RESULTS_DIR / f"up_k{len(roots)}_{h:.10f}.json"
    with open(fname, "w") as f:
        json.dump(result, f, indent=2)
    log(f"  SAVED: {fname.name}")
    return h


def make_insertion_starts(base_roots):
    """Generate k+1 candidates by inserting a root at various positions."""
    starts = []
    # Try positions across the range
    for pos in np.linspace(1, 280, 100):
        cand = sorted(base_roots + [float(pos)])
        if all(cand[i + 1] - cand[i] >= 0.5 for i in range(len(cand) - 1)):
            starts.append((cand, f"ins_{pos:.0f}"))
    return starts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-k", type=int, default=19)
    parser.add_argument("--sigma", type=float, default=0.3)
    parser.add_argument("--fevals", type=int, default=4000)
    parser.add_argument("--rounds", type=int, default=5, help="Number of CMA-ES rounds")
    parser.add_argument("--insert", action="store_true", help="Try k+1 insertion")
    parser.add_argument("--seed", type=int, default=2026)
    parser.add_argument("--dps", type=int, default=100)
    args = parser.parse_args()

    base_roots, base_score = load_best_k(args.base_k)
    log("=" * 70)
    log(f"POLY OPTIMIZER: k={args.base_k}, base_score={base_score:.14f}")
    log(f"sigma={args.sigma}, fevals={args.fevals}, rounds={args.rounds}")
    log("=" * 70)

    best_score = base_score
    best_roots = list(base_roots)

    if args.insert:
        # Try inserting a root to go to k+1
        starts = make_insertion_starts(base_roots)
        log(f"\nTrying {len(starts)} insertion positions for k={args.base_k + 1}")

        for cand_roots, tag in starts:
            score, gaps, _ = cma_optimize(
                cand_roots, args.sigma, args.fevals // 2, args.seed, tag, args.dps
            )
            if score < best_score - 1e-12:
                roots = gaps_to_roots(gaps)
                if all(0 < r <= 300 for r in roots):
                    h = verify_and_save(roots, score, f"k{len(roots)}_{tag}")
                    if h is not None and h < best_score:
                        best_score = h
                        best_roots = list(roots)
                        log(f"  NEW BEST: {best_score:.14f}")
    else:
        # Optimize current k
        rng = np.random.default_rng(args.seed)
        for rnd in range(args.rounds):
            seed = int(rng.integers(1, 2**31))
            sigma = args.sigma * (0.5 ** (rnd // 2))  # anneal sigma
            tag = f"r{rnd}_s{sigma:.4f}"

            score, gaps, _ = cma_optimize(
                best_roots, sigma, args.fevals, seed, tag, args.dps
            )
            roots = gaps_to_roots(gaps)
            if score < best_score - 1e-12 and all(0 < r <= 300 for r in roots):
                h = verify_and_save(roots, score, f"k{len(roots)}_{tag}")
                if h is not None and h < best_score:
                    best_score = h
                    best_roots = list(roots)
                    log(f"  NEW BEST: {best_score:.14f}")

            # Reload best from disk in case parallel runs saved something better
            try:
                disk_roots, disk_score = load_best_k(len(best_roots))
                if disk_score < best_score:
                    best_roots = disk_roots
                    best_score = disk_score
                    log(f"  Loaded better from disk: {best_score:.14f}")
            except FileNotFoundError:
                pass

    log("\n" + "=" * 70)
    log(f"FINAL BEST: k={len(best_roots)}, score={best_score:.14f}")
    log(f"Roots: {best_roots}")
    log("=" * 70)


if __name__ == "__main__":
    main()
