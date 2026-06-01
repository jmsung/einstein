"""Tests for src/einstein/meta_loop/tool_gaps.py — Goal 1 gap-detector."""

from __future__ import annotations

import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein.meta_loop import tool_gaps  # noqa: E402

# ---------------- fixtures ----------------


def _write_cycle_log(path: Path, rows: list[tuple]) -> None:
    header = (
        "# Cycle log — append-only\n\n"
        "## Cycles\n\n"
        "| # | problem | start → end score | hours | compute | wiki cites "
        "| findings+ | concepts+ | author mix | outcome | notes |\n"
        "|---|---|---|---|---|---|---|---|---|---|---|\n"
    )
    body = "".join("| " + " | ".join(r) + " |\n" for r in rows)
    path.write_text(header + body)


def _no_op_row(cid: int, problem: str, notes: str) -> tuple:
    return (
        str(cid),
        problem,
        "0 (no Δ)",
        "0",
        "none-strategy-only",
        "0",
        "0",
        "0",
        "a:1/h:0",
        "strategy-picked-no-execution",
        notes,
    )


def _write_question(path: Path, *, slug: str, tags: list[str], status: str = "open") -> None:
    fm = (
        "---\n"
        "type: question\n"
        "author: agent\n"
        "drafted: 2026-05-30\n"
        f"status: {status}\n"
        f"tags: [{', '.join(tags)}]\n"
        "---\n\n"
        f"# {slug}\n\nbody\n"
    )
    path.write_text(fm)


# ---------------- canonical-form extraction ----------------


def test_extract_signal_dispatch_failed():
    sig = tool_gaps._extract_signal(
        _row(47, "P14-circle-packing-square", "dispatch-failed: optimizer exited with code 1"),
    )
    assert sig is not None
    assert sig.pattern == "dispatch_failed"
    assert sig.problem_id == "P14"


def test_extract_signal_no_manifest_entry():
    sig = tool_gaps._extract_signal(
        _row(45, "P1-erdos-overlap", "dispatch: no-manifest-entry"),
    )
    assert sig is not None
    assert sig.pattern == "no_manifest_entry"
    assert sig.problem_id == "P1"


def test_extract_signal_manifest_only_exposes():
    sig = tool_gaps._extract_signal(
        _row(
            49,
            "P14-circle-packing-square",
            "manifest only exposes newton_max (strict-tol-failing per exp log); "
            "mpmath-ulp-polish picked novel but unwired",
        ),
    )
    assert sig is not None
    assert sig.pattern == "manifest_gap"
    assert sig.problem_id == "P14"
    # Should extract the novel-tool slug
    assert sig.suggested_tool == "mpmath-ulp-polish"


def test_extract_signal_not_yet_wired():
    sig = tool_gaps._extract_signal(
        _row(
            49,
            "P14-circle-packing-square",
            "llm-strategy=mpmath-ulp-polish (novel; not yet wired into P14 manifest)",
        ),
    )
    assert sig is not None
    assert sig.pattern == "manifest_gap"
    assert sig.suggested_tool == "mpmath-ulp-polish"


def test_extract_signal_no_library_matches():
    sig = tool_gaps._extract_signal(
        _row(
            35,
            "P9-uncertainty",
            "category=functional-inequality; (no library matches — council needed)",
        ),
    )
    assert sig is not None
    assert sig.pattern == "no_library_match"
    assert sig.problem_id == "P9"


def test_extract_signal_returns_none_for_clean_row():
    sig = tool_gaps._extract_signal(
        _row(1, "P19", "improved via slsqp polish"),
    )
    assert sig is None


# ---------------- clustering + threshold ----------------


def test_detect_threshold_one_problem_three_cycles_does_not_pass(tmp_path: Path):
    log = tmp_path / "cycle-log.md"
    _write_cycle_log(
        log,
        [
            _no_op_row(
                49,
                "P14",
                "manifest only exposes newton_max; mpmath-ulp-polish picked novel but unwired",
            ),
            _no_op_row(
                50,
                "P14",
                "manifest only exposes newton_max; mpmath-ulp-polish picked novel but unwired",
            ),
            _no_op_row(
                51,
                "P14",
                "manifest only exposes newton_max; mpmath-ulp-polish picked novel but unwired",
            ),
        ],
    )
    gaps = tool_gaps.detect_recurring_tool_gaps(log)
    # 3 cycles but only 1 problem → does not meet ≥2 problems requirement
    assert gaps == []


def test_detect_threshold_two_problems_three_cycles_passes(tmp_path: Path):
    log = tmp_path / "cycle-log.md"
    _write_cycle_log(
        log,
        [
            _no_op_row(45, "P1", "dispatch: no-manifest-entry"),
            _no_op_row(46, "P1", "dispatch: no-manifest-entry"),
            _no_op_row(
                35, "P9", "category=functional-inequality; (no library matches — council needed)"
            ),
        ],
    )
    gaps = tool_gaps.detect_recurring_tool_gaps(log)
    # Now: P1 has 2 cycles "no-manifest-entry", P9 has 1 cycle "no_library_match".
    # Default canonical key clusters by *pattern* (when no specific tool slug)
    # because P1's no-manifest-entry and P9's no-library-match are both
    # "you cannot dispatch because the manifest doesn't expose anything" —
    # they should cluster as one gap with 3 cycles across 2 problems.
    assert len(gaps) == 1
    g = gaps[0]
    assert g.cycle_count == 3
    assert g.problem_count == 2
    assert set(g.problem_ids) == {"P1", "P9"}


def test_detect_with_explicit_tool_slug_does_not_cluster_with_unmatched(tmp_path: Path):
    log = tmp_path / "cycle-log.md"
    _write_cycle_log(
        log,
        [
            # P14: 3 cycles, same tool slug
            _no_op_row(
                49,
                "P14",
                "manifest only exposes newton_max; mpmath-ulp-polish picked novel but unwired",
            ),
            _no_op_row(50, "P14", "mpmath-ulp-polish novel; not yet wired into P14 manifest"),
            # P12: 1 cycle, same tool slug — only 2 problems, total 4 cycles
            _no_op_row(70, "P12", "mpmath-ulp-polish picked novel but unwired"),
            # And an unrelated dispatch_failed gap on P5
            _no_op_row(47, "P5", "dispatch-failed: optimizer exited with code 1"),
        ],
    )
    gaps = tool_gaps.detect_recurring_tool_gaps(log, min_cycles=3, min_problems=2)
    # mpmath-ulp-polish: 3 cycles across P14+P12 → passes
    # dispatch_failed on P5 alone: 1 cycle → does not pass
    assert len(gaps) == 1
    g = gaps[0]
    assert g.suggested_tool == "mpmath-ulp-polish"
    assert g.cycle_count == 3
    assert set(g.problem_ids) == {"P14", "P12"}


def test_detect_orders_by_cycle_count_desc(tmp_path: Path):
    log = tmp_path / "cycle-log.md"
    _write_cycle_log(
        log,
        [
            # Gap A: tool-x on 3 problems, 5 cycles
            _no_op_row(10, "P1", "tool-x picked novel but unwired"),
            _no_op_row(11, "P1", "tool-x picked novel but unwired"),
            _no_op_row(12, "P2", "tool-x picked novel but unwired"),
            _no_op_row(13, "P3", "tool-x picked novel but unwired"),
            _no_op_row(14, "P3", "tool-x picked novel but unwired"),
            # Gap B: tool-y on 2 problems, 3 cycles
            _no_op_row(20, "P4", "tool-y picked novel but unwired"),
            _no_op_row(21, "P4", "tool-y picked novel but unwired"),
            _no_op_row(22, "P5", "tool-y picked novel but unwired"),
        ],
    )
    gaps = tool_gaps.detect_recurring_tool_gaps(log)
    assert len(gaps) == 2
    assert gaps[0].suggested_tool == "tool-x"
    assert gaps[0].cycle_count == 5
    assert gaps[1].suggested_tool == "tool-y"


def test_detect_picks_up_tool_gap_tagged_questions(tmp_path: Path):
    log = tmp_path / "cycle-log.md"
    _write_cycle_log(
        log,
        [
            _no_op_row(
                49,
                "P14",
                "manifest only exposes newton_max; mpmath-ulp-polish picked novel but unwired",
            ),
            _no_op_row(50, "P14", "mpmath-ulp-polish not yet wired into P14 manifest"),
            _no_op_row(70, "P12", "mpmath-ulp-polish picked novel but unwired"),
        ],
    )
    qdir = tmp_path / "questions"
    qdir.mkdir()
    _write_question(
        qdir / "2026-05-24-p14-strict-tol-manifest-wiring.md",
        slug="p14 strict-tol manifest wiring",
        tags=["tool-gap", "manifest"],
    )
    # An unrelated answered question should NOT be picked up
    _write_question(qdir / "2026-04-01-other.md", slug="other", tags=["concept"], status="answered")

    gaps = tool_gaps.detect_recurring_tool_gaps(log, questions_dir=qdir)
    assert len(gaps) == 1
    g = gaps[0]
    # The mpmath-ulp-polish gap should now carry the P14 tool-gap question
    assert any(p.name.endswith("p14-strict-tol-manifest-wiring.md") for p in g.open_questions)


def test_detect_missing_files_returns_empty_list(tmp_path: Path):
    assert tool_gaps.detect_recurring_tool_gaps(tmp_path / "nope.md") == []


def test_meets_threshold_property():
    g = tool_gaps.ToolGap(
        canonical="manifest_gap:mpmath-ulp-polish",
        pattern="manifest_gap",
        suggested_tool="mpmath-ulp-polish",
        missing_manifest_entry=None,
        citing_cycles=[49, 50, 70],
        problem_ids=["P14", "P12"],
        open_questions=[],
    )
    assert g.cycle_count == 3
    assert g.problem_count == 2
    assert g.meets_threshold(min_cycles=3, min_problems=2)
    assert not g.meets_threshold(min_cycles=4, min_problems=2)
    assert not g.meets_threshold(min_cycles=3, min_problems=3)


# ---------------- helpers ----------------


def _row(cid: int, problem: str, notes: str):
    """Build a minimal CycleRow for _extract_signal tests."""
    from einstein.meta_loop.diagnose import CycleRow

    return CycleRow(
        cycle_id=cid,
        problem=problem,
        score_field="0 (no Δ)",
        hours="0",
        compute="none-strategy-only",
        wiki_citations="0",
        findings_added="0",
        concepts_added="0",
        author_mix="a:1/h:0",
        outcome="strategy-picked-no-execution",
        notes=notes,
    )
