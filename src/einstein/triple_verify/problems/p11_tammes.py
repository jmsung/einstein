"""P11 — Tammes (n=50 on S²). Score = min pairwise Euclidean distance.

fast  — arena evaluator (normalize + vectorized pairwise)
exact — independent pure-python normalize + math.dist loop over 1225 pairs
cross — mpmath at 50 dps (normalize + min distance, higher precision)
"""

from __future__ import annotations

import math

import mpmath as mp

from einstein.tammes.evaluator import evaluate as _arena

from ..core import Tolerance, register


def _fast(seed: dict) -> float:
    return float(_arena(seed))


def _normalize_py(rows):
    out = []
    for r in rows:
        nrm = math.sqrt(sum(float(c) * float(c) for c in r))
        nrm = nrm if nrm >= 1e-12 else 1e-12
        out.append([float(c) / nrm for c in r])
    return out


def _exact(seed: dict) -> float:
    V = _normalize_py(seed["vectors"])
    n = len(V)
    best = math.inf
    for i in range(n):
        for j in range(i + 1, n):
            d = math.dist(V[i], V[j])
            if d < best:
                best = d
    return best


def _cross(seed: dict) -> float:
    with mp.workdps(50):
        V = []
        for r in seed["vectors"]:
            comps = [mp.mpf(c) for c in r]
            nrm = mp.sqrt(sum(c * c for c in comps))
            if nrm < mp.mpf("1e-12"):
                nrm = mp.mpf("1e-12")
            V.append([c / nrm for c in comps])
        n = len(V)
        best = None
        for i in range(n):
            for j in range(i + 1, n):
                d = mp.sqrt(sum((V[i][d] - V[j][d]) ** 2 for d in range(len(V[i]))))
                if best is None or d < best:
                    best = d
        return float(best)


register(
    11,
    fast=_fast,
    exact=_exact,
    cross=_cross,
    tolerance=Tolerance(abs_tol=1e-11, rel_tol=1e-10),
)
