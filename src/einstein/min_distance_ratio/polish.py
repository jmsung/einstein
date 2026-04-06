"""High-precision polish for Problem 5 (Min Distance Ratio 2D, n=16).

The objective (max_d/min_d)² is non-smooth at the minimum (the optimal
configuration has many edges at min_d and max_d simultaneously). We reformulate
as a smooth NLP:

    minimize   s
    s.t.       ||p_i - p_j||²  >= 1     for all i<j    (120 constraints)
               ||p_i - p_j||²  <= s     for all i<j    (120 constraints)

This fixes scale via min_d² = 1. Translation and rotation are factored by
fixing p_0 = (0,0) and p_1.y = 0. Reflection is left free (both chiralities
are equivalent).

The score is then s = (max_d)² (since min_d² = 1).
"""

from __future__ import annotations

import numpy as np
from scipy.optimize import minimize


def _unpack(x: np.ndarray) -> tuple[np.ndarray, float]:
    """x = [p0x=0, p0y=0, p1x, p1y=0, p2x, p2y, ..., p15x, p15y, s]
    reduced to [p1x, p2x, p2y, p3x, p3y, ..., p15x, p15y, s] — 2*16 - 3 + 1 = 30.
    """
    # 30 elements: 29 coordinate dof + s
    p1x = x[0]
    coords = np.zeros((16, 2), dtype=np.float64)
    coords[1, 0] = p1x
    coords[2:, 0] = x[1::2][:14]
    coords[2:, 1] = x[2::2][:14]
    s = x[-1]
    return coords, s


def _pack(coords: np.ndarray, s: float) -> np.ndarray:
    x = np.empty(30, dtype=np.float64)
    x[0] = coords[1, 0]
    x[1::2][:14] = coords[2:, 0]
    x[2::2][:14] = coords[2:, 1]
    x[-1] = s
    return x


def _align(vectors: np.ndarray) -> np.ndarray:
    """Translate so point 0 is origin, rotate so point 1 has y=0, x>0."""
    V = vectors - vectors[0]
    # Rotate so V[1] points along +x
    angle = -np.arctan2(V[1, 1], V[1, 0])
    c, s = np.cos(angle), np.sin(angle)
    R = np.array([[c, -s], [s, c]])
    V = V @ R.T
    # Scale so V[1][0] positive
    if V[1, 0] < 0:
        V[:, 0] *= -1
    return V


def polish_slsqp(
    initial_vectors: np.ndarray,
    max_iter: int = 500,
    ftol: float = 1e-18,
    verbose: bool = False,
) -> tuple[np.ndarray, float]:
    """Polish a configuration using SLSQP with explicit inequality constraints.

    Returns (polished_vectors, score) where score = (max_d/min_d)^2.
    """
    V0 = _align(initial_vectors.astype(np.float64))
    # Normalize scale so min distance = 1
    D0 = np.sqrt(((V0[:, None] - V0[None]) ** 2).sum(-1))
    iu = np.triu_indices(16, 1)
    mind0 = D0[iu].min()
    V0 = V0 / mind0
    # Recompute after normalization
    D0 = np.sqrt(((V0[:, None] - V0[None]) ** 2).sum(-1))
    maxd0 = D0[iu].max()
    s0 = maxd0 ** 2 + 1e-9

    x0 = _pack(V0, s0)

    I = iu[0]
    J = iu[1]

    def objective(x):
        return x[-1]

    def obj_grad(x):
        g = np.zeros_like(x)
        g[-1] = 1.0
        return g

    def constraint_min(x):
        """d_ij² - 1 >= 0."""
        coords, _ = _unpack(x)
        d2 = ((coords[I] - coords[J]) ** 2).sum(-1)
        return d2 - 1.0

    def constraint_max(x):
        """s - d_ij² >= 0."""
        coords, s = _unpack(x)
        d2 = ((coords[I] - coords[J]) ** 2).sum(-1)
        return s - d2

    cons = [
        {"type": "ineq", "fun": constraint_min},
        {"type": "ineq", "fun": constraint_max},
    ]

    res = minimize(
        objective,
        x0,
        jac=obj_grad,
        constraints=cons,
        method="SLSQP",
        options={"maxiter": max_iter, "ftol": ftol, "disp": verbose},
    )

    coords, s = _unpack(res.x)
    # Compute actual score
    D = np.sqrt(((coords[:, None] - coords[None]) ** 2).sum(-1))
    pd = D[iu]
    mind, maxd = pd.min(), pd.max()
    score = float((maxd / mind) ** 2)
    return coords, score


def score_config(vectors: np.ndarray) -> float:
    """Exact arena-style scoring."""
    V = np.asarray(vectors, dtype=np.float64)
    D = np.sqrt(((V[:, None] - V[None]) ** 2).sum(-1))
    iu = np.triu_indices(16, 1)
    pd = D[iu]
    return float((pd.max() / pd.min()) ** 2)
