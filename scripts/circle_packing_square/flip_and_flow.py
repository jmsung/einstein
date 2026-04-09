"""Poincaré flip-and-flow basin escape for P14 (n=26).

Algorithm (Poincaré council recommendation):
  1. Compute Connelly-Zhang dual stresses on AE's contact graph (= |Lagrange λ_e|).
  2. Rank edges by smallest |stress| (cheapest to break).
  3. For each cheap edge (i,j):
       a. Drop the (i,j) constraint, build modified active set
       b. Perturb circles i and j anti-parallel along their contact normal by σ
       c. SLSQP-refine on the modified (one fewer constraint) → new (i,j) gap > 0
       d. Re-saturate with FULL non-overlap constraints, polish to convergence
       e. Identify the new contact graph; if it differs from AE, we have a new basin
  4. Score each new basin; return any above AE's 2.6359830849176076.
"""

from __future__ import annotations

import argparse
import json
import math
import multiprocessing as mp
import time
from pathlib import Path

import numpy as np


def compute_stresses(circles: np.ndarray, pairs: list, walls: list) -> np.ndarray:
    """Compute Lagrange multipliers (= dual stresses) at the active set."""
    n = len(circles)
    rows = []
    for i, j in pairs:
        dx = circles[i, 0] - circles[j, 0]
        dy = circles[i, 1] - circles[j, 1]
        d = np.hypot(dx, dy)
        row = np.zeros(3 * n)
        row[3 * i + 0] = dx / d
        row[3 * i + 1] = dy / d
        row[3 * i + 2] = -1.0
        row[3 * j + 0] = -dx / d
        row[3 * j + 1] = -dy / d
        row[3 * j + 2] = -1.0
        rows.append(row)
    for side, i in walls:
        row = np.zeros(3 * n)
        if side == "L":
            row[3 * i + 0] = 1
            row[3 * i + 2] = -1
        elif side == "R":
            row[3 * i + 0] = -1
            row[3 * i + 2] = -1
        elif side == "B":
            row[3 * i + 1] = 1
            row[3 * i + 2] = -1
        elif side == "T":
            row[3 * i + 1] = -1
            row[3 * i + 2] = -1
        rows.append(row)
    J = np.array(rows)
    grad_f = np.zeros(3 * n)
    grad_f[2::3] = 1.0
    lam, *_ = np.linalg.lstsq(J.T, grad_f, rcond=None)
    return lam  # length: len(pairs) + len(walls)


def worker(args):
    seed, base_circles, drop_edge_pair, sigma = args
    import scipy.optimize as opt
    import numpy as np
    from einstein.circle_packing_square import N_CIRCLES, evaluate
    from einstein.circle_packing_square.polish import polish

    rng = np.random.default_rng(seed)
    base = np.array(base_circles, dtype=np.float64).copy()

    # Step (b): perturb circles i,j anti-parallel along their contact normal
    i, j = drop_edge_pair
    dx = base[j, 0] - base[i, 0]
    dy = base[j, 1] - base[i, 1]
    d = math.hypot(dx, dy)
    if d < 1e-9:
        return None
    nx, ny = dx / d, dy / d
    base[i, 0] -= 0.5 * sigma * nx
    base[i, 1] -= 0.5 * sigma * ny
    base[j, 0] += 0.5 * sigma * nx
    base[j, 1] += 0.5 * sigma * ny

    # Light global jitter
    base[:, :2] += rng.normal(0, sigma * 0.1, (N_CIRCLES, 2))
    base[:, 0] = np.clip(base[:, 0], base[:, 2], 1.0 - base[:, 2])
    base[:, 1] = np.clip(base[:, 1], base[:, 2], 1.0 - base[:, 2])

    # Step (d): re-saturate with FULL constraints, polish cascade
    cur = base
    best_score = -1.0
    best_c = None
    for slack in (1e-4, 1e-6, 1e-8, 1e-10):
        try:
            new, _ = polish(cur, method="SLSQP", ftol=1e-16, maxiter=2000, overlap_slack=slack)
            try:
                s = evaluate({"circles": new.tolist()}, tol=1e-9)
                if s > best_score:
                    best_score = s
                    best_c = new.copy()
                cur = new
            except Exception:
                pass
        except Exception:
            break
    if best_c is None:
        return None

    # Identify new contact graph
    n = N_CIRCLES
    cs = np.array(best_c)
    new_pairs = set()
    for ii in range(n):
        for jj in range(ii + 1, n):
            dd = math.hypot(cs[ii, 0] - cs[jj, 0], cs[ii, 1] - cs[jj, 1])
            if abs(dd - cs[ii, 2] - cs[jj, 2]) < 1e-7:
                new_pairs.add((ii, jj))

    return (seed, drop_edge_pair, best_score, len(new_pairs), best_c.tolist())


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--base", type=str, default="results-temp/p14_top.json")
    p.add_argument("--workers", type=int, default=None)
    p.add_argument("--n-edges-to-drop", type=int, default=20,
                   help="how many lowest-stress edges to try dropping")
    p.add_argument("--n-jitters", type=int, default=10,
                   help="random seed jitters per edge drop")
    p.add_argument("--sigma", type=float, default=5e-3)
    p.add_argument("--seed-base", type=int, default=200000)
    p.add_argument("--output", type=str, default="results-temp/p14_flipflow.json")
    args = p.parse_args()

    workers = args.workers or max(1, mp.cpu_count() - 1)
    print(f"Workers: {workers}")

    with open(args.base) as f:
        data = json.load(f)
    if isinstance(data, list) and data:
        base = np.array(data[0]["data"]["circles"], dtype=np.float64)
    elif isinstance(data, dict) and "circles" in data:
        base = np.array(data["circles"], dtype=np.float64)
    else:
        raise ValueError("Unknown base format")

    print(f"Base sum_r: {base[:,2].sum():.16f}")

    # Build active set
    n = 26
    pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            d = math.hypot(base[i, 0] - base[j, 0], base[i, 1] - base[j, 1])
            if abs(d - base[i, 2] - base[j, 2]) < 1e-9:
                pairs.append((i, j))
    walls = []
    for i in range(n):
        if abs(base[i, 0] - base[i, 2]) < 1e-9: walls.append(("L", i))
        if abs(1 - base[i, 0] - base[i, 2]) < 1e-9: walls.append(("R", i))
        if abs(base[i, 1] - base[i, 2]) < 1e-9: walls.append(("B", i))
        if abs(1 - base[i, 1] - base[i, 2]) < 1e-9: walls.append(("T", i))

    print(f"Active: {len(pairs)} pairs + {len(walls)} walls")

    # Compute stresses
    lam = compute_stresses(base, pairs, walls)
    print(f"|λ| range: [{np.min(np.abs(lam)):.3e}, {np.max(np.abs(lam)):.3e}]")

    # Rank pair edges by |stress|
    pair_stresses = [(abs(lam[k]), k, pairs[k]) for k in range(len(pairs))]
    pair_stresses.sort()  # ascending |stress| = cheapest first

    print(f"\n10 cheapest pair edges to break:")
    for s, k, pair in pair_stresses[:10]:
        print(f"  pair {pair}: |λ| = {s:.4e}")

    # Build tasks: for each cheap edge, run multiple jitter seeds
    tasks = []
    rng = np.random.default_rng(args.seed_base)
    n_edges = min(args.n_edges_to_drop, len(pairs))
    for ek in range(n_edges):
        s, k, pair = pair_stresses[ek]
        for jit in range(args.n_jitters):
            sigma = args.sigma * float(rng.uniform(0.5, 2.0))
            tasks.append((args.seed_base + ek * 100 + jit, base.tolist(), pair, sigma))

    print(f"\nTotal tasks: {len(tasks)}")

    AE = base[:, 2].sum()
    AE_contact_set = set(tuple(sorted(p)) for p in pairs)

    t0 = time.time()
    best_score = AE
    best_c = base.tolist()
    different_basins = []
    n_done = 0

    with mp.Pool(workers) as pool:
        for result in pool.imap_unordered(worker, tasks):
            n_done += 1
            if result is None:
                continue
            seed, drop_edge, score, new_n_pairs, circles = result
            # Check if contact graph differs from AE
            cs = np.array(circles)
            new_pairs_set = set()
            for ii in range(n):
                for jj in range(ii + 1, n):
                    dd = math.hypot(cs[ii, 0] - cs[jj, 0], cs[ii, 1] - cs[jj, 1])
                    if abs(dd - cs[ii, 2] - cs[jj, 2]) < 1e-9:
                        new_pairs_set.add((ii, jj))
            in_ae = len(AE_contact_set & new_pairs_set)
            new_in_solution = len(new_pairs_set - AE_contact_set)
            removed_from_ae = len(AE_contact_set - new_pairs_set)
            different = removed_from_ae > 0 or new_in_solution > 0

            if score > best_score + 1e-13:
                best_score = score
                best_c = circles
                elapsed = time.time() - t0
                marker = " <<< above AE!" if score > AE else ""
                diff_str = f" (graph diff: -{removed_from_ae} +{new_in_solution})" if different else ""
                print(f"  seed={seed} drop={drop_edge} score={score:.16f} d_AE={score-AE:+.3e}{diff_str} ({elapsed:.1f}s){marker}", flush=True)
            elif different and score > AE - 1e-7:
                different_basins.append({"seed": seed, "score": score, "diff": (removed_from_ae, new_in_solution)})

            if n_done % 50 == 0:
                elapsed = time.time() - t0
                print(f"  ...{n_done}/{len(tasks)} done, best={best_score:.16f}, different_basins_near_AE={len(different_basins)}, {elapsed:.1f}s", flush=True)

    print(f"\nFinal: best={best_score:.16f}  d_AE={best_score-AE:+.3e}")
    print(f"Different basins found near AE: {len(different_basins)}")

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w") as f:
        json.dump({
            "base_score": AE,
            "best_score": best_score,
            "best_circles": best_c,
            "different_basins_count": len(different_basins),
            "different_basins": different_basins[:20],
        }, f, indent=2)


if __name__ == "__main__":
    main()
