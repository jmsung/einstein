"""Tests for score_from_conv — the exact closed-form scoring formula.

Validates: C = (2·Σc² + Σc·c') / (3·Σc·max(c)) matches both arena and FFT evaluators.
"""

import numpy as np
import pytest
from scipy.signal import fftconvolve

from einstein.autocorrelation import evaluate as arena_evaluate
from einstein.autocorrelation.fast import fast_evaluate, score_from_conv


class TestScoreFromConv:
    """Exact closed-form formula must match arena and FFT evaluators."""

    @pytest.mark.parametrize("seed", range(10))
    def test_matches_arena(self, seed):
        rng = np.random.default_rng(seed)
        n = int(rng.integers(50, 2000))
        f = rng.random(n)
        conv = fftconvolve(np.maximum(f, 0), np.maximum(f, 0), mode="full")
        exact = score_from_conv(conv)
        arena = arena_evaluate({"values": f.tolist()})
        assert exact == pytest.approx(arena, rel=1e-10)

    @pytest.mark.parametrize("seed", range(10))
    def test_matches_fast_evaluate(self, seed):
        rng = np.random.default_rng(seed + 100)
        f = rng.random(int(rng.integers(100, 1000)))
        conv = fftconvolve(np.maximum(f, 0), np.maximum(f, 0), mode="full")
        exact = score_from_conv(conv)
        fast = fast_evaluate(f)
        assert exact == pytest.approx(fast, rel=1e-10)

    def test_constant_function(self):
        f = np.ones(1000)
        conv = fftconvolve(f, f, mode="full")
        assert score_from_conv(conv) == pytest.approx(2 / 3, rel=1e-6)

    def test_single_spike(self):
        f = np.zeros(100)
        f[50] = 1.0
        conv = fftconvolve(f, f, mode="full")
        assert score_from_conv(conv) == pytest.approx(2 / 3, rel=1e-6)

    def test_empty_returns_zero(self):
        assert score_from_conv(np.array([])) == 0.0

    def test_zero_conv_returns_zero(self):
        assert score_from_conv(np.zeros(100)) == 0.0

    def test_scale_invariance(self):
        rng = np.random.default_rng(42)
        f = rng.random(500)
        conv1 = fftconvolve(f, f, mode="full")
        conv2 = fftconvolve(f * 10, f * 10, mode="full")
        assert score_from_conv(conv1) == pytest.approx(score_from_conv(conv2), rel=1e-10)
