"""A. Multi-seed basin-hopping from current best.

Run BH N times with different seeds. Each seed explores a different stochastic
trajectory; deepest result is kept.
"""

import json
import shutil
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))

from einstein.edges_triangles.evaluator import compute_score, turan_row  # noqa: E402
from optimize import (  # noqa: E402
    _score_from_arrays,
    basin_hopping_optimize,
    coordinate_descent,
    golden_section_sweep,
    redistribute,
    sa_perturb,
)


def load_to_xy(path: Path) -> tuple[np.ndarray, np.ndarray]:
    with open(path) as f:
        weights = np.array(json.load(f)["weights"], dtype=np.float64)
    weights = np.maximum(weights, 0.0)
    weights /= weights.sum(axis=1, keepdims=True)
    s2 = np.sum(weights**2, axis=1)
    s3 = np.sum(weights**3, axis=1)
    order = np.argsort(1.0 - s2)
    xs = np.concatenate([[0.0], (1.0 - s2)[order], [1.0]])
    ys = np.concatenate([[0.0], (1.0 - 3.0 * s2 + 2.0 * s3)[order], [1.0]])
    return xs, ys


def main():
    sol_path = Path("results/problem-13-edges-triangles/solution.json")
    xs0, ys0 = load_to_xy(sol_path)
    initial = _score_from_arrays(xs0, ys0)
    print(f"=== A. Multi-seed BH from {initial:.14f} ===\n")

    seeds = list(range(10))
    best_score = initial
    best_xs, best_ys = xs0.copy(), ys0.copy()
    results = []

    for s in seeds:
        print(f"\n--- Seed {s} ---")
        xs, ys = xs0.copy(), ys0.copy()
        xs, ys = basin_hopping_optimize(xs, ys, n_iter=50, temp=1e-8, seed=s)
        xs, ys = golden_section_sweep(xs, ys, n_sweeps=50)
        # Quick SA polish
        xs, ys = sa_perturb(xs, ys, n_rounds=10, n_perturbations=80, seed=s + 1000, block_size=5)
        for _ in range(2):
            xs, ys = redistribute(xs, ys)
            xs, ys = golden_section_sweep(xs, ys, n_sweeps=50)
        xs, ys = coordinate_descent(xs, ys, n_iters=15, step_fracs=[0.0001, 0.00003, 0.00001, 0.000003, 0.000001])

        score = _score_from_arrays(xs, ys)
        results.append((s, score))
        print(f"  Seed {s} final: {score:.14f}  (delta from initial: {score - initial:+.2e})")
        if score > best_score:
            best_xs, best_ys, best_score = xs.copy(), ys.copy(), score
            print(f"  *** NEW BEST: {best_score:.14f} ***")

    print("\n" + "=" * 60)
    print("MULTI-SEED BH SUMMARY")
    print("=" * 60)
    for s, sc in sorted(results, key=lambda x: -x[1]):
        marker = " <-- BEST" if sc == best_score else ""
        print(f"  seed {s:4d}: {sc:.14f}{marker}")
    print(f"\nFINAL BEST: {best_score:.14f}")
    print(f"Improvement: {best_score - initial:+.2e}")

    if best_score > initial:
        # Save
        data_xs = best_xs[1:-1]
        weights = np.array([turan_row(np.clip(x, 0.0, 0.95)) for x in data_xs])
        verify = compute_score(weights)
        print(f"Verified: {verify:.14f}")

        out = Path("results/problem-13-edges-triangles/solution-A.json")
        with open(out, "w") as f:
            json.dump({"weights": weights.tolist()}, f)
        print(f"Saved to {out}")
    else:
        print("No improvement.")


if __name__ == "__main__":
    main()
