"""Tests for docs/tools/strategy_picker.py — autoresearch 1+1 rule."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "docs" / "tools"))

import strategy_picker as sp  # noqa: E402


# ---------------- problem → category ----------------


def test_problem_category_from_id() -> None:
    assert sp.category_for(2) == "autocorrelation"
    assert sp.category_for(3) == "autocorrelation"
    assert sp.category_for(4) == "autocorrelation"
    assert sp.category_for(6) == "sphere-packing"
    assert sp.category_for(22) == "sphere-packing"
    assert sp.category_for(11) == "sphere-packing"
    assert sp.category_for(14) == "packing"
    assert sp.category_for(12) == "discrete-combinatorics"
    assert sp.category_for(19) == "discrete-combinatorics"
    assert sp.category_for(9) == "functional-inequality"
    assert sp.category_for(13) == "extremal-graph"
    assert sp.category_for(16) == "extremal-graph"


def test_unknown_problem_returns_question_mark() -> None:
    assert sp.category_for(999) == "?"


# ---------------- skill-library parsing ----------------


def _write_library(tmp_path: Path, rows: list[dict]) -> Path:
    path = tmp_path / "skill-library.md"
    lines = [
        "# Skill library",
        "",
        "## Bootstrap entries",
        "",
        "| technique | category | tried | top3 | finding | last_used | hit_rate |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        lines.append(
            f"| `{r['technique']}` | {r['category']} | {r['tried']} | "
            f"{r['top3']} | {r['finding']} | {r.get('last_used', '2026-01-01')} | "
            f"{r['hit_rate']} |"
        )
    path.write_text("\n".join(lines) + "\n")
    return path


def test_parse_skill_library_basic(tmp_path: Path) -> None:
    lib = _write_library(tmp_path, [
        {"technique": "basin-hopping-multistart.md", "category": "packing",
         "tried": 4, "top3": 2, "finding": 2, "hit_rate": 0.5},
        {"technique": "mpmath-ulp-polish.md", "category": "float64-ceiling",
         "tried": 8, "top3": 5, "finding": 3, "hit_rate": 0.62},
    ])
    rows = sp.load_skill_library(lib)
    assert len(rows) == 2
    assert rows[0].technique == "basin-hopping-multistart.md"
    assert rows[0].tried == 4
    assert rows[0].top3 == 2
    assert rows[0].hit_rate == pytest.approx(0.5)


def test_parse_skill_library_skips_malformed_rows(tmp_path: Path) -> None:
    lib = tmp_path / "lib.md"
    lib.write_text(
        "## Entries\n\n"
        "| technique | category | tried | top3 | finding | last_used | hit_rate |\n"
        "|---|---|---|---|---|---|---|\n"
        "| `valid.md` | packing | 4 | 2 | 1 | 2026-01-01 | 0.5 |\n"
        "| invalid no backticks | packing | 4 | 2 | 1 | 2026-01-01 | 0.5 |\n"
        "| `another.md` | packing | not-a-number | 0 | 0 | 2026-01-01 | 0 |\n"
        "| `valid2.md` | kissing | 1 | 1 | 0 | 2026-01-01 | 1.0 |\n"
    )
    rows = sp.load_skill_library(lib)
    techs = {r.technique for r in rows}
    assert techs == {"valid.md", "valid2.md"}


# ---------------- 1+1 strategy pick ----------------


def test_pick_strategy_returns_prior_and_novel(tmp_path: Path) -> None:
    lib = _write_library(tmp_path, [
        # Prior candidate — highest hit_rate in category
        {"technique": "slsqp-active-pair-polish.md", "category": "packing",
         "tried": 6, "top3": 4, "finding": 1, "hit_rate": 0.67},
        # Novel candidate — produces findings even if no top-3
        {"technique": "kronecker-search-decomposition.md", "category": "packing",
         "tried": 2, "top3": 0, "finding": 2, "hit_rate": 0.0},
        # Wrong category (should not be chosen)
        {"technique": "larger-n-cascade.md", "category": "autocorrelation",
         "tried": 4, "top3": 4, "finding": 2, "hit_rate": 1.0},
    ])
    pick = sp.pick_strategy(lib, category="packing")
    assert pick.prior is not None
    assert pick.prior.technique == "slsqp-active-pair-polish.md"
    assert pick.novel is not None
    assert pick.novel.technique == "kronecker-search-decomposition.md"
    assert pick.prior.technique != pick.novel.technique


def test_pick_strategy_handles_single_technique(tmp_path: Path) -> None:
    """One technique in the category → it becomes prior; novel is None."""
    lib = _write_library(tmp_path, [
        {"technique": "lonely.md", "category": "packing",
         "tried": 1, "top3": 1, "finding": 0, "hit_rate": 1.0},
    ])
    pick = sp.pick_strategy(lib, category="packing")
    assert pick.prior is not None
    assert pick.prior.technique == "lonely.md"
    assert pick.novel is None


def test_pick_strategy_no_techniques_in_category(tmp_path: Path) -> None:
    lib = _write_library(tmp_path, [
        {"technique": "off-topic.md", "category": "autocorrelation",
         "tried": 1, "top3": 0, "finding": 0, "hit_rate": 0},
    ])
    pick = sp.pick_strategy(lib, category="packing")
    assert pick.prior is None
    assert pick.novel is None
    assert "no techniques" in pick.rationale.lower()


def test_pick_strategy_category_fuzzy_match(tmp_path: Path) -> None:
    """Library has 'packing / kissing' and we ask for 'sphere-packing' — should match."""
    lib = _write_library(tmp_path, [
        {"technique": "slsqp-active-pair-polish.md", "category": "packing / kissing",
         "tried": 6, "top3": 4, "finding": 1, "hit_rate": 0.67},
    ])
    pick = sp.pick_strategy(lib, category="sphere-packing")
    assert pick.prior is not None  # fuzzy on 'packing' substring
    assert pick.prior.technique == "slsqp-active-pair-polish.md"


# ---------------- convergence_detect ----------------


def test_convergence_detect_continue_when_score_improved() -> None:
    decision = sp.convergence_detect(
        score_history=[2.0, 1.9],
        new_gap_counts=[0, 0],
    )
    assert decision.action == "continue"


def test_convergence_detect_stop_when_no_progress_and_no_gap() -> None:
    decision = sp.convergence_detect(
        score_history=[2.0, 2.0],
        new_gap_counts=[0, 0],
    )
    assert decision.action == "stop"
    assert "no progress" in decision.reason.lower() or "no gap" in decision.reason.lower()


def test_convergence_detect_continue_when_no_progress_but_new_gap() -> None:
    decision = sp.convergence_detect(
        score_history=[2.0, 2.0],
        new_gap_counts=[0, 1],
    )
    assert decision.action == "continue"


def test_convergence_detect_continue_on_first_attempt() -> None:
    decision = sp.convergence_detect(
        score_history=[2.0],
        new_gap_counts=[0],
    )
    assert decision.action == "continue"


def test_convergence_detect_stop_at_attempt_budget() -> None:
    decision = sp.convergence_detect(
        score_history=[2.0, 2.0, 2.0],
        new_gap_counts=[0, 0, 0],
        max_attempts=3,
    )
    assert decision.action == "stop"
    assert "budget" in decision.reason.lower() or "max" in decision.reason.lower() or "attempts" in decision.reason.lower()
