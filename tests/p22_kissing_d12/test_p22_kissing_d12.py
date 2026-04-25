"""Tests for the Kissing Number d=12 evaluator (Problem 22).

CHRONOS's public SOTA payload (840-vector Leech-Sloane P_{12a} + 1 duplicate
of (1,0,...,0)) must score exactly 2.0 — this is the parity check against
the arena's reported value.
"""

import json
import pathlib

import numpy as np
import pytest

from einstein.p22_kissing_d12.evaluator import (
    DIMENSION,
    N_VECTORS,
    evaluate,
    exact_check,
    overlap_loss,
    overlap_loss_fast,
    overlap_loss_mpmath,
)

RESULTS_DIR = pathlib.Path(__file__).parent.parent.parent / "results" / "p22_kissing_d12"
_CHRONOS_FILE = RESULTS_DIR / "sota_best_chronos_rank1_id2081.json"
_ORGANON_FILE = RESULTS_DIR / "sota_best_organonagent_rank2_id1965.json"


# --- Input validation ---


def test_wrong_shape_raises():
    with pytest.raises(ValueError, match="Expected shape"):
        evaluate({"vectors": np.zeros((10, DIMENSION)).tolist()})


def test_wrong_dimension_raises():
    with pytest.raises(ValueError, match="Expected shape"):
        evaluate({"vectors": np.zeros((N_VECTORS, 5)).tolist()})


def test_zero_vector_raises():
    rng = np.random.default_rng(0)
    vecs = rng.standard_normal((N_VECTORS, DIMENSION))
    vecs[0] = 0
    with pytest.raises(ValueError, match="non-zero"):
        overlap_loss(vecs)


# --- Scoring correctness ---


def test_orthogonal_basis_score_zero():
    """12 orthogonal vectors + 829 duplicates: orthogonal pairs have dist=2."""
    vecs = np.zeros((N_VECTORS, DIMENSION))
    vecs[:DIMENSION] = np.eye(DIMENSION)
    vecs[DIMENSION:] = np.eye(DIMENSION)[0]  # filler all copies of e_1
    # Many duplicates: each of the 829 filler pairs gives overlap 2, plus
    # each filler with vecs[0] gives overlap 2. Not a zero-score config —
    # just a sanity that the loss runs.
    s = overlap_loss(vecs)
    assert s > 0


def test_chronos_sota_matches_arena_2_0():
    if not _CHRONOS_FILE.exists():
        pytest.skip(f"CHRONOS SOTA file not found: {_CHRONOS_FILE}")
    data = json.loads(_CHRONOS_FILE.read_text())
    vecs = np.array(data["vectors"], dtype=np.float64)
    assert vecs.shape == (N_VECTORS, DIMENSION)

    # Float64 fast paths
    s_fast = overlap_loss_fast(vecs)
    s_slow = overlap_loss(vecs)
    assert abs(s_fast - 2.0) < 1e-12
    assert abs(s_slow - 2.0) < 1e-12
    assert abs(s_fast - s_slow) < 1e-14

    # mpmath ground truth matches arena's 2.000000000000000 exactly
    s_mp = overlap_loss_mpmath(vecs, dps=50)
    assert s_mp == 2.0


def test_organon_sota_matches_arena_2_0_plus_5p7e_12():
    """Arena verifier path is the diff-based overlap_loss (not dot-product
    or mpmath) — confirmed by parity to 1 ulp against Organon's submission.
    """
    if not _ORGANON_FILE.exists():
        pytest.skip(f"OrganonAgent SOTA file not found: {_ORGANON_FILE}")
    data = json.loads(_ORGANON_FILE.read_text())
    vecs = np.array(data["vectors"], dtype=np.float64)
    s_slow = overlap_loss(vecs)
    # Arena reported 2.000000000005719; local float64 diff-based = 2.0000000000057208
    assert abs(s_slow - 2.000000000005719) < 1e-14


def test_fast_vs_slow_agree_on_random():
    rng = np.random.default_rng(42)
    vecs = rng.standard_normal((N_VECTORS, DIMENSION))
    s_fast = overlap_loss_fast(vecs)
    s_slow = overlap_loss(vecs)
    # Random config: many overlapping pairs, loss is large; both paths
    # use the same arithmetic so should agree to ~1e-8 relative.
    assert abs(s_fast - s_slow) < max(1e-8, 1e-10 * s_slow)


def test_exact_check_rejects_chronos_duplicate():
    """CHRONOS's config has a duplicate of (1,0,...,0) — so the duplicate
    pair has squared distance 0 < max_sq_norm, exact_check returns False.
    """
    if not _CHRONOS_FILE.exists():
        pytest.skip(f"CHRONOS SOTA file not found: {_CHRONOS_FILE}")
    data = json.loads(_CHRONOS_FILE.read_text())
    vecs = np.array(data["vectors"], dtype=np.float64)
    assert exact_check(vecs) is False
