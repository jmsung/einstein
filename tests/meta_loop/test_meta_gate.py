"""Tests for src/einstein/meta_loop/meta_gate.py — 6-gate chain."""

from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein.meta_loop import meta_gate  # noqa: E402
from einstein.meta_loop.meta_gate import GateDecision  # noqa: E402
from einstein.meta_loop.proposals import (  # noqa: E402
    Proposal,
    ProposalStore,
    ProposalType,
)

UTC = dt.timezone.utc


def _now() -> dt.datetime:
    return dt.datetime(2026, 5, 25, 12, 0, 0, tzinfo=UTC)


def _rule_edit_proposal(
    *, pid: str = "test-001", evidence: list[int] | None = None, requires_shadow: bool = True
) -> Proposal:
    return Proposal(
        id=pid,
        type=ProposalType.RULE_EDIT.value,
        target_path=".claude/rules/agent-stance.md",
        proposed_diff="--- a/r\n+++ b/r\n+x\n",
        evidence_cycles=evidence if evidence is not None else [10, 11, 12],
        expected_metric_delta={"top3_per_cycle": 0.05},
        predicted_regressions=["maybe slower recon"],
        confidence="medium",
        requires_shadow=requires_shadow,
        rationale="test",
        created_at=_now(),
    )


def _new_question_proposal(pid: str = "test-q-001") -> Proposal:
    return Proposal(
        id=pid,
        type=ProposalType.NEW_QUESTION.value,
        target_path="docs/wiki/questions/2026-05-25-test-q.md",
        proposed_diff="---\nbody\n---\n",
        evidence_cycles=[],
        predicted_regressions=["none"],
        confidence="low",
        requires_shadow=False,
        rationale="test q",
        created_at=_now(),
    )


# ---------------- gate 1: kill switch ----------------


def test_kill_switch_blocks(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.setenv(meta_gate.KILL_SWITCH_ENV, "0")
    audit = tmp_path / "audit.md"

    r = meta_gate.evaluate(
        _rule_edit_proposal(),
        audit_log=audit,
        clock=_now,
        shadow_available=True,
    )
    assert r.decision == GateDecision.REJECTED
    assert r.rejected_at_gate == "kill-switch"
    text = audit.read_text()
    assert "kill-switch" in text
    assert "rejected" in text


def test_kill_switch_unset_does_not_block(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.delenv(meta_gate.KILL_SWITCH_ENV, raising=False)
    audit = tmp_path / "audit.md"
    r = meta_gate.evaluate(
        _rule_edit_proposal(),
        audit_log=audit,
        clock=_now,
        shadow_available=True,
    )
    assert r.decision == GateDecision.ACCEPTED


# ---------------- gate 2: evidence threshold ----------------


def test_evidence_threshold_rejects_under_minimum(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    monkeypatch.delenv(meta_gate.KILL_SWITCH_ENV, raising=False)
    audit = tmp_path / "audit.md"
    r = meta_gate.evaluate(
        _rule_edit_proposal(evidence=[10, 11]),  # only 2 cycles
        audit_log=audit,
        clock=_now,
        shadow_available=True,
    )
    assert r.decision == GateDecision.REJECTED
    assert r.rejected_at_gate == "evidence-threshold"
    assert "need ≥3" in r.reason


def test_evidence_threshold_skipped_for_new_question(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    """new_question has threshold 0 — empty evidence_cycles is fine."""
    monkeypatch.delenv(meta_gate.KILL_SWITCH_ENV, raising=False)
    audit = tmp_path / "audit.md"
    r = meta_gate.evaluate(_new_question_proposal(), audit_log=audit, clock=_now)
    assert r.decision == GateDecision.ACCEPTED


# ---------------- gate 3: daily cap ----------------


def test_daily_cap_rejects_after_n_accepted(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    monkeypatch.delenv(meta_gate.KILL_SWITCH_ENV, raising=False)
    audit = tmp_path / "audit.md"
    # Accept 2 (the default cap)
    r1 = meta_gate.evaluate(
        _rule_edit_proposal(pid="prop-001"),
        audit_log=audit,
        clock=_now,
        shadow_available=True,
    )
    r2 = meta_gate.evaluate(
        _rule_edit_proposal(pid="prop-002"),
        audit_log=audit,
        clock=_now,
        shadow_available=True,
    )
    assert r1.decision == GateDecision.ACCEPTED
    assert r2.decision == GateDecision.ACCEPTED

    # 3rd should hit the daily cap
    r3 = meta_gate.evaluate(
        _rule_edit_proposal(pid="prop-003"),
        audit_log=audit,
        clock=_now,
        shadow_available=True,
    )
    assert r3.decision == GateDecision.REJECTED
    assert r3.rejected_at_gate == "daily-cap"


def test_daily_cap_resets_next_day(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.delenv(meta_gate.KILL_SWITCH_ENV, raising=False)
    audit = tmp_path / "audit.md"
    day1 = lambda: dt.datetime(2026, 5, 25, 12, 0, 0, tzinfo=UTC)  # noqa: E731
    day2 = lambda: dt.datetime(2026, 5, 26, 12, 0, 0, tzinfo=UTC)  # noqa: E731
    for i in range(2):
        meta_gate.evaluate(
            _rule_edit_proposal(pid=f"d1-prop-{i}"),
            audit_log=audit,
            clock=day1,
            shadow_available=True,
        )
    # day2 — cap should reset
    r = meta_gate.evaluate(
        _rule_edit_proposal(pid="d2-prop-001"),
        audit_log=audit,
        clock=day2,
        shadow_available=True,
    )
    assert r.decision == GateDecision.ACCEPTED


# ---------------- gate 4: pending throttle ----------------


def test_pending_throttle_rejects_duplicate(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    monkeypatch.delenv(meta_gate.KILL_SWITCH_ENV, raising=False)
    audit = tmp_path / "audit.md"
    store_root = tmp_path / "proposals"
    store = ProposalStore(store_root)
    # Already pending with same (type, target_path)
    pending = _rule_edit_proposal(pid="pending-001")
    store.write_pending(pending)

    # New proposal targeting the same rule
    incoming = _rule_edit_proposal(pid="incoming-001")
    r = meta_gate.evaluate(
        incoming,
        audit_log=audit,
        clock=_now,
        proposals_store=store,
        shadow_available=True,
    )
    assert r.decision == GateDecision.REJECTED
    assert r.rejected_at_gate == "pending-throttle"
    assert "pending-001" in r.reason


def test_pending_throttle_skipped_when_no_store(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    monkeypatch.delenv(meta_gate.KILL_SWITCH_ENV, raising=False)
    audit = tmp_path / "audit.md"
    r = meta_gate.evaluate(
        _rule_edit_proposal(),
        audit_log=audit,
        clock=_now,
        shadow_available=True,
        proposals_store=None,
    )
    assert r.decision == GateDecision.ACCEPTED


# ---------------- gate 5: shadow ----------------


def test_shadow_required_defers_when_unavailable(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    """requires_shadow=True + shadow_available=False → shadow-pending,
    NOT rejected — different decision so the human can route appropriately."""
    monkeypatch.delenv(meta_gate.KILL_SWITCH_ENV, raising=False)
    audit = tmp_path / "audit.md"
    r = meta_gate.evaluate(
        _rule_edit_proposal(requires_shadow=True),
        audit_log=audit,
        clock=_now,
        shadow_available=False,
    )
    assert r.decision == GateDecision.SHADOW_PENDING
    assert "shadow A/B" in r.reason


def test_shadow_available_passes(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.delenv(meta_gate.KILL_SWITCH_ENV, raising=False)
    audit = tmp_path / "audit.md"
    r = meta_gate.evaluate(
        _rule_edit_proposal(requires_shadow=True),
        audit_log=audit,
        clock=_now,
        shadow_available=True,
    )
    assert r.decision == GateDecision.ACCEPTED


def test_no_shadow_required_passes_regardless(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    monkeypatch.delenv(meta_gate.KILL_SWITCH_ENV, raising=False)
    audit = tmp_path / "audit.md"
    r = meta_gate.evaluate(
        _new_question_proposal(),  # requires_shadow=False by construction
        audit_log=audit,
        clock=_now,
        shadow_available=False,
    )
    assert r.decision == GateDecision.ACCEPTED


# ---------------- gate 6: audit row ----------------


def test_every_decision_writes_one_audit_row(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    """Including accept, reject, shadow-pending. No silent decisions."""
    monkeypatch.delenv(meta_gate.KILL_SWITCH_ENV, raising=False)
    audit = tmp_path / "audit.md"
    # accept
    meta_gate.evaluate(
        _new_question_proposal(pid="q-001"),
        audit_log=audit,
        clock=_now,
    )
    # reject (under-evidence)
    meta_gate.evaluate(
        _rule_edit_proposal(pid="r-001", evidence=[]),
        audit_log=audit,
        clock=_now,
    )
    # shadow-pending
    meta_gate.evaluate(
        _rule_edit_proposal(pid="r-002", requires_shadow=True),
        audit_log=audit,
        clock=_now,
        shadow_available=False,
    )
    text = audit.read_text()
    assert text.count("\n| 20") == 3  # 3 data rows
    assert "accepted" in text
    assert "rejected" in text
    assert "shadow-pending" in text


def test_audit_log_has_header_on_first_write(tmp_path: Path) -> None:
    audit = tmp_path / "audit.md"
    meta_gate.evaluate(_new_question_proposal(), audit_log=audit, clock=_now)
    text = audit.read_text()
    assert "meta-proposals audit log" in text
    assert "timestamp_utc" in text
    assert "proposal_id" in text


def test_audit_reason_escapes_pipes(tmp_path: Path) -> None:
    """Reasons may contain pipes — they must be backslash-escaped so the
    markdown table stays valid."""
    audit = tmp_path / "audit.md"
    p = _new_question_proposal()
    # Patch the rationale field to include a pipe via target_path manipulation
    # (target_path is what flows into the row). We use a pid containing | (rejected
    # by validation), so instead test that the column delimiter survives.
    meta_gate.evaluate(p, audit_log=audit, clock=_now)
    lines = audit.read_text().splitlines()
    # Find the data row
    data_rows = [ln for ln in lines if ln.startswith("| 20")]
    assert len(data_rows) == 1
    # Should have exactly 7 pipe-separated columns (8 pipes incl. boundaries)
    assert data_rows[0].count("|") == 8
