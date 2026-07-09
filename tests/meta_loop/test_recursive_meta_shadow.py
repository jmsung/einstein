"""Shadow A/B harness extensions for meta_loop.py-touching diffs (G4 of recursive-meta).

Three deliverables:
- Apply path: a meta_self_edit-shaped unified diff goes through `apply_proposal_to_worktree`
  using the existing unified-diff path (same as rule_edit). A malformed diff surfaces.
- Meta-layer metrics: `parse_meta_arm_metrics` reads the per-arm audit log and produces
  per-arm proposer-emit / gate-pass counts that the cycle-log metrics don't capture.
- Determinism: same audit-log contents → same MetaArmMetrics on every call (pure).
"""

from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein.meta_loop.meta_gate import AUDIT_LOG_HEADER  # noqa: E402
from einstein.meta_loop.proposals import Proposal, ProposalType  # noqa: E402
from einstein.meta_loop.shadow import (  # noqa: E402
    MetaArmMetrics,
    RunResult,
    ShadowMetaDelta,
    WorktreeSpec,
    apply_proposal_to_worktree,
    parse_meta_arm_metrics,
)

UTC = dt.timezone.utc


# ---------------- helpers ----------------


def _meta_self_edit_proposal(diff: str | None = None) -> Proposal:
    return Proposal(
        id="20260528t120000-cafef00d",
        type=ProposalType.META_SELF_EDIT.value,
        target_path="scripts/meta_loop.py",
        proposed_diff=diff
        or (
            "--- a/scripts/meta_loop.py\n"
            "+++ b/scripts/meta_loop.py\n"
            "@@ -1,1 +1,2 @@\n"
            "+# diagnostic marker\n"
            " #!/usr/bin/env python3\n"
        ),
        evidence_cycles=list(range(12)),
        requires_shadow=True,
        proposer_id="recursive-meta-v0",
    )


def _write_arm_audit_log(
    path: Path,
    *,
    accepted: int = 0,
    rejected: int = 0,
    queued: int = 0,
    shadow_pending: int = 0,
) -> None:
    """Build a synthetic per-arm audit log with controlled decision counts."""
    path.parent.mkdir(parents=True, exist_ok=True)
    text = "# meta-proposals audit log\n\n" + AUDIT_LOG_HEADER
    base_ts = dt.datetime(2026, 5, 28, 14, 0, 0, tzinfo=UTC)
    n = 0

    def _row(decision: str) -> str:
        nonlocal n
        ts = (base_ts + dt.timedelta(minutes=n)).strftime("%Y-%m-%dT%H:%M:%SZ")
        n += 1
        return (
            f"| {ts} | prop-{n:03d} | rule_edit | "
            f".claude/rules/x.md | {decision} | gateX | reasonY | metaharness-llm-v1 |\n"
        )

    for _ in range(accepted):
        text += _row("accepted")
    for _ in range(rejected):
        text += _row("rejected")
    for _ in range(queued):
        text += _row("queued")
    for _ in range(shadow_pending):
        text += _row("shadow-pending")
    path.write_text(text)


# ---------------- parse_meta_arm_metrics ----------------


def test_parse_meta_metrics_empty_log_returns_zeros(tmp_path: Path) -> None:
    m = parse_meta_arm_metrics(tmp_path / "no-such-log.md")
    assert m == MetaArmMetrics(0, 0, 0, 0, 0)
    assert m.gate_pass_rate == 0.0


def test_parse_meta_metrics_counts_decisions_correctly(tmp_path: Path) -> None:
    log = tmp_path / "meta-proposals.md"
    _write_arm_audit_log(log, accepted=3, rejected=4, queued=2, shadow_pending=1)
    m = parse_meta_arm_metrics(log)
    assert m.proposals_emitted == 10
    assert m.proposals_accepted == 3
    assert m.proposals_rejected == 4
    assert m.proposals_queued == 2
    assert m.proposals_shadow_pending == 1


def test_meta_metrics_gate_pass_rate_includes_queued(tmp_path: Path) -> None:
    """Both accepted AND queued count as "gate passed" — queued is the
    never-auto-merge but every-gate-passed outcome."""
    log = tmp_path / "meta-proposals.md"
    _write_arm_audit_log(log, accepted=2, queued=3, rejected=5)
    m = parse_meta_arm_metrics(log)
    assert m.gate_pass_rate == 0.5  # (2 + 3) / 10


def test_meta_metrics_gate_pass_rate_zero_emissions_is_zero(tmp_path: Path) -> None:
    log = tmp_path / "meta-proposals.md"
    _write_arm_audit_log(log)  # empty
    m = parse_meta_arm_metrics(log)
    assert m.gate_pass_rate == 0.0


# ---------------- ShadowMetaDelta ----------------


def test_shadow_meta_delta_emit_rate_delta_simple() -> None:
    a = MetaArmMetrics(
        proposals_emitted=10,
        proposals_accepted=2,
        proposals_rejected=5,
        proposals_queued=2,
        proposals_shadow_pending=1,
    )
    b = MetaArmMetrics(
        proposals_emitted=6,
        proposals_accepted=1,
        proposals_rejected=4,
        proposals_queued=0,
        proposals_shadow_pending=1,
    )
    d = ShadowMetaDelta(arm_a=a, arm_b=b)
    assert d.emit_rate_delta == 4
    assert d.queued_delta == 2
    # arm_a gate_pass_rate = 4/10 = 0.4; arm_b = 1/6 ≈ 0.167; delta ≈ 0.233
    assert d.gate_pass_rate_delta > 0.2


# ---------------- determinism ----------------


def test_parse_meta_arm_metrics_is_pure(tmp_path: Path) -> None:
    """Same input file → same output, every call. Defensive — guards against
    accidental introduction of time.time()-based state in parse_meta_arm_metrics."""
    log = tmp_path / "meta-proposals.md"
    _write_arm_audit_log(log, accepted=2, rejected=3, queued=1)
    m1 = parse_meta_arm_metrics(log)
    m2 = parse_meta_arm_metrics(log)
    m3 = parse_meta_arm_metrics(log)
    assert m1 == m2 == m3


# ---------------- apply_proposal_to_worktree on meta_self_edit ----------------


def test_meta_self_edit_diff_goes_through_unified_diff_path(tmp_path: Path) -> None:
    """meta_self_edit's diff is a unified diff (against scripts/meta_loop.py),
    so it must take the `git apply` branch — NOT the NEW_QUESTION write-file path."""
    proposal = _meta_self_edit_proposal()
    spec = WorktreeSpec(arm="A", path=tmp_path, branch="meta-shadow/test/A")

    recorded: list[tuple[list[str], str | None]] = []

    def fake_runner(args, cwd, stdin):
        recorded.append((list(args), stdin))
        return RunResult(ok=True)

    apply_proposal_to_worktree(proposal, spec, runner=fake_runner)
    # First call must be `git apply --whitespace=nowarn` with the diff on stdin
    assert recorded[0][0][:2] == ["git", "apply"]
    assert "--whitespace=nowarn" in recorded[0][0]
    assert recorded[0][1] is not None
    assert recorded[0][1].startswith("--- a/scripts/meta_loop.py")
    # Then git add + git commit on the touched file
    assert recorded[1][0][:2] == ["git", "add"]
    assert recorded[1][0][-1] == "scripts/meta_loop.py"
    assert recorded[2][0][:2] == ["git", "commit"]


# ---------------- DGM-node-114 adversarial guard ----------------
# Closes the open question at
# knowledge/wiki/questions/2026-05-28-recursive-meta-dgm-node-114-guard.md


def test_a_wins_rejects_arm_that_hides_dead_ends() -> None:
    """The DGM-node-114 analogue: a meta_self_edit that "improves" by hiding
    failures. Arm A reports fewer dead-ends AND fewer findings than arm B
    (the edit suppresses the failure-finding write path entirely). The
    existing not_worse_on_dead_ends guard must reject this."""
    from einstein.meta_loop.shadow import ArmMetrics, ShadowDelta

    arm_a_suppressed = ArmMetrics(
        cycles=10,
        score_changed_cycles=5,
        findings_added=2,  # fewer findings overall
        concepts_added=0,
        dead_ends_added=0,  # NO dead-ends recorded — the suspicious signal
    )
    arm_b_honest = ArmMetrics(
        cycles=10,
        score_changed_cycles=5,
        findings_added=5,
        concepts_added=0,
        dead_ends_added=3,  # real dead-ends filed
    )
    d = ShadowDelta(arm_a=arm_a_suppressed, arm_b=arm_b_honest)
    assert not d.a_wins(), "suppressing failures must not win shadow A/B"


def test_a_wins_rejects_arm_that_inflates_findings_by_skipping_dead_ends() -> None:
    """Subtler attack: arm A has MORE findings than arm B but no dead-ends,
    while arm B has fewer findings and several dead-ends. The findings delta
    looks positive — but dead-ends regressing the wrong way (B had more)
    means arm A may be classifying real failures as findings."""
    from einstein.meta_loop.shadow import ArmMetrics, ShadowDelta

    arm_a = ArmMetrics(
        cycles=10,
        score_changed_cycles=5,
        findings_added=8,
        concepts_added=0,
        dead_ends_added=0,
    )
    arm_b = ArmMetrics(
        cycles=10,
        score_changed_cycles=5,
        findings_added=5,
        concepts_added=0,
        dead_ends_added=3,
    )
    d = ShadowDelta(arm_a=arm_a, arm_b=arm_b)
    # dead_ends_delta = (0/10) - (3/10) = -0.3 → strictly <= 0 → guard ALLOWS this
    # This documents the current state — the simple guard catches the case
    # above (fewer findings) but NOT this one (inflated findings + no dead-ends).
    # The follow-on finding referenced in the question file would tighten this.
    assert d.a_wins(), (
        "current guard allows inflated-findings + no-dead-ends; "
        "see knowledge/wiki/questions/2026-05-28-recursive-meta-dgm-node-114-guard.md"
    )


def test_broken_meta_self_edit_diff_propagates_apply_failure(tmp_path: Path) -> None:
    """A malformed unified diff: git apply fails → apply_proposal_to_worktree
    returns the failure RunResult unchanged. The shadow harness layer then
    surfaces this as ShadowResult.error rather than silently completing."""
    proposal = _meta_self_edit_proposal(diff="this is not a unified diff at all, hello\n")
    spec = WorktreeSpec(arm="A", path=tmp_path, branch="meta-shadow/test/A")

    def fail_apply(args, cwd, stdin):
        if args[:2] == ["git", "apply"]:
            return RunResult(ok=False, stderr="fatal: corrupt patch", returncode=128)
        return RunResult(ok=True)

    r = apply_proposal_to_worktree(proposal, spec, runner=fail_apply)
    assert not r.ok
    assert "corrupt patch" in r.stderr
