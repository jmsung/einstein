"""Hinge gradient descent for the norm-2 basin (P6 Kissing Number).

At low scores the smooth-surrogate L-BFGS-B is dominated by the softplus
noise floor. Instead, use the EXACT subgradient of the hinge loss on the
active set (pairs with 2 - dist > 0) and step along it. The key tricks:

  1. Active set is small (~hundreds of pairs at this depth) so the gradient
     is sparse and cheap.
  2. We project back to norm = 2 after each step (basin convention).
  3. Use Armijo backtracking to find a step size that strictly improves the
     SLOW-path score (the only thing the arena cares about).
  4. Each accepted step is verified with overlap_loss before being persisted.

Usage:
    uv run python scripts/kissing_number/polish_hinge_gd.py [--budget 600]
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
NORM = 2.0


def centers_from_v(v: np.ndarray) -> np.ndarray:
    """Match overlap_loss internals exactly: c = 2 * v / ||v||."""
    return 2.0 * v / np.linalg.norm(v, axis=1, keepdims=True)


def slow_score(v: np.ndarray) -> float:
    return overlap_loss(v)


def hinge_grad_centers(c: np.ndarray) -> tuple[np.ndarray, float, int]:
    """Compute (grad wrt c, total hinge loss, n_active_pairs).

    grad[i] = sum_{j active} -(c[i]-c[j])/dist  +  sum_{j active'} (c[i]-c[j])/dist
    Equivalently for each pair (i,j) with 2 - dist > 0:
        grad[i] += -(c[i]-c[j])/dist
        grad[j] += -(c[j]-c[i])/dist
    Using full vectorized form is fine at N=594.
    """
    diff = c[:, None, :] - c[None, :, :]  # (N, N, D)
    dist2 = np.sum(diff * diff, axis=-1)
    np.fill_diagonal(dist2, 4.0)
    dist = np.sqrt(dist2)
    active = (dist < 2.0).astype(np.float64)
    np.fill_diagonal(active, 0.0)
    pen_pair = np.maximum(0.0, 2.0 - dist) * active
    total = 0.5 * float(pen_pair.sum())  # (i,j) and (j,i) double-counted
    n_active = int(active.sum() / 2)
    # safe division
    safe = np.where(dist > 1e-15, dist, 1.0)
    coef = active / safe  # (N, N)
    # grad_c[i] = sum_j -coef[i,j] * (c[i] - c[j]) = -coef[i,:].sum() * c[i] + coef @ c
    grad_c = coef @ c - coef.sum(axis=1)[:, None] * c
    # The above is the gradient for d/dc[i] of  0.5 * sum_{i,j} active*(2-dist).
    # d/dc[i] of (2 - ||c[i]-c[j]||) = -(c[i]-c[j])/dist.
    # 0.5 * sum_{i,j} = sum_{i<j}, and d/dc[i] picks up only terms involving i:
    #   d/dc[i] sum_{j!=i} (2 - dist(i,j)) * active[i,j]
    #   = sum_j active[i,j] * -(c[i]-c[j])/dist[i,j]
    # But we want grad of LOSS = sum_pair pen, so grad[i] = -sum_j active[i,j]*(c[i]-c[j])/dist[i,j]
    #   = -coef.sum(axis=1)*c[i] + coef @ c   ✓
    return grad_c, total, n_active


def project_norm(v: np.ndarray, norm: float) -> np.ndarray:
    return norm * v / np.linalg.norm(v, axis=1, keepdims=True)


def gd_step(v: np.ndarray, lr: float, max_back: int = 25) -> tuple[np.ndarray, float, bool]:
    """Take one GD step on the hinge loss with Armijo backtracking.

    Returns (new_v, new_score, improved).
    """
    c = centers_from_v(v)
    grad_c, _, n_act = hinge_grad_centers(c)
    if n_act == 0:
        return v, slow_score(v), False

    # Project gradient onto the tangent space of each sphere (||c||=2)
    # tangent grad = grad - <grad, c/||c||> * c/||c||
    c_unit = c / 2.0  # unit vectors since ||c||=2
    proj = np.sum(grad_c * c_unit, axis=1, keepdims=True)
    grad_tan = grad_c - proj * c_unit
    # Note: we descend by going in the -grad direction.

    cur = slow_score(v)
    cur_lr = lr
    for _ in range(max_back):
        new_c = c - cur_lr * grad_tan
        # renormalize each row to length 2
        new_c = project_norm(new_c, 2.0)
        # the corresponding v should be the same as new_c (since v is also at norm 2)
        new_v = new_c.copy()
        new_score = slow_score(new_v)
        if new_score < cur:
            return new_v, new_score, True
        cur_lr *= 0.5
    return v, cur, False


def save_best(v: np.ndarray, score: float, tag: str = "hingegd") -> None:
    p = RESULTS / "solution_best.json"
    out = {"vectors": v.tolist(), "score": score, "source": f"polish_hinge_gd:{tag}"}
    tmp = p.with_suffix(".json.tmp")
    with open(tmp, "w") as f:
        json.dump(out, f)
    os.replace(tmp, p)
    if MB_SOLUTIONS is not None:
        MB_SOLUTIONS.mkdir(parents=True, exist_ok=True)
        mb_p = MB_SOLUTIONS / f"hingegd-{tag}-{score:.6e}.json"
        with open(mb_p, "w") as f:
            json.dump(out, f)
    print(f"  >>> SAVED {score:.15e}", flush=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--budget", type=int, default=600)
    parser.add_argument(
        "--lrs",
        type=str,
        default="1e-12,1e-13,1e-14,1e-15",
    )
    parser.add_argument(
        "--warm-start",
        type=str,
        default=str(RESULTS / "solution_best.json"),
    )
    args = parser.parse_args()

    print("=" * 72)
    print("HINGE GRADIENT DESCENT")
    print("=" * 72)

    with open(args.warm_start) as f:
        data = json.load(f)
    v = np.array(data["vectors"], dtype=np.float64)
    v = project_norm(v, NORM)

    start_score = slow_score(v)
    print(f"Start: {start_score:.15e}")

    c = centers_from_v(v)
    _, _, n_act = hinge_grad_centers(c)
    print(f"Active pairs (penalty > 0): {n_act}")

    best_v = v.copy()
    best_score = start_score
    save_best(best_v, best_score, "init")

    lrs = [float(x) for x in args.lrs.split(",")]
    t_start = time.time()
    total_steps = 0

    for lr in lrs:
        if time.time() - t_start > args.budget:
            print("budget reached")
            break
        print(f"\n--- LR = {lr:.0e} ---")
        n_no_improve = 0
        for step_i in range(2000):
            if time.time() - t_start > args.budget:
                break
            new_v, new_score, improved = gd_step(best_v.copy(), lr=lr)
            total_steps += 1
            if improved and new_score < best_score:
                best_v = new_v
                best_score = new_score
                n_no_improve = 0
                if step_i % 5 == 0:
                    save_best(best_v, best_score, f"lr{lr:.0e}")
            else:
                n_no_improve += 1
                if n_no_improve >= 30:
                    print(f"  stalled after {step_i+1} steps at lr={lr:.0e}")
                    break
            if (step_i + 1) % 50 == 0:
                print(
                    f"  step {step_i+1}: best={best_score:.15e}",
                    flush=True,
                )
        save_best(best_v, best_score, f"lr{lr:.0e}_final")

    print()
    print("=" * 72)
    print(f"FINAL: {best_score:.15e}")
    print(f"Total GD steps: {total_steps}")
    print("=" * 72)


if __name__ == "__main__":
    main()
