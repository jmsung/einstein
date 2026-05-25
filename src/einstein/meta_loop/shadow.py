"""meta_loop.shadow — A/B harness for proposals (Goal 5).

Per `docs/wiki/findings/meta-loop-design-from-literature.md` § evaluation:

  Self-attribution is asymmetric (AHE result, 89% of regressions unforeseen).
  Shadow A/B is the regression-foresight gap-filler — fork two worktrees,
  apply the proposal to arm A, run N inner cycles in each arm, compare
  outcome deltas. Promotion requires A wins by a threshold + human sign-off.

Pipeline per proposal (when `requires_shadow=True`):

  1. Create two worktrees:
       cb-shadow-<id>-A on a branch derived from the proposal's diff
       cb-shadow-<id>-B on the current commit (control)
  2. In each arm, run N inner cycles via `cycle_runner(arm_path)`.
  3. Parse each arm's resulting cycle-log; compute per-arm metric tuples.
  4. Compute Δ = A - B on each metric.
  5. Append a row to `mb/logs/meta-shadow-runs.md`.
  6. Cleanup: `git worktree remove` both arms.
  7. Return ShadowResult — Δ + promotion recommendation (still human-gated).

This module exposes pure helpers that are unit-testable (delta computation,
worktree spec construction, the orchestration with an injected cycle_runner).
Actual N-cycle execution is expensive; the harness here is *the contract* —
firing it on a real run is operator-initiated, not in unit tests.
"""

from __future__ import annotations

import datetime as dt
import logging
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from . import diagnose
from .proposals import Proposal, ProposalType

log = logging.getLogger("meta_loop.shadow")


# ---------------- specs ----------------


@dataclass(frozen=True)
class WorktreeSpec:
    """One arm of a shadow A/B run."""

    arm: str  # "A" | "B"
    path: Path
    branch: str

    def __post_init__(self) -> None:
        if self.arm not in ("A", "B"):
            raise ValueError(f"arm must be 'A' or 'B', got {self.arm!r}")


def make_arms(proposal: Proposal, *, worktree_parent: Path) -> tuple[WorktreeSpec, WorktreeSpec]:
    """Build the two arm specs. Branch names embed the proposal id."""
    a = WorktreeSpec(
        arm="A",
        path=worktree_parent / f"cb-shadow-{proposal.id}-A",
        branch=f"meta-shadow/{proposal.id}/A",
    )
    b = WorktreeSpec(
        arm="B",
        path=worktree_parent / f"cb-shadow-{proposal.id}-B",
        branch=f"meta-shadow/{proposal.id}/B",
    )
    return a, b


# ---------------- runner contract ----------------


@dataclass
class RunResult:
    ok: bool
    stdout: str = ""
    stderr: str = ""
    returncode: int = 0


Runner = Callable[[list[str], Path | None, str | None], RunResult]
"""Signature: runner(args, cwd, stdin) -> RunResult."""


def _default_runner(args: list[str], cwd: Path | None, stdin: str | None) -> RunResult:
    try:
        proc = subprocess.run(
            args,
            cwd=cwd,
            input=stdin,
            capture_output=True,
            text=True,
            timeout=900,
        )
    except (subprocess.TimeoutExpired, FileNotFoundError) as e:
        return RunResult(ok=False, stderr=str(e), returncode=-1)
    return RunResult(
        ok=proc.returncode == 0,
        stdout=proc.stdout,
        stderr=proc.stderr,
        returncode=proc.returncode,
    )


# ---------------- worktree setup + apply + cleanup ----------------


def setup_worktree(
    spec: WorktreeSpec,
    *,
    repo_root: Path,
    base_branch: str = "HEAD",
    runner: Runner | None = None,
) -> RunResult:
    """`git worktree add <path> -b <branch> <base>`."""
    r = runner or _default_runner
    return r(
        ["git", "worktree", "add", str(spec.path), "-b", spec.branch, base_branch],
        repo_root,
        None,
    )


def apply_proposal_to_worktree(
    proposal: Proposal,
    spec: WorktreeSpec,
    *,
    runner: Runner | None = None,
) -> RunResult:
    """Apply the proposal's diff/body to the arm's worktree."""
    r = runner or _default_runner
    if proposal.type == ProposalType.NEW_QUESTION.value:
        target = spec.path / proposal.target_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(proposal.proposed_diff)
        add = r(["git", "add", proposal.target_path], spec.path, None)
        if not add.ok:
            return add
        return r(
            ["git", "commit", "-m", f"shadow({spec.arm}): apply {proposal.id}"],
            spec.path,
            None,
        )
    apply_r = r(
        ["git", "apply", "--whitespace=nowarn"],
        spec.path,
        proposal.proposed_diff,
    )
    if not apply_r.ok:
        return apply_r
    add = r(["git", "add", proposal.target_path], spec.path, None)
    if not add.ok:
        return add
    return r(
        ["git", "commit", "-m", f"shadow({spec.arm}): apply {proposal.id}"],
        spec.path,
        None,
    )


def remove_worktree(
    spec: WorktreeSpec,
    *,
    repo_root: Path,
    runner: Runner | None = None,
) -> RunResult:
    """`git worktree remove --force <path>`."""
    r = runner or _default_runner
    res = r(
        ["git", "worktree", "remove", "--force", str(spec.path)],
        repo_root,
        None,
    )
    # On a stale worktree where git lost track, fall back to rm -rf
    if not res.ok and spec.path.exists():
        try:
            shutil.rmtree(spec.path)
            res = RunResult(ok=True, stdout=f"fallback rm -rf {spec.path}")
        except OSError as e:
            res = RunResult(ok=False, stderr=str(e), returncode=-1)
    return res


# ---------------- delta computation ----------------


@dataclass(frozen=True)
class ArmMetrics:
    """Per-arm metric tuple computed from that arm's cycle-log rows."""

    cycles: int
    score_changed_cycles: int
    findings_added: int
    concepts_added: int
    dead_ends_added: int
    tokens_in: int = 0  # placeholder — not parsed yet
    tokens_out: int = 0

    def per_cycle(self, attr: str) -> float:
        if self.cycles == 0:
            return 0.0
        return getattr(self, attr) / self.cycles


def _safe_int(s: str) -> int:
    """Pull the leading integer out of a cell like '1 (`dead-end-foo.md`)'."""
    if not s:
        return 0
    s = s.strip()
    digits = []
    for ch in s:
        if ch.isdigit():
            digits.append(ch)
        elif digits:
            break
    return int("".join(digits)) if digits else 0


def compute_arm_metrics(rows: list[diagnose.CycleRow]) -> ArmMetrics:
    """Aggregate per-arm metrics from parsed cycle-log rows."""
    if not rows:
        return ArmMetrics(0, 0, 0, 0, 0)
    findings = sum(_safe_int(r.findings_added) for r in rows)
    concepts = sum(_safe_int(r.concepts_added) for r in rows)
    # Dead-ends approximated by the count of "dead-end" outcomes
    dead_ends = sum(1 for r in rows if "dead-end" in r.outcome.lower())
    return ArmMetrics(
        cycles=len(rows),
        score_changed_cycles=sum(1 for r in rows if r.score_changed),
        findings_added=findings,
        concepts_added=concepts,
        dead_ends_added=dead_ends,
    )


@dataclass(frozen=True)
class ShadowDelta:
    """Result of one A/B comparison."""

    arm_a: ArmMetrics
    arm_b: ArmMetrics

    # Per-cycle deltas (A - B) on each metric
    @property
    def score_changed_delta(self) -> float:
        return self.arm_a.per_cycle("score_changed_cycles") - self.arm_b.per_cycle(
            "score_changed_cycles"
        )

    @property
    def findings_delta(self) -> float:
        return self.arm_a.per_cycle("findings_added") - self.arm_b.per_cycle("findings_added")

    @property
    def concepts_delta(self) -> float:
        return self.arm_a.per_cycle("concepts_added") - self.arm_b.per_cycle("concepts_added")

    @property
    def dead_ends_delta(self) -> float:
        return self.arm_a.per_cycle("dead_ends_added") - self.arm_b.per_cycle("dead_ends_added")

    def a_wins(
        self, *, min_findings_delta: float = 0.0, min_score_changed_delta: float = 0.0
    ) -> bool:
        """A wins iff A is non-worse on score-change and strictly better on
        any of findings/concepts, with neither regression of either dead-ends
        relative to B.

        Trivial default thresholds — caller can tighten.
        """
        if self.score_changed_delta < min_score_changed_delta:
            return False
        # Strict improvement on findings or concepts (any positive Δ)
        positive_signal = self.findings_delta > min_findings_delta or self.concepts_delta > 0
        # Avoid regressing on dead-ends (more dead-ends = more failed attempts,
        # but it's neutral if score also moved — only flag when score didn't move)
        not_worse_on_dead_ends = self.dead_ends_delta <= 0
        return positive_signal and not_worse_on_dead_ends


# ---------------- shadow log ----------------


SHADOW_LOG_HEADER = (
    "| timestamp_utc | proposal_id | n_cycles | A_score_chg | A_findings "
    "| A_concepts | B_score_chg | B_findings | B_concepts | "
    "Δ_findings_per_cycle | a_wins | reason |\n"
    "|---|---|---|---|---|---|---|---|---|---|---|---|\n"
)


def _ensure_shadow_log_header(path: Path) -> None:
    if path.is_file():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("# meta-shadow runs\n\n" + SHADOW_LOG_HEADER)


def append_shadow_log(
    path: Path,
    *,
    timestamp: dt.datetime,
    proposal: Proposal,
    n_cycles: int,
    delta: ShadowDelta,
    a_wins: bool,
    reason: str,
) -> None:
    _ensure_shadow_log_header(path)
    row = (
        f"| {timestamp.strftime('%Y-%m-%dT%H:%M:%SZ')} "
        f"| {proposal.id} | {n_cycles} "
        f"| {delta.arm_a.score_changed_cycles} | {delta.arm_a.findings_added} "
        f"| {delta.arm_a.concepts_added} "
        f"| {delta.arm_b.score_changed_cycles} | {delta.arm_b.findings_added} "
        f"| {delta.arm_b.concepts_added} "
        f"| {delta.findings_delta:.3f} "
        f"| {'yes' if a_wins else 'no'} "
        f"| {reason} |\n"
    )
    with path.open("a") as fh:
        fh.write(row)


# ---------------- orchestration ----------------


@dataclass
class ShadowResult:
    proposal_id: str
    n_cycles: int
    delta: ShadowDelta | None = None
    a_wins: bool = False
    reason: str = ""
    error: str | None = None
    cleaned_up: bool = False


CycleRunner = Callable[[Path, int], list[diagnose.CycleRow]]
"""run_n_cycles(arm_path, n) -> list of CycleRow rows produced."""


DEFAULT_CYCLE_RUNNER_TIMEOUT_SECONDS = 14400  # 4h — fits N=10 at observed ~12 min/cycle


def default_cycle_runner(
    arm_path: Path,
    n: int,
    *,
    timeout_seconds: int = DEFAULT_CYCLE_RUNNER_TIMEOUT_SECONDS,
) -> list[diagnose.CycleRow]:
    """Shell out to scripts/autonomous_loop.py inside the arm worktree.

    Captures the cycle-log rows that get APPENDED during this run by
    snapshotting the cycle-log size before/after and parsing the delta.

    Heavy: each cycle is an LLM call. Real use is operator-initiated;
    unit tests stub this.

    On `subprocess.TimeoutExpired`: subprocess is killed, but we still parse
    whatever rows the autonomous_loop appended before being killed and return
    them. Without this, a single slow arm crashes the whole shadow run + we
    lose all in-flight work to the `cleanup=True` finally-block.
    """
    cycle_log = arm_path / "docs" / "agent" / "cycle-log.md"
    rows_before = diagnose.parse_cycle_log(cycle_log)
    before_ids = {r.cycle_id for r in rows_before}

    try:
        proc = subprocess.run(
            [
                "uv",
                "run",
                "python",
                "scripts/autonomous_loop.py",
                "--max-problems",
                str(n),
            ],
            cwd=arm_path,
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
            check=False,
        )
        if proc.returncode != 0:
            log.warning(
                "autonomous_loop in %s exited %d; stderr: %s",
                arm_path,
                proc.returncode,
                proc.stderr[-500:],
            )
    except subprocess.TimeoutExpired:
        log.warning(
            "autonomous_loop in %s timed out after %ds; returning partial rows",
            arm_path,
            timeout_seconds,
        )

    rows_after = diagnose.parse_cycle_log(cycle_log)
    return [r for r in rows_after if r.cycle_id not in before_ids]


def run_shadow(
    proposal: Proposal,
    *,
    repo_root: Path,
    n_cycles: int = 10,
    worktree_parent: Path | None = None,
    cycle_runner: CycleRunner,
    git_runner: Runner | None = None,
    shadow_log: Path | None = None,
    cleanup: bool = True,
    clock: Callable[[], dt.datetime] | None = None,
) -> ShadowResult:
    """Run a full shadow A/B comparison. Returns ShadowResult.

    Args:
        proposal: must have requires_shadow=True; this isn't enforced here
            (the gate chain handles routing) but logged.
        cycle_runner: REQUIRED — runs N cycles in one arm and returns the
            parsed cycle-log rows that arm produced. The real implementation
            shells out to scripts/autonomous_loop.py; tests inject a stub.
        cleanup: when True, `git worktree remove` both arms after the run.
            Set False to keep the worktrees for human inspection.
    """
    now = (clock or (lambda: dt.datetime.now(dt.timezone.utc)))()
    parent = worktree_parent or repo_root.parent

    arm_a, arm_b = make_arms(proposal, worktree_parent=parent)
    result = ShadowResult(proposal_id=proposal.id, n_cycles=n_cycles)

    runner = git_runner or _default_runner
    try:
        # Setup both arms from current HEAD
        s = setup_worktree(arm_a, repo_root=repo_root, runner=runner)
        if not s.ok:
            result.error = f"setup A failed: {s.stderr.strip()}"
            return result
        s = setup_worktree(arm_b, repo_root=repo_root, runner=runner)
        if not s.ok:
            result.error = f"setup B failed: {s.stderr.strip()}"
            return result
        # Apply proposal to A only
        a = apply_proposal_to_worktree(proposal, arm_a, runner=runner)
        if not a.ok:
            result.error = f"apply to A failed: {a.stderr.strip()}"
            return result
        # Run N cycles in each arm
        rows_a = cycle_runner(arm_a.path, n_cycles)
        rows_b = cycle_runner(arm_b.path, n_cycles)
        delta = ShadowDelta(
            arm_a=compute_arm_metrics(rows_a),
            arm_b=compute_arm_metrics(rows_b),
        )
        result.delta = delta
        result.a_wins = delta.a_wins()
        result.reason = (
            f"Δfindings/cycle={delta.findings_delta:.3f}, "
            f"Δscore_changed/cycle={delta.score_changed_delta:.3f}"
        )
        if shadow_log is not None:
            append_shadow_log(
                shadow_log,
                timestamp=now,
                proposal=proposal,
                n_cycles=n_cycles,
                delta=delta,
                a_wins=result.a_wins,
                reason=result.reason,
            )
    finally:
        if cleanup:
            for arm in (arm_a, arm_b):
                rm = remove_worktree(arm, repo_root=repo_root, runner=runner)
                if not rm.ok:
                    log.warning("cleanup %s failed: %s", arm.path, rm.stderr)
            result.cleaned_up = True
    return result


__all__ = [
    "ArmMetrics",
    "CycleRunner",
    "RunResult",
    "Runner",
    "ShadowDelta",
    "ShadowResult",
    "WorktreeSpec",
    "append_shadow_log",
    "apply_proposal_to_worktree",
    "compute_arm_metrics",
    "default_cycle_runner",
    "make_arms",
    "remove_worktree",
    "run_shadow",
    "setup_worktree",
]
