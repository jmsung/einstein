"""k=(base_k+1) parallel CMA-ES with smooth penalty.

Loads the best verified base-k from results/, generates many starts by
inserting one extra root at various positions (and a few cluster-structured
random starts), then runs short CMA-ES on each in parallel.

Verifies all improvements with the hybrid evaluator. Saves verified
improvements to both results/ and results/polish-trail/.

Usage: uv run python scripts/uncertainty/k15_parallel_cma.py [--workers N]
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

from einstein.uncertainty.fast import fast_evaluate
from einstein.uncertainty.hybrid import hybrid_evaluate

RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)
POLISH_TRAIL = Path("results/problem-18-uncertainty-principle/polish-trail")
POLISH_TRAIL.mkdir(parents=True, exist_ok=True)
SESSION_ID = time.strftime("%Y%m%d-%H%M%S") + "-" + Path(__file__).stem


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


def make_obj(dps=30):
    """Smooth-penalty objective so optimizers can recover from infeasible steps.

    NOTE: dps must be >= 30 for k>=15 — Laguerre matrix is too ill-conditioned
    otherwise (gives inf for valid configurations).
    """
    def obj(gaps):
        gaps = np.asarray(gaps, dtype=float)
        repaired = np.maximum(gaps, 0.05)
        roots = list(np.cumsum(repaired))
        if roots[-1] > 300:
            scale = 300.0 / roots[-1]
            roots = [r * scale for r in roots]
        if roots[0] <= 0:
            return 100.0
        s = fast_evaluate(roots, dps=dps)
        if not np.isfinite(s):
            return 100.0
        penalty = float(np.sum(np.maximum(0.05 - gaps, 0)))
        return s + 10.0 * penalty

    return obj


def cma_run(args):
    gaps0, sigma, max_fevals, tag, seed = args
    import cma

    obj = make_obj(dps=30)
    try:
        es = cma.CMAEvolutionStrategy(
            gaps0,
            sigma,
            {
                "maxfevals": max_fevals,
                "verbose": -9,
                "tolx": 1e-10,
                "seed": seed,
                "popsize": max(8, 4 + int(3 * np.log(len(gaps0)))),
            },
        )
        es.optimize(obj)
        best_gaps = es.result.xbest if es.result.xbest is not None else gaps0
        best_score = float(es.result.fbest if es.result.fbest is not None else 1e6)
    except Exception as e:
        return float("inf"), gaps0, tag, str(e)
    return best_score, list(best_gaps), tag, None


def make_starts(rng, base_roots, n_starts):
    """Diverse starts: insertion at many positions + cluster-structured randoms."""
    starts = []
    insertion_positions = list(range(2, 290, 5))
    for pos in insertion_positions:
        cand = sorted(base_roots + [float(pos)])
        if not all(cand[i + 1] - cand[i] >= 0.5 for i in range(len(cand) - 1)):
            continue
        starts.append((roots_to_gaps(cand), 0.1, f"pos{pos}"))
        perturbed = [c + rng.normal(0, 0.3) for c in cand]
        perturbed = sorted([max(0.1, p) for p in perturbed])
        if all(perturbed[i + 1] - perturbed[i] >= 0.1 for i in range(len(perturbed) - 1)):
            starts.append((roots_to_gaps(perturbed), 0.2, f"pos{pos}_pert"))

    target_k = len(base_roots) + 1
    for i in range(50):
        n_near = int(rng.integers(2, 5))
        n_far = int(rng.integers(4, 7))
        n_mid = target_k - n_near - n_far
        if n_mid < 2:
            continue
        near = list(np.sort(rng.uniform(2, 10, n_near)))
        mid = list(np.sort(rng.uniform(25, 65, n_mid)))
        far = list(np.sort(rng.uniform(95, 200, n_far)))
        roots = sorted(near + mid + far)
        if all(roots[j + 1] - roots[j] >= 0.5 for j in range(len(roots) - 1)):
            starts.append((roots_to_gaps(roots), 0.3, f"rand{i}_n{n_near}m{n_mid}f{n_far}"))

    rng.shuffle(starts)
    return starts[:n_starts]


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
    trail = POLISH_TRAIL / f"session-{SESSION_ID}-best.json"
    tmp = POLISH_TRAIL / f".tmp-{SESSION_ID}.json"
    with open(tmp, "w") as f:
        json.dump(result, f, indent=2)
    os.replace(tmp, trail)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--starts", type=int, default=64)
    parser.add_argument("--fevals", type=int, default=1500)
    parser.add_argument("--base-k", type=int, default=14)
    args = parser.parse_args()

    base_roots, base_score = _load_best_k(args.base_k)
    log("=" * 70)
    log(f"K={args.base_k + 1} PARALLEL CMA-ES")
    log(f"Base k={args.base_k}, starts={args.starts}, fevals/start={args.fevals}")
    log("=" * 70)

    rng = np.random.default_rng(2026)
    starts = make_starts(rng, base_roots, args.starts)
    log(f"Generated {len(starts)} starts")

    work = [(s[0], s[1], args.fevals, s[2], int(rng.integers(1, 2**31))) for s in starts]

    t0 = time.time()
    results = []
    with mp.Pool(args.workers) as pool:
        for i, res in enumerate(pool.imap_unordered(cma_run, work)):
            score, gaps, tag, err = res
            if err:
                continue
            results.append((score, gaps, tag))
            tag_short = tag[:30]
            if (i + 1) % 8 == 0:
                log(f"  [{i + 1}/{len(work)}] last={score:.6f} ({tag_short})")
    log(f"\nPool finished in {time.time() - t0:.0f}s")

    results.sort(key=lambda x: x[0])

    best_score = base_score
    best_roots = list(base_roots)
    new_bests = 0

    for s, gaps, tag in results[:30]:
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
