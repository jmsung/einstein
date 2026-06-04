"""P16 — Heilbronn triangles in a convex region (n=14).
Score = min triangle area / convex-hull area.

  fast  — vectorized fast_score (scipy ConvexHull volume)
  exact — scalar arena_score (different code path)
  cross — mpmath min-area / mpmath shoelace hull area (the hull area is
          recomputed by the shoelace formula over scipy's hull-vertex order —
          a different *computation* than scipy's ConvexHull.volume)
"""

from __future__ import annotations

import itertools

import mpmath as mp
import numpy as np
from scipy.spatial import ConvexHull

from einstein.heilbronn_convex import evaluator as ev

from ..core import Tolerance, register


def _fast(seed: dict) -> float:
    return float(ev.fast_score(seed["points"]))


def _exact(seed: dict) -> float:
    return float(ev.arena_score(seed["points"]))


def _cross(seed: dict) -> float:
    pts_f = np.asarray(seed["points"], dtype=np.float64)
    verts = ConvexHull(pts_f).vertices  # CCW vertex order
    with mp.workdps(50):
        ring = [(mp.mpf(float(pts_f[v, 0])), mp.mpf(float(pts_f[v, 1]))) for v in verts]
        m = len(ring)
        cross2 = mp.mpf(0)
        for i in range(m):
            x1, y1 = ring[i]
            x2, y2 = ring[(i + 1) % m]
            cross2 += x1 * y2 - x2 * y1
        h_area = abs(cross2) / 2
        pts = [(mp.mpf(x), mp.mpf(y)) for x, y in seed["points"]]
        areas = []
        for i, j, k in itertools.combinations(range(len(pts)), 3):
            a = (
                abs(
                    pts[i][0] * (pts[j][1] - pts[k][1])
                    + pts[j][0] * (pts[k][1] - pts[i][1])
                    + pts[k][0] * (pts[i][1] - pts[j][1])
                )
                / 2
            )
            areas.append(a)
        return float(min(areas) / h_area)


register(
    16,
    fast=_fast,
    exact=_exact,
    cross=_cross,
    tolerance=Tolerance(abs_tol=1e-12, rel_tol=1e-10),
)
