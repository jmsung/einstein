"""P10 — Thomson problem, n=282. Three-way verify of the Coulomb energy.

Three structurally distinct routes to E = Σ_{i<j} 1/‖p_i − p_j‖ (points
projected to the unit sphere, lower E better):

  fast  — ``coulomb_energy_fast``  (vectorised pairwise distance matrix — the
          arena-evaluator path)
  exact — ``coulomb_energy``       (O(n²) explicit double loop — a different
          code path; catches a broadcasting/vectorisation bug)
  cross — mpmath arbitrary-precision energy (dps=30 — a different *kind* of
          evidence: the two numpy routes share float64 roundoff over ~40k
          pairs, ~1e-10; mpmath pins the true value). The three agree to
          ~8e-11 on the Wales global-minimum seed; cross runs in ~0.2s.

There is no closed-form analytical energy for the Thomson minimum at n=282, so
the third check is high-precision arithmetic per the triple-verify fallback.
A Riemannian-gradient KKT stationarity check (the seed is a genuine critical
point of the constrained energy) lives in tests/thomson/test_triple_verify.py
as a structural cross-check.
"""

from __future__ import annotations

import mpmath as mp
import numpy as np

from einstein.thomson.evaluator import DIMENSION, N_POINTS, coulomb_energy, evaluate

from ..core import Tolerance, register


def _pts(seed: dict) -> np.ndarray:
    """Validated points — same contract as the arena evaluator (N_POINTS×3).
    A malformed solution raises → honest-zero on every scorer."""
    pts = np.asarray(seed["vectors"], dtype=np.float64)
    if pts.shape != (N_POINTS, DIMENSION):
        raise ValueError(f"expected {N_POINTS}×{DIMENSION} points, got {pts.shape}")
    return pts


def _fast(seed: dict) -> float:
    _pts(seed)  # enforce the arena shape contract before scoring
    return float(evaluate(seed))


def _exact(seed: dict) -> float:
    pts = _pts(seed)
    norms = np.linalg.norm(pts, axis=1, keepdims=True)
    return float(coulomb_energy(pts / norms))


def _cross(seed: dict, dps: int = 30) -> float:
    """mpmath arbitrary-precision Coulomb energy (points normalised to S²)."""
    mp.mp.dps = dps
    pts = _pts(seed)
    norms = np.linalg.norm(pts, axis=1)
    P = [[mp.mpf(float(c)) / mp.mpf(float(norms[i])) for c in row] for i, row in enumerate(pts)]
    n = len(P)
    e = mp.mpf(0)
    for i in range(n):
        xi, yi, zi = P[i]
        for j in range(i + 1, n):
            dx = xi - P[j][0]
            dy = yi - P[j][1]
            dz = zi - P[j][2]
            e += 1 / mp.sqrt(dx * dx + dy * dy + dz * dz)
    return float(e)


# Wales CCD global-minimum seed: the three routes agree to ~8e-11 (E≈37147.29).
# Large-magnitude score → relative tolerance dominates.
register(
    10,
    fast=_fast,
    exact=_exact,
    cross=_cross,
    tolerance=Tolerance(abs_tol=1e-7, rel_tol=1e-9),
)
