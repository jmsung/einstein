"""Tests for the Heilbronn objective + family registry (pre-reg v2)."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pytest

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein.ablation_packing import families as fam  # noqa: E402
from einstein.ablation_packing import heilbronn as heil  # noqa: E402

# Unit square corners: every triple is a half-unit right triangle → min area 0.5.
SQUARE = np.array([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0]])


def test_min_triangle_area_known():
    assert heil.min_triangle_area(np.array([[0, 0], [1, 0], [0, 1]])) == pytest.approx(0.5)
    assert heil.min_triangle_area(SQUARE) == pytest.approx(0.5)


def test_fast_and_mpmath_agree_random():
    rng = np.random.default_rng(3)
    for _ in range(15):
        c = rng.random((rng.integers(3, 16), 2))
        assert heil.min_triangle_area(c) == pytest.approx(
            heil.min_triangle_area_mpmath(c), abs=1e-12
        )


def test_triple_verify_passes_and_agrees():
    tv = heil.triple_verify_heilbronn(SQUARE)
    assert tv.passed and tv.feasible and tv.reason == "ok"
    assert tv.fast == pytest.approx(tv.exact, abs=1e-12)
    assert tv.fast == pytest.approx(tv.cross, abs=1e-12)


def test_triple_verify_flags_points_outside_square():
    outside = np.array([[0.0, 0.0], [1.0, 0.0], [1.5, 1.0]])  # x=1.5 outside
    tv = heil.triple_verify_heilbronn(outside)
    assert tv.feasible is False and tv.passed is False


def test_triple_verify_random_configs_consistent():
    rng = np.random.default_rng(9)
    for _ in range(10):
        c = rng.random((rng.integers(3, 14), 2))
        tv = heil.triple_verify_heilbronn(c)
        assert tv.passed is True, tv.reason


# ---- family registry ----


def test_registry_resolves_both_families():
    assert fam.get_family("heilbronn_triangle").score is heil.min_triangle_area
    from einstein.ablation_packing import evaluator as ev

    assert fam.get_family("equal_circles_in_unit_square").score is ev.common_radius


def test_registry_unknown_family_raises():
    with pytest.raises(KeyError):
        fam.get_family("nonexistent")
