"""Multistart polisher for Circle Packing in a Square (P14, n=26).

Strategies:
  - random: random non-overlapping seed via greedy + jiggle
  - perturb: perturb a known SOTA and re-polish
  - topology: break a contact in SOTA, perturb, re-polish

Usage:
  uv run python -m scripts.circle_packing_square.multistart \
      --strategy random --n-trials 200 --output results-temp/p14_random.json
  uv run python -m scripts.circle_packing_square.multistart \
      --strategy perturb --n-trials 200 --sigma 0.02 \
      --warm results-temp/p14_top.json --output results-temp/p14_perturb.json
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np

from einstein.circle_packing_square import N_CIRCLES, evaluate, evaluate_strict
from einstein.circle_packing_square.polish import polish


def random_init(rng: np.random.Generator, r_init: float = 0.05) -> np.ndarray:
    """Random initial circles via greedy non-overlapping placement."""
    circles = np.zeros((N_CIRCLES, 3), dtype=np.float64)
    placed = 0
    attempts = 0
    while placed < N_CIRCLES and attempts < 100000:
        cx = rng.uniform(r_init, 1.0 - r_init)
        cy = rng.uniform(r_init, 1.0 - r_init)
        ok = True
        for j in range(placed):
            d = np.hypot(cx - circles[j, 0], cy - circles[j, 1])
            if d < r_init * 2:
                ok = False
                break
        if ok:
            circles[placed] = [cx, cy, r_init]
            placed += 1
        attempts += 1
    if placed < N_CIRCLES:
        # back off radius and retry
        return random_init(rng, r_init * 0.9)
    return circles


def perturb(circles: np.ndarray, rng: np.random.Generator, sigma: float) -> np.ndarray:
    out = circles.copy()
    out[:, 0] += rng.normal(0.0, sigma, N_CIRCLES)
    out[:, 1] += rng.normal(0.0, sigma, N_CIRCLES)
    # keep r non-negative; allow it to drift
    out[:, 2] *= rng.uniform(1.0 - 0.5 * sigma, 1.0 + 0.5 * sigma, N_CIRCLES)
    out[:, 2] = np.clip(out[:, 2], 1e-4, 0.4)
    out[:, 0] = np.clip(out[:, 0], out[:, 2], 1.0 - out[:, 2])
    out[:, 1] = np.clip(out[:, 1], out[:, 2], 1.0 - out[:, 2])
    return out


def safe_polish(circles: np.ndarray, ftol: float = 1e-16) -> tuple[np.ndarray, float] | None:
    """Cascade: loose slack → tight slack → eval at arena tol (1e-9)."""
    try:
        c, info = polish(circles, method="SLSQP", ftol=ftol, maxiter=1500, overlap_slack=1e-6)
        c, info = polish(c, method="SLSQP", ftol=ftol, maxiter=1500, overlap_slack=1e-9)
        c, info = polish(c, method="SLSQP", ftol=ftol, maxiter=1500, overlap_slack=1e-12)
        # Eval at arena tolerance — 1e-9 matches arena verifier
        score = evaluate({"circles": c.tolist()}, tol=1e-9)
        return c, score
    except Exception:
        return None


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--strategy", choices=["random", "perturb"], required=True)
    p.add_argument("--n-trials", type=int, default=50)
    p.add_argument("--sigma", type=float, default=0.02)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--warm", type=str, default=None,
                   help="JSON file with seed solutions (for perturb)")
    p.add_argument("--output", type=str, default="results-temp/p14_multistart.json")
    args = p.parse_args()

    rng = np.random.default_rng(args.seed)

    seeds: list[np.ndarray] = []
    if args.warm and args.strategy == "perturb":
        with open(args.warm) as f:
            data = json.load(f)
        if isinstance(data, list):
            for entry in data:
                if isinstance(entry, dict):
                    if "data" in entry and "circles" in entry["data"]:
                        seeds.append(np.array(entry["data"]["circles"], dtype=np.float64))
                    elif "circles" in entry:
                        seeds.append(np.array(entry["circles"], dtype=np.float64))
        elif isinstance(data, dict) and "circles" in data:
            seeds.append(np.array(data["circles"], dtype=np.float64))
        print(f"Loaded {len(seeds)} warm seeds")

    results = []
    best_score = 0.0
    best_circles = None
    t0 = time.time()
    for trial in range(args.n_trials):
        if args.strategy == "random":
            init = random_init(rng)
        else:
            base = seeds[trial % len(seeds)]
            init = perturb(base, rng, args.sigma)

        out = safe_polish(init)
        if out is None:
            continue
        circles, score = out
        if score > best_score:
            best_score = score
            best_circles = circles
            results.append({"trial": trial, "score": score, "circles": circles.tolist()})
            elapsed = time.time() - t0
            print(f"  trial {trial:4d} NEW BEST {score:.16f}  ({elapsed:.1f}s)", flush=True)
        elif trial % 25 == 0:
            elapsed = time.time() - t0
            print(f"  trial {trial:4d} score={score:.16f}  best={best_score:.16f}  ({elapsed:.1f}s)", flush=True)

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w") as f:
        json.dump({
            "strategy": args.strategy,
            "n_trials": args.n_trials,
            "sigma": args.sigma,
            "seed": args.seed,
            "best_score": best_score,
            "best_circles": best_circles.tolist() if best_circles is not None else None,
            "history": results,
        }, f, indent=2)
    print(f"\nFinal: best={best_score:.16f}  ({time.time()-t0:.1f}s)  -> {args.output}")


if __name__ == "__main__":
    main()
