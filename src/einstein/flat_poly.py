"""Evaluator for the Flat Polynomials problem (Problem 12).

Exact replica of the arena verifier. Given 70 coefficients in {+1, -1}
(descending degree order per np.poly1d convention), evaluates
max|p(z)| / sqrt(71) on 1M unit circle points.

Lower score is better.
"""

import numpy as np

N_POINTS = 1_000_000
NORM = np.sqrt(71)


def compute_score(coefficients: list[int]) -> float:
    """Compute flat polynomial score.

    Args:
        coefficients: 70 values in {-1, +1}, descending degree order
            (coefficients[0] * z^69 + ... + coefficients[69]).

    Returns:
        max|p(z)| / sqrt(71) over 1M unit circle points.
    """
    coeffs = np.asarray(coefficients, dtype=np.float64)
    if len(coeffs) != 70:
        raise AssertionError(f"Expected 70 coefficients, got {len(coeffs)}.")
    if np.isnan(coeffs).any():
        raise AssertionError("Coefficients contain NaN values.")
    if not np.all((coeffs == 1) | (coeffs == -1)):
        raise AssertionError("All coefficients must be +1 or -1.")

    p = np.poly1d(coeffs)
    z = np.exp(2j * np.pi * np.arange(N_POINTS) / N_POINTS)
    return float(np.max(np.abs(p(z))) / NORM)


def evaluate(data: dict) -> float:
    """Score a solution for Problem 12. Matches arena verifier exactly."""
    return compute_score(data["coefficients"])
