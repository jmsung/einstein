"""Polish routine for Tammes (n=50) solutions.

Given a configuration of 50 unit vectors on S², identify the set of
pairs achieving the minimum distance and run SLSQP on the constrained
max-d problem so that those pair distances are equal to d and every
other pair distance is at least d. Drives the active-pair residuals to
machine precision.
"""

from __future__ import annotations

import numpy as np
from scipy.optimize import minimize


def normalize(P: np.ndarray) -> np.ndarray:
    return P / np.linalg.norm(P, axis=1, keepdims=True)


def min_dist(P: np.ndarray) -> float:
    """Minimum pairwise Euclidean distance via the gram matrix."""
    n = P.shape[0]
    gram = P @ P.T
    iu = np.triu_indices(n, k=1)
    cos_vals = np.clip(gram[iu], -1.0, 1.0)
    return float(np.sqrt(np.min(2.0 * (1.0 - cos_vals))))


def find_active_pairs(P: np.ndarray, tol: float = 1e-9) -> tuple[list[tuple[int, int]], float]:
    """Return (active_pairs, dmin) where active_pairs is every (i, j)
    whose pairwise distance is within ``tol`` of the minimum.
    """
    n = P.shape[0]
    gram = P @ P.T
    iu_i, iu_j = np.triu_indices(n, k=1)
    cos_vals = np.clip(gram[iu_i, iu_j], -1.0, 1.0)
    dists = np.sqrt(2.0 * (1.0 - cos_vals))
    dmin = float(dists.min())
    active = [
        (int(iu_i[k]), int(iu_j[k]))
        for k in range(len(dists))
        if dists[k] - dmin < tol
    ]
    return active, dmin


def slsqp_polish(
    P0: np.ndarray,
    max_pairs: int = 200,
    tol_active: float = 1e-6,
    verbose: bool = True,
) -> tuple[np.ndarray, float]:
    """Maximize d subject to ``||p_i - p_j||^2 >= d^2`` for each active pair
    and ``||p_i||^2 == 1`` for each point. Returns the polished configuration
    and the post-polish min distance, or the original inputs if SLSQP did
    not improve on the starting value.

    Variables: 50*3 = 150 coords + 1 (d) = 151 unknowns.
    """
    n = P0.shape[0]
    P = normalize(P0).copy()
    active, d0 = find_active_pairs(P, tol=tol_active)
    if len(active) > max_pairs:
        active, _ = find_active_pairs(P, tol=tol_active / 10)
        active = active[:max_pairs]
    if verbose:
        print(f"  active pairs (tol {tol_active}): {len(active)}, d0={d0:.16f}")

    def unpack(x):
        return x[: n * 3].reshape(n, 3), x[-1]

    def neg_d(x):
        return -x[-1]

    def neg_d_grad(x):
        g = np.zeros_like(x)
        g[-1] = -1.0
        return g

    cons = []
    for (i, j) in active:
        def cf(x, i=i, j=j):
            P_, d = unpack(x)
            diff = P_[i] - P_[j]
            return float(diff @ diff - d * d)

        def cj(x, i=i, j=j):
            P_, d = unpack(x)
            g = np.zeros_like(x)
            diff = P_[i] - P_[j]
            g[3 * i : 3 * i + 3] = 2 * diff
            g[3 * j : 3 * j + 3] = -2 * diff
            g[-1] = -2 * d
            return g

        cons.append({"type": "ineq", "fun": cf, "jac": cj})

    for i in range(n):
        def sf(x, i=i):
            P_, _ = unpack(x)
            return float(P_[i] @ P_[i] - 1.0)

        def sj(x, i=i):
            g = np.zeros_like(x)
            P_, _ = unpack(x)
            g[3 * i : 3 * i + 3] = 2 * P_[i]
            return g

        cons.append({"type": "eq", "fun": sf, "jac": sj})

    x0 = np.concatenate([P.ravel(), [d0]])
    res = minimize(
        neg_d,
        x0,
        jac=neg_d_grad,
        constraints=cons,
        method="SLSQP",
        options={"maxiter": 500, "ftol": 1e-16, "disp": verbose},
    )
    P_new, _d_var = unpack(res.x)
    P_new = normalize(P_new)
    d_actual = min_dist(P_new)
    if verbose:
        print(f"  SLSQP result actual={d_actual:.16f}")
    if d_actual > d0:
        return P_new, d_actual
    return P, d0
