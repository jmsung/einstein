"""Deep refine top k=(base_k+1) candidates in parallel.

Each worker takes a starting position and runs:
  Phase 1: CMA-ES sigma=0.05, ~4000 fevals
  Phase 2: CMA-ES sigma=0.005, ~2000 fevals
  Hybrid verify

Saves verified improvements to results/ and results/polish-trail/.
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
POLISH_TRAIL = Path("results/problem-18-uncertainty-principle/polish-trail")
POLISH_TRAIL.mkdir(parents=True, exist_ok=True)


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


def deep_refine(args):
    start_roots, tag, p1_fevals, p2_fevals, seed = args
    import cma

    obj = make_obj()
    gaps = roots_to_gaps(start_roots)

    try:
        es1 = cma.CMAEvolutionStrategy(
            gaps,
            0.05,
            {
                "maxfevals": p1_fevals,
                "verbose": -9,
                "tolx": 1e-12,
                "seed": seed,
                "popsize": 14,
            },
        )
        es1.optimize(obj)
    except Exception as e:
        return float("inf"), gaps, tag, str(e)
    p1_score = float(es1.result.fbest)
    p1_gaps = list(es1.result.xbest) if es1.result.xbest is not None else gaps
    if p1_score >= 1.0:
        return p1_score, p1_gaps, tag, "p1_failed"

    try:
        es2 = cma.CMAEvolutionStrategy(
            p1_gaps,
            0.005,
            {
                "maxfevals": p2_fevals,
                "verbose": -9,
                "tolx": 1e-14,
                "seed": seed + 7,
                "popsize": 14,
            },
        )
        es2.optimize(obj)
    except Exception:
        return p1_score, p1_gaps, tag, None
    p2_score = float(es2.result.fbest)
    p2_gaps = list(es2.result.xbest) if es2.result.xbest is not None else p1_gaps

    if p2_score < p1_score:
        return p2_score, p2_gaps, tag, None
    return p1_score, p1_gaps, tag, None


def make_starts(base_roots, positions=None):
    """Generate insertion-position trial starts. Default: uniform grid over [2, 290]."""
    if positions is None:
        positions = list(range(2, 290, 12))
    starts = []
    for pos in positions:
        cand = sorted(base_roots + [float(pos)])
        if all(cand[i + 1] - cand[i] >= 0.5 for i in range(len(cand) - 1)):
            starts.append((cand, f"pos{pos}"))
    return starts


def verify_score(roots, fast_score, tag):
    log(f"  [{tag}] verifying ...")
    t0 = time.time()
    try:
        h = hybrid_evaluate(roots)
    except Exception as e:
        log(f"    Hybrid FAILED: {e}")
        return None
    dt = time.time() - t0
    diff = abs(fast_score - h)
    log(f"    Hybrid match diff={diff:.2e} in {dt:.0f}s")
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
    trail = POLISH_TRAIL / f"solution-k{len(roots)}-{score:.10f}.json"
    with open(trail, "w") as f:
        json.dump(result, f, indent=2)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--p1-fevals", type=int, default=4000)
    parser.add_argument("--p2-fevals", type=int, default=2000)
    parser.add_argument("--base-k", type=int, default=14)
    args = parser.parse_args()

    base_roots, base_score = _load_best_k(args.base_k)
    log("=" * 70)
    log(f"K={args.base_k + 1} DEEP PARALLEL REFINEMENT")
    log(f"Base k={args.base_k}, P1 fevals: {args.p1_fevals}, P2 fevals: {args.p2_fevals}")
    log("=" * 70)

    starts = make_starts(base_roots)
    log(f"Refining {len(starts)} promising starts")

    rng = np.random.default_rng(2026)
    work = [(s[0], s[1], args.p1_fevals, args.p2_fevals, int(rng.integers(1, 2**31))) for s in starts]

    t0 = time.time()
    results = []
    with mp.Pool(args.workers) as pool:
        for i, res in enumerate(pool.imap_unordered(deep_refine, work)):
            score, gaps, tag, err = res
            log(f"  [{i + 1}/{len(work)}] {tag}: {score:.14f} {('('+err+')') if err else ''}")
            results.append((score, gaps, tag))
    log(f"\nPool finished in {time.time() - t0:.0f}s")

    results.sort(key=lambda x: x[0])

    best_score = base_score
    best_roots = list(base_roots)
    new_bests = 0

    for s, gaps, tag in results[:15]:
        if s >= base_score - 1e-9:
            continue
        roots = gaps_to_roots(gaps)
        if any(r <= 0 or r > 300 for r in roots):
            continue
        if any(roots[i + 1] - roots[i] < 0.05 for i in range(len(roots) - 1)):
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
