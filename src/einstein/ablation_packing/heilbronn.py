"""Heilbronn triangle objective for the knowledge-compounding ablation (v2).

Objective: place n points in the unit square [0,1]^2; the score is the MINIMUM
triangle area over all C(n,3) triples. Maximize it. Non-smooth (a min over many
terms) — which is exactly why it is not one-shot from training (pre-reg v2 §1).

Generic — the bare objective + triple-verify, no problem-specific method. The
harness scores the agent's output with this; the agent's self-report is ignored.
"""

from __future__ import annotations

from itertools import combinations

import numpy as np

from .evaluator import TripleVerify, _as_centers


def _triple_index(n: int) -> np.ndarray:
    return np.array(list(combinations(range(n), 3)), dtype=int)


def min_triangle_area(centers) -> float:
    """Fast (vectorized numpy) minimum triangle area over all triples (n>=3)."""
    c = _as_centers(centers)
    n = len(c)
    if n < 3:
        return 0.0
    t = _triple_index(n)
    a, b, d = c[t[:, 0]], c[t[:, 1]], c[t[:, 2]]
    area = 0.5 * np.abs(
        (b[:, 0] - a[:, 0]) * (d[:, 1] - a[:, 1]) - (d[:, 0] - a[:, 0]) * (b[:, 1] - a[:, 1])
    )
    return float(area.min())


def min_triangle_area_mpmath(centers, *, dps: int = 50) -> float:
    """Exact (mpmath, pure-python) minimum triangle area — the §A1 independent path."""
    from mpmath import mp, mpf

    mp.dps = dps
    c = _as_centers(centers)
    n = len(c)
    if n < 3:
        return 0.0
    pts = [(mpf(str(x)), mpf(str(y))) for x, y in c]
    best = None
    for i, j, k in combinations(range(n), 3):
        ax, ay = pts[i]
        bx, by = pts[j]
        dx, dy = pts[k]
        area = abs((bx - ax) * (dy - ay) - (dx - ax) * (by - ay)) / 2
        best = area if best is None else min(best, area)
    return float(best)


def triple_verify_heilbronn(centers, *, tol: float = 1e-9) -> TripleVerify:
    """Verify the min triangle area three independent ways (A1) + feasibility.

    fast = vectorized numpy; exact = mpmath; cross = a plain-python loop (a third
    code path). Feasible iff all points lie inside the unit square (within tol) —
    a Heilbronn configuration with points outside [0,1]^2 is invalid.
    """
    c = _as_centers(centers)
    fast = min_triangle_area(c)
    exact = min_triangle_area_mpmath(c)
    # cross: independent plain-python loop
    best = None
    for i, j, k in combinations(range(len(c)), 3):
        ax, ay = c[i]
        bx, by = c[j]
        dx, dy = c[k]
        area = abs((bx - ax) * (dy - ay) - (dx - ax) * (by - ay)) / 2
        best = area if best is None else min(best, area)
    cross = float(best) if best is not None else 0.0

    feasible = bool(np.all(c >= -tol) and np.all(c <= 1 + tol))
    agree = abs(fast - exact) <= tol and abs(fast - cross) <= tol
    passed = agree and feasible
    if not agree:
        reason = f"disagreement: fast={fast:.12f} exact={exact:.12f} cross={cross:.12f}"
    elif not feasible:
        reason = "points outside the unit square"
    else:
        reason = "ok"
    return TripleVerify(
        fast=fast, exact=exact, cross=cross, passed=passed, feasible=feasible, reason=reason
    )
