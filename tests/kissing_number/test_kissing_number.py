"""Tests for the Kissing Number evaluator (Problem 6)."""

import json

import numpy as np
import pytest

from einstein.kissing_number.evaluator import (
    evaluate,
    exact_check,
    overlap_loss,
    overlap_loss_fast,
)

RESULTS_DIR = "results/problem-6-kissing-number"


# --- Input validation ---


def test_wrong_shape_raises():
    with pytest.raises(ValueError, match="Expected shape"):
        evaluate({"vectors": np.zeros((10, 11)).tolist()})


def test_wrong_dimension_raises():
    with pytest.raises(ValueError, match="Expected shape"):
        evaluate({"vectors": np.zeros((594, 5)).tolist()})


def test_zero_vector_raises():
    vecs = np.random.default_rng(0).standard_normal((594, 11))
    vecs[0] = 0
    with pytest.raises(ValueError, match="non-zero"):
        evaluate({"vectors": vecs.tolist()})


# --- Basic scoring ---


def test_orthogonal_vectors_score_zero():
    """11 orthogonal unit vectors have no overlap (all dists = 2)."""
    vecs = np.eye(11)
    # Pad to 594 with copies won't work (copies have dist 0).
    # But 11 orthogonal vectors should have zero overlap among themselves.
    # We can't call evaluate (needs 594), so test overlap_loss directly.
    loss = overlap_loss(vecs)
    assert loss == 0.0


def test_identical_vectors_high_penalty():
    """594 copies of the same vector should have maximum penalty."""
    vecs = np.tile([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], (594, 1)).astype(float)
    # All pairs have dist=0, penalty=2 each. n_pairs = 594*593/2 = 176121
    score = evaluate({"vectors": vecs.tolist()})
    expected = 2.0 * 594 * 593 / 2
    assert abs(score - expected) < 1e-6


def test_two_opposite_vectors_no_penalty():
    """Two antipodal vectors have distance 4, no penalty."""
    vecs = np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=float)
    loss = overlap_loss(vecs)
    assert loss == 0.0


# --- Exact integer check ---


def test_exact_check_orthogonal():
    """Standard basis vectors pass exact check."""
    vecs = np.eye(11)
    assert exact_check(vecs) is True


def test_exact_check_d11_kissing():
    """D_11 lattice kissing vectors: permutations of (±1, ±1, 0, ..., 0)."""
    vecs = []
    for i in range(11):
        for j in range(i + 1, 11):
            for si in [-1, 1]:
                for sj in [-1, 1]:
                    v = [0] * 11
                    v[i] = si
                    v[j] = sj
                    vecs.append(v)
    vecs = np.array(vecs, dtype=float)
    assert vecs.shape == (220, 11)
    # All squared norms = 2, min squared dist = 2 (e.g., (+1,+1,0,...) vs (+1,-1,0,...))
    assert exact_check(vecs) is True


def test_exact_check_fails_for_float():
    """Non-integer vectors should fail exact check."""
    vecs = np.random.default_rng(42).standard_normal((10, 11))
    assert exact_check(vecs) is False


# --- Fast vs standard agreement ---


def test_fast_matches_standard():
    """overlap_loss_fast should match overlap_loss within floating point."""
    rng = np.random.default_rng(123)
    vecs = rng.standard_normal((100, 11))
    loss_std = overlap_loss(vecs)
    loss_fast = overlap_loss_fast(vecs)
    assert abs(loss_std - loss_fast) < 1e-8, f"std={loss_std}, fast={loss_fast}"


# --- SOTA validation ---


@pytest.fixture
def sota_vectors():
    with open(f"{RESULTS_DIR}/sota_vectors.json") as f:
        data = json.load(f)
    return np.array(data["vectors"], dtype=np.float64)


@pytest.fixture
def sota_score():
    with open(f"{RESULTS_DIR}/sota_vectors.json") as f:
        data = json.load(f)
    return data["score"]


def test_sota_shape(sota_vectors):
    assert sota_vectors.shape == (594, 11)


def test_sota_reproduces_score(sota_vectors, sota_score):
    """Our evaluator must match the arena score for the SOTA solution."""
    our_score = evaluate({"vectors": sota_vectors.tolist()})
    # Match to 8 decimal places (arena uses float64)
    assert abs(our_score - sota_score) < 1e-8, (
        f"Our score {our_score} != arena score {sota_score}"
    )


def test_sota_fast_matches(sota_vectors, sota_score):
    """Fast evaluator should also match SOTA score."""
    fast_score = overlap_loss_fast(sota_vectors)
    assert abs(fast_score - sota_score) < 1e-6, (
        f"Fast score {fast_score} != arena score {sota_score}"
    )


def test_determinism(sota_vectors):
    """Same input must always produce the same score."""
    s1 = evaluate({"vectors": sota_vectors.tolist()})
    s2 = evaluate({"vectors": sota_vectors.tolist()})
    assert s1 == s2
