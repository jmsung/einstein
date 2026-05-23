"""Tests for docs/tools/monitor.py — autonomous-loop progress dashboard."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "docs" / "tools"))

import monitor  # noqa: E402


# ---------------- cycle-log parsing ----------------


def _write_log(tmp_path: Path, rows: list[str]) -> Path:
    log = tmp_path / "cycle-log.md"
    header = (
        "# Cycle log\n\n## Cycles\n\n"
        "| # | problem | start → end | hours | compute | cites | findings+ | concepts+ | author_mix | outcome | notes |\n"
        "|---|---|---|---|---|---|---|---|---|---|---|\n"
    )
    log.write_text(header + "\n".join(rows) + "\n")
    return log


def test_parse_cycle_log_basic(tmp_path: Path) -> None:
    log = _write_log(tmp_path, [
        "| 0 | bootstrap | n/a | 1 | local-cpu | 0 | 0 | 0 | a:0/h:1/hyb:0 | bootstrap | seed |",
        "| 1 | P19-diff | 2.639 → 2.639 | 1.5 | local-cpu | 8 | 1 | 0 | a:1/h:0/hyb:0 | no-change | notes |",
    ])
    cycles = monitor.parse_cycle_log(log)
    assert len(cycles) == 2
    assert cycles[0].cycle_id == 0
    assert cycles[1].cycle_id == 1
    assert cycles[1].problem == "P19-diff"
    assert cycles[1].findings_added == 1
    assert cycles[1].author_mix == {"agent": 1, "human": 0, "hybrid": 0}
    assert cycles[1].outcome == "no-change"


def test_parse_cycle_log_handles_score_with_arrow(tmp_path: Path) -> None:
    log = _write_log(tmp_path, [
        "| 7 | P9 | 0.5 → 0.4 | 2 | modal | 3 | 0 | 1 | a:1/h:0/hyb:0 | improved | progress |",
    ])
    cycles = monitor.parse_cycle_log(log)
    assert cycles[0].start_score == "0.5"
    assert cycles[0].end_score == "0.4"


def test_parse_skips_non_data_rows(tmp_path: Path) -> None:
    log = tmp_path / "cycle-log.md"
    log.write_text(
        "# Cycle log\n\n"
        "## Cycles\n\n"
        "| # | problem | other |\n"   # header — skipped (not all-digit first col)
        "|---|---|---|\n"             # separator — skipped
        "| 0 | bootstrap | n/a | 1 | local-cpu | 0 | 0 | 0 | a:0/h:1/hyb:0 | bootstrap | seed |\n"
        "Some prose paragraph\n"
    )
    cycles = monitor.parse_cycle_log(log)
    assert [c.cycle_id for c in cycles] == [0]


# ---------------- summary ----------------


def test_summarize_cumulative_totals(tmp_path: Path) -> None:
    log = _write_log(tmp_path, [
        "| 0 | bootstrap | n/a | 1 | local-cpu | 0 | 0 | 0 | a:0/h:1/hyb:0 | bootstrap | seed |",
        "| 1 | P19 | 2.639 → 2.639 | 1.5 | local-cpu | 8 | 1 | 0 | a:1/h:0/hyb:0 | no-change | x |",
        "| 2 | P19 | 2.639 → 2.639 | 1.0 | local-cpu | 5 | 2 | 0 | a:1/h:0/hyb:1 | no-change | y |",
        "| 3 | P5 | 0.5 → 0.4 | 2 | modal | 3 | 0 | 1 | a:1/h:0/hyb:0 | improved | z |",
    ])
    summary = monitor.summarize(monitor.parse_cycle_log(log))
    assert summary.total_cycles == 4
    assert summary.findings_added_total == 3
    assert summary.concepts_added_total == 1
    assert summary.outcome_counts["no-change"] == 2
    assert summary.outcome_counts["improved"] == 1
    assert summary.author_mix_totals == {"agent": 3, "human": 1, "hybrid": 1}
    # problems_touched: unique problem strings
    assert set(summary.problems_touched) == {"bootstrap", "P19", "P5"}


def test_summarize_recent_cycles_window(tmp_path: Path) -> None:
    log = _write_log(tmp_path, [
        f"| {i} | P{i % 3} | n/a | 1 | cpu | 0 | 0 | 0 | a:1/h:0/hyb:0 | no-change | x |"
        for i in range(10)
    ])
    cycles = monitor.parse_cycle_log(log)
    summary = monitor.summarize(cycles, recent_n=3)
    assert summary.total_cycles == 10
    assert len(summary.recent) == 3
    assert [c.cycle_id for c in summary.recent] == [7, 8, 9]


def test_summarize_empty_log(tmp_path: Path) -> None:
    log = _write_log(tmp_path, [])
    summary = monitor.summarize(monitor.parse_cycle_log(log))
    assert summary.total_cycles == 0
    assert summary.findings_added_total == 0
    assert summary.recent == []
    assert summary.outcome_counts == {}


# ---------------- render ----------------


def test_render_summary_contains_section_headers(tmp_path: Path) -> None:
    log = _write_log(tmp_path, [
        "| 0 | bootstrap | n/a | 1 | cpu | 0 | 0 | 0 | a:0/h:1/hyb:0 | bootstrap | seed |",
        "| 1 | P19 | 2.6 → 2.6 | 1 | cpu | 5 | 1 | 0 | a:1/h:0/hyb:0 | no-change | x |",
    ])
    summary = monitor.summarize(monitor.parse_cycle_log(log), recent_n=5)
    out = monitor.render(summary)
    assert "Totals" in out
    assert "Outcomes" in out
    assert "Recent" in out
    # Cumulative numbers appear
    assert "2" in out  # total_cycles=2
