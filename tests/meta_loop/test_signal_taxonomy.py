"""Tests for meta_loop.signal_taxonomy (Phase 1 of js/feat/meta-learning-automation).

Classification is a pure function; routing writes deterministic artifacts to
tmp paths. Over-firing of the human-gated `promote` action is the key guard.
"""

from __future__ import annotations

import json
from pathlib import Path

from einstein.meta_loop.proposals import ProposalStore, ProposalType
from einstein.meta_loop.signal_taxonomy import (
    classify_signals,
    route_signals,
)


def _result(**kw) -> dict:
    base = {"outcome": "no-change", "notes": "autonomous_loop cycle —", "end_score": 1.0}
    base.update(kw)
    return base


# --------------------------------------------------------------- classify


def test_no_signal_on_plain_no_change() -> None:
    assert classify_signals(_result()) == []


def test_record_signal_from_outcome() -> None:
    sigs = classify_signals(_result(outcome="improved-and-submitted"))
    assert [s.name for s in sigs] == ["record"]


def test_record_signal_from_notes_marker() -> None:
    sigs = classify_signals(_result(notes="... auto-submit: SUBMITTED ..."))
    assert any(s.name == "record" for s in sigs)


def test_dead_end_signal_and_path_extraction() -> None:
    sigs = classify_signals(
        _result(outcome="dead-end", notes="dead_end=knowledge/wiki/findings/dead-end-x.md; foo")
    )
    de = [s for s in sigs if s.name == "dead_end"]
    assert de and de[0].destination == "knowledge/wiki/findings/dead-end-x.md"
    assert "What might still work" in de[0].action


def test_triple_verify_disagreement_signal() -> None:
    sigs = classify_signals(_result(notes="triple-verify=fail [fast=1 exact=2]"))
    assert any(s.name == "triple_verify_disagreement" for s in sigs)
    sigs2 = classify_signals(_result(notes="auto-submit-rejected@triple_verify"))
    assert any(s.name == "triple_verify_disagreement" for s in sigs2)


def test_cross_problem_mechanism_requires_two_problems() -> None:
    assert not any(
        s.name == "cross_problem_mechanism"
        for s in classify_signals(_result(), mechanism_problem_count=1)
    )
    sigs = classify_signals(_result(), mechanism_problem_count=2)
    cpm = [s for s in sigs if s.name == "cross_problem_mechanism"]
    assert cpm and cpm[0].human_gated


def test_prior_violated_only_when_record_and_floor_moved() -> None:
    # record + floor moved → fires
    sigs = classify_signals(
        _result(outcome="conquered", end_score=1.50285),
        prior_floor=1.50286,
    )
    assert any(s.name == "prior_violated" for s in sigs)
    # record but floor unchanged → does not fire
    sigs2 = classify_signals(
        _result(outcome="conquered", end_score=1.50286),
        prior_floor=1.50286,
    )
    assert not any(s.name == "prior_violated" for s in sigs2)
    # floor moved but NOT a record → does not fire
    sigs3 = classify_signals(_result(end_score=9.9), prior_floor=1.0)
    assert not any(s.name == "prior_violated" for s in sigs3)


# --------------------------------------------------------------- route


def test_route_always_appends_capture_queue(tmp_path: Path) -> None:
    q = tmp_path / "capture-queue.jsonl"
    sigs = classify_signals(_result(outcome="dead-end", notes="dead_end=f.md"))
    route_signals(sigs, capture_queue=q, cycle_id=7, problem="P2-x")
    lines = q.read_text().splitlines()
    assert len(lines) == 1
    rec = json.loads(lines[0])
    assert rec["signal"] == "dead_end"
    assert rec["cycle_id"] == 7 and rec["problem"] == "P2-x"


def test_route_promotion_candidate_deduped(tmp_path: Path) -> None:
    q = tmp_path / "q.jsonl"
    plog = tmp_path / "promotion-log.md"
    sigs = classify_signals(_result(), mechanism_problem_count=2)
    # first time → row written
    acts = route_signals(
        sigs, capture_queue=q, promotion_log=plog, mechanism_key="warm-self-pruning"
    )
    assert any(a.action == "promotion-candidate" and a.performed for a in acts)
    assert "warm-self-pruning" in plog.read_text()
    # second time, same mechanism → deduped (not performed)
    acts2 = route_signals(
        sigs, capture_queue=q, promotion_log=plog, mechanism_key="warm-self-pruning"
    )
    assert any(a.action == "promotion-candidate" and not a.performed for a in acts2)
    assert plog.read_text().count("warm-self-pruning") == 1


def test_route_rule_edit_proposal_stub_and_dedupe(tmp_path: Path) -> None:
    q = tmp_path / "q.jsonl"
    store = ProposalStore(tmp_path / "proposals")
    sigs = classify_signals(_result(outcome="conquered", end_score=1.0), prior_floor=2.0)
    assert any(s.name == "prior_violated" for s in sigs)
    acts = route_signals(sigs, capture_queue=q, proposal_store=store, cycle_id=3)
    assert any(a.action == "rule_edit-proposal" and a.performed for a in acts)
    pending = store.list_pending()
    assert len(pending) == 1
    assert pending[0].type == ProposalType.RULE_EDIT.value
    assert pending[0].target_path.startswith(".claude/rules/")
    # re-route → deduped against the pending proposal for the same target
    acts2 = route_signals(sigs, capture_queue=q, proposal_store=store, cycle_id=4)
    assert any(a.action == "rule_edit-proposal" and not a.performed for a in acts2)
    assert len(store.list_pending()) == 1


def test_route_dry_run_writes_nothing(tmp_path: Path) -> None:
    q = tmp_path / "q.jsonl"
    plog = tmp_path / "p.md"
    sigs = classify_signals(_result(), mechanism_problem_count=2)
    acts = route_signals(sigs, capture_queue=q, promotion_log=plog, mechanism_key="m", dry_run=True)
    assert not q.exists()
    assert not plog.exists()
    assert all(not a.performed or a.action == "promotion-candidate" for a in acts)
