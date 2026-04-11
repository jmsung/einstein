"""Aggressive k=15/k=16 optimization for Uncertainty Principle.

Strategy:
  Phase A: Deep k=15 search — wider sigma, more insertion positions, cold starts
  Phase B: k=16 climb from best k=15
  Phase C: Per-root hillclimb with hybrid verification on best candidate
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
SESSION_ID = time.strftime("%Y%m%d-%H%M%S")
K14_ARENA_SCORE = 0.31816916009639484
TARGET = K14_ARENA_SCORE - 1e-5  # 0.31815916


def log(msg):
    ts = time.strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


def roots_to_gaps(roots):
    roots = sorted(roots)
    return [roots[0]] + [roots[i] - roots[i - 1] for i in range(1, len(roots))]


def gaps_to_roots(gaps):
    return list(np.cumsum(gaps))


def make_obj(dps=30):
    def obj(gaps):
        gaps = np.asarray(gaps, dtype=float)
        repaired = np.maximum(gaps, 0.05)
        roots = list(np.cumsum(repaired))
        if roots[-1] > 300 or roots[0] <= 0:
            return 100.0
        s = fast_evaluate(roots, dps=dps)
        if not np.isfinite(s):
            return 100.0
        penalty = float(np.sum(np.maximum(0.05 - gaps, 0)))
        return s + 10.0 * penalty
    return obj


def cma_optimize(gaps, sigma, fevals, seed, popsize=14, tolx=1e-14):
    """Run CMA-ES optimization in gap space."""
    import cma
    obj = make_obj(dps=30)
    try:
        es = cma.CMAEvolutionStrategy(
            gaps, sigma,
            {"maxfevals": fevals, "verbose": -9, "tolx": tolx,
             "seed": seed, "popsize": popsize},
        )
        es.optimize(obj)
        return float(es.result.fbest), list(es.result.xbest) if es.result.xbest is not None else gaps
    except Exception as e:
        return float("inf"), gaps


def worker_k15(args):
    """Worker: optimize a k=15 starting configuration."""
    start_roots, tag, fevals, sigma, seed = args
    gaps = roots_to_gaps(start_roots)

    # Phase 1: Wide exploration
    s1, g1 = cma_optimize(gaps, sigma, fevals, seed, popsize=20)
    if s1 >= 1.0:
        return s1, gaps, tag, "p1_failed"

    # Phase 2: Medium refinement
    s2, g2 = cma_optimize(g1, min(sigma / 5, 0.01), fevals // 2, seed + 7, popsize=14)
    best_s, best_g = (s2, g2) if s2 < s1 else (s1, g1)

    # Phase 3: Fine polish
    s3, g3 = cma_optimize(best_g, 0.002, fevals // 4, seed + 13, popsize=14, tolx=1e-16)
    if s3 < best_s:
        best_s, best_g = s3, g3

    return best_s, best_g, tag, None


def worker_k16(args):
    """Worker: k=16 optimization from k=15 base with inserted root."""
    start_roots, tag, fevals, sigma, seed = args
    gaps = roots_to_gaps(start_roots)

    # Phase 1
    s1, g1 = cma_optimize(gaps, sigma, fevals, seed, popsize=22)
    if s1 >= 1.0:
        return s1, gaps, tag, "p1_failed"

    # Phase 2
    s2, g2 = cma_optimize(g1, sigma / 10, fevals // 2, seed + 7, popsize=16)
    best_s, best_g = (s2, g2) if s2 < s1 else (s1, g1)

    # Phase 3
    s3, g3 = cma_optimize(best_g, 0.002, fevals // 4, seed + 13, popsize=16, tolx=1e-16)
    if s3 < best_s:
        best_s, best_g = s3, g3

    return best_s, best_g, tag, None


def verify_and_save(roots, fast_score, tag, k):
    """Verify with hybrid evaluator and save if valid."""
    log(f"  [{tag}] verifying (fast={fast_score:.14f})...")
    try:
        t0 = time.time()
        h = hybrid_evaluate(roots)
        dt = time.time() - t0
        diff = abs(fast_score - h)
        log(f"    Hybrid: {h:.16f} (diff={diff:.2e}, {dt:.0f}s)")
        if diff > 1e-4:
            log("    REJECTED — far sign change detected")
            return None

        delta = K14_ARENA_SCORE - h
        log(f"    Delta from k=14: {delta:.2e} (need > 1e-5)")
        if h < TARGET:
            log(f"    *** CROSSES GATE *** score={h:.16f}")

        result = {
            "problem": "uncertainty-principle",
            "k": k,
            "score": h,
            "score_fast": fast_score,
            "laguerre_double_roots": list(roots),
            "tag": tag,
            "verified": True,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        }
        fname = RESULTS_DIR / f"up_k{k}_{h:.10f}.json"
        with open(fname, "w") as f:
            json.dump(result, f, indent=2)
        log(f"    SAVED: {fname.name}")

        trail = POLISH_TRAIL / f"session-{SESSION_ID}-k{k}-best.json"
        with open(trail, "w") as f:
            json.dump(result, f, indent=2)

        return h
    except Exception as e:
        log(f"    Hybrid FAILED: {e}")
        return None


def hillclimb_hybrid(roots, tag, rounds=50):
    """Per-root binary-search hillclimb verified by hybrid evaluator."""
    log(f"\n=== HYBRID HILLCLIMB on {tag} ({len(roots)} roots, {rounds} rounds) ===")
    best_roots = list(roots)
    best_score = hybrid_evaluate(best_roots)
    log(f"  Start: {best_score:.16f}")

    step_sizes = [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001]
    improved_count = 0

    for rd in range(rounds):
        improved_this_round = False
        for i in range(len(best_roots)):
            for step in step_sizes:
                for direction in [+1, -1]:
                    trial = list(best_roots)
                    trial[i] += direction * step

                    # Constraints
                    if trial[i] <= 0 or trial[i] > 300:
                        continue
                    trial_sorted = sorted(trial)
                    if any(trial_sorted[j+1] - trial_sorted[j] < 0.05 for j in range(len(trial_sorted)-1)):
                        continue

                    # Fast screen
                    fs = fast_evaluate(trial, dps=30)
                    if not np.isfinite(fs) or fs >= best_score:
                        continue

                    # Hybrid verify
                    try:
                        hs = hybrid_evaluate(trial)
                    except Exception:
                        continue

                    if hs < best_score - 1e-15:
                        delta = best_score - hs
                        best_score = hs
                        best_roots = list(trial)
                        improved_count += 1
                        improved_this_round = True
                        log(f"  Round {rd} root[{i}] {'+' if direction>0 else '-'}{step}: "
                            f"{best_score:.16f} (Δ={delta:.2e})")
                        break  # move to next root
                if improved_this_round:
                    break
            if not improved_this_round:
                continue

        if not improved_this_round:
            # Try smaller steps
            if step_sizes[-1] > 1e-8:
                step_sizes.append(step_sizes[-1] / 10)
            else:
                log(f"  No improvement in round {rd} — stopping")
                break

    log(f"  Hillclimb done: {improved_count} improvements, final={best_score:.16f}")
    delta = K14_ARENA_SCORE - best_score
    log(f"  Delta from k=14: {delta:.2e}")
    return best_roots, best_score


def make_k15_starts(k14_roots, fine_grid=True):
    """Generate diverse k=15 starting positions."""
    starts = []

    # Fine grid near best insertion position (119)
    if fine_grid:
        for pos in range(100, 150):
            cand = sorted(list(k14_roots) + [float(pos)])
            if all(cand[j+1] - cand[j] >= 0.5 for j in range(len(cand)-1)):
                starts.append((cand, f"JS_fine{pos}"))

    # Broad grid
    for pos in range(2, 295, 3):
        cand = sorted(list(k14_roots) + [float(pos)])
        if all(cand[j+1] - cand[j] >= 0.5 for j in range(len(cand)-1)):
            tag = f"JS_broad{pos}"
            if not any(t == tag for _, t in starts):
                starts.append((cand, tag))

    # Mid-cluster insertions (split the mid cluster)
    for pos_f in np.linspace(32, 55, 30):
        pos = round(float(pos_f), 1)
        cand = sorted(list(k14_roots) + [pos])
        if all(cand[j+1] - cand[j] >= 0.5 for j in range(len(cand)-1)):
            starts.append((cand, f"JS_mid{pos}"))

    return starts


def make_k16_starts(k15_roots):
    """Generate k=16 starting positions from k=15 best."""
    starts = []
    for pos in range(2, 295, 2):
        cand = sorted(list(k15_roots) + [float(pos)])
        if all(cand[j+1] - cand[j] >= 0.5 for j in range(len(cand)-1)):
            starts.append((cand, f"k16_pos{pos}"))
    return starts


def make_cold_k15_starts(n_starts=30):
    """Generate random cold-start k=15 configurations."""
    rng = np.random.default_rng(42)
    starts = []
    for i in range(n_starts):
        while True:
            roots = sorted(rng.uniform(1, 280, 15))
            if all(roots[j+1] - roots[j] >= 0.05 for j in range(len(roots)-1)):
                starts.append((list(roots), f"cold{i}"))
                break
    return starts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--phase", choices=["k15", "k16", "hillclimb", "all"], default="all")
    parser.add_argument("--fevals", type=int, default=8000)
    parser.add_argument("--sigma", type=float, default=0.1)
    args = parser.parse_args()

    # Load bases
    with open("results/up_k14_0.3181691601.json") as f:
        k14 = json.load(f)
    k14_roots = k14["laguerre_double_roots"]

    k15_path = list(RESULTS_DIR.glob("up_k15_*.json"))
    if k15_path:
        best_k15_score = float("inf")
        best_k15 = None
        for p in k15_path:
            with open(p) as f:
                d = json.load(f)
            if d.get("verified") and d["score"] < best_k15_score:
                best_k15_score = d["score"]
                best_k15 = d
        if best_k15:
            k15_roots = best_k15["laguerre_double_roots"]
            log(f"Loaded k=15 best: {best_k15_score:.16f}")
        else:
            k15_roots = None
    else:
        k15_roots = None
        best_k15_score = float("inf")

    rng = np.random.default_rng(2026)
    overall_best_score = best_k15_score
    overall_best_roots = k15_roots

    # ===== PHASE A: Deep k=15 search =====
    if args.phase in ("k15", "all"):
        log("=" * 70)
        log("PHASE A: DEEP k=15 SEARCH")
        log(f"Fevals: {args.fevals}, Sigma: {args.sigma}, Workers: {args.workers}")
        log("=" * 70)

        starts = make_k15_starts(k14_roots, fine_grid=True)
        cold_starts = make_cold_k15_starts(20)
        starts.extend(cold_starts)
        log(f"Generated {len(starts)} k=15 starting configurations")

        work = [
            (s[0], s[1], args.fevals, args.sigma, int(rng.integers(1, 2**31)))
            for s in starts
        ]

        t0 = time.time()
        results = []
        with mp.Pool(args.workers) as pool:
            for i, res in enumerate(pool.imap_unordered(worker_k15, work)):
                score, gaps, tag, err = res
                marker = ""
                if score < overall_best_score:
                    marker = " *** NEW BEST ***"
                if score < TARGET:
                    marker = " *** CROSSES GATE ***"
                log(f"  [{i+1}/{len(work)}] {tag}: {score:.14f}{marker}"
                    f"{' ('+err+')' if err else ''}")
                results.append((score, gaps, tag))

        log(f"\nPhase A pool: {time.time()-t0:.0f}s")
        results.sort(key=lambda x: x[0])

        # Verify top candidates
        log("\n--- Verifying top k=15 candidates ---")
        for s, gaps, tag in results[:20]:
            if s >= K14_ARENA_SCORE:
                continue
            roots = gaps_to_roots(gaps)
            if any(r <= 0 or r > 300 for r in roots):
                continue
            if any(roots[j+1] - roots[j] < 0.05 for j in range(len(roots)-1)):
                continue
            h = verify_and_save(roots, s, f"k15_{tag}", 15)
            if h is not None and h < overall_best_score:
                overall_best_score = h
                overall_best_roots = list(roots)

        log(f"\nPhase A best verified: {overall_best_score:.16f}")
        log(f"Delta from k=14: {K14_ARENA_SCORE - overall_best_score:.2e}")

    # ===== PHASE B: k=16 climb =====
    if args.phase in ("k16", "all") and overall_best_roots is not None:
        log("\n" + "=" * 70)
        log("PHASE B: k=16 CLIMB")
        log("=" * 70)

        k16_starts = make_k16_starts(overall_best_roots)
        log(f"Generated {len(k16_starts)} k=16 starting configurations")

        work = [
            (s[0], s[1], args.fevals, args.sigma, int(rng.integers(1, 2**31)))
            for s in k16_starts
        ]

        t0 = time.time()
        results = []
        with mp.Pool(args.workers) as pool:
            for i, res in enumerate(pool.imap_unordered(worker_k16, work)):
                score, gaps, tag, err = res
                marker = ""
                if score < overall_best_score:
                    marker = " *** NEW BEST ***"
                if score < TARGET:
                    marker = " *** CROSSES GATE ***"
                log(f"  [{i+1}/{len(work)}] {tag}: {score:.14f}{marker}"
                    f"{' ('+err+')' if err else ''}")
                results.append((score, gaps, tag))

        log(f"\nPhase B pool: {time.time()-t0:.0f}s")
        results.sort(key=lambda x: x[0])

        # Verify top candidates
        log("\n--- Verifying top k=16 candidates ---")
        for s, gaps, tag in results[:15]:
            if s >= overall_best_score:
                continue
            roots = gaps_to_roots(gaps)
            if any(r <= 0 or r > 300 for r in roots):
                continue
            if any(roots[j+1] - roots[j] < 0.05 for j in range(len(roots)-1)):
                continue
            h = verify_and_save(roots, s, f"k16_{tag}", 16)
            if h is not None and h < overall_best_score:
                overall_best_score = h
                overall_best_roots = list(roots)

        log(f"\nPhase B best verified: {overall_best_score:.16f}")
        log(f"Delta from k=14: {K14_ARENA_SCORE - overall_best_score:.2e}")

    # ===== PHASE C: Hybrid hillclimb on best =====
    if args.phase in ("hillclimb", "all") and overall_best_roots is not None:
        log("\n" + "=" * 70)
        log("PHASE C: HYBRID HILLCLIMB")
        log("=" * 70)

        best_roots, best_score = hillclimb_hybrid(
            overall_best_roots, f"k{len(overall_best_roots)}_best", rounds=30
        )
        if best_score < overall_best_score:
            overall_best_score = best_score
            overall_best_roots = best_roots
            verify_and_save(best_roots, best_score, "hillclimb_final", len(best_roots))

    # ===== Summary =====
    log("\n" + "=" * 70)
    log("FINAL SUMMARY")
    log(f"  Best score: {overall_best_score:.16f}")
    log(f"  k = {len(overall_best_roots) if overall_best_roots else '?'}")
    log(f"  Delta from k=14: {K14_ARENA_SCORE - overall_best_score:.2e}")
    log(f"  Target: < {TARGET:.16f}")
    log(f"  Crosses gate: {overall_best_score < TARGET}")
    log("=" * 70)


if __name__ == "__main__":
    main()
