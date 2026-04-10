"""Polish a warm-start solution with basin-hopping + SA pipeline."""

import json
import sys
from pathlib import Path

import numpy as np

# Make sibling import work
sys.path.insert(0, str(Path(__file__).resolve().parent))

from einstein.edges_triangles.evaluator import compute_score  # noqa: E402
from optimize import (  # noqa: E402
    _score_from_arrays,
    basin_hopping_optimize,
    coordinate_descent,
    golden_section_sweep,
    redistribute,
    sa_perturb,
)


def load_to_xy(path: Path) -> tuple[np.ndarray, np.ndarray]:
    """Load solution.json → (xs, ys) with boundary."""
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


def polish(input_path: Path, label: str) -> tuple[float, np.ndarray, np.ndarray]:
    """Run polish pipeline on a warm-start."""
    xs, ys = load_to_xy(input_path)
    initial = _score_from_arrays(xs, ys)
    print(f"\n=== {label} ===")
    print(f"Initial: {initial:.14f}")

    # Quick CD polish first to bring it to local opt
    print(f"  CD polish...")
    xs, ys = coordinate_descent(xs, ys, n_iters=30, step_fracs=[0.1, 0.03, 0.01, 0.003, 0.001])
    print(f"  After CD: {_score_from_arrays(xs, ys):.14f}")

    print(f"  GS polish...")
    xs, ys = golden_section_sweep(xs, ys, n_sweeps=100)
    print(f"  After GS: {_score_from_arrays(xs, ys):.14f}")

    print(f"  Basin-hopping (50 iters)...")
    xs, ys = basin_hopping_optimize(xs, ys, n_iter=50, temp=1e-8)
    xs, ys = golden_section_sweep(xs, ys, n_sweeps=50)
    print(f"  After BH: {_score_from_arrays(xs, ys):.14f}")

    # SA mega-cycles
    best_xs, best_ys = xs.copy(), ys.copy()
    best_score = _score_from_arrays(best_xs, best_ys)
    for mega in range(3):
        xm, ym = sa_perturb(best_xs, best_ys, n_rounds=15, n_perturbations=80, seed=mega * 17 + 3, block_size=5)
        for _ in range(2):
            xm, ym = redistribute(xm, ym)
            xm, ym = golden_section_sweep(xm, ym, n_sweeps=80)
        xm, ym = coordinate_descent(xm, ym, n_iters=20, step_fracs=[0.0001, 0.00003, 0.00001, 0.000003, 0.000001])
        sm = _score_from_arrays(xm, ym)
        if sm > best_score:
            best_xs, best_ys, best_score = xm.copy(), ym.copy(), sm
            print(f"  Mega {mega}: {best_score:.14f} (NEW BEST)")
        else:
            print(f"  Mega {mega}: {sm:.14f}")

    print(f"FINAL: {best_score:.14f}  (gain from initial: {best_score - initial:+.2e})")
    return best_score, best_xs, best_ys


def main():
    warm_dir = Path("results/problem-13-edges-triangles/warm-starts")
    files = sorted(warm_dir.glob("rank*.json"))

    # Load current best dynamically from solution.json
    cur_xs, cur_ys = load_to_xy(Path("results/problem-13-edges-triangles/solution.json"))
    our_score = _score_from_arrays(cur_xs, cur_ys)
    print(f"Our current best: {our_score:.14f}")
    print(f"Polishing {len(files)} warm-starts...\n")

    results = []
    for f in files:
        label = f.stem
        score, xs, ys = polish(f, label)
        results.append((label, score, xs, ys))

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"{'Warm-start':50s} {'Polished score':>22s}")
    for label, score, _, _ in results:
        marker = ' *** BEATS OUR BEST ***' if score > our_score else ''
        print(f"{label:50s} {score:22.14f}{marker}")
    print(f"{'Our current best':50s} {our_score:22.14f}")

    # Find best overall
    best = max(results, key=lambda r: r[1])
    if best[1] > our_score:
        print(f"\n*** NEW RECORD: {best[1]:.14f} from {best[0]} ***")
        print(f"   Improvement: {best[1] - our_score:+.2e}")

        # Save it
        data_xs = best[2][1:-1]
        from einstein.edges_triangles.evaluator import turan_row
        weights = np.array([turan_row(np.clip(x, 0.0, 0.95)) for x in data_xs])
        verify = compute_score(weights)
        print(f"   Verified: {verify:.14f}")

        out = Path("results/problem-13-edges-triangles/solution.json")
        with open(out, "w") as f:
            json.dump({"weights": weights.tolist()}, f)
        print(f"   Saved to {out}")
    else:
        print(f"\nNo improvement. Our score still best.")


if __name__ == "__main__":
    main()
