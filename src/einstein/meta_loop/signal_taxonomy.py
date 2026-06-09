"""meta_loop.signal_taxonomy — Phase 1: classify a cycle's high-value signals
and route each to its capture destination.

Gap 3 of `docs/agent/meta-learning-automation.md`: "high-quality signal" was
undefined, so capture was discretionary. This formalizes the 5-row taxonomy the
design doc names and auto-routes each fired signal:

| Signal (machine-detectable)        | Owed artifact / destination                |
|------------------------------------|--------------------------------------------|
| record / top-3                     | positive finding + skill-library top3++    |
| dead-end (Δ<min after a wall)      | findings/dead-end-* WITH "what-might-…"    |
| triple-verify disagreement         | verifier-mismatch finding; flag submission |
| mechanism verified on ≥2 problems  | promotion-log row (human-gated → concept)  |
| prior violated (e.g. a tie beaten) | finding + a rule_edit proposal             |

Design split (honest about what is deterministic):

- **Classification** (`classify_signals`) is a pure function — fully testable.
- **Routing** (`route_signals`) performs only the *deterministic, safe* side:
  it always appends a per-signal audit line to a capture-queue JSONL, surfaces a
  promotion *candidate* (human-gated, deduped) for cross-problem mechanisms, and
  emits a `rule_edit` proposal *stub* (deduped) for prior-violations. It never
  fabricates finding prose — that is the LLM/human's job, and the Phase-0
  capture-gate (`docs/tools/capture_gate.py`) is what enforces it got written.

**Over-firing guard (the design's Phase-1 open question):** the live loop passes
`mechanism_problem_count=1` by default, so the human-gated `promote` action stays
dormant until a real cross-cycle counter feeds it ≥2; routing additionally dedupes
against the existing promotion-log and pending proposals.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path

# Outcomes / note markers that the autonomous loop already emits (see
# scripts/autonomous_loop.py::_call_auto_submit and the result-dict builder).
RECORD_OUTCOMES = {"improved-and-submitted", "conquered"}
_SUBMITTED_MARKER = "auto-submit: SUBMITTED"
_DEAD_END_MARKER = "dead_end="
_TV_FAIL_MARKERS = ("triple-verify=fail", "auto-submit-rejected@triple_verify")

# Default rule the prior-violated signal proposes editing — the n-agent-tie /
# floor-claim rule, which is exactly what was edited on 2026-06-08 when a
# documented "honest-zero" P2 floor was beaten.
DEFAULT_PRIOR_VIOLATED_RULE = ".claude/rules/wall-hit-escalation.md"


@dataclass(frozen=True)
class Signal:
    """One fired signal + the artifact it owes and where that lands."""

    name: str
    action: str
    destination: str
    human_gated: bool = False
    rationale: str = ""


# --------------------------------------------------------------- classification


def classify_signals(
    result: dict,
    *,
    arena_sota: float | None = None,
    prior_floor: float | None = None,
    mechanism_problem_count: int = 1,
    prior_violated_rule: str = DEFAULT_PRIOR_VIOLATED_RULE,
) -> list[Signal]:
    """Return the signals fired by one cycle `result` (the dict shaped for
    `format_cycle_log_row`). Zero, one, or several may fire.

    Inputs beyond the result dict are optional context the caller supplies when
    it has them:
      - `prior_floor`: a documented "floor"/"honest-zero" score the cycle may
        have overridden (→ prior_violated).
      - `mechanism_problem_count`: distinct problems a mechanism is now verified
        on (≥2 → cross_problem_mechanism). Defaults to 1 (the over-firing guard).
    `arena_sota` is accepted for symmetry / future direction-aware checks; the
    record signal is keyed off the outcome the auto-submit gate chain already
    produced, which is the authoritative "this beat arena #1" verdict.
    """
    outcome = str(result.get("outcome", ""))
    notes = str(result.get("notes", ""))
    end_score = result.get("end_score")

    signals: list[Signal] = []

    is_record = outcome in RECORD_OUTCOMES or _SUBMITTED_MARKER in notes
    if is_record:
        signals.append(
            Signal(
                name="record",
                action="author positive finding + technique; skill-library top3++",
                destination="docs/wiki/findings/",
                rationale=f"outcome={outcome}",
            )
        )

    if outcome == "dead-end" or _DEAD_END_MARKER in notes:
        signals.append(
            Signal(
                name="dead_end",
                action='author findings/dead-end-* WITH a "What might still work" section',
                destination=_dead_end_path(notes) or "docs/wiki/findings/dead-end-*.md",
                rationale="Δ<min after a wall",
            )
        )

    if any(m in notes for m in _TV_FAIL_MARKERS):
        signals.append(
            Signal(
                name="triple_verify_disagreement",
                action="author verifier-mismatch finding; flag submission for review",
                destination="docs/wiki/findings/",
                rationale="triple-verify did not pass — local↔arena drift suspected",
            )
        )

    if mechanism_problem_count >= 2:
        signals.append(
            Signal(
                name="cross_problem_mechanism",
                action="surface promotion candidate (human-gated → concept)",
                destination="docs/agent/promotion-log.md",
                human_gated=True,
                rationale=f"mechanism verified on {mechanism_problem_count} problems",
            )
        )

    if is_record and prior_floor is not None and _beats_floor(end_score, prior_floor):
        signals.append(
            Signal(
                name="prior_violated",
                action="author finding + propose a rule_edit (a documented prior was wrong)",
                destination=prior_violated_rule,
                rationale=f"end_score {end_score} beat documented floor {prior_floor}",
            )
        )

    return signals


def _beats_floor(end_score: object, prior_floor: float) -> bool:
    """Direction-agnostic 'the documented floor was crossed': any strict
    difference from the recorded floor counts (a floor claimed as unbeatable
    that moved at all is a violated prior)."""
    if not isinstance(end_score, (int, float)):
        return False
    return abs(float(end_score) - float(prior_floor)) > 0


_DEAD_END_RE = re.compile(r"dead_end=([^\s;]+)")


def _dead_end_path(notes: str) -> str | None:
    m = _DEAD_END_RE.search(notes)
    return m.group(1) if m else None


# ------------------------------------------------------------------- routing


@dataclass(frozen=True)
class RoutedAction:
    """What `route_signals` actually did (or would do, in dry_run) per signal."""

    signal: str
    action: str
    target: str
    performed: bool


def route_signals(
    signals: list[Signal],
    *,
    capture_queue: Path,
    promotion_log: Path | None = None,
    proposal_store=None,  # meta_loop.proposals.ProposalStore | None
    cycle_id: int | None = None,
    problem: str = "",
    mechanism_key: str = "",
    dry_run: bool = False,
) -> list[RoutedAction]:
    """Perform the deterministic capture side for each fired signal.

    Always: append one audit line per signal to `capture_queue` (JSONL).
    `cross_problem_mechanism`: append a promotion-log candidate row, deduped
    against existing rows (the human-gated surface — never auto-promotes).
    `prior_violated`: write a `rule_edit` proposal stub to `proposal_store`,
    deduped against pending proposals for the same target rule.
    """
    actions: list[RoutedAction] = []
    for sig in signals:
        if not dry_run:
            _append_capture_queue(
                capture_queue,
                {
                    "cycle_id": cycle_id,
                    "problem": problem,
                    "signal": sig.name,
                    "action": sig.action,
                    "destination": sig.destination,
                    "human_gated": sig.human_gated,
                    "rationale": sig.rationale,
                },
            )
        actions.append(RoutedAction(sig.name, "queue", str(capture_queue), not dry_run))

        if sig.name == "cross_problem_mechanism" and promotion_log is not None:
            performed = _append_promotion_candidate(
                promotion_log,
                mechanism_key=mechanism_key or problem,
                rationale=sig.rationale,
                dry_run=dry_run,
            )
            actions.append(
                RoutedAction(sig.name, "promotion-candidate", str(promotion_log), performed)
            )

        if sig.name == "prior_violated" and proposal_store is not None:
            target, performed = _emit_rule_edit_stub(
                proposal_store,
                rule_path=sig.destination,
                rationale=sig.rationale,
                cycle_id=cycle_id,
                dry_run=dry_run,
            )
            actions.append(RoutedAction(sig.name, "rule_edit-proposal", target, performed))

    return actions


def _append_capture_queue(path: Path, record: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    line = json.dumps(record, sort_keys=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(line + "\n")


def _append_promotion_candidate(
    promotion_log: Path, *, mechanism_key: str, rationale: str, dry_run: bool
) -> bool:
    """Append a candidate row to the promotion-log, deduped by mechanism_key.
    Returns True iff a row was (or would be, dry_run) written."""
    existing = promotion_log.read_text(encoding="utf-8") if promotion_log.exists() else ""
    if mechanism_key and mechanism_key in existing:
        return False  # over-firing guard: already surfaced
    if dry_run:
        return True
    row = (
        f"| (candidate) | {mechanism_key} | (pending human review) | — | "
        f"{rationale} | unreviewed |\n"
    )
    header = (
        ""
        if existing
        else "| Date | Source finding | New concept | Cite count at promotion | Rationale | Approver |\n|---|---|---|---|---|---|\n"
    )
    with promotion_log.open("a", encoding="utf-8") as fh:
        if header:
            fh.write(header)
        fh.write(row)
    return True


def _emit_rule_edit_stub(
    proposal_store, *, rule_path: str, rationale: str, cycle_id: int | None, dry_run: bool
) -> tuple[str, bool]:
    """Write a deduped `rule_edit` proposal stub. Returns (target, performed)."""
    from einstein.meta_loop.proposals import (
        Proposal,
        ProposalType,
        make_proposal_id,
    )

    # Dedupe: skip if a pending proposal already targets this rule.
    try:
        for p in proposal_store.list_pending():
            if p.type == ProposalType.RULE_EDIT.value and p.target_path == rule_path:
                return rule_path, False
    except Exception:  # pragma: no cover — store read best-effort
        pass

    if dry_run:
        return rule_path, True

    pid = make_proposal_id(proposal_type=ProposalType.RULE_EDIT.value, target_path=rule_path)
    stub_diff = (
        f"# TODO(human/agent): a documented prior in {rule_path} was violated this "
        f"cycle.\n# {rationale}\n# Draft the rule edit that records the corrected "
        f"prior, then replace this stub with a real unified diff.\n"
    )
    proposal = Proposal(
        id=pid,
        type=ProposalType.RULE_EDIT.value,
        target_path=rule_path,
        proposed_diff=stub_diff,
        evidence_cycles=[cycle_id] if cycle_id is not None else [],
        rationale=rationale,
        proposer_id="signal-taxonomy-v0",
    )
    try:
        proposal_store.write_pending(proposal)
        return rule_path, True
    except FileExistsError:  # pragma: no cover — id collision, treat as deduped
        return rule_path, False
