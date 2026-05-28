"""Tests for src/einstein/parallel/shadow_ab.py — Goal 5 of js/feat/parallel-attempts.

Mirrors tests/bandit/test_shadow_ab.py in shape: pure verdict logic +
append_run formatting + injectable arm_runner.
"""

from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein.meta_loop import diagnose  # noqa: E402
from einstein.parallel.shadow_ab import (  # noqa: E402
    Verdict,
    append_run,
    decide,
    run_shadow_ab,
)

UTC = dt.timezone.utc


def _row(
    cycle_id: int,
    problem: str = "P14",
    *,
    score_changed: bool = False,
    findings: int = 0,
    notes: str = "",
) -> diagnose.CycleRow:
    score_field = "2.6 → 2.5" if score_changed else "2.6 (no Δ)"
    return diagnose.CycleRow(
        cycle_id=cycle_id,
        problem=problem,
        score_field=score_field,
        hours="0.1",
        compute="local-cpu",
        wiki_citations="0",
        findings_added=str(findings),
        concepts_added="0",
        author_mix="a:1/h:0/hyb:0",
        outcome="improved-local" if score_changed else "no-change",
        notes=notes,
    )


# ---------------- decide ----------------


def test_decide_promote_when_improvements_strictly_higher():
    """Arm A wins on improvements/cycle → promote regardless of findings."""
    a = [_row(1, score_changed=True), _row(2, score_changed=True)]
    b = [_row(1, score_changed=False), _row(2, score_changed=False)]
    v = decide(a, b)
    assert v.promote is True
    assert v.a_improvements_per_cycle > v.b_improvements_per_cycle


def test_decide_promote_when_findings_strictly_higher_non_worse_improvements():
    """Arm A ties on improvements, wins on findings → promote."""
    a = [_row(1, score_changed=False, findings=2), _row(2, score_changed=True, findings=1)]
    b = [_row(1, score_changed=False, findings=0), _row(2, score_changed=True, findings=0)]
    v = decide(a, b)
    assert v.a_findings_per_cycle > v.b_findings_per_cycle
    assert v.a_improvements_per_cycle >= v.b_improvements_per_cycle
    assert v.promote is True


def test_decide_no_promote_when_findings_higher_but_improvements_worse():
    """Arm A wins findings but loses improvements → no promote."""
    a = [_row(1, score_changed=False, findings=3), _row(2, score_changed=False, findings=3)]
    b = [_row(1, score_changed=True, findings=0), _row(2, score_changed=True, findings=0)]
    v = decide(a, b)
    assert v.a_findings_per_cycle > v.b_findings_per_cycle
    assert v.a_improvements_per_cycle < v.b_improvements_per_cycle
    assert v.promote is False


def test_decide_no_promote_when_both_equal():
    a = [_row(1, score_changed=True, findings=1), _row(2, score_changed=False, findings=0)]
    b = [_row(1, score_changed=True, findings=1), _row(2, score_changed=False, findings=0)]
    v = decide(a, b)
    assert v.promote is False


def test_decide_no_promote_when_b_strictly_better():
    a = [_row(1, score_changed=False, findings=0), _row(2, score_changed=False, findings=0)]
    b = [_row(1, score_changed=True, findings=2), _row(2, score_changed=True, findings=2)]
    v = decide(a, b)
    assert v.promote is False


# ---------------- append_run ----------------


def test_append_run_creates_file_with_header(tmp_path: Path):
    path = tmp_path / "logs" / "meta-shadow-runs.md"
    v = Verdict(
        promote=False,
        reason="test",
        a_improvements_per_cycle=0.1,
        b_improvements_per_cycle=0.1,
        a_findings_per_cycle=0.0,
        b_findings_per_cycle=0.0,
        a_cycles=10,
        b_cycles=10,
    )
    append_run(
        path,
        timestamp=dt.datetime(2026, 5, 28, 4, 0, 0, tzinfo=UTC),
        mode="wiring-validation",
        n_cycles=10,
        problems=[9, 14, 17, 22],
        verdict=v,
    )
    text = path.read_text()
    assert "## parallel-K (K=4) vs single-attempt" in text
    assert "2026-05-28T04:00:00Z" in text
    assert "wiring-validation" in text
    assert "P9,P14,P17,P22" in text


def test_append_run_keeps_existing_bandit_section(tmp_path: Path):
    """If the file already has the bandit section, append the parallel section
    without clobbering."""
    path = tmp_path / "meta-shadow-runs.md"
    existing = (
        "# meta-shadow runs — skill-bandit (A) vs manifest dispatcher (B)\n\n"
        "| ts | mode | n | etc |\n|---|---|---|---|\n"
        "| 2026-05-28T03:58:03Z | live | 10 | yes |\n"
    )
    path.write_text(existing)
    v = Verdict(
        promote=True,
        reason="r",
        a_improvements_per_cycle=0.3,
        b_improvements_per_cycle=0.1,
        a_findings_per_cycle=0.0,
        b_findings_per_cycle=0.0,
        a_cycles=10,
        b_cycles=10,
    )
    append_run(
        path,
        timestamp=dt.datetime(2026, 5, 28, 5, 0, 0, tzinfo=UTC),
        mode="live",
        n_cycles=10,
        problems=[14],
        verdict=v,
    )
    text = path.read_text()
    assert "2026-05-28T03:58:03Z" in text  # original row intact
    assert "2026-05-28T05:00:00Z" in text  # new row appended
    assert "## parallel-K (K=4) vs single-attempt" in text


def test_append_run_does_not_redeclare_parallel_section(tmp_path: Path):
    """Second call adds a row, not another section header."""
    path = tmp_path / "log.md"
    v = Verdict(
        promote=False,
        reason="r",
        a_improvements_per_cycle=0.1,
        b_improvements_per_cycle=0.1,
        a_findings_per_cycle=0.0,
        b_findings_per_cycle=0.0,
        a_cycles=10,
        b_cycles=10,
    )
    for i in range(2):
        append_run(
            path,
            timestamp=dt.datetime(2026, 5, 28, i + 1, 0, 0, tzinfo=UTC),
            mode="wiring-validation",
            n_cycles=5,
            problems=[14],
            verdict=v,
        )
    text = path.read_text()
    assert text.count("## parallel-K (K=4) vs single-attempt") == 1


# ---------------- orchestration ----------------


def test_run_shadow_ab_injects_runner_and_logs_verdict(tmp_path: Path):
    """End-to-end: stubbed arm_runner writes synthetic cycle-logs;
    run_shadow_ab decides + logs."""
    arm_a_log = tmp_path / "arm-a.md"
    arm_b_log = tmp_path / "arm-b.md"
    shadow_log = tmp_path / "meta-shadow-runs.md"

    # Write a cycle-log header matching format_cycle_log_row output.
    HEADER = (
        "# Cycle log\n\n"
        "| cycle | problem | score | hours | compute | wiki_citations "
        "| findings | concepts | author_mix | outcome | notes | cites_src |\n"
        "|---|---|---|---|---|---|---|---|---|---|---|---|\n"
    )
    arm_a_rows = (
        "| 1 | P14 | 2.6 → 2.5 | 0.1 | local-cpu | 0 | 1 | 0 "
        "| a:1/h:0/hyb:0 | improved-local | A1 | 0 |\n"
        "| 2 | P17 | 2.6 → 2.4 | 0.1 | local-cpu | 0 | 0 | 0 "
        "| a:1/h:0/hyb:0 | improved-local | A2 | 0 |\n"
    )
    arm_b_rows = (
        "| 1 | P14 | 2.6 (no Δ) | 0.1 | local-cpu | 0 | 0 | 0 "
        "| a:1/h:0/hyb:0 | no-change | B1 | 0 |\n"
        "| 2 | P17 | 2.6 (no Δ) | 0.1 | local-cpu | 0 | 0 | 0 "
        "| a:1/h:0/hyb:0 | no-change | B2 | 0 |\n"
    )

    def stub_runner(arm: str, k: int, problems: list[int], n_cycles: int, log: Path) -> None:
        log.write_text(HEADER + (arm_a_rows if arm == "A" else arm_b_rows))

    result = run_shadow_ab(
        problems=[14, 17],
        n_cycles=2,
        arm_a_log=arm_a_log,
        arm_b_log=arm_b_log,
        arm_runner=stub_runner,
        shadow_log=shadow_log,
        mode="wiring-validation",
        now=dt.datetime(2026, 5, 28, 6, 0, 0, tzinfo=UTC),
    )
    # Arm A always improved; Arm B never did → promote
    assert result.verdict.promote is True
    assert result.verdict.a_improvements_per_cycle == 1.0
    assert result.verdict.b_improvements_per_cycle == 0.0
    # Log row was appended
    assert "2026-05-28T06:00:00Z" in shadow_log.read_text()
    assert "wiring-validation" in shadow_log.read_text()
