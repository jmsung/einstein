"""ShinkaEvolve init + ring rotation for P14 (n=26).

Hardcoded init based on Shinka paper Listing 2:
  centers_init[0:4]   = 4 corners (inset 0.06)
  centers_init[4:8]   = 4 edge midpoints
  centers_init[8]     = (0.5, 0.5)
  centers_init[9:15]  = 6 inner ring at radius 0.23, golden-angle spiral
  centers_init[15:26] = 11 outer ring at radius 0.48, golden-angle * 1.003

Ring rotation move: rotate inner OR outer ring rigidly around center by N(0, 0.15).
SA loop: 70% local jitter (2-5 random circles, σ=0.04), 30% ring rotation.
"""

from __future__ import annotations

import argparse
import json
import math
import multiprocessing as mp
import time
from pathlib import Path

import numpy as np

GOLDEN_ANGLE = math.pi * (3 - math.sqrt(5))  # ≈ 2.39996 rad


def shinka_init() -> np.ndarray:
    """Reproduce ShinkaEvolve's hardcoded initial configuration."""
    centers = np.zeros((26, 2))
    radii = np.full(26, 0.05)

    # 0-3: 4 corners (inset 0.06)
    inset = 0.06
    centers[0] = [inset, inset]
    centers[1] = [1 - inset, inset]
    centers[2] = [inset, 1 - inset]
    centers[3] = [1 - inset, 1 - inset]
    radii[0:4] = inset

    # 4-7: edge midpoints
    centers[4] = [0.5, inset]
    centers[5] = [inset, 0.5]
    centers[6] = [1 - inset, 0.5]
    centers[7] = [0.5, 1 - inset]
    radii[4:8] = inset

    # 8: center
    centers[8] = [0.5, 0.5]
    radii[8] = 0.10

    # 9-14: 6 inner ring at radius 0.23, golden-angle spiral
    r_inner = 0.23
    for k in range(6):
        angle = k * GOLDEN_ANGLE
        centers[9 + k] = [0.5 + r_inner * math.cos(angle),
                          0.5 + r_inner * math.sin(angle)]
        radii[9 + k] = 0.07

    # 15-25: 11 outer ring at radius 0.48 * 1.003 (with offset)
    r_outer = 0.48
    for k in range(11):
        angle = k * GOLDEN_ANGLE * 1.003
        cx = 0.5 + r_outer * math.cos(angle)
        cy = 0.5 + r_outer * math.sin(angle)
        # Clip to inside square
        cx = max(0.06, min(0.94, cx))
        cy = max(0.06, min(0.94, cy))
        centers[15 + k] = [cx, cy]
        radii[15 + k] = 0.06

    return np.column_stack([centers, radii])


def ring_rotate(circles: np.ndarray, ring_idx, angle: float) -> np.ndarray:
    """Rigid rotation of ring circles around center [0.5, 0.5]."""
    out = circles.copy()
    center = np.array([0.5, 0.5])
    for i in ring_idx:
        rel = out[i, :2] - center
        ca, sa = math.cos(angle), math.sin(angle)
        rotated = np.array([ca * rel[0] - sa * rel[1], sa * rel[0] + ca * rel[1]])
        out[i, :2] = center + rotated
    return out


def worker(args):
    seed, mode, n_iters = args
    import scipy.optimize as opt
    import numpy as np
    from einstein.circle_packing_square import N_CIRCLES, evaluate
    from einstein.circle_packing_square.polish import polish

    rng = np.random.default_rng(seed)
    init = shinka_init()

    if mode == "spiral_jitter":
        # Just jitter the spiral init
        init[:, :2] += rng.normal(0, 0.02, (26, 2))
    elif mode == "shinka_sa":
        # Run ShinkaEvolve-style simulated annealing
        T = 0.05
        cool = 0.995
        inner_idx = list(range(9, 15))
        outer_idx = list(range(15, 26))

        # Get initial polish
        cur = init.copy()
        for slack in (1e-3, 1e-5, 1e-7):
            try:
                cur, _ = polish(cur, method="SLSQP", ftol=1e-12, maxiter=1000, overlap_slack=slack)
            except Exception:
                break
        try:
            cur_score = evaluate({"circles": cur.tolist()}, tol=1e-9)
        except Exception:
            cur_score = -1

        best = cur.copy()
        best_score = cur_score
        stagnation = 0

        for it in range(n_iters):
            if rng.random() < 0.7:
                # local jitter
                k = rng.integers(2, 6)
                idxs = rng.choice(26, k, replace=False)
                cand = cur.copy()
                cand[idxs, :2] += rng.normal(0, 0.04, (k, 2))
            else:
                # ring rotation
                ring = inner_idx if rng.random() < 0.5 else outer_idx
                angle = float(rng.normal(0, 0.15))
                cand = ring_rotate(cur, ring, angle)

            cand[:, 0] = np.clip(cand[:, 0], cand[:, 2], 1.0 - cand[:, 2])
            cand[:, 1] = np.clip(cand[:, 1], cand[:, 2], 1.0 - cand[:, 2])

            try:
                # Quick polish
                p_cur = cand
                for slack in (1e-4, 1e-6, 1e-8, 1e-10):
                    p_cur, _ = polish(p_cur, method="SLSQP", ftol=1e-14, maxiter=600, overlap_slack=slack)
                cand_score = evaluate({"circles": p_cur.tolist()}, tol=1e-9)
            except Exception:
                continue

            delta = cand_score - cur_score
            if delta > 0 or rng.random() < math.exp(delta / max(T, 1e-12)):
                cur = p_cur
                cur_score = cand_score
                if cand_score > best_score:
                    best_score = cand_score
                    best = p_cur.copy()
                    stagnation = 0
                else:
                    stagnation += 1
            else:
                stagnation += 1

            if stagnation > 62:
                T = 0.05
                stagnation = 0
            else:
                T *= cool

        return (seed, mode, best_score, best.tolist())

    # Otherwise, just polish init
    cur = init
    best_score = -1.0
    best = None
    for slack in (1e-3, 1e-5, 1e-7, 1e-9):
        try:
            cur, _ = polish(cur, method="SLSQP", ftol=1e-14, maxiter=1500, overlap_slack=slack)
            try:
                s = evaluate({"circles": cur.tolist()}, tol=1e-9)
                if s > best_score:
                    best_score = s
                    best = cur.copy()
            except Exception:
                pass
        except Exception:
            break
    if best is None:
        return None
    return (seed, mode, best_score, best.tolist())


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--mode", choices=["spiral_jitter", "shinka_sa", "spiral_only"], default="shinka_sa")
    p.add_argument("--n-trials", type=int, default=20)
    p.add_argument("--n-iters", type=int, default=100)
    p.add_argument("--workers", type=int, default=None)
    p.add_argument("--seed-base", type=int, default=300000)
    p.add_argument("--output", type=str, default="results-temp/p14_shinka.json")
    args = p.parse_args()

    workers = args.workers or max(1, mp.cpu_count() - 1)
    print(f"Workers: {workers}, mode={args.mode}")

    # Print init
    init = shinka_init()
    print(f"Init sum_r: {init[:,2].sum():.6f}")

    tasks = [(args.seed_base + i, args.mode, args.n_iters) for i in range(args.n_trials)]

    AE = 2.6359830849176076
    t0 = time.time()
    best_score = -1.0
    best_c = None
    n_done = 0

    with mp.Pool(workers) as pool:
        for result in pool.imap_unordered(worker, tasks):
            n_done += 1
            if result is None:
                continue
            seed, mode, score, circles = result
            if score > best_score:
                best_score = score
                best_c = circles
                elapsed = time.time() - t0
                marker = " <<< above AE!" if score > AE else f" (vs AE {score-AE:+.3e})"
                print(f"  seed={seed} score={score:.16f}{marker} ({elapsed:.1f}s, {n_done}/{args.n_trials})", flush=True)

    print(f"\nFinal: best={best_score:.16f}  vs AE: {best_score-AE:+.3e}  ({time.time()-t0:.1f}s)")
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w") as f:
        json.dump({
            "best_score": best_score,
            "best_circles": best_c,
        }, f, indent=2)


if __name__ == "__main__":
    main()
