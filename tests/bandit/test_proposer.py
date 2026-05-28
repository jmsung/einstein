"""Tests for the Thompson bandit meta-loop proposer (Goal 6).

Confirms the swap surface (the `Callable[[ProposerInput], list[dict]]`
contract) works end-to-end with a real non-LLM proposer:
  - direct call: tagged manifest_tweak dict with `thompson-bandit-v0`
  - round-trip through `propose.run`: pending proposal carries the id
  - meta_gate audit row distinguishes bandit from LLM proposals
"""

from __future__ import annotations

import datetime as dt
from pathlib import Path

import pytest

from einstein.bandit import THOMPSON_PROPOSER_ID, thompson_proposer
from einstein.bandit.proposer import MANIFEST_TARGET
from einstein.meta_loop import meta_gate, propose
from einstein.meta_loop.proposals import (
    VALID_PROPOSAL_TYPES,
    Proposal,
    ProposalStore,
    ProposalType,
)


def _now() -> dt.datetime:
    return dt.datetime(2026, 5, 27, 12, 0, 0, tzinfo=dt.timezone.utc)


@pytest.fixture
def fake_repo(tmp_path: Path) -> dict[str, Path]:
    """Same shape as tests/meta_loop/test_propose.py::fake_repo."""
    cycle_log = tmp_path / "agent" / "cycle-log.md"
    skill_library = tmp_path / "agent" / "skill-library.md"
    findings_dir = tmp_path / "wiki" / "findings"
    questions_dir = tmp_path / "wiki" / "questions"
    for d in (cycle_log.parent, findings_dir, questions_dir):
        d.mkdir(parents=True, exist_ok=True)
    cycle_log.write_text(
        "# cycle log\n\n"
        "| # | problem | start → end score | hours | compute | wiki cites "
        "| findings+ | concepts+ | author mix | outcome | notes |\n"
        "|---|---|---|---|---|---|---|---|---|---|---|\n"
        "| 100 | P14 | 2.6 → 2.6 | 0 | local | 0 | 1 | 0 | a:1 | dead-end "
        "| manifest-blocked |\n"
        "| 101 | P22 | 2.0 → 1.9 | 0 | local | 0 | 0 | 0 | a:1 | improved-local "
        "| strategy=thompson-bandit; technique=slsqp.md |\n"
    )
    skill_library.write_text(
        "# skill\n\n| technique | category | tried | top3 | finding | last_used | hit_rate |\n"
        "|---|---|---|---|---|---|---|\n"
        "| `slsqp.md` | packing | 6 | 4 | 1 | 2026-04-12 | 0.67 |\n"
        "| `parallel-tempering-sa.md` | kissing / Coulomb | 5 | 3 | 2 | 2026-04-25 | 0.60 |\n"
    )
    return {
        "cycle_log": cycle_log,
        "skill_library": skill_library,
        "findings_dir": findings_dir,
        "questions_dir": questions_dir,
        "mb_logs_dir": tmp_path / "mb-logs",
        "proposals_root": tmp_path / "proposals",
        "output": tmp_path / "mb-logs" / "meta-loop-report.md",
    }


# ---------------- direct call ----------------


def test_proposer_emits_tagged_manifest_tweak(fake_repo) -> None:
    inp = propose.ProposerInput(
        report_text="",
        cycle_log_path=fake_repo["cycle_log"],
        skill_library_path=fake_repo["skill_library"],
        findings_dir=fake_repo["findings_dir"],
        questions_dir=fake_repo["questions_dir"],
        mb_logs_dir=fake_repo["mb_logs_dir"],
    )
    raws = thompson_proposer(inp)
    assert len(raws) == 1
    r = raws[0]
    assert r["proposer_id"] == THOMPSON_PROPOSER_ID
    assert r["type"] == ProposalType.MANIFEST_TWEAK.value
    assert r["type"] in VALID_PROPOSAL_TYPES
    assert r["target_path"] == MANIFEST_TARGET
    # diff carries the bandit's best-arm-per-category recommendation
    assert "thompson-bandit-v0 recommendations" in r["proposed_diff"]
    assert "packing: slsqp.md" in r["proposed_diff"]
    assert "kissing: parallel-tempering-sa.md" in r["proposed_diff"]
    # evidence_cycles parsed from cycle-log tail
    assert r["evidence_cycles"] == [100, 101]


def test_proposer_empty_library_returns_no_proposals(tmp_path: Path) -> None:
    empty = tmp_path / "empty-skill-library.md"
    empty.write_text("# skill\n\n| technique | category | tried | top3 |\n")
    inp = propose.ProposerInput(
        report_text="",
        cycle_log_path=tmp_path / "no.md",
        skill_library_path=empty,
        findings_dir=tmp_path,
        questions_dir=tmp_path,
        mb_logs_dir=tmp_path,
    )
    assert thompson_proposer(inp) == []


# ---------------- round-trip through propose.run ----------------


def test_pending_proposal_carries_proposer_id(fake_repo) -> None:
    """propose.run with the bandit proposer → pending Proposal has provenance."""
    result = propose.run(proposer=thompson_proposer, now=_now(), **fake_repo)
    assert result.proposer_error is None
    assert len(result.written) == 1
    store = ProposalStore(fake_repo["proposals_root"])
    pending = store.list_pending()
    assert len(pending) == 1
    p = pending[0]
    assert p.proposer_id == THOMPSON_PROPOSER_ID
    assert p.type == ProposalType.MANIFEST_TWEAK.value
    assert p.target_path == MANIFEST_TARGET


# ---------------- audit row distinguishes bandit from LLM ----------------


def test_audit_row_carries_thompson_bandit_id(fake_repo, tmp_path: Path) -> None:
    """meta_gate.evaluate writes an audit row whose proposer_id == bandit's id."""
    raws = thompson_proposer(
        propose.ProposerInput(
            report_text="",
            cycle_log_path=fake_repo["cycle_log"],
            skill_library_path=fake_repo["skill_library"],
            findings_dir=fake_repo["findings_dir"],
            questions_dir=fake_repo["questions_dir"],
            mb_logs_dir=fake_repo["mb_logs_dir"],
        )
    )
    proposal = propose._coerce_raw(raws[0], now=_now())
    assert isinstance(proposal, Proposal)
    audit = tmp_path / "meta-proposals.md"
    meta_gate.evaluate(proposal, audit_log=audit)
    text = audit.read_text()
    assert THOMPSON_PROPOSER_ID in text
    # not tagged as legacy (the migration-shim default for empty proposer_id)
    assert "(legacy)" not in text
