"""Core utilities for Erdős Minimum Overlap optimization."""

import numpy as np
from scipy.signal import fftconvolve


def score(h: np.ndarray) -> float:
    """Compute Erdős overlap score. Lower is better."""
    n = len(h)
    s = np.sum(h)
    target = n / 2.0
    if s != target and s != 0:
        h = h * (target / s)
    one_minus_h = 1.0 - h
    corr = fftconvolve(h, one_minus_h[::-1], mode="full")
    return float(np.max(corr)) / n * 2


def correlation_vector(h: np.ndarray) -> np.ndarray:
    """Full cross-correlation vector C(k) = sum_m h[m]*(1-h[m-k])."""
    n = len(h)
    s = np.sum(h)
    target = n / 2.0
    if s != target and s != 0:
        h = h * (target / s)
    return fftconvolve(h, (1.0 - h)[::-1], mode="full")


def project(h: np.ndarray) -> np.ndarray:
    """Project h onto feasible set: h in [0,1], sum=n/2."""
    n = len(h)
    h = np.clip(h, 0.0, 1.0)
    # Adjust sum to n/2 by shifting
    target = n / 2.0
    excess = np.sum(h) - target
    if abs(excess) > 1e-12:
        # Distribute excess proportionally among non-boundary elements
        if excess > 0:
            # Need to reduce: reduce non-zero elements
            mask = h > 1e-15
            if mask.any():
                h[mask] -= excess * (h[mask] / np.sum(h[mask]))
                h = np.clip(h, 0.0, 1.0)
        else:
            # Need to increase: increase non-one elements
            mask = h < 1.0 - 1e-15
            if mask.any():
                room = 1.0 - h[mask]
                h[mask] += (-excess) * (room / np.sum(room))
                h = np.clip(h, 0.0, 1.0)
        # Final exact normalization
        s = np.sum(h)
        if s > 0 and abs(s - target) > 1e-15:
            h = h * (target / s)
            h = np.clip(h, 0.0, 1.0)
    return h


def smooth_max_score(h: np.ndarray, beta: float = 100.0) -> float:
    """Smoothed max using log-sum-exp. Differentiable approximation."""
    corr = correlation_vector(h)
    n = len(h)
    # log-sum-exp of corr * beta
    c_max = np.max(corr)
    return (c_max + np.log(np.sum(np.exp(beta * (corr - c_max)))) / beta) / n * 2


def random_init(n: int, seed: int = None) -> np.ndarray:
    """Random feasible initialization."""
    rng = np.random.default_rng(seed)
    h = rng.random(n)
    h = h / np.sum(h) * (n / 2)
    h = np.clip(h, 0.0, 1.0)
    # Re-normalize
    s = np.sum(h)
    if s > 0:
        h = h * (n / 2 / s)
    return h


def smart_init(n: int, seed: int = None) -> np.ndarray:
    """Smarter initialization: mostly 0/1 with some transition region."""
    rng = np.random.default_rng(seed)
    h = np.zeros(n)
    # Set roughly n/2 elements to 1
    # Use a random permutation
    perm = rng.permutation(n)
    h[perm[:n//2]] = 1.0
    # Add some randomness to smooth it out
    h += rng.normal(0, 0.05, n)
    h = np.clip(h, 0.0, 1.0)
    return project(h)


def haugland_init(n: int) -> np.ndarray:
    """Initialize with a Haugland-style symmetric step function."""
    h = np.zeros(n)
    # Roughly: h = 1 on [0, 0.4] and [1.6, 2], h = 0.5 in between
    # Scaled to n points covering [0, 2]
    for i in range(n):
        x = 2.0 * i / n
        if x < 0.4 or x > 1.6:
            h[i] = 1.0
        elif 0.4 <= x < 0.6 or 1.4 <= x <= 1.6:
            h[i] = 0.5
        else:
            h[i] = 0.0
    return project(h)


def upsample(h: np.ndarray, new_n: int) -> np.ndarray:
    """Upsample step function to higher resolution via linear interpolation."""
    n = len(h)
    x_old = np.linspace(0, 1, n)
    x_new = np.linspace(0, 1, new_n)
    h_new = np.interp(x_new, x_old, h)
    return project(h_new)
