"""Kissing family — total sphere-overlap penalty (minimise).

One registration covers every fixed-n kissing problem, because they share a
single objective and differ only in (n, d), which each scorer reads from the
seed's own shape:

    6  kissing-number-d11      (n=594, solved)
    24 kissing-number-d11-605  (n=605, open)
    25 kissing-number-d12-842  (n=842, open)

The three checks are three *independent code paths* on that one objective —
not one function called thrice — so a bug in any single path is caught:

    fast  = overlap_loss_fast   (Gram / dot-product, float64)
    exact = overlap_loss        (distance-matrix, float64, different path)
    cross = overlap_loss_mpmath (bignum dps=50, the arena ground truth)

Why register here rather than triple-verify inside the push loop: the loop used
to trust the polish's saved ``score`` (a surrogate — see the Goal-2 finding that
the "5e-6" was ``polish_ulp_coord``'s internal surrogate, not the objective).
Routing through this registry forces honest scoring on the real objective before
``auto_submit.try_submit`` gate 2.
"""

from __future__ import annotations

import numpy as np

from einstein.kissing_number.evaluator import (
    overlap_loss,
    overlap_loss_fast,
    overlap_loss_mpmath,
)

from ..core import Tolerance, register

_KISSING_IDS = (6, 24, 25)


def _vectors(seed: dict) -> np.ndarray:
    return np.asarray(seed["vectors"], dtype=np.float64)


def _fast(seed: dict) -> float:
    return overlap_loss_fast(_vectors(seed))


def _exact(seed: dict) -> float:
    return overlap_loss(_vectors(seed))


def _cross(seed: dict) -> float:
    return overlap_loss_mpmath(_vectors(seed), dps=50)


# abs_tol 1e-9 matches the arena verifier's overlap tolerance; the two float64
# paths and the dps=50 path agree far tighter than this for real configs, so a
# genuine sign/scale bug (which diverges by O(score)) still fails the gate.
for _pid in _KISSING_IDS:
    register(
        _pid,
        fast=_fast,
        exact=_exact,
        cross=_cross,
        tolerance=Tolerance(abs_tol=1e-9, rel_tol=1e-8),
    )
