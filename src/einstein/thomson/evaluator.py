"""Evaluator for the Thomson Problem (Problem 10).

Place 282 points on the unit sphere S^2 to minimize Coulomb energy:

    E = sum_{i<j} 1 / ||p_i - p_j||

Points are auto-normalized to the unit sphere. Pairwise distances
below 1e-12 are clamped to avoid division by zero.

Lower score is better.
"""

import numpy as np

N_POINTS = 282
DIMENSION = 3
DIST_CLAMP = 1e-12


def coulomb_energy(points: np.ndarray) -> float:
    """Compute Coulomb energy for points on the unit sphere.

    Points are normalized to unit sphere. Returns sum of 1/r_ij
    over all distinct pairs.
    """
    norms = np.linalg.norm(points, axis=1, keepdims=True)
    if np.any(norms < DIST_CLAMP):
        raise ValueError("All vectors must be non-zero")
    pts = points / norms

    n = len(pts)
    energy = 0.0
    for i in range(n):
        for j in range(i + 1, n):
            diff = pts[i] - pts[j]
            dist = np.sqrt(np.dot(diff, diff))
            dist = max(dist, DIST_CLAMP)
            energy += 1.0 / dist
    return energy


def coulomb_energy_fast(points: np.ndarray) -> float:
    """Fast Coulomb energy using vectorized distance matrix."""
    norms = np.linalg.norm(points, axis=1, keepdims=True)
    if np.any(norms < DIST_CLAMP):
        raise ValueError("All vectors must be non-zero")
    pts = points / norms

    # Pairwise distance matrix via broadcasting
    diff = pts[:, None, :] - pts[None, :, :]
    dist_sq = np.sum(diff ** 2, axis=-1)

    n = len(pts)
    idx_i, idx_j = np.triu_indices(n, k=1)
    dists = np.sqrt(dist_sq[idx_i, idx_j])
    dists = np.maximum(dists, DIST_CLAMP)

    return float(np.sum(1.0 / dists))


def evaluate(data: dict) -> float:
    """Score a Thomson problem solution. Matches arena verifier."""
    vectors = np.array(data["vectors"], dtype=np.float64)
    if vectors.ndim != 2 or vectors.shape[0] != N_POINTS or vectors.shape[1] != DIMENSION:
        raise ValueError(
            f"Expected {N_POINTS} points in {DIMENSION}D, got shape {vectors.shape}"
        )
    return coulomb_energy_fast(vectors)
