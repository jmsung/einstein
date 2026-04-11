"""KKT-based algebraic attack on Heilbronn Convex P16.

Approach:
1. Perturb along null space directions with large steps to escape local basin
2. Use Jacobian structure to find descent directions for inactive constraints
3. Try topological surgery: change which triples are active
4. Use interval arithmetic to verify whether higher-scoring configs are possible

Usage:
    uv run python scripts/heilbronn_convex/kkt_attack.py --time 600 --seed 99
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np
from scipy.spatial import ConvexHull

from einstein.heilbronn_convex import (
    arena_score, fast_score, all_triangle_areas, active_triples,
    hull_vertex_indices, min_triangle_area
)
from einstein.heilbronn_convex.evaluator import _TRIPLES
from einstein.heilbronn_convex.optimizer import polish_slsqp

RESULTS_DIR = Path("results/problem-16-heilbronn-convex")

ARENA_BEST = 0.02783558051755368259
SUBMIT_THRESHOLD = 0.02783558045993943589 + 1e-9


def load_solution(name):
    for f in RESULTS_DIR.glob("*.json"):
        if name in f.stem:
            data = json.loads(f.read_text())
            return np.array(data["points"], dtype=np.float64)
    return None


def compute_jacobian(pts, active_idx):
    """Compute Jacobian of active triangle area constraints.

    For each active triple (i,j,k), the area = |cross(pj-pi, pk-pi)|/2.
    The gradient w.r.t. each point coordinate can be computed analytically.
    """
    n_active = len(active_idx)
    J = np.zeros((n_active, 28))  # 28 = 14 * 2

    for row, triple_idx in enumerate(active_idx):
        i, j, k = _TRIPLES[triple_idx]
        pi, pj, pk = pts[i], pts[j], pts[k]

        # area = |pi[0]*(pj[1]-pk[1]) + pj[0]*(pk[1]-pi[1]) + pk[0]*(pi[1]-pj[1])| / 2
        cross = pi[0]*(pj[1]-pk[1]) + pj[0]*(pk[1]-pi[1]) + pk[0]*(pi[1]-pj[1])
        sign = 1.0 if cross >= 0 else -1.0

        # d(area)/d(pi[0]) = sign * (pj[1] - pk[1]) / 2
        J[row, 2*i]     = sign * (pj[1] - pk[1]) / 2
        J[row, 2*i + 1] = sign * (pk[0] - pj[0]) / 2
        J[row, 2*j]     = sign * (pk[1] - pi[1]) / 2
        J[row, 2*j + 1] = sign * (pi[0] - pk[0]) / 2
        J[row, 2*k]     = sign * (pi[1] - pj[1]) / 2
        J[row, 2*k + 1] = sign * (pj[0] - pi[0]) / 2

    return J


def find_active_indices(pts, rel_tol=1e-9):
    """Find indices into _TRIPLES of active constraints."""
    areas = all_triangle_areas(pts)
    min_a = areas.min()
    mask = areas < min_a * (1.0 + rel_tol) + 1e-18
    return np.where(mask)[0]


def null_space_escape(pts, rng, step_sizes, n_trials=1000):
    """Try large steps in the null space of the active Jacobian to escape basin."""
    active_idx = find_active_indices(pts, rel_tol=1e-9)
    J = compute_jacobian(pts, active_idx)

    # SVD to find null space
    U, S, Vt = np.linalg.svd(J, full_matrices=True)
    rank = np.sum(S > 1e-10)
    null_vecs = Vt[rank:]  # Null space basis

    print(f"  Active: {len(active_idx)}, Jacobian rank: {rank}, "
          f"Null dim: {len(null_vecs)}")

    if len(null_vecs) == 0:
        return pts, fast_score(pts)

    best_pts = pts.copy()
    best_score = fast_score(pts)

    for trial in range(n_trials):
        # Random combination of null space vectors with varying scales
        coeffs = rng.normal(0, 1, len(null_vecs))
        direction = coeffs @ null_vecs

        for step in step_sizes:
            new_pts = pts + (direction * step).reshape(14, 2)
            # Polish
            polished, score = polish_slsqp(new_pts, max_iter=300)
            if score > best_score:
                best_score = score
                best_pts = polished.copy()
                print(f"    Null-space escape improvement! score={score:.16f} step={step:.2e}")

    return best_pts, best_score


def active_set_surgery(pts, rng, n_trials=500):
    """Try changing which triples are active by perturbing specific points.

    Strategy: pick a random active triple (i,j,k), move one of the points
    to increase that triangle's area while potentially making a different
    triple the new minimum.
    """
    best_pts = pts.copy()
    best_score = fast_score(pts)

    areas = all_triangle_areas(pts)
    min_a = areas.min()
    active_mask = areas < min_a * (1.0 + 1e-9) + 1e-18
    active_idx = np.where(active_mask)[0]

    for trial in range(n_trials):
        # Pick a random active triple
        triple_idx = rng.choice(active_idx)
        i, j, k = _TRIPLES[triple_idx]

        # Pick one vertex to move
        vertex = rng.choice([i, j, k])

        # Find direction that increases this triple's area
        pi, pj, pk = pts[i], pts[j], pts[k]
        cross = pi[0]*(pj[1]-pk[1]) + pj[0]*(pk[1]-pi[1]) + pk[0]*(pi[1]-pj[1])
        sign = 1.0 if cross >= 0 else -1.0

        # Gradient of area w.r.t. the chosen vertex
        if vertex == i:
            grad = sign * np.array([pj[1]-pk[1], pk[0]-pj[0]]) / 2
        elif vertex == j:
            grad = sign * np.array([pk[1]-pi[1], pi[0]-pk[0]]) / 2
        else:
            grad = sign * np.array([pi[1]-pj[1], pj[0]-pi[0]]) / 2

        # Move in gradient direction with various scales
        for scale in [1e-4, 5e-4, 1e-3, 5e-3, 1e-2, 5e-2]:
            new_pts = pts.copy()
            new_pts[vertex] += grad * scale / (np.linalg.norm(grad) + 1e-15)
            # Also add random perpendicular component
            perp = np.array([-grad[1], grad[0]])
            new_pts[vertex] += perp * rng.normal(0, scale * 0.5) / (np.linalg.norm(perp) + 1e-15)

            polished, score = polish_slsqp(new_pts, max_iter=300)
            if score > best_score:
                best_score = score
                best_pts = polished.copy()
                at = active_triples(best_pts, rel_tol=1e-9)
                print(f"    Surgery improvement! score={score:.16f} "
                      f"scale={scale:.0e} active={len(at)}")

    return best_pts, best_score


def combinatorial_interior_search(pts_hull, rng, n_trials=2000):
    """Fix hull vertices and search for optimal interior point placement.

    Since the hull is 10 points, try many different interior configurations
    for the remaining 4 points.
    """
    hv = hull_vertex_indices(pts_hull)
    hull_pts = pts_hull[hv].copy()

    # Compute hull centroid and bounding box for interior
    centroid = hull_pts.mean(axis=0)
    hull_obj = ConvexHull(hull_pts)

    best_score = -np.inf
    best_pts = pts_hull.copy()

    for trial in range(n_trials):
        # Generate 4 interior points
        interior = np.zeros((4, 2))
        for i in range(4):
            # Sample from within convex hull
            for _ in range(100):
                pt = centroid + rng.normal(0, 0.3, 2)
                # Simple containment check (approximate)
                if _point_in_hull(pt, hull_pts):
                    interior[i] = pt
                    break
            else:
                interior[i] = centroid + rng.normal(0, 0.1, 2)

        # Assemble full configuration
        new_pts = np.vstack([hull_pts, interior])
        # Polish
        polished, score = polish_slsqp(new_pts, max_iter=300)
        if score > best_score:
            best_score = score
            best_pts = polished.copy()

    return best_pts, best_score


def _point_in_hull(pt, hull_pts):
    """Quick check if point is inside convex hull of hull_pts."""
    try:
        hull = ConvexHull(np.vstack([hull_pts, pt.reshape(1, 2)]))
        # If adding the point doesn't change the hull, it's inside
        return len(hull.vertices) == len(hull_pts)
    except Exception:
        return False


def deformation_search(pts, rng, n_trials=500):
    """Apply continuous deformations to the configuration.

    Instead of point-wise moves, apply global transformations:
    - Affine shears
    - Quadratic warps
    - Conformal maps
    Then polish.
    """
    best_score = fast_score(pts)
    best_pts = pts.copy()

    center = pts.mean(axis=0)
    centered = pts - center

    for trial in range(n_trials):
        r = rng.random()
        if r < 0.25:
            # Random affine shear
            M = np.eye(2) + rng.normal(0, 0.05, (2, 2))
            new_pts = centered @ M.T + center
        elif r < 0.5:
            # Quadratic warp
            eps = rng.normal(0, 0.01, 6)  # 6 quadratic coefficients
            new_pts = pts.copy()
            for i in range(14):
                x, y = centered[i]
                new_pts[i, 0] = pts[i, 0] + eps[0]*x**2 + eps[1]*y**2 + eps[2]*x*y
                new_pts[i, 1] = pts[i, 1] + eps[3]*x**2 + eps[4]*y**2 + eps[5]*x*y
        elif r < 0.75:
            # Radial scaling (expand/contract by distance from center)
            new_pts = pts.copy()
            for i in range(14):
                d = np.linalg.norm(centered[i]) + 1e-15
                scale = 1.0 + rng.normal(0, 0.05) * d
                new_pts[i] = center + centered[i] * scale
        else:
            # Angular perturbation (rotate each point by angle proportional to radius)
            new_pts = pts.copy()
            twist = rng.normal(0, 0.1)
            for i in range(14):
                d = np.linalg.norm(centered[i])
                angle = twist * d
                c, s = np.cos(angle), np.sin(angle)
                R = np.array([[c, -s], [s, c]])
                new_pts[i] = center + R @ centered[i]

        polished, score = polish_slsqp(new_pts, max_iter=300)
        if score > best_score:
            best_score = score
            best_pts = polished.copy()
            at = active_triples(best_pts, rel_tol=1e-9)
            print(f"    Deformation improvement! score={score:.16f} active={len(at)}")

    return best_pts, best_score


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--time", type=float, default=600.0)
    parser.add_argument("--seed", type=int, default=99)
    parser.add_argument("--out", type=str, default="/tmp/heilbronn_kkt_attack.json")
    args = parser.parse_args()

    rng = np.random.default_rng(args.seed)
    start = time.time()

    print(f"Target: {SUBMIT_THRESHOLD:.20f}")
    print(f"Arena #1: {ARENA_BEST:.20f}")
    print(f"Gap: {SUBMIT_THRESHOLD - ARENA_BEST:.3e}")

    # Load starting points
    pts_ref = load_solution("reference")
    pts_jsagent = load_solution("jsagent")
    pts_alt = load_solution("alt")

    best_score = ARENA_BEST
    best_pts = pts_ref.copy() if pts_ref is not None else None
    results = []

    starting_configs = [
        ("reference", pts_ref),
        ("jsagent", pts_jsagent),
        ("alt", pts_alt),
    ]

    for name, pts in starting_configs:
        if pts is None:
            continue
        sc = arena_score(pts)
        at = active_triples(pts, rel_tol=1e-9)
        hv = hull_vertex_indices(pts)
        print(f"\n{name}: score={sc:.16f}  hull={len(hv)}+{14-len(hv)}  active={len(at)}")

    # Phase 1: Null space escape with LARGE steps
    print(f"\n{'='*60}")
    print("Phase 1: Null space escape (large steps)")
    print(f"{'='*60}")

    step_sizes = [1e-6, 1e-5, 1e-4, 1e-3, 5e-3, 1e-2, 5e-2, 0.1, 0.3, 0.5, 1.0]
    for name, pts in starting_configs:
        if pts is None or time.time() - start > args.time * 0.3:
            break
        print(f"\n  From {name}:")
        escaped, esc_score = null_space_escape(
            pts, rng, step_sizes, n_trials=500
        )
        results.append({"phase": f"nullspace-{name}", "score": esc_score})
        if esc_score > best_score:
            best_score = esc_score
            best_pts = escaped.copy()
            print(f"  → Best from null-space: {esc_score:.16f}")

    # Phase 2: Active set surgery
    print(f"\n{'='*60}")
    print("Phase 2: Active set surgery")
    print(f"{'='*60}")

    for name, pts in starting_configs:
        if pts is None or time.time() - start > args.time * 0.55:
            break
        print(f"\n  From {name}:")
        surgered, surg_score = active_set_surgery(pts, rng, n_trials=300)
        results.append({"phase": f"surgery-{name}", "score": surg_score})
        if surg_score > best_score:
            best_score = surg_score
            best_pts = surgered.copy()

    # Phase 3: Deformation search
    print(f"\n{'='*60}")
    print("Phase 3: Continuous deformation search")
    print(f"{'='*60}")

    for name, pts in starting_configs:
        if pts is None or time.time() - start > args.time * 0.8:
            break
        print(f"\n  From {name}:")
        deformed, def_score = deformation_search(pts, rng, n_trials=300)
        results.append({"phase": f"deformation-{name}", "score": def_score})
        if def_score > best_score:
            best_score = def_score
            best_pts = deformed.copy()

    # Phase 4: Combinatorial interior search from reference hull
    remaining = args.time - (time.time() - start)
    if remaining > 30 and pts_ref is not None:
        print(f"\n{'='*60}")
        print(f"Phase 4: Combinatorial interior search ({remaining:.0f}s)")
        print(f"{'='*60}")
        n_trials = max(100, int(remaining * 5))
        combo_pts, combo_score = combinatorial_interior_search(
            pts_ref, rng, n_trials=min(n_trials, 5000)
        )
        results.append({"phase": "combo-interior", "score": combo_score})
        print(f"  Best from interior search: {combo_score:.16f}")
        if combo_score > best_score:
            best_score = combo_score
            best_pts = combo_pts.copy()

    # Summary
    elapsed = time.time() - start
    print(f"\n{'='*60}")
    print(f"KKT ATTACK SUMMARY after {elapsed:.1f}s")
    print(f"{'='*60}")
    print(f"Best score: {best_score:.20f}")
    print(f"Arena #1:   {ARENA_BEST:.20f}")
    print(f"Threshold:  {SUBMIT_THRESHOLD:.20f}")
    if best_score > SUBMIT_THRESHOLD:
        print("*** SUBMITTABLE! ***")
    else:
        print(f"Gap to threshold: {SUBMIT_THRESHOLD - best_score:.3e}")

    out = {
        "best_score": best_score,
        "best_pts": best_pts.tolist(),
        "above_threshold": best_score > SUBMIT_THRESHOLD,
        "elapsed_s": elapsed,
        "results": results,
    }
    Path(args.out).write_text(json.dumps(out, indent=2))
    print(f"\nSaved to {args.out}")


if __name__ == "__main__":
    main()
