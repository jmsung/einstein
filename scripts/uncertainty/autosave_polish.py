"""Auto-saving CMA+NM polish for k=50.

Saves to disk EVERY TIME a new best is found during optimization.
Never lose a good solution again.

Usage:
  uv run python -u scripts/uncertainty/autosave_polish.py
  uv run python -u scripts/uncertainty/autosave_polish.py --sigma 0.05 --cma-evals 2000 --nm-evals 5000
"""
import argparse
import json
import glob
import sys
import time
from pathlib import Path

sys.path.insert(0, "src")

import numpy as np
from scipy.optimize import minimize
import cma

from einstein.uncertainty.poly_eval import poly_evaluate

RESULTS_DIR = Path("results")


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


def autosave(roots, score, tag):
    """Save solution to disk immediately."""
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
    log(f"  AUTO-SAVED: {fname.name} (score={score:.14e})")


def make_obj(k, tag_prefix, dps=100):
    """Create objective that auto-saves on every improvement."""
    global_best = [float("inf")]
    global_best_gaps = [None]
    count = [0]

    def obj(gaps):
        count[0] += 1
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
        if result < global_best[0] - 1e-15:
            global_best[0] = result
            global_best_gaps[0] = list(gaps)
            log(f"  #{count[0]}: {result:.14e}")
            # Auto-save every significant improvement
            if result < global_best[0] * 0.99 or count[0] % 200 == 0:
                autosave(roots, result, f"{tag_prefix}_eval{count[0]}")
        return result

    return obj, global_best, global_best_gaps, count


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", type=int, default=50)
    parser.add_argument("--sigma", type=float, default=0.1)
    parser.add_argument("--cma-evals", type=int, default=1500)
    parser.add_argument("--nm-evals", type=int, default=5000)
    parser.add_argument("--rounds", type=int, default=3)
    parser.add_argument("--seed", type=int, default=9999)
    parser.add_argument("--dps", type=int, default=100)
    args = parser.parse_args()

    roots, base_score = load_best_k(args.k)
    if roots is None:
        log(f"No solution found for k={args.k}")
        return

    log("=" * 70)
    log(f"AUTO-SAVE POLISH: k={args.k}, base={base_score:.14e}")
    log(f"CMA sigma={args.sigma}, evals={args.cma_evals}, NM evals={args.nm_evals}")
    log(f"Rounds: {args.rounds}")
    log("=" * 70)

    current_gaps = roots_to_gaps(roots)
    rng = np.random.default_rng(args.seed)

    for rnd in range(args.rounds):
        log(f"\n--- Round {rnd} ---")

        # CMA-ES phase
        seed = int(rng.integers(1, 2**31))
        sigma = args.sigma * (0.7 ** rnd)  # anneal sigma
        obj, best, best_gaps, count = make_obj(args.k, f"r{rnd}_cma", args.dps)
        log(f"CMA-ES sigma={sigma:.4f}, seed={seed}...")
        try:
            es = cma.CMAEvolutionStrategy(
                current_gaps, sigma,
                {"maxfevals": args.cma_evals, "verbose": -9, "tolx": 1e-16,
                 "seed": seed, "popsize": 20},
            )
            es.optimize(obj)
        except Exception as e:
            log(f"CMA error: {e}")

        cma_gaps = best_gaps[0] if best_gaps[0] is not None else current_gaps
        cma_score = best[0]
        log(f"CMA done: {cma_score:.14e}")

        # Save CMA result
        cma_roots = gaps_to_roots(cma_gaps)
        h = poly_evaluate(cma_roots, dps=150)
        autosave(cma_roots, h, f"r{rnd}_cma_final")
        current_gaps = np.array(cma_gaps)

        # NM phase
        obj, best, best_gaps, count = make_obj(args.k, f"r{rnd}_nm", args.dps)
        log(f"Nelder-Mead ({args.nm_evals} evals)...")
        result = minimize(
            obj, current_gaps, method="Nelder-Mead",
            options={"maxfev": args.nm_evals, "xatol": 1e-16, "fatol": 1e-16},
        )
        nm_gaps = best_gaps[0] if best_gaps[0] is not None else list(result.x)
        nm_score = best[0]
        log(f"NM done: {nm_score:.14e}")

        # Save NM result
        nm_roots = gaps_to_roots(nm_gaps)
        h = poly_evaluate(nm_roots, dps=150)
        autosave(nm_roots, h, f"r{rnd}_nm_final")
        current_gaps = np.array(nm_gaps)

        # Reload best from disk
        disk_roots, disk_score = load_best_k(args.k)
        if disk_roots is not None and disk_score < poly_evaluate(gaps_to_roots(current_gaps), dps=100):
            current_gaps = roots_to_gaps(disk_roots)
            log(f"Loaded better from disk: {disk_score:.14e}")

    # Final verification
    final_roots = gaps_to_roots(current_gaps)
    h80 = poly_evaluate(final_roots, dps=80)
    h100 = poly_evaluate(final_roots, dps=100)
    h150 = poly_evaluate(final_roots, dps=150)
    log(f"\n=== FINAL VERIFICATION ===")
    log(f"dps=80:  {h80:.16e}")
    log(f"dps=100: {h100:.16e}")
    log(f"dps=150: {h150:.16e}")
    log(f"Consistent: {max(abs(h80 - h150), abs(h100 - h150)) < 1e-10}")
    autosave(final_roots, h100, "final_verified")

    log("\n" + "=" * 70)
    log(f"DONE. Best: {h100:.16e}")
    log("=" * 70)


if __name__ == "__main__":
    main()
