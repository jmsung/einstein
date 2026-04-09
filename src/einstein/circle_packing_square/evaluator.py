"""Arena-matching evaluator for Problem 14: Circle Packing in a Square (n=26).

Score = Σ r_i. Maximize.

Constraints:
  - exactly 26 circles
  - all inside the unit square: r ≤ cx ≤ 1−r and r ≤ cy ≤ 1−r
  - pairwise disjoint: ‖c_i − c_j‖ ≥ r_i + r_j

Tolerance: arena verifier accepts the leaderboard #1 (AlphaEvolve) which
contains float64-noise overlaps. We use OVERLAP_TOL=1e-9 by default,
matching the band observed on adjacent problems (P17 circles_rectangle).
A strict mode (tol=0) is provided for verifying our submissions.
"""

from __future__ import annotations

import itertools

import numpy as np

N_CIRCLES = 26
SQUARE_SIDE = 1.0
OVERLAP_TOL = 1e-9
WALL_TOL = 1e-9


def verify_inside_square(circles: np.ndarray, tol: float = WALL_TOL) -> None:
    """All circles fully inside [0, 1]^2."""
    cx = circles[:, 0]
    cy = circles[:, 1]
    r = circles[:, 2]
    if np.any(r < -tol):
        raise AssertionError(f"Negative radius: {float(r.min())}")
    left = cx - r
    right = SQUARE_SIDE - (cx + r)
    bottom = cy - r
    top = SQUARE_SIDE - (cy + r)
    worst = float(min(left.min(), right.min(), bottom.min(), top.min()))
    if worst < -tol:
        raise AssertionError(
            f"Circle outside unit square (slack={worst:.3e} < -{tol:.0e})"
        )


def verify_circles_disjoint(circles: np.ndarray, tol: float = OVERLAP_TOL) -> None:
    """Disjointness check — accepts overlaps within ``tol`` (float64 noise)."""
    for c1, c2 in itertools.combinations(circles, 2):
        center_distance = np.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)
        radii_sum = c1[2] + c2[2]
        if center_distance + tol < radii_sum:
            raise AssertionError(
                f"Circles overlap by {radii_sum - center_distance:.3e} > {tol:.0e}: "
                f"{c1.tolist()} and {c2.tolist()}"
            )


def evaluate(data: dict, tol: float = OVERLAP_TOL) -> float:
    """Arena-matching verifier — returns Σ r_i, raises if invalid.

    Args:
        data: dict with key "circles" → list/array of 26 [cx, cy, r] triples.
        tol: max accepted overlap / wall slack (default 1e-9, arena tolerance).

    Returns:
        Σ r_i if valid; raises AssertionError otherwise.
    """
    circles = np.array(data["circles"], dtype=np.float64)
    if circles.ndim != 2 or circles.shape != (N_CIRCLES, 3):
        raise ValueError(f"Expected shape ({N_CIRCLES}, 3), got {circles.shape}")
    verify_inside_square(circles, tol=tol)
    verify_circles_disjoint(circles, tol=tol)
    return float(np.sum(circles[:, 2]))


def evaluate_strict(data: dict) -> float:
    """Strict verifier (tol=0) — for final submission gating."""
    return evaluate(data, tol=0.0)


def evaluate_verbose(data: dict, eps: float = 1e-9) -> dict:
    """Score plus diagnostics: contact graph, wall contacts, worst overlap."""
    circles = np.array(data["circles"], dtype=np.float64)
    n = circles.shape[0]

    cc_pairs: list[tuple[int, int, float]] = []
    worst_overlap = 0.0
    for i in range(n):
        for j in range(i + 1, n):
            d = np.sqrt(
                (circles[i, 0] - circles[j, 0]) ** 2
                + (circles[i, 1] - circles[j, 1]) ** 2
            )
            gap = d - circles[i, 2] - circles[j, 2]
            if gap < worst_overlap:
                worst_overlap = float(gap)
            if abs(gap) < eps:
                cc_pairs.append((i, j, float(gap)))

    cx = circles[:, 0]
    cy = circles[:, 1]
    r = circles[:, 2]
    left = [i for i in range(n) if abs(cx[i] - r[i]) < eps]
    right = [i for i in range(n) if abs(SQUARE_SIDE - cx[i] - r[i]) < eps]
    bottom = [i for i in range(n) if abs(cy[i] - r[i]) < eps]
    top = [i for i in range(n) if abs(SQUARE_SIDE - cy[i] - r[i]) < eps]

    return {
        "score": float(np.sum(r)),
        "n_inter_contacts": len(cc_pairs),
        "worst_overlap": worst_overlap,
        "wall_contacts": {
            "left": left, "right": right, "bottom": bottom, "top": top,
        },
        "contact_pairs": cc_pairs,
    }
