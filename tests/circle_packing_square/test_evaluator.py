"""Tests for the Circle Packing in a Square (n=26) evaluator."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pytest

from einstein.circle_packing_square.evaluator import (
    N_CIRCLES,
    evaluate,
    evaluate_strict,
    evaluate_verbose,
)

RESULTS = Path("results/problem-14-circle-packing-square")


def _identity_packing() -> np.ndarray:
    """A trivially valid 26-circle config: grid of small circles."""
    circles = np.zeros((N_CIRCLES, 3))
    r = 0.04
    for k in range(N_CIRCLES):
        i, j = k // 6, k % 6
        circles[k] = (0.1 + 0.15 * j, 0.1 + 0.15 * i, r)
    return circles


def test_evaluate_shape_check():
    with pytest.raises(ValueError):
        evaluate({"circles": [[0.0, 0.0, 0.1]]})


def test_evaluate_valid_trivial():
    circles = _identity_packing()
    score = evaluate({"circles": circles.tolist()})
    assert abs(score - N_CIRCLES * 0.04) < 1e-12


def test_evaluate_rejects_overlap():
    """Two circles on top of each other must fail."""
    circles = _identity_packing()
    circles[1, 0] = circles[0, 0]  # overlap circles 0 and 1
    circles[1, 1] = circles[0, 1]
    with pytest.raises(AssertionError):
        evaluate({"circles": circles.tolist()})


def test_evaluate_rejects_outside_square():
    """A circle crossing the wall must fail."""
    circles = _identity_packing()
    circles[0, 0] = -0.1  # outside left wall
    with pytest.raises(AssertionError):
        evaluate({"circles": circles.tolist()})


def test_evaluator_strict_tolerance_zero():
    """Identity packing must pass with tol=0."""
    circles = _identity_packing()
    sol = {"circles": circles.tolist()}
    evaluate_strict(sol)


def test_solution_best_strict_valid():
    """The committed solution-best.json must validate strictly (tol=0)."""
    sol_path = RESULTS / "solution-best.json"
    if not sol_path.exists():
        pytest.skip("solution-best.json not built")
    with open(sol_path) as f:
        sol = json.load(f)
    # Strict verification — must match arena's tol=0 gate
    score = evaluate_strict(sol)
    v = evaluate_verbose(sol)
    assert v["worst_overlap"] >= 0, f"negative overlap: {v['worst_overlap']}"
    # Score sanity: near the known ceiling (~2.6359830849)
    assert 2.63 < score < 2.64
