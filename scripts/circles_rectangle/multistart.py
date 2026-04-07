"""Multistart search for a better basin on Circles in Rectangle (n=21).

Polishes top-leaderboard solutions and many random starts to discover any
configuration that beats capybara's 2.3658323759185 by minImprovement (1e-7).
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np

from einstein.circles_rectangle.evaluator import N_CIRCLES, evaluate_verbose
from einstein.circles_rectangle.polish import polish

CAPYBARA = 2.3658323759185156
MIN_IMPROVEMENT = 1e-7


def random_start(seed: int, w_init: float = 1.0) -> np.ndarray:
    """Generate a random non-overlapping start by greedy placement."""
    rng = np.random.default_rng(seed)
    h_init = 2.0 - w_init
    circles = np.zeros((N_CIRCLES, 3))
    placed = 0
    attempts = 0
    while placed < N_CIRCLES and attempts < 50000:
        attempts += 1
        r = rng.uniform(0.06, 0.16)
        cx = rng.uniform(r, w_init - r)
        cy = rng.uniform(r, h_init - r)
        ok = True
        for k in range(placed):
            d = np.hypot(circles[k, 0] - cx, circles[k, 1] - cy)
            if d < r + circles[k, 2]:
                ok = False
                break
        if ok:
            circles[placed] = (cx, cy, r)
            placed += 1
    if placed < N_CIRCLES:
        # Fallback: shrink and retry
        return random_start(seed * 7 + 13, w_init)
    return circles


def grid_start(rows: int, cols: int, w: float = 1.0) -> np.ndarray:
    """Regular grid start (rows × cols ≥ 21)."""
    h = 2.0 - w
    n = rows * cols
    if n < N_CIRCLES:
        raise ValueError(f"rows×cols={n} < {N_CIRCLES}")
    cell_w = w / cols
    cell_h = h / rows
    r = 0.5 * min(cell_w, cell_h) * 0.95
    circles = []
    for i in range(rows):
        for j in range(cols):
            cx = (j + 0.5) * cell_w
            cy = (i + 0.5) * cell_h
            circles.append([cx, cy, r])
            if len(circles) == N_CIRCLES:
                return np.array(circles, dtype=np.float64)
    return np.array(circles[:N_CIRCLES], dtype=np.float64)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-random", type=int, default=30)
    parser.add_argument("--seed-offset", type=int, default=0)
    parser.add_argument("--out", type=str, default="results/problem-17-circles-rectangle/multistart.jsonl")
    args = parser.parse_args()

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    log = []

    best_score = -np.inf
    best_idx = -1
    target = CAPYBARA + MIN_IMPROVEMENT

    print(f"Target to beat: {target:.13f}  (capybara + 1e-7)")
    print(f"Capybara floor: {CAPYBARA:.13f}")
    print()

    starts = []

    # 5 grid starts
    for rows, cols in [(3, 7), (7, 3), (4, 6), (6, 4), (5, 5)]:
        try:
            starts.append((f"grid-{rows}x{cols}", grid_start(rows, cols)))
        except Exception:
            pass

    # Different aspect ratios
    for w in [0.85, 0.95, 1.0, 1.05, 1.15]:
        starts.append((f"grid-7x3-w{w:.2f}", grid_start(7, 3, w=w)))

    # Random starts
    for k in range(args.n_random):
        seed = args.seed_offset + k * 31 + 7
        try:
            starts.append((f"random-s{seed}", random_start(seed)))
        except Exception as e:
            print(f"  random-s{seed}: failed to seed ({e})")

    print(f"Total starts: {len(starts)}")
    print()

    t0 = time.time()
    for idx, (name, x0) in enumerate(starts):
        try:
            polished, w, info = polish(x0, maxiter=500, overlap_slack=0.0)
        except Exception as e:
            print(f"[{idx:3d}] {name}: polish FAILED — {e}")
            continue

        score = info["score"]
        delta = score - CAPYBARA
        if score > best_score:
            best_score = score
            best_idx = idx

        # Save if competitive
        marker = ""
        if score > CAPYBARA:
            marker = "  *** above capybara ***"
        if score >= target:
            marker = "  *** BEATS capybara + 1e-7 ***"

        print(f"[{idx:3d}] {name:<25} score={score:.13f} Δcap={delta:+.3e}{marker}")

        log.append({
            "idx": idx,
            "name": name,
            "score": score,
            "delta_cap": delta,
            "perim": info["perimeter"],
            "circles": polished.tolist(),
        })

    print()
    print(f"Best: idx={best_idx}  score={best_score:.13f}  (Δcap={best_score-CAPYBARA:+.3e})")
    print(f"Total time: {time.time() - t0:.1f}s")

    # Save all
    with open(out_path, "w") as f:
        for entry in log:
            f.write(json.dumps(entry) + "\n")
    print(f"Saved to {out_path}")


if __name__ == "__main__":
    main()
