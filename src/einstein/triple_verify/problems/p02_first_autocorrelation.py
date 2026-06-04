"""P2 — first autocorrelation inequality. Three-way verify (autoconvolution peak)."""

from __future__ import annotations

from einstein.first_autocorrelation.evaluator import evaluate as _arena

from ..core import Tolerance, register
from . import _autocorr

# n=30000 FFT roundoff: the three routes agree to ~1e-10 relative on the seed
# (calibrated in tests/first_autocorrelation/test_triple_verify.py).
register(
    2,
    fast=_autocorr.make_fast(_arena),
    exact=_autocorr.make_exact(require_nonneg=True, take_abs=False),
    cross=_autocorr.make_cross(take_abs=False),
    tolerance=Tolerance(abs_tol=1e-12, rel_tol=1e-9),
)
