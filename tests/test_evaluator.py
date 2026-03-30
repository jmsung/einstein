"""Tests for the Uncertainty Principle evaluator."""

import pytest
from einstein.fast_eval import fast_evaluate
from einstein.verifier import evaluate

# REDACTED's best k=13 roots
K13_ROOTS = [
    3.1427440085666496, 4.469993893132148, 6.078689469782297,
    32.637646271046336, 38.265477818082566, 41.06153063739393,
    43.09262298321874, 50.81816373872074, 58.61770809389174,
    96.07661117430976, 111.48735817427675, 118.74229251036576,
    141.09580664199572,
]
K13_EXPECTED = REDACTED

K6_ROOTS = [3.64273649, 5.68246114, 33.00463486, 40.97185579, 50.1028231, 53.76768016]
K6_EXPECTED = 0.3282706174313453


class TestFastEvaluate:
    def test_k13_score(self):
        score = fast_evaluate(K13_ROOTS)
        assert abs(score - K13_EXPECTED) < 1e-6, f"k=13 score {score} != {K13_EXPECTED}"

    def test_k6_score(self):
        score = fast_evaluate(K6_ROOTS)
        assert abs(score - K6_EXPECTED) < 1e-6, f"k=6 score {score} != {K6_EXPECTED}"

    def test_empty_roots_returns_inf(self):
        assert fast_evaluate([]) == float("inf")

    def test_negative_root_returns_inf(self):
        assert fast_evaluate([-1.0]) == float("inf")

    def test_root_exceeds_300_returns_inf(self):
        assert fast_evaluate([301.0]) == float("inf")


class TestFastVsExactVerifier:
    """Ensure fast_evaluate agrees with the exact SymPy verifier."""

    @pytest.mark.slow
    def test_k6_fast_matches_exact(self):
        fast_score = fast_evaluate(K6_ROOTS)
        exact_score = evaluate({"laguerre_double_roots": K6_ROOTS})
        assert abs(fast_score - exact_score) < 1e-6, (
            f"fast={fast_score}, exact={exact_score}"
        )

    @pytest.mark.slow
    def test_k13_fast_matches_exact(self):
        fast_score = fast_evaluate(K13_ROOTS)
        exact_score = evaluate({"laguerre_double_roots": K13_ROOTS})
        assert abs(fast_score - exact_score) < 1e-6, (
            f"fast={fast_score}, exact={exact_score}"
        )
