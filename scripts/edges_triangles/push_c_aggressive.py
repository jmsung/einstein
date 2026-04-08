"""C. Aggressive basin-hopping with larger noise + more iterations.

Higher noise scale → larger jumps → may escape current basin to a deeper one.
More iterations → longer search.
"""

import json
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
    print(f"=== C. Aggressive BH from {initial:.14f} ===\n")

    # Try several aggressive parameter combos with different seeds
    configs = [
        ("aggressive-1", 200, 0.5, 0.05, 333),
        ("aggressive-2", 200, 0.3, 0.03, 444),
        ("aggressive-3", 150, 0.7, 0.07, 555),
        ("aggressive-4", 150, 0.4, 0.02, 666),
    ]

    best_score = initial
    best_xs, best_ys = xs0.copy(), ys0.copy()
    results = []

    for label, n_iter, noise_max, noise_min, seed in configs:
        print(f"\n--- {label}: n_iter={n_iter}, noise={noise_min}-{noise_max}, seed={seed} ---")
        xs, ys = xs0.copy(), ys0.copy()
        xs, ys = basin_hopping_optimize(
            xs, ys,
            n_iter=n_iter, temp=1e-8, seed=seed,
            noise_max=noise_max, noise_min=noise_min,
        )
        xs, ys = golden_section_sweep(xs, ys, n_sweeps=80)
        # SA polish
        xs, ys = sa_perturb(xs, ys, n_rounds=15, n_perturbations=80, seed=seed + 1000, block_size=5)
        for _ in range(2):
            xs, ys = redistribute(xs, ys)
            xs, ys = golden_section_sweep(xs, ys, n_sweeps=50)
        xs, ys = coordinate_descent(xs, ys, n_iters=15, step_fracs=[0.0001, 0.00003, 0.00001, 0.000003, 0.000001])

        score = _score_from_arrays(xs, ys)
        results.append((label, score))
        print(f"  {label} final: {score:.14f}  (delta from initial: {score - initial:+.2e})")
        if score > best_score:
            best_xs, best_ys, best_score = xs.copy(), ys.copy(), score
            print(f"  *** NEW BEST: {best_score:.14f} ***")

    print("\n" + "=" * 60)
    print("AGGRESSIVE BH SUMMARY")
    print("=" * 60)
    for lbl, sc in sorted(results, key=lambda x: -x[1]):
        marker = " <-- BEST" if sc == best_score else ""
        print(f"  {lbl:20s}: {sc:.14f}{marker}")
    print(f"\nFINAL BEST: {best_score:.14f}")
    print(f"Improvement: {best_score - initial:+.2e}")

    if best_score > initial:
        data_xs = best_xs[1:-1]
        weights = np.array([turan_row(np.clip(x, 0.0, 0.95)) for x in data_xs])
        verify = compute_score(weights)
        print(f"Verified: {verify:.14f}")
        out = Path("results/problem-13-edges-triangles/solution-C.json")
        with open(out, "w") as f:
            json.dump({"weights": weights.tolist()}, f)
        print(f"Saved to {out}")
    else:
        print("No improvement.")


if __name__ == "__main__":
    main()
