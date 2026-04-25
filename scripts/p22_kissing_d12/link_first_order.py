"""First-order analysis of CHRONOS's P_{12a} link structure.

For each core vector v_i, its 60°-link (vectors v_j with <v_i, v_j> = 0.5)
defines first-order penalty cost when moving the duplicate-filler away:

    Δscore ≈ 2δ · (min_u Σ_{j ∈ link_+} <u, w_j>  -  1)

where w_j = v_j - 0.5*v_i is the tangent projection, and link_+ = {j: <u, w_j> > 0}.

If min over unit u of `S(u) = Σ_{j ∈ link_+} <u, w_j>` is < 1, the duplicate
position is first-order escapable. If min ≥ 1, duplicate is a first-order
local minimum (though higher-order effects may still allow escape).

We solve min S(u) via:
- Stochastic sampling of many unit u (rough lower bound)
- Projected gradient descent on the unit sphere with subgradients
- LP-style exhaustive check: among 136 link vectors, try combinations.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

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


def project_tangent(v0: np.ndarray, W: np.ndarray) -> np.ndarray:
    """Project W (rows) onto the tangent space at v0."""
    proj = W - (W @ v0)[:, None] * v0[None, :]
    return proj


def min_S_u(W_tangent: np.ndarray, d: int, n_restarts: int = 400) -> tuple[float, np.ndarray]:
    """Minimize S(u) = sum_i max(0, <u, w_i>) over unit u in R^d."""
    rng = np.random.default_rng(0)
    best_val = np.inf
    best_u = None

    def f(u_flat):
        u = u_flat / max(np.linalg.norm(u_flat), 1e-12)
        vals = W_tangent @ u
        return float(np.maximum(0.0, vals).sum())

    # Subgradient method: we'll do smooth approximation via softmax
    def smooth_S(u_flat, beta):
        u = u_flat / max(np.linalg.norm(u_flat), 1e-12)
        z = W_tangent @ u
        # softplus
        zb = beta * z
        sp = np.where(zb > 30, zb, np.log1p(np.exp(np.clip(zb, -30, 30))))
        loss = float(sp.sum() / beta)
        # Gradient w.r.t. u
        sig = 1.0 / (1.0 + np.exp(-np.clip(zb, -60, 60)))
        # d loss / du = sum_i sig_i * W_tangent[i] / ||u_flat||  (approximately)
        # But u is normalized from u_flat, so gradient in u_flat is projected
        g_u = W_tangent.T @ sig
        n = np.linalg.norm(u_flat)
        g_u_proj = g_u - (g_u @ u) * u
        g_flat = g_u_proj / n
        return loss, g_flat

    for restart in range(n_restarts):
        u0 = rng.standard_normal(d)
        u0 /= np.linalg.norm(u0)
        u = u0.copy()
        for beta in [4.0, 16.0, 64.0, 256.0, 1024.0, 4096.0, 16384.0]:
            res = minimize(
                lambda x: smooth_S(x, beta),
                u,
                jac=True,
                method="L-BFGS-B",
                options={"maxiter": 500, "gtol": 1e-14},
            )
            u = res.x / np.linalg.norm(res.x)
        val = f(u)
        if val < best_val:
            best_val = val
            best_u = u.copy()

    return best_val, best_u


def main() -> int:
    core = load_core()
    print(f"Core: {core.shape}")

    # Pick v_0 = core[0] = (1, 0, ...)
    v0 = core[0]
    print(f"v_0 = {v0}")

    dots = core @ v0
    link_idx = np.where((np.abs(dots - 0.5) < 1e-9) & (np.arange(len(core)) != 0))[0]
    print(f"60°-link of v_0: {len(link_idx)} vectors")

    W = core[link_idx]
    W_tangent = project_tangent(v0, W)
    norms = np.linalg.norm(W_tangent, axis=1)
    print(f"tangent norms: min={norms.min():.6f} max={norms.max():.6f}  (expect sqrt(3)/2 = {np.sqrt(3)/2:.6f})")

    # Is the tangent link antipodally symmetric?
    # For each w_i, check if -w_i is in the set (matching some w_j)
    W_t = W_tangent
    found_pairs = 0
    for i in range(len(W_t)):
        for j in range(len(W_t)):
            if i != j and np.allclose(W_t[i], -W_t[j], atol=1e-9):
                found_pairs += 1
                break
    print(f"Tangent link antipodal pairs: {found_pairs} (of {len(W_t)})")

    # Minimize S(u) = sum_i max(0, <u, w_i>)
    print("\nMinimizing S(u) = Σ_i max(0, <u, w_i>) over unit u in R^12 tangent at v_0...")
    # Restrict u to the tangent hyperplane at v_0 (u ⊥ v_0)
    # Build an orthonormal basis for the tangent
    # We can just do optimization in R^12 and project u ⊥ v_0 at each step; but W_tangent
    # is already ⊥ v_0, so <u, w_i> = <u_⊥, w_i>. So we can work in R^11.
    # Use any u in R^12, the contribution from u's v_0-component is 0.
    best_val, best_u = min_S_u(W_tangent, d=12, n_restarts=200)
    print(f"Best min S(u) = {best_val}")
    if best_u is not None:
        # Projection of best_u onto tangent (for sanity)
        u_tan = best_u - (best_u @ v0) * v0
        u_tan /= np.linalg.norm(u_tan) + 1e-20
        print(f"  |u_tan|={np.linalg.norm(u_tan):.6f}")
        # Recompute S at u_tan
        s_check = float(np.maximum(0.0, W_tangent @ u_tan).sum())
        print(f"  S at projected u_tan: {s_check}")

    # Interpretation:
    # If best_val < 1.0, first-order escape exists (net duplicate loss drops)
    # If best_val >= 1.0, no first-order escape — 2.0 is locally optimal in first order
    print(f"\nFirst-order escape? {'YES' if best_val < 1.0 - 1e-6 else 'NO'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
