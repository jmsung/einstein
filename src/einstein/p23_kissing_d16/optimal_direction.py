"""Find the unit direction u* that minimizes S(u) = sum_i [<u, w_i>]_+ over
the link of v_0 in BW16.

This direction is what the rank-2 squeeze uses as the tangent to tilt the
4321st filler. Smaller S(u*) -> smaller score above 2.0 for a given delta.

Two passes:
1. Multi-start subgradient descent on the unit sphere of v_0-perp.
2. Polish via softplus-smoothed loss (so the active set stays differentiable).
"""

from __future__ import annotations

import numpy as np


def link_unit_projections(v0: np.ndarray, vectors: np.ndarray, tol: float = 1e-8) -> np.ndarray:
    """Return unit-normalized v_0-perp components of vectors at IP=1/2 with v_0."""
    inner = vectors @ v0
    mask = np.abs(inner - 0.5) < tol
    link = vectors[mask]
    proj = link - np.outer(link @ v0, v0)
    proj /= np.linalg.norm(proj, axis=1, keepdims=True)
    return proj


def s_value(u: np.ndarray, w: np.ndarray) -> float:
    return float(np.maximum(0.0, w @ u).sum())


def s_subgrad(u: np.ndarray, w: np.ndarray) -> np.ndarray:
    inner = w @ u
    active = inner > 0
    return w[active].sum(axis=0)


def s_softplus(u: np.ndarray, w: np.ndarray, beta: float = 50.0) -> tuple[float, np.ndarray]:
    """Softplus smoothing of S(u) for differentiable polish."""
    inner = w @ u  # (k,)
    bh = beta * inner
    sp = np.where(bh > 30, bh, np.log1p(np.exp(np.minimum(bh, 30))))
    score = float(sp.sum() / beta)
    sig = 1.0 / (1.0 + np.exp(-np.clip(bh, -500, 500)))
    grad = (sig[:, None] * w).sum(axis=0)
    return score, grad


def find_min_s_direction(
    bw_vectors: np.ndarray,
    v0: np.ndarray,
    n_starts: int = 400,
    n_steps_subgrad: int = 600,
    n_steps_polish: int = 800,
    lr: float = 0.05,
    seed: int = 0,
) -> tuple[np.ndarray, float]:
    """Return (u*, S(u*)) where u* lives in the (d-1)-dim subspace v_0-perp.

    The returned u* is in coordinates of an orthonormal basis of v_0-perp; in
    BW16 with v0 = e_0 we drop the first coord.
    """
    w_full = link_unit_projections(v0, bw_vectors)
    # basis of v0-perp (assumes v0 is along a coordinate axis)
    nz = np.nonzero(np.abs(v0) > 0.5)[0]
    assert len(nz) == 1, "Currently expects v_0 to be an axis-aligned ±e_i"
    drop_axis = nz[0]
    keep = [k for k in range(len(v0)) if k != drop_axis]
    w = w_full[:, keep]  # (k, d-1)

    rng = np.random.default_rng(seed)
    best_s = np.inf
    best_u = None
    d = w.shape[1]

    for s_idx in range(n_starts):
        u = rng.standard_normal(d)
        u /= np.linalg.norm(u)
        # subgradient pass
        for _ in range(n_steps_subgrad):
            g = s_subgrad(u, w)
            g_tan = g - (g @ u) * u
            u = u - lr * g_tan
            u /= np.linalg.norm(u)
        # polish with softplus
        for beta in (50.0, 200.0, 800.0):
            for _ in range(n_steps_polish // 3):
                _, g = s_softplus(u, w, beta=beta)
                g_tan = g - (g @ u) * u
                u = u - (lr * 0.3) * g_tan
                u /= np.linalg.norm(u)
        s = s_value(u, w)
        if s < best_s:
            best_s = s
            best_u = u.copy()
    return best_u, best_s
