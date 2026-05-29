"""Tests for src/einstein/meta_loop/proposals.py — schema + store."""

from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein.meta_loop.proposals import (  # noqa: E402
    Confidence,
    Proposal,
    ProposalStore,
    ProposalType,
    ProposalValidationError,
    make_proposal_id,
)

UTC = dt.timezone.utc


def _now() -> dt.datetime:
    return dt.datetime(2026, 5, 25, 12, 0, 0, tzinfo=UTC)


# ---------------- schema validation ----------------


def _minimal_kwargs(**overrides) -> dict:
    base = {
        "id": "test-prop-001",
        "type": ProposalType.NEW_QUESTION.value,
        "target_path": "docs/wiki/questions/2026-05-25-test-question.md",
        "proposed_diff": "---\ntype: question\n---\n\nbody\n",
        "evidence_cycles": [49, 50, 51],
        "expected_metric_delta": {"top3_per_cycle": 0.05},
        "predicted_regressions": ["none expected"],
        "confidence": Confidence.MEDIUM.value,
        "requires_shadow": False,
        "rationale": "test",
        "created_at": _now(),
        "author": "agent",
    }
    base.update(overrides)
    return base


def test_minimal_proposal_validates() -> None:
    p = Proposal(**_minimal_kwargs())
    assert p.type == ProposalType.NEW_QUESTION.value
    assert p.evidence_cycles == [49, 50, 51]


def test_invalid_type_rejected() -> None:
    with pytest.raises(ProposalValidationError, match="type="):
        Proposal(**_minimal_kwargs(type="code_edit"))  # deferred to Goal 5


def test_invalid_id_rejected() -> None:
    with pytest.raises(ProposalValidationError, match="id="):
        Proposal(**_minimal_kwargs(id="X bad spaces"))


def test_target_path_must_match_type_pattern() -> None:
    # rule_edit pointing at a non-rules file
    with pytest.raises(ProposalValidationError, match="target_path"):
        Proposal(
            **_minimal_kwargs(
                type=ProposalType.RULE_EDIT.value,
                target_path="src/einstein/optimizer.py",
            )
        )


def test_target_path_matches_for_rule_edit() -> None:
    # Should validate fine
    p = Proposal(
        **_minimal_kwargs(
            type=ProposalType.RULE_EDIT.value,
            target_path=".claude/rules/agent-stance.md",
            proposed_diff="--- a/rules\n+++ b/rules\n+new line\n",
        )
    )
    assert p.type == ProposalType.RULE_EDIT.value


# ---------------- meta_self_edit (recursive-meta) ----------------


def test_meta_self_edit_accepts_scripts_meta_loop_py() -> None:
    p = Proposal(
        **_minimal_kwargs(
            type=ProposalType.META_SELF_EDIT.value,
            target_path="scripts/meta_loop.py",
            proposed_diff="--- a/scripts/meta_loop.py\n+++ b/scripts/meta_loop.py\n+# diagnostic column\n",
            evidence_cycles=list(range(10)),  # 10 cycles to anticipate proposer/gate floor
        )
    )
    assert p.type == ProposalType.META_SELF_EDIT.value
    assert p.target_path == "scripts/meta_loop.py"


def test_meta_self_edit_rejects_src_einstein() -> None:
    # Scope whitelist: must touch only scripts/meta_loop.py — touching the
    # gate / proposer source would let the meta-loop bypass its own gates.
    with pytest.raises(ProposalValidationError, match="target_path"):
        Proposal(
            **_minimal_kwargs(
                type=ProposalType.META_SELF_EDIT.value,
                target_path="src/einstein/meta_loop/meta_gate.py",
                proposed_diff="--- a/x\n+++ b/x\n+ \n",
                evidence_cycles=list(range(10)),
            )
        )


def test_meta_self_edit_rejects_test_files() -> None:
    with pytest.raises(ProposalValidationError, match="target_path"):
        Proposal(
            **_minimal_kwargs(
                type=ProposalType.META_SELF_EDIT.value,
                target_path="tests/meta_loop/test_meta_gate.py",
                proposed_diff="--- a/x\n+++ b/x\n+ \n",
                evidence_cycles=list(range(10)),
            )
        )


def test_meta_self_edit_rejects_other_scripts() -> None:
    # Tightness check: scripts/autonomous_loop.py is also off-limits — the
    # queue_reorder pattern catches it, but meta_self_edit must not.
    with pytest.raises(ProposalValidationError, match="target_path"):
        Proposal(
            **_minimal_kwargs(
                type=ProposalType.META_SELF_EDIT.value,
                target_path="scripts/autonomous_loop.py",
                proposed_diff="--- a/x\n+++ b/x\n+ \n",
                evidence_cycles=list(range(10)),
            )
        )


def test_meta_self_edit_round_trips() -> None:
    p = Proposal(
        **_minimal_kwargs(
            type=ProposalType.META_SELF_EDIT.value,
            target_path="scripts/meta_loop.py",
            proposed_diff="--- a/scripts/meta_loop.py\n+++ b/scripts/meta_loop.py\n@@\n+# new column\n",
            evidence_cycles=list(range(10)),
            proposer_id="recursive-meta-v0",
            requires_shadow=True,
        )
    )
    text = p.to_markdown()
    assert "type: meta_self_edit" in text
    assert "proposer_id: recursive-meta-v0" in text
    p2 = Proposal.from_markdown(text)
    assert p2.type == ProposalType.META_SELF_EDIT.value
    assert p2.proposer_id == "recursive-meta-v0"
    assert p2.target_path == "scripts/meta_loop.py"


def test_invalid_confidence_rejected() -> None:
    with pytest.raises(ProposalValidationError, match="confidence"):
        Proposal(**_minimal_kwargs(confidence="extremely-sure"))


def test_negative_cycle_id_rejected() -> None:
    with pytest.raises(ProposalValidationError, match="evidence_cycles"):
        Proposal(**_minimal_kwargs(evidence_cycles=[-1]))


def test_blank_diff_rejected() -> None:
    with pytest.raises(ProposalValidationError, match="proposed_diff"):
        Proposal(**_minimal_kwargs(proposed_diff="   \n  \n"))


# ---------------- round-trip serialization ----------------


def test_round_trip_to_markdown_and_back() -> None:
    p = Proposal(**_minimal_kwargs())
    text = p.to_markdown()
    assert text.startswith("---\n")
    assert "id: test-prop-001" in text
    p2 = Proposal.from_markdown(text)
    assert p2.id == p.id
    assert p2.type == p.type
    assert p2.evidence_cycles == p.evidence_cycles
    assert p2.expected_metric_delta == p.expected_metric_delta
    # The body's trailing whitespace gets canonicalized — content equivalent
    assert p2.proposed_diff.strip() == p.proposed_diff.strip()
    assert p2.created_at == p.created_at


def test_proposer_id_round_trips() -> None:
    p = Proposal(**_minimal_kwargs(proposer_id="thompson-bandit-v0"))
    text = p.to_markdown()
    assert "proposer_id: thompson-bandit-v0" in text
    p2 = Proposal.from_markdown(text)
    assert p2.proposer_id == "thompson-bandit-v0"


def test_proposer_id_defaults_empty_when_absent() -> None:
    # A proposal constructed without proposer_id defaults to "" on the dataclass.
    p = Proposal(**_minimal_kwargs())
    assert p.proposer_id == ""
    # And a markdown file with no proposer_id key reads back as "".
    text = p.to_markdown().replace("proposer_id: ''\n", "")
    assert "proposer_id" not in text
    p2 = Proposal.from_markdown(text)
    assert p2.proposer_id == ""


def test_from_markdown_rejects_missing_frontmatter() -> None:
    with pytest.raises(ProposalValidationError, match="frontmatter"):
        Proposal.from_markdown("just body, no frontmatter\n")


def test_from_markdown_rejects_bad_yaml() -> None:
    text = "---\n!!! not yaml !!!: : : :\n---\n\nbody\n"
    with pytest.raises(ProposalValidationError):
        Proposal.from_markdown(text)


# ---------------- id helper ----------------


def test_make_proposal_id_deterministic() -> None:
    t = _now()
    a = make_proposal_id(
        proposal_type=ProposalType.RULE_EDIT.value,
        target_path=".claude/rules/x.md",
        now=t,
    )
    b = make_proposal_id(
        proposal_type=ProposalType.RULE_EDIT.value,
        target_path=".claude/rules/x.md",
        now=t,
    )
    assert a == b
    assert a.startswith("20260525t120000-")


def test_make_proposal_id_differs_by_inputs() -> None:
    t = _now()
    a = make_proposal_id(
        proposal_type=ProposalType.RULE_EDIT.value,
        target_path=".claude/rules/x.md",
        now=t,
    )
    b = make_proposal_id(
        proposal_type=ProposalType.RULE_EDIT.value,
        target_path=".claude/rules/y.md",
        now=t,
    )
    assert a != b


# ---------------- store ----------------


def test_store_creates_subdirs(tmp_path: Path) -> None:
    store = ProposalStore(tmp_path)
    for sub in ProposalStore.SUBDIRS:
        assert (tmp_path / sub).is_dir()


def test_store_writes_and_lists_pending(tmp_path: Path) -> None:
    store = ProposalStore(tmp_path)
    p = Proposal(**_minimal_kwargs())
    written = store.write_pending(p)
    assert written.exists()
    assert written.parent.name == "pending"
    listed = store.list_pending()
    assert len(listed) == 1
    assert listed[0].id == p.id


def test_store_refuses_collision(tmp_path: Path) -> None:
    store = ProposalStore(tmp_path)
    p = Proposal(**_minimal_kwargs())
    store.write_pending(p)
    with pytest.raises(FileExistsError):
        store.write_pending(p)


def test_store_move_pending_to_applied(tmp_path: Path) -> None:
    store = ProposalStore(tmp_path)
    p = Proposal(**_minimal_kwargs())
    store.write_pending(p)
    new_path = store.move(p.id, from_="pending", to="applied")
    assert new_path.parent.name == "applied"
    assert not (tmp_path / "pending" / f"{p.id}.md").exists()
    assert store.list_pending() == []
    assert len(store.list_applied()) == 1


def test_store_skips_malformed_files(tmp_path: Path) -> None:
    store = ProposalStore(tmp_path)
    (tmp_path / "pending" / "garbage.md").write_text("not a proposal at all")
    p = Proposal(**_minimal_kwargs())
    store.write_pending(p)
    # Only the valid one comes back
    assert len(store.list_pending()) == 1
