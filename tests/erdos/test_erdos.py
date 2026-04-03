"""Tests for the Erdos minimum overlap evaluator (Problem 1).

Verifies that our local evaluator exactly matches the arena's scoring function.
Comprehensive coverage: constraints, scoring correctness, mathematical properties,
edge cases, performance, and arena cross-validation.
"""

import time

import numpy as np
import pytest
from einstein.erdos.evaluator import _normalize_sum_constraint, compute_upper_bound, evaluate


# ---------------------------------------------------------------------------
# Reference: inline arena verifier for cross-validation
# ---------------------------------------------------------------------------
def _arena_verify(values):
    """Exact copy of the arena verifier — used as ground truth."""
    sequence_array = np.array(values, dtype=np.float64)
    if np.isnan(sequence_array).any():
        raise AssertionError("The sequence contains NaN values.")
    if np.any(sequence_array < 0) or np.any(sequence_array > 1):
        raise AssertionError("All values in the sequence must be between 0 and 1.")
    target_sum = len(sequence_array) / 2.0
    current_sum = float(np.sum(sequence_array))
    if current_sum != target_sum:
        if current_sum == 0.0:
            raise AssertionError("Cannot normalize sequence with zero total sum.")
        sequence_array = sequence_array * (target_sum / current_sum)
    if np.any(sequence_array < 0) or np.any(sequence_array > 1):
        raise AssertionError(
            "After normalization, all values in the sequence must be between 0 and 1."
        )
    convolution_values = np.correlate(sequence_array, 1 - sequence_array, mode="full")
    return np.max(convolution_values) / len(values) * 2


# ---------------------------------------------------------------------------
# Input validation
# ---------------------------------------------------------------------------
class TestEvaluateConstraints:
    """Input validation — reject bad inputs fast."""

    def test_nan_rejected(self):
        with pytest.raises(AssertionError, match="NaN"):
            evaluate({"values": [0.5, float("nan"), 0.5]})

    def test_negative_values_rejected(self):
        with pytest.raises(AssertionError, match="between 0 and 1"):
            evaluate({"values": [0.5, -0.1, 0.5]})

    def test_values_above_one_rejected(self):
        with pytest.raises(AssertionError, match="between 0 and 1"):
            evaluate({"values": [0.5, 1.1, 0.5]})

    def test_zero_sum_rejected(self):
        with pytest.raises(AssertionError, match="zero total sum"):
            evaluate({"values": [0.0, 0.0, 0.0]})

    def test_empty_rejected(self):
        """Empty array should fail (no valid correlation)."""
        with pytest.raises(Exception):
            evaluate({"values": []})

    def test_missing_key_rejected(self):
        with pytest.raises(KeyError):
            evaluate({"wrong_key": [0.5, 0.5]})

    def test_post_normalization_violation(self):
        """If all values are near 1.0 but sum > n/2, normalization is fine.
        But if some values are near 1.0 and one is tiny, normalization
        might push values above 1.0."""
        # n=4, sum=3.8, target=2.0. Scale = 2/3.8 = 0.526 -> all shrink, OK
        score = evaluate({"values": [1.0, 1.0, 1.0, 0.8]})
        assert score > 0

    def test_post_normalization_violation_caught(self):
        """Values that are valid pre-normalization but invalid after.
        Need sum < n/2 so normalization scales UP, pushing max > 1."""
        # n=10, all values are 0.4, sum=4.0, target=5.0
        # Scale = 5/4 = 1.25, so 0.4 * 1.25 = 0.5 — still OK
        # Need: value close to 1.0 but sum < n/2
        # n=4: [1.0, 0.0, 0.0, 0.0], sum=1.0, target=2.0, scale=2.0 -> 1.0*2=2.0 > 1
        with pytest.raises(AssertionError, match="After normalization"):
            evaluate({"values": [1.0, 0.0, 0.0, 0.0]})


# ---------------------------------------------------------------------------
# Scoring correctness — known shapes
# ---------------------------------------------------------------------------
class TestEvaluateScoring:
    """Scoring correctness for known function shapes."""

    def test_constant_half(self):
        """Constant h=0.5 on n points. Sum = n/2, so no normalization.
        correlate(0.5, 0.5, 'full') peaks at n*0.25. Score = n*0.25/n*2 = 0.5."""
        n = 1000
        score = evaluate({"values": [0.5] * n})
        assert score == pytest.approx(0.5, rel=1e-10)

    def test_constant_half_small(self):
        """Constant h=0.5, small n."""
        score = evaluate({"values": [0.5] * 10})
        assert score == pytest.approx(0.5, rel=1e-10)

    def test_step_function(self):
        """h = 1 on [0,1], 0 on [1,2]. Sum = n/2, no normalization.
        correlate([1]*50, [1]*50) peaks at 50. Score = 50/100*2 = 1.0."""
        n = 100
        h = [1.0] * (n // 2) + [0.0] * (n // 2)
        score = evaluate({"values": h})
        assert score == pytest.approx(1.0, rel=1e-10)

    def test_random_in_valid_range(self):
        """Score should always be positive for valid inputs.
        Use [0.1, 0.9] range so normalization stays within [0,1]."""
        for seed in range(5):
            rng = np.random.default_rng(seed)
            h = rng.uniform(0.1, 0.9, 500).tolist()
            score = evaluate({"values": h})
            assert score > 0, f"seed={seed}, score={score}"

    def test_near_uniform_scores_near_half(self):
        """Nearly uniform h~0.5 should score close to 0.5."""
        rng = np.random.default_rng(99)
        h = (0.5 + 0.01 * rng.standard_normal(1000)).clip(0, 1).tolist()
        score = evaluate({"values": h})
        assert 0.45 < score < 0.55

    def test_single_value(self):
        """n=1: h=[v], normalized to 0.5. correlate([0.5], [0.5]) = [0.25].
        Score = 0.25 / 1 * 2 = 0.5."""
        score = evaluate({"values": [0.7]})
        assert score == pytest.approx(0.5, rel=1e-10)

    def test_two_values(self):
        """n=2 should work."""
        score = evaluate({"values": [0.8, 0.2]})
        assert score > 0


# ---------------------------------------------------------------------------
# Mathematical properties
# ---------------------------------------------------------------------------
class TestMathProperties:
    """Properties that C must satisfy for any valid function."""

    def test_normalization_idempotent(self):
        """If sum already equals n/2, normalization is a no-op."""
        n = 200
        h = [0.5] * n  # sum = 100 = n/2
        arr = np.array(h, dtype=np.float64)
        normalized = _normalize_sum_constraint(arr)
        np.testing.assert_array_equal(arr, normalized)

    def test_normalization_scales_correctly(self):
        """Normalization scales to target sum = n/2."""
        arr = np.array([0.3, 0.3, 0.3, 0.3], dtype=np.float64)
        # sum=1.2, target=2.0, scale=2.0/1.2=5/3
        normalized = _normalize_sum_constraint(arr)
        assert float(np.sum(normalized)) == pytest.approx(2.0, rel=1e-12)

    def test_deterministic(self):
        """Same input always gives same output."""
        h = [0.5] * 300
        s1 = evaluate({"values": h})
        s2 = evaluate({"values": h})
        assert s1 == s2

    def test_score_bounded(self):
        """C is in (0, 1] for any valid h."""
        h = [0.5] * 200
        score = evaluate({"values": h})
        assert 0 < score <= 1.0

    def test_constant_half_equals_half(self):
        """The trivial h=0.5 gives C=0.5."""
        score = evaluate({"values": [0.5] * 500})
        assert score == pytest.approx(0.5, rel=1e-10)

    def test_symmetry(self):
        """Reversing h should give the same score."""
        h = [0.5] * 200
        # Make an asymmetric perturbation that's still valid
        h[10] = 0.8
        h[190] = 0.2
        # Re-balance so sum stays n/2
        s_forward = evaluate({"values": h})
        s_reverse = evaluate({"values": h[::-1]})
        assert s_forward == pytest.approx(s_reverse, rel=1e-12)


# ---------------------------------------------------------------------------
# Arena cross-validation (the critical test)
# ---------------------------------------------------------------------------
class TestArenaMatch:
    """Exact match against the arena verifier — THE critical correctness gate."""

    @pytest.mark.parametrize("seed", range(10))
    def test_random_functions(self, seed):
        """Random functions of various sizes must match arena exactly.
        Use [0.1, 0.9] range so normalization stays within [0,1]."""
        rng = np.random.default_rng(seed)
        n = int(rng.integers(50, 500))
        h = rng.uniform(0.1, 0.9, n).tolist()
        ours = evaluate({"values": h})
        arena = _arena_verify(h)
        assert ours == pytest.approx(arena, rel=1e-12), (
            f"seed={seed}, n={n}: ours={ours}, arena={arena}"
        )

    def test_constant_half_match(self):
        """Constant h=0.5 matches arena."""
        h = [0.5] * 500
        assert evaluate({"values": h}) == pytest.approx(_arena_verify(h), rel=1e-12)

    def test_step_function_match(self):
        """Step function matches arena."""
        h = [1.0] * 250 + [0.0] * 250
        # This will be normalized: sum=250, target=250. OK.
        assert evaluate({"values": h}) == pytest.approx(_arena_verify(h), rel=1e-12)

    def test_sparse_function_match(self):
        """Sparse function that sums to n/2 matches arena."""
        n = 500
        h = [0.5] * n  # sum = 250 = n/2
        # Perturb some values while keeping within [0,1]
        h[10] = 0.8
        h[100] = 0.2
        h[200] = 0.9
        h[350] = 0.1
        h[490] = 0.7
        assert evaluate({"values": h}) == pytest.approx(_arena_verify(h), rel=1e-12)

    def test_near_boundary_values_match(self):
        """Values near 0 and 1 boundaries match arena."""
        rng = np.random.default_rng(42)
        h = rng.choice([0.001, 0.999, 0.5], size=300).tolist()
        assert evaluate({"values": h}) == pytest.approx(_arena_verify(h), rel=1e-12)

    def test_compute_upper_bound_matches(self):
        """Direct call to compute_upper_bound matches evaluate wrapper."""
        rng = np.random.default_rng(7)
        h = rng.random(300).tolist()
        assert compute_upper_bound(h) == evaluate({"values": h})

    @pytest.mark.parametrize("n", [10, 50, 100, 500, 1000])
    def test_various_sizes_match(self, n):
        """Various array sizes all match arena."""
        rng = np.random.default_rng(n)
        h = rng.uniform(0.1, 0.9, n).tolist()
        ours = evaluate({"values": h})
        arena = _arena_verify(h)
        assert ours == pytest.approx(arena, rel=1e-12), f"n={n}: ours={ours}, arena={arena}"


# ---------------------------------------------------------------------------
# Performance — fast enough for optimization loops
# ---------------------------------------------------------------------------
class TestPerformance:
    """Ensure evaluation is fast enough for iterative optimization."""

    def test_n1000_under_10ms(self):
        """n=1000 should evaluate in < 10ms."""
        h = [0.5] * 1000
        t0 = time.perf_counter()
        for _ in range(10):
            evaluate({"values": h})
        elapsed = (time.perf_counter() - t0) / 10
        assert elapsed < 0.01, f"n=1000 took {elapsed:.4f}s (target < 10ms)"

    def test_n10000_under_500ms(self):
        """n=10,000 should evaluate in < 500ms.
        np.correlate is O(n^2), so 10k is much slower than convolve."""
        h = [0.5] * 10_000
        t0 = time.perf_counter()
        for _ in range(3):
            evaluate({"values": h})
        elapsed = (time.perf_counter() - t0) / 3
        assert elapsed < 0.5, f"n=10000 took {elapsed:.4f}s (target < 500ms)"
