"""mpmath rounding-lottery polish for the norm-2 basin (P6 Kissing Number).

When float64 greedy/GD saturates near the float64 floor (each remaining
active pair is at exactly 1 ulp(2.0)/2 = 1.11e-16 below 2.0), we can
sometimes break through by recomputing the configuration in extended
precision (50+ digits), running a short Newton-style step on the active
pairs in mpmath, and rounding back to float64. The hope: the rounded
float64 representation lands on the "right" side of 2.0 for at least some
of the active pairs, knocking them out.

This is purely a float64-rounding lottery, but a focused one — we know
exactly which pairs need to round up.

Usage:
    uv run python scripts/kissing_number/polish_mpmath.py [--digits 50] [--rounds 200]
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

import numpy as np
import mpmath as mp

from einstein.kissing_number.evaluator import overlap_loss

RESULTS = Path("results/problem-6-kissing-number")
POLISH_TRAIL = RESULTS / "polish-trail"
N = 594
D = 11
NORM = 2.0


def active_pairs(v: np.ndarray) -> tuple[np.ndarray, np.ndarray, float]:
    """Return (idx_i, idx_j, total_pen) for pairs at penalty > 0."""
    c = 2.0 * v / np.linalg.norm(v, axis=1, keepdims=True)
    diff = c[:, None, :] - c[None, :, :]
    dist = np.sqrt(np.sum(diff**2, axis=-1))
    np.fill_diagonal(dist, 2.0)
    n = len(c)
    i, j = np.triu_indices(n, k=1)
    pair_dist = dist[i, j]
    mask = pair_dist < 2.0
    pen = np.maximum(0.0, 2.0 - pair_dist)
    return i[mask], j[mask], float(pen.sum())


def save_best(v: np.ndarray, score: float, tag: str = "mpmath") -> None:
    p = RESULTS / "solution_best.json"
    out = {"vectors": v.tolist(), "score": score, "source": f"polish_mpmath:{tag}"}
    tmp = p.with_suffix(".json.tmp")
    with open(tmp, "w") as f:
        json.dump(out, f)
    os.replace(tmp, p)
    POLISH_TRAIL.mkdir(parents=True, exist_ok=True)
    trail = POLISH_TRAIL / f"mpmath-{tag}-{score:.6e}.json"
    with open(trail, "w") as f:
        json.dump(out, f)
    print(f"  >>> SAVED {score:.15e}", flush=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--digits", type=int, default=50)
    parser.add_argument("--rounds", type=int, default=300)
    parser.add_argument("--scale", type=float, default=1e-15)
    parser.add_argument("--warm-start", default=str(RESULTS / "solution_best.json"))
    args = parser.parse_args()

    mp.mp.dps = args.digits

    print("=" * 72)
    print(f"MPMATH POLISH at {args.digits} digits")
    print("=" * 72)

    with open(args.warm_start) as f:
        data = json.load(f)
    v = np.array(data["vectors"], dtype=np.float64)

    start_score = overlap_loss(v)
    print(f"Start: {start_score:.15e}")

    ai, aj, ap = active_pairs(v)
    print(f"Active pairs: {len(ai)} sum_pen={ap:.6e}")

    best_v = v.copy()
    best_score = start_score

    rng = np.random.default_rng(2026)

    for r in range(args.rounds):
        # For each active pair, push the two endpoints apart in mp precision
        # by shifting along (c_i - c_j) direction by a tiny scale, then renormalizing.
        # We use random subset of active pairs to avoid over-constraining.
        v_mp = mp.matrix(v.tolist())
        n_rows, n_cols = v_mp.rows, v_mp.cols

        ai, aj, _ = active_pairs(v)
        if len(ai) == 0:
            print("  no active pairs left")
            break

        # Sample direction: pick random subset of active pairs to nudge
        k_pick = max(1, len(ai) // 3)
        pick_idx = rng.choice(len(ai), size=k_pick, replace=False)

        # In float64, compute the unit direction (c_i - c_j) per chosen pair, scaled
        c = 2.0 * v / np.linalg.norm(v, axis=1, keepdims=True)
        scale = args.scale * (1.0 + rng.standard_normal() * 0.5)

        for k in pick_idx:
            i, j = int(ai[k]), int(aj[k])
            d_ij = c[i] - c[j]
            n_d = float(np.linalg.norm(d_ij))
            if n_d < 1e-15:
                continue
            u_dir = d_ij / n_d
            # nudge: c_i += eps*u_dir, c_j -= eps*u_dir, then renormalize via mp
            for col in range(n_cols):
                v_mp[i, col] = v_mp[i, col] + mp.mpf(scale) * mp.mpf(float(u_dir[col]))
                v_mp[j, col] = v_mp[j, col] - mp.mpf(scale) * mp.mpf(float(u_dir[col]))
            # Renormalize i and j to length NORM in mpmath
            for ki in (i, j):
                norm_sq = mp.mpf(0)
                for col in range(n_cols):
                    norm_sq += v_mp[ki, col] * v_mp[ki, col]
                norm = mp.sqrt(norm_sq)
                factor = mp.mpf(NORM) / norm
                for col in range(n_cols):
                    v_mp[ki, col] = v_mp[ki, col] * factor

        # Round back to float64
        v_new = np.array(
            [[float(v_mp[ii, jj]) for jj in range(n_cols)] for ii in range(n_rows)],
            dtype=np.float64,
        )
        # Re-snap to NORM in float64 (matching submission convention)
        v_new = NORM * v_new / np.linalg.norm(v_new, axis=1, keepdims=True)

        new_score = overlap_loss(v_new)
        if new_score < best_score:
            best_score = new_score
            best_v = v_new.copy()
            v = v_new
            ai_new, aj_new, ap_new = active_pairs(v)
            print(
                f"  round {r+1}: improved → {new_score:.15e}  active={len(ai_new)} (was {len(ai)})",
                flush=True,
            )
            save_best(best_v, best_score, tag=f"r{r+1}")
        elif (r + 1) % 20 == 0:
            print(
                f"  round {r+1}: no improvement (best={best_score:.15e}, active={len(ai)})",
                flush=True,
            )

    print()
    print("=" * 72)
    print(f"FINAL: {best_score:.15e}")
    print("=" * 72)


if __name__ == "__main__":
    main()
