"""P12 triple-verify: SOTA seed agrees 3-way; documents the grid-sampling drift."""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _triple_verify_util import load_seed, max_pairwise_delta  # noqa: E402

from einstein.flat_poly.evaluator import NORM  # noqa: E402
from einstein.triple_verify import core  # noqa: E402

SEED = "scripts/flat_poly/seeds/best.json"
PINNED_DELTA = 1e-10  # fast / fft / mpmath agree to <1e-15 on the 1M-grid max


def test_seed_passes_three_way():
    r = core.verify(load_seed(SEED), core.get_verifier(12))
    assert r.passed, r.reason
    assert max_pairwise_delta(r) < PINNED_DELTA


def test_grid_sampling_drift_is_bounded():
    """Independent dense/shifted-grid re-evaluation (the branch's third idea).
    A denser grid catches a slightly higher peak than the 1M arena grid — this
    is the documented local↔arena drift, bounded at ~1e-9. We assert it is real
    but small, rather than fold it into the 3-way tolerance (which would hide
    it). See dead-end-p12-grid-sampling-drift.md."""
    coeffs = np.asarray(load_seed(SEED)["coefficients"], dtype=np.float64)
    grid_1m = float(
        np.max(np.abs(np.poly1d(coeffs)(np.exp(2j * np.pi * np.arange(1_000_000) / 1_000_000))))
        / NORM
    )
    z2 = np.exp(2j * np.pi * (np.arange(4_000_000) + 0.5) / 4_000_000)
    grid_dense = float(np.max(np.abs(np.poly1d(coeffs)(z2))) / NORM)
    drift = grid_dense - grid_1m
    assert 0 < drift < 1e-8  # denser grid ≥ coarser; drift is real but ~7e-10


def test_wrong_coeff_values_fail():
    r = core.verify({"coefficients": [2] * 70}, core.get_verifier(12))
    assert not r.passed  # not in {+1,-1} → honest-zero
