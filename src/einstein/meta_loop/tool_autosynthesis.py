"""meta_loop.tool_autosynthesis — Goal 5 promotion gate + audit log.

The promotion verdict for `code_edit` proposals. Citation-grounded: A
wins iff the proposed tool was actually invoked AND produced a finding in
the A-arm, AND the B-arm (control) didn't outperform it, AND the
validator passed.

**Arm convention (matches `research_synthesis_shadow.py` and
`shadow.run_shadow`):**
- **A** = treatment. The proposal is applied to arm A — for `code_edit`,
  that means the draft is graduated to `scripts/<slug>.py` and the
  manifest is wired (see `shadow._apply_code_edit_graduation`).
- **B** = control. Untouched HEAD; the proposed tool is absent.

The fifth gate — human approval — is reflected by a separate
`Decision.promoted` field that callers set explicitly. The mechanical
gates produce `a_wins=True/False + reason`; promotion requires both
`a_wins` AND human sign-off.

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
    + manifest commit on `main`) requires `a_wins=True` AND an explicit
    human approval. The decision itself only carries the mechanical
    verdict; `promoted` is what the human flips after reading the audit
    row.
    """

    a_wins: bool
    reason: str
    arm_a_findings: int
    arm_b_findings: int
    tool_invoked_cycles_a: int
    validator_passed: bool
    # Set True by the human after `a_wins == True`.
    promoted: bool = False


def tool_autosynthesis_promotion_decision(
    *,
    arm_a: ArmMetrics,
    arm_b: ArmMetrics,
    validator: ValidationReport | None,
    min_b_findings_delta: int = 0,
) -> ToolPromotionDecision:
    """Citation-grounded promotion gate for `code_edit` proposals.

    Arm convention: A = treatment (proposal applied), B = control. Matches
    `shadow.run_shadow` which calls `apply_proposal_to_worktree(proposal,
    arm_a, ...)` and `research_synthesis_shadow`'s "arm A: this proposal
    applied / arm B: control" phrasing.

    A wins iff ALL of:
      1. validator.passed (or None — explicit "skipped" case, e.g. dry-run)
      2. arm_a.tool_invoked_cycles >= 1   (the tool was actually dispatched)
      3. arm_a.findings_added >= 1         (the dispatch produced a finding)
      4. arm_a.findings_added - arm_b.findings_added >= min_b_findings_delta
                                            (no regression vs control)

    Gate 1 differs from research-synthesis: there, the validator step
    doesn't exist (rule_edit is a markdown swap). Here the validator is a
    hard gate — a draft that can't even import shouldn't survive shadow.

    Args:
        arm_a: treatment metrics (manifest wired with the proposed tool).
        arm_b: control metrics (existing manifest, no proposed tool).
        validator: result of `validate_proposed_tool` on the draft body.
            `None` means "validator wasn't run" — treated as a fail
            (defensive). Pass an explicit no-op report to bypass for
            tests.
        min_b_findings_delta: how much A can lag B on findings before we
            consider it a regression. Default 0 means "A must match or
            exceed B's findings count."
    """
    reasons: list[str] = []
    validator_ok = validator is not None and validator.passed
    if validator is None:
        reasons.append("validator did not run")
    elif not validator.passed:
        reasons.append("validator failed")
    if arm_a.tool_invoked_cycles < 1:
        reasons.append(f"A-arm did not invoke the tool ({arm_a.tool_invoked_cycles} cycles cited)")
    if arm_a.findings_added < 1:
        reasons.append(f"A-arm produced no findings ({arm_a.findings_added})")
    findings_delta = arm_a.findings_added - arm_b.findings_added
    if findings_delta < min_b_findings_delta:
        reasons.append(
            f"A regressed vs control: findings_delta={findings_delta} < {min_b_findings_delta}"
        )

    a_wins = not reasons
    if a_wins:
        reason = (
            f"a_wins=true (validator_ok=true, tool_invoked_A={arm_a.tool_invoked_cycles}, "
            f"findings_A={arm_a.findings_added}, findings_B={arm_b.findings_added})"
        )
    else:
        reason = "a_wins=false: " + "; ".join(reasons)

    return ToolPromotionDecision(
        a_wins=a_wins,
        reason=reason,
        arm_a_findings=arm_a.findings_added,
        arm_b_findings=arm_b.findings_added,
        tool_invoked_cycles_a=arm_a.tool_invoked_cycles,
        validator_passed=validator_ok,
    )


# ---------------- audit log ----------------


AUDIT_LOG_HEADER = (
    "| timestamp_utc | proposal_id | tool_slug | n_cycles_per_arm "
    "| A_findings (treatment) | B_findings (control) | tool_invoked_cycles_A "
    "| validator_passed | a_wins | promoted | reason |\n"
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

    Promote-or-reject is captured in `decision.promoted`. An
    `a_wins=true, promoted=false` row is the "mechanical pass, human
    didn't promote" case; an `a_wins=false, promoted=false` row is the
    "mechanical reject" case. Both are useful audit signals.
    """
    _ensure_audit_log_header(path)
    row = (
        f"| {timestamp.strftime('%Y-%m-%dT%H:%M:%SZ')} "
        f"| {proposal_id} | {tool_slug} | {n_cycles} "
        f"| {decision.arm_a_findings} | {decision.arm_b_findings} "
        f"| {decision.tool_invoked_cycles_a} "
        f"| {'yes' if decision.validator_passed else 'no'} "
        f"| {'yes' if decision.a_wins else 'no'} "
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
