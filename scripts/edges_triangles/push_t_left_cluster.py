"""P13 push: test Council 5's left-side clustering hypothesis.

Council 5 claim: t'(x) has sqrt singularity (x_k - x)^{-1/2} at the RIGHT endpoint
of scallop k (approaching cusp from left). So sqrt(phi) ~ (x_k - x)^{-1/4}, and
the optimal density CLUSTERS LEFT of each cusp, not symmetrically.

Current solution: 1 point per cusp snapped to x_k + 1e-9 (right side).
Test: move those points to x_k - 1e-3 (LEFT side, scallop k-1), polish.

Also tries other left-side offsets.
"""

import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from einstein.edges_triangles.evaluator import compute_score  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from push_d_torch_lbfgs import load_xs_from_solution  # noqa: E402
from push_g_bounded import lbfgs_polish_bounded, save_solution, true_score  # noqa: E402

RESULTS = Path("results/problem-13-edges-triangles")


def move_snapped_to_left(multi_xs: np.ndarray, offset: float, k_range=range(3, 20)) -> np.ndarray:
    """Move cusp-snapped points from right (x_k+eps) to left (x_k-offset)."""
    xs = multi_xs.copy()
    for k in k_range:
        x_k = 1.0 - 1.0 / k
        idx = int(np.argmin(np.abs(xs - x_k)))
        if abs(xs[idx] - x_k) > 1e-6:
            continue
        # Currently at x_k + eps. Move to x_k - offset (in scallop k-1)
        xs[idx] = x_k - offset
    return np.sort(xs)


def main():
    bi_xs, multi_xs = load_xs_from_solution(RESULTS / "solution.json")
    init_score = true_score(bi_xs, multi_xs)
    print(f"Initial: {init_score:.14f}")

    best_multi = multi_xs.copy()
    best_score = init_score

    print("\n=== Left-side clustering test ===")
    for offset in [1e-9, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 5e-4, 2e-3]:
        adjusted = move_snapped_to_left(multi_xs, offset)
        try:
            pol, _ = lbfgs_polish_bounded(adjusted, bi_xs, max_rounds=80)
            sc = true_score(bi_xs, pol)
            marker = " NEW BEST" if sc > best_score + 1e-13 else ""
            print(f"  offset={offset:.1e}: raw={true_score(bi_xs, adjusted):.14f} polished={sc:.14f}{marker}")
            if sc > best_score + 1e-13:
                best_multi = pol.copy()
                best_score = sc
        except Exception as e:
            print(f"  offset={offset}: failed ({e})")

    # Mixed: some cusps left, some right
    print("\n=== Per-cusp left/right mix ===")
    # For each cusp, try snapping JUST that one to left and see if it helps
    for k in range(3, 20):
        adjusted = multi_xs.copy()
        x_k = 1.0 - 1.0 / k
        idx = int(np.argmin(np.abs(adjusted - x_k)))
        if abs(adjusted[idx] - x_k) > 1e-6:
            continue
        for offset in [1e-4, 1e-3]:
            test = adjusted.copy()
            test[idx] = x_k - offset
            test = np.sort(test)
            try:
                pol, _ = lbfgs_polish_bounded(test, bi_xs, max_rounds=60)
                sc = true_score(bi_xs, pol)
                if sc > best_score + 1e-13:
                    best_multi = pol.copy()
                    best_score = sc
                    print(f"  k={k:2d} offset={offset:.1e}: {sc:.14f} NEW BEST (+{sc-init_score:.3e})")
            except Exception:
                pass

    print(f"\nFinal: {best_score:.14f}")
    print(f"Gain : {best_score - init_score:+.3e}")

    if best_score > init_score + 1e-13:
        save_solution(bi_xs, best_multi, "push-t-final")
        print("\n** IMPROVED")


if __name__ == "__main__":
    main()
