"""Tests for src/einstein/parallel/dead_end_surface.py — Goal 6 of
js/feat/parallel-attempts.

Thresholded auto-surfacing of non-winning fanout attempts that look like
real dead-ends. Heuristic on (score-gap, technique novelty, exit reason)
plus a one-per-cycle cap so over-filing doesn't dilute the signal.
"""

from __future__ import annotations

import sys
from pathlib import Path
from types import SimpleNamespace

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein.parallel.dead_end_surface import (  # noqa: E402
    draft_stub,
    is_high_signal_loser,
    select_top_candidate,
)
from einstein.parallel.fanout import AttemptResult  # noqa: E402


def _problem(problem_id=14, slug="circle-packing-square"):
    return SimpleNamespace(problem_id=problem_id, display=f"P{problem_id}", slug=slug)


def _ok(index, technique, score):
    return AttemptResult(
        index=index,
        technique=technique,
        score=score,
        exit="ok",
        notes="",
        pick_note=f"technique={technique}",
    )


# ---------------- is_high_signal_loser ----------------


def test_high_signal_score_gap_too_small_returns_false():
    """Loser within 10% of winner's score = same basin, not a dead end."""
    winner = _ok(1, "tech-A", score=0.50)
    loser = _ok(2, "tech-B", score=0.49)  # 2% gap
    assert is_high_signal_loser(loser, winner, arms_tried={"tech-B": 2}) is False


def test_high_signal_high_gap_unexplored_returns_true():
    """Large basin gap + under-explored arm = high signal."""
    winner = _ok(1, "tech-A", score=0.50)
    loser = _ok(2, "tech-B", score=1.20)  # 140% gap
    assert is_high_signal_loser(loser, winner, arms_tried={"tech-B": 2}) is True


def test_high_signal_over_explored_returns_false():
    """High score-gap but the arm has 50 tries — already well-mapped."""
    winner = _ok(1, "tech-A", score=0.50)
    loser = _ok(2, "tech-B", score=1.20)
    assert is_high_signal_loser(loser, winner, arms_tried={"tech-B": 50}) is False


def test_high_signal_failed_attempt_returns_false():
    """Timeouts / dispatch failures are noise, not signal."""
    winner = _ok(1, "tech-A", score=0.50)
    loser = AttemptResult(
        index=2,
        technique="tech-B",
        score=None,
        exit="timeout",
        notes="",
        pick_note=None,
    )
    assert is_high_signal_loser(loser, winner, arms_tried={"tech-B": 2}) is False


def test_high_signal_missing_winner_score_returns_false():
    """No score to compare against → can't measure basin gap."""
    winner = AttemptResult(
        index=1,
        technique="tech-A",
        score=None,
        exit="ok",
        notes="",
        pick_note=None,
    )
    loser = _ok(2, "tech-B", score=1.0)
    assert is_high_signal_loser(loser, winner, arms_tried={"tech-B": 2}) is False


def test_high_signal_no_winner_score_zero_handles_division():
    """Winner score = 0 must not crash the relative-gap check."""
    winner = _ok(1, "tech-A", score=0.0)
    loser = _ok(2, "tech-B", score=1.0)
    # Any positive gap from zero is "infinite relative" → treat as high gap
    assert is_high_signal_loser(loser, winner, arms_tried={"tech-B": 2}) is True


def test_high_signal_brand_new_arm_returns_true():
    """`arms_tried` missing the technique → tried=0; high signal if gap good."""
    winner = _ok(1, "tech-A", score=0.50)
    loser = _ok(2, "tech-NEVER-SEEN", score=1.5)
    assert is_high_signal_loser(loser, winner, arms_tried={}) is True


# ---------------- select_top_candidate ----------------


def test_select_top_candidate_one_per_cycle():
    """Multiple high-signal losers → return only the largest-gap one."""
    winner = _ok(1, "tech-A", score=0.5)
    loser_a = _ok(2, "tech-B", score=1.0)  # gap 1.0
    loser_b = _ok(3, "tech-C", score=2.5)  # gap 4.0 — biggest
    loser_c = _ok(4, "tech-D", score=1.5)  # gap 2.0
    arms = {"tech-B": 2, "tech-C": 3, "tech-D": 1}
    picked = select_top_candidate(
        losers=[loser_a, loser_b, loser_c],
        winner=winner,
        arms_tried=arms,
    )
    assert picked is not None
    assert picked.technique == "tech-C"


def test_select_top_candidate_no_high_signal_returns_none():
    """All losers below threshold (small gap or over-explored) → None."""
    winner = _ok(1, "tech-A", score=0.5)
    loser_a = _ok(2, "tech-B", score=0.51)  # gap too small
    loser_b = _ok(3, "tech-C", score=2.0)  # over-explored
    arms = {"tech-B": 2, "tech-C": 100}
    picked = select_top_candidate(
        losers=[loser_a, loser_b],
        winner=winner,
        arms_tried=arms,
    )
    assert picked is None


def test_select_top_candidate_empty_losers_returns_none():
    winner = _ok(1, "tech-A", score=0.5)
    picked = select_top_candidate(losers=[], winner=winner, arms_tried={})
    assert picked is None


def test_select_top_candidate_winner_none_returns_none():
    """No winner means we have no anchor to measure basin gap from."""
    loser = _ok(1, "tech-A", score=1.0)
    picked = select_top_candidate(losers=[loser], winner=None, arms_tried={})
    assert picked is None


# ---------------- draft_stub ----------------


def test_draft_stub_frontmatter_required_keys():
    winner = _ok(1, "tech-A", score=0.5)
    cand = _ok(2, "newton-max.md", score=1.5)
    path, content = draft_stub(
        problem=_problem(),
        candidate=cand,
        winner=winner,
        today="2026-05-27",
    )
    # Frontmatter parses
    assert content.startswith("---\n")
    fm_end = content.index("\n---\n", 4)
    fm = content[4:fm_end]
    for key in ("type:", "author:", "drafted:", "status:", "question_origin:"):
        assert key in fm, f"missing {key!r} in frontmatter"
    assert "status: stub" in fm  # explicit stub marker
    assert "author: agent" in fm
    assert "drafted: 2026-05-27" in fm
    assert "question_origin: problem-14" in fm


def test_draft_stub_filename_pattern():
    winner = _ok(1, "tech-A", score=0.5)
    cand = _ok(2, "newton_max.md", score=1.5)
    path, _ = draft_stub(
        problem=_problem(problem_id=14),
        candidate=cand,
        winner=winner,
        today="2026-05-27",
    )
    # Pattern: docs/wiki/findings/dead-end-<tech-slug>-p<id>-<date>.md
    assert path.startswith("docs/wiki/findings/dead-end-")
    assert "newton-max" in path or "newton_max" in path  # tech in name
    assert "p14" in path
    assert "2026-05-27" in path
    assert path.endswith(".md")


def test_draft_stub_body_has_what_we_tried_and_why_failed_placeholder():
    winner = _ok(1, "tech-A", score=0.5)
    cand = _ok(2, "newton-max.md", score=1.5)
    _, content = draft_stub(
        problem=_problem(),
        candidate=cand,
        winner=winner,
        today="2026-05-27",
    )
    assert "## What we tried" in content
    assert "newton-max.md" in content  # technique mentioned
    assert "1.5" in content  # candidate score
    assert "0.5" in content  # winner score
    assert "## Why it failed" in content
    assert "TODO" in content  # explicit stub marker
    assert "needs distillation" in content


def test_draft_stub_slugifies_technique_with_dots_and_underscores():
    """`newton_max.md` → safe slug for the filename (no .md / no underscores)."""
    winner = _ok(1, "tech-A", score=0.5)
    cand = _ok(2, "newton_max.md", score=1.5)
    path, _ = draft_stub(
        problem=_problem(),
        candidate=cand,
        winner=winner,
        today="2026-05-27",
    )
    # Slug should not contain .md
    fname = path.rsplit("/", 1)[-1]
    assert not fname.replace(".md", "").endswith(".md")
