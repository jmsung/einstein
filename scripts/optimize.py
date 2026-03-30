"""Hillclimb optimizer for the Uncertainty Principle problem.

Starts from the best known k=13 solution (Together-AI) and applies
coordinate-wise perturbations + random multi-coordinate moves.
"""
import sys
sys.path.insert(0, "src")

import json
import time
import numpy as np
from pathlib import Path
from einstein.fast_eval import fast_evaluate

RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)

# Together-AI's best k=13 roots (score 0.3188545891623888)
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


def coordinate_hillclimb(roots, step_sizes=None, max_iters=500):
    """Coordinate-wise hillclimbing with adaptive step sizes."""
    roots = list(roots)
    k = len(roots)
    best_score = fast_evaluate(roots)
    print(f"Initial score: {best_score:.15f}")

    if step_sizes is None:
        step_sizes = [0.01] * k

    improved_count = 0
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
                    # Keep roots sorted
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
                        improved_count += 1
                        print(f"  iter {iteration}, root[{i}] += {delta:+.6f} -> {best_score:.15f} (improvement: {improvement:.2e})")
                        break
                if any_improved:
                    break

        if not any_improved:
            # Shrink step sizes
            step_sizes = [s * 0.5 for s in step_sizes]
            if max(step_sizes) < 1e-12:
                print(f"Converged after {iteration} iterations, {improved_count} improvements")
                break
            print(f"  iter {iteration}: shrinking steps, max={max(step_sizes):.2e}")

    return roots, best_score


def random_perturbation_search(roots, n_trials=500, sigma=0.1):
    """Random perturbation search - perturb multiple roots at once."""
    roots = list(roots)
    k = len(roots)
    best_score = fast_evaluate(roots)
    print(f"\nRandom perturbation search (sigma={sigma}, {n_trials} trials)")
    print(f"Starting score: {best_score:.15f}")

    improved = 0
    for t in range(n_trials):
        trial = list(roots)
        # Perturb 1-4 random roots
        n_perturb = np.random.randint(1, min(5, k + 1))
        indices = np.random.choice(k, n_perturb, replace=False)
        for i in indices:
            trial[i] += np.random.randn() * sigma * (1 + abs(trial[i]) * 0.01)

        # Ensure validity
        trial.sort()
        if any(z <= 0 or z > 300 for z in trial):
            continue
        if any(trial[i + 1] - trial[i] < 0.01 for i in range(len(trial) - 1)):
            continue

        score = fast_evaluate(trial)
        if score < best_score - 1e-14:
            improvement = best_score - score
            best_score = score
            roots = trial
            improved += 1
            print(f"  trial {t}: score={best_score:.15f} (improvement: {improvement:.2e})")

    print(f"  {improved} improvements in {n_trials} trials")
    return roots, best_score


def try_add_root(roots, best_score):
    """Try adding a root at various positions to see if k+1 helps."""
    k = len(roots)
    print(f"\nTrying k={k+1} by adding a root...")

    # Scan candidate positions
    candidates = []
    # Between existing roots
    for i in range(k - 1):
        mid = (roots[i] + roots[i + 1]) / 2
        candidates.append(mid)
    # Before first root
    candidates.append(roots[0] / 2)
    # After last root
    for offset in [10, 20, 30, 50, 70]:
        if roots[-1] + offset <= 300:
            candidates.append(roots[-1] + offset)
    # In the gap regions
    for x in np.linspace(60, 200, 30):
        if all(abs(x - r) > 1 for r in roots):
            candidates.append(x)

    best_new = None
    best_new_score = best_score

    for c in candidates:
        trial = sorted(roots + [c])
        if any(trial[i + 1] - trial[i] < 0.01 for i in range(len(trial) - 1)):
            continue
        score = fast_evaluate(trial)
        if score < best_new_score:
            best_new_score = score
            best_new = trial
            print(f"  k={k+1}, new root at {c:.3f}: score={score:.15f}")

    if best_new is not None:
        print(f"  Best k={k+1} score: {best_new_score:.15f}")
        return best_new, best_new_score
    else:
        print(f"  No improvement found with k={k+1}")
        return roots, best_score


def main():
    print("=" * 60)
    print("Uncertainty Principle - Hillclimb Optimizer")
    print("=" * 60)

    roots = list(BEST_K13)
    score = fast_evaluate(roots)
    print(f"\nStarting from Together-AI's k=13 solution")
    print(f"Score: {score:.15f}")
    print(f"Roots: {roots}")

    # Phase 1: Coordinate hillclimb from the best known solution
    print("\n--- Phase 1: Coordinate hillclimb ---")
    roots, score = coordinate_hillclimb(
        roots,
        step_sizes=[0.05, 0.05, 0.05,  # near cluster
                    0.1, 0.1, 0.1, 0.1, 0.1, 0.1,  # mid cluster
                    0.5, 0.5, 0.5, 1.0],  # far cluster
        max_iters=200,
    )
    save_result(roots, score, "phase1_coord")

    # Phase 2: Random perturbation
    print("\n--- Phase 2: Random perturbation ---")
    for sigma in [0.5, 0.1, 0.05, 0.01]:
        roots, score = random_perturbation_search(roots, n_trials=300, sigma=sigma)
    save_result(roots, score, "phase2_random")

    # Phase 3: Fine coordinate hillclimb
    print("\n--- Phase 3: Fine coordinate hillclimb ---")
    roots, score = coordinate_hillclimb(
        roots,
        step_sizes=[0.001] * len(roots),
        max_iters=200,
    )
    save_result(roots, score, "phase3_fine")

    # Phase 4: Try adding a root
    print("\n--- Phase 4: Try k+1 ---")
    new_roots, new_score = try_add_root(roots, score)
    if new_score < score:
        roots, score = new_roots, new_score
        # Hillclimb the new root set
        roots, score = coordinate_hillclimb(roots, max_iters=200)
        save_result(roots, score, "phase4_k_plus_1")

    print("\n" + "=" * 60)
    print(f"FINAL RESULT")
    print(f"k={len(roots)}, score={score:.15f}")
    print(f"Roots: {roots}")
    print("=" * 60)

    save_result(roots, score, "final")


if __name__ == "__main__":
    main()
