"""Evaluator for Heilbronn Convex (n=14) — Problem 16.

Arena verifier spec (exact, tolerance=0):
    def evaluate(data):
        points = np.array(data["points"], dtype=np.float64)
        if points.shape != (14, 2):
            return -float("inf")
        if not np.isfinite(points).all():
            return -float("inf")
        def tri_area(p1, p2, p3):
            return abs(p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1])
                       + p3[0]*(p1[1]-p2[1])) / 2
        hull_area = ConvexHull(points).volume
        if hull_area < 1e-12:
            return -float("inf")
        min_area = min(tri_area(points[i], points[j], points[k])
                       for i, j, k in itertools.combinations(range(14), 3))
        return float(min_area / hull_area)

Our module provides:
    arena_score(points)    — byte-exact port of the arena verifier
    fast_score(points)     — vectorized numpy version for tight optimization loops
    min_triangle_area(pts) — returns min area and the argmin triple
    hull_area(pts)         — convex hull area
    active_triples(pts, rel_tol) — list of (i,j,k) with area within rel_tol of min
"""

from __future__ import annotations

import itertools

import numpy as np
from scipy.spatial import ConvexHull

# Index of all C(14,3)=364 triples — precomputed for speed
N = 14
_TRIPLES = np.array(list(itertools.combinations(range(N), 3)), dtype=np.int64)


def _tri_area_scalar(p1, p2, p3) -> float:
    """Signed-free triangle area using the cross-product formula (matches verifier)."""
    return abs(
        p1[0] * (p2[1] - p3[1])
        + p2[0] * (p3[1] - p1[1])
        + p3[0] * (p1[1] - p2[1])
    ) / 2.0


def arena_score(points) -> float:
    """Exact port of the arena verifier. Returns -inf on invalid input."""
    pts = np.asarray(points, dtype=np.float64)
    if pts.shape != (N, 2):
        return -float("inf")
    if not np.isfinite(pts).all():
        return -float("inf")
    try:
        h_area = ConvexHull(pts).volume  # 2D: "volume" = area
    except Exception:
        return -float("inf")
    if h_area < 1e-12:
        return -float("inf")
    min_area = min(
        _tri_area_scalar(pts[i], pts[j], pts[k])
        for i, j, k in itertools.combinations(range(N), 3)
    )
    return float(min_area / h_area)


def all_triangle_areas(points) -> np.ndarray:
    """Return the (364,) array of triangle areas in the canonical triple order."""
    pts = np.asarray(points, dtype=np.float64)
    i = _TRIPLES[:, 0]
    j = _TRIPLES[:, 1]
    k = _TRIPLES[:, 2]
    p1 = pts[i]
    p2 = pts[j]
    p3 = pts[k]
    cross = (
        p1[:, 0] * (p2[:, 1] - p3[:, 1])
        + p2[:, 0] * (p3[:, 1] - p1[:, 1])
        + p3[:, 0] * (p1[:, 1] - p2[:, 1])
    )
    return np.abs(cross) * 0.5


def min_triangle_area(points) -> tuple[float, tuple[int, int, int]]:
    """Minimum triangle area and the triple that attains it."""
    areas = all_triangle_areas(points)
    idx = int(np.argmin(areas))
    return float(areas[idx]), tuple(_TRIPLES[idx].tolist())


def hull_area(points) -> float:
    """Convex hull area (2D)."""
    pts = np.asarray(points, dtype=np.float64)
    try:
        return float(ConvexHull(pts).volume)
    except Exception:
        return 0.0


def fast_score(points) -> float:
    """Vectorized score = min triangle area / hull area. Matches arena up to
    floating-point evaluation order; for strict parity use `arena_score`."""
    pts = np.asarray(points, dtype=np.float64)
    if pts.shape != (N, 2):
        return -float("inf")
    if not np.isfinite(pts).all():
        return -float("inf")
    try:
        h = ConvexHull(pts).volume
    except Exception:
        return -float("inf")
    if h < 1e-12:
        return -float("inf")
    areas = all_triangle_areas(pts)
    return float(areas.min() / h)


def active_triples(
    points, rel_tol: float = 1e-9
) -> list[tuple[int, int, int]]:
    """Return list of triples whose area is within rel_tol * min_area of the minimum.

    An "active" triple is one that (approximately) attains the min. These define
    the constraint set for Lagrangian / equioscillation analysis.
    """
    areas = all_triangle_areas(points)
    min_a = areas.min()
    mask = areas < min_a * (1.0 + rel_tol) + 1e-18
    return [tuple(t.tolist()) for t in _TRIPLES[mask]]


def hull_vertex_indices(points) -> list[int]:
    """Indices of the points that form the convex hull, in counterclockwise order."""
    pts = np.asarray(points, dtype=np.float64)
    hull = ConvexHull(pts)
    return hull.vertices.tolist()
