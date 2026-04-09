"""Tests for Third Autocorrelation Inequality (Problem 4) evaluator."""

from __future__ import annotations

import numpy as np
import pytest

from einstein.third_autocorrelation.evaluator import evaluate, verify_and_compute


def test_constant_function() -> None:
    """f ≡ 1 on n=100 → C = 2 exactly (positive peak at the endpoints)."""
    f = [1.0] * 100
    c = verify_and_compute(f)
    assert abs(c - 2.0) < 1e-12


def test_negative_values_allowed() -> None:
    """Unlike first autocorrelation, f may go negative here.

    Hand-computed oracle for [1, -0.5, 1, -0.5, 1] at n=5, dx=0.1:
    autoconv max occurs at the symmetric center (k=4) with value 0.35;
    integral = 0.2; C = abs(0.35) / 0.2**2 = 8.75.
    """
    c = verify_and_compute([1.0, -0.5, 1.0, -0.5, 1.0])
    assert c == 8.75


def test_zero_integral_raises() -> None:
    with pytest.raises(ValueError, match="positive"):
        verify_and_compute([0.0] * 10)


def test_evaluate_dict_form() -> None:
    f = [1.0, 2.0, 3.0, 2.0, 1.0]
    c_dict = evaluate({"values": f})
    c_direct = verify_and_compute(f)
    assert c_dict == c_direct


def test_scale_invariance() -> None:
    """C(α·f) = C(f) for any α ≠ 0 (including negative α)."""
    rng = np.random.default_rng(0)
    f = rng.normal(0.5, 0.5, 50).tolist()
    base = verify_and_compute(f)
    scaled_pos = verify_and_compute([10.0 * x for x in f])
    scaled_neg = verify_and_compute([-10.0 * x for x in f])
    assert abs(base - scaled_pos) < 1e-12
    assert abs(base - scaled_neg) < 1e-12


def test_arena_verifier_match() -> None:
    """Match the verifier formula bit-for-bit (np.convolve full)."""
    rng = np.random.default_rng(7)
    f = rng.normal(0.5, 0.5, 200)
    # Ensure ∫f ≠ 0
    f[0] += 5.0
    n = len(f)
    dx = 0.5 / n
    autoconv = np.convolve(f, f, mode="full") * dx
    integral_sq = (np.sum(f) * dx) ** 2
    expected = float(abs(np.max(autoconv)) / integral_sq)
    actual = verify_and_compute(f.tolist())
    assert actual == expected
