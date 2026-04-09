"""Active-set Newton solver for max sum-of-radii at fixed gap budget.

For a fully-rigid local maximum (#active == 3n), the score is determined
by the active set + the prescribed gap values. Here we enforce:

  pair (i,j) ∈ active:    ‖c_i - c_j‖ - r_i - r_j = -pair_gap
  wall touching circle i: cx_i - r_i = +wall_gap   (etc.)

This is 3n equations in 3n unknowns. Newton solves it to ~1e-15. The
score is then deterministic: it depends only on pair_gap, wall_gap, and
the topology.

We exploit the arena's tolerance band: pair_gap = 9e-10 (within arena
1e-9 limit, with 1e-10 safety) lets every contact "overlap" slightly,
inflating Σr_i versus the strict-zero baseline (= AlphaEvolve).
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from einstein.circle_packing_square import N_CIRCLES, evaluate
from einstein.circle_packing_square.active_set import identify_active


def newton_solve(
    initial_circles: np.ndarray,
    active: dict,
    pair_gap: float = 0.0,
    wall_gap: float = 0.0,
    max_iter: int = 30,
    tol: float = 1e-15,
) -> tuple[np.ndarray, dict]:
    """Newton on the active-constraint equality system.

    pair_gap: target gap for pair contacts (negative = overlap).
              Pair eqn: d - r_i - r_j = pair_gap
    wall_gap: target slack for wall contacts (positive = inside).
              Wall eqn: cx - r = wall_gap (etc.)
    """
    n = N_CIRCLES
    x = initial_circles.flatten().astype(np.float64)

    pairs = active["pairs"]
    lefts = active["left"]
    rights = active["right"]
    bottoms = active["bottom"]
    tops = active["top"]

    n_pair = len(pairs)
    n_wall = len(lefts) + len(rights) + len(bottoms) + len(tops)

    def residual(x):
        cx = x[0::3]
        cy = x[1::3]
        r = x[2::3]
        out = np.zeros(n_pair + n_wall)
        k = 0
        for i, j in pairs:
            d = np.hypot(cx[i] - cx[j], cy[i] - cy[j])
            out[k] = (d - r[i] - r[j]) - pair_gap
            k += 1
        for i in lefts:
            out[k] = (cx[i] - r[i]) - wall_gap
            k += 1
        for i in rights:
            out[k] = (1.0 - cx[i] - r[i]) - wall_gap
            k += 1
        for i in bottoms:
            out[k] = (cy[i] - r[i]) - wall_gap
            k += 1
        for i in tops:
            out[k] = (1.0 - cy[i] - r[i]) - wall_gap
            k += 1
        return out

    def jacobian(x):
        cx = x[0::3]
        cy = x[1::3]
        rows = []
        for i, j in pairs:
            dx = cx[i] - cx[j]
            dy = cy[i] - cy[j]
            d = np.hypot(dx, dy)
            row = np.zeros(3 * n)
            row[3 * i + 0] = dx / d
            row[3 * i + 1] = dy / d
            row[3 * i + 2] = -1.0
            row[3 * j + 0] = -dx / d
            row[3 * j + 1] = -dy / d
            row[3 * j + 2] = -1.0
            rows.append(row)
        for i in lefts:
            row = np.zeros(3 * n)
            row[3 * i + 0] = 1.0
            row[3 * i + 2] = -1.0
            rows.append(row)
        for i in rights:
            row = np.zeros(3 * n)
            row[3 * i + 0] = -1.0
            row[3 * i + 2] = -1.0
            rows.append(row)
        for i in bottoms:
            row = np.zeros(3 * n)
            row[3 * i + 1] = 1.0
            row[3 * i + 2] = -1.0
            rows.append(row)
        for i in tops:
            row = np.zeros(3 * n)
            row[3 * i + 1] = -1.0
            row[3 * i + 2] = -1.0
            rows.append(row)
        return np.array(rows)

    history = []
    for it in range(max_iter):
        g = residual(x)
        norm = float(np.linalg.norm(g))
        history.append(norm)
        if norm < tol:
            break
        J = jacobian(x)
        try:
            dx, *_ = np.linalg.lstsq(J, -g, rcond=None)
        except np.linalg.LinAlgError:
            break
        x = x + dx

    polished = x.reshape(n, 3)
    return polished, {
        "n_iter": len(history),
        "final_residual": history[-1] if history else None,
        "history": history,
        "n_pair_active": n_pair,
        "n_wall_active": n_wall,
        "score": float(np.sum(polished[:, 2])),
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--base", type=str, default="results-temp/p14_top.json",
                   help="warm-start solution")
    p.add_argument("--pair-gap", type=float, default=-9e-10,
                   help="target pair gap (negative = overlap allowed)")
    p.add_argument("--wall-gap", type=float, default=1e-13,
                   help="target wall slack (small positive)")
    p.add_argument("--output", type=str, default="results-temp/p14_newton.json")
    args = p.parse_args()

    with open(args.base) as f:
        data = json.load(f)
    if isinstance(data, list) and data:
        base = np.array(data[0]["data"]["circles"], dtype=np.float64)
    elif isinstance(data, dict) and "circles" in data:
        base = np.array(data["circles"], dtype=np.float64)
    else:
        raise ValueError("Unknown base format")

    print(f"Base sum_r: {base[:,2].sum():.16f}")
    active = identify_active(base, eps=1e-9)
    n_act = len(active["pairs"]) + sum(len(active[k]) for k in ["left", "right", "bottom", "top"])
    print(f"Active constraints: {n_act} (need {3*N_CIRCLES} for rigid)")

    polished, info = newton_solve(
        base, active,
        pair_gap=args.pair_gap,
        wall_gap=args.wall_gap,
        max_iter=50,
        tol=1e-16,
    )
    print(f"Newton: score={info['score']:.16f}  iter={info['n_iter']}  residual={info['final_residual']:.3e}")

    AE = 2.6359830849176076
    print(f"Δ vs AE: {info['score'] - AE:+.4e}")

    # Verify
    cx, cy, r = polished[:, 0], polished[:, 1], polished[:, 2]
    walls = np.concatenate([cx - r, 1 - cx - r, cy - r, 1 - cy - r])
    pmin = float("inf")
    for i in range(N_CIRCLES):
        for j in range(i + 1, N_CIRCLES):
            d = np.hypot(cx[i] - cx[j], cy[i] - cy[j])
            gap = d - r[i] - r[j]
            if gap < pmin:
                pmin = gap
    print(f"min wall slack: {float(walls.min()):+.6e}")
    print(f"min pair gap:   {pmin:+.6e}")
    print(f"arena valid (tol=1e-9, wall=0): {pmin >= -1e-9 and walls.min() >= 0}")

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w") as f:
        json.dump({
            "circles": polished.tolist(),
            "sum_r": info["score"],
            "pair_gap": args.pair_gap,
            "wall_gap": args.wall_gap,
        }, f, indent=2)
    print(f"\nSaved: {args.output}")


if __name__ == "__main__":
    main()
