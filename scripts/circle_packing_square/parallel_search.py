"""Parallel multistart for Circle Packing in a Square (P14, n=26).

Uses multiprocessing to fan out hundreds of polishes across all CPU cores.
Each worker runs random init → SLSQP cascade → record best basin score.

The goal: find a NEW basin (not perturbation of AE) with score > 2.6359830849176076.
"""

from __future__ import annotations

import argparse
import json
import multiprocessing as mp
import os
import time
from pathlib import Path

import numpy as np


def worker(args):
    """Run one polish trial. Imports inside worker for fork safety."""
    seed, strategy, warm_circles = args
    import math
    import numpy as np
    from einstein.circle_packing_square import N_CIRCLES, evaluate
    from einstein.circle_packing_square.polish import polish

    rng = np.random.default_rng(seed)

    # ---- init ----
    if strategy == "random":
        r0 = rng.uniform(0.05, 0.10)
        out = np.zeros((N_CIRCLES, 3))
        placed = 0
        for _ in range(50000):
            cx, cy = rng.uniform(r0, 1 - r0, 2)
            ok = True
            for j in range(placed):
                if math.hypot(cx - out[j, 0], cy - out[j, 1]) < 2 * r0:
                    ok = False
                    break
            if ok:
                out[placed] = [cx, cy, r0]
                placed += 1
                if placed == N_CIRCLES:
                    break
        if placed < N_CIRCLES:
            return None
        init = out
    elif strategy == "perturb_large":
        if warm_circles is None:
            return None
        sigma = rng.uniform(0.05, 0.20)
        init = warm_circles.copy()
        init[:, :2] += rng.normal(0, sigma, (N_CIRCLES, 2))
        init[:, 2] *= rng.uniform(0.7, 1.3, N_CIRCLES)
        init[:, 2] = np.clip(init[:, 2], 1e-3, 0.4)
        init[:, 0] = np.clip(init[:, 0], init[:, 2], 1.0 - init[:, 2])
        init[:, 1] = np.clip(init[:, 1], init[:, 2], 1.0 - init[:, 2])
    elif strategy == "shuffle":
        if warm_circles is None:
            return None
        # Permute circle positions but keep radii
        idx = rng.permutation(N_CIRCLES)
        init = warm_circles.copy()
        init[:, :2] = init[idx, :2]
        init[:, :2] += rng.normal(0, 0.01, (N_CIRCLES, 2))
    elif strategy == "kick":
        # Move a few specific circles to new random positions
        if warm_circles is None:
            return None
        init = warm_circles.copy()
        n_kick = int(rng.integers(2, 8))
        kick_idx = rng.choice(N_CIRCLES, n_kick, replace=False)
        for k in kick_idx:
            init[k, 0] = rng.uniform(0.1, 0.9)
            init[k, 1] = rng.uniform(0.1, 0.9)
            init[k, 2] = rng.uniform(0.04, 0.12)
    else:
        return None

    # ---- polish cascade — verify feasibility at strict 1e-9 every step ----
    # We track the best STRICT-1e-9-feasible result. Any score gain from
    # looser slack is rejected unless it survives the strict check.
    best_score = -1.0
    best_c = None
    cur = init
    for slack in (1e-4, 1e-6, 1e-8, 1e-10, 1e-12):
        try:
            new, _ = polish(cur, method="SLSQP", ftol=1e-16, maxiter=1500, overlap_slack=slack)
            # Always re-verify under strict 1e-9 tolerance (matches arena ceiling)
            try:
                s = evaluate({"circles": new.tolist()}, tol=1e-9)
                if s > best_score:
                    best_score = s
                    best_c = new.copy()
                cur = new
            except AssertionError:
                # This polish step produced something infeasible — drop it
                # but allow the next step to try refining `cur` (the last good)
                pass
        except Exception:
            break
    if best_c is None:
        return None
    return (seed, strategy, best_score, best_c.tolist())


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--n-trials", type=int, default=200)
    p.add_argument("--strategy", choices=["random", "perturb_large", "kick", "shuffle", "mixed"], default="mixed")
    p.add_argument("--warm", type=str, default="results-temp/p14_top.json")
    p.add_argument("--workers", type=int, default=None)
    p.add_argument("--seed-base", type=int, default=0)
    p.add_argument("--output", type=str, default="results-temp/p14_parallel.json")
    args = p.parse_args()

    workers = args.workers or max(1, mp.cpu_count() - 1)
    print(f"Workers: {workers}")

    warm: np.ndarray | None = None
    if args.warm and Path(args.warm).exists():
        with open(args.warm) as f:
            data = json.load(f)
        if isinstance(data, list) and data:
            warm = np.array(data[0]["data"]["circles"], dtype=np.float64)
        elif isinstance(data, dict) and "best_circles" in data and data["best_circles"]:
            warm = np.array(data["best_circles"], dtype=np.float64)
        elif isinstance(data, dict) and "circles" in data:
            warm = np.array(data["circles"], dtype=np.float64)
        if warm is not None:
            print(f"Loaded warm seed: sum_r={warm[:,2].sum():.13f}")

    strategies = ["random", "perturb_large", "kick", "shuffle"] if args.strategy == "mixed" else [args.strategy]
    tasks = []
    for i in range(args.n_trials):
        s = strategies[i % len(strategies)]
        seed = args.seed_base + i
        tasks.append((seed, s, warm))

    t0 = time.time()
    best_score = 0.0
    best_circles = None
    best_strategy = None
    history = []
    n_done = 0
    n_failed = 0

    with mp.Pool(workers) as pool:
        for result in pool.imap_unordered(worker, tasks):
            n_done += 1
            if result is None:
                n_failed += 1
                continue
            seed, strat, score, circles = result
            if score > best_score:
                best_score = score
                best_circles = circles
                best_strategy = strat
                history.append({"trial": seed, "strategy": strat, "score": score})
                elapsed = time.time() - t0
                print(f"  [{strat:14s}] seed={seed:5d} NEW BEST {score:.16f}  ({elapsed:.1f}s, {n_done}/{args.n_trials})", flush=True)
            elif n_done % 50 == 0:
                elapsed = time.time() - t0
                print(f"  ...{n_done}/{args.n_trials} done, best={best_score:.16f}, fail={n_failed}, {elapsed:.1f}s", flush=True)

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w") as f:
        json.dump({
            "n_trials": args.n_trials,
            "best_score": best_score,
            "best_strategy": best_strategy,
            "best_circles": best_circles,
            "history": history,
        }, f, indent=2)
    print(f"\nFinal: best={best_score:.16f}  strategy={best_strategy}  ({time.time()-t0:.1f}s, fail={n_failed}/{args.n_trials})")
    print(f"Output: {args.output}")


if __name__ == "__main__":
    main()
