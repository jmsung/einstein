"""P13 optimizer via efficient reinsertion.

For each of the 500 points, try removing it and reinserting at the optimal
position from a fine grid. Each evaluation is O(1) — only 2-3 local segments
change. This escapes the current basin by allowing points to jump across
scallop boundaries.

Expected: O(500 * N_candidates) per sweep, runs in seconds.
"""

import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from einstein.edges_triangles.evaluator import (
    compute_densities,
    compute_score,
    turan_row,
)

SOLUTION_PATH = Path("results/problem-13-edges-triangles/solution-best.json")
RESULTS_DIR = Path("results/problem-13-edges-triangles")
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

N_CANDIDATES = 20000  # fine grid resolution


def seg_area(y0, y1, h):
    """Area under one slope-3 interpolation segment."""
    if h <= 0:
        return 0.0
    dy = y1 - y0
    if dy < 0:
        return y1 * h
    elif dy <= 3 * h:
        return -dy**2 / 6 + y1 * h
    else:
        return y0 * h + 1.5 * h**2


def build_candidate_table(n_candidates):
    """Precompute (x, y) for all candidate positions."""
    xs = np.linspace(1e-6, 0.95 - 1e-6, n_candidates)
    ys = np.zeros(n_candidates)
    for i, x in enumerate(xs):
        p = turan_row(x)
        _, ys[i] = compute_densities(p)
    return xs, ys


def total_score(xs_sorted, ys_sorted):
    """Compute total score from sorted arrays (including boundaries)."""
    xs = np.concatenate([[0.0], xs_sorted, [1.0]])
    ys = np.concatenate([[0.0], ys_sorted, [1.0]])
    area = 0.0
    max_gap = 0.0
    for i in range(len(xs) - 1):
        h = xs[i + 1] - xs[i]
        if h <= 0:
            continue
        max_gap = max(max_gap, h)
        area += seg_area(ys[i], ys[i + 1], h)
    return -(area + 10 * max_gap)


def reinsertion_sweep(xs, ys, cand_xs, cand_ys, verbose=True):
    """One sweep: for each point, try reinserting at every candidate.

    Returns: (new_xs, new_ys, new_score, n_improved)
    """
    n = len(xs)
    # Full arrays with boundaries
    full_xs = np.concatenate([[0.0], xs, [1.0]])
    full_ys = np.concatenate([[0.0], ys, [1.0]])

    # Precompute current total score
    current_score = total_score(xs, ys)
    n_improved = 0

    for point_idx in range(n):
        # This point is at full_xs[point_idx + 1], full_ys[point_idx + 1]
        fi = point_idx + 1  # index in full arrays

        # Current contribution: segments (fi-1, fi) and (fi, fi+1)
        h_left = full_xs[fi] - full_xs[fi - 1]
        h_right = full_xs[fi + 1] - full_xs[fi]
        area_left = seg_area(full_ys[fi - 1], full_ys[fi], h_left)
        area_right = seg_area(full_ys[fi], full_ys[fi + 1], h_right)
        current_local_area = area_left + area_right

        # Area of merged segment (without this point)
        h_merged = h_left + h_right
        area_merged = seg_area(full_ys[fi - 1], full_ys[fi + 1], h_merged)

        # Now try inserting at each candidate position
        # Find which segment the candidate falls in (after removing this point)
        # The segments after removal: full_xs without index fi
        xs_without = np.delete(full_xs, fi)
        ys_without = np.delete(full_ys, fi)

        best_gain = 0.0  # must improve (gain > 0)
        best_cand_idx = -1
        best_insert_pos = -1

        for ci in range(len(cand_xs)):
            cx = cand_xs[ci]
            cy = cand_ys[ci]

            # Find where cx would be inserted in xs_without
            pos = np.searchsorted(xs_without, cx)
            if pos == 0 or pos >= len(xs_without):
                continue  # can't insert at boundaries

            # The candidate splits segment (pos-1, pos) into two
            x_left = xs_without[pos - 1]
            x_right = xs_without[pos]
            y_left = ys_without[pos - 1]
            y_right = ys_without[pos]

            h_seg = x_right - x_left
            if h_seg < 1e-14:
                continue

            h_new_left = cx - x_left
            h_new_right = x_right - cx

            if h_new_left < 1e-14 or h_new_right < 1e-14:
                continue

            area_old_seg = seg_area(y_left, y_right, h_seg)
            area_new = seg_area(y_left, cy, h_new_left) + seg_area(cy, y_right, h_new_right)

            # Total area change:
            # Remove point: +area_merged - current_local_area
            # Insert at candidate: +area_new - area_old_seg
            # But area_merged and area_old_seg depend on whether the candidate
            # is in the same merged segment or a different one.

            # If candidate is in the merged segment:
            if pos - 1 == fi - 1 or (pos == fi and fi - 1 < len(xs_without)):
                # The merged segment IS the segment we're splitting
                area_change = area_new - current_local_area
            else:
                # Different segment
                area_change = (area_merged - current_local_area) + (area_new - area_old_seg)

            # Also check gap constraint
            max_gap_new = max(h_new_left, h_new_right)
            if pos - 1 == fi - 1 or pos == fi:
                pass  # the merged segment is being split, so gap decreases
            else:
                if h_merged > 0.05:
                    continue  # removing the point creates a gap > max_gap

            gain = -area_change  # positive gain = score improvement
            if gain > best_gain:
                best_gain = gain
                best_cand_idx = ci
                best_insert_pos = pos

        if best_cand_idx >= 0:
            # Apply the reinsertion
            cx = cand_xs[best_cand_idx]
            cy = cand_ys[best_cand_idx]

            # Remove old point and insert new
            full_xs = np.delete(full_xs, fi)
            full_ys = np.delete(full_ys, fi)
            ins_pos = np.searchsorted(full_xs, cx)
            full_xs = np.insert(full_xs, ins_pos, cx)
            full_ys = np.insert(full_ys, ins_pos, cy)

            n_improved += 1
            if verbose and n_improved <= 5:
                new_score = total_score(full_xs[1:-1], full_ys[1:-1])
                print(f"  point {point_idx}: gain={best_gain:.2e} "
                      f"score={new_score:.16f}")

    # Extract inner points
    new_xs = full_xs[1:-1].copy()
    new_ys = full_ys[1:-1].copy()
    new_score = total_score(new_xs, new_ys)
    return new_xs, new_ys, new_score, n_improved


def optimized_reinsertion(xs, ys, cand_xs, cand_ys, max_sweeps=50):
    """Run reinsertion sweeps until convergence."""
    best_score = total_score(xs, ys)
    best_xs = xs.copy()
    best_ys = ys.copy()

    for sweep in range(max_sweeps):
        xs_new, ys_new, score_new, n_improved = reinsertion_sweep(
            best_xs, best_ys, cand_xs, cand_ys, verbose=(sweep == 0))
        print(f"Sweep {sweep}: score={score_new:.16f} improved={n_improved} "
              f"Δ={score_new - best_score:.2e}")

        if score_new > best_score:
            best_score = score_new
            best_xs = xs_new
            best_ys = ys_new
        else:
            print("Converged (no improvement)")
            break

    return best_xs, best_ys, best_score


def main():
    print("Loading best solution...")
    with open(SOLUTION_PATH) as f:
        sol = json.load(f)
    w = np.array(sol["weights"])
    baseline = compute_score(w)
    print(f"Baseline score: {baseline:.16f}")

    # Extract (x, y) pairs
    xs_list = []
    ys_list = []
    for row in w:
        row = row / row.sum()
        x, y = compute_densities(row)
        xs_list.append(x)
        ys_list.append(y)

    order = np.argsort(xs_list)
    xs = np.array([xs_list[i] for i in order])
    ys = np.array([ys_list[i] for i in order])

    # Build candidate table
    print(f"Building {N_CANDIDATES} candidate positions...")
    cand_xs, cand_ys = build_candidate_table(N_CANDIDATES)

    # Also add candidates near scallop boundaries (finer resolution)
    extra_xs = []
    extra_ys = []
    for k in range(2, 21):
        x_boundary = 1 - 1 / k
        for offset in np.linspace(-0.001, 0.001, 201):
            x = x_boundary + offset
            if 0.001 < x < 0.949:
                p = turan_row(x)
                _, y = compute_densities(p)
                extra_xs.append(x)
                extra_ys.append(y)
    cand_xs = np.concatenate([cand_xs, extra_xs])
    cand_ys = np.concatenate([cand_ys, extra_ys])
    print(f"Total candidates: {len(cand_xs)}")

    # Run reinsertion optimization
    print("\n=== Reinsertion optimization ===")
    best_xs, best_ys, best_score = optimized_reinsertion(
        xs, ys, cand_xs, cand_ys, max_sweeps=20)

    print(f"\n=== RESULT ===")
    print(f"Baseline:  {baseline:.16f}")
    print(f"Best:      {best_score:.16f}")
    print(f"Δ:         {best_score - baseline:.2e}")

    if best_score > baseline:
        # Build weight matrix
        w_new = np.zeros((len(best_xs), 20))
        for i, x in enumerate(best_xs):
            w_new[i] = turan_row(np.clip(x, 1e-14, 0.95))
        verify = compute_score(w_new)
        print(f"Verified:  {verify:.16f}")

        out = {"weights": w_new.tolist()}
        out_path = RESULTS_DIR / "solution-reinsertion.json"
        with open(out_path, "w") as f:
            json.dump(out, f)
        print(f"Saved to {out_path}")

        # Check vs arena
        print(f"Score:     {verify:.16f}")
    else:
        print("No improvement found.")


if __name__ == "__main__":
    main()
