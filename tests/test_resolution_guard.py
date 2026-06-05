"""Procedural arena-resolution guard for discretised-functional problems."""

import pytest

from einstein.triple_verify.resolution_guard import (
    ARENA_RESOLUTION_CAP,
    assert_arena_resolution,
)


def test_valid_length_passes():
    assert assert_arena_resolution([0.0] * 100_000) == 100_000
    assert assert_arena_resolution([1.0] * 50_000) == 50_000


def test_over_cap_rejected():
    with pytest.raises(ValueError, match="exceeds arena cap"):
        assert_arena_resolution([0.0] * (ARENA_RESOLUTION_CAP + 1))


def test_empty_rejected():
    with pytest.raises(ValueError, match="empty"):
        assert_arena_resolution([])
