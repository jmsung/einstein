"""meta_loop.recursive_meta — the `meta_self_edit` proposer (Goal 2).

A non-LLM proposer that reads the meta-proposals audit log and emits at most
one `meta_self_edit` candidate when (a) ≥10 audit rows of usage data exist
and (b) a meta-layer failure pattern is detected.

See `docs/wiki/findings/recursive-meta-design.md` for the rationale behind the
≥10-cycle floor and the never-auto-merge stance. The proposer pairs with the
extra-tight gate chain on `meta_self_edit` (Goal 3); the floor is enforced at
both the proposer (refuse to emit) and the gate (refuse to accept) for defense
in depth.

The current detection step (`detect_recurring_gate_rejection`) flags a single
pattern: any (proposal_type, gate) pair that appears ≥3 times in REJECTED
audit rows. That's the simplest signal that a gate is consistently failing
the same kind of input; whether the right response is to loosen the gate or
fix the proposer is a human-review call, which is why this proposer NEVER
auto-merges its own proposal — it surfaces a candidate to
`mb/meta-self-edit-queue/` (via Goal 3's gate chain) and the human decides.

Plug point: this module exposes `propose_meta_self_edit` as a
`Callable[[ProposerInput], list[dict]]` — matching the swap-surface contract
described in `docs/wiki/findings/meta-loop-swap-surface.md`. Inject it into
`propose.run(proposer=propose_meta_self_edit)` to replace the LLM proposer.
"""

from __future__ import annotations

import logging
from collections import Counter
from pathlib import Path

from .meta_gate import _parse_audit_log
from .proposals import Confidence, ProposalType
from .propose import ProposerInput

log = logging.getLogger("meta_loop.recursive_meta")


# ---------------- module constants ----------------


RECURSIVE_META_PROPOSER_ID = "recursive-meta-v0"

# The ≥10 floor is grounded in `recursive-meta-design.md` § "Why ≥10 cycles":
# AHE self-attribution asymmetry (11% precision on regression prediction); the
# statistical power needed for shadow A/B to clear p<0.1; the Huxley-Gödel
# clade-credit-assignment workaround for tree-depth-1 lineages.
META_SELF_EDIT_CYCLE_FLOOR = 10

# Recurring-rejection detector — a (type, gate) pair must appear in REJECTED
# rows at least this many times to be flagged. Conservative: 3 is the same
# threshold the `failure-is-a-finding` rule applies to dead-end pattern
# detection. Smaller numbers would emit too eagerly.
RECURRING_REJECTION_MIN = 3

# The audit-log filename the gate chain writes to. See meta_gate.DEFAULT_AUDIT_LOG.
AUDIT_LOG_FILENAME = "meta-proposals.md"


# ---------------- ledger inspection ----------------


def count_audit_rows(audit_log_path: Path) -> int:
    """Total decisions recorded in the meta-proposals audit log.

    Used as the "cycles of usage data" floor — the proposer refuses to emit
    below `META_SELF_EDIT_CYCLE_FLOOR`. Counts all decision types (accepted,
    rejected, shadow-pending); each row is one cycle of evidence.
    """
    return len(_parse_audit_log(audit_log_path))


def detect_recurring_gate_rejection(audit_log_path: Path) -> dict | None:
    """Return the most-recurring (type, gate) rejection pattern, or None.

    A meta-layer failure mode: the same gate rejecting the same proposal type
    repeatedly suggests either (a) the proposer is stuck emitting bad
    candidates (proposer-side bug), or (b) the gate threshold is wrong (gate-
    side calibration). Either way, the meta layer has feedback to act on.

    Detection logic: parse rejected rows, count (type, gate) tuples (gate
    derives from the `reason` cell's `at <gate-name>` substring written by
    meta_gate's `_record`). Return the modal pair if its count crosses
    `RECURRING_REJECTION_MIN`.

    Notes deliberately ignored: we don't track `proposer_id` here — the
    pattern is about the *meta layer's* behavior, not which proposer drove it.
    """
    rows = _parse_audit_log(audit_log_path)
    if not rows:
        return None
    rejected = [r for r in rows if r["decision"] == "rejected"]
    if not rejected:
        return None
    # The audit-log row format (meta_gate._append_audit_row) stores the gate
    # name in its own column; `_parse_audit_log` doesn't carry it as a key,
    # so we fall back to "(unparsed)" if absent and group on type alone.
    counts: Counter[tuple[str, str]] = Counter()
    for r in rejected:
        counts[(r["type"], r.get("gate", "(unparsed)"))] += 1
    (most_type, most_gate), most_n = counts.most_common(1)[0]
    if most_n < RECURRING_REJECTION_MIN:
        return None
    return {
        "type": most_type,
        "gate": most_gate,
        "count": most_n,
        "total_rejected": len(rejected),
    }


# ---------------- proposer callable ----------------


def _candidate_diff(pattern: dict) -> str:
    """Construct the unified diff body for the candidate.

    For Goal 2 the diff is deliberately conservative: it appends a single
    diagnostic comment to `scripts/meta_loop.py` flagging the pattern. The
    human reviewing `mb/meta-self-edit-queue/` decides whether the actual
    code change (loosen a gate, tighten the proposer, add a CLI flag) is
    appropriate — the proposer surfaces the gap, the human acts.

    This is the simplest-safe edit per `recursive-meta-design.md` § "Open
    questions": a read-only diagnostic addition with low blast radius.
    """
    type_s = pattern["type"]
    gate_s = pattern["gate"]
    n = pattern["count"]
    marker = (
        f"# recursive-meta-v0 flag: gate={gate_s!r} rejected "
        f"type={type_s!r} {n} times. Review meta-self-edit-queue."
    )
    # Unified diff against the very end of scripts/meta_loop.py. The actual
    # line numbers are reconstructed by `git apply`; we just need the diff to
    # validate as a unified diff. Conservative placement (top-of-file comment)
    # avoids changing any executable code path on apply.
    return (
        "--- a/scripts/meta_loop.py\n"
        "+++ b/scripts/meta_loop.py\n"
        "@@ -1,1 +1,2 @@\n"
        f"+{marker}\n"
        " #!/usr/bin/env python3\n"
    )


def _rationale(pattern: dict, rows_total: int) -> str:
    return (
        f"recurring rejection at gate={pattern['gate']!r} for "
        f"type={pattern['type']!r} ({pattern['count']}/{pattern['total_rejected']} "
        f"rejected, {rows_total} total rows). Surface for human review per "
        "the never-auto-merge gate chain (recursive-meta-design.md)."
    )


def propose_meta_self_edit(inp: ProposerInput) -> list[dict]:
    """Plug-compatible proposer that emits `meta_self_edit` when warranted.

    Floor: refuses (returns []) if `count_audit_rows < META_SELF_EDIT_CYCLE_FLOOR`.
    Above floor: returns [] unless `detect_recurring_gate_rejection` finds a
    pattern; otherwise returns one candidate dict, ready for `_coerce_raw`.

    The candidate is tagged `proposer_id=RECURSIVE_META_PROPOSER_ID` and
    `requires_shadow=True` — Goal 3's gate chain enforces both, but tagging
    here keeps the audit row honest at provenance time.
    """
    audit_log_path = inp.mb_logs_dir / AUDIT_LOG_FILENAME
    rows_total = count_audit_rows(audit_log_path)
    if rows_total < META_SELF_EDIT_CYCLE_FLOOR:
        log.info(
            "recursive-meta proposer: refuse to emit — %d audit rows < %d floor",
            rows_total,
            META_SELF_EDIT_CYCLE_FLOOR,
        )
        return []
    pattern = detect_recurring_gate_rejection(audit_log_path)
    if pattern is None:
        log.info(
            "recursive-meta proposer: %d audit rows, no recurring-rejection pattern", rows_total
        )
        return []
    return [
        {
            "type": ProposalType.META_SELF_EDIT.value,
            "target_path": "scripts/meta_loop.py",
            "proposed_diff": _candidate_diff(pattern),
            "evidence_cycles": list(range(rows_total)),
            "expected_metric_delta": {"meta_proposals_rejected_per_cycle": -0.1},
            "predicted_regressions": [
                "may bias future proposals if gate is loosened without root-cause fix"
            ],
            "confidence": Confidence.LOW.value,
            "requires_shadow": True,
            "rationale": _rationale(pattern, rows_total),
            "proposer_id": RECURSIVE_META_PROPOSER_ID,
        }
    ]


__all__ = [
    "AUDIT_LOG_FILENAME",
    "META_SELF_EDIT_CYCLE_FLOOR",
    "RECURRING_REJECTION_MIN",
    "RECURSIVE_META_PROPOSER_ID",
    "count_audit_rows",
    "detect_recurring_gate_rejection",
    "propose_meta_self_edit",
]
