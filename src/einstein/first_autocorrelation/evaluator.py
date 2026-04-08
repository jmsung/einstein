"""Exact replica of the arena verifier for Problem ID 2.

The arena server runs the following code (verbatim from /api/problems/first-autocorrelation-inequality):

    def verify_and_compute(values: list[float]) -> float:
        f = np.array(values, dtype=np.float64)
        if np.any(f < 0):
            raise ValueError("All values must be non-negative.")
        if np.sum(f) == 0:
            raise ValueError("The integral of f must be non-trivially positive.")
        n_points = len(values)
        dx = 0.5 / n_points
        autoconv = np.convolve(f, f, mode="full") * dx
        integral_sq = (np.sum(f) * dx) ** 2
        return float(np.max(autoconv) / integral_sq)

We replicate this byte-for-byte. C is scale-invariant in f.
"""

from __future__ import annotations

import numpy as np


def evaluate(data: dict) -> float:
    """Score a solution. Matches arena verifier exactly (tol=0)."""
    return verify_and_compute(data["values"])


def verify_and_compute(values: list[float]) -> float:
    f = np.array(values, dtype=np.float64)
    if np.any(f < 0):
        raise ValueError("All values must be non-negative.")
    if np.sum(f) == 0:
        raise ValueError("The integral of f must be non-trivially positive.")
    n_points = len(values)
    dx = 0.5 / n_points
    autoconv = np.convolve(f, f, mode="full") * dx
    integral_sq = (np.sum(f) * dx) ** 2
    return float(np.max(autoconv) / integral_sq)
