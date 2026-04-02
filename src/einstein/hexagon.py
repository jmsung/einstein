"""Evaluator for Hexagon Packing in a Hexagon (Problem 17).

Pack 12 disjoint unit regular hexagons inside a larger regular hexagon,
minimizing the outer hexagon's side length. Uses the Separating Axis Theorem
for overlap detection and vertex-in-polygon for containment.

Score = outer_side_length + penalty_per_violation * num_violations.
"""

import numpy as np


def hexagon_vertices(
    cx: float, cy: float, angle_deg: float, side: float = 1.0
) -> np.ndarray:
    """Compute 6 vertices of a regular hexagon.

    Args:
        cx, cy: Center coordinates.
        angle_deg: Rotation angle in degrees (counterclockwise).
        side: Side length (= circumradius).

    Returns:
        (6, 2) array of vertex coordinates.
    """
    angles = np.deg2rad(angle_deg + np.arange(6) * 60)
    xs = cx + side * np.cos(angles)
    ys = cy + side * np.sin(angles)
    return np.column_stack([xs, ys])


def _edge_normals(vertices: np.ndarray) -> np.ndarray:
    """Outward-facing edge normals for a convex polygon.

    Returns:
        (n, 2) array of unit normal vectors.
    """
    n = len(vertices)
    edges = np.roll(vertices, -1, axis=0) - vertices
    normals = np.column_stack([edges[:, 1], -edges[:, 0]])
    lengths = np.sqrt(normals[:, 0] ** 2 + normals[:, 1] ** 2)
    return normals / lengths[:, np.newaxis]


def _project(vertices: np.ndarray, axis: np.ndarray) -> tuple[float, float]:
    """Project polygon vertices onto an axis; return (min, max)."""
    dots = vertices @ axis
    return float(dots.min()), float(dots.max())


def polygons_overlap(verts_a: np.ndarray, verts_b: np.ndarray) -> bool:
    """Separating Axis Theorem overlap test for two convex polygons.

    Returns True if the interiors overlap (touching boundaries = no overlap).
    """
    for verts in (verts_a, verts_b):
        normals = _edge_normals(verts)
        for axis in normals:
            min_a, max_a = _project(verts_a, axis)
            min_b, max_b = _project(verts_b, axis)
            if max_a <= min_b or max_b <= min_a:
                return False
    return True


def polygon_contained(
    inner: np.ndarray, outer: np.ndarray, tol: float = 1e-9
) -> bool:
    """Check if inner polygon is fully contained within outer convex polygon.

    Uses the half-plane test: inner is contained iff every inner vertex is on
    the inward side of every edge of the outer polygon.
    """
    n = len(outer)
    for i in range(n):
        j = (i + 1) % n
        edge = outer[j] - outer[i]
        # Inward normal (pointing into the polygon)
        normal = np.array([-edge[1], edge[0]])
        # Reference: centroid of outer should be on the inward side
        centroid = outer.mean(axis=0)
        if normal @ (centroid - outer[i]) < 0:
            normal = -normal
        # Check all inner vertices
        for v in inner:
            if normal @ (v - outer[i]) < -tol:
                return False
    return True


def evaluate(data: dict, penalty: float = 1000.0) -> float:
    """Score a hexagon packing solution.

    Args:
        data: Solution dict with keys:
            - hexagons: list of 12 × [cx, cy, angle_deg]
            - outer_side_length: float
            - outer_center: [x, y]
            - outer_angle_deg: float
        penalty: Penalty added per violation (overlap or containment).

    Returns:
        outer_side_length + penalty * num_violations.
    """
    hexagons = data["hexagons"]
    assert len(hexagons) == 12, f"Expected 12 hexagons, got {len(hexagons)}"

    outer_side = float(data["outer_side_length"])
    outer_center = data["outer_center"]
    outer_angle = float(data["outer_angle_deg"])

    # Validate no NaN
    for i, h in enumerate(hexagons):
        for val in h:
            assert not np.isnan(val), f"NaN in hexagon {i}"
    assert not np.isnan(outer_side), "NaN in outer_side_length"

    # Compute all inner hexagon vertices
    inner_verts = []
    for cx, cy, angle in hexagons:
        inner_verts.append(hexagon_vertices(cx, cy, angle, side=1.0))

    # Compute outer hexagon vertices
    outer_verts = hexagon_vertices(
        outer_center[0], outer_center[1], outer_angle, side=outer_side
    )

    violations = 0

    # Check pairwise overlap (66 pairs for 12 hexagons)
    for i in range(12):
        for j in range(i + 1, 12):
            if polygons_overlap(inner_verts[i], inner_verts[j]):
                violations += 1

    # Check containment
    for i in range(12):
        if not polygon_contained(inner_verts[i], outer_verts):
            violations += 1

    return outer_side + penalty * violations
