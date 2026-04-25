"""Rigorous first-order analysis: compute min_{||u||=1, u⊥v_0} Σ_i max(0, <u, w_i>).

Since tangent link is fully antipodally symmetric (68 pairs), the objective
reduces to:  S(u) = Σ_{k=1..68} |<u, w_k>| .

We solve min S(u) s.t. ||u||=1 via:
1. Stochastic sampling + subgradient descent on sphere.
2. LP-based lower bound: for each representative w_k, compute
   cos-angle to minimize Σ; but the 68 w_k's live in R^11.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, "src")

RESULTS_DIR = Path("results/p22_kissing_d12")
CHRONOS_PATH = RESULTS_DIR / "sota_best_chronos_rank1_id2081.json"


def load_core() -> np.ndarray:
    data = json.loads(CHRONOS_PATH.read_text())
    vecs = np.array(data["vectors"], dtype=np.float64)
    seen = {}
    keep = []
    for i, row in enumerate(vecs):
        key = tuple(row.tolist())
        if key not in seen:
            seen[key] = i
            keep.append(i)
    return vecs[keep] / np.linalg.norm(vecs[keep], axis=1, keepdims=True)


def link_at(core: np.ndarray, i: int) -> np.ndarray:
    v0 = core[i]
    dots = core @ v0
    mask = (np.abs(dots - 0.5) < 1e-9) & (np.arange(len(core)) != i)
    return np.where(mask)[0]


def tangent(v0: np.ndarray, W: np.ndarray) -> np.ndarray:
    return W - (W @ v0)[:, None] * v0[None, :]


def antipodal_representatives(W: np.ndarray) -> np.ndarray:
    """Pick one per antipodal pair. Returns reps (n/2, d)."""
    n = len(W)
    used = np.zeros(n, dtype=bool)
    reps = []
    for i in range(n):
        if used[i]:
            continue
        used[i] = True
        # Find its antipode
        for j in range(i + 1, n):
            if used[j]:
                continue
            if np.allclose(W[i], -W[j], atol=1e-9):
                used[j] = True
                break
        reps.append(W[i])
    return np.array(reps)


def min_l1_subgrad(W: np.ndarray, n_restarts: int = 1000, n_iters: int = 5000, d: int = 11) -> tuple[float, np.ndarray]:
    """Minimize sum |<u, w_k>| over ||u||=1 in R^d via projected subgradient.
    W is shape (K, d_full), but we know it's in d-dim subspace.
    """
    rng = np.random.default_rng(42)
    # Project W onto its column-span
    U, S, Vt = np.linalg.svd(W, full_matrices=False)
    rank = int(np.sum(S > 1e-10))
    V = Vt[:rank]  # (rank, d_full), rows form orthonormal basis of span(W.T)
    Wproj = W @ V.T  # (K, rank)
    print(f"W rank={rank} (K={len(W)} reps in R^{W.shape[1]})")

    best_val = np.inf
    best_u = None
    K = len(W)
    for restart in range(n_restarts):
        u = rng.standard_normal(rank)
        u /= np.linalg.norm(u)
        lr = 0.1
        for it in range(n_iters):
            vals = Wproj @ u
            s = np.sum(np.abs(vals))
            if s < best_val:
                best_val = s
                best_u = V.T @ u  # back to full-dim
            # Subgradient: Σ sgn(v_k) · w_k
            sgn = np.sign(vals)
            # Avoid the 0 set
            sgn[sgn == 0] = rng.choice([-1.0, 1.0], size=(sgn == 0).sum())
            grad = Wproj.T @ sgn
            # Project onto tangent of sphere: g_⊥ = g - (g·u)u
            grad_t = grad - (grad @ u) * u
            u = u - lr * grad_t
            u /= np.linalg.norm(u)
            # Slow annealing
            if it % 500 == 499:
                lr *= 0.5

    return best_val, best_u


def main() -> int:
    core = load_core()
    print(f"Core shape: {core.shape}")

    v0 = core[0]
    link_idx = link_at(core, 0)
    W = core[link_idx]
    Wt = tangent(v0, W)

    reps = antipodal_representatives(Wt)
    print(f"Antipodal reps: {len(reps)} (of {len(Wt)} full link)")

    # Rank of reps
    print(f"rank(reps): {np.linalg.matrix_rank(reps, tol=1e-10)}")

    # Confirm reps span R^11 tangent
    # Minimize S(u) = Σ |<u, w_k>| over k=1..68, ||u||=1
    print("\nMinimizing S(u) = Σ |<u, w_k>| over unit u (subgradient)...")
    best_val, best_u = min_l1_subgrad(reps, n_restarts=100, n_iters=3000)
    print(f"Best min S(u) = {best_val:.10f}")
    print(f"best_u shape: {best_u.shape if best_u is not None else None}")
    if best_u is not None:
        # Full re-check
        vals = Wt @ best_u
        s_full = float(np.maximum(0.0, vals).sum())
        s_symm = float(np.abs(reps @ best_u).sum())
        print(f"Re-check: S_full_asym={s_full:.10f}  S_symm={s_symm:.10f}")
        # The first-order condition for escape is:
        # Δscore ≈ 2δ*(S_full - 1), and S_full = S_symm (for antipodal link)
        # Actually: S_full = Σ max(0, <u, w_i>) = (1/2) Σ |<u, w_i>| = (1/2) Σ |<u, w_i>|
        # where the sum is over all 136 link vectors. For antipodal link,
        # S_full = (1/2) Σ_{i=1..136} |<u, w_i>| = Σ_{k=1..68} |<u, w_k>| = S_symm
        # So the first-order loss change per δ is 2δ*(S_symm - 1).

    print(f"\n=== First-order verdict ===")
    print(f"Net Δscore per δ movement = 2δ · (S_min - 1) = 2δ · ({best_val:.6f} - 1) = 2δ · ({best_val - 1:.6f})")
    if best_val < 1 - 1e-6:
        print(">>> FIRST-ORDER ESCAPE EXISTS. Move in direction best_u to drop below 2.0.")
    else:
        print(">>> NO first-order escape. 2.0 is first-order optimal at the duplicate position.")

    # Save
    out = {
        "n_link": int(len(link_idx)),
        "n_reps": int(len(reps)),
        "rank_tangent": int(np.linalg.matrix_rank(reps, tol=1e-10)),
        "min_S": float(best_val),
        "best_u": best_u.tolist() if best_u is not None else None,
    }
    with open(RESULTS_DIR / "link_first_order.json", "w") as f:
        json.dump(out, f, indent=2)
    print(f"Saved → {RESULTS_DIR / 'link_first_order.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
