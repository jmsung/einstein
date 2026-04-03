"""Tests for the Uncertainty Principle evaluators (Problem 18).

Validates both the exact symbolic verifier and the fast numerical evaluator.
"""

import numpy as np
import pytest

from einstein.uncertainty.verifier import evaluate as exact_evaluate
from einstein.uncertainty.fast import fast_evaluate


# Reference k=13 roots for testing
KNOWN_ROOTS = [
    3.1427440085666496, 4.469993893132148, 6.078689469782297,
    32.637646271046336, 38.265477818082566, 41.06153063739393,
    43.09262298321874, 50.81816373872074, 58.61770809389174,
    96.07661117430976, 111.48735817427675, 118.74229251036576,
    141.09580664199572,
]


class TestExactVerifier:
    """Exact symbolic verifier (sympy) tests."""

    def test_known_k13_solution(self):
        score = exact_evaluate({"laguerre_double_roots": KNOWN_ROOTS})
        assert 0.318 < score < 0.320

    def test_empty_roots_rejected(self):
        with pytest.raises(ValueError):
            exact_evaluate({"laguerre_double_roots": []})

    def test_negative_root_rejected(self):
        with pytest.raises(ValueError):
            exact_evaluate({"laguerre_double_roots": [-1.0, 2.0]})

    def test_root_above_300_rejected(self):
        with pytest.raises(ValueError):
            exact_evaluate({"laguerre_double_roots": [1.0, 301.0]})

    def test_too_many_roots_rejected(self):
        with pytest.raises(ValueError):
            exact_evaluate({"laguerre_double_roots": list(range(1, 52))})


class TestFastEvaluator:
    """Fast numerical evaluator (mpmath + numpy) tests."""

    def test_known_k13_solution(self):
        score = fast_evaluate(KNOWN_ROOTS)
        assert 0.318 < score < 0.320

    def test_matches_exact_on_known_solution(self):
        fast = fast_evaluate(KNOWN_ROOTS)
        exact = exact_evaluate({"laguerre_double_roots": KNOWN_ROOTS})
        assert fast == pytest.approx(exact, rel=1e-4)

    def test_k6_solution(self):
        roots = [3.64273649, 5.68246114, 33.00463486, 40.97185579, 50.1028231, 53.76768016]
        score = fast_evaluate(roots)
        assert 0.32 < score < 0.34

    def test_empty_returns_inf(self):
        assert fast_evaluate([]) == np.inf

    def test_negative_root_returns_inf(self):
        assert fast_evaluate([-1.0, 2.0]) == np.inf

    def test_root_above_300_returns_inf(self):
        assert fast_evaluate([1.0, 301.0]) == np.inf

    def test_single_root(self):
        score = fast_evaluate([10.0])
        assert np.isfinite(score)
        assert score > 0

    def test_deterministic(self):
        s1 = fast_evaluate(KNOWN_ROOTS)
        s2 = fast_evaluate(KNOWN_ROOTS)
        assert s1 == s2
