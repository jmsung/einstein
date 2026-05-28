"""Tests for src/einstein/parallel/fanout.py — K-attempt orchestrator (Goal 1).

Covers the K-pull Thompson contract pinned down in Goal 0:
  - K independent draws from the SAME posterior; collisions allowed.
  - Deterministic under a shared seeded RNG.
  - Winner selection by extremum of `score` over completed attempts;
    direction = "min" by default (codebase convention; see plan).
  - "no-arm" / "timeout" / "dispatch-failed" attempts still produce
    AttemptResult rows but don't compete for the winner.
"""

from __future__ import annotations

import random
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein.bandit.thompson import ThompsonSampler  # noqa: E402
from einstein.parallel.fanout import (  # noqa: E402
    AttemptContext,
    AttemptResult,
    FanoutResult,
    run_fanout,
)


def _row(technique, category, tried, top3):
    return SimpleNamespace(technique=technique, category=category, tried=tried, top3=top3)


def _problem(problem_id=14, score=1.0):
    return SimpleNamespace(problem_id=problem_id, score_current=score, display=f"P{problem_id}")


# Two-arm library: dominant arm (50 hits / 50 tries) vs ~uniform arm.
DOMINANT_ROWS = [
    _row("dominant.md", "circle-packing", tried=50, top3=50),
    _row("loser.md", "circle-packing", tried=50, top3=0),
]


# A canned runner that records the contexts it saw + returns scripted results.
def _scripted_runner(results_by_index):
    """Returns a runner that yields a pre-scripted AttemptResult per attempt.

    `results_by_index` is a dict keyed by 1-indexed attempt number → AttemptResult.
    The runner records each AttemptContext it saw to `runner.calls`.
    """
    calls: list[AttemptContext] = []

    def _runner(ctx: AttemptContext) -> AttemptResult:
        calls.append(ctx)
        return results_by_index[ctx.attempt_index]

    _runner.calls = calls  # type: ignore[attr-defined]
    return _runner


def _ok(index: int, technique: str | None, score: float, **kw) -> AttemptResult:
    return AttemptResult(
        index=index,
        technique=technique,
        score=score,
        exit="ok",
        notes=kw.get("notes", ""),
        pick_note=kw.get("pick_note"),
    )


def _failed(index: int, exit_reason: str, technique: str | None = None) -> AttemptResult:
    return AttemptResult(
        index=index,
        technique=technique,
        score=None,
        exit=exit_reason,
        notes="",
        pick_note=None,
    )


# ---------------- K-pull semantics ----------------


def test_run_fanout_k_pulls_independent_collisions_allowed():
    """K=4 against a strongly-dominant arm → all 4 picks land on the dominant arm.

    Collisions are the CORRECT behavior under Thompson (Goal 0 research note):
    when one arm's posterior dominates, K independent draws from the same
    posterior all pick that arm with high probability. Any "exclusion" variant
    that forces 4 distinct arms would break probability matching.
    """
    bandit = ThompsonSampler(rows=DOMINANT_ROWS)
    rng = random.Random(42)
    runner = _scripted_runner({i: _ok(i, technique=None, score=float(i)) for i in range(1, 5)})

    result = run_fanout(
        _problem(),
        k=4,
        bandit=bandit,
        category="circle-packing",
        rng=rng,
        runner=runner,
    )

    # Every attempt context saw `dominant.md` as the technique
    assert len(runner.calls) == 4  # type: ignore[attr-defined]
    techniques = [ctx.technique for ctx in runner.calls]  # type: ignore[attr-defined]
    assert (
        techniques == ["dominant.md"] * 4
    ), f"K=4 against Beta(51,1) vs Beta(1,51) should always pick dominant; got {techniques}"
    # FanoutResult carries K attempts in order
    assert len(result.attempts) == 4
    assert [a.index for a in result.attempts] == [1, 2, 3, 4]


def test_run_fanout_deterministic_under_seed():
    """Same (rows, seed, runner-side-effects-free) → identical FanoutResult."""
    runner1 = _scripted_runner({i: _ok(i, None, score=float(i)) for i in range(1, 5)})
    runner2 = _scripted_runner({i: _ok(i, None, score=float(i)) for i in range(1, 5)})
    bandit1 = ThompsonSampler(rows=DOMINANT_ROWS)
    bandit2 = ThompsonSampler(rows=DOMINANT_ROWS)

    r1 = run_fanout(
        _problem(),
        k=4,
        bandit=bandit1,
        category="circle-packing",
        rng=random.Random(7),
        runner=runner1,
    )
    r2 = run_fanout(
        _problem(),
        k=4,
        bandit=bandit2,
        category="circle-packing",
        rng=random.Random(7),
        runner=runner2,
    )
    # Same techniques picked, same order
    assert [c.technique for c in runner1.calls] == [c.technique for c in runner2.calls]  # type: ignore[attr-defined]
    # Same per-attempt RNG seed → same first draw from each attempt rng
    assert [c.rng.random() for c in runner1.calls] == [c.rng.random() for c in runner2.calls]  # type: ignore[attr-defined]
    assert r1.winner_index == r2.winner_index


def test_run_fanout_per_attempt_rng_streams_independent():
    """Each AttemptContext.rng must be a distinct stream so per-attempt
    seeded ops in the runner produce diverse results."""
    bandit = ThompsonSampler(rows=DOMINANT_ROWS)
    runner = _scripted_runner({i: _ok(i, None, score=float(i)) for i in range(1, 5)})
    run_fanout(
        _problem(),
        k=4,
        bandit=bandit,
        category="circle-packing",
        rng=random.Random(42),
        runner=runner,
    )
    first_draws = [ctx.rng.random() for ctx in runner.calls]  # type: ignore[attr-defined]
    assert (
        len(set(first_draws)) == 4
    ), f"K=4 per-attempt rngs should produce 4 distinct first draws; got {first_draws}"


# ---------------- winner selection ----------------


def test_run_fanout_winner_by_min_score_default():
    """Default `score_direction='min'` (codebase convention: lower is better)."""
    bandit = ThompsonSampler(rows=DOMINANT_ROWS)
    runner = _scripted_runner(
        {
            1: _ok(1, "dominant.md", score=1.0),
            2: _ok(2, "dominant.md", score=0.5),
            3: _ok(3, "dominant.md", score=0.8),
            4: _ok(4, "dominant.md", score=0.3),
        }
    )
    result = run_fanout(
        _problem(),
        k=4,
        bandit=bandit,
        category="circle-packing",
        rng=random.Random(1),
        runner=runner,
    )
    assert result.winner_index == 3
    assert result.winner is not None
    assert result.winner.score == 0.3


def test_run_fanout_winner_by_max_score_explicit():
    """`score_direction='max'` for any future maximize-by-convention problem."""
    bandit = ThompsonSampler(rows=DOMINANT_ROWS)
    runner = _scripted_runner(
        {
            1: _ok(1, "dominant.md", score=1.0),
            2: _ok(2, "dominant.md", score=0.5),
            3: _ok(3, "dominant.md", score=0.8),
            4: _ok(4, "dominant.md", score=0.3),
        }
    )
    result = run_fanout(
        _problem(),
        k=4,
        bandit=bandit,
        category="circle-packing",
        rng=random.Random(1),
        runner=runner,
        score_direction="max",
    )
    assert result.winner_index == 0
    assert result.winner is not None
    assert result.winner.score == 1.0


def test_run_fanout_winner_skips_failed_attempts():
    """`winner_index` is over `exit == 'ok'` attempts only."""
    bandit = ThompsonSampler(rows=DOMINANT_ROWS)
    runner = _scripted_runner(
        {
            1: _failed(1, "timeout"),
            2: _ok(2, "dominant.md", score=0.5),
            3: _failed(3, "dispatch-failed"),
            4: _ok(4, "dominant.md", score=0.7),
        }
    )
    result = run_fanout(
        _problem(),
        k=4,
        bandit=bandit,
        category="circle-packing",
        rng=random.Random(1),
        runner=runner,
    )
    assert result.winner_index == 1
    assert result.k_completed == 2
    # All 4 attempts still appear in the result for cycle-log purposes
    assert len(result.attempts) == 4


def test_run_fanout_all_failed_winner_none():
    """Every attempt failed → winner_index is None, k_completed is 0."""
    bandit = ThompsonSampler(rows=DOMINANT_ROWS)
    runner = _scripted_runner(
        {
            1: _failed(1, "timeout"),
            2: _failed(2, "dispatch-failed"),
            3: _failed(3, "timeout"),
        }
    )
    result = run_fanout(
        _problem(),
        k=3,
        bandit=bandit,
        category="circle-packing",
        rng=random.Random(1),
        runner=runner,
    )
    assert result.winner_index is None
    assert result.winner is None
    assert result.k_completed == 0


# ---------------- no-arm propagation ----------------


def test_run_fanout_no_bandit_arm_attempt_has_none_technique():
    """When bandit has no matching arm, every AttemptContext.technique is None
    and pick_note is None; the runner gets called K times anyway so the caller
    can decide fallback (council, manifest dispatch, skip)."""
    bandit = ThompsonSampler(rows=DOMINANT_ROWS)  # no arms for "kissing"

    def _no_arm_runner(ctx: AttemptContext) -> AttemptResult:
        assert ctx.technique is None
        assert ctx.pick_note is None
        return AttemptResult(
            index=ctx.attempt_index,
            technique=None,
            score=None,
            exit="no-arm",
            notes="bandit no-arm; caller fallback",
            pick_note=None,
        )

    result = run_fanout(
        _problem(),
        k=3,
        bandit=bandit,
        category="kissing",
        rng=random.Random(1),
        runner=_no_arm_runner,
    )
    assert len(result.attempts) == 3
    assert all(a.technique is None for a in result.attempts)
    assert all(a.exit == "no-arm" for a in result.attempts)
    assert result.winner_index is None


# ---------------- K=1 + validation ----------------


def test_run_fanout_k_eq_1_single_attempt():
    """K=1 reduces to a single attempt; winner is that attempt iff it succeeded."""
    bandit = ThompsonSampler(rows=DOMINANT_ROWS)
    runner = _scripted_runner({1: _ok(1, "dominant.md", score=0.42)})
    result = run_fanout(
        _problem(),
        k=1,
        bandit=bandit,
        category="circle-packing",
        rng=random.Random(1),
        runner=runner,
    )
    assert len(result.attempts) == 1
    assert result.winner_index == 0
    assert result.winner is not None
    assert result.winner.score == 0.42


def test_run_fanout_validates_k_min_1():
    bandit = ThompsonSampler(rows=DOMINANT_ROWS)
    with pytest.raises(ValueError, match="K"):
        run_fanout(
            _problem(),
            k=0,
            bandit=bandit,
            category="circle-packing",
            rng=random.Random(1),
            runner=_scripted_runner({}),
        )


def test_run_fanout_validates_score_direction():
    bandit = ThompsonSampler(rows=DOMINANT_ROWS)
    with pytest.raises(ValueError, match="score_direction"):
        run_fanout(
            _problem(),
            k=1,
            bandit=bandit,
            category="circle-packing",
            rng=random.Random(1),
            runner=_scripted_runner({1: _ok(1, None, 0.0)}),
            score_direction="neither",  # type: ignore[arg-type]
        )


# ---------------- audit-field plumbing ----------------


def test_attempt_context_carries_audit_fields():
    """Bandit's pick.note() lands on AttemptContext.pick_note AND on the
    AttemptResult.pick_note (so Goal 3's cycle-log can record every arm)."""
    bandit = ThompsonSampler(rows=DOMINANT_ROWS)
    seen_notes: list[str | None] = []

    def _capture_runner(ctx: AttemptContext) -> AttemptResult:
        seen_notes.append(ctx.pick_note)
        return AttemptResult(
            index=ctx.attempt_index,
            technique=ctx.technique,
            score=0.1 * ctx.attempt_index,
            exit="ok",
            notes="",
            pick_note=ctx.pick_note,  # propagate
        )

    result = run_fanout(
        _problem(),
        k=3,
        bandit=bandit,
        category="circle-packing",
        rng=random.Random(1),
        runner=_capture_runner,
    )
    assert all(n is not None for n in seen_notes)
    assert all(a.pick_note is not None for a in result.attempts)
    # Format check — the note should mention the picked technique
    assert all("technique=" in (a.pick_note or "") for a in result.attempts)


# ---------------- type sanity ----------------


def test_fanout_result_is_frozen():
    result = FanoutResult(attempts=(), winner_index=None)
    with pytest.raises((AttributeError, Exception)):
        result.winner_index = 0  # type: ignore[misc]


# ---------------- Goal 4: per-attempt timeout + partial-K ----------------


import time as _time  # noqa: E402


def test_run_fanout_per_attempt_timeout_fires():
    """A runner that sleeps past the timeout produces exit='timeout' results.

    Technique + pick_note must be preserved on the fabricated timeout result
    so Goal 3's cycle-log + bandit-counter machinery still has the audit info."""
    bandit = ThompsonSampler(rows=DOMINANT_ROWS)

    def slow_runner(ctx: AttemptContext) -> AttemptResult:
        _time.sleep(0.5)
        return AttemptResult(
            index=ctx.attempt_index,
            technique=ctx.technique,
            score=0.0,
            exit="ok",
            notes="should-not-be-reached",
            pick_note=ctx.pick_note,
        )

    result = run_fanout(
        _problem(),
        k=3,
        bandit=bandit,
        category="circle-packing",
        rng=random.Random(1),
        runner=slow_runner,
        per_attempt_timeout_seconds=0.05,
    )
    assert all(a.exit == "timeout" for a in result.attempts)
    assert result.k_completed == 0
    assert result.winner_index is None
    # Each timeout result preserves the bandit pick's audit fields
    for a in result.attempts:
        assert a.technique == "dominant.md"
        assert a.pick_note is not None
        assert "technique=dominant.md" in a.pick_note


def test_run_fanout_partial_k_with_timeout():
    """Some attempts complete within timeout, some don't — k_completed reflects
    the ok ones; winner is picked from those."""
    bandit = ThompsonSampler(rows=DOMINANT_ROWS)

    def mixed_runner(ctx: AttemptContext) -> AttemptResult:
        # Even attempts are slow, odd attempts are fast
        if ctx.attempt_index % 2 == 0:
            _time.sleep(0.5)
        return AttemptResult(
            index=ctx.attempt_index,
            technique=ctx.technique,
            score=0.1 * ctx.attempt_index,
            exit="ok",
            notes="",
            pick_note=ctx.pick_note,
        )

    result = run_fanout(
        _problem(),
        k=4,
        bandit=bandit,
        category="circle-packing",
        rng=random.Random(1),
        runner=mixed_runner,
        per_attempt_timeout_seconds=0.1,
    )
    # Odd attempts (1, 3) completed; even (2, 4) timed out
    assert result.k_completed == 2
    completed = [a for a in result.attempts if a.exit == "ok"]
    timed_out = [a for a in result.attempts if a.exit == "timeout"]
    assert len(completed) == 2 and len(timed_out) == 2
    assert {a.index for a in completed} == {1, 3}
    # Winner is the min-score ok attempt (score = 0.1 * index, so index 1 wins)
    assert result.winner is not None
    assert result.winner.index == 1


def test_run_fanout_no_timeout_is_sequential():
    """`per_attempt_timeout_seconds=None` → sequential path (no threads).

    Pinned by checking that the runner's call order matches submission order
    (the threaded path collects in submission order too, but the no-thread
    path doesn't create the executor at all)."""
    bandit = ThompsonSampler(rows=DOMINANT_ROWS)
    call_order: list[int] = []

    def runner(ctx: AttemptContext) -> AttemptResult:
        call_order.append(ctx.attempt_index)
        return AttemptResult(
            index=ctx.attempt_index,
            technique=ctx.technique,
            score=float(ctx.attempt_index),
            exit="ok",
            notes="",
            pick_note=ctx.pick_note,
        )

    run_fanout(
        _problem(),
        k=3,
        bandit=bandit,
        category="circle-packing",
        rng=random.Random(1),
        runner=runner,
        per_attempt_timeout_seconds=None,
    )
    assert call_order == [1, 2, 3]


def test_run_fanout_timeout_results_in_index_order():
    """When threads finish out of order, results[] is still sorted by index
    (so attempt_rewards[i] in Goal 3 lines up with chosen_techniques[i])."""
    bandit = ThompsonSampler(rows=DOMINANT_ROWS)

    def reversed_speed_runner(ctx: AttemptContext) -> AttemptResult:
        # Later attempts finish first (sleep decreases by index)
        _time.sleep(max(0, 0.05 - ctx.attempt_index * 0.01))
        return AttemptResult(
            index=ctx.attempt_index,
            technique=ctx.technique,
            score=float(ctx.attempt_index),
            exit="ok",
            notes="",
            pick_note=ctx.pick_note,
        )

    result = run_fanout(
        _problem(),
        k=4,
        bandit=bandit,
        category="circle-packing",
        rng=random.Random(1),
        runner=reversed_speed_runner,
        per_attempt_timeout_seconds=5.0,
    )
    indices = [a.index for a in result.attempts]
    assert indices == [1, 2, 3, 4]


def test_run_fanout_timeout_with_executor_seam():
    """Caller can inject an executor (test seam for deterministic shutdown)."""
    from concurrent.futures import ThreadPoolExecutor

    bandit = ThompsonSampler(rows=DOMINANT_ROWS)
    runner = _scripted_runner({i: _ok(i, None, score=float(i)) for i in range(1, 4)})
    with ThreadPoolExecutor(max_workers=2) as ex:
        result = run_fanout(
            _problem(),
            k=3,
            bandit=bandit,
            category="circle-packing",
            rng=random.Random(1),
            runner=runner,
            per_attempt_timeout_seconds=5.0,
            executor=ex,
        )
    assert len(result.attempts) == 3
    assert result.k_completed == 3
