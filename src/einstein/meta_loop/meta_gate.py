"""meta_loop.meta_gate — 6-gate decision chain for meta-proposals.

Mirrors `src/einstein/auto_submit.py`'s gate pattern. Per
`docs/wiki/findings/meta-loop-design-from-literature.md`:

  Gate order (fail-fast, cheapest first):
    1. Kill switch         — env EINSTEIN_META_LOOP=0 disables the loop
    2. Evidence threshold  — proposal must cite ≥N supporting cycles (per-type)
    3. Daily cap           — default 2 accepted/day across all proposals
    4. Pending throttle    — same (type, target_path) already pending → reject
    5. Shadow gate         — if requires_shadow & shadow not available,
                              mark as shadow-pending (deferred — not rejected)
    6. POST + audit        — append decision row regardless of outcome.

Every decision (accept / reject / shadow-pending) appends one row to
`mb/logs/meta-proposals.md`. Audit-row hygiene is the floor — no silent
rejections.

The shadow gate is "optional" in the sense that proposals with
`requires_shadow=False` pass through; proposals with `requires_shadow=True`
get deferred to the shadow harness (Goal 5) instead of rejected — they
still need human eyes, but they're not abandoned.
"""

from __future__ import annotations

import datetime as dt
import logging
import os
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Callable

from .proposals import Proposal, ProposalStore, ProposalType

log = logging.getLogger("meta_loop.meta_gate")


# ---------------- module constants ----------------


KILL_SWITCH_ENV = "EINSTEIN_META_LOOP"
DEFAULT_DAILY_CAP = 2

# Per-type minimum evidence cycle count. `new_question` is a read-only
# artifact that can stand on findings/dead-ends — cycle count not required.
DEFAULT_EVIDENCE_THRESHOLDS: dict[str, int] = {
    ProposalType.RULE_EDIT.value: 3,
    ProposalType.MANIFEST_TWEAK.value: 3,
    ProposalType.QUEUE_REORDER.value: 3,
    ProposalType.NEW_QUESTION.value: 0,
}

_REPO = Path(__file__).resolve().parents[3]
DEFAULT_AUDIT_LOG = _REPO.parent / "mb" / "logs" / "meta-proposals.md"

AUDIT_LOG_HEADER = (
    "| timestamp_utc | proposal_id | type | target_path | decision | "
    "gate | reason |\n"
    "|---|---|---|---|---|---|---|\n"
)


# ---------------- result ----------------


class GateDecision(str, Enum):
    """Outcome of one evaluate() call."""

    ACCEPTED = "accepted"
    REJECTED = "rejected"
    SHADOW_PENDING = "shadow-pending"


@dataclass
class GateResult:
    decision: GateDecision
    proposal_id: str
    rejected_at_gate: str | None = None
    reason: str = ""


# ---------------- audit log ----------------


def _ensure_audit_header(audit_log: Path) -> None:
    if audit_log.is_file():
        return
    audit_log.parent.mkdir(parents=True, exist_ok=True)
    audit_log.write_text("# meta-proposals audit log\n\n" + AUDIT_LOG_HEADER)


def _append_audit_row(
    audit_log: Path,
    *,
    timestamp: dt.datetime,
    proposal: Proposal,
    decision: GateDecision,
    gate: str | None,
    reason: str,
) -> None:
    _ensure_audit_header(audit_log)
    safe = lambda s: (s or "").replace("|", "\\|")  # noqa: E731
    row = (
        f"| {timestamp.strftime('%Y-%m-%dT%H:%M:%SZ')} "
        f"| {safe(proposal.id)} "
        f"| {safe(proposal.type)} "
        f"| {safe(proposal.target_path)} "
        f"| {decision.value} "
        f"| {safe(gate) or '—'} "
        f"| {safe(reason)} |\n"
    )
    with audit_log.open("a") as fh:
        fh.write(row)


def _parse_audit_log(audit_log: Path) -> list[dict]:
    """Return list of past decisions, oldest first."""
    if not audit_log.is_file():
        return []
    rows: list[dict] = []
    for line in audit_log.read_text().splitlines():
        if not line.startswith("| 20"):
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) < 5:
            continue
        try:
            ts = dt.datetime.strptime(parts[0], "%Y-%m-%dT%H:%M:%SZ")
            ts = ts.replace(tzinfo=dt.timezone.utc)
        except ValueError:
            continue
        rows.append(
            {
                "timestamp": ts,
                "proposal_id": parts[1],
                "type": parts[2],
                "target_path": parts[3],
                "decision": parts[4],
            }
        )
    return rows


# ---------------- main entry point ----------------


def evaluate(
    proposal: Proposal,
    *,
    audit_log: Path | None = None,
    proposals_store: ProposalStore | None = None,
    evidence_thresholds: dict[str, int] | None = None,
    daily_cap: int = DEFAULT_DAILY_CAP,
    shadow_available: bool = False,
    clock: Callable[[], dt.datetime] | None = None,
) -> GateResult:
    """Run the 6-gate chain on `proposal`. Always writes one audit row.

    Args:
        proposal: validated Proposal (from proposals.Proposal — caller is
            expected to have it validated already).
        audit_log: path for the mb/logs/meta-proposals.md audit. Defaults
            to repo-relative DEFAULT_AUDIT_LOG.
        proposals_store: optional — used for the pending-throttle gate.
            None = skip throttle check (e.g. during one-shot tests).
        evidence_thresholds: per-type minimum cycle count; defaults to
            DEFAULT_EVIDENCE_THRESHOLDS.
        daily_cap: max ACCEPTED decisions across all proposal types/day.
        shadow_available: True iff the shadow harness (Goal 5) can run.
            When False and proposal.requires_shadow, the decision is
            "shadow-pending" rather than rejected.
        clock: injectable for testing.

    Returns GateResult.
    """
    log_path = audit_log if audit_log is not None else DEFAULT_AUDIT_LOG
    thresholds = evidence_thresholds or DEFAULT_EVIDENCE_THRESHOLDS
    now = (clock or (lambda: dt.datetime.now(dt.timezone.utc)))()
    if now.tzinfo is None:
        now = now.replace(tzinfo=dt.timezone.utc)

    def _record(*, decision: GateDecision, gate: str | None, reason: str) -> GateResult:
        _append_audit_row(
            log_path,
            timestamp=now,
            proposal=proposal,
            decision=decision,
            gate=gate,
            reason=reason,
        )
        return GateResult(
            decision=decision,
            proposal_id=proposal.id,
            rejected_at_gate=gate if decision == GateDecision.REJECTED else None,
            reason=reason,
        )

    # --- Gate 1: kill switch ----------------------------------------------
    if os.environ.get(KILL_SWITCH_ENV) == "0":
        return _record(
            decision=GateDecision.REJECTED,
            gate="kill-switch",
            reason=f"{KILL_SWITCH_ENV}=0 — meta-loop disabled",
        )

    # --- Gate 2: evidence threshold ---------------------------------------
    needed = thresholds.get(proposal.type, 3)
    have = len(proposal.evidence_cycles)
    if have < needed:
        return _record(
            decision=GateDecision.REJECTED,
            gate="evidence-threshold",
            reason=f"have {have} cycle(s), need ≥{needed} for type={proposal.type}",
        )

    # --- Gate 3: daily cap (counts accepted only) -------------------------
    past = _parse_audit_log(log_path)
    today = now.date()
    accepted_today = sum(
        1
        for r in past
        if r["decision"] == GateDecision.ACCEPTED.value and r["timestamp"].date() == today
    )
    if accepted_today >= daily_cap:
        return _record(
            decision=GateDecision.REJECTED,
            gate="daily-cap",
            reason=f"{accepted_today} accepted today (cap={daily_cap})",
        )

    # --- Gate 4: pending-throttle (avoid duplicate work) ------------------
    if proposals_store is not None:
        pending = proposals_store.list_pending()
        dupes = [
            p
            for p in pending
            if p.id != proposal.id
            and p.type == proposal.type
            and p.target_path == proposal.target_path
        ]
        if dupes:
            return _record(
                decision=GateDecision.REJECTED,
                gate="pending-throttle",
                reason=(
                    f"another proposal for ({proposal.type}, "
                    f"{proposal.target_path}) is already pending: {dupes[0].id}"
                ),
            )

    # --- Gate 5: shadow gate (optional — defers, doesn't reject) ----------
    if proposal.requires_shadow and not shadow_available:
        return _record(
            decision=GateDecision.SHADOW_PENDING,
            gate="shadow-required",
            reason="proposal requires shadow A/B; harness not yet available (Goal 5)",
        )

    # --- Gate 6: accept (audit row appended by _record) -------------------
    return _record(
        decision=GateDecision.ACCEPTED,
        gate=None,
        reason=(
            f"all gates passed — evidence={have}/{needed}, "
            f"accepted_today={accepted_today}/{daily_cap}"
        ),
    )


__all__ = [
    "DEFAULT_AUDIT_LOG",
    "DEFAULT_DAILY_CAP",
    "DEFAULT_EVIDENCE_THRESHOLDS",
    "GateDecision",
    "GateResult",
    "KILL_SWITCH_ENV",
    "evaluate",
]
