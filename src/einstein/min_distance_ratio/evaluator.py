"""Arena-matching evaluator for Problem 5: Min Distance Ratio (2D, n=16).

Score = (max_pairwise_distance / min_pairwise_distance) ** 2.

Lower is better. Points must be distinct (min distance > 1e-12).
"""

from __future__ import annotations

import numpy as np


def evaluate(data: dict) -> float:
    """Exact arena verifier (copied verbatim from the arena spec).

    Args:
        data: dict with key "vectors" → array of 16 [x, y] coord pairs.

    Returns:
        (max_dist / min_dist) ** 2.
    """
    vectors = np.array(data["vectors"], dtype=np.float64)
    if vectors.ndim != 2 or vectors.shape[0] != 16 or vectors.shape[1] != 2:
        raise ValueError("Expected exactly 16 points in 2 dimensions, shape (16, 2)")
    n = vectors.shape[0]
    diff = vectors[:, None, :] - vectors[None, :, :]
    dist_matrix = np.sqrt(np.sum(diff ** 2, axis=-1))
    mask = np.triu(np.ones((n, n), dtype=bool), k=1)
    pairwise = dist_matrix[mask]
    min_d = np.min(pairwise)
    if min_d < 1e-12:
        raise ValueError("Points must be distinct (min distance < 1e-12)")
    max_d = np.max(pairwise)
    return float((max_d / min_d) ** 2)


def evaluate_verbose(data: dict) -> dict:
    """Return score plus contact-graph diagnostics.

    min_edges: number of pairs at min distance (within 1e-10 rel tol)
    max_edges: number of pairs at max distance (within 1e-10 rel tol)
    """
    vectors = np.array(data["vectors"], dtype=np.float64)
    n = vectors.shape[0]
    diff = vectors[:, None, :] - vectors[None, :, :]
    D = np.sqrt(np.sum(diff ** 2, axis=-1))
    iu = np.triu_indices(n, k=1)
    pair = D[iu]
    mind = pair.min()
    maxd = pair.max()
    score = float((maxd / mind) ** 2)
    min_edges = int(np.sum(pair < mind * (1 + 1e-10)))
    max_edges = int(np.sum(pair > maxd * (1 - 1e-10)))
    # Also tighter tolerance for true contacts
    min_edges_tight = int(np.sum(pair < mind * (1 + 1e-6)))
    max_edges_tight = int(np.sum(pair > maxd * (1 - 1e-6)))
    return {
        "score": score,
        "min_dist": float(mind),
        "max_dist": float(maxd),
        "min_edges": min_edges,
        "max_edges": max_edges,
        "min_edges_tight": min_edges_tight,
        "max_edges_tight": max_edges_tight,
    }
