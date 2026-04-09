"""Topology mutation search for Circle Packing in a Square (P14, n=26).

Strategy: at a fully-rigid local maximum (78 active constraints, 78 vars),
the score is determined by the contact graph. To find a better basin, we
systematically mutate the contact graph:

  - swap_one: drop 1 active edge, add 1 inactive edge, re-polish
  - swap_two: drop 2 active edges, add 2 inactive edges, re-polish
  - swap_wall: change which circles touch which walls

For each mutated topology, perturb circles slightly and re-polish. If the
result satisfies all constraints AND has higher Σr than AE, we have a new
basin.
"""

from __future__ import annotations

import argparse
import json
import multiprocessing as mp
import time
from pathlib import Path

import numpy as np


def worker(args):
    seed, base_circles, edge_to_drop, edge_to_add, sigma = args
    import math
    import numpy as np
    from einstein.circle_packing_square import N_CIRCLES, evaluate
    from einstein.circle_packing_square.polish import polish

    rng = np.random.default_rng(seed)
    base = np.array(base_circles, dtype=np.float64)

    # Apply the mutation: pull edge_to_drop apart and push edge_to_add together
    init = base.copy()
    if edge_to_drop is not None:
        i, j = edge_to_drop
        # Push these two circles apart by sigma in their connecting direction
        d = init[j, :2] - init[i, :2]
        n = np.linalg.norm(d)
        if n > 1e-6:
            init[i, :2] -= d / n * sigma * 0.5
            init[j, :2] += d / n * sigma * 0.5
    if edge_to_add is not None:
        i, j = edge_to_add
        # Pull together
        d = init[j, :2] - init[i, :2]
        n = np.linalg.norm(d)
        if n > 1e-6:
            init[i, :2] += d / n * sigma * 0.5
            init[j, :2] -= d / n * sigma * 0.5

    # Add overall jitter
    init[:, :2] += rng.normal(0, sigma * 0.3, (N_CIRCLES, 2))
    init[:, 2] *= rng.uniform(0.97, 1.03, N_CIRCLES)
    init[:, 0] = np.clip(init[:, 0], init[:, 2], 1.0 - init[:, 2])
    init[:, 1] = np.clip(init[:, 1], init[:, 2], 1.0 - init[:, 2])

    # Verified cascade
    best_score = -1.0
    best_c = None
    cur = init
    for slack in (1e-4, 1e-6, 1e-8, 1e-10, 1e-12):
        try:
            new, _ = polish(cur, method="SLSQP", ftol=1e-16, maxiter=2000, overlap_slack=slack)
            try:
                s = evaluate({"circles": new.tolist()}, tol=1e-9)
                if s > best_score:
                    best_score = s
                    best_c = new.copy()
                cur = new
            except AssertionError:
                pass
        except Exception:
            break
    if best_c is None:
        return None
    return (seed, best_score, best_c.tolist())


def get_active_pairs(circles, eps=1e-7):
    n = len(circles)
    active = []
    for i in range(n):
        for j in range(i + 1, n):
            d = np.hypot(circles[i, 0] - circles[j, 0], circles[i, 1] - circles[j, 1])
            if abs(d - circles[i, 2] - circles[j, 2]) < eps:
                active.append((i, j))
    return active


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--base", type=str, default="results-temp/p14_top.json",
                   help="warm-start solution(s) JSON")
    p.add_argument("--n-trials", type=int, default=400)
    p.add_argument("--workers", type=int, default=None)
    p.add_argument("--sigma", type=float, default=0.02)
    p.add_argument("--seed-base", type=int, default=10000)
    p.add_argument("--output", type=str, default="results-temp/p14_topology.json")
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

    active = get_active_pairs(base, eps=1e-7)
    print(f"Active pair contacts: {len(active)}")

    # Generate mutation tasks
    rng = np.random.default_rng(args.seed_base)
    n = len(base)
    all_pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    inactive = [p for p in all_pairs if p not in set(active)]

    tasks = []
    for trial in range(args.n_trials):
        # Random pick: drop one active, add one inactive
        e_drop = active[int(rng.integers(0, len(active)))] if rng.random() < 0.7 else None
        e_add = inactive[int(rng.integers(0, len(inactive)))] if rng.random() < 0.7 else None
        sigma = args.sigma * float(rng.uniform(0.5, 2.0))
        tasks.append((args.seed_base + trial, base.tolist(), e_drop, e_add, sigma))

    t0 = time.time()
    best_score = base[:, 2].sum()
    best_circles = base.tolist()
    history = []
    n_done = 0
    n_failed = 0

    AE = 2.6359830849176076

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
                history.append({"trial": seed, "score": score})
                elapsed = time.time() - t0
                marker = " <<< above AE!" if score > AE + 1e-12 else ""
                print(f"  seed={seed:5d} NEW BEST {score:.16f}  d_AE={score-AE:+.2e}  ({elapsed:.1f}s){marker}", flush=True)
            elif n_done % 50 == 0:
                elapsed = time.time() - t0
                print(f"  ...{n_done}/{args.n_trials}, best={best_score:.16f}, fail={n_failed}, {elapsed:.1f}s", flush=True)

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w") as f:
        json.dump({
            "n_trials": args.n_trials,
            "best_score": best_score,
            "best_circles": best_circles,
            "history": history,
        }, f, indent=2)
    print(f"\nFinal: best={best_score:.16f}  ({time.time()-t0:.1f}s, fail={n_failed}/{args.n_trials})")


if __name__ == "__main__":
    main()
