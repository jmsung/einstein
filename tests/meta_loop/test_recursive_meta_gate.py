"""Tests for the meta_self_edit post-shadow gate chain (G3 of recursive-meta).

Covers Gates A (cycles floor), B (shadow statistical), C (never auto-merge —
queue not apply), D (snapshot before queue).
"""

from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein.meta_loop.meta_gate import (  # noqa: E402
    META_SELF_EDIT_FINDINGS_DELTA_MIN,
    GateDecision,
    _binomial_one_sided_p,
    evaluate_meta_self_edit_post_shadow,
)
from einstein.meta_loop.proposals import Proposal, ProposalType  # noqa: E402
from einstein.meta_loop.shadow import ArmMetrics, ShadowDelta, ShadowResult  # noqa: E402

UTC = dt.timezone.utc


# ---------------- fixtures ----------------


def _meta_self_edit_proposal(*, evidence_cycles_count: int = 12) -> Proposal:
    return Proposal(
        id="20260528t120000-abcdef01",
        type=ProposalType.META_SELF_EDIT.value,
        target_path="scripts/meta_loop.py",
        proposed_diff=(
            "--- a/scripts/meta_loop.py\n"
            "+++ b/scripts/meta_loop.py\n"
            "@@ -1,1 +1,2 @@\n"
            "+# diagnostic marker\n"
            " #!/usr/bin/env python3\n"
        ),
        evidence_cycles=list(range(evidence_cycles_count)),
        expected_metric_delta={"meta_proposals_rejected_per_cycle": -0.1},
        predicted_regressions=["may bias future proposals"],
        confidence="low",
        requires_shadow=True,
        rationale="test candidate",
        proposer_id="recursive-meta-v0",
    )


def _shadow_result(
    *,
    findings_a: int,
    findings_b: int,
    score_changed_a: int = 5,
    score_changed_b: int = 5,
    dead_ends_a: int = 1,
    dead_ends_b: int = 1,
    error: str | None = None,
    n_cycles: int = 10,
) -> ShadowResult:
    if error:
        return ShadowResult(proposal_id="20260528t120000-abcdef01", n_cycles=n_cycles, error=error)
    delta = ShadowDelta(
        arm_a=ArmMetrics(
            cycles=n_cycles,
            score_changed_cycles=score_changed_a,
            findings_added=findings_a,
            concepts_added=0,
            dead_ends_added=dead_ends_a,
        ),
        arm_b=ArmMetrics(
            cycles=n_cycles,
            score_changed_cycles=score_changed_b,
            findings_added=findings_b,
            concepts_added=0,
            dead_ends_added=dead_ends_b,
        ),
    )
    return ShadowResult(
        proposal_id="20260528t120000-abcdef01",
        n_cycles=n_cycles,
        delta=delta,
        a_wins=delta.a_wins(),
        reason="(test fixture)",
    )


def _setup_dirs(tmp_path: Path) -> dict[str, Path]:
    queue_dir = tmp_path / "meta-self-edit-queue"
    snapshot_dir = tmp_path / "meta-loop-snapshots"
    audit_log = tmp_path / "meta-proposals.md"
    source = tmp_path / "scripts" / "meta_loop.py"
    source.parent.mkdir(parents=True, exist_ok=True)
    source.write_text("#!/usr/bin/env python3\n# original\n")
    return dict(
        queue_dir=queue_dir,
        snapshot_dir=snapshot_dir,
        audit_log=audit_log,
        source=source,
    )


def _now() -> dt.datetime:
    return dt.datetime(2026, 5, 28, 12, 30, 0, tzinfo=UTC)


# ---------------- _binomial_one_sided_p ----------------


def test_binomial_p_zero_data_returns_one() -> None:
    assert _binomial_one_sided_p(0, 0) == 1.0


def test_binomial_p_symmetric_50_50() -> None:
    # 5 vs 5 → P(X >= 5 | N=10) = 0.6230 (close to coin-flip)
    p = _binomial_one_sided_p(5, 5)
    assert 0.5 < p < 0.7


def test_binomial_p_strong_a_advantage() -> None:
    # 9 vs 1 → P(X >= 9 | N=10) = 11/1024 ≈ 0.0107
    p = _binomial_one_sided_p(9, 1)
    assert p < 0.02


def test_binomial_p_b_advantage_gives_high_p() -> None:
    # 1 vs 9 → P(X >= 1 | N=10) = 1023/1024 ≈ 0.999
    p = _binomial_one_sided_p(1, 9)
    assert p > 0.99


# ---------------- Gate A: cycles floor ----------------


def test_gate_a_rejects_below_cycles_floor(tmp_path: Path) -> None:
    proposal = _meta_self_edit_proposal(evidence_cycles_count=9)
    shadow = _shadow_result(findings_a=10, findings_b=1)
    dirs = _setup_dirs(tmp_path)
    result = evaluate_meta_self_edit_post_shadow(
        proposal,
        shadow,
        snapshot_source=dirs["source"],
        queue_dir=dirs["queue_dir"],
        snapshot_dir=dirs["snapshot_dir"],
        audit_log=dirs["audit_log"],
        clock=_now,
    )
    assert result.decision == GateDecision.REJECTED
    assert result.rejected_at_gate == "meta-cycles-floor"
    assert not dirs["queue_dir"].exists() or not any(dirs["queue_dir"].iterdir())


# ---------------- Gate B: shadow statistical ----------------


def test_gate_b_rejects_a_wins_false(tmp_path: Path) -> None:
    # findings_a < findings_b → a_wins=False
    proposal = _meta_self_edit_proposal()
    shadow = _shadow_result(findings_a=1, findings_b=10)
    dirs = _setup_dirs(tmp_path)
    result = evaluate_meta_self_edit_post_shadow(
        proposal,
        shadow,
        snapshot_source=dirs["source"],
        queue_dir=dirs["queue_dir"],
        snapshot_dir=dirs["snapshot_dir"],
        audit_log=dirs["audit_log"],
        clock=_now,
    )
    assert result.decision == GateDecision.REJECTED
    assert result.rejected_at_gate == "shadow-stat"


def test_gate_b_rejects_directional_but_high_p(tmp_path: Path) -> None:
    # a_wins=True with findings_delta=0.3 (≥ min), but p=0.62 (≥ floor 0.1) → reject
    proposal = _meta_self_edit_proposal()
    shadow = _shadow_result(findings_a=5, findings_b=2, n_cycles=10)
    # findings_delta = (5/10) - (2/10) = 0.3 ≥ 0.2 → a_wins=True
    # but p(X>=5|N=7) is high → reject
    assert shadow.delta.a_wins(min_findings_delta=META_SELF_EDIT_FINDINGS_DELTA_MIN)
    dirs = _setup_dirs(tmp_path)
    result = evaluate_meta_self_edit_post_shadow(
        proposal,
        shadow,
        snapshot_source=dirs["source"],
        queue_dir=dirs["queue_dir"],
        snapshot_dir=dirs["snapshot_dir"],
        audit_log=dirs["audit_log"],
        clock=_now,
    )
    assert result.decision == GateDecision.REJECTED
    assert result.rejected_at_gate == "shadow-stat"
    assert "p=" in result.reason


def test_gate_b_rejects_shadow_error(tmp_path: Path) -> None:
    proposal = _meta_self_edit_proposal()
    shadow = _shadow_result(findings_a=0, findings_b=0, error="worktree add failed")
    dirs = _setup_dirs(tmp_path)
    result = evaluate_meta_self_edit_post_shadow(
        proposal,
        shadow,
        snapshot_source=dirs["source"],
        queue_dir=dirs["queue_dir"],
        snapshot_dir=dirs["snapshot_dir"],
        audit_log=dirs["audit_log"],
        clock=_now,
    )
    assert result.decision == GateDecision.REJECTED
    assert result.rejected_at_gate == "shadow-error"


# ---------------- Gates C + D: queue + snapshot ----------------


def test_all_gates_pass_writes_queue_and_snapshot(tmp_path: Path) -> None:
    proposal = _meta_self_edit_proposal()
    # 10 vs 0 → findings_delta=1.0, p ≈ 0.001
    shadow = _shadow_result(findings_a=10, findings_b=0, n_cycles=10)
    dirs = _setup_dirs(tmp_path)
    result = evaluate_meta_self_edit_post_shadow(
        proposal,
        shadow,
        snapshot_source=dirs["source"],
        queue_dir=dirs["queue_dir"],
        snapshot_dir=dirs["snapshot_dir"],
        audit_log=dirs["audit_log"],
        clock=_now,
    )
    assert result.decision == GateDecision.QUEUED
    assert result.rejected_at_gate is None
    # Queue entry exists and references the snapshot
    queue_files = list(dirs["queue_dir"].iterdir())
    assert len(queue_files) == 1
    qbody = queue_files[0].read_text()
    assert "meta_self_edit candidate" in qbody
    assert proposal.id in qbody
    assert "a_wins=True" in qbody
    # Snapshot exists and equals the source content
    snap_files = list(dirs["snapshot_dir"].iterdir())
    assert len(snap_files) == 1
    assert snap_files[0].read_text() == dirs["source"].read_text()
    # Snapshot path appears in queue body (revert recipe)
    assert snap_files[0].name in qbody


def test_queue_entry_contains_proposed_diff(tmp_path: Path) -> None:
    proposal = _meta_self_edit_proposal()
    shadow = _shadow_result(findings_a=10, findings_b=0)
    dirs = _setup_dirs(tmp_path)
    evaluate_meta_self_edit_post_shadow(
        proposal,
        shadow,
        snapshot_source=dirs["source"],
        queue_dir=dirs["queue_dir"],
        snapshot_dir=dirs["snapshot_dir"],
        audit_log=dirs["audit_log"],
        clock=_now,
    )
    qbody = list(dirs["queue_dir"].iterdir())[0].read_text()
    assert "+# diagnostic marker" in qbody
    assert "scripts/meta_loop.py" in qbody


def test_audit_log_records_queued_decision(tmp_path: Path) -> None:
    proposal = _meta_self_edit_proposal()
    shadow = _shadow_result(findings_a=10, findings_b=0)
    dirs = _setup_dirs(tmp_path)
    evaluate_meta_self_edit_post_shadow(
        proposal,
        shadow,
        snapshot_source=dirs["source"],
        queue_dir=dirs["queue_dir"],
        snapshot_dir=dirs["snapshot_dir"],
        audit_log=dirs["audit_log"],
        clock=_now,
    )
    log_text = dirs["audit_log"].read_text()
    # decision column = "queued"
    assert "| queued |" in log_text
    # proposer_id provenance kept
    assert "recursive-meta-v0" in log_text


# ---------------- non-meta_self_edit proposal rejected at function boundary --


def test_function_rejects_non_meta_self_edit_proposal_type(tmp_path: Path) -> None:
    rule_edit = Proposal(
        id="20260528t120000-deadbeef",
        type=ProposalType.RULE_EDIT.value,
        target_path=".claude/rules/agent-stance.md",
        proposed_diff="--- a/x\n+++ b/x\n+ \n",
        evidence_cycles=[1, 2, 3],
    )
    shadow = _shadow_result(findings_a=10, findings_b=0)
    dirs = _setup_dirs(tmp_path)
    with pytest.raises(ValueError, match="meta_self_edit"):
        evaluate_meta_self_edit_post_shadow(
            rule_edit,
            shadow,
            snapshot_source=dirs["source"],
            queue_dir=dirs["queue_dir"],
            snapshot_dir=dirs["snapshot_dir"],
            audit_log=dirs["audit_log"],
            clock=_now,
        )


# ---------------- Gate A also applies through standard evaluate() flow -----


def test_standard_evaluate_uses_10_cycle_threshold_for_meta_self_edit(tmp_path: Path) -> None:
    """The DEFAULT_EVIDENCE_THRESHOLDS update means meta_gate.evaluate also
    enforces ≥10 on meta_self_edit proposals — not just the post-shadow gate."""
    from einstein.meta_loop.meta_gate import (
        DEFAULT_EVIDENCE_THRESHOLDS,
    )
    from einstein.meta_loop.meta_gate import (
        evaluate as standard_evaluate,
    )

    assert DEFAULT_EVIDENCE_THRESHOLDS[ProposalType.META_SELF_EDIT.value] == 10
    # 9 cycles → rejected at evidence-threshold gate in the standard chain
    proposal = _meta_self_edit_proposal(evidence_cycles_count=9)
    audit = tmp_path / "audit.md"
    result = standard_evaluate(proposal, audit_log=audit, clock=_now)
    assert result.decision == GateDecision.REJECTED
    assert result.rejected_at_gate == "evidence-threshold"
    assert "need ≥10" in result.reason
