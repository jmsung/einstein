"""Fast evaluator for the Erdos Minimum Overlap problem (Problem 1).

Uses FFT-based correlation (O(n log n)) instead of np.correlate (O(n^2)).
Matches arena verifier to ~1e-12. Designed for optimization loops.

Arena formula:
    C = max(correlate(h, 1-h, 'full')) * 2/n
where h is normalized so sum(h) = n/2.
"""

import numpy as np
from scipy.signal import fftconvolve


def fast_evaluate(values: np.ndarray | list[float]) -> float:
    """Score a function for Problem 1 using FFT correlation.

    Matches the arena verifier to ~1e-12 relative error.
    Much faster than np.correlate at large n.

    Args:
        values: Floats in [0, 1] representing discretized h.

    Returns:
        C = max(correlate(h, 1-h, 'full')) * 2/n, or inf on invalid input.
    """
    h = np.asarray(values, dtype=np.float64)
    n = len(h)

    if n == 0:
        return float("inf")

    # Validate [0, 1] range
    if np.any(h < 0) or np.any(h > 1):
        return float("inf")

    # Normalize sum to n/2
    s = float(np.sum(h))
    if s == 0.0:
        return float("inf")
    target = n / 2.0
    if s != target:
        h = h * (target / s)
    if np.any(h > 1.0):
        return float("inf")

    # Cross-correlation via FFT: correlate(h, 1-h) = correlate(h, 1) - correlate(h, h)
    # correlate(h, 1-h, 'full') at lag k = sum_m h[m] * (1 - h[m-k])
    # = sum(h) - sum_m h[m]*h[m-k]
    # = target - autocorr[k]
    # But simpler: just compute fftconvolve(h, (1-h)[::-1]) which is the correlation.
    one_minus_h = 1.0 - h
    corr = fftconvolve(h, one_minus_h[::-1], mode="full")

    return float(np.max(corr)) / n * 2
