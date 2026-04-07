"""Arena-matching evaluator for Problem 17 (id 18): Circles in a Rectangle (n=21).

Score = Σ r_i. Maximize.

Constraints (from arena spec / AlphaEvolve repo notebook B.13):
  - exactly 21 circles
  - circles disjoint: ||c_i - c_j|| >= r_i + r_j
  - minimum circumscribing rectangle has perimeter <= 4 (i.e. w + h <= 2)

Note on tolerance: the AlphaEvolve published verifier uses strict `>=`,
but the arena's actual verifier accepts the leaderboard #1 which has
44 float64-noise overlaps up to 7.5e-12. The arena must therefore allow
small numerical violations. We use OVERLAP_TOL=1e-9 by default, well
above the observed noise floor, and PERIMETER_TOL=1e-12.
"""

from __future__ import annotations

import itertools

import numpy as np

N_CIRCLES = 21
PERIMETER_BOUND = 4.0  # equivalent to w + h <= 2
OVERLAP_TOL = 1e-9     # max accepted overlap (float64 noise)
PERIMETER_TOL = 1e-12  # numerical slack on perimeter


def minimum_circumscribing_rectangle(circles: np.ndarray) -> tuple[float, float]:
    """Width and height of the minimum bounding rectangle (axis-aligned)."""
    min_x = float(np.min(circles[:, 0] - circles[:, 2]))
    max_x = float(np.max(circles[:, 0] + circles[:, 2]))
    min_y = float(np.min(circles[:, 1] - circles[:, 2]))
    max_y = float(np.max(circles[:, 1] + circles[:, 2]))
    return max_x - min_x, max_y - min_y


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
    """Arena verifier — returns sum of radii, raises if invalid.

    Args:
        data: dict with key "circles" → list/array of 21 [x, y, r] triples.
        tol: max accepted overlap (default 1e-9 — matches arena tolerance).

    Returns:
        Σ r_i if valid; raises AssertionError otherwise.
    """
    circles = np.array(data["circles"], dtype=np.float64)
    if circles.ndim != 2 or circles.shape != (N_CIRCLES, 3):
        raise ValueError(f"Expected shape ({N_CIRCLES}, 3), got {circles.shape}")
    verify_circles_disjoint(circles, tol=tol)
    width, height = minimum_circumscribing_rectangle(circles)
    perimeter = 2.0 * (width + height)
    if perimeter > PERIMETER_BOUND + PERIMETER_TOL:
        raise AssertionError(
            f"Rectangle perimeter {perimeter} > {PERIMETER_BOUND}"
        )
    return float(np.sum(circles[:, 2]))


def evaluate_verbose(data: dict, eps: float = 1e-9) -> dict:
    """Score plus diagnostics: width, height, perimeter slack, contact graph."""
    circles = np.array(data["circles"], dtype=np.float64)
    width, height = minimum_circumscribing_rectangle(circles)
    perimeter = 2.0 * (width + height)
    slack = PERIMETER_BOUND - perimeter

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

    # Wall contacts
    xmin = float(np.min(circles[:, 0] - circles[:, 2]))
    xmax = float(np.max(circles[:, 0] + circles[:, 2]))
    ymin = float(np.min(circles[:, 1] - circles[:, 2]))
    ymax = float(np.max(circles[:, 1] + circles[:, 2]))
    left = [i for i in range(n) if circles[i, 0] - circles[i, 2] - xmin < eps]
    right = [i for i in range(n) if xmax - circles[i, 0] - circles[i, 2] < eps]
    bottom = [i for i in range(n) if circles[i, 1] - circles[i, 2] - ymin < eps]
    top = [i for i in range(n) if ymax - circles[i, 1] - circles[i, 2] < eps]

    return {
        "score": float(np.sum(circles[:, 2])),
        "width": width,
        "height": height,
        "perimeter": perimeter,
        "slack": slack,
        "n_inter_contacts": len(cc_pairs),
        "worst_overlap": worst_overlap,
        "wall_contacts": {
            "left": left, "right": right, "bottom": bottom, "top": top,
        },
        "contact_pairs": cc_pairs,
    }
