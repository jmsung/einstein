"""Tests for src/einstein/meta_loop/tool_autosynthesis.py — Goal 5 gate + audit log."""

from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein.meta_loop.sandbox import StepResult, ValidationReport  # noqa: E402
from einstein.meta_loop.shadow import ArmMetrics  # noqa: E402
from einstein.meta_loop.tool_autosynthesis import (  # noqa: E402
    AUDIT_LOG_HEADER,
    append_audit_row,
    tool_autosynthesis_promotion_decision,
)

UTC = dt.timezone.utc


def _arm(
    *,
    cycles: int = 10,
    score_changed: int = 0,
    findings: int = 0,
    concepts: int = 0,
    dead_ends: int = 0,
    tool_invoked: int = 0,
) -> ArmMetrics:
    return ArmMetrics(
        cycles=cycles,
        score_changed_cycles=score_changed,
        findings_added=findings,
        concepts_added=concepts,
        dead_ends_added=dead_ends,
        tool_invoked_cycles=tool_invoked,
    )


def _validator(passed: bool = True) -> ValidationReport:
    rep = ValidationReport(target_path="scripts/proposed/x.py")
    rep.steps.append(StepResult(name="ruff", ok=passed))
    rep.steps.append(StepResult(name="import", ok=passed))
    rep.steps.append(StepResult(name="pytest", ok=True, skipped=True))
    return rep


# ---------------- gate logic ----------------


def test_b_wins_when_all_gates_pass() -> None:
    d = tool_autosynthesis_promotion_decision(
        arm_a=_arm(findings=1),
        arm_b=_arm(findings=2, tool_invoked=3),
        validator=_validator(),
    )
    assert d.b_wins
    assert d.validator_passed
    assert d.tool_invoked_cycles_b == 3
    assert d.arm_b_findings == 2


def test_b_loses_when_tool_not_invoked() -> None:
    d = tool_autosynthesis_promotion_decision(
        arm_a=_arm(findings=0),
        arm_b=_arm(findings=2, tool_invoked=0),
        validator=_validator(),
    )
    assert not d.b_wins
    assert "did not invoke" in d.reason


def test_b_loses_when_no_finding_in_b() -> None:
    d = tool_autosynthesis_promotion_decision(
        arm_a=_arm(findings=0),
        arm_b=_arm(findings=0, tool_invoked=2),
        validator=_validator(),
    )
    assert not d.b_wins
    assert "produced no findings" in d.reason


def test_b_loses_when_validator_failed() -> None:
    d = tool_autosynthesis_promotion_decision(
        arm_a=_arm(findings=0),
        arm_b=_arm(findings=2, tool_invoked=1),
        validator=_validator(passed=False),
    )
    assert not d.b_wins
    assert not d.validator_passed
    assert "validator failed" in d.reason


def test_b_loses_when_validator_none() -> None:
    d = tool_autosynthesis_promotion_decision(
        arm_a=_arm(findings=0),
        arm_b=_arm(findings=2, tool_invoked=1),
        validator=None,
    )
    assert not d.b_wins
    assert "validator did not run" in d.reason


def test_b_loses_when_a_regression() -> None:
    """B had findings AND used the tool but A produced more — regression."""
    d = tool_autosynthesis_promotion_decision(
        arm_a=_arm(findings=5),
        arm_b=_arm(findings=2, tool_invoked=2),
        validator=_validator(),
    )
    assert not d.b_wins
    assert "regressed" in d.reason


def test_human_promote_flag_default_false() -> None:
    d = tool_autosynthesis_promotion_decision(
        arm_a=_arm(findings=0),
        arm_b=_arm(findings=1, tool_invoked=1),
        validator=_validator(),
    )
    assert d.b_wins
    # Even when mechanical gates pass, promoted=False until the human flips it
    assert d.promoted is False


# ---------------- audit log ----------------


def test_append_audit_row_creates_header(tmp_path: Path) -> None:
    log = tmp_path / "tool-autosynthesis.md"
    d = tool_autosynthesis_promotion_decision(
        arm_a=_arm(findings=0),
        arm_b=_arm(findings=1, tool_invoked=1),
        validator=_validator(),
    )
    append_audit_row(
        log,
        timestamp=dt.datetime(2026, 5, 31, 12, 0, 0, tzinfo=UTC),
        proposal_id="prop-abc",
        tool_slug="mpmath-ulp-polish",
        n_cycles=10,
        decision=d,
    )
    body = log.read_text()
    assert AUDIT_LOG_HEADER.strip() in body
    assert "mpmath-ulp-polish" in body
    assert "prop-abc" in body
    assert "2026-05-31T12:00:00Z" in body


def test_append_audit_row_logs_reject_path_too(tmp_path: Path) -> None:
    """Rejects must be logged. Transparency over silent drops."""
    log = tmp_path / "tool-autosynthesis.md"
    d = tool_autosynthesis_promotion_decision(
        arm_a=_arm(findings=5),
        arm_b=_arm(findings=2, tool_invoked=1),  # A regression
        validator=_validator(),
    )
    assert not d.b_wins
    append_audit_row(
        log,
        timestamp=dt.datetime(2026, 5, 31, 12, 0, 0, tzinfo=UTC),
        proposal_id="prop-reject",
        tool_slug="some-tool",
        n_cycles=10,
        decision=d,
    )
    body = log.read_text()
    # Both columns "b_wins" and "promoted" must show 'no'
    last_row = body.strip().splitlines()[-1]
    cols = [c.strip() for c in last_row.strip("|").split("|")]
    # cols: ts, id, slug, n, A_f, B_f, tool_inv_B, val_passed, b_wins, promoted, reason
    assert cols[8] == "no"  # b_wins
    assert cols[9] == "no"  # promoted
    assert "regressed" in cols[10]


def test_append_audit_row_appends_idempotently(tmp_path: Path) -> None:
    log = tmp_path / "tool-autosynthesis.md"
    d = tool_autosynthesis_promotion_decision(
        arm_a=_arm(),
        arm_b=_arm(findings=1, tool_invoked=1),
        validator=_validator(),
    )
    for i in range(3):
        append_audit_row(
            log,
            timestamp=dt.datetime(2026, 5, 31, 12, 0, i, tzinfo=UTC),
            proposal_id=f"prop-{i}",
            tool_slug="t",
            n_cycles=5,
            decision=d,
        )
    # header + 3 rows
    rows = [line for line in log.read_text().splitlines() if line.startswith("| 2026-")]
    assert len(rows) == 3
