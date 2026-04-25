"""First-order link analysis at v_0 in BW16.

Penalty function p(γ) = 2 - 2*sqrt(2(1-γ)) for γ > 1/2.
At a duplicate filler position v* = v_0 + ε*u (u in v_0-tangent), to first order:

  Δscore_per_neighbor ≈ -p'(0.5) * <u, w_i> = -2 * <u, w_i>     (when <u, w_i> > 0)

But the duplicate-pair penalty also drops from 2 to ~ 2 - 2|ε|:

  Δscore_dup ≈ +2|ε| * <duplicate_anchor> = ... but actually
  ||c_dup - c_v0|| -> 2|ε| as ε -> 0 along the tangent, so penalty
  drops as 2 - 2|ε| (per pair), and we save 2|ε|.

Net first-order change:
  dscore/dε|_{ε=0+} = -2 + 2 * Σ_{i ∈ link, <u, w_i> > 0} <u, w_i>
                    = 2 * (S(u) - 1)        where S(u) = Σ [<u, w_i>]_+.

If min_u S(u) < 1 over the unit sphere in v_0⊥, score < 2 is achievable.
If min_u S(u) >= 1, 2.0 is a strict first-order local min (need second-order
or basin-jumping to escape).

This script:
1. Builds BW16, finds the 280 link vectors of v_0.
2. Projects them to v_0⊥ and renormalizes (these are the w_i unit vectors
   the analysis uses).
3. Multi-start gradient descent on S(u) over u in S^14 to estimate
   min_u S(u).
"""

from __future__ import annotations

import numpy as np

from einstein.p23_kissing_d16.baseline import bw16_min_vectors


def link_projections(v0: np.ndarray, vectors: np.ndarray, tol: float = 1e-8) -> np.ndarray:
    """Return unit-normalized projections of link(v0) onto v0-perp.

    The link of v0 is the set of v_i with <v_i, v0> = 1/2 (60-degree kiss).
    We zero out the v0-component and renormalize.
    """
    inner = vectors @ v0
    mask = np.abs(inner - 0.5) < tol
    link = vectors[mask]
    proj = link - np.outer(link @ v0, v0)
    norms = np.linalg.norm(proj, axis=1)
    proj = proj / norms[:, None]
    return proj


def s_value(u: np.ndarray, w: np.ndarray) -> float:
    """S(u) = sum max(0, <u, w_i>). w is (k, d). u is (d,)."""
    inner = w @ u
    return float(np.maximum(0.0, inner).sum())


def s_grad(u: np.ndarray, w: np.ndarray) -> np.ndarray:
    """Gradient of S(u) wrt u (subgradient at non-smooth points)."""
    inner = w @ u
    active = inner > 0
    return w[active].sum(axis=0)


def min_s_over_sphere(w: np.ndarray, n_starts: int = 1000, n_steps: int = 500, lr: float = 0.05, seed: int = 0) -> tuple[float, np.ndarray]:
    """Multi-start projected gradient descent on S(u) over the unit sphere."""
    rng = np.random.default_rng(seed)
    best_s = np.inf
    best_u = None
    d = w.shape[1]
    for s_idx in range(n_starts):
        u = rng.standard_normal(d)
        u /= np.linalg.norm(u)
        for _ in range(n_steps):
            g = s_grad(u, w)
            # Project gradient onto tangent at u, then retract
            g_tan = g - (g @ u) * u
            u = u - lr * g_tan
            u /= np.linalg.norm(u)
        s = s_value(u, w)
        if s < best_s:
            best_s = s
            best_u = u.copy()
    return best_s, best_u


def main() -> None:
    bw = bw16_min_vectors()
    v0 = bw[0]  # = (1, 0, ..., 0) since first ±e_i emitted by np.eye is +e_0
    # Or use v0 = -e_0 (matches CHRONOS SOTA orientation)
    print(f"v0 = {v0[:5]}... (first 5 coords)")

    w_full = link_projections(v0, bw)
    print(f"link size: {w_full.shape[0]} (expected 280)")
    print(f"link vectors live in v0-perp: max |<w_i, v0>| = {np.max(np.abs(w_full @ v0)):.2e}")

    # Project to a 15-d basis of v0-perp
    # Build basis: drop first coord (since v0 has only first coord nonzero)
    basis = np.eye(16)[1:]  # 15 x 16
    w15 = w_full @ basis.T  # (280, 15)
    print(f"w15 norms unique: {np.unique(np.round(np.linalg.norm(w15, axis=1), 8))}")

    print("\nMulti-start gradient descent on S(u)...")
    best_s, best_u = min_s_over_sphere(w15, n_starts=400, n_steps=600, lr=0.05)
    print(f"\nmin_u S(u) ≈ {best_s:.10f}")
    print(f"First-order escape iff min S(u) < 1.")
    print(f"Score change = 2*(S(u) - 1) per unit of |ε|; smaller S = better.")

    # Also report distribution of S(u) at convergence
    print()


if __name__ == "__main__":
    main()
