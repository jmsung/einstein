"""Tests for First Autocorrelation Inequality (Problem 2) evaluator."""

from __future__ import annotations

import numpy as np
import pytest

from einstein.first_autocorrelation.evaluator import evaluate, verify_and_compute


def test_constant_function() -> None:
    """f ≡ 1 on n=100 → C = 2 exactly (uniform extremal)."""
    f = [1.0] * 100
    C = verify_and_compute(f)
    assert abs(C - 2.0) < 1e-12


def test_negative_raises() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        verify_and_compute([1.0, -0.1, 1.0])


def test_zero_integral_raises() -> None:
    with pytest.raises(ValueError, match="positive"):
        verify_and_compute([0.0] * 10)


def test_evaluate_dict_form() -> None:
    """The arena calls evaluate(data) with data['values']."""
    f = [1.0, 2.0, 3.0, 2.0, 1.0]
    C_dict = evaluate({"values": f})
    C_direct = verify_and_compute(f)
    assert C_dict == C_direct


def test_scale_invariance() -> None:
    """C(α·f) = C(f) for any α > 0."""
    rng = np.random.default_rng(0)
    f = rng.uniform(0.1, 1.0, 50).tolist()
    base = verify_and_compute(f)
    scaled = verify_and_compute([10.0 * x for x in f])
    assert abs(base - scaled) < 1e-12


def test_arena_verifier_match() -> None:
    """Match the verifier formula bit-for-bit (np.convolve full)."""
    rng = np.random.default_rng(7)
    f = rng.uniform(0, 1, 200)
    n = len(f)
    dx = 0.5 / n
    autoconv = np.convolve(f, f, mode="full") * dx
    integral_sq = (np.sum(f) * dx) ** 2
    expected = float(np.max(autoconv) / integral_sq)
    actual = verify_and_compute(f.tolist())
    assert actual == expected
