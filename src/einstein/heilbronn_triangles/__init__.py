"""Heilbronn Problem for Triangles (n=11) — Problem 15.

Place 11 points on or within an equilateral triangle with vertices
    A = (0, 0), B = (1, 0), C = (1/2, sqrt(3)/2)
(area = sqrt(3)/4) to maximize the normalized minimum triangle area:

    score = min_{i<j<k} area(p_i, p_j, p_k) / (sqrt(3)/4)
"""

from .evaluator import (
    EQ_TRI_AREA,
    EQ_TRI_VERTICES,
    active_triples,
    all_triangle_areas,
    arena_score,
    fast_score,
    in_triangle,
    min_triangle_area,
    project_into_triangle,
)

__all__ = [
    "EQ_TRI_AREA",
    "EQ_TRI_VERTICES",
    "active_triples",
    "all_triangle_areas",
    "arena_score",
    "fast_score",
    "in_triangle",
    "min_triangle_area",
    "project_into_triangle",
]
