"""Exact replica of the arena verifier for Problem ID 4 (Third Autocorrelation).

Arena verifier (per problem page, variant b):

    def verify_and_compute(values: list[float]) -> float:
        f = np.array(values, dtype=np.float64)
        if np.sum(f) == 0:
            raise ValueError("The integral of f must be non-trivially positive.")
        n_points = len(values)
        dx = 0.5 / n_points
        autoconv = np.convolve(f, f, mode="full") * dx
        integral_sq = (np.sum(f) * dx) ** 2
        return float(abs(np.max(autoconv)) / integral_sq)

Unlike Problem 2 (first autocorrelation), f MAY be negative here. Only the
POSITIVE peak of f★f counts; negative excursions are free.

C is scale-invariant in f.
"""

from __future__ import annotations

import numpy as np


def evaluate(data: dict) -> float:
    """Score a solution. Matches arena verifier exactly (tol=0)."""
    return verify_and_compute(data["values"])


def verify_and_compute(values: list[float]) -> float:
    f = np.array(values, dtype=np.float64)
    if np.sum(f) == 0:
        raise ValueError("The integral of f must be non-trivially positive.")
    n_points = len(values)
    dx = 0.5 / n_points
    autoconv = np.convolve(f, f, mode="full") * dx
    integral_sq = (np.sum(f) * dx) ** 2
    # |max_t (f★f)(t)| — absolute value of the MAX, NOT max of |·|.
    # Negative excursions of f★f are not penalized in this variant.
    return float(abs(np.max(autoconv)) / integral_sq)
