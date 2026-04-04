"""Tests for the Thomson Problem evaluator (Problem 10).

Thomson problem: place 282 points on unit sphere to minimize
Coulomb energy E = sum_{i<j} 1/||p_i - p_j||.
"""

import json

import numpy as np
import pytest

from einstein.thomson.evaluator import (
    coulomb_energy,
    coulomb_energy_fast,
    evaluate,
)

RESULTS_DIR = "results/problem-10-thomson"
N_POINTS = 282
DIMENSION = 3


# --- Input validation ---


def test_wrong_count_raises():
    with pytest.raises(ValueError, match="Expected 282"):
        evaluate({"vectors": np.zeros((10, 3)).tolist()})


def test_wrong_dimension_raises():
    with pytest.raises(ValueError, match="Expected 282"):
        evaluate({"vectors": np.zeros((282, 2)).tolist()})


def test_zero_vector_raises():
    vecs = np.random.default_rng(0).standard_normal((282, 3))
    vecs[0] = 0
    with pytest.raises(ValueError, match="non-zero"):
        evaluate({"vectors": vecs.tolist()})


# --- Basic scoring ---


def test_two_points_antipodal():
    """Two antipodal points on unit sphere: dist=2, energy=0.5."""
    pts = np.array([[0, 0, 1.0], [0, 0, -1.0]])
    energy = coulomb_energy(pts)
    assert abs(energy - 0.5) < 1e-12


def test_two_points_adjacent():
    """Two points at 90 degrees: dist=sqrt(2), energy=1/sqrt(2)."""
    pts = np.array([[1.0, 0, 0], [0, 1.0, 0]])
    energy = coulomb_energy(pts)
    expected = 1.0 / np.sqrt(2.0)
    assert abs(energy - expected) < 1e-12


def test_three_equatorial():
    """Three equidistant points on equator: each pair dist=sqrt(3)."""
    angles = [0, 2 * np.pi / 3, 4 * np.pi / 3]
    pts = np.array([[np.cos(a), np.sin(a), 0] for a in angles])
    energy = coulomb_energy(pts)
    expected = 3.0 / np.sqrt(3.0)  # 3 pairs, each 1/sqrt(3)
    assert abs(energy - expected) < 1e-10


def test_auto_normalization():
    """Points not on unit sphere should be normalized."""
    pts = np.array([[0, 0, 5.0], [0, 0, -3.0]])
    energy = coulomb_energy(pts)
    assert abs(energy - 0.5) < 1e-12


def test_energy_positive():
    """Energy is always positive for distinct points."""
    rng = np.random.default_rng(42)
    pts = rng.standard_normal((50, 3))
    energy = coulomb_energy(pts)
    assert energy > 0


# --- Fast vs standard agreement ---


def test_fast_matches_standard():
    """coulomb_energy_fast should match coulomb_energy within float64."""
    rng = np.random.default_rng(123)
    pts = rng.standard_normal((100, 3))
    e_std = coulomb_energy(pts)
    e_fast = coulomb_energy_fast(pts)
    assert abs(e_std - e_fast) / e_std < 1e-10, f"std={e_std}, fast={e_fast}"


# --- Distance clamping ---


def test_coincident_points_clamped():
    """Coincident points should have clamped distance, not inf."""
    pts = np.array([[1.0, 0, 0], [1.0, 0, 0], [0, 1.0, 0]])
    energy = coulomb_energy(pts)
    assert np.isfinite(energy)


# --- SOTA validation ---


@pytest.fixture
def sota_arena():
    with open(f"{RESULTS_DIR}/sota_arena.json") as f:
        return json.load(f)


@pytest.fixture
def sota_wales():
    with open(f"{RESULTS_DIR}/sota_wales.json") as f:
        return json.load(f)


def test_sota_arena_shape(sota_arena):
    vecs = np.array(sota_arena["vectors"])
    assert vecs.shape == (282, 3)


def test_sota_arena_reproduces_score(sota_arena):
    """Our evaluator must match the arena score for the SOTA solution."""
    our_score = evaluate({"vectors": sota_arena["vectors"]})
    arena_score = sota_arena["score"]
    assert abs(our_score - arena_score) < 1e-6, (
        f"Our score {our_score} != arena score {arena_score}"
    )


def test_sota_wales_energy(sota_wales):
    """Wales database coordinates should give near-SOTA energy."""
    our_score = evaluate({"vectors": sota_wales["vectors"]})
    # Wales coordinates may have limited precision, so allow wider tolerance
    assert our_score < 37148.0, f"Wales energy {our_score} too high"


def test_fast_matches_sota(sota_arena):
    """Fast evaluator should match SOTA score."""
    vecs = np.array(sota_arena["vectors"], dtype=np.float64)
    fast_score = coulomb_energy_fast(vecs)
    arena_score = sota_arena["score"]
    assert abs(fast_score - arena_score) < 1e-4, (
        f"Fast score {fast_score} != arena score {arena_score}"
    )


def test_determinism(sota_arena):
    """Same input must always produce the same score."""
    s1 = evaluate({"vectors": sota_arena["vectors"]})
    s2 = evaluate({"vectors": sota_arena["vectors"]})
    assert s1 == s2
