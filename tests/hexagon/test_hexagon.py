"""Tests for the hexagon packing evaluator (Problem 17).

Verifies that our local evaluator correctly scores hexagon-in-hexagon packing
solutions. Covers: geometry helpers, overlap detection (SAT), containment,
input validation, and cross-validation against known arena solutions.
"""

import json
import pathlib

import numpy as np
import pytest
from einstein.hexagon import (
    evaluate,
    hexagon_vertices,
    polygon_contained,
    polygons_overlap,
)

_SOLUTION_FILE = (
    pathlib.Path(__file__).parent.parent.parent
    / "results" / "problem-17-hexagon" / "solution.json"
)
_solution = json.loads(_SOLUTION_FILE.read_text()) if _SOLUTION_FILE.exists() else None

# ---------------------------------------------------------------------------
# Geometry helpers
# ---------------------------------------------------------------------------


class TestHexagonVertices:
    """Vertex generation for regular hexagons."""

    def test_unit_hexagon_no_rotation(self):
        verts = hexagon_vertices(0, 0, 0, side=1.0)
        assert verts.shape == (6, 2)
        # All vertices at distance 1 from center
        dists = np.sqrt(verts[:, 0] ** 2 + verts[:, 1] ** 2)
        np.testing.assert_allclose(dists, 1.0, atol=1e-12)

    def test_vertex_count(self):
        verts = hexagon_vertices(3.0, -2.0, 45.0, side=2.0)
        assert verts.shape == (6, 2)

    def test_center_offset(self):
        cx, cy = 5.0, -3.0
        verts = hexagon_vertices(cx, cy, 0, side=1.0)
        center = verts.mean(axis=0)
        np.testing.assert_allclose(center, [cx, cy], atol=1e-12)

    def test_rotation_preserves_distances(self):
        cx, cy, side = 1.0, 2.0, 1.5
        v0 = hexagon_vertices(cx, cy, 0, side)
        v45 = hexagon_vertices(cx, cy, 45, side)
        d0 = np.sqrt((v0[:, 0] - cx) ** 2 + (v0[:, 1] - cy) ** 2)
        d45 = np.sqrt((v45[:, 0] - cx) ** 2 + (v45[:, 1] - cy) ** 2)
        np.testing.assert_allclose(d0, side, atol=1e-12)
        np.testing.assert_allclose(d45, side, atol=1e-12)

    def test_60deg_rotation_permutes_vertices(self):
        """Rotating 60° should produce same vertex set (permuted)."""
        v0 = hexagon_vertices(0, 0, 0, side=1.0)
        v60 = hexagon_vertices(0, 0, 60, side=1.0)
        # Each vertex in v60 should be close to some vertex in v0
        for v in v60:
            dists = np.sqrt(np.sum((v0 - v) ** 2, axis=1))
            assert np.min(dists) < 1e-12


# ---------------------------------------------------------------------------
# Overlap detection (SAT)
# ---------------------------------------------------------------------------


class TestPolygonsOverlap:
    """Separating Axis Theorem for convex polygon overlap."""

    def test_coincident_hexagons_overlap(self):
        v = hexagon_vertices(0, 0, 0, side=1.0)
        assert polygons_overlap(v, v) is True

    def test_far_apart_no_overlap(self):
        v1 = hexagon_vertices(0, 0, 0, side=1.0)
        v2 = hexagon_vertices(100, 100, 0, side=1.0)
        assert polygons_overlap(v1, v2) is False

    def test_slightly_separated(self):
        """Two unit hexagons with centers 3 apart (flat-to-flat ~sqrt(3) < 3)."""
        v1 = hexagon_vertices(0, 0, 0, side=1.0)
        v2 = hexagon_vertices(3.0, 0, 0, side=1.0)
        assert polygons_overlap(v1, v2) is False

    def test_overlapping_close_hexagons(self):
        """Two unit hexagons with centers 1.0 apart must overlap."""
        v1 = hexagon_vertices(0, 0, 0, side=1.0)
        v2 = hexagon_vertices(1.0, 0, 0, side=1.0)
        assert polygons_overlap(v1, v2) is True

    def test_rotated_overlap(self):
        """Overlapping pair with different rotations."""
        v1 = hexagon_vertices(0, 0, 0, side=1.0)
        v2 = hexagon_vertices(0.5, 0.5, 30, side=1.0)
        assert polygons_overlap(v1, v2) is True


# ---------------------------------------------------------------------------
# Containment
# ---------------------------------------------------------------------------


class TestPolygonContained:
    """Check that inner polygon is fully inside outer polygon."""

    def test_small_inside_large(self):
        inner = hexagon_vertices(0, 0, 0, side=1.0)
        outer = hexagon_vertices(0, 0, 0, side=5.0)
        assert polygon_contained(inner, outer) is True

    def test_same_size_same_center_same_angle(self):
        """Identical hexagons: boundary touching, should be contained."""
        v = hexagon_vertices(0, 0, 0, side=1.0)
        assert polygon_contained(v, v) is True

    def test_shifted_outside(self):
        inner = hexagon_vertices(10, 10, 0, side=1.0)
        outer = hexagon_vertices(0, 0, 0, side=2.0)
        assert polygon_contained(inner, outer) is False

    def test_partially_outside(self):
        """Inner hexagon straddles outer boundary."""
        inner = hexagon_vertices(1.5, 0, 0, side=1.0)
        outer = hexagon_vertices(0, 0, 0, side=2.0)
        assert polygon_contained(inner, outer) is False


# ---------------------------------------------------------------------------
# Full evaluator
# ---------------------------------------------------------------------------


class TestEvaluateConstraints:
    """Input validation — reject bad inputs."""

    def test_missing_hexagons_key(self):
        data = {"outer_side_length": 5, "outer_center": [0, 0], "outer_angle_deg": 0}
        with pytest.raises((KeyError, AssertionError)):
            evaluate(data)

    def test_wrong_hexagon_count(self):
        data = {
            "hexagons": [[0, 0, 0]] * 11,
            "outer_side_length": 10,
            "outer_center": [0, 0],
            "outer_angle_deg": 0,
        }
        with pytest.raises(AssertionError, match="12"):
            evaluate(data)

    def test_nan_in_hexagons(self):
        hexs = [[0, 0, 0]] * 12
        hexs[0] = [float("nan"), 0, 0]
        data = {
            "hexagons": hexs,
            "outer_side_length": 10,
            "outer_center": [0, 0],
            "outer_angle_deg": 0,
        }
        with pytest.raises(AssertionError, match="NaN"):
            evaluate(data)


class TestEvaluateScoring:
    """Scoring correctness for known configurations."""

    def _widely_spaced_packing(self, outer_side=20.0):
        """12 hexagons in a grid, far apart inside a huge outer hexagon."""
        hexagons = []
        for i in range(4):
            for j in range(3):
                cx = -6.0 + i * 4.0
                cy = -4.0 + j * 4.0
                hexagons.append([cx, cy, 0])
        return {
            "hexagons": hexagons,
            "outer_side_length": outer_side,
            "outer_center": [0, 0],
            "outer_angle_deg": 0,
        }

    def test_valid_packing_returns_side_length(self):
        data = self._widely_spaced_packing(20.0)
        score = evaluate(data)
        assert score == pytest.approx(20.0, abs=1e-6)

    def test_smaller_valid_packing(self):
        data = self._widely_spaced_packing(25.0)
        score = evaluate(data)
        assert score == pytest.approx(25.0, abs=1e-6)

    def test_overlap_incurs_penalty(self):
        """All 12 hexagons at same position → overlap penalty."""
        data = {
            "hexagons": [[0, 0, 0]] * 12,
            "outer_side_length": 5.0,
            "outer_center": [0, 0],
            "outer_angle_deg": 0,
        }
        score = evaluate(data)
        assert score > 100  # large penalty

    def test_containment_violation_incurs_penalty(self):
        """Hexagons outside the outer container."""
        hexagons = [[100 + i * 5, 0, 0] for i in range(12)]
        data = {
            "hexagons": hexagons,
            "outer_side_length": 2.0,
            "outer_center": [0, 0],
            "outer_angle_deg": 0,
        }
        score = evaluate(data)
        assert score > 100  # large penalty

    @pytest.mark.skipif(_solution is None, reason="results/problem-17-hexagon/solution.json not found")
    def test_sota_solution_valid(self):
        """Known solution should return its outer_side_length."""
        score = evaluate(_solution)
        assert score == pytest.approx(_solution["outer_side_length"], abs=1e-6)


class TestEvaluateProperties:
    """Mathematical properties of the scoring function."""

    @pytest.mark.skipif(_solution is None, reason="results/problem-17-hexagon/solution.json not found")
    def test_deterministic(self):
        s1 = evaluate(_solution)
        s2 = evaluate(_solution)
        assert s1 == s2
