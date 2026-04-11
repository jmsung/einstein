"""Structure-aware simulated annealing for Heilbronn Convex P16.

Unlike previous multistart+SLSQP approaches, this uses:
1. Custom SA with moves that preserve hull/interior structure
2. Adaptive move operators (hull slide, interior perturbation, point swap)
3. Very slow cooling over long runs
4. Multiple independent restarts from diverse initial conditions
5. Greedy hill-climb phases between SA phases

Key insight: SLSQP converges to the nearest local max. SA can escape local maxima.

Usage:
    uv run python scripts/heilbronn_convex/sa_attack.py --time 1800 --seed 7
"""

from __future__ import annotations

import argparse
import json
import math
import time
from pathlib import Path

import numpy as np
from scipy.spatial import ConvexHull

from einstein.heilbronn_convex import arena_score, fast_score, active_triples, hull_vertex_indices
from einstein.heilbronn_convex.optimizer import polish_slsqp

RESULTS_DIR = Path("results/problem-16-heilbronn-convex")

ARENA_BEST = 0.02783558051755368259
SUBMIT_THRESHOLD = 0.02783558045993943589 + 1e-9


def load_reference():
    """Load reference solution from results directory."""
    data = json.loads((RESULTS_DIR / "reference_solution.json").read_text())
    return np.array(data["points"], dtype=np.float64)


def load_all_top():
    """Load top solutions as warm starts."""
    solutions = []
    for f in RESULTS_DIR.glob("*.json"):
        try:
            data = json.loads(f.read_text())
            pts = np.array(data["points"], dtype=np.float64)
            if pts.shape == (14, 2):
                sc = fast_score(pts)
                if sc > 0.027:
                    solutions.append((pts, sc, f.stem))
        except Exception:
            continue
    solutions.sort(key=lambda x: -x[1])
    return solutions


def sa_move(pts, rng, temp, move_type="auto"):
    """Generate a neighbor configuration with structure-aware moves."""
    new_pts = pts.copy()
    hv = set(hull_vertex_indices(pts))
    interior = [i for i in range(14) if i not in hv]

    if move_type == "auto":
        r = rng.random()
        if r < 0.3:
            move_type = "interior_perturb"
        elif r < 0.5:
            move_type = "hull_slide"
        elif r < 0.65:
            move_type = "point_swap"
        elif r < 0.8:
            move_type = "global_perturb"
        elif r < 0.9:
            move_type = "rotate_subset"
        else:
            move_type = "mirror_point"

    scale = temp * 0.5  # Scale moves with temperature

    if move_type == "interior_perturb" and interior:
        # Move one interior point
        i = rng.choice(interior)
        new_pts[i] += rng.normal(0, scale, 2)

    elif move_type == "hull_slide":
        # Slide a hull vertex along the hull boundary
        hv_list = sorted(hv)
        i = rng.choice(hv_list)
        # Move along tangent to hull
        idx = hv_list.index(i)
        j = hv_list[(idx + 1) % len(hv_list)]
        k = hv_list[(idx - 1) % len(hv_list)]
        tangent = pts[j] - pts[k]
        tangent = tangent / (np.linalg.norm(tangent) + 1e-15)
        new_pts[i] += tangent * rng.normal(0, scale)
        # Also add small normal perturbation
        normal = np.array([-tangent[1], tangent[0]])
        new_pts[i] += normal * rng.normal(0, scale * 0.3)

    elif move_type == "point_swap":
        # Swap positions of two random points
        i, j = rng.choice(14, 2, replace=False)
        new_pts[i], new_pts[j] = pts[j].copy(), pts[i].copy()
        # Add small perturbation after swap
        new_pts[i] += rng.normal(0, scale * 0.1, 2)
        new_pts[j] += rng.normal(0, scale * 0.1, 2)

    elif move_type == "global_perturb":
        # Perturb all points slightly
        new_pts += rng.normal(0, scale * 0.3, (14, 2))

    elif move_type == "rotate_subset":
        # Rotate a random subset of points around centroid
        n_rotate = rng.integers(3, 10)
        subset = rng.choice(14, n_rotate, replace=False)
        center = pts[subset].mean(axis=0)
        angle = rng.normal(0, scale * 2)
        c, s = np.cos(angle), np.sin(angle)
        R = np.array([[c, -s], [s, c]])
        for i in subset:
            new_pts[i] = center + R @ (pts[i] - center)

    elif move_type == "mirror_point":
        # Mirror a random point through the centroid
        i = rng.integers(14)
        center = pts.mean(axis=0)
        direction = center - pts[i]
        alpha = rng.uniform(0.5, 2.0)
        new_pts[i] = pts[i] + alpha * direction

    return new_pts


def simulated_annealing(
    pts_init, rng, max_iter=500_000, t_start=0.1, t_end=1e-8,
    callback=None
):
    """Custom SA with structure-aware moves and slow geometric cooling."""
    pts = pts_init.copy()
    score = fast_score(pts)
    best_pts = pts.copy()
    best_score = score

    alpha = (t_end / t_start) ** (1.0 / max_iter)  # Geometric cooling

    accepts = 0
    improves = 0

    for step in range(max_iter):
        temp = t_start * (alpha ** step)
        new_pts = sa_move(pts, rng, temp)
        new_score = fast_score(new_pts)

        if not np.isfinite(new_score) or new_score < 0:
            continue

        delta = new_score - score
        if delta > 0 or rng.random() < math.exp(delta / (temp + 1e-20)):
            pts = new_pts
            score = new_score
            accepts += 1
            if score > best_score:
                best_score = score
                best_pts = pts.copy()
                improves += 1

        if callback and step % 50000 == 0 and step > 0:
            callback(step, best_score, score, temp, accepts, improves)

    return best_pts, best_score


def greedy_hillclimb(pts, rng, n_steps=10000, step_size=1e-5):
    """Greedy coordinate-wise hill climbing."""
    pts = pts.copy()
    score = fast_score(pts)

    for _ in range(n_steps):
        i = rng.integers(14)
        d = rng.integers(2)
        delta = rng.choice([-1, 1]) * step_size
        pts[i, d] += delta
        new_score = fast_score(pts)
        if new_score > score:
            score = new_score
        else:
            pts[i, d] -= delta

    return pts, score


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--time", type=float, default=1800.0)
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--out", type=str, default="/tmp/heilbronn_sa_attack.json")
    args = parser.parse_args()

    rng = np.random.default_rng(args.seed)
    start = time.time()

    print(f"Target: {SUBMIT_THRESHOLD:.20f}")
    print(f"Arena #1: {ARENA_BEST:.20f}")
    print(f"Gap to threshold: {SUBMIT_THRESHOLD - ARENA_BEST:.3e}")

    top_solutions = load_all_top()
    print(f"Loaded {len(top_solutions)} warm-start solutions")

    best_score = ARENA_BEST
    best_pts = load_reference()
    all_records = []

    def status_callback(step, best, current, temp, acc, imp):
        elapsed = time.time() - start
        print(f"    step={step:7d}  best={best:.16f}  cur={current:.16f}  "
              f"T={temp:.2e}  acc={acc}  imp={imp}  [{elapsed:.0f}s]")

    round_num = 0
    while time.time() - start < args.time:
        round_num += 1
        elapsed = time.time() - start
        remaining = args.time - elapsed

        # Choose starting point
        r = rng.random()
        if r < 0.3 and top_solutions:
            # Warm start from a known solution with perturbation
            idx = rng.integers(0, min(5, len(top_solutions)))
            pts0 = top_solutions[idx][0].copy()
            scale = rng.choice([1e-3, 5e-3, 1e-2, 3e-2, 0.1])
            pts0 += rng.normal(0, scale, pts0.shape)
            init_type = f"warm-{scale:.0e}"
        elif r < 0.5:
            # Crossover between two solutions
            if len(top_solutions) >= 2:
                ia = rng.integers(0, min(5, len(top_solutions)))
                ib = rng.integers(0, len(top_solutions))
                alpha = rng.uniform(0.2, 0.8)
                pts0 = alpha * top_solutions[ia][0] + (1 - alpha) * top_solutions[ib][0]
                pts0 += rng.normal(0, 0.01, pts0.shape)
                init_type = f"xover-{alpha:.2f}"
            else:
                pts0 = rng.uniform(-1, 1, (14, 2))
                init_type = "random"
        elif r < 0.7:
            # Random 10+4
            angles = np.sort(rng.uniform(0, 2 * np.pi, 10))
            radii = rng.uniform(0.8, 1.2, 10)
            hull = np.column_stack([radii * np.cos(angles), radii * np.sin(angles)])
            interior = rng.uniform(-0.5, 0.5, (4, 2))
            pts0 = np.vstack([hull, interior])
            init_type = "10p4-random"
        elif r < 0.85:
            # Non-standard hull sizes
            n_hull = rng.choice([7, 8, 9, 11, 12, 13])
            n_int = 14 - n_hull
            angles = np.sort(rng.uniform(0, 2 * np.pi, n_hull))
            radii = rng.uniform(0.8, 1.2, n_hull)
            hull = np.column_stack([radii * np.cos(angles), radii * np.sin(angles)])
            if n_int > 0:
                interior = rng.uniform(-0.5, 0.5, (n_int, 2))
                pts0 = np.vstack([hull, interior])
            else:
                pts0 = hull
            init_type = f"hull-{n_hull}+{n_int}"
        else:
            # Fully random
            pts0 = rng.uniform(-1, 1, (14, 2))
            init_type = "random"

        # Adaptive SA parameters based on remaining time
        sa_time = min(remaining * 0.15, 120)  # Cap each SA run
        n_iter = max(50000, int(sa_time * 5000))  # ~5000 iter/sec estimate

        t_start = rng.choice([0.01, 0.05, 0.1, 0.5, 1.0])
        t_end = rng.choice([1e-8, 1e-10, 1e-12])

        print(f"\nRound {round_num} [{elapsed:.0f}s]: {init_type}  "
              f"SA(iter={n_iter}, T={t_start:.2e}→{t_end:.2e})")

        # Run SA
        sa_pts, sa_score = simulated_annealing(
            pts0, rng, max_iter=n_iter,
            t_start=t_start, t_end=t_end,
            callback=status_callback
        )

        # Polish with SLSQP
        polished, pol_score = polish_slsqp(sa_pts, max_iter=500)

        # Greedy hill-climb refinement
        final, final_score = greedy_hillclimb(polished, rng, n_steps=5000, step_size=1e-7)
        final_arena = arena_score(final)

        hv = hull_vertex_indices(final)
        at = active_triples(final, rel_tol=1e-9)

        print(f"  → SA={sa_score:.12f}  polish={pol_score:.16f}  "
              f"final={final_arena:.16f}  hull={len(hv)}+{14-len(hv)}  active={len(at)}")

        all_records.append({
            "round": round_num,
            "init_type": init_type,
            "sa_score": sa_score,
            "polish_score": pol_score,
            "final_score": final_arena,
            "n_hull": len(hv),
            "active": len(at),
        })

        if final_arena > best_score:
            best_score = final_arena
            best_pts = final.copy()
            delta = final_arena - ARENA_BEST
            print(f"\n*** NEW BEST! {final_arena:.20f}  delta={delta:+.3e}")
            if final_arena > SUBMIT_THRESHOLD:
                print(f"*** ABOVE SUBMIT THRESHOLD! ***")
                out = {"points": final.tolist(), "score": final_arena, "round": round_num}
                Path("/tmp/heilbronn_sa_candidate.json").write_text(json.dumps(out, indent=2))

    # Summary
    elapsed = time.time() - start
    print(f"\n{'='*60}")
    print(f"SA ATTACK SUMMARY after {elapsed:.1f}s, {round_num} rounds")
    print(f"{'='*60}")
    print(f"Best score: {best_score:.20f}")
    print(f"Arena #1:   {ARENA_BEST:.20f}")
    print(f"Threshold:  {SUBMIT_THRESHOLD:.20f}")
    if best_score > SUBMIT_THRESHOLD:
        print("*** SUBMITTABLE! ***")
    else:
        print(f"Gap to threshold: {SUBMIT_THRESHOLD - best_score:.3e}")

    # Save
    top_records = sorted(all_records, key=lambda r: -r["final_score"])[:20]
    out = {
        "best_score": best_score,
        "best_pts": best_pts.tolist(),
        "arena_best": ARENA_BEST,
        "submit_threshold": SUBMIT_THRESHOLD,
        "above_threshold": best_score > SUBMIT_THRESHOLD,
        "rounds": round_num,
        "elapsed_s": elapsed,
        "top_records": top_records,
    }
    Path(args.out).write_text(json.dumps(out, indent=2))
    print(f"Results saved to {args.out}")


if __name__ == "__main__":
    main()
