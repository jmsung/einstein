"""Optimizer for the Uncertainty Principle problem.

Strategies:
  1. CMA-ES (primary) — global search per k-value
  2. Coordinate hillclimb — local refinement
  3. Multi-start k-scanning — try k=5..20 with random initializations
"""

import sys
sys.path.insert(0, "src")

import json
import time
import numpy as np
import cma
from pathlib import Path
from einstein.fast_eval import fast_evaluate

RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)

# REDACTED's best k=13 roots (score REDACTED)
BEST_K13 = [
    3.1427440085666496, 4.469993893132148, 6.078689469782297,
    32.637646271046336, 38.265477818082566, 41.06153063739393,
    43.09262298321874, 50.81816373872074, 58.61770809389174,
    96.07661117430976, 111.48735817427675, 118.74229251036576,
    141.09580664199572,
]


def save_result(roots, score, tag=""):
    """Save a result to disk."""
    result = {
        "problem": "uncertainty-principle",
        "k": len(roots),
        "score": score,
        "laguerre_double_roots": roots,
        "tag": tag,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    fname = RESULTS_DIR / f"up_k{len(roots)}_{score:.10f}.json"
    with open(fname, "w") as f:
        json.dump(result, f, indent=2)
    print(f"  Saved to {fname}")


def random_sorted_roots(k, lo=0.5, hi=250.0):
    """Generate k random sorted roots in (lo, hi) with minimum spacing."""
    roots = sorted(np.random.uniform(lo, hi, k))
    # Ensure minimum spacing of 0.5
    for i in range(1, k):
        if roots[i] - roots[i - 1] < 0.5:
            roots[i] = roots[i - 1] + 0.5
    if roots[-1] > 300:
        return None
    return roots


def cma_objective(x):
    """CMA-ES objective: roots encoded as sorted cumulative gaps."""
    # x[0] = first root position, x[i>0] = gap to next root
    roots = np.cumsum(np.abs(x))
    roots = list(roots)
    if any(z <= 0 or z > 300 for z in roots):
        return 1e6
    if any(roots[i + 1] - roots[i] < 0.01 for i in range(len(roots) - 1)):
        return 1e6
    score = fast_evaluate(roots)
    return score if np.isfinite(score) else 1e6


def roots_to_gaps(roots):
    """Convert sorted roots to gap encoding for CMA-ES."""
    gaps = [roots[0]]
    for i in range(1, len(roots)):
        gaps.append(roots[i] - roots[i - 1])
    return gaps


def gaps_to_roots(gaps):
    """Convert gap encoding back to sorted roots."""
    return list(np.cumsum(np.abs(gaps)))


def run_cma(roots, sigma=2.0, max_evals=1000, tag="cma"):
    """Run CMA-ES optimization starting from given roots."""
    k = len(roots)
    x0 = roots_to_gaps(roots)

    opts = cma.CMAOptions()
    opts["maxfevals"] = max_evals
    opts["tolfun"] = 1e-14
    opts["tolx"] = 1e-12
    opts["verbose"] = -1  # quiet
    opts["bounds"] = [[0.01] * k, [300.0] + [299.0] * (k - 1)]

    es = cma.CMAEvolutionStrategy(x0, sigma, opts)
    es.optimize(cma_objective)

    best_gaps = es.result.xbest
    best_roots = gaps_to_roots(best_gaps)
    best_score = es.result.fbest

    print(f"  CMA-ES k={k}: score={best_score:.15f} ({es.result.evaluations} evals)")
    return best_roots, best_score


def coordinate_hillclimb(roots, step_sizes=None, max_iters=500):
    """Coordinate-wise hillclimbing with adaptive step sizes."""
    roots = list(roots)
    k = len(roots)
    best_score = fast_evaluate(roots)

    if step_sizes is None:
        step_sizes = [0.01] * k

    for iteration in range(max_iters):
        any_improved = False
        for i in range(k):
            for direction in [1, -1]:
                for scale in [1.0, 0.5, 0.1, 2.0, 5.0]:
                    trial = list(roots)
                    delta = direction * step_sizes[i] * scale
                    trial[i] += delta
                    if trial[i] <= 0 or trial[i] > 300:
                        continue
                    if i > 0 and trial[i] <= trial[i - 1] + 0.01:
                        continue
                    if i < k - 1 and trial[i] >= trial[i + 1] - 0.01:
                        continue

                    score = fast_evaluate(trial)
                    if score < best_score - 1e-14:
                        improvement = best_score - score
                        best_score = score
                        roots = trial
                        any_improved = True
                        print(f"  iter {iteration}, root[{i}] += {delta:+.6f} -> {best_score:.15f} (Δ={improvement:.2e})")
                        break
                if any_improved:
                    break

        if not any_improved:
            step_sizes = [s * 0.5 for s in step_sizes]
            if max(step_sizes) < 1e-12:
                print(f"  Converged after {iteration} iterations")
                break

    return roots, best_score


def scan_k_values(k_range=range(5, 21), starts_per_k=3, cma_evals=500):
    """Scan different k values with multi-start CMA-ES."""
    print("\n=== K-value scan ===")
    results = {}

    for k in k_range:
        print(f"\n--- k={k} ---")
        best_roots, best_score = None, float("inf")

        for start in range(starts_per_k):
            init = random_sorted_roots(k)
            if init is None:
                continue
            try:
                roots, score = run_cma(init, sigma=5.0, max_evals=cma_evals, tag=f"scan_k{k}")
                if score < best_score:
                    best_score = score
                    best_roots = roots
            except Exception as e:
                print(f"  start {start} failed: {e}")

        if best_roots is not None:
            results[k] = (best_roots, best_score)
            print(f"  Best k={k}: {best_score:.15f}")
            save_result(best_roots, best_score, f"scan_k{k}")

    # Summary
    print("\n=== K-scan summary ===")
    for k in sorted(results):
        _, score = results[k]
        print(f"  k={k:2d}: {score:.15f}")

    return results


def main():
    print("=" * 60)
    print("Uncertainty Principle — Optimizer")
    print("=" * 60)

    # Phase 1: CMA-ES from the best known k=13 solution
    print("\n--- Phase 1: CMA-ES from best known k=13 ---")
    roots = list(BEST_K13)
    score = fast_evaluate(roots)
    print(f"Starting score: {score:.15f}")

    roots, score = run_cma(roots, sigma=1.0, max_evals=2000)
    save_result(roots, score, "phase1_cma")

    # Phase 2: Fine coordinate hillclimb
    print("\n--- Phase 2: Fine hillclimb ---")
    roots, score = coordinate_hillclimb(roots, step_sizes=[0.001] * len(roots), max_iters=200)
    save_result(roots, score, "phase2_fine")

    # Phase 3: CMA-ES again with tighter sigma
    print("\n--- Phase 3: CMA-ES refinement ---")
    roots, score = run_cma(roots, sigma=0.5, max_evals=2000)
    save_result(roots, score, "phase3_cma_refine")

    # Phase 4: Scan other k values
    print("\n--- Phase 4: K-value scan ---")
    scan_results = scan_k_values(k_range=range(8, 18), starts_per_k=3, cma_evals=1000)

    # Find global best across all k
    all_results = {13: (roots, score)}
    all_results.update(scan_results)

    global_best_k = min(all_results, key=lambda k: all_results[k][1])
    best_roots, best_score = all_results[global_best_k]

    # Phase 5: Final refinement of global best
    print(f"\n--- Phase 5: Final refinement (k={global_best_k}) ---")
    best_roots, best_score = run_cma(best_roots, sigma=0.3, max_evals=3000)
    best_roots, best_score = coordinate_hillclimb(
        best_roots, step_sizes=[0.0001] * len(best_roots), max_iters=300
    )
    save_result(best_roots, best_score, "final")

    print("\n" + "=" * 60)
    print(f"FINAL RESULT")
    print(f"k={len(best_roots)}, score={best_score:.15f}")
    print(f"Roots: {best_roots}")
    print("=" * 60)


if __name__ == "__main__":
    main()
