"""Fast evaluator for the Second Autocorrelation Inequality (Problem 3).

Uses FFT-based convolution (O(n log n)) instead of np.convolve (O(n²)).
Matches arena verifier to ~1e-15. Designed for optimization loops.

Exact scoring formula (from arena discussion, equivalent to Simpson rule):
    C = (2·Σc_i² + Σc_i·c_{i+1}) / (3 · Σc_i · max(c_i))
where c = np.convolve(f, f, mode='full').

Typical speed:
    n=100k  → 3ms/eval
    n=500k  → 20ms/eval
    n=1M    → 50ms/eval
"""

import numpy as np
from scipy.signal import fftconvolve


def fast_evaluate(values: np.ndarray | list[float]) -> float:
    """Score a function for Problem 3 using FFT convolution.

    Matches the arena verifier to ~1e-15 relative error.
    ~100x faster than arena verifier at n=100k.

    Args:
        values: Non-negative floats (array or list).

    Returns:
        C = ||f★f||₂² / (||f★f||₁ · ||f★f||∞), or 0.0 on invalid input.
    """
    f = np.asarray(values, dtype=np.float64)
    f = np.maximum(f, 0.0)

    if f.size == 0 or np.sum(f) == 0:
        return 0.0

    # Autoconvolution via FFT — O(n log n)
    conv = fftconvolve(f, f, mode="full")
    nc = len(conv)

    # Vectorized Simpson's rule for L2² (matches arena's piecewise quadratic)
    dx = np.diff(np.linspace(-0.5, 0.5, nc + 2))
    y = np.empty(nc + 2)
    y[0] = 0.0
    y[1:-1] = conv
    y[-1] = 0.0
    y1 = y[:-1]
    y2 = y[1:]
    l2_sq = np.sum((dx / 3.0) * (y1 * y1 + y1 * y2 + y2 * y2))

    # L1 and L∞ norms (match arena normalization)
    l1 = np.sum(np.abs(conv)) / (nc + 1)
    l_inf = np.max(np.abs(conv))

    if l1 == 0.0 or l_inf == 0.0:
        return 0.0

    return float(l2_sq / (l1 * l_inf))


def score_from_conv(conv: np.ndarray) -> float:
    """Compute C directly from an autoconvolution array.

    Uses the exact closed-form formula equivalent to the arena Simpson rule:
        C = (2·Σc² + Σc·c_shift) / (3 · Σc · max(c))

    This avoids recomputing the convolution when only values change locally.
    """
    if conv.size == 0:
        return 0.0
    c_sum = np.sum(conv)
    c_max = np.max(conv)
    if c_sum == 0.0 or c_max == 0.0:
        return 0.0
    numerator = 2.0 * np.sum(conv * conv) + np.sum(conv[:-1] * conv[1:])
    return float(numerator / (3.0 * c_sum * c_max))


def diagnose(values: np.ndarray | list[float]) -> dict:
    """Analyze a solution's autoconvolution structure.

    Returns diagnostic metrics useful for understanding and improving solutions.
    """
    f = np.asarray(values, dtype=np.float64)
    f = np.maximum(f, 0.0)
    conv = fftconvolve(f, f, mode="full")

    c_max = np.max(conv)
    if c_max == 0:
        return {"score": 0.0, "error": "zero autoconvolution"}

    # Flatness: fraction of autoconvolution within X% of max
    near_max_01 = np.sum(conv > 0.999 * c_max)  # within 0.1%
    near_max_1 = np.sum(conv > 0.99 * c_max)  # within 1%
    near_max_10 = np.sum(conv > 0.90 * c_max)  # within 10%

    # Support analysis
    nnz = int(np.count_nonzero(f))
    support_frac = nnz / len(f) if len(f) > 0 else 0

    # Find contiguous blocks in f
    nonzero_mask = f > 0
    block_starts = np.where(np.diff(np.concatenate(([0], nonzero_mask.astype(int)))) == 1)[0]
    block_ends = np.where(np.diff(np.concatenate((nonzero_mask.astype(int), [0]))) == -1)[0]
    n_blocks = len(block_starts)
    block_widths = block_ends - block_starts + 1 if n_blocks > 0 else np.array([])

    return {
        "score": fast_evaluate(f),
        "n_points": len(f),
        "nnz": nnz,
        "support_fraction": support_frac,
        "n_blocks": n_blocks,
        "mean_block_width": float(np.mean(block_widths)) if n_blocks > 0 else 0,
        "conv_length": len(conv),
        "conv_max": float(c_max),
        "conv_mean": float(np.mean(conv)),
        "conv_std_over_mean": float(np.std(conv) / np.mean(conv)) if np.mean(conv) > 0 else float("inf"),
        "flatness_0.1pct": int(near_max_01),
        "flatness_1pct": int(near_max_1),
        "flatness_10pct": int(near_max_10),
    }
