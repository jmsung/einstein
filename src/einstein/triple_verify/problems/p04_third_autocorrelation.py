"""P4 — third autocorrelation inequality. Three-way verify (autoconvolution peak).

Unlike P2, f may be negative; only the positive peak counts (abs of max).
"""

from __future__ import annotations

from einstein.third_autocorrelation.evaluator import evaluate as _arena

from ..core import Tolerance, register
from . import _autocorr

register(
    4,
    fast=_autocorr.make_fast(_arena),
    exact=_autocorr.make_exact(require_nonneg=False, take_abs=True),
    cross=_autocorr.make_cross(take_abs=True),
    tolerance=Tolerance(abs_tol=1e-12, rel_tol=1e-9),
)
