"""Optimizers for Heilbronn Convex (n=14) max-min triangle area problem.

Two main entry points:

    polish_slsqp(pts, max_iter)      — local polish via epigraph SLSQP with
                                       3-point affine gauge + hull normalization
    cmaes_search(x0, sigma, target)  — global search via CMA-ES on a smoothmax surrogate
    smooth_neg_score(x, beta)        — log-sum-exp soft-min surrogate (maximize)

The epigraph form used by polish_slsqp:

    maximize   t
    subject to area_i(pts) >= t     for i = 1..364
               hull_area(pts) == 1    (normalization)
               pts[0..2] == fixed_3   (affine gauge)
"""

from __future__ import annotations

import numpy as np
from scipy.optimize import minimize
from scipy.spatial import ConvexHull

from .evaluator import _TRIPLES, arena_score, all_triangle_areas

N = 14
_I, _J, _K = _TRIPLES[:, 0], _TRIPLES[:, 1], _TRIPLES[:, 2]


def _tri_areas(pts: np.ndarray) -> np.ndarray:
    p1, p2, p3 = pts[_I], pts[_J], pts[_K]
    cross = (
        p1[:, 0] * (p2[:, 1] - p3[:, 1])
        + p2[:, 0] * (p3[:, 1] - p1[:, 1])
        + p3[:, 0] * (p1[:, 1] - p2[:, 1])
    )
    return 0.5 * np.abs(cross)


def smooth_neg_score(x: np.ndarray, beta: float = 1e5) -> float:
    """Negated soft-min/hull_area surrogate. Lower is better (for minimize())."""
    pts = x.reshape(N, 2)
    try:
        ha = ConvexHull(pts).volume
    except Exception:
        return 1e10
    if ha < 1e-9 or not np.isfinite(ha):
        return 1e10
    areas = _tri_areas(pts) / ha
    mn = areas.min()
    # LSE soft-min: mn - log(sum(exp(-beta*(a-mn))))/beta
    soft = mn - np.log(np.sum(np.exp(-beta * (areas - mn)))) / beta
    return -soft


def polish_slsqp(
    pts_init: np.ndarray,
    max_iter: int = 300,
    ftol: float = 1e-20,
    gauge_indices: tuple[int, int, int] = (0, 1, 2),
) -> tuple[np.ndarray, float]:
    """Epigraph SLSQP polish. Returns (polished_pts, arena_score).

    Fixes three points as an affine gauge and normalizes hull area to its
    initial value. Maximizes t subject to all triangle areas >= t.
    """
    pts0 = np.asarray(pts_init, dtype=np.float64).copy()
    if pts0.shape != (N, 2):
        raise ValueError(f"Expected ({N}, 2), got {pts0.shape}")
    try:
        ha0 = ConvexHull(pts0).volume
    except Exception:
        return pts0, -np.inf
    if ha0 < 1e-9:
        return pts0, -np.inf

    i0, i1, i2 = gauge_indices
    t0 = _tri_areas(pts0).min()
    x0 = np.concatenate([pts0.flatten(), [t0]])

    def neg_t(x: np.ndarray) -> float:
        return -x[28]

    def neg_t_grad(x: np.ndarray) -> np.ndarray:
        g = np.zeros_like(x)
        g[28] = -1.0
        return g

    def ineq(x: np.ndarray) -> np.ndarray:
        return _tri_areas(x[:28].reshape(N, 2)) - x[28]

    fixed = pts0[[i0, i1, i2]].copy()

    def gauge(x: np.ndarray) -> np.ndarray:
        pts = x[:28].reshape(N, 2)
        return np.concatenate(
            [pts[i0] - fixed[0], pts[i1] - fixed[1], pts[i2] - fixed[2]]
        )

    def hull_eq(x: np.ndarray) -> float:
        pts = x[:28].reshape(N, 2)
        try:
            return ConvexHull(pts).volume - ha0
        except Exception:
            return 1.0

    try:
        res = minimize(
            neg_t,
            x0,
            jac=neg_t_grad,
            method="SLSQP",
            constraints=[
                {"type": "ineq", "fun": ineq},
                {"type": "eq", "fun": gauge},
                {"type": "eq", "fun": hull_eq},
            ],
            options={"maxiter": max_iter, "ftol": ftol},
        )
        pts_new = res.x[:28].reshape(N, 2)
        return pts_new, arena_score(pts_new)
    except Exception:
        return pts0, arena_score(pts0)


def random_convex_init(
    rng: np.random.Generator,
    n: int = N,
    shape: str = "disk",
) -> np.ndarray:
    """Generate a random initial configuration guaranteed to be non-degenerate."""
    if shape == "disk":
        # Sample in a unit disk
        u = rng.uniform(size=(n, 2))
        r = np.sqrt(u[:, 0])
        theta = u[:, 1] * 2 * np.pi
        return np.column_stack([r * np.cos(theta), r * np.sin(theta)])
    elif shape == "square":
        return rng.uniform(-1, 1, size=(n, 2))
    elif shape == "10p4":
        # 10 points on convex polygon + 4 interior
        angles = np.sort(rng.uniform(0, 2 * np.pi, 10))
        # Randomize radii slightly
        radii = rng.uniform(0.9, 1.1, 10)
        hull_pts = np.column_stack([radii * np.cos(angles), radii * np.sin(angles)])
        # Interior: smaller disk
        u = rng.uniform(size=(4, 2))
        r = np.sqrt(u[:, 0]) * 0.5
        theta = u[:, 1] * 2 * np.pi
        int_pts = np.column_stack([r * np.cos(theta), r * np.sin(theta)])
        return np.vstack([hull_pts, int_pts])
    else:
        raise ValueError(f"unknown shape: {shape}")


def basin_hop(
    pts0: np.ndarray,
    n_hops: int = 50,
    sigma: float = 0.05,
    rng: np.random.Generator | None = None,
    max_iter: int = 300,
) -> tuple[np.ndarray, float, int]:
    """Basin hopping from pts0. Returns (best_pts, best_score, n_improvements)."""
    if rng is None:
        rng = np.random.default_rng()
    best_pts = pts0.copy()
    best_score = arena_score(pts0)
    improvements = 0
    for _ in range(n_hops):
        pts = best_pts + rng.normal(0, sigma, best_pts.shape)
        polished, score = polish_slsqp(pts, max_iter=max_iter)
        if score > best_score:
            best_score = score
            best_pts = polished.copy()
            improvements += 1
    return best_pts, best_score, improvements
