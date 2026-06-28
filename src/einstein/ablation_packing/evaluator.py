"""Equal circles in the unit square — the held-out family's objective + verify.

Objective (identical to config/ablation_problems.yaml): given n circle centers in
[0,1]^2, the achievable common radius is

    r(centers) = min( 0.5 * min_{i<j} ||c_i - c_j||,           # half closest gap
                      min_i min(cx_i, 1-cx_i, cy_i, 1-cy_i) )  # nearest wall

Maximize r. The reference optima (Packomania) are the best-known max r(n).

Triple-verify (A1): three independent code paths must agree before a score is
trusted —
  1. fast    — numpy vectorized,
  2. exact   — mpmath at high precision, pure-python loops (different code path),
  3. cross   — scipy pdist (C path) + a *feasibility* check that radius r is
               actually achievable (different KIND of evidence).
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


def _as_centers(centers) -> np.ndarray:
    arr = np.asarray(centers, dtype=np.float64)
    if arr.ndim != 2 or arr.shape[1] != 2:
        raise ValueError(f"centers must be (n, 2); got {arr.shape}")
    return arr


def common_radius(centers) -> float:
    """Fast (numpy) achievable common radius for the given centers (>=1 pt).

    Centers outside [0,1]^2 yield a negative wall term, so the radius reflects
    the constraint violation rather than silently clamping."""
    c = _as_centers(centers)
    n = len(c)
    walls = np.min([c[:, 0], 1.0 - c[:, 0], c[:, 1], 1.0 - c[:, 1]])
    if n < 2:
        return float(walls)
    diffs = c[:, None, :] - c[None, :, :]
    d2 = np.sum(diffs * diffs, axis=-1)
    iu = np.triu_indices(n, k=1)
    half_min_gap = 0.5 * float(np.sqrt(np.min(d2[iu])))
    return float(min(half_min_gap, walls))


def common_radius_mpmath(centers, *, dps: int = 50) -> float:
    """Exact (mpmath, high-precision, pure-python) common radius — the §A1
    independent reimplementation that catches numpy float drift / bugs."""
    from mpmath import mp, mpf, sqrt

    mp.dps = dps
    c = _as_centers(centers)
    n = len(c)
    pts = [(mpf(str(x)), mpf(str(y))) for x, y in c]
    wall = min(min(x, 1 - x, y, 1 - y) for x, y in pts)
    if n < 2:
        return float(wall)
    half_min_gap = None
    for i in range(n):
        for j in range(i + 1, n):
            dx = pts[i][0] - pts[j][0]
            dy = pts[i][1] - pts[j][1]
            d = sqrt(dx * dx + dy * dy) / 2
            half_min_gap = d if half_min_gap is None else min(half_min_gap, d)
    return float(min(half_min_gap, wall))


@dataclass(frozen=True)
class TripleVerify:
    """Result of the three-way score check (A1)."""

    fast: float
    exact: float
    cross: float
    passed: bool
    feasible: bool
    reason: str


def triple_verify_radius(centers, *, tol: float = 1e-9) -> TripleVerify:
    """Verify the common radius three independent ways (A1).

    Passes iff fast/exact/cross agree within `tol` AND radius r is feasible
    (circles of radius r are pairwise disjoint and inside the square within tol).
    If any two disagree the score is fake — `passed=False` with a reason.
    """
    from scipy.spatial.distance import pdist

    c = _as_centers(centers)
    fast = common_radius(c)
    exact = common_radius_mpmath(c)

    # cross: scipy C-path pairwise + numpy wall (structurally different from fast)
    walls = float(np.min([c[:, 0], 1.0 - c[:, 0], c[:, 1], 1.0 - c[:, 1]]))
    if len(c) >= 2:
        cross = float(min(0.5 * float(np.min(pdist(c))), walls))
    else:
        cross = walls

    # feasibility: radius r actually achievable? (different KIND of check)
    r = fast
    feasible = True
    # Red-team 2026-06-27: explicitly reject degenerate/invalid geometry — otherwise a
    # non-positive radius makes the gap/wall checks below vacuously true, so out-of-square
    # points, duplicate centers, and negative radii all passed `feasible=True`.
    if r <= tol:
        feasible = False  # duplicate/coincident centers (r≈0) or out-of-square (r<0)
    if np.any(c < -tol) or np.any(c > 1.0 + tol):
        feasible = False  # a center lies outside the unit square
    if len(c) >= 2:
        gaps = pdist(c)
        if np.any(gaps < 2 * r - tol):
            feasible = False
    if walls < r - tol:
        feasible = False

    agree = abs(fast - exact) <= tol and abs(fast - cross) <= tol
    passed = agree and feasible
    if not agree:
        reason = f"disagreement: fast={fast:.12f} exact={exact:.12f} cross={cross:.12f}"
    elif not feasible:
        reason = f"radius {r:.12f} not feasible (overlap or out-of-square)"
    else:
        reason = "ok"
    return TripleVerify(
        fast=fast, exact=exact, cross=cross, passed=passed, feasible=feasible, reason=reason
    )


def cold_init(n: int, seed: int) -> np.ndarray:
    """Deterministic cold-start: n centers i.i.d. uniform in [0,1]^2 (pre-reg §5
    no-warm-start). Same (n, seed) always yields the same init so Cold and Warm
    share the cold baseline for a given (problem, seed) cell."""
    rng = np.random.default_rng(seed)
    return rng.random((n, 2))
