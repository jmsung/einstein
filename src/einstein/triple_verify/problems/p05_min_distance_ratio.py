"""P5 — min distance ratio (2D, n=16). Score = (max_d / min_d)².

fast  — arena evaluator (vectorized numpy pairwise matrix)
exact — pure-python loop over the 120 pairs with math.hypot (different path)
cross — mpmath at 60 dps (higher-precision, different *kind* of evidence)
"""

from __future__ import annotations

import math

import mpmath as mp

from einstein.min_distance_ratio.evaluator import evaluate as _arena

from ..core import Tolerance, register


def _fast(seed: dict) -> float:
    return float(_arena(seed))


def _exact(seed: dict) -> float:
    pts = [(float(x), float(y)) for x, y in seed["vectors"]]
    n = len(pts)
    dists = [
        math.hypot(pts[i][0] - pts[j][0], pts[i][1] - pts[j][1])
        for i in range(n)
        for j in range(i + 1, n)
    ]
    mn, mx = min(dists), max(dists)
    if mn < 1e-12:
        raise ValueError("degenerate: min distance < 1e-12")
    return (mx / mn) ** 2


def _cross(seed: dict) -> float:
    with mp.workdps(60):
        pts = [(mp.mpf(x), mp.mpf(y)) for x, y in seed["vectors"]]
        n = len(pts)
        ds = [
            mp.sqrt((pts[i][0] - pts[j][0]) ** 2 + (pts[i][1] - pts[j][1]) ** 2)
            for i in range(n)
            for j in range(i + 1, n)
        ]
        return float((max(ds) / min(ds)) ** 2)


register(
    5,
    fast=_fast,
    exact=_exact,
    cross=_cross,
    tolerance=Tolerance(abs_tol=1e-10, rel_tol=1e-10),
)
