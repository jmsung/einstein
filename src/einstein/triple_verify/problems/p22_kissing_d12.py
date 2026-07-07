"""P22 — kissing number in d=12 (n=841). Total sphere-overlap penalty (minimise).

Was a ``stub_no_op_no_solution`` unavailable-stub (registered honestly when no
solution payload existed). P22 shares the kissing overlap objective and ships its
own shape-locked (841, 12) evaluator, so it now registers three genuinely
independent code paths — same discipline as the fixed-n frontier siblings in
``p_kissing`` (ids 6/24/25), but bound to P22's exact-shape verifier:

    fast  = overlap_loss_fast   (Gram / dot-product, float64)
    exact = overlap_loss        (distance-matrix, float64, different path)
    cross = overlap_loss_mpmath (bignum dps=50, arena ground truth; ~7s at n=841)

A submit-time payload with the wrong shape raises inside the evaluator, which the
agreement gate surfaces as a failed verify (honest-zero over fake-pass).
"""

from __future__ import annotations

import numpy as np

from einstein.p22_kissing_d12.evaluator import (
    overlap_loss,
    overlap_loss_fast,
    overlap_loss_mpmath,
)

from ..core import Tolerance, register


def _vectors(seed: dict) -> np.ndarray:
    return np.asarray(seed["vectors"], dtype=np.float64)


def _fast(seed: dict) -> float:
    return overlap_loss_fast(_vectors(seed))


def _exact(seed: dict) -> float:
    return overlap_loss(_vectors(seed))


def _cross(seed: dict) -> float:
    return overlap_loss_mpmath(_vectors(seed), dps=50)


# abs_tol 1e-9 matches the arena overlap tolerance; the two float64 paths and the
# dps=50 path agree to ~1e-12 for real configs (see the family rationale in
# p_kissing), so a genuine sign/scale bug still fails the gate.
register(
    22,
    fast=_fast,
    exact=_exact,
    cross=_cross,
    tolerance=Tolerance(abs_tol=1e-9, rel_tol=1e-8),
)
