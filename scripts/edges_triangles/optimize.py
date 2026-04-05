"""Optimizer for Edges vs Triangles (Problem 13)."""

import json
from pathlib import Path

import numpy as np

from einstein.edges_triangles.evaluator import compute_densities, compute_score, turan_row


def _segment_area(y0: float, y1: float, h: float) -> float:
    """Area under slope-3 interpolated segment."""
    if h <= 0:
        return 0.0
    dy = y1 - y0
    if dy < 0:
        return y1 * h
    elif dy <= 3 * h:
        return -dy**2 / 6 + y1 * h
    else:
        return y0 * h + 1.5 * h**2


def _score_from_arrays(xs: np.ndarray, ys: np.ndarray) -> float:
    """Compute score from sorted xs/ys arrays (including boundary points)."""
    area = 0.0
    max_gap = 0.0
    for i in range(len(xs) - 1):
        h = xs[i + 1] - xs[i]
        if h <= 0:
            continue
        max_gap = max(max_gap, h)
        area += _segment_area(ys[i], ys[i + 1], h)
    return -(area + 10 * max_gap)


def build_solution(data_xs: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Build sorted xs/ys arrays from data x-positions (auto-adds boundary)."""
    rows = []
    ys_data = []
    for x in data_xs:
        p = turan_row(np.clip(x, 0.0, 0.95))
        rows.append(p)
        _, y = compute_densities(p)
        ys_data.append(y)

    order = np.argsort(data_xs)
    data_xs = data_xs[order]
    ys_data = np.array(ys_data)[order]

    xs = np.concatenate([[0.0], data_xs, [1.0]])
    ys = np.concatenate([[0.0], ys_data, [1.0]])
    return xs, ys, np.array(rows)[order]


def greedy_insert(xs: list, ys: list, n_target: int, n_candidates: int = 50):
    """Greedily insert points in [0.5, 0.95] to minimize area."""
    while len(xs) - 2 < n_target:
        best_reduction = -1e-20
        best_idx = -1
        best_x = 0.0
        best_y = 0.0

        for i in range(len(xs) - 1):
            h = xs[i + 1] - xs[i]
            if h < 1e-14:
                continue

            old_area = _segment_area(ys[i], ys[i + 1], h)

            for j in range(1, n_candidates + 1):
                x_new = xs[i] + h * j / (n_candidates + 1)
                if x_new < 0.5 or x_new > 0.95:
                    continue
                p = turan_row(x_new)
                _, y_new = compute_densities(p)

                left_area = _segment_area(ys[i], y_new, x_new - xs[i])
                right_area = _segment_area(y_new, ys[i + 1], xs[i + 1] - x_new)
                reduction = old_area - (left_area + right_area)

                if reduction > best_reduction:
                    best_reduction = reduction
                    best_idx = i + 1
                    best_x = x_new
                    best_y = y_new

        if best_idx < 0 or best_reduction <= 0:
            break

        xs.insert(best_idx, best_x)
        ys.insert(best_idx, best_y)

        if (len(xs) - 2) % 100 == 0:
            score = _score_from_arrays(np.array(xs), np.array(ys))
            print(f"  {len(xs)-2} pts: {score:.10f}")


def coordinate_descent(xs: np.ndarray, ys: np.ndarray, n_iters: int = 20) -> tuple[np.ndarray, np.ndarray]:
    """Optimize x-positions via coordinate descent (points in [0.5, 0.95] only)."""
    xs = xs.copy()
    ys = ys.copy()
    n = len(xs)
    step_fracs = [0.4, 0.15, 0.05, 0.015, 0.005]

    for it in range(n_iters):
        improved = 0
        for frac in step_fracs:
            for i in range(1, n - 1):
                if xs[i] < 0.49:
                    continue  # skip bipartite coverage points

                h_left = xs[i] - xs[i - 1]
                h_right = xs[i + 1] - xs[i]
                old_area = _segment_area(ys[i - 1], ys[i], h_left) + _segment_area(
                    ys[i], ys[i + 1], h_right
                )

                step = min(h_left, h_right) * frac
                for dx in [-step, step]:
                    x_new = xs[i] + dx
                    if x_new <= xs[i - 1] + 1e-15 or x_new >= xs[i + 1] - 1e-15:
                        continue
                    if x_new < 0.0 or x_new > 0.95:
                        continue
                    p = turan_row(x_new)
                    _, y_new = compute_densities(p)

                    new_area = _segment_area(ys[i - 1], y_new, x_new - xs[i - 1]) + _segment_area(
                        y_new, ys[i + 1], xs[i + 1] - x_new
                    )

                    if new_area < old_area - 1e-18:
                        xs[i] = x_new
                        ys[i] = y_new
                        old_area = new_area
                        improved += 1

        score = _score_from_arrays(xs, ys)
        print(f"  CD iter {it}: {score:.10f} ({improved} moves)")
        if improved == 0:
            break

    return xs, ys


def main():
    print("=== Edges vs Triangles Optimizer ===\n")

    # --- Gap coverage: 11 points in [0, 0.5] (bipartite, y=0) ---
    n_bipartite = 11
    bipartite_xs = np.linspace(0.05, 0.5, n_bipartite)

    # --- Seed for multipartite region [0.5, 0.95] ---
    # Turán breakpoints + midpoints
    seed_multi = set()
    for k in range(2, 21):
        x_break = 1.0 - 1.0 / k
        if 0.5 <= x_break <= 0.95:
            seed_multi.add(x_break)
    # Add midpoints between consecutive breakpoints
    breakpoints = sorted(seed_multi)
    for i in range(len(breakpoints) - 1):
        seed_multi.add((breakpoints[i] + breakpoints[i + 1]) / 2)
    seed_multi.add(0.95)
    seed_multi = sorted(seed_multi)

    # Build initial (xs, ys) with bipartite + seed
    all_data_xs = sorted(list(bipartite_xs) + seed_multi)
    all_data_ys = []
    for x in all_data_xs:
        p = turan_row(min(x, 0.95))
        _, y = compute_densities(p)
        all_data_ys.append(y)

    xs = [0.0] + all_data_xs + [1.0]
    ys = [0.0] + all_data_ys + [1.0]

    score = _score_from_arrays(np.array(xs), np.array(ys))
    n_data = len(all_data_xs)
    print(f"Seed: {n_data} data pts, score={score:.10f}")

    # --- Greedy insertion to 500 ---
    print("\nPhase 1: Greedy insertion...")
    greedy_insert(xs, ys, n_target=500, n_candidates=50)
    score = _score_from_arrays(np.array(xs), np.array(ys))
    print(f"After greedy ({len(xs)-2} pts): {score:.10f}")

    # --- Coordinate descent ---
    print("\nPhase 2: Coordinate descent...")
    xs_arr = np.array(xs)
    ys_arr = np.array(ys)
    xs_arr, ys_arr = coordinate_descent(xs_arr, ys_arr, n_iters=20)

    score = _score_from_arrays(xs_arr, ys_arr)
    area_val = sum(
        _segment_area(ys_arr[i], ys_arr[i + 1], xs_arr[i + 1] - xs_arr[i])
        for i in range(len(xs_arr) - 1)
    )
    gap_val = max(xs_arr[i + 1] - xs_arr[i] for i in range(len(xs_arr) - 1))
    print(f"\nFinal: score={score:.10f} (area={area_val:.10f}, gap={gap_val:.6f})")

    # Build weight matrix
    data_xs = xs_arr[1:-1]  # strip boundary
    rows = [turan_row(np.clip(x, 0.0, 0.95)) for x in data_xs]
    weights = np.array(rows)

    verify_score = compute_score(weights)
    print(f"Verified: {verify_score:.10f}")

    # Save
    out_dir = Path("results/problem-13-edges-triangles")
    out_dir.mkdir(parents=True, exist_ok=True)
    solution = {"weights": weights.tolist()}
    out_path = out_dir / "solution.json"
    with open(out_path, "w") as f:
        json.dump(solution, f)
    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    main()
