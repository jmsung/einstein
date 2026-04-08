"""k=15 climb optimizer (parallel multi-start, single-base).

Loads the best verified k=14 from `results/` (gitignored), inserts a 15th root
at many positions, runs short Nelder-Mead in gap space + hillclimb, and
verifies any improvements with the hybrid evaluator.

Usage:
    uv run python scripts/uncertainty/k15_climb.py [--workers N] [--nm-iter N]
"""
import argparse
import json
import os
import sys
import time
from pathlib import Path

os.environ.setdefault("NUMBA_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")

sys.path.insert(0, "src")

import multiprocessing as mp

import numpy as np
from scipy.optimize import minimize

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
    """Load best verified k-root solution from results/ (gitignored)."""
    best_score = float("inf")
    best_roots = None
    for p in RESULTS_DIR.glob(f"up_k{k}_*.json"):
        with open(p) as f:
            d = json.load(f)
        if d.get("verified") and d["score"] < best_score:
            best_score = d["score"]
            best_roots = d["laguerre_double_roots"]
    if best_roots is None:
        raise FileNotFoundError(
            f"No verified k={k} result in results/. Run earlier optimizer first."
        )
    return list(best_roots), best_score


def log(msg):
    ts = time.strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


def roots_to_gaps(roots):
    roots = sorted(roots)
    return [roots[0]] + [roots[i] - roots[i - 1] for i in range(1, len(roots))]


def gaps_to_roots(gaps):
    return list(np.cumsum(gaps))


def obj_gaps(gaps, dps=30):
    if any(g < 0.05 for g in gaps):
        return 1e6
    roots = gaps_to_roots(gaps)
    if roots[-1] > 300 or roots[0] <= 0:
        return 1e6
    s = fast_evaluate(roots, dps=dps)
    return s if np.isfinite(s) else 1e6


def generate_candidates(base_roots):
    """Insert one extra root at many positions to seed multi-start search."""
    candidates = []
    base_sorted = sorted(base_roots)
    positions = (
        list(range(2, 30, 1))
        + list(range(30, 80, 2))
        + list(range(80, 200, 3))
        + list(range(200, 290, 5))
    )
    for pos in positions:
        cand = sorted(base_sorted + [float(pos)])
        if (
            all(cand[i + 1] - cand[i] >= 0.5 for i in range(len(cand) - 1))
            and cand[0] > 0
            and cand[-1] <= 300
        ):
            candidates.append((cand, f"insert_{pos}"))
    return candidates


def optimize_one(args):
    roots, tag, max_nm_iter, max_hc_rounds = args
    k = len(roots)

    gaps = roots_to_gaps(roots)
    try:
        res = minimize(
            obj_gaps,
            gaps,
            method="Nelder-Mead",
            options={
                "maxiter": max_nm_iter,
                "maxfev": max_nm_iter * 2,
                "xatol": 1e-12,
                "fatol": 1e-14,
                "adaptive": True,
            },
        )
    except Exception:
        return float("inf"), roots, tag

    if res.fun < 1e5 and all(g > 0 for g in res.x):
        roots = gaps_to_roots(list(res.x))
    nm_score = float(res.fun)

    if not np.isfinite(nm_score) or nm_score >= 1.0:
        return nm_score, roots, tag

    best = fast_evaluate(roots)
    if not np.isfinite(best):
        return nm_score, roots, tag

    step = 0.05
    rounds = 0
    while step > 1e-12 and rounds < max_hc_rounds:
        improved = False
        for i in range(k):
            for d in (1, -1):
                for sm in (1.0, 0.5, 0.1, 2.0, 5.0):
                    s = step * sm
                    trial = list(roots)
                    trial[i] += d * s
                    if trial[i] <= 0 or trial[i] > 300:
                        continue
                    if i > 0 and trial[i] <= trial[i - 1] + 0.05:
                        continue
                    if i < k - 1 and trial[i] >= trial[i + 1] - 0.05:
                        continue
                    score = fast_evaluate(trial)
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

    return float(best), list(roots), tag


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
    mb_fname = MB_SOLUTIONS_DIR / f"solution-k{len(roots)}-{score:.10f}.json"
    with open(mb_fname, "w") as f:
        json.dump(result, f, indent=2)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--nm-iter", type=int, default=2000)
    parser.add_argument("--hc-rounds", type=int, default=80)
    parser.add_argument("--top", type=int, default=40)
    parser.add_argument("--base-k", type=int, default=14)
    args = parser.parse_args()

    base_roots, base_score = _load_best_k(args.base_k)
    log("=" * 70)
    log(f"K={args.base_k + 1} CLIMB OPTIMIZER")
    log(f"Base k={args.base_k}, score loaded from results/")
    log(f"Workers: {args.workers}")
    log("=" * 70)

    candidates = generate_candidates(base_roots)
    log(f"Generated {len(candidates)} candidates")

    work = []
    for roots, tag in candidates:
        s = fast_evaluate(roots)
        if np.isfinite(s):
            work.append((roots, tag, args.nm_iter, args.hc_rounds))
    log(f"Finite candidates: {len(work)}")

    log(f"\nRunning {len(work)} optimizations on {args.workers} workers...")
    t_pool = time.time()
    with mp.Pool(args.workers) as pool:
        results = []
        for i, res in enumerate(pool.imap_unordered(optimize_one, work)):
            results.append(res)
            score, _, tag = res
            tag_short = tag[:30]
            if (i + 1) % 10 == 0:
                log(f"  [{i + 1}/{len(work)}] last: {score:.6f} ({tag_short})")
    log(f"Pool finished in {time.time() - t_pool:.0f}s")

    results.sort(key=lambda x: x[0])

    best_score = base_score
    best_roots = list(base_roots)
    new_bests = 0

    for s, roots, tag in results[: args.top]:
        if s >= best_score - 1e-9:
            continue
        verified = verify_score(roots, s, tag)
        if verified is None:
            continue
        if verified < best_score - 1e-12:
            save_result(roots, verified, s, f"k{len(roots)}_{tag}")
            best_score = verified
            best_roots = list(roots)
            new_bests += 1

    log("\n" + "=" * 70)
    log(f"FINAL: k={len(best_roots)}, new verified bests: {new_bests}")


if __name__ == "__main__":
    main()
