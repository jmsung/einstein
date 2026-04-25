"""Tests for the P23 (kissing d=16) evaluator."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pytest

from einstein.p23_kissing_d16.evaluator import (
    DIMENSION,
    N_VECTORS,
    evaluate,
    exact_check,
    overlap_loss,
    overlap_loss_fast,
    overlap_loss_mpmath,
)

SOTA_PATH = Path.home() / "projects/einstein/mb/knowledge/problem-23-kissing-d16/solutions/chronos_id2082_score2.0.json"


def load_sota() -> np.ndarray:
    with open(SOTA_PATH) as f:
        d = json.load(f)
    return np.array(d["vectors"], dtype=np.float64)


def test_shape_constants() -> None:
    assert N_VECTORS == 4321
    assert DIMENSION == 16


def test_sota_score_matches_arena() -> None:
    """CHRONOS id 2082 is exactly score 2.0 on the arena leaderboard."""
    if not SOTA_PATH.exists():
        pytest.skip("SOTA solution not present locally")
    v = load_sota()
    assert v.shape == (N_VECTORS, DIMENSION)
    assert overlap_loss_fast(v) == 2.0
    assert overlap_loss_mpmath(v, dps=50) == 2.0
    assert overlap_loss_mpmath(v, dps=100) == 2.0


def test_overlap_loss_paths_agree_on_random() -> None:
    rng = np.random.default_rng(42)
    n_small = 50
    v = rng.standard_normal((n_small, DIMENSION))
    a = overlap_loss(v)
    b = overlap_loss_fast(v)
    assert abs(a - b) < 1e-10


def test_evaluate_validates_shape() -> None:
    with pytest.raises(ValueError):
        evaluate({"vectors": np.zeros((10, 5))})


def test_zero_vector_rejected() -> None:
    v = np.eye(DIMENSION)[:N_VECTORS] if N_VECTORS <= DIMENSION else np.zeros((N_VECTORS, DIMENSION))
    v = np.zeros((N_VECTORS, DIMENSION))
    with pytest.raises(ValueError):
        overlap_loss_fast(v)


def test_exact_check_rejects_duplicate() -> None:
    """Even with integer-valued vectors, duplicates make exact_check fail."""
    rng = np.random.default_rng(0)
    n_small = 5
    v = np.eye(DIMENSION, dtype=np.float64)[:n_small].copy()
    v[-1] = v[0]
    assert exact_check(v) is False
