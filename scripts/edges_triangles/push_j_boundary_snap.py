"""P13 push: snap to scallop boundaries + polish.

Scallop boundaries are at x = 1 - 1/k for k = 2..19. At each boundary, the
Turán lower envelope has a kink. Slope-3 interpolation across a kink is an
upper bound on the true area; placing a point EXACTLY at the boundary tightens
the bound.

Strategy:
1. Load current best
2. For each scallop boundary x*, find the nearest multipartite point
3. SNAP that point to the boundary (add tiny eps for numerical safety)
4. Run bounded L-BFGS polish on the rest (keep snapped points anchored)
5. Also try: ADD a new point at each boundary (replaces a redundant interior point)
"""

import json
import shutil
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from einstein.edges_triangles.evaluator import compute_score, compute_densities, turan_row  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from push_d_torch_lbfgs import load_xs_from_solution  # noqa: E402
from push_g_bounded import lbfgs_polish_bounded, save_solution, true_score  # noqa: E402

RESULTS = Path("results/problem-13-edges-triangles")


def snap_to_boundaries(multi_xs: np.ndarray, k_range: range = range(3, 20)) -> np.ndarray:
    """For each scallop boundary x*=1-1/k, snap the nearest point."""
    snapped = multi_xs.copy()
    for k in k_range:
        x_star = 1.0 - 1.0 / k
        # Find nearest point that's not already at a boundary (avoid double-snap)
        idx = int(np.argmin(np.abs(snapped - x_star)))
        # Snap to slightly below boundary (stays in scallop k-1) or slightly above (scallop k)?
        # The boundary x*= 1-1/k is where scallop k-1 ends and scallop k starts.
        # At x*, both formulas give the same y (continuity). So pick either side.
        # Place slightly INSIDE the scallop k (the larger side)
        snapped[idx] = x_star + 1e-9
    return np.sort(snapped)


def polish_with_snapped(multi_xs: np.ndarray, bi_xs: np.ndarray, snap_ks: range) -> tuple[np.ndarray, float]:
    """Snap to boundaries, then polish the rest."""
    snapped = snap_to_boundaries(multi_xs, snap_ks)
    # Now polish
    polished, _ = lbfgs_polish_bounded(snapped, bi_xs, max_rounds=80)
    return polished, true_score(bi_xs, polished)


def insert_boundary_points(multi_xs: np.ndarray, k_range: range, x_lo: float = 0.5, x_hi: float = 0.95) -> np.ndarray:
    """Insert points at scallop boundaries, remove an equal number of redundant interior points.

    Strategy: for each scallop boundary not already present, insert a point there.
    Then drop the interior points that are closest to their neighbors (lowest marginal gain).
    """
    # Find which boundaries are missing (> 1e-8 from any point)
    missing = []
    for k in k_range:
        x_star = 1.0 - 1.0 / k
        if np.min(np.abs(multi_xs - x_star)) > 1e-8:
            missing.append(x_star)
    if not missing:
        return multi_xs.copy()

    new_xs = np.sort(np.concatenate([multi_xs, missing]))

    # Now we have too many points; drop the ones with smallest neighbor gaps
    # (those contribute least to discretization)
    n_remove = len(missing)
    # Compute "smallness" metric: gap from left neighbor
    gaps = np.diff(new_xs)
    # Score each interior point by its immediate gap — smallest gap = most removable
    # (but don't remove boundary-snapped ones)
    is_boundary = np.zeros(len(new_xs), dtype=bool)
    for k in k_range:
        x_star = 1.0 - 1.0 / k
        idx = int(np.argmin(np.abs(new_xs - x_star)))
        if abs(new_xs[idx] - x_star) < 1e-8:
            is_boundary[idx] = True

    # For each interior point, its local gap sum (left + right)
    local_gaps = np.full(len(new_xs), np.inf)
    for i in range(1, len(new_xs) - 1):
        if is_boundary[i]:
            continue
        local_gaps[i] = min(new_xs[i] - new_xs[i-1], new_xs[i+1] - new_xs[i])

    # Remove n_remove points with smallest local_gaps
    remove_idx = np.argsort(local_gaps)[:n_remove]
    keep_mask = np.ones(len(new_xs), dtype=bool)
    keep_mask[remove_idx] = False
    return new_xs[keep_mask]


def main():
    bi_xs, multi_xs = load_xs_from_solution(RESULTS / "solution.json")
    init_score = true_score(bi_xs, multi_xs)
    print(f"Initial: {init_score:.14f} ({len(multi_xs)} multi)")

    best_multi = multi_xs.copy()
    best_score = init_score

    # Strategy 1: snap points to boundaries
    print("\n=== Snap to boundaries + polish ===")
    for k_set in [
        range(3, 20),      # all scallop boundaries
        range(3, 10),      # low-k only (bigger scallops)
        range(10, 20),     # high-k only
        range(3, 8),
        range(8, 15),
    ]:
        snapped_multi, sc = polish_with_snapped(multi_xs, bi_xs, k_set)
        delta = sc - init_score
        marker = " NEW BEST" if sc > best_score + 1e-13 else ""
        print(f"  snap {list(k_set)[0]}..{list(k_set)[-1]}: {sc:.14f}  delta={delta:+.3e}{marker}")
        if sc > best_score + 1e-13:
            best_multi = snapped_multi.copy()
            best_score = sc

    # Strategy 2: insert boundary points
    print("\n=== Insert boundary points ===")
    for k_set in [
        range(3, 20),
        range(3, 10),
        range(10, 20),
    ]:
        try:
            new_multi = insert_boundary_points(multi_xs, k_set)
            # Polish
            pol, _ = lbfgs_polish_bounded(new_multi, bi_xs, max_rounds=60)
            sc = true_score(bi_xs, pol)
            delta = sc - init_score
            marker = " NEW BEST" if sc > best_score + 1e-13 else ""
            print(f"  insert {list(k_set)[0]}..{list(k_set)[-1]}: {sc:.14f} delta={delta:+.3e}{marker}")
            if sc > best_score + 1e-13:
                best_multi = pol.copy()
                best_score = sc
        except Exception as e:
            print(f"  insert failed: {e}")

    # Final report
    print(f"\nInitial: {init_score:.14f}")
    print(f"Final  : {best_score:.14f}")
    print(f"Gain   : {best_score - init_score:+.3e}")

    if best_score > init_score + 1e-12:
        save_solution(bi_xs, best_multi, "push-j-final")
        print("\n** IMPROVED — saved")


if __name__ == "__main__":
    main()
