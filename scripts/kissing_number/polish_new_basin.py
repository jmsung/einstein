"""Slow-path greedy polish for the norm-2 basin (P6 Kissing Number, d=11).

Loads results/problem-6-kissing-number/solution_best.json and runs greedy
single-vector polish using the SLOW-PATH evaluator formula (matching the
arena verifier bit-exactly).

Why slow-path: a fast cosine-based inner loop has float64 noise comparable
to the score itself in this basin. We must use the slow-path centers
formula for both candidate scoring and running total.

Vectors are kept at norm = 2.0 (basin convention).
Saves on every strict improvement to solution_best.json. If the env var
EINSTEIN_MB_ROOT is set, also writes a backup to that directory.
"""

from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path

import numpy as np

from einstein.kissing_number.evaluator import overlap_loss

RESULTS = Path("results/problem-6-kissing-number")
MB_ROOT = os.environ.get("EINSTEIN_MB_ROOT")
MB_SOLUTIONS = (
    Path(MB_ROOT) / "docs/problem-6-kissing-number/solutions" if MB_ROOT else None
)
N = 594
D = 11
NORM = 2.0  # basin convention: ||v_i|| = 2 exactly


def slow_total(v: np.ndarray) -> float:
    """Match overlap_loss exactly: compute centers internally then full slow path."""
    norms = np.linalg.norm(v, axis=1, keepdims=True)
    c = 2.0 * v / norms
    diff = c[:, None, :] - c[None, :, :]
    dist = np.sqrt(np.sum(diff**2, axis=-1))
    n = c.shape[0]
    mask = np.triu(np.ones((n, n), dtype=bool), k=1)
    return float(np.sum(np.maximum(0.0, 2.0 - dist[mask])))


def vec_pen(c: np.ndarray, idx: int) -> float:
    """Sum over j != idx of max(0, 2 - ||c[idx] - c[j]||) using slow path."""
    diffs = c[idx] - c  # (n, d)
    dists = np.sqrt(np.sum(diffs**2, axis=1))  # (n,)
    pen = np.maximum(0.0, 2.0 - dists)
    pen[idx] = 0.0
    return float(pen.sum())


def all_vec_pens(c: np.ndarray) -> np.ndarray:
    """Per-vector contribution for sampling weights."""
    diff = c[:, None, :] - c[None, :, :]
    dist = np.sqrt(np.sum(diff**2, axis=-1))
    np.fill_diagonal(dist, 2.0)
    pen_mat = np.maximum(0.0, 2.0 - dist)
    np.fill_diagonal(pen_mat, 0.0)
    return pen_mat.sum(axis=1)


def polish_round(
    v: np.ndarray,
    scale: float,
    seed: int,
    time_limit_s: float,
    label: str,
    save_callback,
) -> tuple[np.ndarray, float, int]:
    """Run greedy single-vector polish at the given scale until time runs out.

    Returns (best_v, best_total, n_improvements).
    """
    rng = np.random.default_rng(seed)
    norms = np.linalg.norm(v, axis=1, keepdims=True)
    c = 2.0 * v / norms
    total = slow_total(v)
    best_v = v.copy()
    best_total = total

    vec_pens = all_vec_pens(c)
    pen_sum = vec_pens.sum()
    probs = vec_pens / pen_sum if pen_sum > 0 else np.full(N, 1.0 / N)

    n_imp = 0
    n_iter = 0
    t0 = time.time()
    last_resync = 0
    last_log = t0

    while True:
        n_iter += 1

        # Periodic resync of total + vec_pens to avoid drift and refresh sampling
        if n_iter - last_resync >= 5_000:
            total = slow_total(v)
            vec_pens = all_vec_pens(c)
            pen_sum = vec_pens.sum()
            probs = vec_pens / pen_sum if pen_sum > 0 else np.full(N, 1.0 / N)
            last_resync = n_iter

        idx = int(rng.choice(N, p=probs))

        old_v = v[idx].copy()
        old_c = c[idx].copy()
        old_vp = vec_pen(c, idx)  # always fresh, never cached

        # Perturb v[idx], rescale to ||v|| = NORM
        delta_vec = rng.standard_normal(D) * scale
        v[idx] = old_v + delta_vec
        v[idx] *= NORM / np.linalg.norm(v[idx])
        c[idx] = 2.0 * v[idx] / np.linalg.norm(v[idx])

        new_vp = vec_pen(c, idx)
        d = new_vp - old_vp

        if d < 0:
            total += d
            n_imp += 1
            if total < best_total:
                # Verify with full slow_total — drift can mislead
                exact = slow_total(v)
                if exact < best_total:
                    best_total = exact
                    best_v = v.copy()
                    save_callback(best_v, best_total)
                    total = exact  # resync running total to exact
        else:
            v[idx] = old_v
            c[idx] = old_c

        now = time.time()
        if now - last_log >= 30.0:
            last_log = now
            print(
                f"  [{label} {scale:.0e}] iter={n_iter:>9,d} "
                f"best={best_total:.15e} "
                f"impr={n_imp} ({n_imp/n_iter*100:.2f}%) {now-t0:.0f}s",
                flush=True,
            )

        if now - t0 > time_limit_s:
            break

    return best_v, best_total, n_imp


def save_best(v: np.ndarray, score: float) -> None:
    """Atomically save to solution_best.json. Optional MB backup if EINSTEIN_MB_ROOT is set."""
    p = RESULTS / "solution_best.json"
    out = {"vectors": v.tolist(), "score": score, "source": "polish_new_basin.py"}
    tmp = p.with_suffix(".json.tmp")
    with open(tmp, "w") as f:
        json.dump(out, f)
    os.replace(tmp, p)
    if MB_SOLUTIONS is not None:
        MB_SOLUTIONS.mkdir(parents=True, exist_ok=True)
        mb_p = MB_SOLUTIONS / f"new-basin-polish-{score:.6e}.json"
        with open(mb_p, "w") as f:
            json.dump(out, f)
    print(f"  >>> SAVED {score:.15e}", flush=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--budget", type=int, default=1800, help="Total seconds")
    parser.add_argument("--seed", type=int, default=2026)
    parser.add_argument(
        "--scales",
        type=str,
        default="1e-13,1e-14,1e-15,1e-13,1e-14,1e-15,1e-14,1e-15",
        help="Comma-separated scale schedule",
    )
    parser.add_argument(
        "--warm-start",
        type=str,
        default=str(RESULTS / "solution_best.json"),
        help="Path to JSON with 'vectors' key",
    )
    args = parser.parse_args()

    print("=" * 72)
    print(f"SLOW-PATH GREEDY POLISH — total budget {args.budget}s")
    print(f"Warm start: {args.warm_start}")
    print("=" * 72)

    with open(args.warm_start) as f:
        data = json.load(f)
    v = np.array(data["vectors"], dtype=np.float64)
    # Coerce to norm = NORM exactly (basin convention)
    v *= NORM / np.linalg.norm(v, axis=1, keepdims=True)

    start_score = overlap_loss(v)
    print(f"Start score:    {start_score:.15e}")
    print()

    rng = np.random.default_rng(args.seed)
    scales = [float(s) for s in args.scales.split(",")]
    per_round = max(60, args.budget // len(scales))
    print(f"Schedule: {scales}, {per_round}s each")

    best_v = v.copy()
    best_score = start_score
    save_best(best_v, best_score)

    t_start = time.time()
    for ridx, scale in enumerate(scales, 1):
        if time.time() - t_start > args.budget:
            print("  total budget reached")
            break
        sd = int(rng.integers(1_000_000_000))
        new_v, new_score, n_imp = polish_round(
            best_v.copy(),
            scale=scale,
            seed=sd,
            time_limit_s=per_round,
            label=f"R{ridx:02d}",
            save_callback=save_best,
        )
        exact = overlap_loss(new_v)
        if exact < best_score:
            best_v = new_v.copy()
            best_score = exact
            print(
                f"  Round {ridx}/{len(scales)} {scale:.0e}: exact={exact:.15e} "
                f"(Δ={start_score - exact:+.3e}) [{n_imp} improvements]"
            )
            save_best(best_v, best_score)
        else:
            print(
                f"  Round {ridx}/{len(scales)} {scale:.0e}: exact={exact:.15e} (no improvement, {n_imp} attempted)"
            )

    final = overlap_loss(best_v)
    print()
    print("=" * 72)
    print(f"FINAL: {final:.15e}")
    print(f"Start: {start_score:.15e}")
    print(f"Delta: {start_score - final:+.6e}")
    print("=" * 72)


if __name__ == "__main__":
    main()
