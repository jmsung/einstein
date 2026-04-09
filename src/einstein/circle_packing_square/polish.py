"""High-precision SLSQP polisher for Circle Packing in a Square (n=26).

Maximize Σ r_i subject to:
  - circles inside [0,1]^2: cx_i ± r_i ∈ [0,1], cy_i ± r_i ∈ [0,1]
  - ‖c_i − c_j‖ ≥ r_i + r_j for all i < j

Variables: x = [cx_1, cy_1, r_1, …, cx_26, cy_26, r_26]. 78 variables,
26·4 = 104 wall constraints, C(26,2) = 325 pair constraints.
"""

from __future__ import annotations

from typing import Sequence

import numpy as np
from scipy.optimize import minimize

from .evaluator import N_CIRCLES, SQUARE_SIDE


def _unpack(x: np.ndarray) -> np.ndarray:
    return x.reshape(N_CIRCLES, 3)


def _pack(circles: np.ndarray) -> np.ndarray:
    return circles.flatten().astype(np.float64).copy()


def _objective(x: np.ndarray) -> float:
    return -float(np.sum(x[2::3]))  # − Σ r_i


def _objective_jac(x: np.ndarray) -> np.ndarray:
    g = np.zeros_like(x)
    g[2::3] = -1.0
    return g


def _wall_constraints(x: np.ndarray) -> np.ndarray:
    """Wall slacks ≥ 0 (4 per circle)."""
    c = _unpack(x)
    cx, cy, r = c[:, 0], c[:, 1], c[:, 2]
    return np.concatenate([
        cx - r,                      # left
        SQUARE_SIDE - cx - r,        # right
        cy - r,                      # bottom
        SQUARE_SIDE - cy - r,        # top
    ])


def _pair_constraints(x: np.ndarray, slack: float = 0.0) -> np.ndarray:
    """Disjointness slacks ≥ 0: ‖c_i−c_j‖ − r_i − r_j + slack ≥ 0."""
    c = _unpack(x)
    n = N_CIRCLES
    out = np.empty(n * (n - 1) // 2)
    k = 0
    for i in range(n):
        for j in range(i + 1, n):
            dx = c[i, 0] - c[j, 0]
            dy = c[i, 1] - c[j, 1]
            out[k] = np.sqrt(dx * dx + dy * dy) - c[i, 2] - c[j, 2] + slack
            k += 1
    return out


def _all_constraints(x: np.ndarray, slack: float = 0.0,
                     wall_slack: float | None = None) -> np.ndarray:
    """Combined constraints. ``slack`` applies to pair distances; ``wall_slack``
    (default same as ``slack``) applies to wall constraints. Use a small
    positive ``wall_slack`` to keep walls strictly satisfied while letting
    pairs sit at the arena tolerance band."""
    if wall_slack is None:
        wall_slack = slack
    walls = _wall_constraints(x) - wall_slack  # subtract: forces ≥ wall_slack
    pairs = _pair_constraints(x, slack=slack)
    return np.concatenate([walls, pairs])


def polish(
    initial_circles: np.ndarray | Sequence,
    method: str = "SLSQP",
    maxiter: int = 1000,
    ftol: float = 1e-16,
    overlap_slack: float = 0.0,
    verbose: bool = False,
) -> tuple[np.ndarray, dict]:
    """Polish a circle configuration to a high-precision local maximum.

    Args:
        initial_circles: shape (26, 3) array of [cx, cy, r] triples.
        method: 'SLSQP' or 'trust-constr'.
        maxiter: solver iterations.
        ftol: solver tolerance.
        overlap_slack: tolerated overlap during optimization.
        verbose: print solver output.

    Returns:
        (polished_circles, info_dict).
    """
    circles = np.array(initial_circles, dtype=np.float64).copy()
    assert circles.shape == (N_CIRCLES, 3), f"got {circles.shape}"

    x0 = _pack(circles)

    constraints = [{
        "type": "ineq",
        "fun": _all_constraints,
        "args": (overlap_slack,),
    }]
    bounds = [(0.0, 1.0)] * (3 * N_CIRCLES)

    if method == "SLSQP":
        result = minimize(
            _objective,
            x0,
            jac=_objective_jac,
            constraints=constraints,
            bounds=bounds,
            method="SLSQP",
            options={"ftol": ftol, "maxiter": maxiter, "disp": verbose},
        )
    else:
        from scipy.optimize import NonlinearConstraint
        nlc = NonlinearConstraint(
            lambda x: _all_constraints(x, slack=overlap_slack), 0, np.inf
        )
        result = minimize(
            _objective,
            x0,
            jac=_objective_jac,
            constraints=nlc,
            bounds=bounds,
            method="trust-constr",
            options={
                "xtol": ftol,
                "gtol": ftol,
                "maxiter": maxiter,
                "verbose": 3 if verbose else 0,
            },
        )

    polished = _unpack(result.x)
    score = float(np.sum(polished[:, 2]))
    info = {
        "score": score,
        "n_iter": int(result.nit) if hasattr(result, "nit") else None,
        "success": bool(result.success),
        "message": str(result.message),
    }
    return polished, info
