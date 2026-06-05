"""Procedural arena-resolution guard for discretised-functional problems."""

import pytest

from einstein.triple_verify.resolution_guard import (
    ARENA_RESOLUTION_CAP,
    assert_arena_resolution,
)


def test_valid_length_passes():
    assert assert_arena_resolution([0.0] * 100_000) == 100_000
    assert assert_arena_resolution([1.0] * 50_000) == 50_000


def test_cap_is_two_million():
    # CORRECTED 2026-06-04: the P3 page allows up to 2,000,000 points; the live
    # #1 is an n=400000 array scored at its full resolution. The old 100k cap
    # was a mis-inference from the resolution-inflation episode.
    assert ARENA_RESOLUTION_CAP == 2_000_000
    assert assert_arena_resolution([1.0] * 400_000) == 400_000
    assert assert_arena_resolution([1.0] * 2_000_000) == 2_000_000


def test_over_cap_rejected():
    with pytest.raises(ValueError, match="exceeds arena cap"):
        assert_arena_resolution([0.0] * (ARENA_RESOLUTION_CAP + 1))


def test_empty_rejected():
    with pytest.raises(ValueError, match="empty"):
        assert_arena_resolution([])
