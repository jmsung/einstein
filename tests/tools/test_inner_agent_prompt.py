"""Tests for docs/tools/inner_agent_prompt.py (Goal 7.1)."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "docs" / "tools"))

import inner_agent_prompt as iap  # noqa: E402

# ---------------- CycleRow.parse ----------------


def test_cycle_row_parse_real_row():
    line = (
        "| 42 | P18-circles-rectangle | 2.365832385208 (no Δ) | 0 | "
        "none-strategy-only | 0 | 0 | 0 | a:1/h:0/hyb:0 | "
        "strategy-picked-no-execution | autonomous_loop inner_attempt — "
        "category=packing |"
    )
    row = iap.CycleRow.parse(line)
    assert row is not None
    assert row.cycle_id == 42
    assert row.problem == "P18-circles-rectangle"
    assert row.outcome == "strategy-picked-no-execution"
    assert "category=packing" in row.notes


def test_cycle_row_parse_skips_header_and_separator():
    assert iap.CycleRow.parse("| # | problem | start → end score | ... |") is None
    assert iap.CycleRow.parse("|---|---|---|") is None
    assert iap.CycleRow.parse("not a row") is None
    assert iap.CycleRow.parse("") is None


def test_cycle_row_parse_score_pair_arrow():
    line = (
        "| 5 | P14-circle-packing-square | 2.640 → 2.636 | 1.5 | local-cpu | "
        "3 | 0 | 0 | a:1/h:0/hyb:0 | improved | basin-hopping yielded a "
        "small improvement |"
    )
    row = iap.CycleRow.parse(line)
    assert row is not None
    assert row.score_pair == "2.640 → 2.636"
    assert row.outcome == "improved"


# ---------------- _strip_frontmatter + _tail + _read_safe ----------------


def test_strip_frontmatter_present():
    text = "---\nfoo: 1\nbar: 2\n---\nbody\nhere\n"
    assert iap._strip_frontmatter(text) == "body\nhere\n"


def test_strip_frontmatter_absent():
    text = "no frontmatter\nbody\n"
    assert iap._strip_frontmatter(text) == text


def test_tail_no_truncation():
    s = "a\nb\nc"
    assert iap._tail(s, 10) == s


def test_tail_truncates():
    s = "\n".join(str(i) for i in range(20))
    out = iap._tail(s, 5)
    assert out.startswith("15\n16\n17\n18\n19")
    assert "truncated to last 5 of 20" in out


def test_read_safe_missing_returns_default(tmp_path):
    assert iap._read_safe(tmp_path / "nope.md", default="X") == "X"


def test_read_safe_present(tmp_path):
    p = tmp_path / "a.md"
    p.write_text("hello")
    assert iap._read_safe(p) == "hello"


# ---------------- _cycle_rows_for ----------------


def test_cycle_rows_for_filters_and_tails(tmp_path):
    cycle_log = tmp_path / "cycle-log.md"
    cycle_log.write_text(
        """
header garbage
| 1 | P14-circle-packing-square | a | b | c | d | e | f | g | imp | n1 |
| 2 | P18-circles-rectangle    | a | b | c | d | e | f | g | imp | n2 |
| 3 | P14-circle-packing-square | a | b | c | d | e | f | g | imp | n3 |
| 4 | P14-circle-packing-square | a | b | c | d | e | f | g | imp | n4 |
""".lstrip()
    )
    rows = iap._cycle_rows_for(cycle_log, "P14-circle-packing-square", n=2)
    assert [r.cycle_id for r in rows] == [3, 4]


def test_cycle_rows_for_missing_log_returns_empty(tmp_path):
    rows = iap._cycle_rows_for(tmp_path / "nope.md", "P1-foo", n=5)
    assert rows == []


# ---------------- render_prompt ----------------


@pytest.fixture
def fake_layout(tmp_path):
    """A minimal repo-shaped tree for render_prompt to read from."""
    problems_dir = tmp_path / "knowledge" / "wiki" / "problems"
    problems_dir.mkdir(parents=True)
    (problems_dir / "14-circle-packing-square.md").write_text(
        "---\n"
        "type: problem\n"
        "problem_id: 14\n"
        "status: rank-2-frozen\n"
        "score_current: 2.6359830849175\n"
        "---\n"
        "# Problem 14\n\n"
        "Pack k unit circles in the unit square; minimize the longest edge\n"
        "of the contact graph. Arena score = ... \n"
    )

    cycle_log = tmp_path / "docs" / "agent" / "cycle-log.md"
    cycle_log.parent.mkdir(parents=True)
    cycle_log.write_text(
        "| 10 | P14-circle-packing-square | 2.640 → 2.636 | 1.0 | local-cpu | "
        "1 | 0 | 0 | a:1/h:0/hyb:0 | improved | basin-hop |\n"
        "| 11 | P14-circle-packing-square | 2.636 (no Δ) | 0.3 | local-cpu | "
        "0 | 0 | 0 | a:1/h:0/hyb:0 | no-change | nelder-mead |\n"
    )

    skill_library = tmp_path / "docs" / "agent" / "skill-library.md"
    skill_library.write_text("(library content)\n")

    experiment_dir = tmp_path / "mb" / "problems"
    (experiment_dir / "14-circle-packing-square").mkdir(parents=True)
    (experiment_dir / "14-circle-packing-square" / "experiment-log.md").write_text(
        "2026-05-01: tried multistart, no improvement\n"
        "2026-05-02: tried CMA-ES with rotation lottery, +0.001 on best\n"
    )

    return {
        "problems_dir": problems_dir,
        "cycle_log": cycle_log,
        "skill_library": skill_library,
        "experiment_log_dir": experiment_dir,
    }


def test_render_prompt_includes_core_sections(fake_layout):
    prompt = iap.render_prompt(
        problem_id=14,
        problem_slug="circle-packing-square",
        file_slug="14-circle-packing-square",
        score_current=2.6359830849175,
        status="rank-2-frozen",
        tier="A",
        category="packing",
        cycle_id=99,
        attempt_index=1,
        **fake_layout,
    )
    assert "P14-circle-packing-square" in prompt
    assert "Attempt 1/3" in prompt
    assert "cycle_id=99" in prompt
    assert "category=packing" in prompt
    assert "WIKI-FIRST" in prompt
    assert "Pack k unit circles" in prompt  # problem body
    assert "2.6359830849175" in prompt  # score_current
    assert "rank-2-frozen" in prompt  # status
    assert "cycle 10:" in prompt and "cycle 11:" in prompt  # prior cycles
    assert "this is attempt 1 of the visit" in prompt
    assert "(library content)" in prompt
    assert "tried CMA-ES with rotation lottery" in prompt
    assert "qmd query" in prompt  # tool allowlist
    assert "optimizer_dispatch" in prompt
    assert "Required output" in prompt
    assert '"strategy"' in prompt  # schema appears verbatim


def test_render_prompt_attempt_2_includes_visit_history(fake_layout):
    prompt = iap.render_prompt(
        problem_id=14,
        problem_slug="circle-packing-square",
        file_slug="14-circle-packing-square",
        score_current=2.6359830849175,
        status="rank-2-frozen",
        tier="A",
        category="packing",
        cycle_id=100,
        attempt_index=2,
        prior_visit_summaries=[
            "tried basin-hopping; no improvement; council surfaced rotation-lottery question"
        ],
        **fake_layout,
    )
    assert "Attempt 2/3" in prompt
    assert "attempt 1: tried basin-hopping" in prompt
    assert "this is attempt 1 of the visit" not in prompt
    # Attempt-aware guidance: 1+1 rule + "avoid repeating" — phrasing spans
    # a line break in the prompt body so check the canonical pieces.
    assert "autoresearch 1+1 rule" in prompt
    assert "avoid repeating" in prompt


def test_render_prompt_no_prior_cycles_for_unseen_problem(fake_layout):
    prompt = iap.render_prompt(
        problem_id=99,
        problem_slug="never-tried",
        file_slug="99-never-tried",
        score_current=None,
        status="open",
        tier="?",
        category="?",
        cycle_id=999,
        attempt_index=1,
        **fake_layout,
    )
    assert "(no prior cycles on this problem)" in prompt
    assert "score_current: none" in prompt
    assert "(problem statement not found)" in prompt


def test_render_prompt_missing_experiment_log_renders_safely(fake_layout, tmp_path):
    # Point at a fresh dir with no per-problem subdirs.
    empty_exp_dir = tmp_path / "no-mb"
    empty_exp_dir.mkdir()
    layout = dict(fake_layout)
    layout["experiment_log_dir"] = empty_exp_dir
    prompt = iap.render_prompt(
        problem_id=14,
        problem_slug="circle-packing-square",
        file_slug="14-circle-packing-square",
        score_current=2.636,
        status="rank-2-frozen",
        tier="A",
        category="packing",
        cycle_id=99,
        attempt_index=1,
        **layout,
    )
    assert "(no experiment log yet)" in prompt


def test_render_prompt_truncates_long_skill_library(fake_layout):
    long_skill = "\n".join(f"row {i}" for i in range(500))
    fake_layout["skill_library"].write_text(long_skill)
    prompt = iap.render_prompt(
        problem_id=14,
        problem_slug="circle-packing-square",
        file_slug="14-circle-packing-square",
        score_current=2.636,
        status="rank-2-frozen",
        tier="A",
        category="packing",
        cycle_id=99,
        attempt_index=1,
        skill_library_tail_lines=20,
        **fake_layout,
    )
    assert "row 499" in prompt  # last line preserved
    assert "row 100" not in prompt  # earlier lines dropped
    assert "truncated to last 20 of 500" in prompt


# Goal 8 of js/feat/research-synthesis: pre_cycle_synthesis kwarg


def test_render_prompt_omits_synthesis_section_when_none(fake_layout):
    """Default behaviour: no synthesis content → no ## Pre-cycle synthesis section."""
    prompt = iap.render_prompt(
        problem_id=14,
        problem_slug="circle-packing-square",
        file_slug="14-circle-packing-square",
        score_current=2.636,
        status="rank-2-frozen",
        tier="A",
        category="packing",
        cycle_id=99,
        attempt_index=1,
        **fake_layout,
    )
    assert "## Pre-cycle synthesis (auto-generated)" not in prompt
    # No mysterious empty section either
    assert "auto-generated" not in prompt


def test_render_prompt_omits_synthesis_when_empty_string(fake_layout):
    """Empty / whitespace-only synthesis → still no section."""
    prompt = iap.render_prompt(
        problem_id=14,
        problem_slug="circle-packing-square",
        file_slug="14-circle-packing-square",
        score_current=2.636,
        status="rank-2-frozen",
        tier="A",
        category="packing",
        cycle_id=99,
        attempt_index=1,
        pre_cycle_synthesis="   \n  \n",
        **fake_layout,
    )
    assert "## Pre-cycle synthesis (auto-generated)" not in prompt


def test_render_prompt_includes_synthesis_section_when_provided(fake_layout):
    """When orchestrator provides synthesis, it lands BEFORE ## Your task."""
    body = (
        "# Literature synthesis: P14 — circle-packing-square\n\n"
        "## Top sources\n- 88% knowledge/source/2016-cohn-some-properties.md — magic function\n\n"
        "## Cross-source patterns\n### Pattern: peak-locking transfer\n"
    )
    prompt = iap.render_prompt(
        problem_id=14,
        problem_slug="circle-packing-square",
        file_slug="14-circle-packing-square",
        score_current=2.636,
        status="rank-2-frozen",
        tier="A",
        category="packing",
        cycle_id=99,
        attempt_index=1,
        pre_cycle_synthesis=body,
        **fake_layout,
    )
    assert "## Pre-cycle synthesis (auto-generated)" in prompt
    # Synthesis body inlined verbatim
    assert "2016-cohn-some-properties.md" in prompt
    assert "Pattern: peak-locking transfer" in prompt
    # Must appear BEFORE ## Your task
    assert prompt.index("## Pre-cycle synthesis") < prompt.index("## Your task")
    # The instruction nudges the agent to use cited_sources
    assert "cited_sources" in prompt


# ---------------- G2 extension: bandit recommendation hint ----------------


def test_bandit_recommendation_renders_section(fake_layout):
    prompt = iap.render_prompt(
        problem_id=14,
        problem_slug="circle-packing-square",
        file_slug="14-circle-packing-square",
        score_current=2.6,
        status="rank-2-frozen",
        tier="A",
        category="packing",
        cycle_id=1,
        attempt_index=1,
        bandit_recommendation="technique=slsqp.md prior=Beta(5,3) sampled_θ=0.71",
        **fake_layout,
    )
    assert "Bandit recommendation" in prompt
    assert "technique=slsqp.md" in prompt
    assert "prior=Beta(5,3)" in prompt
    assert "sampled_θ=0.71" in prompt
    assert "strong prior" in prompt  # framing


def test_no_bandit_recommendation_omits_section(fake_layout):
    prompt = iap.render_prompt(
        problem_id=14,
        problem_slug="circle-packing-square",
        file_slug="14-circle-packing-square",
        score_current=2.6,
        status="rank-2-frozen",
        tier="A",
        category="packing",
        cycle_id=1,
        attempt_index=1,
        **fake_layout,
    )
    assert "Bandit recommendation" not in prompt
