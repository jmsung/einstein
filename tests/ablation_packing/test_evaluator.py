"""Tests for the generic held-out circle-packing evaluator (Goal 1)."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pytest

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein.ablation_packing import evaluator as ev  # noqa: E402

# A known exact value: the 2×2 grid packs 4 circles at r = 1/4 (the optimum for
# n=4). Centers strictly inside so both the wall term and the pair term equal 0.25.
GRID4 = np.array([[0.25, 0.25], [0.25, 0.75], [0.75, 0.25], [0.75, 0.75]])


def test_common_radius_known_grid():
    assert ev.common_radius(GRID4) == pytest.approx(0.25, abs=1e-12)


def test_common_radius_wall_binds_when_point_near_edge():
    # one point hard against the wall → wall term (0.05) dominates the pair term
    centers = np.array([[0.05, 0.5], [0.5, 0.5]])
    assert ev.common_radius(centers) == pytest.approx(0.05, abs=1e-12)


def test_common_radius_single_point_is_wall_only():
    assert ev.common_radius(np.array([[0.3, 0.4]])) == pytest.approx(0.3, abs=1e-12)


def test_common_radius_negative_when_outside_square():
    # center outside [0,1]^2 → negative wall term surfaces the violation
    assert ev.common_radius(np.array([[1.2, 0.5], [0.5, 0.5]])) < 0


def test_fast_and_mpmath_agree_on_random_configs():
    rng = np.random.default_rng(7)
    for _ in range(20):
        c = rng.random((rng.integers(2, 16), 2))
        assert ev.common_radius(c) == pytest.approx(ev.common_radius_mpmath(c), abs=1e-12)


def test_triple_verify_passes_and_agrees_three_ways():
    tv = ev.triple_verify_radius(GRID4)
    assert tv.passed is True and tv.feasible is True and tv.reason == "ok"
    assert tv.fast == pytest.approx(tv.exact, abs=1e-12)
    assert tv.fast == pytest.approx(tv.cross, abs=1e-12)
    assert tv.fast == pytest.approx(0.25, abs=1e-12)


def test_triple_verify_random_configs_consistent():
    rng = np.random.default_rng(11)
    for _ in range(15):
        c = rng.random((rng.integers(2, 14), 2))
        tv = ev.triple_verify_radius(c)
        assert tv.passed is True, tv.reason  # derived radius is always self-consistent + feasible


def test_cold_init_deterministic_and_in_range():
    a = ev.cold_init(12, seed=3)
    b = ev.cold_init(12, seed=3)
    assert a.shape == (12, 2)
    assert np.array_equal(a, b)  # same (n, seed) → identical init
    assert a.min() >= 0.0 and a.max() <= 1.0


def test_cold_init_varies_by_seed():
    assert not np.array_equal(ev.cold_init(12, seed=1), ev.cold_init(12, seed=2))


# ---------------- triple-verify rejects infeasible geometry (red-team 2026-06-27) ----------------


@pytest.mark.parametrize("centers", [
    [[0.5, 0.5], [0.5, -0.05]],   # a center outside the unit square
    [[0.3, 0.3], [0.3, 0.3]],     # duplicate / coincident centers (r≈0)
    [[1.5, 1.5], [0.2, 0.2]],     # wildly out of square (r<0)
])
def test_triple_verify_rejects_infeasible(centers):
    tv = ev.triple_verify_radius(np.array(centers, dtype=float))
    assert tv.feasible is False and tv.passed is False


def test_triple_verify_accepts_valid():
    tv = ev.triple_verify_radius(np.array([[0.25, 0.25], [0.75, 0.75]], dtype=float))
    assert tv.feasible is True and tv.passed is True
