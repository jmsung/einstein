"""Parity tests for P15 Heilbronn Triangles evaluator.

Verifies arena_score() byte-exactly reproduces the leaderboard claimed score
for every downloaded solution (top 15 agents).
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from einstein.heilbronn_triangles import (
    active_triples,
    arena_score,
    fast_score,
    in_triangle,
    min_triangle_area,
)

SOL_DIR = Path(__file__).resolve().parents[2] / "results" / "problem-15-heilbronn-triangles"


def _all_solutions():
    if not SOL_DIR.exists():
        return []
    return sorted(SOL_DIR.glob("rank*.json"))


@pytest.mark.parametrize("sol_path", _all_solutions(), ids=lambda p: p.name)
def test_arena_score_matches_leaderboard(sol_path: Path) -> None:
    """arena_score() must reproduce the leaderboard claimed score bit-exactly."""
    data = json.loads(sol_path.read_text())
    pts = data["data"]["points"]
    claimed = data["score"]
    ours = arena_score(pts)
    assert ours == claimed, (
        f"{sol_path.name}: arena_score={ours!r} vs claimed={claimed!r}, "
        f"delta={ours - claimed:.3e}"
    )


def test_fast_score_matches_arena_on_top_solution() -> None:
    paths = _all_solutions()
    if not paths:
        pytest.skip("no solution files downloaded")
    data = json.loads(paths[0].read_text())
    pts = data["data"]["points"]
    assert arena_score(pts) == fast_score(pts)


def test_top_solution_has_many_active_triples() -> None:
    paths = _all_solutions()
    if not paths:
        pytest.skip("no solution files downloaded")
    data = json.loads(paths[0].read_text())
    pts = data["data"]["points"]
    active = active_triples(pts, rel_tol=1e-9)
    assert len(active) >= 10, (
        f"top solution should equioscillate with 10+ active triples, "
        f"got {len(active)}"
    )


def test_in_triangle_accepts_top_solution() -> None:
    paths = _all_solutions()
    if not paths:
        pytest.skip("no solution files downloaded")
    data = json.loads(paths[0].read_text())
    pts = data["data"]["points"]
    assert in_triangle(pts, tol=0.0)


def test_min_triangle_area_consistency() -> None:
    paths = _all_solutions()
    if not paths:
        pytest.skip("no solution files downloaded")
    data = json.loads(paths[0].read_text())
    pts = data["data"]["points"]
    area, triple = min_triangle_area(pts)
    import math
    assert area / (math.sqrt(3) / 4) == arena_score(pts)
    i, j, k = triple
    assert 0 <= i < j < k < 11
