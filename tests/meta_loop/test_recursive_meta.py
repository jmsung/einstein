"""Tests for src/einstein/meta_loop/recursive_meta.py — the meta_self_edit proposer."""

from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein.meta_loop import meta_gate  # noqa: E402
from einstein.meta_loop.proposals import Proposal, ProposalType  # noqa: E402
from einstein.meta_loop.propose import ProposerInput  # noqa: E402
from einstein.meta_loop.recursive_meta import (  # noqa: E402
    META_SELF_EDIT_CYCLE_FLOOR,
    RECURRING_REJECTION_MIN,
    RECURSIVE_META_PROPOSER_ID,
    count_audit_rows,
    detect_recurring_gate_rejection,
    propose_meta_self_edit,
)

UTC = dt.timezone.utc


# ---------------- synthetic ledger helpers ----------------


def _write_audit_log(
    path: Path,
    *,
    rejected_pattern_count: int = 0,
    other_rows: int = 0,
    pattern_type: str = "rule_edit",
    pattern_gate: str = "evidence-threshold",
) -> None:
    """Build a synthetic meta-proposals.md with controlled row counts.

    `rejected_pattern_count` rows are rejected at the same (type, gate) pair;
    `other_rows` rows are accepted with no pattern. Total = sum.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    text = "# meta-proposals audit log\n\n" + meta_gate.AUDIT_LOG_HEADER
    base_ts = dt.datetime(2026, 5, 28, 12, 0, 0, tzinfo=UTC)
    n = 0
    for i in range(rejected_pattern_count):
        ts = (base_ts + dt.timedelta(minutes=n)).strftime("%Y-%m-%dT%H:%M:%SZ")
        text += (
            f"| {ts} | prop-rej-{i:03d} | {pattern_type} | "
            f".claude/rules/some-rule.md | rejected | {pattern_gate} | "
            f"have 2, need 3 | recursive-meta-v0 |\n"
        )
        n += 1
    for i in range(other_rows):
        ts = (base_ts + dt.timedelta(minutes=n)).strftime("%Y-%m-%dT%H:%M:%SZ")
        text += (
            f"| {ts} | prop-acc-{i:03d} | new_question | "
            f"docs/wiki/questions/2026-05-28-q-{i}.md | accepted | — | "
            f"all gates passed | metaharness-llm-v1 |\n"
        )
        n += 1
    path.write_text(text)


def _proposer_input(mb_logs_dir: Path) -> ProposerInput:
    """Build a minimal ProposerInput; only mb_logs_dir is read by the proposer."""
    return ProposerInput(
        report_text="",
        cycle_log_path=mb_logs_dir / "cycle-log.md",
        skill_library_path=mb_logs_dir / "skill-library.md",
        findings_dir=mb_logs_dir / "findings",
        questions_dir=mb_logs_dir / "questions",
        mb_logs_dir=mb_logs_dir,
    )


# ---------------- count_audit_rows ----------------


def test_count_audit_rows_empty(tmp_path: Path) -> None:
    assert count_audit_rows(tmp_path / "no-such-file.md") == 0


def test_count_audit_rows_matches_synthetic_writes(tmp_path: Path) -> None:
    log = tmp_path / "meta-proposals.md"
    _write_audit_log(log, rejected_pattern_count=4, other_rows=6)
    assert count_audit_rows(log) == 10


# ---------------- detect_recurring_gate_rejection ----------------


def test_detect_returns_none_on_empty_log(tmp_path: Path) -> None:
    assert detect_recurring_gate_rejection(tmp_path / "no.md") is None


def test_detect_returns_none_below_min(tmp_path: Path) -> None:
    log = tmp_path / "meta-proposals.md"
    _write_audit_log(log, rejected_pattern_count=RECURRING_REJECTION_MIN - 1, other_rows=10)
    assert detect_recurring_gate_rejection(log) is None


def test_detect_returns_pattern_at_min(tmp_path: Path) -> None:
    log = tmp_path / "meta-proposals.md"
    _write_audit_log(log, rejected_pattern_count=RECURRING_REJECTION_MIN, other_rows=10)
    p = detect_recurring_gate_rejection(log)
    assert p is not None
    assert p["type"] == "rule_edit"
    assert p["gate"] == "evidence-threshold"
    assert p["count"] == RECURRING_REJECTION_MIN


# ---------------- propose_meta_self_edit — floor enforcement ----------------


def test_proposer_refuses_at_floor_minus_one(tmp_path: Path) -> None:
    log = tmp_path / "meta-proposals.md"
    # Build exactly FLOOR-1 = 9 rows (4 rejected pattern, 5 other) — below floor.
    _write_audit_log(
        log,
        rejected_pattern_count=4,
        other_rows=META_SELF_EDIT_CYCLE_FLOOR - 1 - 4,
    )
    assert count_audit_rows(log) == META_SELF_EDIT_CYCLE_FLOOR - 1
    candidates = propose_meta_self_edit(_proposer_input(tmp_path))
    assert candidates == []


def test_proposer_emits_at_floor(tmp_path: Path) -> None:
    log = tmp_path / "meta-proposals.md"
    # FLOOR=10 rows: 4 rejected pattern (above RECURRING_REJECTION_MIN=3), 6 other
    _write_audit_log(log, rejected_pattern_count=4, other_rows=META_SELF_EDIT_CYCLE_FLOOR - 4)
    assert count_audit_rows(log) == META_SELF_EDIT_CYCLE_FLOOR
    candidates = propose_meta_self_edit(_proposer_input(tmp_path))
    assert len(candidates) == 1


def test_proposer_emits_above_floor(tmp_path: Path) -> None:
    log = tmp_path / "meta-proposals.md"
    _write_audit_log(log, rejected_pattern_count=4, other_rows=META_SELF_EDIT_CYCLE_FLOOR - 4 + 1)
    assert count_audit_rows(log) == META_SELF_EDIT_CYCLE_FLOOR + 1
    candidates = propose_meta_self_edit(_proposer_input(tmp_path))
    assert len(candidates) == 1


def test_proposer_returns_empty_when_floor_met_but_no_pattern(tmp_path: Path) -> None:
    log = tmp_path / "meta-proposals.md"
    # 10 rows all accepted — no rejection pattern
    _write_audit_log(log, rejected_pattern_count=0, other_rows=META_SELF_EDIT_CYCLE_FLOOR)
    assert propose_meta_self_edit(_proposer_input(tmp_path)) == []


# ---------------- propose_meta_self_edit — candidate shape ----------------


def test_emitted_candidate_has_correct_provenance(tmp_path: Path) -> None:
    log = tmp_path / "meta-proposals.md"
    _write_audit_log(log, rejected_pattern_count=4, other_rows=META_SELF_EDIT_CYCLE_FLOOR - 4)
    candidates = propose_meta_self_edit(_proposer_input(tmp_path))
    cand = candidates[0]
    assert cand["proposer_id"] == RECURSIVE_META_PROPOSER_ID
    assert cand["type"] == ProposalType.META_SELF_EDIT.value
    assert cand["target_path"] == "scripts/meta_loop.py"
    assert cand["requires_shadow"] is True


def test_emitted_candidate_round_trips_via_coerce(tmp_path: Path) -> None:
    """The candidate dict must satisfy `_coerce_raw` + `Proposal._validate`."""
    log = tmp_path / "meta-proposals.md"
    _write_audit_log(log, rejected_pattern_count=4, other_rows=META_SELF_EDIT_CYCLE_FLOOR - 4)
    candidates = propose_meta_self_edit(_proposer_input(tmp_path))
    cand = candidates[0]
    # Constructing a Proposal directly is the strictest validation path.
    p = Proposal(
        id="recursive-meta-test-001",
        type=cand["type"],
        target_path=cand["target_path"],
        proposed_diff=cand["proposed_diff"],
        evidence_cycles=cand["evidence_cycles"],
        expected_metric_delta=cand["expected_metric_delta"],
        predicted_regressions=cand["predicted_regressions"],
        confidence=cand["confidence"],
        requires_shadow=cand["requires_shadow"],
        rationale=cand["rationale"],
        proposer_id=cand["proposer_id"],
    )
    assert p.proposer_id == RECURSIVE_META_PROPOSER_ID
    assert p.type == ProposalType.META_SELF_EDIT.value


def test_emitted_diff_preserves_shebang(tmp_path: Path) -> None:
    """Regression: the candidate diff must NOT insert lines before the shebang.

    A diff that places content above `#!/usr/bin/env python3` makes
    `./scripts/meta_loop.py` no longer recognized as a Python script by the
    kernel — the executable bit becomes useless. The marker is added AFTER
    the shebang for this reason.
    """
    log = tmp_path / "meta-proposals.md"
    _write_audit_log(log, rejected_pattern_count=4, other_rows=META_SELF_EDIT_CYCLE_FLOOR - 4)
    cand = propose_meta_self_edit(_proposer_input(tmp_path))[0]
    diff = cand["proposed_diff"]
    # Find the body lines after `@@` header
    body = diff.split("@@")[-1].splitlines()
    body = [line for line in body if line.strip()]  # drop blank lines
    # First non-blank body line MUST be the shebang context (' #!/...') not a
    # '+'-prefixed marker line
    assert body[0].startswith(
        " #!/usr/bin/env python3"
    ), f"first hunk body line should be the shebang context, got: {body[0]!r}"
    # Marker line must be a `+` line that appears AFTER the shebang context
    plus_lines = [i for i, line in enumerate(body) if line.startswith("+")]
    shebang_idx = next(i for i, line in enumerate(body) if "#!/usr/bin/env python3" in line)
    assert all(
        i > shebang_idx for i in plus_lines
    ), "marker `+` lines must appear after the shebang context line"


def test_emitted_candidate_evidence_cycles_meets_floor(tmp_path: Path) -> None:
    """The candidate's evidence_cycles count must be ≥ the floor — defense in
    depth so the gate also sees the right count (G3's gate re-checks)."""
    log = tmp_path / "meta-proposals.md"
    _write_audit_log(
        log,
        rejected_pattern_count=4,
        other_rows=META_SELF_EDIT_CYCLE_FLOOR + 5 - 4,
    )
    candidates = propose_meta_self_edit(_proposer_input(tmp_path))
    cand = candidates[0]
    assert len(cand["evidence_cycles"]) >= META_SELF_EDIT_CYCLE_FLOOR


# ---------------- meta_gate audit-log shim still backward-compatible ----------------


def test_parse_audit_log_carries_gate_and_reason(tmp_path: Path) -> None:
    """Verify the meta_gate._parse_audit_log extension this branch added."""
    log = tmp_path / "meta-proposals.md"
    _write_audit_log(log, rejected_pattern_count=2, other_rows=0)
    rows = meta_gate._parse_audit_log(log)
    assert len(rows) == 2
    assert rows[0]["gate"] == "evidence-threshold"
    assert "have 2" in rows[0]["reason"]
