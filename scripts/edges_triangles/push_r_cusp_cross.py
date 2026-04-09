"""P13 push: force cusp crossing.

Council 4 insight: bounded L-BFGS holds each point in its assigned scallop
via sigmoid bounds. If the true optimum has a point slightly across a
cusp (in the OTHER scallop from where the optimizer assigned it), bounded
L-BFGS can never find it.

Test: for each cusp k in 3..19, take the point nearest the cusp (currently
at x_k + 1e-9 inside scallop k), move it to the OTHER side (x_k - 1e-9 inside
scallop k-1), re-run polish. Also try pairs (move point from k to k-1 AND
a different point from k-1 to k).
"""

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from einstein.edges_triangles.evaluator import compute_score, turan_row  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from push_d_torch_lbfgs import assign_scallops, load_xs_from_solution  # noqa: E402
from push_g_bounded import lbfgs_polish_bounded, save_solution, true_score  # noqa: E402

RESULTS = Path("results/problem-13-edges-triangles")


def force_cross_cusp(multi_xs: np.ndarray, k: int, direction: str = "down") -> np.ndarray:
    """Move the nearest point to cusp x_k across to the other scallop.

    direction 'down': move from scallop k to scallop k-1
    direction 'up':   move from scallop k-1 to scallop k
    """
    x_k = 1.0 - 1.0 / k
    result = multi_xs.copy()
    idx = int(np.argmin(np.abs(result - x_k)))
    if direction == "down":
        # Move to just below cusp (in scallop k-1)
        result[idx] = x_k - 1e-9
    else:
        result[idx] = x_k + 1e-9
    return np.sort(result)


def merge_and_redistribute(multi_xs: np.ndarray, i: int, j: int) -> np.ndarray:
    """Merge adjacent points i and j into a single midpoint.

    Creates a 'free slot' by shrinking count by 1. Then inserts a new
    point at a random high-density region to keep count fixed.
    """
    result = multi_xs.copy()
    if j == i + 1:
        mid = (result[i] + result[j]) / 2
        result[i] = mid
        result = np.delete(result, j)
        # Now have m-1 points; insert a new one in the densest scallop (k=2)
        new_x = 0.5 + (1.0 - 1.0 / 2 - 0.5) * 0.5  # scallop k=2 midpoint
        result = np.sort(np.append(result, new_x))
    return result


def main():
    bi_xs, multi_xs = load_xs_from_solution(RESULTS / "solution.json")
    init_score = true_score(bi_xs, multi_xs)
    print(f"Initial: {init_score:.14f}")

    best_multi = multi_xs.copy()
    best_score = init_score

    print("\n=== Cusp crossing test ===")
    for k in range(3, 20):
        for direction in ["down", "up"]:
            try:
                crossed = force_cross_cusp(best_multi, k, direction)
                pol, _ = lbfgs_polish_bounded(crossed, bi_xs, max_rounds=80)
                sc = true_score(bi_xs, pol)
                delta = sc - init_score
                marker = " NEW BEST" if sc > best_score + 1e-13 else ""
                print(f"  k={k:2d} {direction}: {sc:.14f} delta={delta:+.3e}{marker}")
                if sc > best_score + 1e-13:
                    best_multi = pol.copy()
                    best_score = sc
            except Exception as e:
                print(f"  k={k} {direction}: failed ({e})")

    print(f"\n=== Current best after cusp cross: {best_score:.14f} ===")

    # Also try: ALL cusps down simultaneously
    print("\n=== Bulk cusp cross (all down) ===")
    try:
        bulk = best_multi.copy()
        for k in range(3, 20):
            bulk = force_cross_cusp(bulk, k, "down")
        pol, _ = lbfgs_polish_bounded(bulk, bi_xs, max_rounds=150)
        sc = true_score(bi_xs, pol)
        print(f"  bulk down: {sc:.14f} delta={sc-init_score:+.3e}")
        if sc > best_score + 1e-13:
            best_multi = pol.copy()
            best_score = sc
    except Exception as e:
        print(f"  bulk failed: {e}")

    print("\n=== Bulk cusp cross (all up) ===")
    try:
        bulk = best_multi.copy()
        for k in range(3, 20):
            bulk = force_cross_cusp(bulk, k, "up")
        pol, _ = lbfgs_polish_bounded(bulk, bi_xs, max_rounds=150)
        sc = true_score(bi_xs, pol)
        print(f"  bulk up: {sc:.14f} delta={sc-init_score:+.3e}")
        if sc > best_score + 1e-13:
            best_multi = pol.copy()
            best_score = sc
    except Exception as e:
        print(f"  bulk failed: {e}")

    print(f"\nFinal: {best_score:.14f}")
    print(f"Gain : {best_score - init_score:+.3e}")

    if best_score > init_score + 1e-13:
        save_solution(bi_xs, best_multi, "push-r-final")
        print("\n** IMPROVED")


if __name__ == "__main__":
    main()
