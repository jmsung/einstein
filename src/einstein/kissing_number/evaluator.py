"""Evaluator for the Kissing Number problem (Problem 6).

Exact replica of the arena verifier. Given 594 non-zero vectors in R^11,
place sphere centers at c_i = 2 * v_i / ||v_i|| and compute total overlap:

    score = sum_{i<j} max(0, 2 - ||c_i - c_j||)

If vectors are integer-valued (within 0.01 tolerance), uses exact integer
arithmetic: score = 0.0 if min pairwise squared distance >= max squared norm.

Lower score is better. Score = 0 would prove kappa(11) >= 594.
"""

import itertools

import numpy as np

N_VECTORS = 594
DIMENSION = 11


def exact_check(vectors: np.ndarray) -> bool:
    """Check if integer vectors form a valid kissing configuration.

    Returns True (score = 0) if all vectors are near-integer, non-zero,
    and min pairwise squared distance >= max squared norm.
    """
    rounded = np.around(vectors).astype(np.int64)
    if np.max(np.abs(vectors - rounded)) > 0.01:
        return False

    squared_norms = [sum(int(x) ** 2 for x in c) for c in rounded]
    if min(squared_norms) == 0:
        return False

    max_sq_norm = max(squared_norms)
    min_sq_dist = min(
        sum(int(a - b) ** 2 for a, b in zip(p, q))
        for p, q in itertools.combinations(rounded, 2)
    )
    return min_sq_dist >= max_sq_norm


def overlap_loss(vectors: np.ndarray) -> float:
    """Compute total overlap penalty for sphere centers.

    Centers are placed at c_i = 2 * v_i / ||v_i||. Two spheres overlap
    when ||c_i - c_j|| < 2. Penalty per pair = max(0, 2 - dist).
    """
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    if np.any(norms < 1e-12):
        raise ValueError("All vectors must be non-zero")

    centers = 2.0 * vectors / norms

    # Use dot products: ||c_i - c_j||^2 = 8(1 - <v_i, v_j>/(||v_i|| ||v_j||))
    # But match arena verifier exactly: build distance matrix
    diff = centers[:, None, :] - centers[None, :, :]
    dist_matrix = np.sqrt(np.sum(diff**2, axis=-1))

    n = centers.shape[0]
    mask = np.triu(np.ones((n, n), dtype=bool), k=1)
    penalties = np.maximum(0.0, 2.0 - dist_matrix[mask])
    return float(np.sum(penalties))


def overlap_loss_fast(vectors: np.ndarray) -> float:
    """Fast overlap loss via dot products. Equivalent but ~3x faster."""
    norms = np.linalg.norm(vectors, axis=1)
    if np.any(norms < 1e-12):
        raise ValueError("All vectors must be non-zero")

    unit = vectors / norms[:, None]
    gram = unit @ unit.T

    # ||c_i - c_j||^2 = 8(1 - gram[i,j]) => dist = 2*sqrt(2*(1-gram[i,j]))
    # penalty = max(0, 2 - dist) = max(0, 2 - 2*sqrt(2*(1 - gram[i,j])))
    # penalty > 0 when gram[i,j] > 0.5

    n = len(vectors)
    idx_i, idx_j = np.triu_indices(n, k=1)
    cos_vals = gram[idx_i, idx_j]

    # Clip for numerical safety
    cos_vals = np.clip(cos_vals, -1.0, 1.0)
    dists = 2.0 * np.sqrt(2.0 * (1.0 - cos_vals))
    penalties = np.maximum(0.0, 2.0 - dists)
    return float(np.sum(penalties))


def evaluate(data: dict) -> float:
    """Score a kissing number solution. Matches arena verifier exactly."""
    vectors = np.array(data["vectors"], dtype=np.float64)
    if vectors.ndim != 2 or vectors.shape[0] != N_VECTORS or vectors.shape[1] != DIMENSION:
        raise ValueError(f"Expected shape ({N_VECTORS}, {DIMENSION}), got {vectors.shape}")

    if exact_check(vectors):
        return 0.0

    return overlap_loss(vectors)
