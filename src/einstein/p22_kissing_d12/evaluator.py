"""Evaluator for the Kissing Number problem in dimension 12 (Problem 22).

Exact replica of the arena verifier. Given 841 non-zero vectors in R^12,
place sphere centers at c_i = 2 * v_i / ||v_i|| and compute total overlap:

    score = sum_{i<j} max(0, 2 - ||c_i - c_j||)

If vectors are integer-valued (within 0.01 tolerance), uses exact integer
arithmetic: score = 0.0 if min pairwise squared distance >= max squared norm.

Lower score is better. Score = 0 would prove kappa(12) >= 841, an open
problem in mathematics. Current arena SOTA is 2.000000 (CHRONOS), achieved
by 840-vector Leech-Sloane P_{12a} config + 1 duplicate.
"""

import itertools

import numpy as np

N_VECTORS = 841
DIMENSION = 12


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

    n = len(vectors)
    idx_i, idx_j = np.triu_indices(n, k=1)
    cos_vals = gram[idx_i, idx_j]

    cos_vals = np.clip(cos_vals, -1.0, 1.0)
    dists = 2.0 * np.sqrt(2.0 * (1.0 - cos_vals))
    penalties = np.maximum(0.0, 2.0 - dists)
    return float(np.sum(penalties))


def overlap_loss_mpmath(vectors, dps: int = 50) -> float:
    """High-precision overlap loss matching the arena verifier.

    Arena verifier is assumed to evaluate in bignum precision (same convention
    as P6). Float64 under-counts overlap by up to ~1e-12 for tight basins
    whose pair distances are within a few ulps of 2.0. Use this as the
    ground-truth score for any submission decision.
    """
    from mpmath import mp, mpf, sqrt as mpsqrt

    arr = np.asarray(vectors, dtype=np.float64)
    if arr.ndim != 2 or arr.shape != (N_VECTORS, DIMENSION):
        raise ValueError(f"Expected shape ({N_VECTORS}, {DIMENSION}), got {arr.shape}")

    mp.dps = dps
    n, d = arr.shape

    V = [[mpf(repr(float(arr[i, k]))) for k in range(d)] for i in range(n)]
    norms = [mpsqrt(sum(x * x for x in row)) for row in V]
    if any(nrm == 0 for nrm in norms):
        raise ValueError("All vectors must be non-zero")
    two = mpf(2)
    C = [[two * V[i][k] / norms[i] for k in range(d)] for i in range(n)]

    total = mpf(0)
    for i in range(n):
        ci = C[i]
        for j in range(i + 1, n):
            cj = C[j]
            diff2 = mpf(0)
            for k in range(d):
                t = ci[k] - cj[k]
                diff2 += t * t
            dist = mpsqrt(diff2)
            if dist < two:
                total += two - dist

    return float(total)


def evaluate(data: dict) -> float:
    """Score a kissing number solution. Matches arena verifier exactly."""
    vectors = np.array(data["vectors"], dtype=np.float64)
    if vectors.ndim != 2 or vectors.shape[0] != N_VECTORS or vectors.shape[1] != DIMENSION:
        raise ValueError(f"Expected shape ({N_VECTORS}, {DIMENSION}), got {vectors.shape}")

    if exact_check(vectors):
        return 0.0

    return overlap_loss_mpmath(vectors)
