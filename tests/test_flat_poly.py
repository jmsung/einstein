"""Tests for the Flat Polynomials evaluator (Problem 12).

Verifies that our local evaluator exactly matches the arena's scoring function.
Comprehensive coverage: constraints, scoring correctness, mathematical properties,
arena cross-validation, and performance.
"""

import time

import numpy as np
import pytest
from einstein.flat_poly import compute_score, evaluate


# ---------------------------------------------------------------------------
# Reference: independent FFT-based scoring for cross-validation
# ---------------------------------------------------------------------------
def _arena_verify(coefficients):
    """Independent implementation via FFT — cross-check against np.poly1d.

    Reverses coefficients to ascending order, then uses FFT to evaluate
    the polynomial at 1M unit circle points. Different algorithm than
    the evaluator's Horner method, so a genuine cross-check.
    """
    coeffs = np.array(coefficients, dtype=np.float64)
    assert len(coeffs) == 70
    assert all(c in (-1, 1) for c in coeffs)
    # Reverse to ascending order [a_0, a_1, ..., a_69] for FFT
    ascending = coeffs[::-1]
    # FFT evaluates p(z) at z = exp(-2πi k/N), same set of points as exp(+2πi k/N)
    fft_vals = np.fft.fft(ascending, n=1_000_000)
    return float(np.max(np.abs(fft_vals)) / np.sqrt(71))


# ---------------------------------------------------------------------------
# Input validation
# ---------------------------------------------------------------------------
class TestConstraints:
    """Input validation — reject bad inputs fast."""

    def test_wrong_length_short(self):
        with pytest.raises(AssertionError, match="70"):
            evaluate({"coefficients": [1] * 69})

    def test_wrong_length_long(self):
        with pytest.raises(AssertionError, match="70"):
            evaluate({"coefficients": [1] * 71})

    def test_non_pm1_rejected(self):
        coeffs = [1] * 70
        coeffs[5] = 2
        with pytest.raises(AssertionError, match="must be"):
            evaluate({"coefficients": coeffs})

    def test_zero_rejected(self):
        coeffs = [1] * 70
        coeffs[0] = 0
        with pytest.raises(AssertionError, match="must be"):
            evaluate({"coefficients": coeffs})

    def test_nan_rejected(self):
        coeffs = [1.0] * 70
        coeffs[3] = float("nan")
        with pytest.raises(AssertionError, match="NaN"):
            evaluate({"coefficients": coeffs})

    def test_missing_key_rejected(self):
        with pytest.raises(KeyError):
            evaluate({"values": [1] * 70})

    def test_float_pm1_accepted(self):
        """±1.0 floats should work (they equal ±1 exactly)."""
        coeffs = [1.0] * 35 + [-1.0] * 35
        score = evaluate({"coefficients": coeffs})
        assert score > 0


# ---------------------------------------------------------------------------
# Scoring correctness — known shapes
# ---------------------------------------------------------------------------
class TestScoring:
    """Scoring correctness for known polynomial shapes."""

    def test_all_ones(self):
        """p(z) = z^69 + z^68 + ... + 1. At z=1: p(1) = 70.
        Score = 70 / sqrt(71) ≈ 8.307."""
        score = evaluate({"coefficients": [1] * 70})
        expected = 70.0 / np.sqrt(71)
        assert score == pytest.approx(expected, rel=1e-6)

    def test_all_neg_ones(self):
        """p(z) = -(z^69 + ... + 1). At z=1: |p(1)| = 70.
        Same score as all-ones."""
        score_pos = evaluate({"coefficients": [1] * 70})
        score_neg = evaluate({"coefficients": [-1] * 70})
        assert score_pos == pytest.approx(score_neg, rel=1e-12)

    def test_alternating_at_minus_one(self):
        """Alternating [1, -1, 1, -1, ...].
        At z=-1: p(-1) = sum_{k=0}^{69} (-1)^k * (-1)^(69-k) = -70.
        Score = 70 / sqrt(71)."""
        coeffs = [(-1) ** k for k in range(70)]
        score = evaluate({"coefficients": coeffs})
        expected = 70.0 / np.sqrt(71)
        assert score == pytest.approx(expected, rel=1e-6)

    def test_score_positive(self):
        """Score is always positive for valid inputs."""
        for seed in range(5):
            rng = np.random.default_rng(seed)
            coeffs = rng.choice([-1, 1], size=70).tolist()
            assert evaluate({"coefficients": coeffs}) > 0


# ---------------------------------------------------------------------------
# Mathematical properties
# ---------------------------------------------------------------------------
class TestMathProperties:
    """Properties that the score must satisfy."""

    def test_parseval_lower_bound(self):
        """By Parseval: ||p||_2 = sqrt(70). Since ||p||_inf >= ||p||_2,
        score >= sqrt(70)/sqrt(71) ≈ 0.993."""
        lower = np.sqrt(70) / np.sqrt(71)
        for seed in range(10):
            rng = np.random.default_rng(seed)
            coeffs = rng.choice([-1, 1], size=70).tolist()
            score = evaluate({"coefficients": coeffs})
            assert score >= lower - 1e-6, f"seed={seed}: {score} < {lower}"

    def test_deterministic(self):
        """Same coefficients always give same score."""
        coeffs = [1, -1] * 35
        s1 = evaluate({"coefficients": coeffs})
        s2 = evaluate({"coefficients": coeffs})
        assert s1 == s2

    def test_negation_same_score(self):
        """Negating all coefficients: |-p(z)| = |p(z)|. Same score."""
        rng = np.random.default_rng(7)
        coeffs = rng.choice([-1, 1], size=70).tolist()
        neg_coeffs = [-c for c in coeffs]
        s1 = evaluate({"coefficients": coeffs})
        s2 = evaluate({"coefficients": neg_coeffs})
        assert s1 == pytest.approx(s2, rel=1e-12)

    def test_reversal_same_score(self):
        """Reversing coefficients: p_rev(z) = z^69 * p(1/z).
        On the unit circle |z|=1, |p_rev(z)| = |p(1/z)| = |p(z̄)|.
        Max over unit circle is same."""
        rng = np.random.default_rng(13)
        coeffs = rng.choice([-1, 1], size=70).tolist()
        rev_coeffs = coeffs[::-1]
        s1 = evaluate({"coefficients": coeffs})
        s2 = evaluate({"coefficients": rev_coeffs})
        assert s1 == pytest.approx(s2, rel=1e-6)


# ---------------------------------------------------------------------------
# Arena cross-validation (the critical test)
# ---------------------------------------------------------------------------
class TestArenaMatch:
    """Cross-validate against independent FFT implementation."""

    @pytest.mark.parametrize("seed", range(10))
    def test_random_coefficients_match(self, seed):
        """Random ±1 polynomials: poly1d and FFT must agree."""
        rng = np.random.default_rng(seed)
        coeffs = rng.choice([-1, 1], size=70).tolist()
        ours = evaluate({"coefficients": coeffs})
        arena = _arena_verify(coeffs)
        assert ours == pytest.approx(arena, rel=1e-6), (
            f"seed={seed}: ours={ours}, arena={arena}"
        )

    def test_all_ones_match(self):
        coeffs = [1] * 70
        assert evaluate({"coefficients": coeffs}) == pytest.approx(
            _arena_verify(coeffs), rel=1e-6
        )

    def test_asymmetric_match(self):
        """Asymmetric polynomial — verifies coefficient ordering."""
        coeffs = [1] * 35 + [-1] * 35
        assert evaluate({"coefficients": coeffs}) == pytest.approx(
            _arena_verify(coeffs), rel=1e-6
        )

    def test_compute_score_matches_evaluate(self):
        """Direct call to compute_score matches evaluate wrapper."""
        rng = np.random.default_rng(99)
        coeffs = rng.choice([-1, 1], size=70).tolist()
        assert compute_score(coeffs) == evaluate({"coefficients": coeffs})


# ---------------------------------------------------------------------------
# Performance
# ---------------------------------------------------------------------------
class TestPerformance:
    """Ensure evaluation is fast enough for optimization."""

    def test_single_eval_under_200ms(self):
        """Single evaluation should complete in < 200ms."""
        coeffs = [1] * 70
        t0 = time.perf_counter()
        for _ in range(3):
            evaluate({"coefficients": coeffs})
        elapsed = (time.perf_counter() - t0) / 3
        assert elapsed < 0.2, f"Single eval took {elapsed:.4f}s (target < 200ms)"
