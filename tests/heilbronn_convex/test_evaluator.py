"""Tests for the Heilbronn Convex (n=14) evaluator.

Verifies that:
1. `arena_score` is a byte-exact port of the arena verifier (by running the
   original spec and comparing to our implementation)
2. `fast_score` agrees with `arena_score` to relative 1e-14 on real data
3. Degenerate inputs are rejected the same way
4. Known SOTA solutions score as expected
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import numpy as np
import pytest
from scipy.spatial import ConvexHull

from einstein.heilbronn_convex import (
    active_triples,
    all_triangle_areas,
    arena_score,
    fast_score,
    hull_area,
    min_triangle_area,
)


# --------------------------------------------------------------------------
# Arena verifier reference implementation (copy-pasted from API spec).
# This is the ground truth our evaluator must match.
# --------------------------------------------------------------------------
def _arena_reference(data):
    points = np.array(data["points"], dtype=np.float64)
    if points.shape != (14, 2):
        return -float("inf")
    if not np.isfinite(points).all():
        return -float("inf")

    def tri_area(p1, p2, p3):
        return (
            abs(
                p1[0] * (p2[1] - p3[1])
                + p2[0] * (p3[1] - p1[1])
                + p3[0] * (p1[1] - p2[1])
            )
            / 2
        )

    try:
        h_area = ConvexHull(points).volume
    except Exception:
        return -float("inf")
    if h_area < 1e-12:
        return -float("inf")
    min_area = min(
        tri_area(points[i], points[j], points[k])
        for i, j, k in itertools.combinations(range(14), 3)
    )
    return float(min_area / h_area)


SOLUTIONS_DIR = (
    Path.home()
    / "projects/workbench/memory-bank/einstein/docs/problem-16-heilbronn-convex/solutions"
)


def _load_leaderboard():
    if not SOLUTIONS_DIR.exists():
        pytest.skip("MB solutions dir not present")
    files = sorted(SOLUTIONS_DIR.glob("*.json"))
    out = []
    for f in files:
        data = json.loads(f.read_text())
        expected = float(f.stem.split("_")[-1])
        out.append((f.name, data, expected))
    return out


@pytest.fixture(scope="module")
def leaderboard():
    return _load_leaderboard()


def test_reference_matches_arena_scores(leaderboard):
    """Every downloaded solution must re-evaluate to (within ulp) its recorded score."""
    for name, data, expected in leaderboard:
        got = _arena_reference(data)
        assert abs(got - expected) < 1e-10, f"{name}: expected {expected}, got {got}"


def test_arena_score_matches_reference(leaderboard):
    """Our arena_score implementation must agree with the reference."""
    for name, data, _expected in leaderboard:
        ref = _arena_reference(data)
        ours = arena_score(data["points"])
        assert ours == ref, f"{name}: arena {ref}, ours {ours}"


def test_fast_score_matches_arena_score(leaderboard):
    """Vectorized fast_score must agree with arena_score to numerical precision."""
    for name, data, _expected in leaderboard:
        arena = arena_score(data["points"])
        fast = fast_score(data["points"])
        rel = abs(arena - fast) / max(abs(arena), 1e-15)
        assert rel < 1e-14, f"{name}: arena {arena}, fast {fast} (rel {rel:.2e})"


def test_invalid_shape_returns_neginf():
    assert arena_score([[0.0, 0.0]] * 13) == -float("inf")
    assert arena_score([[0.0, 0.0]] * 15) == -float("inf")
    assert arena_score(np.zeros((14, 3))) == -float("inf")


def test_non_finite_returns_neginf():
    pts = [[0.0, 0.0]] * 14
    pts[0] = [float("inf"), 0.0]
    assert arena_score(pts) == -float("inf")


def test_collinear_hull_returns_neginf():
    pts = [[float(i), 0.0] for i in range(14)]
    assert arena_score(pts) == -float("inf")


def test_min_triangle_area_consistent(leaderboard):
    for name, data, _expected in leaderboard:
        pts = np.array(data["points"], dtype=np.float64)
        min_a, triple = min_triangle_area(pts)
        ha = hull_area(pts)
        assert abs(min_a / ha - fast_score(pts)) < 1e-14
        i, j, k = triple
        # Verify the triple actually has this area
        got = 0.5 * abs(
            pts[i, 0] * (pts[j, 1] - pts[k, 1])
            + pts[j, 0] * (pts[k, 1] - pts[i, 1])
            + pts[k, 0] * (pts[i, 1] - pts[j, 1])
        )
        assert abs(got - min_a) < 1e-14


def test_active_triples_finds_equioscillation(leaderboard):
    """Capybara's solution should have 20 near-active triples; tied group ~16."""
    for name, data, expected in leaderboard:
        pts = np.array(data["points"], dtype=np.float64)
        n_active = len(active_triples(pts, rel_tol=1e-9))
        if "capybara007" in name:
            assert n_active == 20, f"capybara expected 20 active, got {n_active}"
        elif expected > 0.02783557 and expected < 0.02783558:
            # Tied group
            assert 14 <= n_active <= 18, (
                f"{name}: expected ~16 active, got {n_active}"
            )


def test_all_triangle_areas_length():
    rng = np.random.default_rng(0)
    pts = rng.normal(size=(14, 2))
    areas = all_triangle_areas(pts)
    assert areas.shape == (364,)
