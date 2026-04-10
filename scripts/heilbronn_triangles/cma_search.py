"""CMA-ES search for Heilbronn Triangles (n=11) basins.

Evolution-strategy search on random initial layouts, polished via SLSQP.
CMA-ES is much better at escaping shallow local minima than gradient methods,
so this tests whether there's a qualitatively different basin we're missing.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import sys
import time
from pathlib import Path

import cma
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from einstein.heilbronn_triangles import arena_score  # noqa: E402

# Import helpers from the multistart_search module
sys.path.insert(0, str(Path(__file__).resolve().parent))
from multistart_search import (  # noqa: E402
    N, SQRT3, TRIPLES, CENTROID,
    slsqp_polish, project_into_triangle, init_random_uniform,
)


def soft_score(x, beta=5000.0):
    """Smooth score for CMA-ES: softmin * (-1 for minimize)."""
    pts = x.reshape(N, 2)
    # Containment penalty (strong)
    y = pts[:, 1]
    px = pts[:, 0]
    pen = 0.0
    v1 = np.minimum(y, 0)
    v2 = np.minimum(SQRT3 * px - y, 0)
    v3 = np.minimum(SQRT3 * (1 - px) - y, 0)
    pen = 1e4 * (np.sum(v1**2) + np.sum(v2**2) + np.sum(v3**2))
    # Softmin
    i = TRIPLES[:, 0]
    j = TRIPLES[:, 1]
    k = TRIPLES[:, 2]
    p1 = pts[i]; p2 = pts[j]; p3 = pts[k]
    cross = (
        p1[:, 0] * (p2[:, 1] - p3[:, 1])
        + p2[:, 0] * (p3[:, 1] - p1[:, 1])
        + p3[:, 0] * (p1[:, 1] - p2[:, 1])
    )
    areas = 0.5 * np.abs(cross)
    a_min = areas.min()
    if a_min <= 0:
        return -1e6 * a_min + pen  # heavy penalty
    shifted = np.clip(-beta * (areas - a_min), -50, 50)
    sm = a_min - np.log(np.exp(shifted).sum()) / beta
    return -sm + pen


def cma_run(x0, sigma0, maxiter=200, beta=5000):
    es = cma.CMAEvolutionStrategy(
        x0, sigma0,
        {"maxiter": maxiter, "verbose": -9, "popsize": 30, "tolx": 1e-10,
         "tolfun": 1e-12},
    )
    while not es.stop():
        X = es.ask()
        F = [soft_score(np.asarray(x), beta=beta) for x in X]
        es.tell(X, F)
    return np.asarray(es.result.xbest)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--time", type=float, default=300.0)
    ap.add_argument("--sigma0", type=float, default=0.1)
    ap.add_argument("--maxiter", type=int, default=100)
    ap.add_argument("--seed-start", type=int, default=0)
    args = ap.parse_args()

    t0 = time.time()
    best_score = -float("inf")
    best_pts = None
    trial = 0
    seed = args.seed_start

    while time.time() - t0 < args.time:
        # Choose init strategy
        strat = trial % 4
        if strat == 0:
            x0 = init_random_uniform(seed + trial)
        elif strat == 1:
            chr_path = Path("results/problem-15-heilbronn-triangles/rank01_CHRONOS_0.0365298898800302.json")
            pts = np.array(json.loads(chr_path.read_text())["data"]["points"])
            x0 = pts.flatten() + 0.15 * np.random.default_rng(seed + trial).standard_normal(22)
        elif strat == 2:
            # D3 symmetric: 3+3+3+1 = 10, add 1 extra at centroid offset -> 11
            rng = np.random.default_rng(seed + trial)
            pts = [list(CENTROID)]
            r1 = 0.2
            for k in range(3):
                a = k * 2 * math.pi / 3 + rng.uniform(0, 0.1)
                pts.append([CENTROID[0] + r1 * math.cos(a),
                            CENTROID[1] + r1 * math.sin(a)])
            r2 = 0.4
            for k in range(3):
                a = k * 2 * math.pi / 3 + rng.uniform(0, 0.1) + math.pi / 3
                pts.append([CENTROID[0] + r2 * math.cos(a),
                            CENTROID[1] + r2 * math.sin(a)])
            for k in range(3):
                a = k * 2 * math.pi / 3 + rng.uniform(0, 0.1)
                r = 0.3
                pts.append([CENTROID[0] + r * math.cos(a),
                            CENTROID[1] + r * math.sin(a)])
            # Extra point to get 11
            pts.append([CENTROID[0] + 0.02 * rng.uniform(-1, 1),
                        CENTROID[1] + 0.02 * rng.uniform(-1, 1)])
            x0 = np.array(pts).flatten()
        else:
            # Large random perturbation
            rng = np.random.default_rng(seed + trial)
            x0 = rng.uniform(0.1, 0.9, 22)

        if x0.size != 22:
            trial += 1
            continue
        x0 = project_into_triangle(x0, eps=1e-4)
        try:
            x_cma = cma_run(x0, sigma0=args.sigma0, maxiter=args.maxiter, beta=2000)
        except Exception as e:
            print(f"CMA-ES failed: {e}")
            trial += 1
            continue
        # Polish with SLSQP
        pts, s = slsqp_polish(x_cma)
        trial += 1
        marker = ""
        if s > best_score:
            best_score = s
            best_pts = pts
            marker = " ★"
        print(f"[{time.time()-t0:6.1f}s] cma-t{trial:3d} strat={strat} s={s:.17g}{marker}",
              flush=True)

    print(f"\nCMA-ES best: {best_score!r}")
    print(f"Delta to CHRONOS: {best_score - 0.036529889880030156:.3e}")

    if best_pts is not None and best_score > 0.036529889880029:
        fn = Path("results/problem-15-heilbronn-triangles") / f"cma_best_{best_score:.15g}.json"
        fn.write_text(json.dumps({"points": best_pts.tolist()}, indent=2))
        print(f"Saved to {fn}")


if __name__ == "__main__":
    main()
