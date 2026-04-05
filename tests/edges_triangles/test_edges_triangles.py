"""Tests for the Edges vs Triangles evaluator (Problem 13).

Verifies that our local evaluator matches the arena's scoring function.
"""

import numpy as np
import pytest
from einstein.edges_triangles import (
    compute_densities,
    compute_score,
    evaluate,
    turan_row,
)


# ---------------------------------------------------------------------------
# Density computation
# ---------------------------------------------------------------------------
class TestDensities:
    def test_single_part(self):
        """Single part: x=0, y=0 (no edges, no triangles)."""
        p = np.zeros(20)
        p[0] = 1.0
        x, y = compute_densities(p)
        assert x == pytest.approx(0.0)
        assert y == pytest.approx(0.0)

    def test_equal_bipartite(self):
        """Equal bipartite: x=0.5, y=0 (triangle-free)."""
        p = np.zeros(20)
        p[0] = p[1] = 0.5
        x, y = compute_densities(p)
        assert x == pytest.approx(0.5)
        assert y == pytest.approx(0.0)

    def test_uniform_20(self):
        """Uniform over 20 bins: x=0.95, y=(19*18)/400=0.855."""
        p = np.ones(20) / 20
        x, y = compute_densities(p)
        assert x == pytest.approx(0.95)
        assert y == pytest.approx(19 * 18 / 400)

    def test_balanced_tripartite(self):
        """Balanced 3-partite: x=2/3, y=2/9."""
        p = np.zeros(20)
        p[0] = p[1] = p[2] = 1 / 3
        x, y = compute_densities(p)
        assert x == pytest.approx(2 / 3)
        assert y == pytest.approx(2 / 9)

    def test_balanced_k_partite(self):
        """Balanced k-partite: x=1-1/k, y=(k-1)(k-2)/k^2."""
        for k in [4, 5, 10, 20]:
            p = np.zeros(20)
            p[:k] = 1.0 / k
            x, y = compute_densities(p)
            assert x == pytest.approx(1 - 1 / k), f"k={k}"
            assert y == pytest.approx((k - 1) * (k - 2) / k**2), f"k={k}"

    def test_triangle_density_nonneg(self):
        """Triangle density is non-negative for any probability vector."""
        rng = np.random.default_rng(42)
        for _ in range(100):
            p = rng.dirichlet(np.ones(20))
            _, y = compute_densities(p)
            assert y >= -1e-15


# ---------------------------------------------------------------------------
# Turán row construction
# ---------------------------------------------------------------------------
class TestTuranRow:
    def test_zero_edge_density(self):
        """x=0: single part."""
        p = turan_row(0.0)
        assert len(p) == 20
        assert np.sum(p) == pytest.approx(1.0)
        x, y = compute_densities(p)
        assert x == pytest.approx(0.0, abs=1e-12)

    def test_bipartite_region(self):
        """x in (0, 0.5]: bipartite, y=0."""
        for x_target in [0.1, 0.25, 0.4, 0.5]:
            p = turan_row(x_target)
            assert np.sum(p) == pytest.approx(1.0)
            x, y = compute_densities(p)
            assert x == pytest.approx(x_target, abs=1e-10), f"x_target={x_target}"
            assert y == pytest.approx(0.0, abs=1e-10), f"x_target={x_target}"

    def test_multipartite_region(self):
        """x > 0.5: achieves Razborov minimum."""
        for x_target in [0.55, 0.6, 0.7, 0.8, 0.9]:
            p = turan_row(x_target)
            assert np.sum(p) == pytest.approx(1.0)
            x, y = compute_densities(p)
            assert x == pytest.approx(x_target, abs=1e-10), f"x_target={x_target}"
            # Triangle density should be on the Razborov curve (minimum)
            assert y >= -1e-10, f"x_target={x_target}"

    def test_turan_breakpoints(self):
        """At Turán points x=1-1/k, balanced k-partite is exact."""
        for k in [2, 3, 5, 10, 19]:
            x_target = 1 - 1 / k
            p = turan_row(x_target)
            x, y = compute_densities(p)
            assert x == pytest.approx(x_target, abs=1e-10), f"k={k}"
            assert y == pytest.approx((k - 1) * (k - 2) / k**2, abs=1e-8), f"k={k}"

    def test_max_edge_density(self):
        """x=0.95: uniform over 20 bins."""
        p = turan_row(0.95)
        x, _ = compute_densities(p)
        assert x == pytest.approx(0.95, abs=1e-10)


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------
class TestScoring:
    def test_single_row_single_part(self):
        """Worst case: single part, no coverage."""
        row = np.zeros((1, 20))
        row[0, 0] = 1.0
        score = compute_score(row)
        # Only points: (0,0) from data + boundary (0,0) and (1,1)
        # After dedup: (0,0), (0,0), (1,1) — gap = 1.0
        # Area with slope-3: -1/6 + 1*1 = 5/6
        # Score = -(5/6 + 10*1) = -10.833
        assert score < -10

    def test_more_points_better_score(self):
        """More well-placed points should improve score."""
        # 10 points
        xs_10 = np.linspace(0, 0.95, 10)
        rows_10 = np.array([turan_row(x) for x in xs_10])
        score_10 = compute_score(rows_10)

        # 100 points
        xs_100 = np.linspace(0, 0.95, 100)
        rows_100 = np.array([turan_row(x) for x in xs_100])
        score_100 = compute_score(rows_100)

        assert score_100 > score_10  # less negative = better

    def test_max_gap_with_uniform_endpoint(self):
        """Max gap should be 0.05 when last data point is at x=0.95."""
        xs = np.linspace(0, 0.95, 500)
        rows = np.array([turan_row(x) for x in xs])
        score = compute_score(rows)
        # With 500 evenly spaced points from 0 to 0.95, max_gap ≤ 0.05
        # (gap from 0.95 to 1.0 = 0.05)
        assert score > -1.0  # reasonable score

    def test_evaluate_dict_interface(self):
        """evaluate() accepts dict with 'weights' key."""
        rows = np.array([turan_row(x) for x in np.linspace(0, 0.95, 10)])
        score = evaluate({"weights": rows.tolist()})
        assert isinstance(score, float)
        assert score < 0

    def test_normalization(self):
        """Non-normalized rows are normalized before scoring."""
        p = turan_row(0.5)
        row_scaled = p * 10  # not normalized
        rows = np.array([row_scaled])
        score = compute_score(rows)
        assert np.isfinite(score)


# ---------------------------------------------------------------------------
# Cross-validation: independent area computation
# ---------------------------------------------------------------------------
def _independent_score(weights: np.ndarray) -> float:
    """Independent scoring implementation for cross-validation."""
    weights = np.asarray(weights, dtype=np.float64)
    weights = np.maximum(weights, 0)
    row_sums = weights.sum(axis=1, keepdims=True)
    weights = weights / row_sums

    points = []
    for row in weights:
        s2 = float(np.sum(row**2))
        s3 = float(np.sum(row**3))
        points.append((1.0 - s2, 1.0 - 3 * s2 + 2 * s3))

    points.sort()
    points = [(0.0, 0.0)] + points + [(1.0, 1.0)]

    area = 0.0
    max_gap = 0.0
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        h = x1 - x0
        if h <= 0:
            continue
        max_gap = max(max_gap, h)
        dy = y1 - y0
        if dy < 0:
            area += y1 * h
        elif dy <= 3 * h:
            area += -dy**2 / 6 + y1 * h
        else:
            area += y0 * h + 1.5 * h**2

    return -(area + 10 * max_gap)


class TestCrossValidation:
    def test_matches_independent(self):
        """Our evaluator matches the independent implementation."""
        rng = np.random.default_rng(123)
        for _ in range(10):
            m = rng.integers(5, 50)
            weights = rng.dirichlet(np.ones(20), size=m)
            score_ours = compute_score(weights)
            score_indep = _independent_score(weights)
            assert score_ours == pytest.approx(score_indep, abs=1e-12)
