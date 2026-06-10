"""Tests for docs/tools/problem_priority.py — Phase 3 Goal 1 priority picker.

priority = headroom × hit-rate × staleness. Ranking, tie-breaks, and the
no-headroom-data fallback to problem_id order are the contract from the
branch file (js/feat/meta-learning-scheduler Goal 1).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "docs" / "tools"))
sys.path.insert(0, str(_REPO / "scripts"))

import autonomous_loop as al  # noqa: E402
import problem_priority as pp  # noqa: E402

# ---------------- relative_headroom ----------------


def test_headroom_zero_when_tied() -> None:
    assert pp.relative_headroom(1.5, 1.5, minimize=True) == 0.0


def test_headroom_zero_when_we_lead_minimize() -> None:
    # Lower is better and ours is lower → we lead → no headroom.
    assert pp.relative_headroom(1.4, 1.5, minimize=True) == 0.0


def test_headroom_zero_when_we_lead_maximize() -> None:
    assert pp.relative_headroom(2.0, 1.5, minimize=False) == 0.0


def test_headroom_positive_when_behind_minimize() -> None:
    # P12-shaped: ours 1.3539, arena #1 1.2809, minimize.
    h = pp.relative_headroom(1.3539, 1.2809, minimize=True)
    assert h == pytest.approx((1.3539 - 1.2809) / 1.2809, rel=1e-9)


def test_headroom_positive_when_behind_maximize() -> None:
    h = pp.relative_headroom(0.9622, 0.9626, minimize=False)
    assert h == pytest.approx((0.9626 - 0.9622) / 0.9626, rel=1e-6)


def test_headroom_none_when_missing_inputs() -> None:
    assert pp.relative_headroom(None, 1.5, minimize=True) is None
    assert pp.relative_headroom(1.5, None, minimize=True) is None
    assert pp.relative_headroom(1.5, 1.4, minimize=None) is None


# ---------------- category_hit_rate ----------------

_SKILL_LIB = """\
| technique | category | tried | top3 | finding | last_used | hit_rate |
|---|---|---|---|---|---|---|
| `memetic-tabu-search.md` | discrete-combinatorics | 4 | 0 | 1 | 2026-04-02 | 0.00 |
| `bnb-exhaustive-w3.md` | discrete-combinatorics | 1 | 0 | 1 | 2026-04-09 | 0.00 |
| `slsqp-active-pair-polish.md` | packing / kissing | 25 | 6 | 1 | 2026-06-03 | 0.24 |
| `arena-tolerance-slsqp.md` | packing | 34 | 9 | 1 | 2026-06-03 | 0.26 |
| `larger-n-cascade.md` | autocorrelation | 19 | 4 | 3 | 2026-06-06 | 0.21 |
"""


def _write_skill_lib(tmp_path: Path) -> Path:
    p = tmp_path / "skill-library.md"
    p.write_text(_SKILL_LIB)
    return p


def test_category_hit_rate_aggregates_tried_weighted(tmp_path: Path) -> None:
    lib = _write_skill_lib(tmp_path)
    # packing: (6+9)/(25+34) — substring match picks up "packing / kissing".
    assert pp.category_hit_rate("packing", lib) == pytest.approx(15 / 59)


def test_category_hit_rate_zero_hit_category(tmp_path: Path) -> None:
    lib = _write_skill_lib(tmp_path)
    assert pp.category_hit_rate("discrete-combinatorics", lib) == 0.0


def test_category_hit_rate_unknown_category_is_none(tmp_path: Path) -> None:
    lib = _write_skill_lib(tmp_path)
    assert pp.category_hit_rate("sieve", lib) is None
    assert pp.category_hit_rate("?", lib) is None


def test_category_hit_rate_missing_file_is_none(tmp_path: Path) -> None:
    assert pp.category_hit_rate("packing", tmp_path / "nope.md") is None


# ---------------- staleness ----------------

_CYCLE_LOG = """\
# Cycle log

| 280 | P2-first-autocorrelation | 1.5 (no Δ) | 1 | local-cpu | 0 | 0 | 0 | a:1/h:0/hyb:0 | converged | x | 0 |
| 281 | P4-third-autocorrelation | 1.4 (no Δ) | 1 | local-cpu | 0 | 0 | 0 | a:1/h:0/hyb:0 | converged | x | 0 |
| 287 | P12-flat-polynomials | 1.3 (no Δ) | 1 | local-cpu+llm | 0 | 1 | 0 | a:1/h:0/hyb:0 | converged | x | 0 |
"""


def _write_cycle_log(tmp_path: Path) -> Path:
    p = tmp_path / "cycle-log.md"
    p.write_text(_CYCLE_LOG)
    return p


def test_staleness_most_recent_is_zero(tmp_path: Path) -> None:
    log = _write_cycle_log(tmp_path)
    assert pp.staleness("P12-flat-polynomials", log) == 0.0


def test_staleness_older_visit_positive_and_ordered(tmp_path: Path) -> None:
    log = _write_cycle_log(tmp_path)
    s2 = pp.staleness("P2-first-autocorrelation", log)
    s4 = pp.staleness("P4-third-autocorrelation", log)
    assert 0.0 < s4 < s2 <= 1.0


def test_staleness_never_visited_is_max(tmp_path: Path) -> None:
    log = _write_cycle_log(tmp_path)
    assert pp.staleness("P10-thomson-n282", log) == 1.0


def test_staleness_missing_log_is_max(tmp_path: Path) -> None:
    assert pp.staleness("P12-flat-polynomials", tmp_path / "nope.md") == 1.0


# ---------------- problem_priority ----------------


def test_priority_monotone_in_each_factor() -> None:
    base = pp.problem_priority(headroom=0.05, hit_rate=0.5, staleness=0.5)
    assert pp.problem_priority(0.10, 0.5, 0.5) > base
    assert pp.problem_priority(0.05, 0.9, 0.5) > base
    assert pp.problem_priority(0.05, 0.5, 0.9) > base


def test_priority_zero_headroom_is_zero() -> None:
    # Tied/leading problems must rank at the bottom regardless of other terms.
    assert pp.problem_priority(0.0, 1.0, 1.0) == 0.0


def test_priority_zero_hit_rate_does_not_annihilate() -> None:
    # A category with 0 hit-rate (e.g. P12 discrete-combinatorics) must not
    # erase real headroom — the floor keeps the problem rankable.
    assert pp.problem_priority(0.05, 0.0, 0.5) > 0.0


def test_priority_missing_hit_rate_is_neutral() -> None:
    # hit_rate=None → neutral 0.5, identical to passing 0.5 explicitly.
    assert pp.problem_priority(0.05, None, 0.5) == pp.problem_priority(0.05, 0.5, 0.5)


# ---------------- build_priority_queue ----------------


def _mk_problem(pid: int, slug: str, score: float | None = 1.0) -> al.Problem:
    return al.Problem(
        problem_id=pid,
        slug=slug,
        tier="B",
        status="open",
        score_current=score,
        path=Path(f"/dev/null/{pid}-{slug}.md"),
        extra={},
    )


def test_queue_ranks_by_priority_desc(tmp_path: Path) -> None:
    lib = _write_skill_lib(tmp_path)
    log = _write_cycle_log(tmp_path)
    problems = [
        _mk_problem(2, "first-autocorrelation"),
        _mk_problem(4, "third-autocorrelation"),
        _mk_problem(12, "flat-polynomials"),
    ]
    # P12 has the largest raw headroom but was just visited (staleness floor)
    # and its category has 0 hit-rate; P4 is staler with a productive category.
    headrooms = {2: 1e-7, 4: 1e-4, 12: 0.057}
    queue = pp.build_priority_queue(problems, headrooms, skill_library=lib, cycle_log=log)
    ids = [p.problem_id for p in queue]
    # Log-compression keeps headroom dominant but lets hit-rate + staleness
    # rotate the queue: P4 edges fresh/0-hit P12 (the Goal-5 anti-grind fix);
    # P2's sub-minImprovement headroom sinks it to the bottom.
    assert ids == [4, 12, 2]


def test_queue_tie_break_is_problem_id_asc(tmp_path: Path) -> None:
    lib = _write_skill_lib(tmp_path)
    log = tmp_path / "empty-log.md"
    # P2 and P4 share the autocorrelation category → identical hit-rate;
    # equal headroom + both never-visited → a true priority tie.
    problems = [_mk_problem(4, "b"), _mk_problem(2, "a")]
    headrooms = {2: 0.01, 4: 0.01}
    queue = pp.build_priority_queue(problems, headrooms, skill_library=lib, cycle_log=log)
    assert [p.problem_id for p in queue] == [2, 4]


def test_queue_no_headroom_data_falls_back_to_id_order(tmp_path: Path) -> None:
    lib = _write_skill_lib(tmp_path)
    log = _write_cycle_log(tmp_path)
    problems = [_mk_problem(12, "c"), _mk_problem(2, "a"), _mk_problem(4, "b")]
    headrooms: dict[int, float | None] = {2: None, 4: None, 12: None}
    queue = pp.build_priority_queue(problems, headrooms, skill_library=lib, cycle_log=log)
    assert [p.problem_id for p in queue] == [2, 4, 12]


def test_queue_unknown_headroom_problems_rank_after_scored(tmp_path: Path) -> None:
    lib = _write_skill_lib(tmp_path)
    log = _write_cycle_log(tmp_path)
    problems = [_mk_problem(2, "a"), _mk_problem(4, "b"), _mk_problem(12, "c")]
    headrooms = {2: None, 4: 1e-4, 12: None}
    queue = pp.build_priority_queue(problems, headrooms, skill_library=lib, cycle_log=log)
    assert [p.problem_id for p in queue] == [4, 2, 12]


# ---------------- headroom cache ----------------


def test_cache_roundtrip(tmp_path: Path) -> None:
    cache = tmp_path / "headroom-cache.json"
    pp.save_cached_arena_best(cache, 12, 1.2809, ts="2026-06-09T00:00:00Z")
    assert pp.load_cached_arena_best(cache, 12) == 1.2809
    assert pp.load_cached_arena_best(cache, 99) is None


def test_cache_missing_file_is_none(tmp_path: Path) -> None:
    assert pp.load_cached_arena_best(tmp_path / "nope.json", 12) is None


def test_cache_corrupt_file_is_none_not_raise(tmp_path: Path) -> None:
    cache = tmp_path / "headroom-cache.json"
    cache.write_text("{not json")
    assert pp.load_cached_arena_best(cache, 12) is None
    # And save still works (overwrites corrupt content).
    pp.save_cached_arena_best(cache, 12, 1.0, ts="2026-06-09T00:00:00Z")
    assert pp.load_cached_arena_best(cache, 12) == 1.0


def test_cache_save_preserves_other_pids(tmp_path: Path) -> None:
    cache = tmp_path / "headroom-cache.json"
    pp.save_cached_arena_best(cache, 12, 1.2809, ts="t1")
    pp.save_cached_arena_best(cache, 4, 1.4523, ts="t2")
    data = json.loads(cache.read_text())
    assert set(data) == {"12", "4"}


# ---------------- headroom_for (fetch → cache → None ladder) ----------------


def test_headroom_for_live_fetch_updates_cache(tmp_path: Path) -> None:
    cache = tmp_path / "headroom-cache.json"
    h = pp.headroom_for(
        12,
        our_score=1.3539,
        minimize=True,
        fetcher=lambda pid: 1.2809,
        cache_path=cache,
        ts="2026-06-09T00:00:00Z",
    )
    assert h == pytest.approx((1.3539 - 1.2809) / 1.2809, rel=1e-9)
    assert pp.load_cached_arena_best(cache, 12) == 1.2809


def test_headroom_for_falls_back_to_cache_on_fetch_failure(tmp_path: Path) -> None:
    cache = tmp_path / "headroom-cache.json"
    pp.save_cached_arena_best(cache, 12, 1.2809, ts="t0")

    def boom(pid: int) -> float:
        raise OSError("network down")

    h = pp.headroom_for(12, our_score=1.3539, minimize=True, fetcher=boom, cache_path=cache)
    assert h == pytest.approx((1.3539 - 1.2809) / 1.2809, rel=1e-9)


def test_headroom_for_none_when_no_fetch_no_cache(tmp_path: Path) -> None:
    def boom(pid: int) -> float:
        raise OSError("network down")

    h = pp.headroom_for(
        12,
        our_score=1.3539,
        minimize=True,
        fetcher=boom,
        cache_path=tmp_path / "nope.json",
    )
    assert h is None


def test_headroom_for_none_when_direction_unknown(tmp_path: Path) -> None:
    # Fail-closed on unknown direction (dead-end-auto-submit-direction-sign).
    h = pp.headroom_for(
        99,
        our_score=1.0,
        minimize=None,
        fetcher=lambda pid: 2.0,
        cache_path=tmp_path / "c.json",
    )
    assert h is None


def test_overall_hit_rate_is_tried_weighted(tmp_path: Path) -> None:
    lib = _write_skill_lib(tmp_path)
    # (0+0+6+9+4) / (4+1+25+34+19)
    assert pp.overall_hit_rate(lib) == pytest.approx(19 / 83)
    assert pp.overall_hit_rate(tmp_path / "nope.md") is None


def test_unknown_category_uses_library_prior_not_half(tmp_path: Path) -> None:
    """Goal-5 iterate fix: a no-data category must not outrank measured ones
    via the generous 0.5 neutral — it gets the library-wide rate instead."""
    lib = _write_skill_lib(tmp_path)
    log = tmp_path / "empty.md"
    # P10's category (sphere-packing-ish) has no rows; P4's (autocorrelation)
    # does. Equal headroom + equal staleness → the measured category with the
    # HIGHER actual rate must win iff its rate beats the library prior.
    problems = [_mk_problem(10, "thomson-n282"), _mk_problem(4, "third-autocorrelation")]
    headrooms = {10: 1e-4, 4: 1e-4}
    queue = pp.build_priority_queue(problems, headrooms, skill_library=lib, cycle_log=log)
    # library prior = 19/83 ≈ 0.229 > autocorrelation's 4/19 ≈ 0.211 — so P10
    # edges P4 here, but by the prior's honest margin, not by 0.5-vs-0.21.
    pri = {p.problem_id: i for i, p in enumerate(queue)}
    assert set(pri) == {4, 10}
