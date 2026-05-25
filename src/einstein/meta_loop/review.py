"""meta_loop.review — human-review surface for pending proposals (Goal 4).

Three actions per pending proposal:
  - accept → apply the diff to target_path, git-commit, move to mb/proposals/applied/
  - reject → move to mb/proposals/rejected/ with the human's reason appended
  - skip   → leave in pending/ for next pass

Application strategy depends on proposal type:
  - `new_question`           → proposed_diff IS the file body; write to target_path
  - rule_edit / others       → proposed_diff is a unified diff; `git apply` it

The git invocations are wrapped behind an injectable `git_runner` so tests
can verify control flow without touching the real worktree.
"""

from __future__ import annotations

import datetime as dt
import logging
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

from .proposals import Proposal, ProposalStore, ProposalType

log = logging.getLogger("meta_loop.review")


# ---------------- action contract ----------------


@dataclass
class ReviewDecision:
    """Human (or agent) decision on one pending proposal."""

    proposal_id: str
    action: str  # "accept" | "reject" | "skip"
    reason: str = ""

    def __post_init__(self) -> None:
        if self.action not in ("accept", "reject", "skip"):
            raise ValueError(f"unknown action: {self.action!r}")


@dataclass
class ReviewOutcome:
    proposal: Proposal
    decision: ReviewDecision
    commit_sha: str | None = None
    error: str | None = None
    moved_to: Path | None = None


@dataclass
class ReviewSummary:
    outcomes: list[ReviewOutcome] = field(default_factory=list)

    @property
    def accepted(self) -> list[ReviewOutcome]:
        return [o for o in self.outcomes if o.decision.action == "accept" and not o.error]

    @property
    def rejected(self) -> list[ReviewOutcome]:
        return [o for o in self.outcomes if o.decision.action == "reject"]

    @property
    def skipped(self) -> list[ReviewOutcome]:
        return [o for o in self.outcomes if o.decision.action == "skip"]

    @property
    def errored(self) -> list[ReviewOutcome]:
        return [o for o in self.outcomes if o.error]


# ---------------- git runner contract ----------------


@dataclass
class GitRunResult:
    ok: bool
    stdout: str = ""
    stderr: str = ""
    returncode: int = 0


GitRunner = Callable[[list[str], Path, str | None], GitRunResult]
"""Signature: git_runner(args, cwd, stdin) -> GitRunResult.

`args` excludes the leading `git`. `stdin` is the diff content or None.
"""


def _default_git_runner(args: list[str], cwd: Path, stdin: str | None) -> GitRunResult:
    """Real git subprocess. Tests inject a stub."""
    try:
        proc = subprocess.run(
            ["git", *args],
            cwd=cwd,
            input=stdin,
            capture_output=True,
            text=True,
            timeout=60,
        )
    except (subprocess.TimeoutExpired, FileNotFoundError) as e:
        return GitRunResult(ok=False, stderr=str(e), returncode=-1)
    return GitRunResult(
        ok=proc.returncode == 0,
        stdout=proc.stdout,
        stderr=proc.stderr,
        returncode=proc.returncode,
    )


# ---------------- apply / reject ----------------


def _commit_message(proposal: Proposal) -> str:
    short = (proposal.rationale[:60] + "…") if len(proposal.rationale) > 60 else proposal.rationale
    return (
        f"meta-loop({proposal.type}): apply {proposal.id}\n\n"
        f"target: {proposal.target_path}\n"
        f"evidence cycles: {proposal.evidence_cycles}\n"
        f"rationale: {short or '(none)'}\n"
    )


def _apply_new_question(
    proposal: Proposal, repo_root: Path, *, git_runner: GitRunner
) -> tuple[str | None, str | None]:
    """For NEW_QUESTION the diff IS the file body. Write + add + commit."""
    target = repo_root / proposal.target_path
    if target.exists():
        return None, f"target already exists: {target}"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(proposal.proposed_diff)
    add = git_runner(["add", proposal.target_path], repo_root, None)
    if not add.ok:
        return None, f"git add failed: {add.stderr.strip()}"
    commit = git_runner(["commit", "-m", _commit_message(proposal)], repo_root, None)
    if not commit.ok:
        return None, f"git commit failed: {commit.stderr.strip()}"
    sha = git_runner(["rev-parse", "HEAD"], repo_root, None)
    return sha.stdout.strip() if sha.ok else None, None


def _apply_unified_diff(
    proposal: Proposal, repo_root: Path, *, git_runner: GitRunner
) -> tuple[str | None, str | None]:
    """`git apply` the diff body, then add + commit the touched file."""
    apply_r = git_runner(["apply", "--whitespace=nowarn"], repo_root, proposal.proposed_diff)
    if not apply_r.ok:
        return None, f"git apply failed: {apply_r.stderr.strip()}"
    add = git_runner(["add", proposal.target_path], repo_root, None)
    if not add.ok:
        return None, f"git add failed: {add.stderr.strip()}"
    commit = git_runner(["commit", "-m", _commit_message(proposal)], repo_root, None)
    if not commit.ok:
        return None, f"git commit failed: {commit.stderr.strip()}"
    sha = git_runner(["rev-parse", "HEAD"], repo_root, None)
    return sha.stdout.strip() if sha.ok else None, None


def accept_proposal(
    proposal: Proposal,
    *,
    repo_root: Path,
    store: ProposalStore,
    git_runner: GitRunner | None = None,
) -> ReviewOutcome:
    """Apply the diff, commit, move pending → applied. Returns ReviewOutcome."""
    runner = git_runner or _default_git_runner
    if proposal.type == ProposalType.NEW_QUESTION.value:
        sha, err = _apply_new_question(proposal, repo_root, git_runner=runner)
    else:
        sha, err = _apply_unified_diff(proposal, repo_root, git_runner=runner)

    decision = ReviewDecision(proposal_id=proposal.id, action="accept", reason=sha or "")
    if err:
        return ReviewOutcome(proposal=proposal, decision=decision, error=err)

    # Annotate the proposal file with the commit SHA before moving it
    src = store._path("pending", proposal.id)  # noqa: SLF001 — friend-class shortcut
    if src.exists() and sha:
        appended = (
            src.read_text().rstrip()
            + f"\n\n<!-- applied at {dt.datetime.now(dt.timezone.utc).isoformat()} "
            + f"commit={sha} -->\n"
        )
        src.write_text(appended)
    moved = store.move(proposal.id, from_="pending", to="applied")
    return ReviewOutcome(proposal=proposal, decision=decision, commit_sha=sha, moved_to=moved)


def reject_proposal(
    proposal: Proposal,
    *,
    store: ProposalStore,
    reason: str,
) -> ReviewOutcome:
    """Move pending → rejected, with the reason appended to the proposal body."""
    src = store._path("pending", proposal.id)  # noqa: SLF001
    if src.exists():
        appended = (
            src.read_text().rstrip()
            + f"\n\n<!-- rejected at {dt.datetime.now(dt.timezone.utc).isoformat()} "
            + f"reason: {reason.replace('-->', '— ->')} -->\n"
        )
        src.write_text(appended)
    moved = store.move(proposal.id, from_="pending", to="rejected")
    return ReviewOutcome(
        proposal=proposal,
        decision=ReviewDecision(proposal_id=proposal.id, action="reject", reason=reason),
        moved_to=moved,
    )


# ---------------- review loop ----------------


def _stdin_prompt(proposal: Proposal) -> ReviewDecision:
    """Default interactive prompt. Used by the CLI when no decisions list passed."""
    print(f"\n--- proposal {proposal.id} ---")
    print(f"type: {proposal.type}")
    print(f"target: {proposal.target_path}")
    print(f"confidence: {proposal.confidence}")
    print(f"rationale: {proposal.rationale}")
    print(f"evidence cycles: {proposal.evidence_cycles}")
    print(f"predicted regressions: {proposal.predicted_regressions}")
    print(f"requires shadow: {proposal.requires_shadow}")
    print("\n--- diff ---")
    print(proposal.proposed_diff)
    print("--- end diff ---")
    while True:
        try:
            ans = input("\n[a]ccept / [r]eject / [s]kip ? ").strip().lower()
        except EOFError:
            ans = "s"
        if ans in {"a", "accept"}:
            return ReviewDecision(proposal.id, "accept")
        if ans in {"r", "reject"}:
            reason = input("reason: ").strip() or "(no reason given)"
            return ReviewDecision(proposal.id, "reject", reason=reason)
        if ans in {"s", "skip", ""}:
            return ReviewDecision(proposal.id, "skip")


def review_pending(
    store: ProposalStore,
    *,
    repo_root: Path,
    decisions: list[ReviewDecision] | None = None,
    prompt_fn: Callable[[Proposal], ReviewDecision] | None = None,
    git_runner: GitRunner | None = None,
) -> ReviewSummary:
    """Iterate over pending proposals; apply decisions.

    Args:
        decisions: if provided, treated as authoritative — non-interactive.
            Must be one ReviewDecision per pending proposal id (any missing
            ids default to skip). Extra decisions for unknown ids are ignored.
        prompt_fn: optional — used when `decisions` is None. Defaults to
            stdin-based prompt.
        git_runner: injected for tests. Defaults to real `git`.

    Returns:
        ReviewSummary with one ReviewOutcome per processed proposal.
    """
    pending = store.list_pending()
    summary = ReviewSummary()

    if decisions is not None:
        decision_map = {d.proposal_id: d for d in decisions}
    else:
        decision_map = None

    runner = git_runner or _default_git_runner
    prompt = prompt_fn or _stdin_prompt

    for proposal in pending:
        if decision_map is not None:
            decision = decision_map.get(
                proposal.id,
                ReviewDecision(proposal.id, "skip", reason="not in decisions list"),
            )
        else:
            decision = prompt(proposal)

        if decision.action == "accept":
            outcome = accept_proposal(
                proposal,
                repo_root=repo_root,
                store=store,
                git_runner=runner,
            )
        elif decision.action == "reject":
            outcome = reject_proposal(proposal, store=store, reason=decision.reason)
        else:  # skip
            outcome = ReviewOutcome(proposal=proposal, decision=decision)

        summary.outcomes.append(outcome)

    return summary


# ---------------- list-only mode ----------------


def list_pending(store: ProposalStore) -> str:
    """Render pending proposals as a short human-readable list. No mutation."""
    pending = store.list_pending()
    if not pending:
        return "no pending proposals\n"
    lines = [f"{len(pending)} pending proposal(s):\n"]
    for i, p in enumerate(pending, 1):
        lines.append(
            f"  [{i}] {p.id}  type={p.type}  target={p.target_path}  "
            f"confidence={p.confidence}  shadow={p.requires_shadow}"
        )
        if p.rationale:
            lines.append(f"      rationale: {p.rationale[:100]}")
    return "\n".join(lines) + "\n"


__all__ = [
    "GitRunResult",
    "GitRunner",
    "ReviewDecision",
    "ReviewOutcome",
    "ReviewSummary",
    "accept_proposal",
    "list_pending",
    "reject_proposal",
    "review_pending",
]
