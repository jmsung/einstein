"""Diverse initialization strategies for circle packing in square (n=26).

The perturbation strategy stays in AlphaEvolve's basin. To find a NEW basin,
we need fundamentally different starting topologies. This script generates
diverse seed configurations from:

  - hex lattice (5 rows x 6 cols, drop 4)
  - square lattice (5 x 6, drop 4)
  - brick lattice (offset rows)
  - random with various seed densities
  - shrinking simulation (start large, shrink until non-overlapping)
  - jittered AlphaEvolve with 2-circle topology swaps

Each seed is polished via SLSQP cascade and the best is reported.
"""

from __future__ import annotations

import argparse
import json
import math
import time
from pathlib import Path

import numpy as np

from einstein.circle_packing_square import N_CIRCLES, evaluate, evaluate_strict
from einstein.circle_packing_square.polish import polish
from einstein.circle_packing_square.active_set import newton_polish, identify_active


# ----- initialization strategies -----

def init_hex(rng, jitter: float = 0.005) -> np.ndarray:
    """5-row hexagonal: 6+5+6+5+6 = 28, drop 2 corners."""
    rows = [(0, 6), (1, 5), (0, 6), (1, 5), (0, 6)]
    pts = []
    n_rows = 5
    h = 1.0 / (n_rows + 0.2)
    for r_idx, (off, ncols) in enumerate(rows):
        y = h * (r_idx + 0.6)
        for c in range(ncols):
            if off:
                x = (c + 1.0) / 6.0
            else:
                x = (c + 0.5) / 6.0
            pts.append([x, y])
    pts = pts[:N_CIRCLES]
    pts = np.array(pts)
    pts += rng.normal(0, jitter, pts.shape)
    radii = np.full(N_CIRCLES, 0.07)
    return np.column_stack([pts, radii])


def init_grid(rng, rows: int = 5, cols: int = 6, jitter: float = 0.005) -> np.ndarray:
    """rows x cols grid (truncated to N_CIRCLES)."""
    n = rows * cols
    pts = []
    for i in range(rows):
        for j in range(cols):
            x = (j + 0.5) / cols
            y = (i + 0.5) / rows
            pts.append([x, y])
    pts = pts[:N_CIRCLES]
    pts = np.array(pts)
    pts += rng.normal(0, jitter, pts.shape)
    radii = np.full(N_CIRCLES, min(0.5/cols, 0.5/rows) * 0.9)
    return np.column_stack([pts, radii])


def init_brick(rng, jitter: float = 0.005) -> np.ndarray:
    """Offset brick rows (5x5 + 1 extra)."""
    pts = []
    rows = 5
    cols = 5
    h = 1.0 / rows
    w = 1.0 / cols
    for i in range(rows):
        for j in range(cols):
            x = (j + 0.5) / cols + (h * 0.5 if i % 2 else 0)
            x = x % 1.0
            y = (i + 0.5) / rows
            pts.append([x, y])
    # 1 extra in the centre
    pts.append([0.5, 0.5])
    pts = np.array(pts[:N_CIRCLES])
    pts += rng.normal(0, jitter, pts.shape)
    radii = np.full(N_CIRCLES, 0.08)
    return np.column_stack([pts, radii])


def init_random_dense(rng, max_attempts: int = 50000, r_init: float | None = None) -> np.ndarray:
    """Greedy random non-overlapping placement, decreasing r_init on retry."""
    if r_init is None:
        r_init = rng.uniform(0.04, 0.10)
    out = np.zeros((N_CIRCLES, 3))
    placed = 0
    attempts = 0
    while placed < N_CIRCLES and attempts < max_attempts:
        cx, cy = rng.uniform(r_init, 1 - r_init, 2)
        ok = True
        for j in range(placed):
            d = math.hypot(cx - out[j, 0], cy - out[j, 1])
            if d < 2 * r_init:
                ok = False
                break
        if ok:
            out[placed] = [cx, cy, r_init]
            placed += 1
        attempts += 1
    if placed < N_CIRCLES:
        return init_random_dense(rng, max_attempts, r_init * 0.9)
    return out


def init_shrink(rng, n_iter: int = 200) -> np.ndarray:
    """Soft-disk simulation: random init, repulsion + boundary, then shrink."""
    pts = rng.uniform(0.05, 0.95, (N_CIRCLES, 2))
    r = np.full(N_CIRCLES, 0.05)
    dt = 0.01
    for _ in range(n_iter):
        forces = np.zeros((N_CIRCLES, 2))
        for i in range(N_CIRCLES):
            for j in range(i + 1, N_CIRCLES):
                dx = pts[i] - pts[j]
                d = np.linalg.norm(dx)
                target = r[i] + r[j]
                if d < target * 1.05:
                    push = (target - d) / max(d, 1e-6)
                    forces[i] += dx * push * 0.5
                    forces[j] -= dx * push * 0.5
            # walls
            for k in range(2):
                if pts[i, k] - r[i] < 0:
                    forces[i, k] += (r[i] - pts[i, k]) * 1.0
                if pts[i, k] + r[i] > 1:
                    forces[i, k] -= (pts[i, k] + r[i] - 1) * 1.0
        pts += forces * dt
        np.clip(pts, 0.01, 0.99, out=pts)
    return np.column_stack([pts, r])


def init_topo_swap(rng, base: np.ndarray, n_swaps: int = 2) -> np.ndarray:
    """Take base solution, swap n_swaps random circle positions, then jitter."""
    out = base.copy()
    for _ in range(n_swaps):
        i, j = rng.choice(N_CIRCLES, 2, replace=False)
        # swap centres but keep radii
        out[i, :2], out[j, :2] = out[j, :2].copy(), out[i, :2].copy()
    out[:, :2] += rng.normal(0, 0.02, (N_CIRCLES, 2))
    out[:, 2] *= rng.uniform(0.9, 1.1, N_CIRCLES)
    out[:, 2] = np.clip(out[:, 2], 0.01, 0.4)
    return out


# ----- polish with cascade -----

def cascade_polish(circles: np.ndarray) -> tuple[np.ndarray, float] | None:
    """SLSQP slack cascade then Newton refinement."""
    try:
        c, info = polish(circles, method="SLSQP", ftol=1e-16, maxiter=1500, overlap_slack=1e-5)
        c, info = polish(c, method="SLSQP", ftol=1e-16, maxiter=1500, overlap_slack=1e-7)
        c, info = polish(c, method="SLSQP", ftol=1e-16, maxiter=2000, overlap_slack=1e-9)
        c, info = polish(c, method="SLSQP", ftol=1e-16, maxiter=2000, overlap_slack=1e-12)
        # Newton on active set for machine precision
        active = identify_active(c, eps=1e-7)
        n_act = sum(len(v) if isinstance(v, list) else 0 for k, v in active.items() if k != "pairs") + len(active["pairs"])
        if n_act >= 3 * N_CIRCLES - 4:  # near-rigid
            c, info = newton_polish(c, active=active, max_iter=20, tol=1e-15)
        # Verify strict
        score = evaluate({"circles": c.tolist()}, tol=1e-12)
        return c, score
    except Exception:
        return None


# ----- main -----

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--n-trials", type=int, default=100)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--warm", type=str, default=None)
    p.add_argument("--output", type=str, default="results-temp/p14_diverse.json")
    args = p.parse_args()

    rng = np.random.default_rng(args.seed)
    base_seeds: list[np.ndarray] = []
    if args.warm:
        with open(args.warm) as f:
            data = json.load(f)
        if isinstance(data, list):
            for entry in data:
                d = entry.get("data", entry)
                if "circles" in d:
                    base_seeds.append(np.array(d["circles"], dtype=np.float64))
        elif isinstance(data, dict) and "circles" in data:
            base_seeds.append(np.array(data["circles"], dtype=np.float64))

    strategies = ["hex", "grid", "brick", "random", "shrink", "topo_swap"]

    results = []
    best_score = 0.0
    best_circles = None
    best_strategy = None
    t0 = time.time()
    for trial in range(args.n_trials):
        strat = strategies[trial % len(strategies)]
        try:
            if strat == "hex":
                init = init_hex(rng, jitter=rng.uniform(0.001, 0.02))
            elif strat == "grid":
                rows, cols = rng.choice([(5, 6), (6, 5), (5, 5)])  # type: ignore
                init = init_grid(rng, rows=int(rows), cols=int(cols))
            elif strat == "brick":
                init = init_brick(rng)
            elif strat == "random":
                init = init_random_dense(rng)
            elif strat == "shrink":
                init = init_shrink(rng)
            elif strat == "topo_swap":
                if not base_seeds:
                    init = init_random_dense(rng)
                else:
                    base = base_seeds[trial % len(base_seeds)]
                    init = init_topo_swap(rng, base, n_swaps=int(rng.integers(1, 5)))
            else:
                continue
        except Exception:
            continue

        out = cascade_polish(init)
        if out is None:
            continue
        circles, score = out
        if score > best_score:
            best_score = score
            best_circles = circles
            best_strategy = strat
            results.append({
                "trial": trial, "strategy": strat,
                "score": score, "circles": circles.tolist(),
            })
            elapsed = time.time() - t0
            print(f"  [{strat:10s}] trial {trial:4d} NEW BEST {score:.16f}  ({elapsed:.1f}s)", flush=True)

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w") as f:
        json.dump({
            "n_trials": args.n_trials,
            "seed": args.seed,
            "best_score": best_score,
            "best_strategy": best_strategy,
            "best_circles": best_circles.tolist() if best_circles is not None else None,
            "history": results,
        }, f, indent=2)
    print(f"\nFinal: best={best_score:.16f}  strategy={best_strategy}  ({time.time()-t0:.1f}s)")


if __name__ == "__main__":
    main()
