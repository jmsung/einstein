"""Tests for src/einstein/meta_loop/code_edit.py — Goal 2 draft-writer."""

from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein.meta_loop.code_edit import (  # noqa: E402
    PROPOSER_ID,
    apply_code_edit_to_worktree,
    make_code_edit_proposal,
)
from einstein.meta_loop.proposals import (  # noqa: E402
    Proposal,
    ProposalStore,
    ProposalType,
    ProposalValidationError,
)
from einstein.meta_loop.tool_gaps import ToolGap  # noqa: E402

UTC = dt.timezone.utc


def _now() -> dt.datetime:
    return dt.datetime(2026, 5, 31, 12, 0, 0, tzinfo=UTC)


def _gap(
    *,
    suggested: str | None = "mpmath-ulp-polish",
    cycles: list[int] | None = None,
    problems: list[str] | None = None,
    pattern: str = "manifest_gap",
) -> ToolGap:
    cycles = cycles or [49, 50, 70]
    problems = problems or ["P14", "P12"]
    return ToolGap(
        canonical=f"manifest_gap:{suggested}" if suggested else "manifest_or_dispatch_gap",
        pattern=pattern,
        suggested_tool=suggested,
        missing_manifest_entry="newton_max",
        citing_cycles=cycles,
        problem_ids=problems,
        open_questions=[],
    )


# ---------------- type validity ----------------


def test_code_edit_now_in_valid_types() -> None:
    """The schema must accept code_edit (no longer deferred)."""
    assert ProposalType.CODE_EDIT.value == "code_edit"


def test_code_edit_target_path_pattern_accepts_scripts_proposed() -> None:
    p = make_code_edit_proposal(_gap(), now=_now())
    assert p.type == "code_edit"
    assert p.target_path.startswith("scripts/proposed/")
    assert p.target_path.endswith(".py")
    # Schema validation must have passed
    p._validate()


def test_code_edit_target_path_rejects_scripts_root() -> None:
    """A code_edit cannot target `scripts/foo.py` directly — only proposed/."""
    with pytest.raises(ProposalValidationError, match="target_path"):
        Proposal(
            id="test-code-edit-001",
            type=ProposalType.CODE_EDIT.value,
            target_path="scripts/foo.py",
            proposed_diff="x",
            confidence="low",
            requires_shadow=True,
            created_at=_now(),
        )


# ---------------- make_code_edit_proposal ----------------


def test_make_code_edit_proposal_below_threshold_raises() -> None:
    g = _gap(cycles=[49], problems=["P14"])
    with pytest.raises(ProposalValidationError, match="below threshold"):
        make_code_edit_proposal(g, now=_now())


def test_make_code_edit_proposal_carries_evidence_and_proposer_id() -> None:
    p = make_code_edit_proposal(_gap(), now=_now())
    assert p.evidence_cycles == [49, 50, 70]
    assert p.proposer_id == PROPOSER_ID
    assert p.requires_shadow is True
    assert "mpmath-ulp-polish" in p.target_path


def test_draft_body_contains_cite_block_and_notimplemented() -> None:
    p = make_code_edit_proposal(_gap(), now=_now())
    body = p.proposed_diff
    assert "Citation block" in body
    assert "mpmath-ulp-polish" in body
    assert "NotImplementedError" in body
    # Evidence cycles surface in the cite block
    assert "49" in body and "50" in body and "70" in body
    # Provenance is named
    assert PROPOSER_ID in body


def test_draft_body_uses_snake_case_python_identifier() -> None:
    p = make_code_edit_proposal(_gap(suggested="algebraic-construction-flat-poly"), now=_now())
    # Python def must be a valid identifier
    assert "def algebraic_construction_flat_poly(" in p.proposed_diff


def test_make_code_edit_fungible_marker_synthesizes_slug() -> None:
    """When the gap has no suggested_tool, synthesize a slug from pattern + problems."""
    g = _gap(
        suggested=None,
        cycles=[45, 46, 47],
        problems=["P1", "P9"],
        pattern="manifest_or_dispatch_gap",
    )
    p = make_code_edit_proposal(g, now=_now())
    slug = Path(p.target_path).stem
    # Synthesized slug embeds the problems and pattern
    assert "p1" in slug
    assert "p9" in slug
    assert "manifest-or-dispatch-gap" in slug


# ---------------- apply_code_edit_to_worktree ----------------


def test_apply_code_edit_to_worktree_writes_to_proposed(tmp_path: Path) -> None:
    p = make_code_edit_proposal(_gap(), now=_now())
    out = apply_code_edit_to_worktree(p, tmp_path)
    expected = tmp_path / "scripts" / "proposed" / "mpmath-ulp-polish.py"
    assert out == expected
    assert expected.is_file()
    assert "NotImplementedError" in expected.read_text()


def test_apply_code_edit_refuses_overwrite_in_proposed(tmp_path: Path) -> None:
    p = make_code_edit_proposal(_gap(), now=_now())
    apply_code_edit_to_worktree(p, tmp_path)
    with pytest.raises(FileExistsError, match="draft already exists"):
        apply_code_edit_to_worktree(p, tmp_path)


def test_apply_code_edit_refuses_when_scripts_root_taken(tmp_path: Path) -> None:
    """If `scripts/<slug>.py` already exists (e.g. graduated), refuse."""
    (tmp_path / "scripts").mkdir()
    (tmp_path / "scripts" / "mpmath-ulp-polish.py").write_text("# existing tool\n")
    p = make_code_edit_proposal(_gap(), now=_now())
    with pytest.raises(FileExistsError, match="already exists"):
        apply_code_edit_to_worktree(p, tmp_path)


def test_apply_code_edit_rejects_wrong_type(tmp_path: Path) -> None:
    p = Proposal(
        id="not-code-edit",
        type=ProposalType.NEW_QUESTION.value,
        target_path="knowledge/wiki/questions/2026-05-31-x.md",
        proposed_diff="x\n",
        confidence="low",
        requires_shadow=False,
        created_at=_now(),
    )
    with pytest.raises(ValueError, match="expected code_edit"):
        apply_code_edit_to_worktree(p, tmp_path)


# ---------------- ProposalStore round-trip ----------------


def test_proposal_store_round_trip_for_code_edit(tmp_path: Path) -> None:
    p = make_code_edit_proposal(_gap(), now=_now())
    store = ProposalStore(tmp_path)
    path = store.write_pending(p)
    assert path.is_file()
    pending = store.list_pending()
    assert len(pending) == 1
    rt = pending[0]
    assert rt.id == p.id
    assert rt.type == p.type
    assert rt.target_path == p.target_path
    assert rt.proposer_id == PROPOSER_ID
    assert rt.requires_shadow is True


def test_proposal_store_collision_refused(tmp_path: Path) -> None:
    p = make_code_edit_proposal(_gap(), now=_now())
    store = ProposalStore(tmp_path)
    store.write_pending(p)
    with pytest.raises(FileExistsError):
        store.write_pending(p)
