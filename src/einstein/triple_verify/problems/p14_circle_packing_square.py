"""P14 — circle packing in the unit square (n=26). Score = Σ r_i (maximize).

Feasibility (re-validated independently by exact + cross): all circles inside
[0,1]² and pairwise disjoint, within tol=1e-9.
"""

from __future__ import annotations

import mpmath as mp

from einstein.circle_packing_square.evaluator import evaluate as _arena

from ..core import Tolerance, register
from . import _circles

WALL_TOL = 1e-9


def _inside_square_py(circles, tol: float = WALL_TOL) -> None:
    for i, (cx, cy, r) in enumerate(((float(c[0]), float(c[1]), float(c[2])) for c in circles)):
        if r < -tol:
            raise ValueError(f"circle {i} negative radius")
        if min(cx - r, 1.0 - (cx + r), cy - r, 1.0 - (cy + r)) < -tol:
            raise ValueError(f"circle {i} outside unit square")


def _fast(seed: dict) -> float:
    return float(_arena(seed))


def _exact(seed: dict) -> float:
    circles = seed["circles"]
    _inside_square_py(circles)
    _circles._pairs_disjoint_py(circles)
    return _circles.sum_radii_py(circles)


def _cross(seed: dict) -> float:
    circles = seed["circles"]
    with mp.workdps(50):
        for cx, cy, r in ((mp.mpf(c[0]), mp.mpf(c[1]), mp.mpf(c[2])) for c in circles):
            if min(cx - r, mp.mpf(1) - (cx + r), cy - r, mp.mpf(1) - (cy + r)) < -mp.mpf(WALL_TOL):
                raise ValueError("circle outside unit square (mpmath)")
    _circles._pairs_disjoint_mp(circles)
    return _circles.sum_radii_mp(circles)


register(
    14,
    fast=_fast,
    exact=_exact,
    cross=_cross,
    tolerance=Tolerance(abs_tol=1e-12, rel_tol=1e-10),
)
