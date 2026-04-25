"""Attack: beat CHRONOS's 2.0 by finding a better 841st vector.

Strategy:
- Fix CHRONOS's 840 distinct P_{12a} unit vectors.
- Search over positions v ∈ S^11 for the 841st to minimize total hinge loss.
- Duplicate position gives exactly 2.0; we want strictly less.

Methods:
1. Analytical link-projection attack on v_0 = (1, 0, ..., 0). Given the
   12 axis-aligned neighbors at inner product 0.5, solve for u minimizing
   the first-order penalty.
2. Multi-start Nelder-Mead / L-BFGS from random + hole-seeded positions.
3. Softplus-smoothed hinge with L-BFGS, anneal smoothing → 0.

Outputs: results/p22_kissing_d12/attack_single_filler.json with best
config and score; prints progress.
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy.optimize import minimize
from scipy.spatial.distance import pdist, cdist

sys.path.insert(0, "src")
from einstein.p22_kissing_d12.evaluator import overlap_loss

RESULTS_DIR = Path("results/p22_kissing_d12")
CHRONOS_PATH = RESULTS_DIR / "sota_best_chronos_rank1_id2081.json"
OUT_PATH = RESULTS_DIR / "attack_single_filler.json"


def load_chronos_core() -> np.ndarray:
    """Return the 840 distinct CHRONOS unit vectors (dropping the duplicate)."""
    data = json.loads(CHRONOS_PATH.read_text())
    vecs = np.array(data["vectors"], dtype=np.float64)
    # Drop the duplicate: find two identical rows and keep one.
    seen = {}
    keep = []
    for i, row in enumerate(vecs):
        key = tuple(row.tolist())
        if key not in seen:
            seen[key] = i
            keep.append(i)
    core = vecs[keep]
    assert core.shape == (840, 12), f"expected (840, 12), got {core.shape}"
    # Re-normalize for numerical safety
    core = core / np.linalg.norm(core, axis=1, keepdims=True)
    return core


def score_with_filler(core: np.ndarray, v: np.ndarray) -> float:
    """Compute total hinge loss for the 840 core + one filler v."""
    v = v / np.linalg.norm(v)
    # Fast: compute centers = 2 * unit vectors, all pairwise distances
    centers = 2.0 * np.vstack([core, v[None, :]])
    d = pdist(centers)
    return float(np.maximum(0.0, 2.0 - d).sum())


def score_via_arena_path(core: np.ndarray, v: np.ndarray) -> float:
    """Score via the diff-based (arena-matching) overlap_loss."""
    v = v / np.linalg.norm(v)
    all_vecs = np.vstack([core, v[None, :]])
    return overlap_loss(all_vecs)


def link_of(core: np.ndarray, i: int, gamma_thresh: float = 0.5 - 1e-9) -> np.ndarray:
    """Return indices of core vectors j != i with <v_i, v_j> >= gamma_thresh."""
    v_i = core[i]
    dots = core @ v_i
    idx = np.where((np.arange(len(core)) != i) & (dots >= gamma_thresh))[0]
    return idx


def analyze_link(core: np.ndarray, i: int) -> None:
    """Print the link structure of core[i] — distribution of inner products."""
    v_i = core[i]
    dots = core @ v_i
    dots = np.delete(dots, i)
    vals, counts = np.unique(np.round(dots, 10), return_counts=True)
    print(f"  link of core[{i}] inner-product distribution:")
    for g, c in zip(vals, counts):
        print(f"    γ = {g:+.4f} : {c}x")


def neg_hinge_over_filler(v_flat: np.ndarray, core: np.ndarray) -> float:
    v = v_flat
    n = np.linalg.norm(v)
    if n < 1e-12:
        return 1e9
    u = v / n
    # Inner products
    gamma = core @ u
    # Pairs with gamma > 0.5 contribute
    mask = gamma > 0.5
    if not np.any(mask):
        return 0.0
    g = np.clip(gamma[mask], -1.0, 1.0)
    d = 2.0 * np.sqrt(2.0 * (1.0 - g))
    return float(np.sum(np.maximum(0.0, 2.0 - d)))


def softplus_hinge(v_flat: np.ndarray, core: np.ndarray, beta: float) -> tuple[float, np.ndarray]:
    """Softplus-smoothed hinge: log(1+exp(β(2-dist)))/β.  As β→∞, → max(0, 2-dist).

    Returns (loss, grad_u) where grad_u is the (unnormalized) gradient w.r.t. v.
    """
    v = v_flat
    n = np.linalg.norm(v)
    if n < 1e-12:
        return 1e9, np.zeros_like(v)
    u = v / n
    gamma = core @ u
    g = np.clip(gamma, -1.0 + 1e-15, 1.0 - 1e-15)
    # dist_i = 2 sqrt(2(1 - g_i))
    # hinge = 2 - dist_i
    h = 2.0 - 2.0 * np.sqrt(2.0 * (1.0 - g))
    # softplus(βh)/β
    z = beta * h
    # Stable softplus
    sp = np.where(z > 30, z, np.log1p(np.exp(np.clip(z, -30, 30))))
    loss = float(sp.sum() / beta)

    # Gradient: dsp/dh = sigmoid(βh) = 1/(1+e^{-βh})
    sig = 1.0 / (1.0 + np.exp(-np.clip(z, -60, 60)))
    # dh/dg = d(2 - 2*sqrt(2(1-g)))/dg = -2 * (-1/sqrt(2(1-g))) = sqrt(2)/sqrt(1-g)
    dh_dg = np.sqrt(2.0) / np.sqrt(1.0 - g)
    # dg/du = core (each row is v_i, and gamma_i = <core_i, u>)
    # dg/dv = (I - u u^T) / ||v|| ⋅ core_i^T
    # loss grad_v = sum_i sig_i * dh/dg_i * dg_i/dv
    # dg_i/dv = (v_i - (<v_i, u>) u) / ||v||
    w = sig * dh_dg  # per-row weight (shape 840,)
    # sum_i w_i * core_i (gradient of sum w_i * g_i w.r.t. u)
    grad_u_unprojected = core.T @ w
    # Project onto tangent at u: P = I - u u^T
    grad_u_tangent = grad_u_unprojected - (u @ grad_u_unprojected) * u
    # grad_v = grad_u_tangent / ||v||
    grad_v = grad_u_tangent / n
    return loss, grad_v


def optimize_filler_softplus(
    core: np.ndarray,
    v0: np.ndarray,
    betas: list[float] | None = None,
    maxiter_per_beta: int = 500,
) -> tuple[np.ndarray, float]:
    """Anneal softplus β and run L-BFGS at each level. Returns best (v, exact_loss)."""
    if betas is None:
        betas = [4.0, 16.0, 64.0, 256.0, 1024.0, 4096.0, 16384.0, 65536.0]
    v = v0.copy()
    v /= np.linalg.norm(v)
    for beta in betas:
        def f_and_g(v_flat):
            loss, grad = softplus_hinge(v_flat, core, beta)
            return loss, grad

        res = minimize(
            f_and_g,
            v,
            jac=True,
            method="L-BFGS-B",
            options={"maxiter": maxiter_per_beta, "gtol": 1e-16, "ftol": 1e-18},
        )
        v = res.x / np.linalg.norm(res.x)
    exact = neg_hinge_over_filler(v, core)
    return v, exact


def sample_sphere(rng: np.random.Generator, d: int = 12) -> np.ndarray:
    x = rng.standard_normal(d)
    return x / np.linalg.norm(x)


def main() -> int:
    core = load_chronos_core()
    print(f"Loaded CHRONOS core: shape={core.shape}")

    # Duplicate baseline: filler = core[0]
    v_dup = core[0].copy()
    s_dup = score_via_arena_path(core, v_dup)
    print(f"Duplicate baseline (filler = core[0]): arena-path score = {s_dup!r}")

    # Analyze link of v_0
    print("\n=== Link analysis of v_0 = core[0] ===")
    analyze_link(core, 0)
    nbrs = link_of(core, 0)
    print(f"  60-degree neighbors (γ=0.5): {len(nbrs)}")

    # --- Attack 1: multi-start softplus L-BFGS ---
    print("\n=== Attack 1: multi-start softplus L-BFGS ===")
    rng = np.random.default_rng(20260425)
    N_RESTARTS = 200
    best = {"score": s_dup, "v": v_dup.copy(), "method": "duplicate"}

    # Seeds:
    # (a) All unit random on sphere
    # (b) Perturbed duplicate positions
    # (c) Midpoints between pairs of neighbors (candidate deep-hole directions)
    seeds: list[tuple[str, np.ndarray]] = []
    for k in range(N_RESTARTS):
        seeds.append((f"rand{k}", sample_sphere(rng)))

    # Perturbed duplicates: take a core vector and perturb
    for k in range(50):
        i = rng.integers(0, 840)
        pert = core[i] + 0.2 * rng.standard_normal(12)
        pert /= np.linalg.norm(pert)
        seeds.append((f"pert_dup{i}_{k}", pert))

    # Neighbor midpoints (pairs of near-neighbors for candidate hole centers)
    for k in range(50):
        i = rng.integers(0, 840)
        j = rng.integers(0, 840)
        while j == i:
            j = rng.integers(0, 840)
        mid = core[i] + core[j]
        if np.linalg.norm(mid) > 1e-9:
            mid /= np.linalg.norm(mid)
            seeds.append((f"mid_{i}_{j}", mid))

    t0 = time.time()
    for name, v0 in seeds:
        v_opt, s_opt = optimize_filler_softplus(core, v0)
        if s_opt < best["score"] - 1e-15:
            best = {"score": s_opt, "v": v_opt.copy(), "method": f"softplus-lbfgs:{name}"}
            # Re-verify via arena-path
            s_arena = score_via_arena_path(core, v_opt)
            print(f"  IMPROVEMENT: {name}  score={s_opt!r}  arena-path={s_arena!r}")

    elapsed = time.time() - t0
    print(f"\nAttack 1 done: {len(seeds)} starts in {elapsed:.1f}s. Best score = {best['score']!r}")

    # Re-score best via arena path for fidelity
    best_arena = score_via_arena_path(core, best["v"])
    print(f"Best re-scored via arena path: {best_arena!r}")

    # Save
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    out = {
        "core_source": str(CHRONOS_PATH),
        "method": best["method"],
        "score_internal": best["score"],
        "score_arena_path": best_arena,
        "v": best["v"].tolist(),
        "all_vectors": np.vstack([core, best["v"][None, :]]).tolist(),
    }
    with open(OUT_PATH, "w") as f:
        json.dump(out, f)
    print(f"\nSaved best config → {OUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
