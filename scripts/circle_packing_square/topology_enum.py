"""Single-edge topology enumeration for Circle Packing in Square (n=26).

For each (active_edge, inactive_pair) candidate, drop the active edge
and add the inactive pair as a new constraint. Solve the resulting
78-equation system via Newton starting from a small perturbation of
the base configuration. Keep any solution that:
  - converges (residual < 1e-12)
  - is feasible (all constraints satisfied at arena tol)
  - has higher Σr than the base

This brute-forces the local topology neighbourhood of the AE basin —
one of the few ways to discover a fundamentally different rigid maximum.
"""

from __future__ import annotations

import argparse
import json
import multiprocessing as mp
import time
from pathlib import Path

import numpy as np


def worker(args):
    seed, base_circles, drop_edge, add_edge, sigma = args
    import math
    import numpy as np
    from einstein.circle_packing_square import N_CIRCLES
    from einstein.circle_packing_square.active_set import identify_active
    from scripts.circle_packing_square.newton_max import newton_solve

    rng = np.random.default_rng(seed)
    base = np.array(base_circles, dtype=np.float64)

    # Build mutated active set: identify base, drop one pair, add another
    active = identify_active(base, eps=1e-7)
    new_pairs = [p for p in active["pairs"] if tuple(p) != tuple(drop_edge)]
    new_pairs.append(tuple(add_edge))
    new_active = {
        "pairs": new_pairs,
        "left": active["left"],
        "right": active["right"],
        "bottom": active["bottom"],
        "top": active["top"],
    }

    # Perturb start: nudge the dropped pair apart, the added pair together
    init = base.copy()
    i, j = drop_edge
    d = init[j, :2] - init[i, :2]
    n = np.linalg.norm(d)
    if n > 1e-6:
        push = sigma * 0.5
        init[i, :2] -= d / n * push
        init[j, :2] += d / n * push
    i, j = add_edge
    d = init[j, :2] - init[i, :2]
    n = np.linalg.norm(d)
    if n > 1e-6:
        pull = sigma * 0.5
        init[i, :2] += d / n * pull
        init[j, :2] -= d / n * pull
    init[:, :2] += rng.normal(0, sigma * 0.1, (N_CIRCLES, 2))
    init[:, 0] = np.clip(init[:, 0], init[:, 2], 1.0 - init[:, 2])
    init[:, 1] = np.clip(init[:, 1], init[:, 2], 1.0 - init[:, 2])

    try:
        polished, info = newton_solve(
            init, new_active,
            pair_gap=0.0,
            wall_gap=0.0,
            max_iter=80,
            tol=1e-14,
        )
    except Exception:
        return None

    if info["final_residual"] is None or info["final_residual"] > 1e-10:
        return None  # didn't converge

    # Verify FEASIBILITY of all constraints (including non-active)
    cx, cy, r = polished[:, 0], polished[:, 1], polished[:, 2]
    walls = np.concatenate([cx - r, 1.0 - cx - r, cy - r, 1.0 - cy - r])
    if walls.min() < -1e-12:
        return None
    if (r < 0).any():
        return None
    pmin = float("inf")
    for ii in range(26):
        for jj in range(ii + 1, 26):
            d = np.hypot(cx[ii] - cx[jj], cy[ii] - cy[jj])
            gap = d - r[ii] - r[jj]
            if gap < pmin:
                pmin = gap
    if pmin < -1e-12:
        return None

    return (seed, drop_edge, add_edge, info["score"], pmin, float(walls.min()), polished.tolist())


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--base", type=str, default="results-temp/p14_top.json")
    p.add_argument("--n-trials", type=int, default=1000,
                   help="number of (drop, add) pairs to try")
    p.add_argument("--workers", type=int, default=None)
    p.add_argument("--sigma", type=float, default=0.005)
    p.add_argument("--seed-base", type=int, default=70000)
    p.add_argument("--output", type=str, default="results-temp/p14_topo_enum.json")
    args = p.parse_args()

    workers = args.workers or max(1, mp.cpu_count() - 1)
    print(f"Workers: {workers}")

    with open(args.base) as f:
        data = json.load(f)
    if isinstance(data, list) and data:
        base = np.array(data[0]["data"]["circles"], dtype=np.float64)
    elif isinstance(data, dict) and "circles" in data:
        base = np.array(data["circles"], dtype=np.float64)
    elif isinstance(data, dict) and "best_circles" in data and data["best_circles"]:
        base = np.array(data["best_circles"], dtype=np.float64)
    else:
        raise ValueError("Unknown base format")

    print(f"Base sum_r: {base[:,2].sum():.16f}")

    from einstein.circle_packing_square.active_set import identify_active
    active = identify_active(base, eps=1e-7)
    n = 26
    all_pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    active_set = set(tuple(p) for p in active["pairs"])
    inactive = [p for p in all_pairs if p not in active_set]

    print(f"Active pairs: {len(active['pairs'])}, inactive: {len(inactive)}")

    rng = np.random.default_rng(args.seed_base)

    # Sample (drop, add) candidates
    tasks = []
    for trial in range(args.n_trials):
        drop = active["pairs"][int(rng.integers(0, len(active["pairs"])))]
        add = inactive[int(rng.integers(0, len(inactive)))]
        sigma = args.sigma * float(rng.uniform(0.5, 2.0))
        tasks.append((args.seed_base + trial, base.tolist(), drop, add, sigma))

    AE = base[:, 2].sum()

    t0 = time.time()
    best_score = AE
    best_record = None
    found_above = []
    n_done = 0
    n_converged = 0

    with mp.Pool(workers) as pool:
        for result in pool.imap_unordered(worker, tasks):
            n_done += 1
            if result is None:
                continue
            n_converged += 1
            seed, drop, add, score, pmin, wmin, circles = result
            if score > AE + 1e-13:
                found_above.append((score, drop, add))
                if score > best_score:
                    best_score = score
                    best_record = {
                        "seed": seed, "drop": drop, "add": add,
                        "score": score, "pmin": pmin, "wmin": wmin,
                        "circles": circles,
                    }
                    elapsed = time.time() - t0
                    print(f"  seed={seed:5d} drop={drop} add={add} score={score:.16f} d_AE={score-AE:+.3e} ({elapsed:.1f}s) <<< NEW", flush=True)
            if n_done % 50 == 0:
                elapsed = time.time() - t0
                print(f"  ...{n_done}/{args.n_trials} done, converged={n_converged}, found above AE: {len(found_above)}, best={best_score:.16f} ({elapsed:.1f}s)", flush=True)

    print()
    print(f"Final: best={best_score:.16f}  d_AE={best_score-AE:+.3e}  ({time.time()-t0:.1f}s)")
    print(f"Converged: {n_converged}/{args.n_trials}, found above AE: {len(found_above)}")

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w") as f:
        json.dump({
            "base_score": AE,
            "best_score": best_score,
            "best_record": best_record,
            "n_converged": n_converged,
            "n_above_AE": len(found_above),
        }, f, indent=2)


if __name__ == "__main__":
    main()
