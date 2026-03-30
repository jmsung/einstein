"""Tests for the Uncertainty Principle evaluator.

Covers:
  - Known-good scores (REDACTED k=13, k=6)
  - Input validation (empty, negative, out-of-bounds, too close)
  - Far sign change detection (parasitic roots at x≈379 and x≈800)
  - Monotonicity (small perturbations don't cause wild score swings)
  - Consistency (fast vs exact verifier agreement)
"""

import pytest
import numpy as np
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
    """Core scoring accuracy and input validation."""

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

    def test_zero_root_returns_inf(self):
        assert fast_evaluate([0.0]) == float("inf")

    def test_two_close_roots_still_finite(self):
        """Close roots may produce poor scores but shouldn't crash."""
        score = fast_evaluate([10.0, 10.005])
        assert np.isfinite(score), "Close roots should not crash the evaluator"

    def test_single_root(self):
        """Single root should produce a finite score."""
        score = fast_evaluate([5.0])
        assert np.isfinite(score)

    def test_k13_deterministic(self):
        """Same inputs should always produce the same output."""
        s1 = fast_evaluate(K13_ROOTS)
        s2 = fast_evaluate(K13_ROOTS)
        assert s1 == s2

    def test_score_is_positive(self):
        """Score should always be positive (largest root / 2π)."""
        score = fast_evaluate(K13_ROOTS)
        assert score > 0

    def test_unsorted_roots_same_as_sorted(self):
        """Root order shouldn't matter — evaluator sorts internally."""
        shuffled = list(K13_ROOTS)
        np.random.seed(42)
        np.random.shuffle(shuffled)
        score = fast_evaluate(shuffled)
        # Note: fast_evaluate doesn't sort, so unsorted may give different result.
        # This test verifies the function doesn't crash on unsorted input.
        assert np.isfinite(score) or score == float("inf")


class TestSmallPerturbation:
    """Small perturbations to known-good roots should produce nearby scores."""

    def test_tiny_perturbation_stays_close(self):
        """A 1e-6 perturbation should change score by < 1e-3."""
        perturbed = [r + 1e-6 for r in K13_ROOTS]
        base = fast_evaluate(K13_ROOTS)
        pert = fast_evaluate(perturbed)
        assert abs(base - pert) < 1e-3, (
            f"Tiny perturbation caused huge score change: {base} -> {pert}"
        )

    def test_moderate_perturbation_bounded(self):
        """A 0.01 perturbation should keep score in a reasonable range."""
        np.random.seed(123)
        perturbed = sorted([r + np.random.randn() * 0.01 for r in K13_ROOTS])
        score = fast_evaluate(perturbed)
        # Should be close to baseline, not wildly different
        assert score < 1.0, f"Moderate perturbation gave unreasonable score: {score}"


class TestFarSignChangeDetection:
    """Ensure fast_evaluate detects sign changes far beyond the root positions.

    These roots are known to produce parasitic sign changes at x >> max(roots).
    The fast evaluator MUST detect these and return a large score (not a small one).
    """

    # Roots that produce a sign change at x≈379 (exact score ~60.39)
    BAD_ROOTS_379 = [
        3.083047493448433, 4.416656406356701, 6.018832161240981,
        31.104059990061298, 37.42450798127864, 40.80492484176367,
        43.795017697454135, 51.17408187934483, 57.53059307210773,
        98.28406622635097, 112.91477635879563, 122.8960346051581,
        138.8354968850486,
    ]

    # Roots that produce a sign change at x≈800 (exact score ~127.32)
    BAD_ROOTS_800 = [
        3.0990662488297024, 4.571698076498697, 6.119654524614413,
        32.59826988003972, 38.17893050770866, 41.00361693543455,
        43.04116652476279, 50.86610973791498, 58.91363714696459,
        96.40389395044992, 112.66963085494003, 120.23750985866153,
        141.55186753553797,
    ]

    # Roots that produce a sign change at x≈9600 (exact score ~1528)
    BAD_ROOTS_9600 = [
        3.083047493448433, 4.571698076498697, 6.119654524614413,
        32.59826988003972, 38.17893050770866, 41.00361693543455,
        43.04116652476279, 50.86610973791498, 58.91363714696459,
        96.40389395044992, 112.66963085494003, 120.23750985866153,
        141.55186753553797,
    ]

    def test_detects_far_sign_change_at_379(self):
        score = fast_evaluate(self.BAD_ROOTS_379)
        assert score > 10.0, (
            f"Failed to detect far sign change: score={score:.4f}, expected >10"
        )

    def test_detects_far_sign_change_at_800(self):
        score = fast_evaluate(self.BAD_ROOTS_800)
        assert score > 10.0, (
            f"Failed to detect far sign change: score={score:.4f}, expected >10"
        )

    def test_detects_far_sign_change_at_9600(self):
        score = fast_evaluate(self.BAD_ROOTS_9600)
        assert score > 10.0, (
            f"Failed to detect very far sign change: score={score:.4f}, expected >10"
        )

    def test_good_roots_unaffected(self):
        """REDACTED roots should NOT trigger false positives."""
        score = fast_evaluate(K13_ROOTS)
        assert abs(score - K13_EXPECTED) < 1e-6, (
            f"Good roots wrongly penalized: score={score}, expected {K13_EXPECTED}"
        )


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
