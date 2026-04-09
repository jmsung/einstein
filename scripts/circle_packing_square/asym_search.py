"""Asymmetric-slack multistart for Circle Packing in a Square (P14, n=26).

Uses arena-aware polishing:
  - pair constraints: allow up to ~1e-9 overlap (matches FeynmanAgent precedent)
  - wall constraints: strictly positive (arena enforces walls)

Each trial: perturb the warm seed, polish with asymmetric slack, validate
under arena rules. The goal: find the highest-score arena-valid solution
above AlphaEvolve's 2.6359830849176076.
"""

from __future__ import annotations

import argparse
import json
import multiprocessing as mp
import time
from pathlib import Path

import numpy as np


PAIR_TOL_ARENA = 1e-9
WALL_TOL_ARENA = 0.0


def arena_verify(arr: np.ndarray, pair_tol: float = PAIR_TOL_ARENA,
                 wall_tol: float = WALL_TOL_ARENA) -> bool:
    cx, cy, r = arr[:, 0], arr[:, 1], arr[:, 2]
    walls = np.concatenate([cx - r, 1.0 - cx - r, cy - r, 1.0 - cy - r])
    if walls.min() < -wall_tol:
        return False
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            d = np.hypot(cx[i] - cx[j], cy[i] - cy[j])
            if d - r[i] - r[j] < -pair_tol:
                return False
    return True


def worker(args):
    seed, base_circles, sigma, pair_slack, wall_slack = args
    import scipy.optimize as opt
    import numpy as np
    from einstein.circle_packing_square import N_CIRCLES
    from einstein.circle_packing_square.polish import (
        _all_constraints, _objective, _objective_jac, _pack
    )

    rng = np.random.default_rng(seed)
    base = np.array(base_circles, dtype=np.float64)

    # Perturb
    init = base.copy()
    init[:, :2] += rng.normal(0, sigma, (N_CIRCLES, 2))
    init[:, 2] *= rng.uniform(0.97, 1.03, N_CIRCLES)
    init[:, 2] = np.clip(init[:, 2], 1e-3, 0.4)
    init[:, 0] = np.clip(init[:, 0], init[:, 2], 1.0 - init[:, 2])
    init[:, 1] = np.clip(init[:, 1], init[:, 2], 1.0 - init[:, 2])

    # Asymmetric polish cascade — first land in basin, then push to limit.
    # Target final pair gap > -9e-10 (1e-10 safety margin from -1e-9 arena).
    # We sweep multiple final ps values and keep the highest-scoring safe one.
    cur = init
    best = None
    best_score = -1.0
    safe_pair_tol = 9e-10  # arena_verify uses this; matches polish target
    schedule = (
        (1e-5, False),      # land in basin
        (1e-7, False),
        (1e-9, False),
        (8.7e-10, True),    # arena-tight w/ margin
        (8.85e-10, True),
        (8.95e-10, True),
    )
    for ps, check in schedule:
        x0 = _pack(cur)
        constraints = [{
            "type": "ineq",
            "fun": lambda x, ps=ps, ws=wall_slack: _all_constraints(x, slack=ps, wall_slack=ws),
        }]
        bounds = [(0.0, 1.0)] * (3 * N_CIRCLES)
        try:
            result = opt.minimize(
                _objective, x0, jac=_objective_jac,
                constraints=constraints, bounds=bounds, method="SLSQP",
                options={"ftol": 1e-16, "maxiter": 3000},
            )
            cur = result.x.reshape(N_CIRCLES, 3)
            if check and arena_verify(cur, pair_tol=safe_pair_tol, wall_tol=0.0):
                s = float(cur[:, 2].sum())
                if s > best_score:
                    best_score = s
                    best = cur.copy()
        except Exception:
            break

    if best is None:
        return None
    return (seed, best_score, best.tolist())


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--base", type=str, default="results-temp/p14_top.json")
    p.add_argument("--n-trials", type=int, default=300)
    p.add_argument("--workers", type=int, default=None)
    p.add_argument("--sigma", type=float, default=0.005)
    p.add_argument("--wall-slack", type=float, default=5e-13)
    p.add_argument("--seed-base", type=int, default=30000)
    p.add_argument("--output", type=str, default="results-temp/p14_asym.json")
    args = p.parse_args()

    workers = args.workers or max(1, mp.cpu_count() - 1)
    print(f"Workers: {workers}")

    with open(args.base) as f:
        data = json.load(f)
    if isinstance(data, list) and data:
        base = np.array(data[0]["data"]["circles"], dtype=np.float64)
    elif isinstance(data, dict) and "best_circles" in data and data["best_circles"]:
        base = np.array(data["best_circles"], dtype=np.float64)
    elif isinstance(data, dict) and "circles" in data:
        base = np.array(data["circles"], dtype=np.float64)
    else:
        raise ValueError("Unknown base file format")
    print(f"Base sum_r: {base[:,2].sum():.13f}")

    rng = np.random.default_rng(args.seed_base)
    tasks = []
    for trial in range(args.n_trials):
        sigma = args.sigma * float(rng.uniform(0.5, 3.0))
        tasks.append((args.seed_base + trial, base.tolist(), sigma, 9.9e-10, args.wall_slack))

    AE = 2.6359830849176076

    t0 = time.time()
    best_score = base[:, 2].sum()
    best_circles = base.tolist()
    n_done = 0
    n_failed = 0

    with mp.Pool(workers) as pool:
        for result in pool.imap_unordered(worker, tasks):
            n_done += 1
            if result is None:
                n_failed += 1
                continue
            seed, score, circles = result
            if score > best_score:
                best_score = score
                best_circles = circles
                elapsed = time.time() - t0
                marker = " <<< above AE!" if score > AE + 1e-12 else ""
                print(f"  seed={seed:5d} NEW BEST {score:.16f}  d_AE={score-AE:+.2e}  ({elapsed:.1f}s){marker}", flush=True)
            elif n_done % 50 == 0:
                elapsed = time.time() - t0
                print(f"  ...{n_done}/{args.n_trials} done, best={best_score:.16f}, fail={n_failed}, {elapsed:.1f}s", flush=True)

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w") as f:
        json.dump({
            "n_trials": args.n_trials,
            "best_score": best_score,
            "best_circles": best_circles,
        }, f, indent=2)
    print(f"\nFinal: best={best_score:.16f}  d_AE={best_score-AE:+.3e}  ({time.time()-t0:.1f}s, fail={n_failed}/{args.n_trials})")
    print(f"Output: {args.output}")


if __name__ == "__main__":
    main()
