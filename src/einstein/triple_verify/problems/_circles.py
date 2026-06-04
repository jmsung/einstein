"""Shared circle-packing checks for P14 (square) and P18 (rectangle).

The score is Σ r_i — so all three routes compute the same trivial sum and
agree to float roundoff. The *substance* of the verification is that each route
**independently re-validates feasibility** and raises (→ honest-zero,
passed=False) on an infeasible configuration:

  fast  — the arena evaluator (numpy, tol=1e-9 disjoint + bounds)
  exact — pure-python feasibility re-check + math.fsum of radii
  cross — mpmath feasibility re-check + mpmath.fsum of radii (higher precision)
"""

from __future__ import annotations

import math

import mpmath as mp

OVERLAP_TOL = 1e-9


def _pairs_disjoint_py(circles, tol: float = OVERLAP_TOL) -> None:
    n = len(circles)
    for i in range(n):
        xi, yi, ri = (float(circles[i][0]), float(circles[i][1]), float(circles[i][2]))
        for j in range(i + 1, n):
            xj, yj, rj = (float(circles[j][0]), float(circles[j][1]), float(circles[j][2]))
            d = math.hypot(xi - xj, yi - yj)
            if d + tol < ri + rj:
                raise ValueError(f"circles {i},{j} overlap by {ri + rj - d:.3e} > {tol:.0e}")


def _pairs_disjoint_mp(circles, tol: float = OVERLAP_TOL) -> None:
    tolm = mp.mpf(tol)
    n = len(circles)
    for i in range(n):
        xi, yi, ri = (mp.mpf(circles[i][0]), mp.mpf(circles[i][1]), mp.mpf(circles[i][2]))
        for j in range(i + 1, n):
            xj, yj, rj = (mp.mpf(circles[j][0]), mp.mpf(circles[j][1]), mp.mpf(circles[j][2]))
            d = mp.sqrt((xi - xj) ** 2 + (yi - yj) ** 2)
            if d + tolm < ri + rj:
                raise ValueError(f"circles {i},{j} overlap (mpmath)")


def sum_radii_py(circles) -> float:
    return math.fsum(float(c[2]) for c in circles)


def sum_radii_mp(circles) -> float:
    with mp.workdps(50):
        return float(mp.fsum([mp.mpf(c[2]) for c in circles]))
