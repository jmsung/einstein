"""Evaluator for the Tammes Problem (Problem 11, arena ID 11).

Exact replica of the arena verifier. Place n=50 points on the unit sphere
S² ⊂ R³, normalized to unit length, and compute the minimum pairwise
Euclidean distance. Higher is better.
"""

from __future__ import annotations

import numpy as np

N_VECTORS = 50
DIMENSION = 3


def evaluate(data: dict) -> float:
    """Score a Tammes solution. Matches arena verifier exactly.

    Each point is normalized to the unit sphere before scoring. Pairwise
    distances below 1e-12 are clamped (here: norms below 1e-12 are clamped).
    """
    vectors = np.array(data["vectors"], dtype=np.float64)
    assert vectors.shape == (N_VECTORS, DIMENSION), (
        f"Expected ({N_VECTORS}, {DIMENSION}), got {vectors.shape}"
    )
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    norms[norms < 1e-12] = 1e-12
    vectors = vectors / norms
    diffs = vectors[:, None, :] - vectors[None, :, :]
    dist_sq = np.sum(diffs**2, axis=2)
    iu = np.triu_indices(N_VECTORS, k=1)
    dists = np.sqrt(dist_sq[iu])
    return float(np.min(dists))


def min_distance(vectors: np.ndarray) -> float:
    """Fast min distance for already-unit vectors. Returns float min distance."""
    n = vectors.shape[0]
    gram = vectors @ vectors.T
    iu = np.triu_indices(n, k=1)
    cos_vals = np.clip(gram[iu], -1.0, 1.0)
    dist_sq = 2.0 * (1.0 - cos_vals)
    return float(np.sqrt(np.min(dist_sq)))


def project_to_sphere(vectors: np.ndarray) -> np.ndarray:
    """Normalize each row to unit length."""
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    norms[norms < 1e-12] = 1e-12
    return vectors / norms
