"""Projected-Hessian floor certificate for sphere-constrained energy minima.

Promoted from the P10 Phase-7 finding
(knowledge/wiki/findings/p10-wales-global-min-hessian-certificate.md). A second-order
*certificate* that a configuration is a strict local minimum — stronger and
cheaper than a micro-perturbation lottery.

For points on the unit sphere minimising a pairwise energy E = Σ_{i<j} φ(p_i−p_j),
the Riemannian (projected) Hessian on the tangent space is

    H_tan = Tᵀ H_amb T − Tᵀ diag(μ_i I₃) T

where H_amb is the ambient Hessian, T is the 2-per-point tangent basis, and
μ_i = g_i·p_i is the constraint normal force (Lagrange multiplier). A
positive-definite H_tan — modulo the 3 SO(3) rotational zero modes of a
rotation-invariant energy — certifies a strict local minimum.

Default energy is Coulomb (φ(d)=1/‖d‖, Thomson). Pass `hess_block` for another
pairwise potential (Tammes / Riesz) — see `coulomb_hess_block`.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import numpy as np

_I3 = np.eye(3)


@dataclass(frozen=True)
class HessianCertificate:
    """Verdict of the projected-Hessian floor test."""

    is_strict_local_min: bool
    lambda_min_nonzero: float  # smallest non-gauge eigenvalue (the spectral gap)
    n_zero_modes: int  # expected 3 (SO(3) rotation) for a rotation-invariant energy
    n_negative_modes: int  # > 0 ⇒ saddle, not a minimum
    max_tangential_gradient: float  # ‖g − μp‖_max; ≈0 ⇒ a critical point
    eigenvalues: np.ndarray


def coulomb_hess_block(d: np.ndarray, dist: float) -> np.ndarray:
    """Hessian block ∇²(1/‖d‖) = (3 d dᵀ/‖d‖² − I)/‖d‖³."""
    return (3 * np.outer(d, d) / dist**2 - _I3) / dist**3


def certify_local_min(
    points: np.ndarray,
    *,
    hess_block: Callable[[np.ndarray, float], np.ndarray] = coulomb_hess_block,
    zero_tol: float = 1e-6,
    grad_tol: float = 1e-5,
) -> HessianCertificate:
    """Certify whether `points` (n×3, on/near the unit sphere) is a strict local
    minimum of the pairwise energy via the projected Hessian spectrum.

    `hess_block(d, ‖d‖)` returns the 3×3 ambient Hessian of the pair potential
    φ at separation d = p_i − p_j (Coulomb by default). The certificate is
    energy-agnostic given the right block.
    """
    P = np.asarray(points, dtype=np.float64)
    P = P / np.linalg.norm(P, axis=1, keepdims=True)
    n = len(P)

    diff = P[:, None, :] - P[None, :, :]
    dist = np.linalg.norm(diff, axis=2)
    np.fill_diagonal(dist, np.inf)
    inv3 = dist**-3

    # ambient gradient g_i = −Σ_j (p_i−p_j)/d³ (Coulomb force); μ_i = g_i·p_i
    G = -np.einsum("ijk,ij->ik", diff, inv3)
    mu = np.einsum("ik,ik->i", G, P)
    max_tan_grad = float(np.max(np.linalg.norm(G - mu[:, None] * P, axis=1)))

    # ambient Hessian (3n×3n)
    H = np.zeros((3 * n, 3 * n))
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            Hb = hess_block(diff[i, j], dist[i, j])
            H[3 * i : 3 * i + 3, 3 * j : 3 * j + 3] += -Hb
            H[3 * i : 3 * i + 3, 3 * i : 3 * i + 3] += Hb

    # tangent basis: 2 orthonormal vecs per point, ⊥ p_i
    T = np.zeros((3 * n, 2 * n))
    for i in range(n):
        p = P[i]
        a = np.array([1.0, 0, 0]) if abs(p[0]) < 0.9 else np.array([0, 1.0, 0])
        e1 = a - np.dot(a, p) * p
        e1 /= np.linalg.norm(e1)
        e2 = np.cross(p, e1)
        T[3 * i : 3 * i + 3, 2 * i] = e1
        T[3 * i : 3 * i + 3, 2 * i + 1] = e2

    # constraint-curvature correction −μ_i on each tangent direction
    M = np.zeros((3 * n, 3 * n))
    for i in range(n):
        M[3 * i : 3 * i + 3, 3 * i : 3 * i + 3] = mu[i] * _I3

    Hred = T.T @ H @ T - T.T @ M @ T
    Hred = 0.5 * (Hred + Hred.T)
    ev = np.linalg.eigvalsh(Hred)

    n_zero = int(np.sum(np.abs(ev) < zero_tol))
    n_neg = int(np.sum(ev < -zero_tol))
    nonzero = ev[np.abs(ev) >= zero_tol]
    lam_min = float(nonzero.min()) if nonzero.size else 0.0
    is_min = (n_neg == 0) and (max_tan_grad < grad_tol) and lam_min > 0

    return HessianCertificate(
        is_strict_local_min=is_min,
        lambda_min_nonzero=lam_min,
        n_zero_modes=n_zero,
        n_negative_modes=n_neg,
        max_tangential_gradient=max_tan_grad,
        eigenvalues=ev,
    )
