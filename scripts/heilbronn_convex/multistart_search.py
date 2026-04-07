"""Multistart global search for Heilbronn Convex (n=14).

Launches many SLSQP polishes from diverse initial configurations:
- warm-started perturbations of capybara007 and AlphaEvolve
- random 10+4 layouts
- symmetric configurations with small random breakage
Keeps a population of distinct local maxima binned by score.

Usage:
    uv run python scripts/heilbronn_convex/multistart_search.py \
        --time 300 --seed 42 --out /tmp/heilbronn_pop.json
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np

from einstein.heilbronn_convex import arena_score, hull_vertex_indices
from einstein.heilbronn_convex.optimizer import (
    polish_slsqp,
    random_convex_init,
)

SOLDIR = (
    Path.home()
    / "projects/workbench/memory-bank/einstein/docs/problem-16-heilbronn-convex/solutions"
)


def load_reference_solutions():
    """Load capybara007 and AlphaEvolve reference solutions."""
    capy = json.loads((SOLDIR / "capybara007_1029_0.027835580518.json").read_text())
    ae = json.loads((SOLDIR / "AlphaEvolve_631_0.027835571458.json").read_text())
    return (
        np.array(capy["points"], dtype=np.float64),
        np.array(ae["points"], dtype=np.float64),
    )


def generate_starting_points(rng, pts_capy, pts_ae, kind):
    """Generate one starting configuration based on the strategy kind."""
    r = rng.random()
    if kind == "near_capy":
        scale = rng.choice([1e-4, 1e-3, 5e-3, 1e-2, 3e-2])
        return pts_capy + rng.normal(0, scale, pts_capy.shape)
    if kind == "far_capy":
        scale = rng.choice([0.05, 0.1, 0.2, 0.3])
        return pts_capy + rng.normal(0, scale, pts_capy.shape)
    if kind == "near_ae":
        scale = rng.choice([1e-3, 1e-2, 5e-2])
        return pts_ae + rng.normal(0, scale, pts_ae.shape)
    if kind == "random_disk":
        return random_convex_init(rng, shape="disk")
    if kind == "random_10p4":
        return random_convex_init(rng, shape="10p4")
    if kind == "symmetric":
        # Symmetric n=14 layout: 10 on circle + 4 interior in a rect
        angles = np.linspace(0, 2 * np.pi, 11)[:-1] + rng.uniform(0, 0.3)
        hull = np.column_stack([np.cos(angles), np.sin(angles)])
        # Random rectangle of interior
        w = rng.uniform(0.1, 0.4)
        h = rng.uniform(0.1, 0.4)
        interior = np.array([[-w, -h], [w, -h], [-w, h], [w, h]])
        pts = np.vstack([hull, interior])
        # Break symmetry
        pts = pts + rng.normal(0, 0.02, pts.shape)
        return pts
    raise ValueError(f"unknown kind {kind}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--time", type=float, default=120.0, help="Wall time budget (s)")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--out", type=str, default="/tmp/heilbronn_pop.json")
    parser.add_argument("--max-iter", type=int, default=400)
    args = parser.parse_args()

    pts_capy, pts_ae = load_reference_solutions()
    target = arena_score(pts_capy)
    print(f"Target (capybara): {target:.16f}")

    rng = np.random.default_rng(args.seed)
    strategies = [
        "near_capy", "near_capy", "near_capy",
        "far_capy", "far_capy",
        "near_ae", "near_ae",
        "random_10p4", "random_10p4",
        "symmetric",
    ]

    best_score = target
    best_pts = pts_capy.copy()
    # Population of distinct maxima (binned by score at 1e-10 resolution)
    pop: dict[int, tuple[float, np.ndarray, str]] = {}
    start = time.time()
    trials = 0
    by_kind: dict[str, int] = {}

    while time.time() - start < args.time:
        kind = rng.choice(strategies)
        try:
            pts0 = generate_starting_points(rng, pts_capy, pts_ae, kind)
        except Exception:
            continue
        polished, score = polish_slsqp(pts0, max_iter=args.max_iter)
        trials += 1
        by_kind[kind] = by_kind.get(kind, 0) + 1
        if not np.isfinite(score) or score < 0.02:
            continue
        key = int(round(score * 1e11))  # 1e-11 bin
        if key not in pop or score > pop[key][0]:
            pop[key] = (score, polished.copy(), kind)
        if score > best_score:
            improvement = score - target
            print(
                f"[{trials:5d}][{kind:12s}] NEW BEST! {score:.20f}  delta={improvement:+.3e}"
            )
            best_score = score
            best_pts = polished.copy()
        if trials % 100 == 0:
            top_scores = sorted({v[0] for v in pop.values()}, reverse=True)[:5]
            elapsed = time.time() - start
            print(
                f"[{trials:5d}] {elapsed:5.0f}s  pop={len(pop)}  best={best_score:.16f}  "
                f"top5={[f'{s:.10f}' for s in top_scores]}"
            )

    print(f"\nDone. Trials={trials}, elapsed={time.time()-start:.1f}s")
    print(f"By kind: {by_kind}")

    # Dump top-20 of population to file
    sorted_pop = sorted(pop.values(), key=lambda x: -x[0])[:20]
    out = {
        "target": target,
        "best_score": best_score,
        "best_pts": best_pts.tolist(),
        "population_top20": [
            {"score": s, "points": pts.tolist(), "kind": kind, "n_hull": len(hull_vertex_indices(pts))}
            for s, pts, kind in sorted_pop
        ],
        "stats": {"trials": trials, "elapsed_s": time.time() - start, "by_kind": by_kind},
    }
    Path(args.out).write_text(json.dumps(out, indent=2))
    print(f"Saved population to {args.out}")
    print("\nTop 10 unique scores found:")
    for i, (s, pts, kind) in enumerate(sorted_pop[:10]):
        nh = len(hull_vertex_indices(pts))
        print(f"  #{i+1:2d}  score={s:.16f}  hull={nh}+{14-nh}  kind={kind}")


if __name__ == "__main__":
    main()
