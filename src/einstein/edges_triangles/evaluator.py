"""Evaluator for Edges vs Triangles (Problem 13).

Given a weight matrix (m×20), computes edge/triangle density points via
complete-multipartite graphon power-sum formulas, then scores the piecewise
slope-3 interpolated curve.

Score = -(area + 10·max_gap), higher (less negative) is better.
"""

import numpy as np


def compute_densities(p: np.ndarray) -> tuple[float, float]:
    """Compute edge and triangle density from a probability vector.

    Each row represents part sizes of a complete multipartite graph.

    Args:
        p: probability vector (non-negative, sums to 1), length n.

    Returns:
        (edge_density, triangle_density).
    """
    s2 = float(np.sum(p**2))
    s3 = float(np.sum(p**3))
    return 1.0 - s2, 1.0 - 3.0 * s2 + 2.0 * s3


def compute_score(weights: np.ndarray) -> float:
    """Compute score from a weight matrix.

    Args:
        weights: (m, 20) array of non-negative values. Rows are normalized.

    Returns:
        Score = -(area + 10·max_gap).
    """
    weights = np.asarray(weights, dtype=np.float64)
    m, n = weights.shape
    assert 1 <= m <= 500 and n == 20

    weights = np.maximum(weights, 0.0)
    weights = weights / weights.sum(axis=1, keepdims=True)

    # Vectorized density computation
    s2 = np.sum(weights**2, axis=1)
    s3 = np.sum(weights**3, axis=1)
    xs = 1.0 - s2
    ys = 1.0 - 3.0 * s2 + 2.0 * s3

    # Sort by edge density
    order = np.argsort(xs)
    xs = np.concatenate([[0.0], xs[order], [1.0]])
    ys = np.concatenate([[0.0], ys[order], [1.0]])

    # Slope-3 interpolated area + max gap
    hs = np.diff(xs)
    dys = np.diff(ys)

    area = 0.0
    for i in range(len(hs)):
        h = hs[i]
        if h <= 0:
            continue
        dy = dys[i]
        y1 = ys[i + 1]
        if dy < 0:
            area += y1 * h
        elif dy <= 3 * h:
            area += -dy**2 / 6 + y1 * h
        else:
            area += ys[i] * h + 1.5 * h**2

    max_gap = float(np.max(hs))
    return -(area + 10.0 * max_gap)


def evaluate(data: dict) -> float:
    """Score a solution for Problem 13. Matches arena verifier."""
    return compute_score(np.asarray(data["weights"], dtype=np.float64))


# ---------------------------------------------------------------------------
# Turán row construction
# ---------------------------------------------------------------------------


def turan_row(x_target: float, n_bins: int = 20) -> np.ndarray:
    """Construct probability vector achieving Razborov-minimum triangle density.

    Uses complete multipartite (Turán family) construction:
    - x ≤ 0.5: bipartite (triangle-free, y=0)
    - x > 0.5: (k+1)-partite on scallop k

    Args:
        x_target: target edge density in [0, 1-1/n_bins].
        n_bins: number of bins (default 20).

    Returns:
        Probability vector of length n_bins.
    """
    p = np.zeros(n_bins)

    if x_target <= 1e-14:
        p[0] = 1.0
        return p

    if x_target <= 0.5:
        # Bipartite: 2a(1-a) = x → a = (1 - sqrt(1-2x))/2
        a = 0.5 * (1.0 - np.sqrt(max(0.0, 1.0 - 2.0 * x_target)))
        p[0] = a
        p[1] = 1.0 - a
        return p

    # Find scallop k: x ∈ [1-1/k, 1-1/(k+1))
    k = int(1.0 / (1.0 - x_target) + 1e-10)
    k = max(k, 2)
    k = min(k, n_bins)

    if k >= n_bins:
        # Uniform distribution (max edge density)
        p[:] = 1.0 / n_bins
        return p

    # (k+1)-partite: k parts of size c, 1 part of size (1-kc)
    # Solve k(k+1)c² - 2kc + x = 0
    disc = 4.0 * k**2 - 4.0 * k * (k + 1) * x_target
    if disc < 0:
        # Fallback: balanced (k+1)-partite
        p[: k + 1] = 1.0 / (k + 1)
        return p

    sqrt_disc = np.sqrt(disc)
    c = (2.0 * k + sqrt_disc) / (2.0 * k * (k + 1))

    # Clamp to valid range [1/(k+1), 1/k]
    c = np.clip(c, 1.0 / (k + 1), 1.0 / k)
    remainder = max(0.0, 1.0 - k * c)

    p[:k] = c
    p[k] = remainder
    return p
