"""Hybrid-verified hillclimb on the best verified k-root solution.

Loads the current best for the given k from results/, then performs a
per-root hillclimb. Every candidate that the fast evaluator likes is
verified with the hybrid evaluator (sympy + numpy.roots) before accepting,
which catches all far sign changes.

Usage: uv run python scripts/uncertainty/k14_polish.py [--rounds N] [--k 14]
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
        raise FileNotFoundError(f"No verified k={k} result in results/")
    return list(best_roots), best_score


def log(msg):
    ts = time.strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


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
    trail = POLISH_TRAIL / f"session-{SESSION_ID}-best.json"
    tmp = POLISH_TRAIL / f".tmp-{SESSION_ID}.json"
    with open(tmp, "w") as f:
        json.dump(result, f, indent=2)
    os.replace(tmp, trail)
    log(f"    SAVED: {fname.name}")


def verify(roots, fast_score):
    try:
        h = hybrid_evaluate(roots)
    except Exception as e:
        log(f"    Hybrid FAILED: {e}")
        return None
    diff = abs(fast_score - h)
    if diff > 1e-4:
        log(f"    REJECTED — far sign change (hybrid={h:.6f})")
        return None
    return h


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rounds", type=int, default=80)
    parser.add_argument("--minstep", type=float, default=1e-12)
    parser.add_argument("--k", type=int, default=14)
    args = parser.parse_args()

    log("=" * 70)
    log(f"K={args.k} POLISH (hybrid-verified hillclimb)")
    log(f"Rounds: {args.rounds}, min step: {args.minstep}")
    log("=" * 70)

    roots, base_fast = _load_best_k(args.k)
    k = len(roots)
    log(f"Loaded k={k} from results/")
    log(f"Starting fast: {base_fast:.16f}")
    base_hybrid = hybrid_evaluate(roots)
    log(f"Starting hyb:  {base_hybrid:.16f}")

    best_fast = base_fast
    best_hybrid = base_hybrid
    n_improvements = 0

    # Per-root step sizes
    step_sizes = [0.001] * k

    for round_idx in range(args.rounds):
        round_improved = False
        round_best_delta = 0.0
        for i in range(k):
            for d in (1, -1):
                for mult in (1.0, 0.5, 0.2, 0.1, 2.0, 5.0, 10.0):
                    step = step_sizes[i] * mult
                    if step < args.minstep:
                        continue
                    trial = list(roots)
                    trial[i] += d * step
                    if trial[i] <= 0 or trial[i] > 300:
                        continue
                    if i > 0 and trial[i] <= trial[i - 1] + 0.05:
                        continue
                    if i < k - 1 and trial[i] >= trial[i + 1] - 0.05:
                        continue

                    f_score = fast_evaluate(trial, dps=30)
                    if not np.isfinite(f_score) or f_score >= best_fast:
                        continue

                    # Worth verifying
                    h_score = verify(trial, f_score)
                    if h_score is None or h_score >= best_hybrid - 1e-15:
                        continue

                    delta = best_hybrid - h_score
                    n_improvements += 1
                    log(f"  [r{round_idx} #{n_improvements}] z[{i}] {d * step:+.6e}: "
                        f"hyb={h_score:.16f} (Δ={delta:.4e})")
                    save_result(trial, h_score, f_score, f"k14pol_r{round_idx}_z{i}")
                    roots = trial
                    best_fast = f_score
                    best_hybrid = h_score
                    step_sizes[i] = step
                    round_improved = True
                    round_best_delta = max(round_best_delta, delta)
                    break
                if round_improved:
                    break
            if round_improved:
                break

        if not round_improved:
            step_sizes = [s * 0.3 for s in step_sizes]
            log(f"  round {round_idx + 1}: no improvement, max step "
                f"{max(step_sizes):.2e}")
            if max(step_sizes) < args.minstep:
                log("  step sizes exhausted, stopping")
                break
        else:
            log(f"  round {round_idx + 1}: improved Δ={round_best_delta:.4e}, "
                f"running total {base_hybrid - best_hybrid:.4e}")

    log("\n" + "=" * 70)
    log(f"FINAL: k=14, S={best_hybrid:.16f}")
    log(f"Improvement vs base: {base_hybrid - best_hybrid:.6e}")
    log(f"Improvements: {n_improvements}")


if __name__ == "__main__":
    main()
