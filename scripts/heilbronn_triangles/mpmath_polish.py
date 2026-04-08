"""mpmath high-precision polish for Heilbronn Triangles (n=11).

Given a warm-start (CHRONOS #1), polish the point positions at 50+ decimal
digits to determine the basin's true-math ceiling. If the mpmath-polished
score rounded to float64 equals the CHRONOS score, the basin is at the
float64 ceiling and improvement via local polish is impossible.

Strategy: Newton-Raphson on the reduced system
    equations:
        area_{active_i}(p) - t = 0   for each active triple i
        edge constraint on p_i = 0   for each point fixed on an edge
    variables:
        p_i = (x_i, y_i) for interior points
        single coordinate for edge points (the free direction)
        t = minimum area

The CHRONOS #1 solution has 17 active triples. With 2 points on each of the
3 edges (6 × 1 DoF) + 5 interior (5 × 2 DoF = 10 DoF) + 1 (t) = 17 unknowns.
Exactly determined system.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import sys
from pathlib import Path

import mpmath as mp
import numpy as np

# Ensure we can import the einstein package
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from einstein.heilbronn_triangles import (  # noqa: E402
    EQ_TRI_AREA,
    arena_score,
    fast_score,
)

SQRT3 = mp.sqrt(3)
EQ_AREA_MP = SQRT3 / 4


def detect_edge(p, tol=1e-9):
    """Return edge label: 'B' (bottom), 'L' (left), 'R' (right), or 'I' (interior)."""
    x, y = float(p[0]), float(p[1])
    sr3 = math.sqrt(3)
    if abs(y) < tol:
        return "B"
    if abs(y - sr3 * x) < tol:
        return "L"
    if abs(y - sr3 * (1 - x)) < tol:
        return "R"
    return "I"


def mp_tri_area(p1, p2, p3):
    """mpmath triangle area via cross product."""
    return (
        abs(
            p1[0] * (p2[1] - p3[1])
            + p2[0] * (p3[1] - p1[1])
            + p3[0] * (p1[1] - p2[1])
        )
        / 2
    )


def mp_signed_area(p1, p2, p3):
    """mpmath signed cross-product (NOT divided by 2, no abs)."""
    return (
        p1[0] * (p2[1] - p3[1])
        + p2[0] * (p3[1] - p1[1])
        + p3[0] * (p1[1] - p2[1])
    ) / 2


def build_reduced_system(points_mp, edge_labels, active_triples):
    """Build a reduced parameterization:

    - For each point on bottom edge (y=0): free variable is x
    - For each point on left edge (y=sqrt3*x): free variable is x, y=sqrt3*x
    - For each point on right edge (y=sqrt3*(1-x)): free variable is x, y=sqrt3*(1-x)
    - For each interior point: free variables are x, y
    - Plus one extra variable t (the minimum area)

    Returns (var0, to_points, residual_fn) where:
        var0 = list of mpmath initial values
        to_points(var) = list of 11 (x, y) mpmath tuples
        residual_fn(var) = list of equations (active_i area - t)
    """
    N = 11
    var0 = []
    slots = []  # (point_idx, 'B'/'L'/'R'/'I')
    for i in range(N):
        lab = edge_labels[i]
        slots.append((i, lab))
        x, y = points_mp[i]
        if lab == "B":
            var0.append(x)
        elif lab == "L":
            var0.append(x)
        elif lab == "R":
            var0.append(x)
        elif lab == "I":
            var0.append(x)
            var0.append(y)
    # t = current min area
    t_init = min(
        mp_tri_area(points_mp[i], points_mp[j], points_mp[k])
        for i, j, k in active_triples
    )
    var0.append(t_init)

    def to_points(var):
        pts = [None] * N
        k = 0
        for (idx, lab) in slots:
            if lab == "B":
                pts[idx] = (var[k], mp.mpf(0))
                k += 1
            elif lab == "L":
                pts[idx] = (var[k], SQRT3 * var[k])
                k += 1
            elif lab == "R":
                pts[idx] = (var[k], SQRT3 * (1 - var[k]))
                k += 1
            elif lab == "I":
                pts[idx] = (var[k], var[k + 1])
                k += 2
        return pts

    def residuals(var):
        pts = to_points(var)
        t = var[-1]
        # For each active triple, the signed area must equal ±t depending on orientation
        res = []
        for (i, j, k) in active_triples:
            sa = mp_signed_area(pts[i], pts[j], pts[k])
            # Use |sa| = t but branch continuously using sign at init
            res.append(abs(sa) - t)
        return res

    return var0, to_points, residuals, slots


def orient_residuals(points_mp, active_triples):
    """Pre-compute signs of active triples so we can use signed_area directly
    without abs() (which isn't smooth for Newton)."""
    signs = {}
    for (i, j, k) in active_triples:
        sa = mp_signed_area(points_mp[i], points_mp[j], points_mp[k])
        signs[(i, j, k)] = 1 if sa > 0 else -1
    return signs


def run_newton(warm_start_path: Path, dps: int = 60, max_iter: int = 40, verbose: bool = True):
    mp.mp.dps = dps
    data = json.loads(warm_start_path.read_text())
    pts_f64 = np.array(data["data"]["points"], dtype=np.float64)
    claimed = data["score"]
    if verbose:
        print(f"Warm start: {warm_start_path.name}")
        print(f"Claimed float64 score: {claimed!r}")

    # Convert to mpmath
    points_mp = [(mp.mpf(str(x)), mp.mpf(str(y))) for (x, y) in pts_f64.tolist()]

    # Edge labels
    edge_labels = [detect_edge(pts_f64[i], tol=1e-10) for i in range(11)]
    if verbose:
        print(f"Edge labels: {edge_labels}")

    # Active triples at rel_tol 1e-9 (from float64 eval)
    from einstein.heilbronn_triangles import active_triples as _active
    active = _active(pts_f64, rel_tol=1e-9)
    if verbose:
        print(f"Active triples ({len(active)}):")
        for t in active:
            print(f"  {t}")

    # Pre-compute orientation signs
    signs = orient_residuals(points_mp, active)

    # Build reduced system (signed version, no abs)
    N = 11
    slots = []
    var0 = []
    for i in range(N):
        lab = edge_labels[i]
        slots.append((i, lab))
        x, y = points_mp[i]
        if lab in ("B", "L", "R"):
            var0.append(x)
        else:  # "I"
            var0.append(x)
            var0.append(y)
    t_init = min(
        mp_tri_area(points_mp[i], points_mp[j], points_mp[k])
        for i, j, k in active
    )
    var0.append(t_init)
    n_vars = len(var0)

    def to_points(var):
        pts = [None] * N
        k = 0
        for (idx, lab) in slots:
            if lab == "B":
                pts[idx] = (var[k], mp.mpf(0))
                k += 1
            elif lab == "L":
                pts[idx] = (var[k], SQRT3 * var[k])
                k += 1
            elif lab == "R":
                pts[idx] = (var[k], SQRT3 * (1 - var[k]))
                k += 1
            else:
                pts[idx] = (var[k], var[k + 1])
                k += 2
        return pts

    def residuals(var):
        pts = to_points(var)
        t = var[-1]
        res = []
        for (i, j, k) in active:
            sa = mp_signed_area(pts[i], pts[j], pts[k])
            res.append(signs[(i, j, k)] * sa - t)
        return res

    # We have n_eq equations, n_vars variables. If square, Newton. If over/underdetermined,
    # use pseudo-inverse via mpmath.
    n_eq = len(active)
    if verbose:
        print(f"n_vars={n_vars}, n_eq={n_eq}")

    if n_eq == n_vars:
        if verbose:
            print("Square system — using Newton")
        solver = "newton_square"
    elif n_eq > n_vars:
        if verbose:
            print(f"Overdetermined (rows={n_eq} > cols={n_vars}) — "
                  "using Gauss-Newton via pseudo-inverse")
        solver = "gauss_newton"
    else:
        if verbose:
            print(f"Underdetermined (rows={n_eq} < cols={n_vars}) — "
                  "using LS step with extra maximize-t direction")
        solver = "maximize_t"

    # Compute Jacobian via mpmath finite differences
    def numerical_jacobian(var, eps=None):
        if eps is None:
            eps = mp.mpf(10) ** (-dps // 2)
        J = mp.matrix(n_eq, n_vars)
        r0 = residuals(var)
        for j in range(n_vars):
            var_p = list(var)
            var_p[j] = var_p[j] + eps
            r_p = residuals(var_p)
            for i in range(n_eq):
                J[i, j] = (r_p[i] - r0[i]) / eps
        return J, r0

    var = list(var0)
    best_score = float(var[-1]) / float(EQ_AREA_MP)
    if verbose:
        print(f"Initial mpmath score: {best_score!r}")
        print(f"Initial vs claimed diff: {best_score - claimed:.3e}")

    for it in range(max_iter):
        J, r = numerical_jacobian(var)
        r_norm = float(max(abs(ri) for ri in r))
        if verbose and it % 2 == 0:
            print(f"iter {it:3d}  ||r||_inf = {r_norm:.3e}  t = {float(var[-1])!r}")
        if r_norm < mp.mpf(10) ** (-(dps - 10)):
            if verbose:
                print(f"Converged at iter {it}")
            break
        try:
            if solver == "newton_square":
                delta = mp.lu_solve(J, mp.matrix(r))
            elif solver == "gauss_newton":
                JT = J.T
                delta = mp.lu_solve(JT * J, JT * mp.matrix(r))
            else:  # underdetermined
                JT = J.T
                delta = JT * mp.lu_solve(J * JT, mp.matrix(r))
        except Exception as e:
            if verbose:
                print(f"Solver failed at iter {it}: {e}")
            break
        for j in range(n_vars):
            var[j] = var[j] - delta[j]

    # Extract final points
    pts_final = to_points(var)
    pts_np = np.array(
        [[float(px), float(py)] for (px, py) in pts_final], dtype=np.float64
    )

    # True min area at full precision
    min_area_mp = min(
        mp_tri_area(pts_final[i], pts_final[j], pts_final[k])
        for i, j, k in itertools.combinations(range(N), 3)
    )
    true_score_mp = min_area_mp / EQ_AREA_MP
    true_score_f64 = float(true_score_mp)

    if verbose:
        print(f"\n=== RESULTS ===")
        print(f"Claimed (CHRONOS #1): {claimed!r}")
        print(f"mpmath true score (at {dps} dps): {mp.nstr(true_score_mp, 25)}")
        print(f"True math score rounded to float64: {true_score_f64!r}")
        print(f"Delta (true - claimed): {true_score_f64 - claimed:.3e}")
        if true_score_f64 > claimed:
            print("  ✓ True math exceeds claimed — basin has float64 headroom!")
        else:
            print("  ✗ True math ≤ claimed — basin is at float64 ceiling.")

        # Arena-evaluated score of the polished points
        polished_arena = arena_score(pts_np)
        print(f"Polished points arena_score: {polished_arena!r}")
        print(f"Delta (polished - claimed): {polished_arena - claimed:.3e}")

    return {
        "claimed": claimed,
        "true_score_mp": str(true_score_mp),
        "true_score_f64": true_score_f64,
        "delta_true": true_score_f64 - claimed,
        "polished_arena": arena_score(pts_np),
        "polished_points": pts_np.tolist(),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--warm-start",
        default="results/problem-15-heilbronn-triangles/rank01_CHRONOS_0.0365298898800302.json",
        help="Path to warm start JSON",
    )
    ap.add_argument("--dps", type=int, default=60, help="mpmath decimal precision")
    ap.add_argument("--max-iter", type=int, default=40)
    args = ap.parse_args()
    result = run_newton(Path(args.warm_start), dps=args.dps, max_iter=args.max_iter)
    print(f"\nFinal: delta={result['delta_true']:.3e}")


if __name__ == "__main__":
    main()
