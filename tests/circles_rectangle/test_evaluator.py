"""Tests for the Circles in Rectangle (n=21) evaluator and polisher."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pytest

from einstein.circles_rectangle.evaluator import (
    N_CIRCLES,
    PERIMETER_BOUND,
    evaluate,
    evaluate_verbose,
    minimum_circumscribing_rectangle,
)
from einstein.circles_rectangle.polish import polish

RESULTS = Path("results/problem-17-circles-rectangle")


def _identity_packing() -> np.ndarray:
    """A trivially valid 21-circle config: 21 small circles on a grid."""
    circles = np.zeros((21, 3))
    r = 0.05
    for k in range(21):
        i, j = k // 7, k % 7
        circles[k] = (0.1 + 0.15 * j, 0.1 + 0.2 * i, r)
    return circles


def test_evaluate_shape_check():
    with pytest.raises(ValueError):
        evaluate({"circles": [[0.0, 0.0, 0.1]]})


def test_evaluate_valid_trivial():
    circles = _identity_packing()
    score = evaluate({"circles": circles.tolist()})
    assert abs(score - 21 * 0.05) < 1e-12


def test_minimum_circumscribing_rectangle_basic():
    circles = np.array([[0.5, 0.5, 0.5]])
    w, h = minimum_circumscribing_rectangle(circles)
    assert w == 1.0 and h == 1.0


def test_polish_alphaevolve_recovers_basin():
    """SLSQP polish of AlphaEvolve start must reach the published basin floor."""
    ae_path = RESULTS / "sota-AlphaEvolve-2.3658321334168.json"
    if not ae_path.exists():
        pytest.skip("AE solution not downloaded")
    with open(ae_path) as f:
        ae = json.load(f)
    polished, w, info = polish(np.array(ae["circles"]), maxiter=500)
    # Polished score must improve on the start by at least 1e-8
    start = float(np.sum(np.array(ae["circles"])[:, 2]))
    assert info["score"] > start + 1e-8
    # And it should reach the basin floor (~2.36583237591)
    assert info["score"] > 2.36583237590


def test_solution_best_is_valid_and_in_window():
    """The committed solution-best.json must validate strictly and sit in the rank-2 window."""
    sol_path = RESULTS / "solution-best.json"
    if not sol_path.exists():
        pytest.skip("solution-best.json not built")
    with open(sol_path) as f:
        sol = json.load(f)
    # tol=0 strict
    score = evaluate(sol, tol=0)
    v = evaluate_verbose(sol)
    assert v["worst_overlap"] >= 0
    assert v["perimeter"] <= PERIMETER_BOUND
    # Window: above AE (#2) by > 1e-7, below capybara (#1) by > 1e-7
    SOTA = 2.3658323759185156
    SECOND = 2.3658321334168
    assert score - SECOND > 1e-7
    assert SOTA - score > 1e-7


def test_evaluator_strict_tolerance_zero():
    """Identity packing must pass with tol=0."""
    circles = _identity_packing()
    sol = {"circles": circles.tolist()}
    evaluate(sol, tol=0)
