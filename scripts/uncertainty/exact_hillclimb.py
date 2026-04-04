"""Exact hillclimb using the sympy verifier.

Key insight: the fast evaluator has 90%+ false positive rate for improvements.
The sympy verifier is the ground truth (exact rational arithmetic).
By using the exact verifier directly in the hillclimb, EVERY improvement is real.

Trade-off: each evaluation takes ~minutes instead of ~0.2s.
But we only need to close a gap of 1.3e-4, so a few real improvements suffice.

Strategy:
1. Use fast evaluator to SCREEN candidates (accept only improvements > 1e-6)
2. Use exact verifier to VALIDATE candidates
3. Fine per-root hillclimb with adaptive steps
"""
import sys
sys.path.insert(0, "src")

import json
import time
import numpy as np
from pathlib import Path
from einstein.uncertainty.fast import fast_evaluate
from einstein.uncertainty.verifier import evaluate as exact_evaluate

RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)

TARGET = 0.318221

BEST = [
    3.0886658942606733, 4.435156861236376, 6.034127890108831,
    30.945538933257353, 36.84167838791129, 42.20424571337132,
    47.682624801878234, 51.92315504790176, 57.58188043903107,
    100.75022929245691, 115.44761608340504, 123.04406833559523,
    140.04812478845042,
]


def log(msg):
    ts = time.strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


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
    fname = RESULTS_DIR / f"up_exact_{score:.10f}.json"
    with open(fname, "w") as f:
        json.dump(result, f, indent=2)
    log(f"  SAVED: {fname.name}")


def main():
    log("="*70)
    log("EXACT HILLCLIMB — Sympy-verified improvements only")
    log("="*70)

    # First: get exact baseline score
    log("Computing exact baseline...")
    t0 = time.time()
    exact_base = exact_evaluate({"laguerre_double_roots": BEST})
    fast_base = fast_evaluate(BEST)
    dt = time.time() - t0
    log(f"  Exact: {exact_base:.16f} ({dt:.1f}s)")
    log(f"  Fast:  {fast_base:.16f}")
    log(f"  Diff:  {abs(exact_base - fast_base):.2e}")
    log(f"  Target: {TARGET}")
    log(f"  Gap:    {exact_base - TARGET:.10f}")

    roots = list(BEST)
    best_exact = exact_base
    best_fast = fast_base
    total_evals = 0
    total_improvements = 0

    # Phase 1: Fast-screened exact hillclimb
    log("\n--- Phase 1: Per-root hillclimb ---")
    # Run the optimizer loop with exact verification only
    # The fast evaluator is UNRELIABLE for this problem (90%+ false positive rate)
    # So we use exact verifier as the ONLY truth source
    k = len(roots)
    step_sizes = [0.001] * k  # Start conservative — fast evaluator pre-screens

    for round_idx in range(500):
        round_improved = False

        for i in range(k):
            # Try multiple step sizes for each root
            for mult in [1.0, 0.5, 0.2, 2.0, 5.0, 10.0, 0.1, 0.01]:
                step = step_sizes[i] * mult

                for d in [1, -1]:
                    trial = list(roots)
                    trial[i] += d * step
                    if trial[i] <= 0 or trial[i] > 300:
                        continue
                    if i > 0 and trial[i] <= trial[i-1] + 0.01:
                        continue
                    if i < k-1 and trial[i] >= trial[i+1] - 0.01:
                        continue

                    # Fast screen: only verify if fast score improves
                    # BUT: fast evaluator has 90%+ false positive rate
                    # So we accept small improvements too
                    fast_score = fast_evaluate(trial)
                    if not np.isfinite(fast_score) or fast_score >= best_fast:
                        continue

                    # Exact verification
                    log(f"  z[{i}] += {d*step:+.6f}: fast={fast_score:.14f} "
                        f"(Δ={fast_score-best_fast:+.4e}). Verifying...")

                    t0 = time.time()
                    try:
                        exact_score = exact_evaluate({"laguerre_double_roots": trial})
                    except Exception as e:
                        log(f"    Verifier error: {e}")
                        continue
                    dt = time.time() - t0
                    total_evals += 1

                    diff = abs(fast_score - exact_score)
                    if diff > 1e-4:
                        log(f"    REJECTED: exact={exact_score:.10f} ({dt:.0f}s) "
                            f"— far sign change!")
                        continue

                    if exact_score < best_exact - 1e-12:
                        old = best_exact
                        best_exact = exact_score
                        best_fast = fast_score
                        roots = list(trial)
                        step_sizes[i] = step
                        total_improvements += 1
                        save_result(roots, exact_score, f"exact_hc_r{round_idx}_i{i}")
                        log(f"    *** VERIFIED IMPROVEMENT #{total_improvements}: "
                            f"{old:.14f} → {exact_score:.14f} "
                            f"(Δ={old-exact_score:.4e}) ({dt:.0f}s) ***")
                        round_improved = True

                        if exact_score < TARGET:
                            log(f"\n!!! BEAT TARGET {TARGET} !!!")
                            return

                        break  # Move to next root
                if round_improved:
                    break
            if round_improved:
                break

        if not round_improved:
            # Shrink step sizes
            step_sizes = [s * 0.3 for s in step_sizes]
            log(f"  Round {round_idx+1}: no improvement, shrinking steps "
                f"(max={max(step_sizes):.2e})")
            if max(step_sizes) < 1e-12:
                log("  Steps too small, stopping")
                break
        else:
            log(f"  Round {round_idx+1}: improvement found. "
                f"Best={best_exact:.14f}")

    # Phase 2: Pairwise perturbation with exact verification
    log("\n--- Phase 2: Pairwise perturbation ---")
    for round_idx in range(20):
        improved = False
        for i in range(k):
            for j in range(i+1, k):
                for di, dj in [(1,1), (1,-1), (-1,1), (-1,-1)]:
                    for s in [0.001, 0.01, 0.05, 0.1]:
                        trial = list(roots)
                        trial[i] += di * s
                        trial[j] += dj * s
                        trial_sorted = sorted(trial)
                        if any(z <= 0 or z > 300 for z in trial_sorted):
                            continue
                        if any(trial_sorted[m+1] - trial_sorted[m] < 0.01
                               for m in range(k-1)):
                            continue

                        fast_score = fast_evaluate(trial_sorted)
                        if not np.isfinite(fast_score) or fast_score >= best_fast - 1e-8:
                            continue

                        log(f"  z[{i},{j}]: fast={fast_score:.14f}. Verifying...")
                        try:
                            exact_score = exact_evaluate(
                                {"laguerre_double_roots": trial_sorted})
                        except Exception:
                            continue
                        total_evals += 1

                        diff = abs(fast_score - exact_score)
                        if diff > 1e-4:
                            log(f"    REJECTED (far sign change)")
                            continue

                        if exact_score < best_exact - 1e-12:
                            old = best_exact
                            best_exact = exact_score
                            best_fast = fast_score
                            roots = list(trial_sorted)
                            total_improvements += 1
                            save_result(roots, exact_score,
                                       f"exact_pair_r{round_idx}_i{i}_j{j}")
                            log(f"    *** PAIR IMPROVEMENT #{total_improvements}: "
                                f"{old:.14f} → {exact_score:.14f} ***")
                            improved = True

                            if exact_score < TARGET:
                                log(f"\n!!! BEAT TARGET !!!")
                                return
                            break
                    if improved:
                        break
                if improved:
                    break
            if improved:
                break
        if not improved:
            log(f"  Pairwise round {round_idx+1}: no improvement")
            break

    log(f"\n{'='*70}")
    log(f"Final exact score: {best_exact:.16f}")
    log(f"Total exact evals: {total_evals}")
    log(f"Total improvements: {total_improvements}")
    if best_exact < TARGET:
        log("SUCCESS!")
    else:
        log(f"Gap: {best_exact - TARGET:.10f}")
    log(f"Roots: {roots}")


if __name__ == "__main__":
    main()
