"""P15 — Heilbronn triangles in an equilateral triangle (n=11).
Score = min triangle area / equilateral-triangle area.

  fast  — vectorized fast_score
  exact — scalar arena_score (different code path; enforces containment)
  cross — mpmath at 50 dps min-area / (√3/4) (higher precision)

The containment check lives in fast/exact: an out-of-triangle point makes both
return −inf while cross returns a finite number, so the verdict disagrees and
gate 2 rejects (correct — an infeasible point isn't a real score).
"""

from __future__ import annotations

import itertools

import mpmath as mp

from einstein.heilbronn_triangles import evaluator as ev

from ..core import Tolerance, register


def _fast(seed: dict) -> float:
    return float(ev.fast_score(seed["points"]))


def _exact(seed: dict) -> float:
    return float(ev.arena_score(seed["points"]))


def _cross(seed: dict) -> float:
    with mp.workdps(50):
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
        eq = mp.sqrt(3) / 4
        return float(min(areas) / eq)


register(
    15,
    fast=_fast,
    exact=_exact,
    cross=_cross,
    tolerance=Tolerance(abs_tol=1e-12, rel_tol=1e-10),
)
