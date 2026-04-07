"""Tests for the Tammes evaluator (matches arena verifier exactly)."""

import numpy as np
import pytest

from einstein.tammes.evaluator import evaluate, min_distance, project_to_sphere


def _golden_set():
    """50 random unit vectors with a fixed seed — known min distance."""
    rng = np.random.default_rng(42)
    P = rng.standard_normal((50, 3))
    P = P / np.linalg.norm(P, axis=1, keepdims=True)
    return P


def test_identical_points_score_zero():
    P = np.zeros((50, 3))
    P[:, 0] = 1.0
    # All identical points → min dist = 0
    s = evaluate({"vectors": P.tolist()})
    assert s < 1e-10


def test_unit_normalization():
    P = _golden_set() * 7.5  # scale so norms != 1
    s_scaled = evaluate({"vectors": P.tolist()})
    s_unit = evaluate({"vectors": (P / np.linalg.norm(P, axis=1, keepdims=True)).tolist()})
    assert abs(s_scaled - s_unit) < 1e-12


def test_invalid_shape():
    with pytest.raises(AssertionError):
        evaluate({"vectors": np.zeros((49, 3)).tolist()})
    with pytest.raises(AssertionError):
        evaluate({"vectors": np.zeros((50, 4)).tolist()})


def test_min_distance_consistency():
    """min_distance and evaluate should agree for unit-normalized inputs."""
    P = _golden_set()
    s1 = evaluate({"vectors": P.tolist()})
    s2 = min_distance(P)
    # Numerical methods differ slightly (one uses gram, one uses diff)
    assert abs(s1 - s2) < 1e-12


def test_score_known_solution():
    """If we have a known good solution in the results dir, verify it scores
    in the right ballpark (≥ 0.5)."""
    import json
    from pathlib import Path

    results = Path(__file__).resolve().parents[2] / "results" / "problem-11-tammes"
    sols = list(results.glob("solution-*.json"))
    if not sols:
        pytest.skip("no solutions yet")
    for sp in sols:
        with open(sp) as f:
            d = json.load(f)
        s = evaluate(d)
        assert s > 0.5, f"{sp.name}: score {s} too low"
        assert s < 0.6, f"{sp.name}: score {s} too high (sanity check)"


def test_arena_verifier_exact_replica():
    """Run the arena verifier code verbatim and compare to ours."""
    P = _golden_set() * 1.7  # non-unit input

    # Verbatim from the API:
    def arena_evaluate(data):
        vectors = np.array(data["vectors"], dtype=np.float64)
        assert vectors.shape == (50, 3), f"Expected (50, 3), got {vectors.shape}"
        norms = np.linalg.norm(vectors, axis=1, keepdims=True)
        norms[norms < 1e-12] = 1e-12
        vectors = vectors / norms
        diffs = vectors[:, None, :] - vectors[None, :, :]
        dist_sq = np.sum(diffs**2, axis=2)
        iu = np.triu_indices(50, k=1)
        dists = np.sqrt(dist_sq[iu])
        return float(np.min(dists))

    s_ours = evaluate({"vectors": P.tolist()})
    s_arena = arena_evaluate({"vectors": P.tolist()})
    assert s_ours == s_arena
