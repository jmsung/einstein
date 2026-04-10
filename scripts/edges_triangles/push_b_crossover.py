"""B. Crossover / recombination of polished solutions.

Take multipartite x-positions from multiple polished solutions, merge into a
super-set, then greedily prune back to 489 multipartite points keeping the
configuration with lowest area. Then polish.
"""

import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))

from einstein.edges_triangles.evaluator import compute_score, compute_densities, turan_row  # noqa: E402
from optimize import (  # noqa: E402
    _score_from_arrays,
    _segment_area,
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
    print("=== B. Crossover recombination ===\n")

    # Load current best as one source
    current_best_path = Path("results/problem-13-edges-triangles/solution.json")
    cur_xs, cur_ys = load_to_xy(current_best_path)
    current_best_score = _score_from_arrays(cur_xs, cur_ys)
    sources = [current_best_path]

    print("Loading polished solutions...")
    all_multi_xs = []
    for src in sources:
        if src.exists():
            xs, ys = load_to_xy(src)
            multi = xs[(xs > 0.49) & (xs < 0.96)]
            print(f"  {src.name}: {len(multi)} multipartite points")
            all_multi_xs.append(multi)

    # Also fetch additional ranks from the leaderboard
    import urllib.request
    sys.path.insert(0, "scripts")
    from check_submission import API_URL, load_api_key
    api_key = load_api_key()
    req = urllib.request.Request(
        f'{API_URL}/solutions/best?problem_id=13&limit=5',
        headers={'Authorization': f'Bearer {api_key}'},
    )
    with urllib.request.urlopen(req) as resp:
        sols = json.loads(resp.read())

    # rank3 warm-start
    rank3 = sols[2]
    w3 = np.array(rank3['data']['weights'], dtype=np.float64)
    w3 = np.maximum(w3, 0)
    w3 /= w3.sum(axis=1, keepdims=True)
    xs3 = np.sort(1 - np.sum(w3**2, axis=1))
    multi3 = xs3[xs3 > 0.49]
    print(f"  rank3 raw: {len(multi3)} multipartite points")
    all_multi_xs.append(multi3)

    # rank4 warm-start
    rank4 = sols[3]
    w4 = np.array(rank4['data']['weights'], dtype=np.float64)
    w4 = np.maximum(w4, 0)
    w4 /= w4.sum(axis=1, keepdims=True)
    xs4 = np.sort(1 - np.sum(w4**2, axis=1))
    multi4 = xs4[xs4 > 0.49]
    print(f"  rank4 raw: {len(multi4)} multipartite points")
    all_multi_xs.append(multi4)

    # Merge all into a super-set
    super_set = np.unique(np.concatenate(all_multi_xs))
    print(f"\nMerged super-set: {len(super_set)} unique multipartite points")

    # Build initial structure: 11 bipartite + super-set + boundaries
    bipartite = np.linspace(0.05, 0.5, 11)
    all_data = np.sort(np.concatenate([bipartite, super_set]))
    xs = np.concatenate([[0.0], all_data, [1.0]])
    ys = np.empty_like(xs)
    ys[0], ys[-1] = 0.0, 1.0
    for i in range(1, len(xs) - 1):
        _, ys[i] = compute_densities(turan_row(np.clip(xs[i], 0.0, 0.95)))

    initial_super = _score_from_arrays(xs, ys)
    print(f"Super-set initial score: {initial_super:.14f}")
    print(f"  ({len(xs)-2} data points — too many, need to prune to 500)")

    # Greedy prune: remove the point whose removal increases area least
    print("\nGreedy pruning to 500 points...")
    while len(xs) - 2 > 500:
        best_idx = -1
        best_delta = float('inf')
        # Skip bipartite points (xs[i] <= 0.5)
        for i in range(1, len(xs) - 1):
            if xs[i] <= 0.5:
                continue  # don't remove bipartite coverage
            # Compute area before/after removal
            old_left = _segment_area(ys[i - 1], ys[i], xs[i] - xs[i - 1])
            old_right = _segment_area(ys[i], ys[i + 1], xs[i + 1] - xs[i])
            new_combined = _segment_area(ys[i - 1], ys[i + 1], xs[i + 1] - xs[i - 1])
            delta = new_combined - (old_left + old_right)  # positive = worse to remove
            if delta < best_delta:
                best_delta = delta
                best_idx = i
        if best_idx < 0:
            break
        xs = np.delete(xs, best_idx)
        ys = np.delete(ys, best_idx)
        if (len(xs) - 2) % 50 == 0:
            print(f"  {len(xs)-2} pts: {_score_from_arrays(xs, ys):.14f}")

    after_prune = _score_from_arrays(xs, ys)
    print(f"After pruning: {after_prune:.14f}")

    # Polish
    print("\nPolishing pruned configuration...")
    xs, ys = coordinate_descent(xs, ys, n_iters=20)
    xs, ys = coordinate_descent(xs, ys, n_iters=50, step_fracs=[0.001, 0.0003, 0.0001, 0.00003, 0.00001])
    xs, ys = golden_section_sweep(xs, ys, n_sweeps=100)
    for _ in range(2):
        xs, ys = redistribute(xs, ys)
        xs, ys = golden_section_sweep(xs, ys, n_sweeps=80)
    xs, ys = basin_hopping_optimize(xs, ys, n_iter=50, temp=1e-8, seed=999)
    xs, ys = golden_section_sweep(xs, ys, n_sweeps=80)
    for mega in range(3):
        xs, ys = sa_perturb(xs, ys, n_rounds=15, n_perturbations=80, seed=mega * 11 + 5, block_size=5)
        for _ in range(2):
            xs, ys = redistribute(xs, ys)
            xs, ys = golden_section_sweep(xs, ys, n_sweeps=50)
        xs, ys = coordinate_descent(xs, ys, n_iters=15, step_fracs=[0.0001, 0.00003, 0.00001, 0.000003, 0.000001])

    final = _score_from_arrays(xs, ys)
    print(f"\nFINAL crossover: {final:.14f}")
    print(f"vs current best:  {current_best_score:.14f}")
    print(f"Improvement: {final - current_best_score:+.2e}")

    if final > current_best_score:
        data_xs = xs[1:-1]
        weights = np.array([turan_row(np.clip(x, 0.0, 0.95)) for x in data_xs])
        verify = compute_score(weights)
        print(f"Verified: {verify:.14f}")
        out = Path("results/problem-13-edges-triangles/solution-B.json")
        with open(out, "w") as f:
            json.dump({"weights": weights.tolist()}, f)
        print(f"*** NEW RECORD saved to {out} ***")
    else:
        print("No improvement over current best.")


if __name__ == "__main__":
    main()
