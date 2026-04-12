"""Arena-tolerance-exploiting polisher for Circles in Rectangle (n=21).

Unlike the strict polisher (polish.py), this allows configurable:
  - overlap tolerance (arena accepts overlaps up to ~1e-9)
  - perimeter slack (arena accepts perimeter slightly > 4)

Variables: [cx_1, cy_1, r_1, ..., cx_21, cy_21, r_21, w, h]  (65 total)
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

from einstein.circles_rectangle.evaluator import N_CIRCLES, evaluate_verbose

RESULTS_DIR = Path("results/problem-17-circles-rectangle")


def _unpack(x: np.ndarray) -> tuple[np.ndarray, float, float]:
    circles = x[: 3 * N_CIRCLES].reshape(N_CIRCLES, 3)
    w = float(x[3 * N_CIRCLES])
    h = float(x[3 * N_CIRCLES + 1])
    return circles, w, h


def _pack(circles: np.ndarray, w: float, h: float) -> np.ndarray:
    out = np.empty(3 * N_CIRCLES + 2)
    out[: 3 * N_CIRCLES] = circles.flatten()
    out[3 * N_CIRCLES] = w
    out[3 * N_CIRCLES + 1] = h
    return out


def _objective(x: np.ndarray) -> float:
    return -float(np.sum(x[2 : 3 * N_CIRCLES : 3]))


def _objective_jac(x: np.ndarray) -> np.ndarray:
    g = np.zeros_like(x)
    g[2 : 3 * N_CIRCLES : 3] = -1.0
    return g


def _wall_constraints(x: np.ndarray) -> np.ndarray:
    """Wall slacks >= 0."""
    circles, w, h = _unpack(x)
    cx, cy, r = circles[:, 0], circles[:, 1], circles[:, 2]
    return np.concatenate([cx - r, w - cx - r, cy - r, h - cy - r])


def _pair_constraints(x: np.ndarray, overlap_tol: float) -> np.ndarray:
    """Disjointness with tolerance: d(i,j) - r_i - r_j + overlap_tol >= 0."""
    circles, _, _ = _unpack(x)
    n = N_CIRCLES
    out = np.empty(n * (n - 1) // 2)
    k = 0
    for i in range(n):
        for j in range(i + 1, n):
            dx = circles[i, 0] - circles[j, 0]
            dy = circles[i, 1] - circles[j, 1]
            out[k] = np.sqrt(dx * dx + dy * dy) - circles[i, 2] - circles[j, 2] + overlap_tol
            k += 1
    return out


def _perimeter_constraint(x: np.ndarray, half_perim_slack: float) -> np.ndarray:
    """w + h <= 2 + half_perim_slack."""
    w = x[3 * N_CIRCLES]
    h = x[3 * N_CIRCLES + 1]
    return np.array([2.0 + half_perim_slack - w - h])


def arena_polish(
    initial_circles: np.ndarray,
    initial_w: float | None = None,
    initial_h: float | None = None,
    overlap_tol: float = 9.5e-10,
    half_perim_slack: float = 1e-9,
    maxiter: int = 2000,
    ftol: float = 1e-18,
    verbose: bool = False,
) -> tuple[np.ndarray, float, float, dict]:
    """Polish with arena-tolerance exploitation.

    Args:
        overlap_tol: allowed overlap per pair (arena accepts ~1e-9)
        half_perim_slack: w+h can exceed 2 by this much (perimeter excess = 2*slack)

    Returns:
        (circles, w, h, info)
    """
    circles = np.array(initial_circles, dtype=np.float64).copy()
    assert circles.shape == (N_CIRCLES, 3)

    if initial_w is None or initial_h is None:
        xs, ys, rs = circles[:, 0], circles[:, 1], circles[:, 2]
        xmin = float((xs - rs).min())
        ymin = float((ys - rs).min())
        circles[:, 0] -= xmin
        circles[:, 1] -= ymin
        initial_w = float((circles[:, 0] + circles[:, 2]).max())
        initial_h = float((circles[:, 1] + circles[:, 2]).max())

    x0 = _pack(circles, initial_w, initial_h)

    constraints = [
        {"type": "ineq", "fun": _wall_constraints},
        {"type": "ineq", "fun": _pair_constraints, "args": (overlap_tol,)},
        {"type": "ineq", "fun": _perimeter_constraint, "args": (half_perim_slack,)},
    ]

    # Bounds: positive radii, reasonable w/h
    bounds = [(0.0, 2.0)] * (3 * N_CIRCLES) + [(0.01, 1.99), (0.01, 1.99)]

    result = minimize(
        _objective,
        x0,
        jac=_objective_jac,
        constraints=constraints,
        bounds=bounds,
        method="SLSQP",
        options={"ftol": ftol, "maxiter": maxiter, "disp": verbose},
    )

    polished, w, h = _unpack(result.x)
    score = float(np.sum(polished[:, 2]))
    info = {
        "score": score,
        "w": w,
        "h": h,
        "perimeter": 2.0 * (w + h),
        "n_iter": int(result.nit) if hasattr(result, "nit") else None,
        "success": bool(result.success),
        "message": str(result.message),
        "overlap_tol": overlap_tol,
        "half_perim_slack": half_perim_slack,
    }
    return polished, w, h, info


def main():
    # Load current #1 solution as warm start
    with open(RESULTS_DIR / "leaderboard-top5.json") as f:
        solutions = json.load(f)

    sota = solutions[0]
    sota_score = sota["score"]
    circles_init = np.array(sota["data"]["circles"])
    print(f"Warm-start: {sota['agentName']} @ {sota_score:.16f}")

    # Translate to origin
    xs, ys, rs = circles_init[:, 0], circles_init[:, 1], circles_init[:, 2]
    xmin = (xs - rs).min()
    ymin = (ys - rs).min()
    circles_init[:, 0] -= xmin
    circles_init[:, 1] -= ymin
    w0 = float((circles_init[:, 0] + circles_init[:, 2]).max())
    h0 = float((circles_init[:, 1] + circles_init[:, 2]).max())
    print(f"Initial w={w0:.16f} h={h0:.16f} perim={2*(w0+h0):.16f}")

    # Polish with arena-safe tolerances
    circles, w, h, info = arena_polish(
        circles_init, w0, h0, maxiter=3000, ftol=1e-18,
    )
    score = info["score"]
    sol = {"circles": circles.tolist()}
    diag = evaluate_verbose(sol)

    print(f"\nPolished score: {score:.16f}  (Δ vs SOTA: {score - sota_score:+.2e})")
    print(f"  worst_overlap: {diag['worst_overlap']:.4e}")
    print(f"  perimeter:     {diag['perimeter']:.16f}")

    if score > sota_score:
        out_path = RESULTS_DIR / "solution-arena-polish.json"
        with open(out_path, "w") as f:
            json.dump(sol, f, indent=2)
        print(f"\nSaved to {out_path}")
    else:
        print("\nDid not beat SOTA. Need different approach.")


if __name__ == "__main__":
    main()
