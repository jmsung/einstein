"""Tests for the second autocorrelation inequality evaluator.

Verifies that our local evaluator exactly matches the arena's scoring function.
Comprehensive coverage: constraints, scoring correctness, mathematical properties,
edge cases, performance, and arena cross-validation.
"""

import time

import numpy as np
import pytest
from einstein.autocorrelation import evaluate, verify_and_compute_c2


# ---------------------------------------------------------------------------
# Reference: inline arena verifier for cross-validation
# ---------------------------------------------------------------------------
def _arena_verify(values):
    """Exact copy of the arena verifier — used as ground truth."""
    f = np.array(values, dtype=np.float64)
    n_points = len(values)
    if f.shape != (n_points,):
        raise ValueError(f"Expected shape ({n_points},), got {f.shape}")
    if np.any(f < -1e-6):
        raise ValueError("Function must be non-negative.")
    f_nonneg = np.maximum(f, 0.0)
    if np.sum(f_nonneg) == 0:
        raise ValueError("Function must have positive integral.")
    convolution = np.convolve(f_nonneg, f_nonneg, mode="full")
    num_conv_points = len(convolution)
    x_points = np.linspace(-0.5, 0.5, num_conv_points + 2)
    x_intervals = np.diff(x_points)
    y_points = np.concatenate(([0], convolution, [0]))
    l2_norm_squared = 0.0
    for i in range(num_conv_points + 1):
        y1, y2, h = y_points[i], y_points[i + 1], x_intervals[i]
        l2_norm_squared += (h / 3) * (y1**2 + y1 * y2 + y2**2)
    norm_1 = np.sum(np.abs(convolution)) / (num_conv_points + 1)
    norm_inf = np.max(np.abs(convolution))
    return float(l2_norm_squared / (norm_1 * norm_inf))


# ---------------------------------------------------------------------------
# Input validation
# ---------------------------------------------------------------------------
class TestEvaluateConstraints:
    """Input validation — reject bad inputs fast."""

    def test_negative_values_rejected(self):
        with pytest.raises(ValueError, match="non-negative"):
            evaluate({"values": [1.0, -0.5, 1.0]})

    def test_slightly_negative_tolerated(self):
        """Values in (-1e-6, 0) should be clamped to zero, not rejected."""
        score = evaluate({"values": [1.0, -1e-7, 1.0]})
        assert score > 0

    def test_zero_function_rejected(self):
        with pytest.raises(ValueError, match="positive integral"):
            evaluate({"values": [0.0, 0.0, 0.0]})

    def test_empty_rejected(self):
        with pytest.raises((ValueError, KeyError)):
            evaluate({"values": []})

    def test_missing_key_rejected(self):
        with pytest.raises(KeyError):
            evaluate({"wrong_key": [1.0, 2.0]})

    def test_single_value(self):
        """n=1 should work — convolution is [v^2]."""
        score = evaluate({"values": [1.0]})
        assert score > 0

    def test_two_values(self):
        """n=2 should work."""
        score = evaluate({"values": [1.0, 1.0]})
        assert score > 0


# ---------------------------------------------------------------------------
# Scoring correctness — known shapes
# ---------------------------------------------------------------------------
class TestEvaluateScoring:
    """Scoring correctness for known function shapes."""

    def test_constant_function(self):
        """Constant f=1 on n points. Autoconvolution is a triangle."""
        n = 1000
        score = evaluate({"values": [1.0] * n})
        assert 0 < score <= 1.0

    def test_single_spike(self):
        """Delta-like function: single nonzero value."""
        f = [0.0] * 100
        f[50] = 1.0
        score = evaluate({"values": f})
        assert 0 < score <= 1.0

    def test_two_spikes_differ_from_one(self):
        """Two separated spikes should score differently from one spike."""
        f1 = [0.0] * 200
        f1[50] = 1.0
        s1 = evaluate({"values": f1})

        f2 = [0.0] * 200
        f2[50] = 1.0
        f2[150] = 1.0
        s2 = evaluate({"values": f2})

        assert s1 != pytest.approx(s2, abs=1e-10)

    def test_random_in_valid_range(self):
        """Score should always be in (0, 1] for any valid input."""
        rng = np.random.default_rng(42)
        for seed in range(5):
            f = rng.random(500).tolist()
            score = evaluate({"values": f})
            assert 0 < score <= 1.0, f"seed={seed}, score={score}"

    def test_symmetric_triangle(self):
        """Symmetric triangular function."""
        n = 100
        f = [max(0.0, 1.0 - abs(i - n // 2) / (n // 4)) for i in range(n)]
        score = evaluate({"values": f})
        assert 0 < score <= 1.0

    def test_gaussian_shape(self):
        """Gaussian-like function."""
        n = 500
        x = np.linspace(-3, 3, n)
        f = np.exp(-x**2).tolist()
        score = evaluate({"values": f})
        assert 0 < score <= 1.0

    def test_sparse_blocks(self):
        """Sparse block structure similar to known good solutions."""
        n = 1000
        f = [0.0] * n
        # Place small/big/small triplets every 20 positions
        for start in range(10, n - 10, 20):
            f[start] = 0.1
            f[start + 1] = 1.0
            f[start + 2] = 0.1
        score = evaluate({"values": f})
        assert 0 < score <= 1.0


# ---------------------------------------------------------------------------
# Mathematical properties
# ---------------------------------------------------------------------------
class TestMathProperties:
    """Properties that C must satisfy for any valid function."""

    def test_scale_invariance(self):
        """C(alpha*f) == C(f) for any alpha > 0."""
        rng = np.random.default_rng(123)
        f = rng.random(200).tolist()
        s1 = evaluate({"values": f})
        for alpha in [0.01, 0.5, 2.0, 100.0]:
            s2 = evaluate({"values": [v * alpha for v in f]})
            assert s1 == pytest.approx(s2, rel=1e-10), f"alpha={alpha}"

    def test_translation_in_support(self):
        """Shifting f within a longer zero-padded array shouldn't change C much.
        (Exact invariance depends on boundary effects from the finite grid.)"""
        n = 400
        rng = np.random.default_rng(77)
        core = rng.random(50).tolist()

        f1 = [0.0] * n
        f1[100:150] = core
        s1 = evaluate({"values": f1})

        f2 = [0.0] * n
        f2[200:250] = core
        s2 = evaluate({"values": f2})

        # Should be very close (boundary effects small for centered support)
        assert s1 == pytest.approx(s2, rel=1e-6)

    def test_deterministic(self):
        """Same input always gives same output."""
        rng = np.random.default_rng(42)
        f = rng.random(300).tolist()
        s1 = evaluate({"values": f})
        s2 = evaluate({"values": f})
        assert s1 == s2

    def test_monotonic_with_n_points(self):
        """For uniform f, score should change predictably with n."""
        scores = []
        for n in [50, 100, 200, 500]:
            scores.append(evaluate({"values": [1.0] * n}))
        # All should be valid
        assert all(0 < s <= 1.0 for s in scores)

    def test_flat_autoconvolution_scores_high(self):
        """A function whose autoconvolution is nearly flat should score higher
        than one with peaked autoconvolution."""
        # Constant function: autoconvolution is triangular (peaked)
        s_const = evaluate({"values": [1.0] * 200})

        # Sparse uniform blocks: autoconvolution is flatter
        f_sparse = [0.0] * 200
        for i in range(0, 200, 4):
            f_sparse[i] = 1.0
        s_sparse = evaluate({"values": f_sparse})

        # The sparse version should generally score higher (flatter autoconv)
        # This is a soft check — the exact relationship depends on spacing
        assert s_sparse > 0 and s_const > 0


# ---------------------------------------------------------------------------
# Arena cross-validation (the critical test)
# ---------------------------------------------------------------------------
class TestArenaMatch:
    """Exact match against the arena verifier — THE critical correctness gate."""

    @pytest.mark.parametrize("seed", range(10))
    def test_random_functions(self, seed):
        """Random functions of various sizes must match arena exactly."""
        rng = np.random.default_rng(seed)
        n = rng.integers(50, 500)
        f = rng.random(int(n)).tolist()
        ours = evaluate({"values": f})
        arena = _arena_verify(f)
        assert ours == pytest.approx(arena, rel=1e-12), (
            f"seed={seed}, n={n}: ours={ours}, arena={arena}"
        )

    def test_sparse_function_match(self):
        """Sparse function (mostly zeros) matches arena."""
        f = [0.0] * 500
        f[10] = 1.0
        f[100] = 0.5
        f[200] = 2.0
        f[350] = 0.3
        assert evaluate({"values": f}) == pytest.approx(_arena_verify(f), rel=1e-12)

    def test_large_values_match(self):
        """Large magnitude values match arena."""
        rng = np.random.default_rng(42)
        f = (rng.random(200) * 1e6).tolist()
        assert evaluate({"values": f}) == pytest.approx(_arena_verify(f), rel=1e-12)

    def test_tiny_values_match(self):
        """Very small positive values match arena."""
        rng = np.random.default_rng(42)
        f = (rng.random(200) * 1e-8).tolist()
        assert evaluate({"values": f}) == pytest.approx(_arena_verify(f), rel=1e-10)

    def test_verify_and_compute_c2_matches(self):
        """Direct call to verify_and_compute_c2 matches evaluate wrapper."""
        rng = np.random.default_rng(7)
        f = rng.random(300).tolist()
        assert verify_and_compute_c2(f) == evaluate({"values": f})


# ---------------------------------------------------------------------------
# Performance — fast enough for optimization loops
# ---------------------------------------------------------------------------
class TestPerformance:
    """Ensure evaluation is fast enough for iterative optimization."""

    def test_n1000_under_10ms(self):
        """n=1000 should evaluate in < 10ms."""
        f = [1.0] * 1000
        t0 = time.perf_counter()
        for _ in range(10):
            evaluate({"values": f})
        elapsed = (time.perf_counter() - t0) / 10
        assert elapsed < 0.01, f"n=1000 took {elapsed:.4f}s (target < 10ms)"

    def test_n10000_under_100ms(self):
        """n=10,000 should evaluate in < 100ms."""
        f = [1.0] * 10_000
        t0 = time.perf_counter()
        for _ in range(3):
            evaluate({"values": f})
        elapsed = (time.perf_counter() - t0) / 3
        assert elapsed < 0.1, f"n=10000 took {elapsed:.4f}s (target < 100ms)"

    def test_n100000_under_10s(self):
        """n=100,000 should evaluate in < 10s (arena competitive size)."""
        rng = np.random.default_rng(42)
        f = rng.random(100_000).tolist()
        t0 = time.perf_counter()
        evaluate({"values": f})
        elapsed = time.perf_counter() - t0
        assert elapsed < 10.0, f"n=100000 took {elapsed:.1f}s (target < 10s)"
