"""Evaluator for the Second Autocorrelation Inequality (Problem 3).

Exact replica of the arena verifier. Given a non-negative function f discretized
as an array of values, computes C = ||f★f||₂² / (||f★f||₁ · ||f★f||∞).

Higher C is better. SOTA is 0.961986 (REDACTED).
"""

import numpy as np


def evaluate(data: dict) -> float:
    """Score a solution for Problem 3. Matches arena verifier exactly."""
    return verify_and_compute_c2(data["values"])


def verify_and_compute_c2(values: list[float]) -> float:
    """Compute C2 score for a discretized non-negative function.

    Args:
        values: Non-negative floats representing the discretized function.

    Returns:
        C = ||f★f||₂² / (||f★f||₁ · ||f★f||∞)
    """
    f = np.array(values, dtype=np.float64)
    n_points = len(values)

    if n_points == 0:
        raise ValueError("values must be non-empty.")
    if f.shape != (n_points,):
        raise ValueError(f"Expected shape ({n_points},), got {f.shape}")
    if np.any(f < -1e-6):
        raise ValueError("Function must be non-negative.")

    f_nonneg = np.maximum(f, 0.0)
    if np.sum(f_nonneg) == 0:
        raise ValueError("Function must have positive integral.")

    # Autoconvolution via numpy
    convolution = np.convolve(f_nonneg, f_nonneg, mode="full")
    num_conv_points = len(convolution)

    # L2 norm squared via Simpson's rule (piecewise quadratic integration)
    x_points = np.linspace(-0.5, 0.5, num_conv_points + 2)
    x_intervals = np.diff(x_points)
    y_points = np.concatenate(([0], convolution, [0]))

    l2_norm_squared = 0.0
    for i in range(num_conv_points + 1):
        y1, y2, h = y_points[i], y_points[i + 1], x_intervals[i]
        l2_norm_squared += (h / 3) * (y1**2 + y1 * y2 + y2**2)

    # L1 norm (discrete sum / normalization)
    norm_1 = np.sum(np.abs(convolution)) / (num_conv_points + 1)

    # L∞ norm
    norm_inf = np.max(np.abs(convolution))

    return float(l2_norm_squared / (norm_1 * norm_inf))
