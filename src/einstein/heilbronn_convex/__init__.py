"""Heilbronn Problem for Convex Regions (n=14) — Problem 16.

Place 14 points in the plane to maximize the area of the smallest triangle
formed by any triple, normalized by the convex hull area:

    score = min_{i<j<k} area(p_i, p_j, p_k) / area(convex_hull(points))

The score is affine-invariant: any affine transformation preserves the
ratio, so solutions can be canonicalized (e.g., hull area fixed to 1).
"""

from .evaluator import (
    arena_score,
    fast_score,
    min_triangle_area,
    all_triangle_areas,
    hull_area,
    active_triples,
    hull_vertex_indices,
)

__all__ = [
    "arena_score",
    "fast_score",
    "min_triangle_area",
    "all_triangle_areas",
    "hull_area",
    "active_triples",
    "hull_vertex_indices",
]
