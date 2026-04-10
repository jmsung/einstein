"""Basin-hopping search from AlphaEvolve/CHRONOS SOTA.

Strategies:
    1. Large random perturbation (sigma 0.1 - 0.3) + SLSQP polish
    2. Teleport single point to a random location + SLSQP polish
    3. Remove point, re-optimize 10 points, add point at largest gap
    4. Topology move: swap active triple by exchanging 2 nearby points
    5. Symmetry break: force different boundary-incidence pattern
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from einstein.heilbronn_triangles import arena_score, active_triples  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from multistart_search import (  # noqa: E402
    N, SQRT3, CENTROID, slsqp_polish, project_into_triangle,
    init_random_uniform,
)

CHRONOS_PATH = Path("results/problem-15-heilbronn-triangles/rank01_CHRONOS_0.0365298898800302.json")
TARGET = 0.036529889880030156


def load_ae():
    return np.array(json.loads(CHRONOS_PATH.read_text())["data"]["points"], dtype=np.float64)


def hop_perturb(x, rng, sigma):
    return (x + sigma * rng.standard_normal(x.shape)).flatten()


def hop_teleport_one(x_flat, rng):
    pts = x_flat.reshape(N, 2).copy()
    i = rng.integers(0, N)
    while True:
        nx = rng.uniform(0, 1)
        ny = rng.uniform(0, SQRT3 / 2)
        if ny <= SQRT3 * nx and ny <= SQRT3 * (1 - nx):
            break
    pts[i] = [nx, ny]
    return pts.flatten()


def hop_teleport_k(x_flat, rng, k):
    pts = x_flat.reshape(N, 2).copy()
    idx = rng.choice(N, k, replace=False)
    for i in idx:
        while True:
            nx = rng.uniform(0, 1)
            ny = rng.uniform(0, SQRT3 / 2)
            if ny <= SQRT3 * nx and ny <= SQRT3 * (1 - nx):
                break
        pts[i] = [nx, ny]
    return pts.flatten()


def hop_swap_nearest(x_flat, rng):
    pts = x_flat.reshape(N, 2).copy()
    # Pick a point, move it toward a random interior spot
    i = rng.integers(0, N)
    target = np.array([rng.uniform(0.2, 0.8), rng.uniform(0.1, 0.6)])
    pts[i] = 0.5 * pts[i] + 0.5 * target
    return pts.flatten()


def hop_boundary_swap(x_flat, rng):
    """Take an interior point and push it to a random edge; or take
    an edge point and pull it inward."""
    pts = x_flat.reshape(N, 2).copy()
    # Find which points are on edges
    x = pts[:, 0]
    y = pts[:, 1]
    on_bot = y < 1e-9
    on_left = abs(y - SQRT3 * x) < 1e-9
    on_right = abs(y - SQRT3 * (1 - x)) < 1e-9
    interior = ~(on_bot | on_left | on_right)
    interior_idx = np.where(interior)[0]
    if len(interior_idx) == 0 or rng.random() < 0.5:
        # Pull an edge point inward
        edge_idx = np.where(~interior)[0]
        if len(edge_idx) == 0:
            return x_flat
        i = rng.choice(edge_idx)
        pts[i] = pts[i] + 0.05 * rng.standard_normal(2)
        pts[i, 1] = max(pts[i, 1], 0.02)
    else:
        # Push an interior point to edge
        i = rng.choice(interior_idx)
        edge_pick = rng.integers(0, 3)
        t = rng.uniform(0.1, 0.9)
        if edge_pick == 0:
            pts[i] = [t, 0.02]
        elif edge_pick == 1:
            pts[i] = [t * 0.5 + 0.02, t * SQRT3 / 2 - 0.035]
        else:
            pts[i] = [1 - t * 0.5 - 0.02, t * SQRT3 / 2 - 0.035]
    return pts.flatten()


HOPS = {
    "small_perturb": lambda x, rng: hop_perturb(x, rng, sigma=0.03),
    "mid_perturb": lambda x, rng: hop_perturb(x, rng, sigma=0.1),
    "large_perturb": lambda x, rng: hop_perturb(x, rng, sigma=0.2),
    "teleport_1": lambda x, rng: hop_teleport_one(x, rng),
    "teleport_2": lambda x, rng: hop_teleport_k(x, rng, 2),
    "teleport_3": lambda x, rng: hop_teleport_k(x, rng, 3),
    "swap_nearest": hop_swap_nearest,
    "boundary_swap": hop_boundary_swap,
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--time", type=float, default=300.0)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--save-threshold", type=float, default=TARGET + 1e-10)
    args = ap.parse_args()

    ae = load_ae()
    ae_score = arena_score(ae)
    print(f"AE/CHRONOS start score: {ae_score}")
    ae_flat = ae.flatten()

    rng = np.random.default_rng(args.seed)
    t0 = time.time()
    best_score = ae_score
    best_pts = ae.copy()
    trial = 0
    by_hop = {k: {"trials": 0, "best": -float("inf")} for k in HOPS}

    while time.time() - t0 < args.time:
        for hop_name, hop_fn in HOPS.items():
            if time.time() - t0 > args.time:
                break
            x_pert = hop_fn(ae_flat.copy(), rng)
            try:
                pts, s = slsqp_polish(x_pert)
            except Exception:
                continue
            trial += 1
            by_hop[hop_name]["trials"] += 1
            if s > by_hop[hop_name]["best"]:
                by_hop[hop_name]["best"] = s
            marker = ""
            if s > best_score + 1e-13:
                best_score = s
                best_pts = pts
                marker = " ★"
            if trial % 10 == 0 or marker:
                print(f"[{time.time() - t0:6.1f}s] t{trial:4d} {hop_name:15s} "
                      f"s={s:.17g}  Δ={s-ae_score:+.3e}{marker}",
                      flush=True)

    print(f"\n=== Basin hopping summary ===")
    print(f"Start: {ae_score}")
    print(f"Best:  {best_score!r}  (Δ={best_score - ae_score:+.3e})")
    print("\nPer-hop bests:")
    for k, v in sorted(by_hop.items(), key=lambda kv: -kv[1]["best"]):
        print(f"  {k:15s}  trials={v['trials']:4d}  best={v['best']:.17g}")

    if best_score > args.save_threshold:
        fn = Path("results/problem-15-heilbronn-triangles") / f"basinhop_{best_score:.15g}.json"
        fn.write_text(json.dumps({"points": best_pts.tolist()}, indent=2))
        print(f"\nSaved to {fn}")


if __name__ == "__main__":
    main()
