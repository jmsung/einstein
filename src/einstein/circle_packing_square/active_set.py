"""Active-set Newton polisher for Circle Packing in a Square (n=26).

Given a configuration near a fully-rigid local maximum (DOF == active
constraints), solve the active-constraint equations exactly via
Newton's method. Quadratic convergence to machine precision (~1e-15).

This is the canonical "polish to the float64 ceiling" technique used
when SLSQP plateaus at 1e-9 due to its line-search precision.

The active set approach works as follows:
  1. Identify which constraints are tight at the current solution.
  2. Form the equation system g_active(x) = 0 (one equation per
     active constraint).
  3. Newton iterate: solve J Δx = −g, set x ← x + Δx, repeat.
  4. After convergence, the score is the basin's true float64 value.
"""

from __future__ import annotations

import numpy as np

from .evaluator import N_CIRCLES, SQUARE_SIDE


def _circle_arrays(x: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    cx = x[0::3]
    cy = x[1::3]
    r = x[2::3]
    return cx, cy, r


def identify_active(circles: np.ndarray, eps: float = 1e-7) -> dict:
    """Find tight contacts (pair distances and wall slacks within eps of 0)."""
    n = circles.shape[0]
    cx, cy, r = circles[:, 0], circles[:, 1], circles[:, 2]

    pair_contacts: list[tuple[int, int]] = []
    for i in range(n):
        for j in range(i + 1, n):
            d = np.hypot(cx[i] - cx[j], cy[i] - cy[j])
            gap = d - r[i] - r[j]
            if abs(gap) < eps:
                pair_contacts.append((i, j))

    left = [i for i in range(n) if abs(cx[i] - r[i]) < eps]
    right = [i for i in range(n) if abs(SQUARE_SIDE - cx[i] - r[i]) < eps]
    bottom = [i for i in range(n) if abs(cy[i] - r[i]) < eps]
    top = [i for i in range(n) if abs(SQUARE_SIDE - cy[i] - r[i]) < eps]

    return {
        "pairs": pair_contacts,
        "left": left,
        "right": right,
        "bottom": bottom,
        "top": top,
    }


def _residual(x: np.ndarray, active: dict) -> np.ndarray:
    """Active-constraint residual vector g(x). Want g(x) = 0."""
    cx, cy, r = _circle_arrays(x)
    pairs = active["pairs"]
    out = []
    # pair contacts: ‖c_i - c_j‖ - r_i - r_j = 0
    for i, j in pairs:
        d = np.hypot(cx[i] - cx[j], cy[i] - cy[j])
        out.append(d - r[i] - r[j])
    # wall contacts
    for i in active["left"]:
        out.append(cx[i] - r[i])
    for i in active["right"]:
        out.append(SQUARE_SIDE - cx[i] - r[i])
    for i in active["bottom"]:
        out.append(cy[i] - r[i])
    for i in active["top"]:
        out.append(SQUARE_SIDE - cy[i] - r[i])
    return np.array(out, dtype=np.float64)


def _residual_jac(x: np.ndarray, active: dict) -> np.ndarray:
    """Jacobian of the active-constraint residual w.r.t. x = [cx,cy,r,...]."""
    n = N_CIRCLES
    cx, cy, r = _circle_arrays(x)
    rows = []
    pairs = active["pairs"]
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
    for i in active["left"]:
        row = np.zeros(3 * n)
        row[3 * i + 0] = 1.0
        row[3 * i + 2] = -1.0
        rows.append(row)
    for i in active["right"]:
        row = np.zeros(3 * n)
        row[3 * i + 0] = -1.0
        row[3 * i + 2] = -1.0
        rows.append(row)
    for i in active["bottom"]:
        row = np.zeros(3 * n)
        row[3 * i + 1] = 1.0
        row[3 * i + 2] = -1.0
        rows.append(row)
    for i in active["top"]:
        row = np.zeros(3 * n)
        row[3 * i + 1] = -1.0
        row[3 * i + 2] = -1.0
        rows.append(row)
    return np.array(rows, dtype=np.float64)


def newton_polish(
    initial_circles: np.ndarray,
    active: dict | None = None,
    max_iter: int = 50,
    tol: float = 1e-15,
    eps_active: float = 1e-7,
    verbose: bool = False,
) -> tuple[np.ndarray, dict]:
    """Newton solve of g_active(x) = 0.

    For a fully-rigid local maximum (#active == 3n), the system is square
    and Newton converges quadratically to machine precision.

    For an under-determined system (#active < 3n), uses least-squares step
    (np.linalg.lstsq), which moves toward the constraint manifold but does
    not maximize Σr — call SLSQP first to land in the basin.

    Args:
        initial_circles: shape (n, 3) starting circles.
        active: pre-computed active set (or None to identify from initial).
        max_iter: Newton iterations.
        tol: residual tolerance for convergence.
        eps_active: tolerance for identifying active constraints.
        verbose: print progress.

    Returns:
        (polished_circles, info_dict).
    """
    circles = np.array(initial_circles, dtype=np.float64).copy()
    x = circles.flatten().astype(np.float64)

    if active is None:
        active = identify_active(circles, eps=eps_active)

    n_active = (
        len(active["pairs"])
        + len(active["left"])
        + len(active["right"])
        + len(active["bottom"])
        + len(active["top"])
    )

    history = []
    for it in range(max_iter):
        g = _residual(x, active)
        res = float(np.linalg.norm(g))
        history.append(res)
        if verbose:
            print(f"  iter {it:2d} ‖g‖={res:.3e}")
        if res < tol:
            break
        J = _residual_jac(x, active)
        # Solve J Δx = -g (least-squares if non-square)
        try:
            dx, *_ = np.linalg.lstsq(J, -g, rcond=None)
        except np.linalg.LinAlgError:
            break
        x = x + dx

    polished = x.reshape(N_CIRCLES, 3)
    score = float(np.sum(polished[:, 2]))
    info = {
        "score": score,
        "n_active": n_active,
        "n_iter": len(history),
        "final_residual": history[-1] if history else None,
        "history": history,
    }
    return polished, info
