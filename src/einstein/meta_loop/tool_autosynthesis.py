"""meta_loop.tool_autosynthesis — Goal 5 promotion gate + audit log.

The promotion verdict for `code_edit` proposals. Citation-grounded: B
wins iff the proposed tool was actually invoked AND produced a finding in
the B-arm, AND the A-arm didn't regress, AND the validator passed.

The fifth gate — human approval — is reflected by a separate
`Decision.promoted` field that callers set explicitly. The mechanical
gates produce `b_wins=True/False + reason`; promotion requires both
`b_wins` AND human sign-off.

Audit log: `mb/logs/tool-autosynthesis.md`. Schema mirrors
`mb/logs/meta-shadow-runs.md`. Reject paths log too — transparency over
silent drops.
"""

from __future__ import annotations

import datetime as dt
from dataclasses import dataclass
from pathlib import Path

from .sandbox import ValidationReport
from .shadow import ArmMetrics

# ---------------- decision ----------------


@dataclass(frozen=True)
class ToolPromotionDecision:
    """Result of the mechanical promotion check (gates 1–4).

    Promotion (mv from `scripts/proposed/<slug>.py` to `scripts/<slug>.py`
    + manifest commit on `main`) requires `b_wins=True` AND an explicit
    human approval. The decision itself only carries the mechanical
    verdict; `promoted` is what the human flips after reading the audit
    row.
    """

    b_wins: bool
    reason: str
    arm_a_findings: int
    arm_b_findings: int
    tool_invoked_cycles_b: int
    validator_passed: bool
    # Set True by the human after `b_wins == True`.
    promoted: bool = False


def tool_autosynthesis_promotion_decision(
    *,
    arm_a: ArmMetrics,
    arm_b: ArmMetrics,
    validator: ValidationReport | None,
    min_a_findings_delta: int = 0,
) -> ToolPromotionDecision:
    """Citation-grounded promotion gate for `code_edit` proposals.

    B wins iff ALL of:
      1. validator.passed (or None — explicit "skipped" case, e.g. dry-run)
      2. arm_b.tool_invoked_cycles >= 1   (the tool was actually dispatched)
      3. arm_b.findings_added >= 1         (the dispatch produced a finding)
      4. arm_b.findings_added - arm_a.findings_added >= min_a_findings_delta
                                            (no A regression)

    Gate 1 differs from research-synthesis: there, the validator step
    doesn't exist (rule_edit is a markdown swap). Here the validator is a
    hard gate — a draft that can't even import shouldn't survive shadow.

    Args:
        arm_a: control metrics (existing manifest, no proposed tool).
        arm_b: treatment metrics (manifest wired with the proposed tool).
        validator: result of `validate_proposed_tool` on the draft body.
            `None` means "validator wasn't run" — treated as a fail
            (defensive). Pass an explicit no-op report to bypass for
            tests.
        min_a_findings_delta: how much B can lag A on findings before we
            consider it a regression. Default 0 means "B must match or
            exceed A's findings count."
    """
    reasons: list[str] = []
    validator_ok = validator is not None and validator.passed
    if validator is None:
        reasons.append("validator did not run")
    elif not validator.passed:
        reasons.append("validator failed")
    if arm_b.tool_invoked_cycles < 1:
        reasons.append(f"B-arm did not invoke the tool ({arm_b.tool_invoked_cycles} cycles cited)")
    if arm_b.findings_added < 1:
        reasons.append(f"B-arm produced no findings ({arm_b.findings_added})")
    findings_delta = arm_b.findings_added - arm_a.findings_added
    if findings_delta < min_a_findings_delta:
        reasons.append(f"A regressed: findings_delta={findings_delta} < {min_a_findings_delta}")

    b_wins = not reasons
    if b_wins:
        reason = (
            f"b_wins=true (validator_ok=true, tool_invoked_B={arm_b.tool_invoked_cycles}, "
            f"findings_B={arm_b.findings_added}, findings_A={arm_a.findings_added})"
        )
    else:
        reason = "b_wins=false: " + "; ".join(reasons)

    return ToolPromotionDecision(
        b_wins=b_wins,
        reason=reason,
        arm_a_findings=arm_a.findings_added,
        arm_b_findings=arm_b.findings_added,
        tool_invoked_cycles_b=arm_b.tool_invoked_cycles,
        validator_passed=validator_ok,
    )


# ---------------- audit log ----------------


AUDIT_LOG_HEADER = (
    "| timestamp_utc | proposal_id | tool_slug | n_cycles_per_arm "
    "| A_findings | B_findings | tool_invoked_cycles_B "
    "| validator_passed | b_wins | promoted | reason |\n"
    "|---|---|---|---|---|---|---|---|---|---|---|\n"
)


def _ensure_audit_log_header(path: Path) -> None:
    if path.is_file():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("# tool-autosynthesis audit log\n\n" + AUDIT_LOG_HEADER)


def append_audit_row(
    path: Path,
    *,
    timestamp: dt.datetime,
    proposal_id: str,
    tool_slug: str,
    n_cycles: int,
    decision: ToolPromotionDecision,
) -> None:
    """Append one row — accept or reject. Always logged.

    Promote-or-reject is captured in `decision.promoted`. A
    `b_wins=true, promoted=false` row is the "mechanical pass, human
    didn't promote" case; a `b_wins=false, promoted=false` row is the
    "mechanical reject" case. Both are useful audit signals.
    """
    _ensure_audit_log_header(path)
    row = (
        f"| {timestamp.strftime('%Y-%m-%dT%H:%M:%SZ')} "
        f"| {proposal_id} | {tool_slug} | {n_cycles} "
        f"| {decision.arm_a_findings} | {decision.arm_b_findings} "
        f"| {decision.tool_invoked_cycles_b} "
        f"| {'yes' if decision.validator_passed else 'no'} "
        f"| {'yes' if decision.b_wins else 'no'} "
        f"| {'yes' if decision.promoted else 'no'} "
        f"| {decision.reason} |\n"
    )
    with path.open("a") as fh:
        fh.write(row)


__all__ = [
    "AUDIT_LOG_HEADER",
    "ToolPromotionDecision",
    "append_audit_row",
    "tool_autosynthesis_promotion_decision",
]
