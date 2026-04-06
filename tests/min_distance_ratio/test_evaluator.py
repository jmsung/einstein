"""Tests for Problem 5 evaluator — must match arena scores exactly."""

import json
from pathlib import Path

import numpy as np
import pytest

from einstein.min_distance_ratio.evaluator import evaluate, evaluate_verbose

FIXTURES = Path(__file__).parent / "fixtures"


def test_shape_validation():
    # Wrong number of points
    with pytest.raises(ValueError, match="shape"):
        evaluate({"vectors": [[0.0, 0.0]] * 15})
    with pytest.raises(ValueError, match="shape"):
        evaluate({"vectors": [[0.0, 0.0]] * 17})
    # Wrong dimension
    with pytest.raises(ValueError, match="shape"):
        evaluate({"vectors": [[0.0, 0.0, 0.0]] * 16})


def test_duplicate_points_rejected():
    verts = [[0.0, 0.0]] * 16
    with pytest.raises(ValueError, match="distinct"):
        evaluate({"vectors": verts})


def test_regular_grid_4x4():
    # 4x4 square grid: min dist = 1, max dist = 3*sqrt(2)
    # Score = (3*sqrt(2))**2 / 1 = 18
    verts = [[i, j] for i in range(4) for j in range(4)]
    score = evaluate({"vectors": verts})
    assert score == pytest.approx(18.0, abs=1e-12)


def test_verbose_regular_grid():
    verts = [[i, j] for i in range(4) for j in range(4)]
    result = evaluate_verbose({"vectors": verts})
    assert result["score"] == pytest.approx(18.0)
    # 4x4 grid has 24 unit edges (horizontal+vertical), 2 max edges (diagonals)
    assert result["min_edges_tight"] == 24
    assert result["max_edges_tight"] == 2


@pytest.mark.parametrize("fixture_name,expected_score", [
    ("together_ai.json", 12.889229907717521),
    ("einstein_ea6391.json", 12.889229908217525),
    ("turing9811.json", 12.889230021301920),
])
def test_arena_parity(fixture_name, expected_score):
    """Local evaluator must match arena-reported scores exactly (strict tol=0)."""
    path = FIXTURES / fixture_name
    if not path.exists():
        pytest.skip(f"fixture missing: {path}")
    data = json.load(open(path))
    score = evaluate(data)
    # Exact float equality — arena uses same numpy code, must match bit-for-bit
    assert score == expected_score, (
        f"Score mismatch: local={score!r} arena={expected_score!r}"
    )
