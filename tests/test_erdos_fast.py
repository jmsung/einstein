"""Tests for the fast Erdos evaluator.

Verifies FFT-based fast evaluator matches the arena-exact evaluator.
"""

import time

import numpy as np
import pytest
from einstein.erdos import evaluate as exact_evaluate
from einstein.erdos_fast import fast_evaluate


class TestFastMatchesArena:
    """Fast evaluator must match exact evaluator to high precision."""

    @pytest.mark.parametrize("seed", range(10))
    def test_random_functions(self, seed):
        """Random h in [0.1, 0.9] must match exact evaluator."""
        rng = np.random.default_rng(seed)
        n = int(rng.integers(50, 500))
        h = rng.uniform(0.1, 0.9, n)
        fast = fast_evaluate(h)
        exact = exact_evaluate({"values": h.tolist()})
        assert fast == pytest.approx(exact, rel=1e-10), (
            f"seed={seed}, n={n}: fast={fast}, exact={exact}"
        )

    def test_constant_half(self):
        """Constant h=0.5 → C=0.5."""
        h = np.full(500, 0.5)
        assert fast_evaluate(h) == pytest.approx(0.5, rel=1e-10)

    def test_step_function(self):
        """Step function h=[1]*250 + [0]*250 → C=1.0."""
        h = np.array([1.0] * 250 + [0.0] * 250)
        assert fast_evaluate(h) == pytest.approx(1.0, rel=1e-10)

    @pytest.mark.parametrize("n", [10, 100, 500, 1000])
    def test_various_sizes(self, n):
        rng = np.random.default_rng(n)
        h = rng.uniform(0.1, 0.9, n)
        fast = fast_evaluate(h)
        exact = exact_evaluate({"values": h.tolist()})
        assert fast == pytest.approx(exact, rel=1e-10)

    def test_accepts_list(self):
        """Should accept plain list input."""
        h = [0.5] * 100
        assert fast_evaluate(h) == pytest.approx(0.5, rel=1e-10)


class TestFastEdgeCases:
    """Edge cases for fast evaluator."""

    def test_empty_returns_inf(self):
        assert fast_evaluate(np.array([])) == float("inf")

    def test_all_zeros_returns_inf(self):
        assert fast_evaluate(np.zeros(100)) == float("inf")

    def test_negative_values_returns_inf(self):
        assert fast_evaluate(np.array([0.5, -0.1, 0.5])) == float("inf")

    def test_above_one_returns_inf(self):
        assert fast_evaluate(np.array([0.5, 1.5, 0.5])) == float("inf")

    def test_post_normalization_violation_returns_inf(self):
        """h=[1,0,0,0]: sum=1, target=2, scale=2 → h[0]=2 > 1."""
        assert fast_evaluate(np.array([1.0, 0.0, 0.0, 0.0])) == float("inf")


class TestFastPerformance:
    """Fast evaluator should be much faster than O(n^2) exact."""

    def test_n10k_under_10ms(self):
        rng = np.random.default_rng(42)
        h = rng.uniform(0.1, 0.9, 10_000)
        t0 = time.perf_counter()
        for _ in range(10):
            fast_evaluate(h)
        elapsed = (time.perf_counter() - t0) / 10
        assert elapsed < 0.01, f"n=10k took {elapsed:.4f}s (target < 10ms)"

    def test_n100k_under_100ms(self):
        rng = np.random.default_rng(42)
        h = rng.uniform(0.1, 0.9, 100_000)
        t0 = time.perf_counter()
        for _ in range(3):
            fast_evaluate(h)
        elapsed = (time.perf_counter() - t0) / 3
        assert elapsed < 0.1, f"n=100k took {elapsed:.4f}s (target < 100ms)"
