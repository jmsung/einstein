"""Tests for src/einstein/meta_loop/review.py — accept/reject CLI."""

from __future__ import annotations

import datetime as dt
import subprocess
import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein.meta_loop.proposals import Proposal, ProposalStore, ProposalType  # noqa: E402
from einstein.meta_loop.review import (  # noqa: E402
    GitRunResult,
    ReviewDecision,
    ReviewSummary,
    accept_proposal,
    list_pending,
    reject_proposal,
    review_pending,
)

UTC = dt.timezone.utc


def _now() -> dt.datetime:
    return dt.datetime(2026, 5, 25, 12, 0, 0, tzinfo=UTC)


def _new_question(pid: str = "test-q-001", target: str | None = None) -> Proposal:
    return Proposal(
        id=pid,
        type=ProposalType.NEW_QUESTION.value,
        target_path=target or "knowledge/wiki/questions/2026-05-25-test-q.md",
        proposed_diff="---\ntype: question\nauthor: agent\n---\n\nbody\n",
        evidence_cycles=[],
        predicted_regressions=["none"],
        confidence="low",
        requires_shadow=False,
        rationale="test",
        created_at=_now(),
    )


def _rule_edit(pid: str = "test-r-001") -> Proposal:
    return Proposal(
        id=pid,
        type=ProposalType.RULE_EDIT.value,
        target_path=".claude/rules/agent-stance.md",
        proposed_diff=(
            "--- a/.claude/rules/agent-stance.md\n"
            "+++ b/.claude/rules/agent-stance.md\n"
            "@@ -1,1 +1,2 @@\n"
            " existing line\n"
            "+new line\n"
        ),
        evidence_cycles=[10, 11, 12],
        predicted_regressions=["maybe slower recon"],
        confidence="medium",
        requires_shadow=False,
        rationale="add a rule",
        created_at=_now(),
    )


# ---------------- Fake git runner ----------------


@pytest.fixture
def fake_git():
    """Record-only git runner — always succeeds and returns 'FAKE_SHA_12345...'."""
    calls: list[tuple[list[str], Path, str | None]] = []

    def runner(args: list[str], cwd: Path, stdin: str | None) -> GitRunResult:
        calls.append((args, cwd, stdin))
        if args[:1] == ["rev-parse"]:
            return GitRunResult(ok=True, stdout="FAKE_SHA_1234567890\n", returncode=0)
        return GitRunResult(ok=True, returncode=0)

    runner.calls = calls  # type: ignore[attr-defined]
    return runner


# ---------------- ReviewDecision validation ----------------


def test_review_decision_rejects_unknown_action() -> None:
    with pytest.raises(ValueError, match="unknown action"):
        ReviewDecision("id", "approve")


# ---------------- accept_proposal: new_question ----------------


def test_accept_new_question_writes_file_and_moves(tmp_path: Path, fake_git) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    store = ProposalStore(tmp_path / "proposals")
    proposal = _new_question()
    store.write_pending(proposal)

    outcome = accept_proposal(
        proposal,
        repo_root=repo,
        store=store,
        git_runner=fake_git,
    )
    assert outcome.error is None
    assert outcome.commit_sha == "FAKE_SHA_1234567890"
    # File created at target_path
    assert (repo / proposal.target_path).is_file()
    # Moved out of pending
    assert store.list_pending() == []
    assert len(store.list_applied()) == 1
    # The applied file has the commit SHA annotation
    applied_text = (tmp_path / "proposals" / "applied" / f"{proposal.id}.md").read_text()
    assert "commit=FAKE_SHA_1234567890" in applied_text


def test_accept_new_question_refuses_existing_target(tmp_path: Path, fake_git) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    store = ProposalStore(tmp_path / "proposals")
    proposal = _new_question()
    store.write_pending(proposal)

    # Pre-create the target file → accept must refuse
    target = repo / proposal.target_path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("already exists\n")

    outcome = accept_proposal(
        proposal,
        repo_root=repo,
        store=store,
        git_runner=fake_git,
    )
    assert outcome.error is not None
    assert "already exists" in outcome.error
    # Stays in pending since we didn't move it
    assert len(store.list_pending()) == 1


# ---------------- accept_proposal: rule_edit ----------------


def test_accept_rule_edit_runs_git_apply(tmp_path: Path, fake_git) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    store = ProposalStore(tmp_path / "proposals")
    proposal = _rule_edit()
    store.write_pending(proposal)

    outcome = accept_proposal(
        proposal,
        repo_root=repo,
        store=store,
        git_runner=fake_git,
    )
    assert outcome.error is None
    assert outcome.commit_sha == "FAKE_SHA_1234567890"
    # First call should be git apply with diff on stdin
    args, cwd, stdin = fake_git.calls[0]
    assert args[0] == "apply"
    assert stdin and "new line" in stdin
    # Moved to applied
    assert len(store.list_applied()) == 1


def test_accept_propagates_git_apply_failure(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    store = ProposalStore(tmp_path / "proposals")
    proposal = _rule_edit()
    store.write_pending(proposal)

    def runner(args, cwd, stdin):
        if args[0] == "apply":
            return GitRunResult(ok=False, stderr="bad diff", returncode=1)
        return GitRunResult(ok=True)

    outcome = accept_proposal(
        proposal,
        repo_root=repo,
        store=store,
        git_runner=runner,
    )
    assert outcome.error is not None
    assert "bad diff" in outcome.error
    # Stays in pending
    assert len(store.list_pending()) == 1


# ---------------- reject_proposal ----------------


def test_reject_moves_to_rejected_with_reason(tmp_path: Path) -> None:
    store = ProposalStore(tmp_path / "proposals")
    proposal = _new_question()
    store.write_pending(proposal)
    outcome = reject_proposal(proposal, store=store, reason="duplicates existing question")
    assert outcome.decision.action == "reject"
    assert outcome.moved_to.parent.name == "rejected"
    rejected_text = outcome.moved_to.read_text()
    assert "duplicates existing question" in rejected_text


# ---------------- review_pending: non-interactive ----------------


def test_review_pending_applies_decisions_list(tmp_path: Path, fake_git) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    store = ProposalStore(tmp_path / "proposals")

    p1 = _new_question(pid="q-001", target="knowledge/wiki/questions/2026-05-25-a.md")
    p2 = _new_question(pid="q-002", target="knowledge/wiki/questions/2026-05-25-b.md")
    p3 = _new_question(pid="q-003", target="knowledge/wiki/questions/2026-05-25-c.md")
    for p in (p1, p2, p3):
        store.write_pending(p)

    decisions = [
        ReviewDecision("q-001", "accept"),
        ReviewDecision("q-002", "reject", reason="not useful"),
        # q-003 not in the list → defaults to skip
    ]
    summary: ReviewSummary = review_pending(
        store,
        repo_root=repo,
        decisions=decisions,
        git_runner=fake_git,
    )
    assert len(summary.accepted) == 1
    assert len(summary.rejected) == 1
    assert len(summary.skipped) == 1
    assert len(summary.errored) == 0
    # q-001 applied, q-002 rejected, q-003 still pending
    assert {p.id for p in store.list_applied()} == {"q-001"}
    assert {p.id for p in store.list_rejected()} == {"q-002"}
    assert {p.id for p in store.list_pending()} == {"q-003"}


def test_review_pending_uses_prompt_fn_when_no_decisions(tmp_path: Path, fake_git) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    store = ProposalStore(tmp_path / "proposals")
    p = _new_question()
    store.write_pending(p)

    calls: list[Proposal] = []

    def prompt(prop):
        calls.append(prop)
        return ReviewDecision(prop.id, "skip")

    summary = review_pending(
        store,
        repo_root=repo,
        prompt_fn=prompt,
        git_runner=fake_git,
    )
    assert len(calls) == 1
    assert calls[0].id == p.id
    assert len(summary.skipped) == 1
    assert len(store.list_pending()) == 1  # skip leaves it


def test_review_pending_handles_apply_errors_in_outcome(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    store = ProposalStore(tmp_path / "proposals")
    p = _rule_edit()
    store.write_pending(p)

    def runner(args, cwd, stdin):
        if args[0] == "apply":
            return GitRunResult(ok=False, stderr="conflict", returncode=1)
        return GitRunResult(ok=True)

    summary = review_pending(
        store,
        repo_root=repo,
        decisions=[ReviewDecision(p.id, "accept")],
        git_runner=runner,
    )
    assert len(summary.errored) == 1
    assert "conflict" in summary.errored[0].error
    # Still in pending since accept failed
    assert len(store.list_pending()) == 1


# ---------------- list_pending ----------------


def test_list_pending_empty(tmp_path: Path) -> None:
    store = ProposalStore(tmp_path / "proposals")
    out = list_pending(store)
    assert "no pending" in out.lower()


def test_list_pending_shows_summary(tmp_path: Path) -> None:
    store = ProposalStore(tmp_path / "proposals")
    p = _new_question()
    store.write_pending(p)
    out = list_pending(store)
    assert p.id in out
    assert p.type in out
    assert p.target_path in out


# ---------------- end-to-end with a real local git repo ----------------


def _have_git() -> bool:
    try:
        subprocess.run(
            ["git", "--version"],
            capture_output=True,
            timeout=10,
            check=True,
        )
        return True
    except (subprocess.SubprocessError, FileNotFoundError, OSError):
        return False


@pytest.mark.skipif(not _have_git(), reason="git not on PATH")
def test_accept_against_real_git_repo(tmp_path: Path) -> None:
    """Verify the default git_runner path against a real init+commit cycle.

    Sanity check that the wiring (git apply, git add, git commit) actually
    works when not stubbed."""
    repo = tmp_path / "repo"
    repo.mkdir()
    # Initialize
    for args in (
        ["init", "-q"],
        ["config", "user.email", "test@example.com"],
        ["config", "user.name", "Test"],
        ["config", "commit.gpgsign", "false"],
    ):
        subprocess.run(["git", *args], cwd=repo, check=True, capture_output=True)
    # Need at least one commit so HEAD exists
    (repo / "seed").write_text("seed\n")
    subprocess.run(["git", "add", "seed"], cwd=repo, check=True, capture_output=True)
    subprocess.run(
        ["git", "commit", "-m", "init", "--no-verify"],
        cwd=repo,
        check=True,
        capture_output=True,
    )

    store = ProposalStore(tmp_path / "proposals")
    p = _new_question()
    store.write_pending(p)

    outcome = accept_proposal(p, repo_root=repo, store=store)
    assert outcome.error is None, outcome.error
    assert outcome.commit_sha is not None
    assert (repo / p.target_path).is_file()
    # Verify the commit landed
    log = subprocess.run(
        ["git", "log", "--oneline"],
        cwd=repo,
        capture_output=True,
        text=True,
        check=True,
    )
    assert "meta-loop" in log.stdout
