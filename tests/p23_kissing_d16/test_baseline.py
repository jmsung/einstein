"""Tests for the BW16 baseline construction."""

from __future__ import annotations

import numpy as np

from einstein.p23_kissing_d16.baseline import (
    bw16_min_vectors,
    bw16_plus_duplicate,
    extended_hamming_16_11_4,
)
from einstein.p23_kissing_d16.evaluator import overlap_loss_fast


def test_extended_hamming_dimensions() -> None:
    code = extended_hamming_16_11_4()
    assert code.shape == (2048, 16)
    weights = code.sum(axis=1)
    counts = dict(zip(*np.unique(weights, return_counts=True)))
    assert counts == {0: 1, 4: 140, 6: 448, 8: 870, 10: 448, 12: 140, 16: 1}
    assert set(np.unique(code).tolist()) == {0, 1}


def test_bw16_unit_norm_and_kissing_tight() -> None:
    bw = bw16_min_vectors()
    assert bw.shape == (4320, 16)
    assert np.allclose(np.linalg.norm(bw, axis=1), 1.0)
    # All 4320 vectors form a perfect kissing config: zero overlap loss.
    assert overlap_loss_fast(bw) == 0.0


def test_bw16_plus_duplicate_score_two() -> None:
    bwd = bw16_plus_duplicate()
    assert bwd.shape == (4321, 16)
    assert overlap_loss_fast(bwd) == 2.0


def test_inner_product_spectrum() -> None:
    """BW16 inner products lie in {-1, -1/2, -1/4, 0, +1/4, +1/2}."""
    bw = bw16_min_vectors()
    gram = bw @ bw.T
    np.fill_diagonal(gram, 0.0)
    unique_ips = np.unique(np.round(gram, 8))
    expected = {-1.0, -0.5, -0.25, 0.0, 0.25, 0.5}
    assert set(unique_ips.tolist()).issubset(expected)
