"""Tests for src/einstein/meta_loop/evolve.py — Goal 4 AlphaEvolve engine.

Covers the test-plan obligations: champion promotes only on strict improvement;
gated off certified-floor problems; reproducible under a fixed seed.
"""

from __future__ import annotations

import random
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

import pytest  # noqa: E402

from einstein.meta_loop import evolve as ev  # noqa: E402
from einstein.meta_loop.trajectory import Classification, ProblemClassification  # noqa: E402


@pytest.fixture
def isolated_registry():
    """Snapshot + restore the global triple-verify registry so these tests'
    register/clear calls don't wipe the real registrations other tests rely on."""
    from einstein.triple_verify import core as tv

    saved = dict(tv._REGISTRY)
    tv.clear_registry()
    try:
        yield tv
    finally:
        tv._REGISTRY.clear()
        tv._REGISTRY.update(saved)


# ---------------- strict_improvement ----------------


def test_strict_improvement_minimize():
    assert ev.strict_improvement(1.4, 1.5, minimize=True)
    assert not ev.strict_improvement(1.5, 1.5, minimize=True)  # equal not strict
    assert not ev.strict_improvement(1.6, 1.5, minimize=True)


def test_strict_improvement_maximize():
    assert ev.strict_improvement(0.55, 0.5, minimize=False)
    assert not ev.strict_improvement(0.5, 0.5, minimize=False)


def test_strict_improvement_respects_min_improvement_margin():
    # a 1e-9 gain does not clear a 1e-6 margin
    assert not ev.strict_improvement(1.5 - 1e-9, 1.5, minimize=True, min_improvement=1e-6)
    assert ev.strict_improvement(1.5 - 1e-3, 1.5, minimize=True, min_improvement=1e-6)


# ---------------- select_best ----------------


def test_select_best_skips_unverified_and_picks_min():
    scored = [({"a": 1}, None), ({"a": 2}, 1.6), ({"a": 3}, 1.4), ({"a": 4}, None)]
    payload, score = ev.select_best(scored, minimize=True)
    assert payload == {"a": 3} and score == 1.4


def test_select_best_none_when_nothing_verifies():
    assert ev.select_best([({"a": 1}, None)], minimize=True) is None


def test_select_best_ties_keep_earliest():
    scored = [({"id": 1}, 1.5), ({"id": 2}, 1.5)]
    payload, _ = ev.select_best(scored, minimize=True)
    assert payload == {"id": 1}


# ---------------- evolve_step ----------------


def test_evolve_step_promotes_on_strict_improvement():
    champ = ev.Champion(score=1.5, payload={"v": 0})
    candidates = [{"v": 1}, {"v": 2}, {"v": 3}]
    scores = {0: None, 1: 1.55, 2: 1.45, 3: 1.50}  # by payload["v"]
    res = ev.evolve_step(champ, candidates, lambda p: scores[p["v"]], minimize=True)
    assert res.promoted is True
    assert res.champion.score == 1.45 and res.champion.payload == {"v": 2}
    assert res.n_candidates == 3 and res.n_verified == 3


def test_evolve_step_keeps_champion_when_no_candidate_beats_it():
    champ = ev.Champion(score=1.5, payload={"v": 0})
    res = ev.evolve_step(champ, [{"v": 1}, {"v": 2}], lambda p: 1.6, minimize=True)
    assert res.promoted is False
    assert res.champion is champ  # unchanged object
    assert res.best_candidate_score == 1.6


def test_evolve_step_handles_all_unverified():
    champ = ev.Champion(score=1.5, payload={})
    res = ev.evolve_step(champ, [{"v": 1}], lambda p: None, minimize=True)
    assert res.promoted is False and res.n_verified == 0
    assert res.best_candidate_score is None
    assert res.champion is champ


# ---------------- evolve loop ----------------


def _descending_mutator(champ, k, rng):
    """Deterministic mutator: each candidate is a small rng-jittered improvement
    on the champion's score (minimize). Reproducible under a seeded rng."""
    return [{"score": champ.score - 0.01 * (i + 1) - rng.random() * 1e-9} for i in range(k)]


def test_evolve_climbs_and_is_monotone():
    champ = ev.Champion(score=2.0, payload={"score": 2.0})
    run = ev.evolve(
        champ,
        generations=3,
        k=4,
        mutator=_descending_mutator,
        verify_fn=lambda p: p["score"],
        rng=random.Random(7),
        minimize=True,
    )
    # champion strictly decreases each generation (monotone)
    seq = [g.champion.score for g in run.generations]
    assert seq == sorted(seq, reverse=True)
    assert run.final_champion.score < 2.0
    assert run.total_promotions == 3 and run.improved


def test_evolve_reproducible_under_fixed_seed():
    champ = ev.Champion(score=2.0, payload={"score": 2.0})
    kw = dict(
        generations=3,
        k=4,
        mutator=_descending_mutator,
        verify_fn=lambda p: p["score"],
        minimize=True,
    )
    a = ev.evolve(champ, rng=random.Random(42), **kw)
    b = ev.evolve(champ, rng=random.Random(42), **kw)
    assert a.final_champion.score == b.final_champion.score
    assert [g.champion.score for g in a.generations] == [g.champion.score for g in b.generations]


def test_evolve_does_not_regress_when_mutants_are_worse():
    champ = ev.Champion(score=1.0, payload={"score": 1.0})
    run = ev.evolve(
        champ,
        generations=5,
        k=3,
        mutator=lambda c, k, rng: [{"score": 1.0 + 0.1 * (i + 1)} for i in range(k)],
        verify_fn=lambda p: p["score"],
        rng=random.Random(1),
        minimize=True,
    )
    assert run.final_champion.score == 1.0  # never promoted a worse mutant
    assert run.total_promotions == 0


# ---------------- the gate ----------------


def _pc(cls):
    return ProblemClassification(1, "P1", cls, [], 0.05, None)


def test_should_evolve_only_for_stuck():
    assert ev.should_evolve(_pc(Classification.STUCK)) is True
    assert ev.should_evolve(_pc(Classification.SOLVED_AT_FLOOR)) is False
    assert ev.should_evolve(_pc(Classification.IMPROVING)) is False
    assert ev.should_evolve(_pc(Classification.UNKNOWN)) is False


# ---------------- triple-verify adapter ----------------


def test_triple_verify_score_fn_returns_score_on_pass(isolated_registry):
    tv = isolated_registry
    tv.register(99, fast=lambda s: s["x"], exact=lambda s: s["x"], cross=lambda s: s["x"])
    assert ev.triple_verify_score_fn(99)({"x": 1.5}) == 1.5


def test_triple_verify_score_fn_none_when_unregistered(isolated_registry):
    assert ev.triple_verify_score_fn(12345)({"x": 1.0}) is None


def test_triple_verify_score_fn_none_on_disagreement(isolated_registry):
    tv = isolated_registry
    tv.register(
        98,
        fast=lambda s: 1.0,
        exact=lambda s: 1.0,
        cross=lambda s: 9.0,  # disagrees → not passed
    )
    assert ev.triple_verify_score_fn(98)({"x": 1.0}) is None
