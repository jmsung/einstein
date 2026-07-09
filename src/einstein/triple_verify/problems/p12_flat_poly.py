"""P12 — flat polynomials. Three-way verify of the CONTINUOUS sup of |p(z)|/√71.

Score = sup_{|z|=1} |p(z)| / √71, p the ±1 coefficient polynomial (descending
degree), lower better. Reconciled 2026-06-04 (Phase 7, Goal 2) to certify the
grid-INDEPENDENT continuous supremum rather than the arena's 1e6-point grid max.

Why the change: the arena score is a grid maximum, which underestimates the true
sup because the peak rarely lands on a node. That grid-vs-continuum gap is the
~7e-10 local↔arena drift (knowledge/wiki/findings/dead-end-p12-grid-sampling-drift.md
and its resolution finding/p12-grid-drift-resolution.md). Verifying the grid
quantity made the three checks agree on a number that *isn't* what the arena
reports. The continuous sup is drift-free: g(θ)=|p(e^{iθ})|² is an exact degree
n-1 trig polynomial, so peaks Newton-refine to machine precision, and all three
routes agree to ~2e-16. The 1e6 grid remains a fast pre-filter (see
`compute_score`), not the authoritative score.

Three routes (all target the continuous sup):

  fast  — FFT(2²⁰)-seeded float64 Newton on g=|p|² (``continuous_sup_score``)
  exact — denser FFT(2²²) seeding + more candidate peaks (different params/path;
          catches a peak the coarser seeding might miss)
  cross — mpmath dps=50 Newton refinement (a different *kind*: arbitrary
          precision pins the peak independent of float64 rounding)

For the SOTA seed: 1M grid 1.2809320520721, arena 1.2809320527988, certified
continuous sup 1.2809320528750 — both grids sit below the true sup, all gaps
< minImprovement (1e-8). SAFE submission rule (see resolution finding): compare a
candidate's continuous sup against arena #1's reported grid score — since grid ≤
continuum always, a continuous sup below the arena grid value is a genuine
improvement on the arena's own metric and never over-claims.
"""

from __future__ import annotations

import numpy as np

from einstein.flat_poly.evaluator import continuous_sup_score, continuous_sup_score_mpmath

from ..core import Tolerance, register


def _coeffs(seed: dict) -> np.ndarray:
    c = np.asarray(seed["coefficients"], dtype=np.float64)
    if len(c) != 70 or not np.all((c == 1) | (c == -1)):
        raise ValueError("expected 70 coefficients in {+1,-1}")
    return c


def _fast(seed: dict) -> float:
    _coeffs(seed)  # enforce the arena contract before scoring
    return continuous_sup_score(seed["coefficients"])


def _exact(seed: dict) -> float:
    """Denser FFT seeding + more peaks — independent of the fast path's grid."""
    _coeffs(seed)
    return continuous_sup_score(seed["coefficients"], m_grid=1 << 22, k_peaks=512)


def _cross(seed: dict) -> float:
    """Arbitrary-precision continuous sup — a different kind of evidence."""
    _coeffs(seed)
    return continuous_sup_score_mpmath(seed["coefficients"])


# SOTA seed: all three certify the continuous sup 1.2809320528750 to ~2e-16.
register(
    12,
    fast=_fast,
    exact=_exact,
    cross=_cross,
    tolerance=Tolerance(abs_tol=1e-10, rel_tol=1e-9),
)
