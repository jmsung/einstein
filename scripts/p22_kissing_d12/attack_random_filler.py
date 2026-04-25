"""Brute-search the 841st vector position over many random starts.

Fix CHRONOS's 840 as the core. Initialize the filler at many random unit
positions on S^11 and run exact-hinge Riemannian GD. Record basin minima.

Goal: find a basin with hinge loss < 2.0 (i.e., a placement where the
841st has multiple small-overlap near-neighbors summing to less than one
duplicate pair).
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


def load_core_840() -> np.ndarray:
    data = json.loads(CHRONOS_PATH.read_text())
    v = np.array(data["vectors"], dtype=np.float64)
    seen = {}
    keep = []
    for i, row in enumerate(v):
        key = tuple(row.tolist())
        if key not in seen:
            seen[key] = i
            keep.append(i)
    core = v[keep]
    return core / np.linalg.norm(core, axis=1, keepdims=True)


def score_of_filler(core: np.ndarray, v: np.ndarray) -> float:
    v = v / np.linalg.norm(v)
    centers = 2.0 * np.vstack([core, v[None, :]])
    d = pdist(centers)
    return float(np.maximum(0.0, 2.0 - d).sum())


def filler_loss_grad(core: np.ndarray, v: np.ndarray) -> tuple[float, np.ndarray]:
    """Return (hinge_loss, tangent gradient) for filler-only.

    v is assumed unit-norm. Gradient is projected onto tangent of S^11 at v.
    """
    gamma = core @ v  # (840,)
    mask = gamma > 0.5 + 1e-15
    if not np.any(mask):
        return 0.0, np.zeros_like(v)
    g = np.clip(gamma[mask], -1.0, 1.0 - 1e-15)
    dist = 2.0 * np.sqrt(2.0 * (1.0 - g))
    loss = float(np.sum(2.0 - dist))
    dh_dg = np.sqrt(2.0) / np.sqrt(1.0 - g)
    # gradient of sum h_i w.r.t. v = sum dh_dg * core[i] (for active i)
    grad_v_ambient = (dh_dg[:, None] * core[mask]).sum(axis=0)
    # tangent projection
    grad_v = grad_v_ambient - (grad_v_ambient @ v) * v
    return loss, grad_v


def rgd_filler(core: np.ndarray, v0: np.ndarray, n_steps: int, lr: float, decay: float = 0.999) -> tuple[np.ndarray, float]:
    v = v0 / np.linalg.norm(v0)
    best_v = v.copy()
    best_loss = score_of_filler(core, v)
    vel = np.zeros_like(v)
    momentum = 0.9
    cur_lr = lr
    for t in range(n_steps):
        loss, g = filler_loss_grad(core, v)
        if loss == 0:  # Outside any overlap — can't improve further
            best_loss = loss
            best_v = v.copy()
            break
        vel = momentum * vel + g
        v = v - cur_lr * vel
        nv = np.linalg.norm(v)
        if nv < 1e-9:
            v = np.random.default_rng().standard_normal(D)
            v /= np.linalg.norm(v)
        else:
            v = v / nv
        cur_lr *= decay
        # Use pdist-based score for fidelity
        s = score_of_filler(core, v)
        if s < best_loss:
            best_loss = s
            best_v = v.copy()
    return best_v, best_loss


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n-starts", type=int, default=200)
    ap.add_argument("--steps", type=int, default=2000)
    ap.add_argument("--lr", type=float, default=1e-3)
    ap.add_argument("--seed", type=int, default=20260425)
    ap.add_argument("--tag", type=str, default="random_filler")
    args = ap.parse_args()

    core = load_core_840()
    print(f"Core: {core.shape}", flush=True)

    rng = np.random.default_rng(args.seed)
    best = {"score": 2.0, "v": None, "source": "duplicate"}

    # Diverse seeds:
    # 1) Random unit vectors
    # 2) Midpoint between pairs of core vectors
    # 3) Small perturbations of core vectors (test each as a candidate)

    n_rand = int(0.5 * args.n_starts)
    seeds = []
    for k in range(n_rand):
        x = rng.standard_normal(D)
        seeds.append(("rand", x / np.linalg.norm(x)))
    # Midpoints between random pairs of core vectors
    for k in range(args.n_starts - n_rand):
        i, j = rng.choice(len(core), 2, replace=False)
        mid = core[i] + core[j]
        nm = np.linalg.norm(mid)
        if nm > 1e-9:
            seeds.append((f"mid_{i}_{j}", mid / nm))
        else:
            x = rng.standard_normal(D)
            seeds.append(("rand", x / np.linalg.norm(x)))

    t0 = time.time()
    basin_scores = []
    for idx, (src, v0) in enumerate(seeds):
        v_opt, s_opt = rgd_filler(core, v0, args.steps, args.lr)
        basin_scores.append(s_opt)
        if s_opt < best["score"] - 1e-14:
            best = {"score": s_opt, "v": v_opt.tolist(), "source": src, "idx": idx}
            print(f"  seed {idx:04d} [{src}] → {s_opt:.15f}  *** NEW BEST ***", flush=True)
        elif idx < 10 or idx % 50 == 0:
            print(f"  seed {idx:04d} [{src}] → {s_opt:.15f}", flush=True)

    elapsed = time.time() - t0
    print(f"\nTotal: {elapsed:.1f}s  ({elapsed/len(seeds):.2f}s/start)", flush=True)

    # Basin stats
    bs = np.array(basin_scores)
    print(f"Basin score distribution:")
    print(f"  min:  {bs.min():.6f}")
    print(f"  10%:  {np.percentile(bs, 10):.6f}")
    print(f"  50%:  {np.percentile(bs, 50):.6f}")
    print(f"  90%:  {np.percentile(bs, 90):.6f}")
    print(f"  max:  {bs.max():.6f}")
    # How many basins below 2.0?
    below_2 = (bs < 2.0 - 1e-12).sum()
    at_2 = (np.abs(bs - 2.0) < 1e-12).sum()
    above_2 = (bs > 2.0 + 1e-12).sum()
    print(f"  below 2.0: {below_2},  at 2.0: {at_2},  above 2.0: {above_2}")

    print(f"\nBest overall: {best['score']!r}")
    out = RESULTS_DIR / f"attack_{args.tag}.json"
    json.dump(best, open(out, "w"))
    print(f"Saved → {out}")


if __name__ == "__main__":
    main()
