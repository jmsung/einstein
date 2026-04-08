"""Deep refine the top k=(base_k+1) candidates with CMA-ES + short hillclimb.

Loads the verified base-k best from results/, generates promising insertion
positions, and runs deep CMA-ES + a few hillclimb rounds on each in parallel.

Usage: uv run python scripts/uncertainty/k15_refine.py [--workers N]
"""
import argparse
import json
import os
import sys
import time
from pathlib import Path

os.environ.setdefault("NUMBA_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")

sys.path.insert(0, "src")

import multiprocessing as mp
import numpy as np

from einstein.uncertainty.fast import fast_evaluate
from einstein.uncertainty.hybrid import hybrid_evaluate

RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)
MB_SOLUTIONS_DIR = (
    Path.home()
    / "projects/workbench/memory-bank/einstein/docs/problem-18-uncertainty-principle/solutions"
)
MB_SOLUTIONS_DIR.mkdir(parents=True, exist_ok=True)


def _load_best_k(k):
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
    ts = time.strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


def roots_to_gaps(roots):
    roots = sorted(roots)
    return [roots[0]] + [roots[i] - roots[i - 1] for i in range(1, len(roots))]


def gaps_to_roots(gaps):
    return list(np.cumsum(gaps))


def make_obj():
    def obj(gaps):
        gaps = np.asarray(gaps, dtype=float)
        repaired = np.maximum(gaps, 0.05)
        roots = list(np.cumsum(repaired))
        if roots[-1] > 300 or roots[0] <= 0:
            return 100.0
        s = fast_evaluate(roots, dps=30)
        if not np.isfinite(s):
            return 100.0
        penalty = float(np.sum(np.maximum(0.05 - gaps, 0)))
        return s + 10.0 * penalty

    return obj


def cma_polish(gaps0, sigma, fevals, seed):
    import cma

    obj = make_obj()
    es = cma.CMAEvolutionStrategy(
        gaps0, sigma,
        {"maxfevals": fevals, "verbose": -9, "tolx": 1e-12, "seed": seed, "popsize": 14},
    )
    es.optimize(obj)
    best = es.result.xbest if es.result.xbest is not None else gaps0
    return float(es.result.fbest), list(best)


def hillclimb(roots, max_rounds=30):
    k = len(roots)
    best = fast_evaluate(roots, dps=30)
    if not np.isfinite(best):
        return roots, float("inf")
    step = 0.01
    rounds = 0
    while step > 1e-10 and rounds < max_rounds:
        improved = False
        for i in range(k):
            for d in (1, -1):
                for sm in (1.0, 0.3, 3.0):
                    s = step * sm
                    trial = list(roots)
                    trial[i] += d * s
                    if trial[i] <= 0 or trial[i] > 300:
                        continue
                    if i > 0 and trial[i] <= trial[i - 1] + 0.05:
                        continue
                    if i < k - 1 and trial[i] >= trial[i + 1] - 0.05:
                        continue
                    score = fast_evaluate(trial, dps=30)
                    if score < best - 1e-16:
                        best = score
                        roots = trial
                        improved = True
                        break
                if improved:
                    break
            if improved:
                break
        if not improved:
            step *= 0.3
        rounds += 1
    return roots, best


def make_starts(base_roots):
    promising_pos = [127, 107, 97, 142, 132, 87, 117, 152, 77, 92]
    starts = []
    for pos in promising_pos:
        cand = sorted(base_roots + [float(pos)])
        if all(cand[i + 1] - cand[i] >= 0.5 for i in range(len(cand) - 1)):
            starts.append((cand, f"pos{pos}"))
    return starts


def refine_one(args):
    roots, tag, fevals, sigma_init, seed = args
    gaps = roots_to_gaps(roots)
    score, best_gaps = cma_polish(gaps, sigma_init, fevals, seed)
    if score >= 1.0:
        return float("inf"), roots, tag
    roots_out = gaps_to_roots(best_gaps)
    if any(r <= 0 or r > 300 for r in roots_out):
        return score, roots_out, tag
    if any(roots_out[i + 1] - roots_out[i] < 0.05 for i in range(len(roots_out) - 1)):
        return score, roots_out, tag
    roots_out, hc_score = hillclimb(roots_out, max_rounds=20)
    return float(hc_score), list(roots_out), tag


def verify_score(roots, fast_score, tag):
    log(f"  [{tag}] verifying ...")
    try:
        h = hybrid_evaluate(roots)
    except Exception as e:
        log(f"    Hybrid FAILED: {e}")
        return None
    diff = abs(fast_score - h)
    log(f"    Hybrid match diff={diff:.2e}")
    if diff > 1e-4:
        log("    REJECTED — far sign change")
        return None
    return h


def save_result(roots, score, fast_score, tag):
    result = {
        "problem": "uncertainty-principle",
        "k": len(roots),
        "score": score,
        "score_fast": fast_score,
        "laguerre_double_roots": list(roots),
        "tag": tag,
        "verified": True,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    fname = RESULTS_DIR / f"up_k{len(roots)}_{score:.10f}.json"
    with open(fname, "w") as f:
        json.dump(result, f, indent=2)
    log(f"    SAVED: {fname.name}")
    mb_fname = MB_SOLUTIONS_DIR / f"solution-k{len(roots)}-{score:.10f}.json"
    with open(mb_fname, "w") as f:
        json.dump(result, f, indent=2)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--fevals", type=int, default=4000)
    parser.add_argument("--sigma", type=float, default=0.05)
    parser.add_argument("--base-k", type=int, default=14)
    args = parser.parse_args()

    base_roots, base_score = _load_best_k(args.base_k)
    log("=" * 70)
    log(f"K={args.base_k + 1} REFINEMENT (CMA + short HC)")
    log(f"Base k={args.base_k}, fevals/start: {args.fevals}, sigma: {args.sigma}")
    log("=" * 70)

    starts = make_starts(base_roots)
    log(f"Refining {len(starts)} promising starts")

    rng = np.random.default_rng(2026)
    work = [(s[0], s[1], args.fevals, args.sigma, int(rng.integers(1, 2**31))) for s in starts]

    t0 = time.time()
    results = []
    with mp.Pool(args.workers) as pool:
        for i, res in enumerate(pool.imap_unordered(refine_one, work)):
            results.append(res)
            score, _, tag = res
            log(f"  [{i + 1}/{len(work)}] {tag}: {score:.14f}")
    log(f"\nPool finished in {time.time() - t0:.0f}s")

    results.sort(key=lambda x: x[0])

    best_score = base_score
    best_roots = list(base_roots)
    new_bests = 0

    for s, roots, tag in results[:15]:
        if s >= base_score:
            continue
        h = verify_score(roots, s, tag)
        if h is None:
            continue
        if h < best_score - 1e-12:
            save_result(roots, h, s, f"k{len(roots)}_{tag}")
            best_score = h
            best_roots = list(roots)
            new_bests += 1

    log("\n" + "=" * 70)
    log(f"New verified bests: {new_bests}")


if __name__ == "__main__":
    main()
