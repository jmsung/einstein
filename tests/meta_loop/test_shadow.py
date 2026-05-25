"""Tests for src/einstein/meta_loop/shadow.py — A/B harness."""

from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein.meta_loop import diagnose  # noqa: E402
from einstein.meta_loop.proposals import Proposal, ProposalType  # noqa: E402
from einstein.meta_loop.shadow import (  # noqa: E402
    ArmMetrics,
    RunResult,
    ShadowDelta,
    WorktreeSpec,
    apply_proposal_to_worktree,
    compute_arm_metrics,
    make_arms,
    run_shadow,
    setup_worktree,
)

UTC = dt.timezone.utc


def _now() -> dt.datetime:
    return dt.datetime(2026, 5, 25, 12, 0, 0, tzinfo=UTC)


def _proposal(pid: str = "test-shadow-001", ptype: str = ProposalType.RULE_EDIT.value) -> Proposal:
    if ptype == ProposalType.NEW_QUESTION.value:
        return Proposal(
            id=pid,
            type=ptype,
            target_path="docs/wiki/questions/2026-05-25-test.md",
            proposed_diff="---\nbody\n---\n",
            evidence_cycles=[10, 11, 12],
            predicted_regressions=["none"],
            confidence="low",
            requires_shadow=True,
            rationale="test",
            created_at=_now(),
        )
    return Proposal(
        id=pid,
        type=ptype,
        target_path=".claude/rules/agent-stance.md",
        proposed_diff="--- a/r\n+++ b/r\n@@ -1,1 +1,2 @@\n existing\n+new\n",
        evidence_cycles=[10, 11, 12],
        predicted_regressions=["maybe slower"],
        confidence="medium",
        requires_shadow=True,
        rationale="test",
        created_at=_now(),
    )


def _cycle_row(
    cid: int,
    *,
    problem: str = "P9",
    score_changed: bool = False,
    findings: int = 0,
    concepts: int = 0,
    outcome: str = "no-change",
) -> diagnose.CycleRow:
    return diagnose.CycleRow(
        cycle_id=cid,
        problem=problem,
        score_field="0.1 → 0.2" if score_changed else "0.1 (no Δ)",
        hours="0",
        compute="local",
        wiki_citations="0",
        findings_added=str(findings),
        concepts_added=str(concepts),
        author_mix="a:1",
        outcome=outcome,
        notes="",
    )


# ---------------- WorktreeSpec ----------------


def test_worktree_spec_rejects_bad_arm() -> None:
    with pytest.raises(ValueError):
        WorktreeSpec(arm="C", path=Path("/x"), branch="b")


def test_make_arms_naming(tmp_path: Path) -> None:
    p = _proposal(pid="prop-xyz")
    a, b = make_arms(p, worktree_parent=tmp_path)
    assert a.arm == "A"
    assert b.arm == "B"
    assert a.path.name == "cb-shadow-prop-xyz-A"
    assert b.path.name == "cb-shadow-prop-xyz-B"
    assert a.branch == "meta-shadow/prop-xyz/A"
    assert b.branch == "meta-shadow/prop-xyz/B"


# ---------------- setup_worktree ----------------


def test_setup_worktree_invokes_git_worktree_add(tmp_path: Path) -> None:
    spec = WorktreeSpec(arm="A", path=tmp_path / "cb-shadow-A", branch="meta/A")
    calls: list[tuple[list[str], Path | None, str | None]] = []

    def runner(args, cwd, stdin):
        calls.append((args, cwd, stdin))
        return RunResult(ok=True)

    setup_worktree(spec, repo_root=tmp_path, runner=runner)
    assert calls[0][0][:3] == ["git", "worktree", "add"]
    assert str(spec.path) in calls[0][0]
    assert spec.branch in calls[0][0]


# ---------------- apply_proposal_to_worktree ----------------


def test_apply_new_question_writes_file_to_arm(tmp_path: Path) -> None:
    p = _proposal(ptype=ProposalType.NEW_QUESTION.value)
    spec = WorktreeSpec(arm="A", path=tmp_path / "arm-a", branch="meta/A")
    spec.path.mkdir()
    calls: list[tuple[list[str], Path | None, str | None]] = []

    def runner(args, cwd, stdin):
        calls.append((args, cwd, stdin))
        return RunResult(ok=True)

    r = apply_proposal_to_worktree(p, spec, runner=runner)
    assert r.ok
    # The file was written
    assert (spec.path / p.target_path).is_file()
    # git add + commit were called
    assert ["git", "add", p.target_path] in [c[0] for c in calls]
    assert any(c[0][:2] == ["git", "commit"] for c in calls)


def test_apply_unified_diff_pipes_diff_to_git_apply(tmp_path: Path) -> None:
    p = _proposal(ptype=ProposalType.RULE_EDIT.value)
    spec = WorktreeSpec(arm="A", path=tmp_path / "arm-a", branch="meta/A")
    spec.path.mkdir()
    calls: list[tuple[list[str], Path | None, str | None]] = []

    def runner(args, cwd, stdin):
        calls.append((args, cwd, stdin))
        return RunResult(ok=True)

    apply_proposal_to_worktree(p, spec, runner=runner)
    apply_calls = [c for c in calls if c[0][:2] == ["git", "apply"]]
    assert len(apply_calls) == 1
    assert "+new" in apply_calls[0][2]


def test_apply_propagates_apply_failure(tmp_path: Path) -> None:
    p = _proposal(ptype=ProposalType.RULE_EDIT.value)
    spec = WorktreeSpec(arm="A", path=tmp_path / "arm-a", branch="meta/A")
    spec.path.mkdir()

    def runner(args, cwd, stdin):
        if args[:2] == ["git", "apply"]:
            return RunResult(ok=False, stderr="patch does not apply", returncode=1)
        return RunResult(ok=True)

    r = apply_proposal_to_worktree(p, spec, runner=runner)
    assert not r.ok
    assert "patch does not apply" in r.stderr


# ---------------- compute_arm_metrics ----------------


def test_compute_arm_metrics_aggregates() -> None:
    rows = [
        _cycle_row(1, score_changed=True, findings=1),
        _cycle_row(2, findings=2, concepts=1),
        _cycle_row(3, outcome="dead-end"),
        _cycle_row(4),
    ]
    m = compute_arm_metrics(rows)
    assert m.cycles == 4
    assert m.score_changed_cycles == 1
    assert m.findings_added == 3
    assert m.concepts_added == 1
    assert m.dead_ends_added == 1


def test_compute_arm_metrics_empty() -> None:
    m = compute_arm_metrics([])
    assert m.cycles == 0
    assert m.score_changed_cycles == 0


def test_per_cycle_zero_safe() -> None:
    m = ArmMetrics(0, 0, 0, 0, 0)
    assert m.per_cycle("findings_added") == 0.0


def test_safe_int_parses_findings_cell() -> None:
    """findings_added cell looks like '1 (`dead-end-foo.md`)' — parser pulls 1."""
    rows = [_cycle_row(1, findings=0)]
    rows[0] = diagnose.CycleRow(
        cycle_id=1,
        problem="P",
        score_field="0.1 (no Δ)",
        hours="0",
        compute="x",
        wiki_citations="0",
        findings_added="2 (`dead-end-foo.md`, `finding-x.md`)",
        concepts_added="0",
        author_mix="a:1",
        outcome="x",
        notes="",
    )
    m = compute_arm_metrics(rows)
    assert m.findings_added == 2


# ---------------- ShadowDelta.a_wins ----------------


def test_a_wins_when_a_has_more_findings_per_cycle() -> None:
    a = ArmMetrics(
        cycles=10, score_changed_cycles=1, findings_added=3, concepts_added=0, dead_ends_added=0
    )
    b = ArmMetrics(
        cycles=10, score_changed_cycles=1, findings_added=1, concepts_added=0, dead_ends_added=0
    )
    d = ShadowDelta(arm_a=a, arm_b=b)
    assert d.findings_delta == pytest.approx(0.2)
    assert d.a_wins()


def test_a_loses_when_a_has_fewer_findings() -> None:
    a = ArmMetrics(
        cycles=10, score_changed_cycles=1, findings_added=0, concepts_added=0, dead_ends_added=0
    )
    b = ArmMetrics(
        cycles=10, score_changed_cycles=1, findings_added=2, concepts_added=0, dead_ends_added=0
    )
    d = ShadowDelta(arm_a=a, arm_b=b)
    assert not d.a_wins()


def test_a_loses_when_dead_ends_regress() -> None:
    a = ArmMetrics(
        cycles=10, score_changed_cycles=1, findings_added=3, concepts_added=0, dead_ends_added=2
    )
    b = ArmMetrics(
        cycles=10, score_changed_cycles=1, findings_added=1, concepts_added=0, dead_ends_added=0
    )
    d = ShadowDelta(arm_a=a, arm_b=b)
    assert not d.a_wins()


# ---------------- run_shadow orchestration ----------------


def test_run_shadow_happy_path(tmp_path: Path) -> None:
    p = _proposal(ptype=ProposalType.NEW_QUESTION.value)
    log_path = tmp_path / "logs" / "meta-shadow-runs.md"

    git_calls: list[list[str]] = []

    def git(args, cwd, stdin):
        git_calls.append(args)
        # Mock worktree add by creating the dir
        if args[:3] == ["git", "worktree", "add"]:
            Path(args[3]).mkdir(parents=True, exist_ok=True)
        return RunResult(ok=True)

    def cycle_runner(arm_path: Path, n: int):
        # A arm gets more findings than B (so a_wins)
        is_a = "A" in arm_path.name
        if is_a:
            return [_cycle_row(i, findings=2) for i in range(n)]
        return [_cycle_row(i, findings=0) for i in range(n)]

    result = run_shadow(
        p,
        repo_root=tmp_path,
        n_cycles=5,
        worktree_parent=tmp_path,
        cycle_runner=cycle_runner,
        git_runner=git,
        shadow_log=log_path,
    )
    assert result.error is None
    assert result.delta is not None
    assert result.delta.findings_delta == pytest.approx(2.0)
    assert result.a_wins
    assert result.cleaned_up
    # Shadow log row appended
    assert log_path.is_file()
    text = log_path.read_text()
    assert p.id in text
    assert "yes" in text  # a_wins=yes


def test_run_shadow_setup_failure_returns_error(tmp_path: Path) -> None:
    p = _proposal()

    def git(args, cwd, stdin):
        if args[:3] == ["git", "worktree", "add"]:
            return RunResult(ok=False, stderr="branch exists", returncode=1)
        return RunResult(ok=True)

    def cycle_runner(arm_path: Path, n: int):
        return []

    result = run_shadow(
        p,
        repo_root=tmp_path,
        worktree_parent=tmp_path,
        n_cycles=3,
        cycle_runner=cycle_runner,
        git_runner=git,
    )
    assert result.error is not None
    assert "setup A failed" in result.error
    assert result.delta is None


def test_run_shadow_apply_failure_skips_cycles(tmp_path: Path) -> None:
    p = _proposal(ptype=ProposalType.RULE_EDIT.value)
    cycle_calls: list[Path] = []

    def git(args, cwd, stdin):
        if args[:3] == ["git", "worktree", "add"]:
            Path(args[3]).mkdir(parents=True, exist_ok=True)
            return RunResult(ok=True)
        if args[:2] == ["git", "apply"]:
            return RunResult(ok=False, stderr="bad diff", returncode=1)
        return RunResult(ok=True)

    def cycle_runner(arm_path: Path, n: int):
        cycle_calls.append(arm_path)
        return []

    result = run_shadow(
        p,
        repo_root=tmp_path,
        worktree_parent=tmp_path,
        n_cycles=3,
        cycle_runner=cycle_runner,
        git_runner=git,
    )
    assert result.error is not None
    assert "apply to A failed" in result.error
    # Cycle runner was NOT invoked since apply failed
    assert cycle_calls == []


def test_run_shadow_cleanup_can_be_disabled(tmp_path: Path) -> None:
    p = _proposal(ptype=ProposalType.NEW_QUESTION.value)

    def git(args, cwd, stdin):
        if args[:3] == ["git", "worktree", "add"]:
            Path(args[3]).mkdir(parents=True, exist_ok=True)
        return RunResult(ok=True)

    def cycle_runner(arm_path: Path, n: int):
        return [_cycle_row(i) for i in range(n)]

    result = run_shadow(
        p,
        repo_root=tmp_path,
        worktree_parent=tmp_path,
        n_cycles=2,
        cycle_runner=cycle_runner,
        git_runner=git,
        cleanup=False,
    )
    assert result.cleaned_up is False


def test_default_cycle_runner_returns_partial_rows_on_timeout(tmp_path: Path, monkeypatch) -> None:
    """Regression: if autonomous_loop subprocess hits the timeout, the runner
    must still return whatever cycle-log rows were appended before the kill.

    Without this fix, a single slow arm crashes the whole shadow run via
    uncaught TimeoutExpired, and the cleanup=True finally-block deletes all
    in-flight cycle-log work.
    """
    import subprocess as _sp

    from einstein.meta_loop.shadow import default_cycle_runner

    # Arm worktree with a pre-existing cycle-log having one row + one row
    # written "during" the (fake) run we'll then have time out.
    cycle_log = tmp_path / "docs" / "agent" / "cycle-log.md"
    cycle_log.parent.mkdir(parents=True)
    cycle_log.write_text(
        "# Cycle log\n\n## Cycles\n\n"
        "| # | problem | start → end | hours | compute | wiki cites | findings+ | "
        "concepts+ | mix | outcome | notes | cites_src |\n"
        "|---|---|---|---|---|---|---|---|---|---|---|---|\n"
        "| 100 | P-old | 1 → 1 | 0.1 | local-cpu | 0 | 0 | 0 | a:1/h:0/hyb:0 | no-change | smoke | 0 |\n"
    )

    def fake_run(*args, **kwargs):
        # Simulate: subprocess wrote one new row to the cycle-log before
        # being killed by timeout.
        with cycle_log.open("a") as f:
            f.write(
                "| 101 | P-new | 1 → 1 | 0.1 | local-cpu | 0 | 0 | 0 | "
                "a:1/h:0/hyb:0 | no-change | partial | 2 |\n"
            )
        raise _sp.TimeoutExpired(cmd=args[0], timeout=kwargs.get("timeout", 0))

    monkeypatch.setattr(_sp, "run", fake_run)

    rows = default_cycle_runner(tmp_path, 10, timeout_seconds=5)

    # The pre-existing row (#100) must be filtered out; only the new row (#101) returned.
    assert len(rows) == 1
    assert rows[0].cycle_id == 101


def test_shadow_log_row_format(tmp_path: Path) -> None:
    """Verify the appended row matches the documented schema."""
    p = _proposal(ptype=ProposalType.NEW_QUESTION.value)
    log_path = tmp_path / "shadow-log.md"

    def git(args, cwd, stdin):
        if args[:3] == ["git", "worktree", "add"]:
            Path(args[3]).mkdir(parents=True, exist_ok=True)
        return RunResult(ok=True)

    def cycle_runner(arm_path: Path, n: int):
        # Use exact arm-based counts
        is_a = "A" in arm_path.name
        return [_cycle_row(i, findings=3 if is_a else 1) for i in range(n)]

    run_shadow(
        p,
        repo_root=tmp_path,
        worktree_parent=tmp_path,
        n_cycles=4,
        cycle_runner=cycle_runner,
        git_runner=git,
        shadow_log=log_path,
    )
    lines = log_path.read_text().splitlines()
    data_rows = [ln for ln in lines if ln.startswith("| 20")]
    assert len(data_rows) == 1
    row = data_rows[0]
    # Schema fields present
    assert p.id in row
    assert "| 4 |" in row  # n_cycles
    assert "yes" in row  # a_wins
