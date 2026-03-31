"""Evaluator for the Erdos Minimum Overlap problem (Problem 1).

Exact replica of the arena verifier. Given a step function h: [0,2] -> [0,1]
with integral 1, computes C = max_k integral(h(x) * (1 - h(x+k))) dx.

Lower C is better.
"""

import numpy as np


def _normalize_sum_constraint(sequence_array: np.ndarray) -> np.ndarray:
    """Normalize array so sum equals n/2 (integral = 1 over [0,2])."""
    target_sum = len(sequence_array) / 2.0
    current_sum = float(np.sum(sequence_array))
    if current_sum != target_sum:
        if current_sum == 0.0:
            raise AssertionError("Cannot normalize sequence with zero total sum.")
        sequence_array = sequence_array * (target_sum / current_sum)
    return sequence_array


def compute_upper_bound(sequence: list[float]) -> float:
    """Compute the Erdos minimum overlap score for a discretized step function.

    Args:
        sequence: Floats in [0, 1] representing the discretized function h.

    Returns:
        C = max(correlate(h, 1-h, 'full')) * dx, where dx = 2/n.
    """
    sequence_array = np.array(sequence, dtype=np.float64)
    if np.isnan(sequence_array).any():
        raise AssertionError("The sequence contains NaN values.")
    if np.any(sequence_array < 0) or np.any(sequence_array > 1):
        raise AssertionError("All values in the sequence must be between 0 and 1.")
    sequence_array = _normalize_sum_constraint(sequence_array)
    if np.any(sequence_array < 0) or np.any(sequence_array > 1):
        raise AssertionError(
            "After normalization, all values in the sequence must be between 0 and 1."
        )
    convolution_values = np.correlate(sequence_array, 1 - sequence_array, mode="full")
    return np.max(convolution_values) / len(sequence) * 2


def evaluate(data: dict) -> float:
    """Score a solution for Problem 1. Matches arena verifier exactly."""
    return compute_upper_bound(data["values"])
