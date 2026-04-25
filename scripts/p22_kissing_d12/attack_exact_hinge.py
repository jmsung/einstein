"""Exact-hinge Riemannian SGD attack on P22.

Strategy:
- CHRONOS's 840 have pairwise γ ≤ 0.5 exactly. Exact hinge: only pairs with γ > 0.5
  contribute. Gradient w.r.t. v_k is zero outside overlap region, so moves preserve
  the kissing structure naturally.
- Joint optimization of all 841 vectors (or filler-only if --fix-core).
- Many restarts with finite perturbations. Anneal step size.

Unlike softplus (which smears false gradient on all pairs), this uses the
exact objective — L-BFGS can handle it if we feed exact hinge + subgradient.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy.spatial.distance import pdist

sys.path.insert(0, "src")
from einstein.p22_kissing_d12.evaluator import overlap_loss

N = 841
D = 12
RESULTS_DIR = Path("results/p22_kissing_d12")
CHRONOS_PATH = RESULTS_DIR / "sota_best_chronos_rank1_id2081.json"


def load_chronos() -> np.ndarray:
    data = json.loads(CHRONOS_PATH.read_text())
    v = np.array(data["vectors"], dtype=np.float64)
    return v / np.linalg.norm(v, axis=1, keepdims=True)


def score(U: np.ndarray) -> float:
    """Arena score: diff-based overlap loss."""
    norms = np.linalg.norm(U, axis=1, keepdims=True)
    centers = 2.0 * U / norms
    d = pdist(centers)
    return float(np.maximum(0.0, 2.0 - d).sum())


def hinge_grad(U: np.ndarray) -> tuple[float, np.ndarray]:
    """Exact hinge loss and Riemannian gradient on S^(d-1)^n.

    Returns (loss, grad_U) where grad_U is projected onto tangent of each sphere.
    loss = Σ_{i<j, dist<2} (2 - dist_ij)
    """
    n = len(U)
    # Pairwise inner products
    G = U @ U.T  # (n, n)
    # Pair distance = 2*sqrt(2(1-γ)) for unit vectors
    # Build pairs only with γ > 0.5
    iu, ju = np.triu_indices(n, k=1)
    g = G[iu, ju]
    mask = g > 0.5 - 1e-15
    if not np.any(mask):
        return 0.0, np.zeros_like(U)

    i_act = iu[mask]
    j_act = ju[mask]
    g_act = np.clip(g[mask], -1.0, 1.0 - 1e-15)
    dist = 2.0 * np.sqrt(2.0 * (1.0 - g_act))
    h = 2.0 - dist
    loss = float(np.sum(h))

    # Gradient: d(2 - dist_ij)/dg_ij = √2 / √(1 - g_ij); sign: penalty rises with γ
    dh_dg = np.sqrt(2.0) / np.sqrt(1.0 - g_act)

    # Gradient in unit-vector space:
    # dg_ij / du_i = u_j, dg_ij / du_j = u_i
    # d loss / du_i = Σ_{j: pair(i,j) active} dh_dg * u_j
    grad_U = np.zeros_like(U)
    # Accumulate via numpy add.at for speed
    np.add.at(grad_U, i_act, dh_dg[:, None] * U[j_act])
    np.add.at(grad_U, j_act, dh_dg[:, None] * U[i_act])

    # Project onto tangent of each sphere
    dot = np.sum(grad_U * U, axis=1, keepdims=True)
    grad_U = grad_U - dot * U
    return loss, grad_U


def rsgd(
    U0: np.ndarray,
    n_steps: int,
    lr0: float,
    lr_decay: float = 1.0,
    momentum: float = 0.0,
    fix_core: bool = False,
    log_every: int = 100,
) -> tuple[np.ndarray, float, list]:
    """Riemannian SGD on the unit spheres.

    If fix_core=True, only the last vector (index 840) moves.
    """
    U = U0.copy()
    best_U = U.copy()
    best_loss = score(U)
    history = []
    vel = np.zeros_like(U)
    lr = lr0
    for t in range(n_steps):
        loss, g = hinge_grad(U)
        if fix_core:
            g[:-1] = 0.0
        vel = momentum * vel + g
        U = U - lr * vel
        U = U / np.linalg.norm(U, axis=1, keepdims=True)
        lr *= lr_decay
        if loss < best_loss - 1e-16:
            best_loss = loss
            best_U = U.copy()
        if t % log_every == 0:
            history.append((t, loss, lr))
    return best_U, best_loss, history


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["filler", "joint"], default="joint")
    ap.add_argument("--steps", type=int, default=2000)
    ap.add_argument("--lr", type=float, default=1e-3)
    ap.add_argument("--restarts", type=int, default=20)
    ap.add_argument("--pert-scales", type=str, default="1e-6,1e-5,1e-4,1e-3,1e-2,1e-1")
    ap.add_argument("--tag", type=str, default="joint")
    args = ap.parse_args()

    base = load_chronos()
    s0 = score(base)
    print(f"CHRONOS base score: {s0!r}  (fix_core={args.mode=='filler'})", flush=True)

    pert_scales = [float(x) for x in args.pert_scales.split(",")]
    rng = np.random.default_rng(20260425)

    best_U = base.copy()
    best_s = s0

    t0 = time.time()
    # First: starting exactly at CHRONOS (no perturbation)
    print(f"--- baseline restart: no perturbation ---", flush=True)
    U_opt, s_opt, _ = rsgd(
        base.copy(),
        args.steps,
        args.lr,
        lr_decay=0.999,
        momentum=0.9,
        fix_core=(args.mode == "filler"),
    )
    print(f"    result: {s_opt!r}  (Δ from CHRONOS: {s_opt - s0:+.3e})", flush=True)
    if s_opt < best_s:
        best_s = s_opt
        best_U = U_opt

    # Now perturbed restarts
    for r in range(args.restarts):
        scale = pert_scales[r % len(pert_scales)]
        pert = rng.standard_normal(base.shape) * scale
        U0 = base + pert
        if args.mode == "filler":
            # Only perturb last vector
            U0 = base.copy()
            U0[-1] = base[-1] + rng.standard_normal(D) * scale
        U0 = U0 / np.linalg.norm(U0, axis=1, keepdims=True)
        U_opt, s_opt, _ = rsgd(
            U0,
            args.steps,
            args.lr,
            lr_decay=0.999,
            momentum=0.9,
            fix_core=(args.mode == "filler"),
        )
        print(f"  restart {r:02d}  scale={scale:.0e}  → score={s_opt:.15f}  (Δ={s_opt - s0:+.3e})", flush=True)
        if s_opt < best_s:
            best_s = s_opt
            best_U = U_opt
            print(f"  >>> NEW BEST: {best_s!r}", flush=True)

    elapsed = time.time() - t0
    print(f"\nDone in {elapsed:.1f}s. Best = {best_s!r} (CHRONOS: {s0!r})", flush=True)
    print(f"Improvement: {s0 - best_s:+.6e}", flush=True)

    out = RESULTS_DIR / f"attack_exact_{args.tag}.json"
    json.dump(
        {"chronos_score": s0, "best_score": best_s, "vectors": best_U.tolist()},
        open(out, "w"),
    )
    print(f"Saved → {out}", flush=True)


if __name__ == "__main__":
    main()
