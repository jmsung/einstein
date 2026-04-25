"""Joint attack: optimize all 841 vectors (not just the filler).

Idea: CHRONOS's 840 kissing pairs each have γ = 0.5 exactly. Moving any of
them to slightly > 0.5 pushes the pair apart without cost (penalty was 0).
That freedom might allow us to "open a hole" for the 841st such that the
total hinge loss drops below 2.0.

Approach:
- Start from CHRONOS 841 (840 + duplicate) → score 2.0.
- Softplus-smoothed hinge with L-BFGS on all 841 × 12 = 10,092 variables.
- Re-normalize unit vectors after each step.
- Anneal softplus β from low (smooth) to high (near-exact hinge).
- Many restarts with different perturbations.
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy.optimize import minimize
from scipy.spatial.distance import pdist

sys.path.insert(0, "src")
from einstein.p22_kissing_d12.evaluator import overlap_loss

RESULTS_DIR = Path("results/p22_kissing_d12")
CHRONOS_PATH = RESULTS_DIR / "sota_best_chronos_rank1_id2081.json"
OUT_PATH = RESULTS_DIR / "attack_joint_best.json"

N = 841
D = 12


def load_chronos_841() -> np.ndarray:
    data = json.loads(CHRONOS_PATH.read_text())
    v = np.array(data["vectors"], dtype=np.float64)
    assert v.shape == (N, D)
    return v / np.linalg.norm(v, axis=1, keepdims=True)


def score_fast(vecs: np.ndarray) -> float:
    """Arena-path score via diff-based pdist (matches overlap_loss)."""
    n = len(vecs)
    norms = np.linalg.norm(vecs, axis=1, keepdims=True)
    centers = 2.0 * vecs / norms
    d = pdist(centers)
    return float(np.maximum(0.0, 2.0 - d).sum())


def softplus_joint(x_flat: np.ndarray, beta: float) -> tuple[float, np.ndarray]:
    """Softplus hinge on all pairs. x_flat has shape (N*D,). Unit-sphere constraint
    is enforced by working with normalized vectors within the cost."""
    X = x_flat.reshape(N, D)
    norms = np.linalg.norm(X, axis=1, keepdims=True)
    U = X / norms  # unit vectors
    # centers c_i = 2 u_i
    C = 2.0 * U
    # pairwise squared distances
    # Use ||c_i - c_j||² = 4 * (1 - <u_i, u_j>) * 2  wait no
    # ||c_i - c_j||² = ||c_i||² + ||c_j||² - 2<c_i, c_j> = 4 + 4 - 8<u_i,u_j> = 8(1 - <u_i,u_j>)
    # dist = sqrt(8(1 - <u_i, u_j>)) = 2*sqrt(2(1 - γ))
    G = U @ U.T  # gram of unit vectors
    np.fill_diagonal(G, np.nan)  # exclude self
    g = G  # (N, N) symmetric
    # Only pairs i<j
    iu, ju = np.triu_indices(N, k=1)
    gij = g[iu, ju]
    gij = np.clip(gij, -1.0 + 1e-15, 1.0 - 1e-15)
    # dist_ij, hinge h_ij = 2 - dist_ij
    dist_ij = 2.0 * np.sqrt(2.0 * (1.0 - gij))
    h = 2.0 - dist_ij
    # softplus
    z = beta * h
    sp = np.where(z > 30, z, np.log1p(np.exp(np.clip(z, -40, 40))))
    loss = float(sp.sum() / beta)

    # Gradient
    # dsp/dh = sigmoid(βh)
    sig = 1.0 / (1.0 + np.exp(-np.clip(z, -60, 60)))
    # dh/dg = d(2 - 2*sqrt(2(1-g)))/dg = sqrt(2) / sqrt(1-g)
    dh_dg = np.sqrt(2.0) / np.sqrt(1.0 - gij)
    # Gradient of loss w.r.t. g_ij:  sig_ij * dh_dg_ij
    # The gradient of g_ij = <u_i, u_j> w.r.t. u_i is u_j (and vice versa)
    # Build a sparse gradient: for each pair, add sig_ij * dh_dg_ij * u_j to grad_u_i (and symmetric).
    # Efficiently: W is (N, N) matrix with W[i,j] = sig_ij * dh_dg_ij, then grad_U = W @ U + W^T @ U = 2 * W @ U
    # (since W is symmetric after filling)
    W = np.zeros((N, N))
    W[iu, ju] = sig * dh_dg
    W[ju, iu] = W[iu, ju]
    dloss_du = W @ U  # (N, D) — each row is sum_j W[i,j] * u_j

    # Now chain to x_flat: u_i = x_i / ||x_i||, so du_i/dx_i = (I - u_i u_i^T) / ||x_i||
    # dloss/dx_i = (I - u_i u_i^T) / ||x_i|| @ dloss_du[i]
    dot = np.sum(dloss_du * U, axis=1, keepdims=True)  # (N, 1)
    dloss_dx = (dloss_du - dot * U) / norms  # (N, D)
    return loss, dloss_dx.flatten()


def optimize_joint(x0: np.ndarray, betas: list[float], maxiter: int = 300) -> tuple[np.ndarray, float]:
    x = x0.flatten()
    for beta in betas:
        res = minimize(
            lambda xf: softplus_joint(xf, beta),
            x,
            jac=True,
            method="L-BFGS-B",
            options={"maxiter": maxiter, "gtol": 1e-14, "ftol": 1e-16},
        )
        x = res.x
        X = x.reshape(N, D)
        # Re-normalize
        norms = np.linalg.norm(X, axis=1, keepdims=True)
        X = X / norms
        x = X.flatten()
        s = score_fast(X)
        print(f"  β={beta:.1f}  loss_softplus={res.fun:.6f}  exact_hinge={s:.9f}")
    return x.reshape(N, D), s


def main() -> int:
    base = load_chronos_841()
    s0 = score_fast(base)
    print(f"CHRONOS base score: {s0!r}")

    best_score = s0
    best_X = base.copy()

    # Start 1: minimal perturbation of CHRONOS
    rng = np.random.default_rng(2026)
    for restart in range(5):
        print(f"\n--- Restart {restart} ---")
        if restart == 0:
            pert = base.copy()  # start exactly at CHRONOS
        else:
            pert = base + rng.standard_normal(base.shape) * (10 ** -(restart + 1))
            pert = pert / np.linalg.norm(pert, axis=1, keepdims=True)

        betas = [4.0, 16.0, 64.0, 256.0, 1024.0, 4096.0, 16384.0, 65536.0]
        X_opt, s_opt = optimize_joint(pert, betas, maxiter=200)
        print(f"Final exact hinge: {s_opt:.12f}")
        if s_opt < best_score:
            print(f">>> NEW BEST: {s_opt!r}")
            best_score = s_opt
            best_X = X_opt

    # Save
    out = {
        "chronos_score": s0,
        "best_score": best_score,
        "improvement": s0 - best_score,
        "vectors": best_X.tolist(),
    }
    with open(OUT_PATH, "w") as f:
        json.dump(out, f)
    print(f"\nBest overall: {best_score!r}  (CHRONOS: {s0!r})")
    print(f"Saved → {OUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
