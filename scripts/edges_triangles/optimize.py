"""Optimizer for Edges vs Triangles (Problem 13).

Full pipeline: greedy → CD → fine CD → GS → redistribution → basin-hopping → SA → polish.
Use --polish to skip the initial pipeline and polish an existing solution.
"""

import json
import shutil
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import minimize_scalar

from einstein.edges_triangles.evaluator import compute_densities, compute_score, turan_row

MB_SOLUTIONS = Path.home() / "projects/workbench/memory-bank/einstein/docs/problem-13-edges-triangles/solutions"


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


def _recompute_ys(xs: np.ndarray) -> np.ndarray:
    """Recompute y-values for all points from Turán construction."""
    ys = np.empty_like(xs)
    ys[0], ys[-1] = 0.0, 1.0
    for i in range(1, len(xs) - 1):
        p = turan_row(np.clip(xs[i], 0.0, 0.95))
        _, ys[i] = compute_densities(p)
    return ys


# ---------------------------------------------------------------------------
# Phase functions
# ---------------------------------------------------------------------------

def greedy_insert(xs: list, ys: list, n_target: int, n_candidates: int = 50):
    """Greedily insert points in [0.5, 0.95] to minimize area."""
    while len(xs) - 2 < n_target:
        best_reduction, best_idx, best_x, best_y = -1e-20, -1, 0.0, 0.0
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
                reduction = old_area - (
                    _segment_area(ys[i], y_new, x_new - xs[i])
                    + _segment_area(y_new, ys[i + 1], xs[i + 1] - x_new)
                )
                if reduction > best_reduction:
                    best_reduction, best_idx, best_x, best_y = reduction, i + 1, x_new, y_new
        if best_idx < 0 or best_reduction <= 0:
            break
        xs.insert(best_idx, best_x)
        ys.insert(best_idx, best_y)
        if (len(xs) - 2) % 100 == 0:
            print(f"  {len(xs)-2} pts: {_score_from_arrays(np.array(xs), np.array(ys)):.10f}")


def coordinate_descent(
    xs: np.ndarray, ys: np.ndarray, n_iters: int = 20,
    step_fracs: list[float] | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    """Optimize x-positions via coordinate descent."""
    xs, ys = xs.copy(), ys.copy()
    if step_fracs is None:
        step_fracs = [0.4, 0.15, 0.05, 0.015, 0.005]
    for it in range(n_iters):
        improved = 0
        for frac in step_fracs:
            for i in range(1, len(xs) - 1):
                if xs[i] < 0.49:
                    continue
                h_left, h_right = xs[i] - xs[i - 1], xs[i + 1] - xs[i]
                old_area = _segment_area(ys[i - 1], ys[i], h_left) + _segment_area(ys[i], ys[i + 1], h_right)
                step = min(h_left, h_right) * frac
                for dx in [-step, step]:
                    x_new = xs[i] + dx
                    if x_new <= xs[i - 1] + 1e-15 or x_new >= xs[i + 1] - 1e-15 or x_new > 0.95:
                        continue
                    p = turan_row(x_new)
                    _, y_new = compute_densities(p)
                    new_area = _segment_area(ys[i - 1], y_new, x_new - xs[i - 1]) + _segment_area(y_new, ys[i + 1], xs[i + 1] - x_new)
                    if new_area < old_area - 1e-18:
                        xs[i], ys[i], old_area = x_new, y_new, new_area
                        improved += 1
        score = _score_from_arrays(xs, ys)
        print(f"  CD iter {it}: {score:.10f} ({improved} moves)")
        if improved == 0:
            break
    return xs, ys


def golden_section_sweep(
    xs: np.ndarray, ys: np.ndarray, n_sweeps: int = 200,
) -> tuple[np.ndarray, np.ndarray]:
    """Optimize each point via golden-section line search."""
    xs, ys = xs.copy(), ys.copy()
    for sweep in range(n_sweeps):
        improved = 0
        for i in range(1, len(xs) - 1):
            if xs[i] < 0.49:
                continue
            lo = max(xs[i - 1] + 1e-15, 0.0)
            hi = min(xs[i + 1] - 1e-15, 0.95)
            if lo >= hi:
                continue

            def local_area(x_new):
                p = turan_row(x_new)
                _, y_new = compute_densities(p)
                return _segment_area(ys[i - 1], y_new, x_new - xs[i - 1]) + _segment_area(y_new, ys[i + 1], xs[i + 1] - x_new)

            old_area = local_area(xs[i])
            res = minimize_scalar(local_area, bounds=(lo, hi), method="bounded", options={"xatol": 1e-14, "maxiter": 200})
            if res.fun < old_area - 1e-18:
                xs[i] = res.x
                _, ys[i] = compute_densities(turan_row(res.x))
                improved += 1
        if sweep % 50 == 0 or improved == 0:
            print(f"  GS sweep {sweep}: {_score_from_arrays(xs, ys):.10f} ({improved} moves)")
        if improved == 0:
            break
    return xs, ys


def redistribute(
    xs: np.ndarray, ys: np.ndarray, windows: list[int] | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    """Redistribute points in sliding windows (uniform spacing)."""
    xs, ys = xs.copy(), ys.copy()
    if windows is None:
        windows = [5, 10, 20, 30, 50, 100]
    first_multi = next(i for i in range(1, len(xs) - 1) if xs[i] >= 0.49)
    for w in windows:
        improved = 0
        for start in range(first_multi, len(xs) - 1 - w):
            end = start + w
            if end >= len(xs) - 1:
                break
            old_area = sum(_segment_area(ys[j], ys[j + 1], xs[j + 1] - xs[j]) for j in range(start, end))
            n_inner = end - start - 1
            if n_inner <= 0:
                continue
            new_xs = np.linspace(xs[start], xs[end], n_inner + 2)[1:-1]
            new_ys = np.array([compute_densities(turan_row(np.clip(x, 0.0, 0.95)))[1] for x in new_xs])
            all_xs = np.concatenate([[xs[start]], new_xs, [xs[end]]])
            all_ys = np.concatenate([[ys[start]], new_ys, [ys[end]]])
            new_area = sum(_segment_area(all_ys[j], all_ys[j + 1], all_xs[j + 1] - all_xs[j]) for j in range(len(all_xs) - 1))
            if new_area < old_area - 1e-18:
                xs[start + 1:end], ys[start + 1:end] = new_xs, new_ys
                improved += 1
        print(f"  Redist w={w}: {_score_from_arrays(xs, ys):.10f} ({improved} moves)")
    return xs, ys


def basin_hopping_optimize(
    xs: np.ndarray, ys: np.ndarray, n_iter: int = 50, temp: float = 1e-8,
    seed: int = 777, noise_max: float = 0.1, noise_min: float = 0.01,
) -> tuple[np.ndarray, np.ndarray]:
    """Basin-hopping: random global jumps in gap-space + GS local minimizer."""
    best_xs, best_ys = xs.copy(), ys.copy()
    best_score = _score_from_arrays(best_xs, best_ys)
    rng = np.random.default_rng(seed)
    first_multi = next(i for i in range(1, len(xs) - 1) if xs[i] >= 0.49)

    for it in range(n_iter):
        xs_trial, ys_trial = best_xs.copy(), best_ys.copy()

        # Perturb via gap-space: add noise to log-gaps
        multi_xs = xs_trial[first_multi:-1].copy()
        all_sorted = np.concatenate([[xs_trial[first_multi - 1]], multi_xs, [xs_trial[-1]]])
        log_gaps = np.log(np.maximum(np.diff(all_sorted), 1e-15))

        noise_scale = noise_max * (1 - it / n_iter) + noise_min
        log_gaps += rng.normal(0, noise_scale, size=len(log_gaps))

        ez = np.exp(log_gaps)
        new_gaps = ez / ez.sum() * (all_sorted[-1] - all_sorted[0])
        new_multi = np.clip(all_sorted[0] + np.cumsum(new_gaps)[:-1], 0.5, 0.95)

        xs_trial[first_multi:first_multi + len(new_multi)] = np.sort(new_multi)
        ys_trial = _recompute_ys(xs_trial)

        # Local minimizer
        xs_trial, ys_trial = golden_section_sweep(xs_trial, ys_trial, n_sweeps=30)
        trial_score = _score_from_arrays(xs_trial, ys_trial)

        delta = trial_score - best_score
        if delta > 0 or (temp > 0 and rng.random() < np.exp(delta / temp)):
            best_xs, best_ys = xs_trial.copy(), ys_trial.copy()
            if trial_score > best_score:
                best_score = trial_score
                print(f"  BH iter {it}: {best_score:.10f} (NEW BEST)")
            else:
                print(f"  BH iter {it}: {trial_score:.10f} (accepted worse)")
        elif it % 10 == 0:
            print(f"  BH iter {it}: {trial_score:.10f} (rejected)")

    return best_xs, best_ys


def sa_perturb(
    xs: np.ndarray, ys: np.ndarray,
    n_rounds: int = 20, n_perturbations: int = 50,
    seed: int = 42, block_size: int = 1,
) -> tuple[np.ndarray, np.ndarray]:
    """SA-style perturbation: perturb random blocks, re-optimize, keep best."""
    best_xs, best_ys = xs.copy(), ys.copy()
    best_score = _score_from_arrays(best_xs, best_ys)
    rng = np.random.default_rng(seed)
    first_multi = next(i for i in range(1, len(xs) - 1) if xs[i] >= 0.49)
    last_multi = len(xs) - 2

    for rnd in range(n_rounds):
        xs_trial, ys_trial = best_xs.copy(), best_ys.copy()
        for _ in range(n_perturbations):
            i_start = rng.integers(first_multi, last_multi + 1)
            scale_frac = rng.uniform(0.01, 0.3)
            for i in range(i_start, min(i_start + block_size, last_multi + 1)):
                h = min(xs_trial[i] - xs_trial[i - 1], xs_trial[i + 1] - xs_trial[i])
                x_new = xs_trial[i] + rng.normal(0, h * scale_frac)
                if xs_trial[i - 1] + 1e-15 < x_new < xs_trial[i + 1] - 1e-15 and 0.5 <= x_new <= 0.95:
                    xs_trial[i] = x_new
                    _, ys_trial[i] = compute_densities(turan_row(x_new))

        xs_trial, ys_trial = golden_section_sweep(xs_trial, ys_trial, n_sweeps=50)
        trial_score = _score_from_arrays(xs_trial, ys_trial)
        if trial_score > best_score:
            best_xs, best_ys, best_score = xs_trial, ys_trial, trial_score
            print(f"  SA round {rnd}: {best_score:.10f} (IMPROVED)")
        elif rnd % 10 == 0:
            print(f"  SA round {rnd}: {trial_score:.10f} (no improvement)")
    return best_xs, best_ys


# ---------------------------------------------------------------------------
# Solution I/O
# ---------------------------------------------------------------------------

def load_solution(path: Path) -> tuple[np.ndarray, np.ndarray]:
    """Load solution.json → (xs_with_boundary, ys_with_boundary)."""
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


def save_solution(xs_arr: np.ndarray, ys_arr: np.ndarray, out_dir: Path) -> Path:
    """Save solution and auto-backup to MB."""
    data_xs = xs_arr[1:-1]
    weights = np.array([turan_row(np.clip(x, 0.0, 0.95)) for x in data_xs])
    score = compute_score(weights)

    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "solution.json"
    with open(out_path, "w") as f:
        json.dump({"weights": weights.tolist()}, f)
    print(f"Saved to {out_path}")
    print(f"Verified: {score:.10f}")

    # Auto-backup to MB
    MB_SOLUTIONS.mkdir(parents=True, exist_ok=True)
    mb_path = MB_SOLUTIONS / f"solution-{score:.8f}.json"
    shutil.copy2(out_path, mb_path)
    # Update best symlink
    best_path = MB_SOLUTIONS / "solution-best.json"
    shutil.copy2(out_path, best_path)
    print(f"Backed up to MB: {mb_path.name}")

    return out_path


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def full_pipeline() -> tuple[np.ndarray, np.ndarray]:
    """Run from scratch: seed → greedy → CD → fine CD → GS → redist."""
    print("=== Full Pipeline ===\n")
    bipartite_xs = np.linspace(0.05, 0.5, 11)
    seed_multi = set()
    for k in range(2, 21):
        x = 1.0 - 1.0 / k
        if 0.5 <= x <= 0.95:
            seed_multi.add(x)
    bp = sorted(seed_multi)
    for i in range(len(bp) - 1):
        seed_multi.add((bp[i] + bp[i + 1]) / 2)
    seed_multi.add(0.95)

    all_xs = sorted(list(bipartite_xs) + sorted(seed_multi))
    all_ys = [compute_densities(turan_row(min(x, 0.95)))[1] for x in all_xs]
    xs, ys = [0.0] + all_xs + [1.0], [0.0] + all_ys + [1.0]
    print(f"Seed: {len(all_xs)} pts")

    print("\nPhase 1: Greedy insertion...")
    greedy_insert(xs, ys, n_target=500, n_candidates=50)

    print("\nPhase 2: Coarse CD...")
    xa, ya = np.array(xs), np.array(ys)
    xa, ya = coordinate_descent(xa, ya, n_iters=20)

    print("\nPhase 3: Ultra-fine CD...")
    xa, ya = coordinate_descent(xa, ya, n_iters=100, step_fracs=[0.001, 0.0003, 0.0001, 0.00003, 0.00001])

    print("\nPhase 4: Golden section...")
    xa, ya = golden_section_sweep(xa, ya, n_sweeps=200)

    for c in range(3):
        print(f"\nPhase 5.{c}: Redistribute + GS...")
        xa, ya = redistribute(xa, ya)
        xa, ya = golden_section_sweep(xa, ya, n_sweeps=100)

    return xa, ya


def main():
    sol_path = Path("results/problem-13-edges-triangles/solution.json")
    polish = "--polish" in sys.argv

    if polish and sol_path.exists():
        print("=== Polish Mode ===\n")
        xs, ys = load_solution(sol_path)
        print(f"Loaded: {_score_from_arrays(xs, ys):.10f} ({len(xs)-2} pts)")
    else:
        xs, ys = full_pipeline()

    score = _score_from_arrays(xs, ys)
    print(f"\n=== Advanced optimization from {score:.10f} ===")

    # Basin-hopping (the breakthrough technique)
    print("\nPhase 6: Basin-hopping...")
    xs_bh, ys_bh = basin_hopping_optimize(xs, ys, n_iter=50, temp=1e-8)
    xs_bh, ys_bh = golden_section_sweep(xs_bh, ys_bh, n_sweeps=100)
    score_bh = _score_from_arrays(xs_bh, ys_bh)
    print(f"BH result: {score_bh:.10f}")

    best_xs, best_ys = (xs_bh, ys_bh) if score_bh > score else (xs.copy(), ys.copy())
    best_score = max(score, score_bh)

    # SA mega-cycles on best result
    print(f"\nPhase 7: SA mega-cycles from {best_score:.10f}...")
    for mega in range(5):
        print(f"\n=== Mega {mega} ===")
        xm, ym = sa_perturb(best_xs, best_ys, n_rounds=20, n_perturbations=100, seed=mega * 13 + 7, block_size=5)
        for _ in range(2):
            xm, ym = redistribute(xm, ym)
            xm, ym = golden_section_sweep(xm, ym, n_sweeps=100)
        xm, ym = coordinate_descent(xm, ym, n_iters=20, step_fracs=[0.0001, 0.00003, 0.00001, 0.000003, 0.000001])
        sm = _score_from_arrays(xm, ym)
        if sm > best_score:
            best_xs, best_ys, best_score = xm.copy(), ym.copy(), sm
            print(f"  Mega {mega}: {best_score:.10f} (NEW BEST)")
        else:
            print(f"  Mega {mega}: {sm:.10f} (no improvement)")

    # Final
    area = sum(_segment_area(best_ys[i], best_ys[i + 1], best_xs[i + 1] - best_xs[i]) for i in range(len(best_xs) - 1))
    gap = max(best_xs[i + 1] - best_xs[i] for i in range(len(best_xs) - 1))
    print(f"\nFinal: score={best_score:.10f} (area={area:.10f}, gap={gap:.6f})")

    save_solution(best_xs, best_ys, Path("results/problem-13-edges-triangles"))


if __name__ == "__main__":
    main()
