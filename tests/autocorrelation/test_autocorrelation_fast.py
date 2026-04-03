"""Tests for the FFT-based fast evaluator.

Validates correctness vs arena verifier and performance at large n.
"""

import time

import numpy as np
import pytest
from einstein.autocorrelation import evaluate as arena_evaluate
from einstein.autocorrelation.fast import diagnose, fast_evaluate


# ---------------------------------------------------------------------------
# Correctness: must match arena verifier
# ---------------------------------------------------------------------------
class TestFastMatchesArena:
    """FFT fast evaluator must agree with arena verifier to high precision."""

    @pytest.mark.parametrize("seed", range(10))
    def test_random_functions(self, seed):
        rng = np.random.default_rng(seed)
        n = int(rng.integers(50, 2000))
        f = rng.random(n).tolist()
        fast = fast_evaluate(f)
        arena = arena_evaluate({"values": f})
        assert fast == pytest.approx(arena, rel=1e-10), (
            f"seed={seed}, n={n}: fast={fast}, arena={arena}"
        )

    @pytest.mark.parametrize("n", [1, 2, 10, 100, 1000, 5000])
    def test_constant_function(self, n):
        f = [1.0] * n
        fast = fast_evaluate(f)
        arena = arena_evaluate({"values": f})
        assert fast == pytest.approx(arena, rel=1e-10)

    def test_sparse_function(self):
        f = np.zeros(1000)
        f[10] = 1.0
        f[100] = 0.5
        f[500] = 2.0
        f[900] = 0.3
        fast = fast_evaluate(f)
        arena = arena_evaluate({"values": f.tolist()})
        assert fast == pytest.approx(arena, rel=1e-10)

    def test_large_values(self):
        rng = np.random.default_rng(42)
        f = (rng.random(500) * 1e6).tolist()
        fast = fast_evaluate(f)
        arena = arena_evaluate({"values": f})
        assert fast == pytest.approx(arena, rel=1e-10)

    def test_tiny_values(self):
        rng = np.random.default_rng(42)
        f = (rng.random(500) * 1e-8).tolist()
        fast = fast_evaluate(f)
        arena = arena_evaluate({"values": f})
        assert fast == pytest.approx(arena, rel=1e-8)

    def test_accepts_numpy_array(self):
        f = np.array([1.0, 2.0, 3.0, 2.0, 1.0])
        fast = fast_evaluate(f)
        arena = arena_evaluate({"values": f.tolist()})
        assert fast == pytest.approx(arena, rel=1e-10)

    def test_scale_invariance(self):
        rng = np.random.default_rng(123)
        f = rng.random(300)
        s1 = fast_evaluate(f)
        s2 = fast_evaluate(f * 100.0)
        assert s1 == pytest.approx(s2, rel=1e-10)


# ---------------------------------------------------------------------------
# Edge cases
# ---------------------------------------------------------------------------
class TestFastEdgeCases:
    """Graceful handling of degenerate inputs."""

    def test_empty_returns_zero(self):
        assert fast_evaluate([]) == 0.0

    def test_all_zeros_returns_zero(self):
        assert fast_evaluate([0.0, 0.0, 0.0]) == 0.0

    def test_negative_values_clamped(self):
        score = fast_evaluate([1.0, -0.5, 1.0])
        assert score > 0  # -0.5 clamped to 0, still valid

    def test_single_value(self):
        assert fast_evaluate([1.0]) > 0


# ---------------------------------------------------------------------------
# Performance
# ---------------------------------------------------------------------------
class TestFastPerformance:
    """FFT evaluator must be fast enough for optimization loops."""

    def test_n100k_under_10ms(self):
        rng = np.random.default_rng(42)
        f = rng.random(100_000)
        # Warm up
        fast_evaluate(f)
        t0 = time.perf_counter()
        for _ in range(10):
            fast_evaluate(f)
        elapsed = (time.perf_counter() - t0) / 10
        assert elapsed < 0.01, f"n=100k took {elapsed*1000:.1f}ms (target < 10ms)"

    def test_n500k_under_50ms(self):
        rng = np.random.default_rng(42)
        f = rng.random(500_000)
        fast_evaluate(f)  # warm up
        t0 = time.perf_counter()
        for _ in range(3):
            fast_evaluate(f)
        elapsed = (time.perf_counter() - t0) / 3
        assert elapsed < 0.05, f"n=500k took {elapsed*1000:.1f}ms (target < 50ms)"

    def test_n1M_under_100ms(self):
        rng = np.random.default_rng(42)
        f = rng.random(1_000_000)
        fast_evaluate(f)  # warm up
        t0 = time.perf_counter()
        fast_evaluate(f)
        elapsed = time.perf_counter() - t0
        assert elapsed < 0.1, f"n=1M took {elapsed*1000:.1f}ms (target < 100ms)"

    def test_100x_faster_than_arena_at_100k(self):
        """FFT evaluator must be at least 10x faster than arena at n=100k."""
        rng = np.random.default_rng(42)
        f = rng.random(100_000)
        fl = f.tolist()

        fast_evaluate(f)  # warm up
        t0 = time.perf_counter()
        for _ in range(5):
            fast_evaluate(f)
        t_fast = (time.perf_counter() - t0) / 5

        arena_evaluate({"values": fl})  # warm up
        t0 = time.perf_counter()
        arena_evaluate({"values": fl})
        t_arena = time.perf_counter() - t0

        speedup = t_arena / t_fast
        assert speedup > 10, f"Speedup only {speedup:.1f}x (expected > 10x)"


# ---------------------------------------------------------------------------
# Diagnostics
# ---------------------------------------------------------------------------
class TestDiagnose:
    """The diagnose function provides useful structural analysis."""

    def test_returns_score(self):
        rng = np.random.default_rng(42)
        f = rng.random(500)
        d = diagnose(f)
        assert d["score"] == pytest.approx(fast_evaluate(f), rel=1e-12)

    def test_block_detection(self):
        f = np.zeros(100)
        f[10:15] = 1.0  # block 1: width 5
        f[50:53] = 1.0  # block 2: width 3
        f[80] = 1.0  # block 3: width 1
        d = diagnose(f)
        assert d["n_blocks"] == 3
        assert d["nnz"] == 9
        assert d["mean_block_width"] == pytest.approx(3.0)

    def test_flatness_metrics(self):
        d = diagnose(np.ones(1000))
        assert d["flatness_0.1pct"] >= 1
        assert d["flatness_1pct"] >= d["flatness_0.1pct"]
        assert d["flatness_10pct"] >= d["flatness_1pct"]

    def test_sparse_vs_dense(self):
        dense = diagnose(np.ones(1000))
        sparse = np.zeros(1000)
        sparse[::10] = 1.0
        sparse_d = diagnose(sparse)
        assert sparse_d["support_fraction"] < dense["support_fraction"]
        assert sparse_d["n_blocks"] > dense["n_blocks"]

    def test_zero_input(self):
        d = diagnose(np.zeros(100))
        assert d["score"] == 0.0
