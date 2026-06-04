"""P18 — circles in a rectangle (n=21). Score = Σ r_i (maximize).

Feasibility (re-validated independently): pairwise disjoint within tol=1e-9 AND
minimum circumscribing rectangle perimeter ≤ 4 (within PERIMETER_TOL=1e-12).
"""

from __future__ import annotations

import mpmath as mp

from einstein.circles_rectangle.evaluator import evaluate as _arena

from ..core import Tolerance, register
from . import _circles

PERIMETER_BOUND = 4.0
PERIMETER_TOL = 1e-12


def _perimeter_py(circles) -> float:
    xs0 = min(float(c[0]) - float(c[2]) for c in circles)
    xs1 = max(float(c[0]) + float(c[2]) for c in circles)
    ys0 = min(float(c[1]) - float(c[2]) for c in circles)
    ys1 = max(float(c[1]) + float(c[2]) for c in circles)
    return 2.0 * ((xs1 - xs0) + (ys1 - ys0))


def _fast(seed: dict) -> float:
    return float(_arena(seed))


def _exact(seed: dict) -> float:
    circles = seed["circles"]
    _circles._pairs_disjoint_py(circles)
    if _perimeter_py(circles) > PERIMETER_BOUND + PERIMETER_TOL:
        raise ValueError("rectangle perimeter > 4")
    return _circles.sum_radii_py(circles)


def _cross(seed: dict) -> float:
    circles = seed["circles"]
    _circles._pairs_disjoint_mp(circles)
    with mp.workdps(50):
        xs0 = min(mp.mpf(c[0]) - mp.mpf(c[2]) for c in circles)
        xs1 = max(mp.mpf(c[0]) + mp.mpf(c[2]) for c in circles)
        ys0 = min(mp.mpf(c[1]) - mp.mpf(c[2]) for c in circles)
        ys1 = max(mp.mpf(c[1]) + mp.mpf(c[2]) for c in circles)
        perim = 2 * ((xs1 - xs0) + (ys1 - ys0))
        if perim > mp.mpf(PERIMETER_BOUND) + mp.mpf(PERIMETER_TOL):
            raise ValueError("rectangle perimeter > 4 (mpmath)")
    return _circles.sum_radii_mp(circles)


register(
    18,
    fast=_fast,
    exact=_exact,
    cross=_cross,
    tolerance=Tolerance(abs_tol=1e-12, rel_tol=1e-10),
)
