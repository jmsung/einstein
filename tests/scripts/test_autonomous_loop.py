"""Tests for scripts/autonomous_loop.py — outer orchestrator + queue."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from unittest.mock import patch

import pytest

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "scripts"))

import autonomous_loop as al  # noqa: E402


# ---------------- fixture builder ----------------


def _write_problem(dir_: Path, *, problem_id: int, slug: str, tier: str = "A",
                   status: str = "open", score: float | None = None) -> None:
    fm_score = f"score_current: {score}\n" if score is not None else ""
    body = (
        "---\n"
        "type: problem\n"
        "author: agent\n"
        "drafted: 2026-05-23\n"
        f"problem_id: {problem_id}\n"
        f"tier: {tier}\n"
        f"status: {status}\n"
        f"{fm_score}"
        "concepts_invoked: []\n"
        "techniques_used: []\n"
        "findings_produced: []\n"
        "---\n\n"
        f"# Problem {problem_id} — {slug}\n"
    )
    (dir_ / f"{problem_id}-{slug}.md").write_text(body)


def _build_wiki_with_problems(tmp_path: Path, problems: list[dict]) -> Path:
    pdir = tmp_path / "docs" / "wiki" / "problems"
    pdir.mkdir(parents=True)
    for p in problems:
        _write_problem(pdir, **p)
    # noise that should be ignored
    (pdir / "README.md").write_text("# readme")
    (pdir / "_inventory.md").write_text("---\ntype: inventory\n---\n# inv")
    return pdir


# ---------------- Problem dataclass + parsing ----------------


def test_load_problems_parses_frontmatter(tmp_path: Path) -> None:
    pdir = _build_wiki_with_problems(tmp_path, [
        dict(problem_id=1, slug="alpha", tier="S", status="open", score=0.38),
        dict(problem_id=2, slug="beta", tier="A", status="rank-1-tied"),
    ])
    problems = al.load_problems(pdir)
    by_id = {p.problem_id: p for p in problems}
    assert by_id[1].tier == "S"
    assert by_id[1].status == "open"
    assert by_id[1].slug == "alpha"
    assert by_id[1].score_current == pytest.approx(0.38)
    assert by_id[2].tier == "A"
    assert by_id[2].status == "rank-1-tied"


def test_load_problems_skips_readme_and_underscore_files(tmp_path: Path) -> None:
    pdir = _build_wiki_with_problems(tmp_path, [
        dict(problem_id=1, slug="alpha"),
    ])
    problems = al.load_problems(pdir)
    assert [p.problem_id for p in problems] == [1]


# ---------------- is_active / skip predicate ----------------


@pytest.mark.parametrize("status,active", [
    ("open", True),
    ("rank-1-tied", True),
    ("rank-2", True),
    ("rank-3", True),
    ("seed", True),
    ("conquered", False),       # already best; only re-enter on new gap
    ("rank-2-frozen", False),   # frozen → skip
    ("rank-5-frozen", False),
    ("frozen", False),
    ("blocked", False),
    ("hidden", False),
    ("shelved", False),
    ("rank-3-frozen-by-proximity-guard", False),
])
def test_is_active_status_predicate(status: str, active: bool) -> None:
    p = al.Problem(problem_id=1, slug="x", tier="A", status=status,
                   score_current=None, path=Path("/nowhere"))
    assert al.is_active(p) is active


# ---------------- priority ordering ----------------


def test_priority_orders_by_tier_then_id(tmp_path: Path) -> None:
    pdir = _build_wiki_with_problems(tmp_path, [
        dict(problem_id=10, slug="b-tier-late", tier="B"),
        dict(problem_id=3, slug="s-tier-early", tier="S"),
        dict(problem_id=7, slug="a-tier-late", tier="A"),
        dict(problem_id=2, slug="s-tier-late", tier="S"),
        dict(problem_id=5, slug="a-tier-early", tier="A"),
        dict(problem_id=9, slug="c-tier", tier="C"),
    ])
    problems = al.load_problems(pdir)
    ordered = al.build_queue(problems)
    # Expected: S2, S3, A5, A7, B10, C9
    assert [p.problem_id for p in ordered] == [2, 3, 5, 7, 10, 9]


def test_queue_filters_inactive(tmp_path: Path) -> None:
    pdir = _build_wiki_with_problems(tmp_path, [
        dict(problem_id=1, slug="active-s", tier="S", status="open"),
        dict(problem_id=2, slug="blocked", tier="S", status="blocked"),
        dict(problem_id=3, slug="frozen", tier="A", status="rank-2-frozen"),
        dict(problem_id=4, slug="active-a", tier="A", status="rank-1-tied"),
        dict(problem_id=5, slug="conquered", tier="S", status="conquered"),
    ])
    problems = al.load_problems(pdir)
    ordered = al.build_queue(problems)
    assert [p.problem_id for p in ordered] == [1, 4]


def test_queue_unknown_tier_sorts_last() -> None:
    p_known = al.Problem(problem_id=1, slug="x", tier="A", status="open",
                         score_current=None, path=Path("/x"))
    p_unknown = al.Problem(problem_id=2, slug="y", tier="???", status="open",
                           score_current=None, path=Path("/y"))
    ordered = al.build_queue([p_unknown, p_known])
    assert [p.problem_id for p in ordered] == [1, 2]


# ---------------- cycle-log row formatting ----------------


def test_format_cycle_log_row_shape() -> None:
    row = al.format_cycle_log_row(
        cycle_id=42,
        problem="P19-difference-bases",
        start_score=2.6390274695,
        end_score=2.6390274695,
        hours=0.5,
        compute="local-cpu",
        wiki_citations=3,
        findings_added=0,
        concepts_added=0,
        author_mix={"agent": 1, "human": 0, "hybrid": 0},
        outcome="no-change",
        notes="Phase 3 smoke test — placeholder inner_attempt",
    )
    assert row.startswith("| 42 |")
    assert "P19-difference-bases" in row
    assert "2.6390274695" in row
    assert "a:1/h:0/hyb:0" in row
    assert "no-change" in row
    assert row.endswith("|")
    # Single line
    assert row.count("\n") == 0


def test_append_cycle_log_row(tmp_path: Path) -> None:
    log = tmp_path / "cycle-log.md"
    log.write_text(
        "# Cycle log\n\n"
        "## Cycles\n\n"
        "| # | problem | start → end | hours | compute | cites | findings+ | concepts+ | mix | outcome | notes |\n"
        "|---|---|---|---|---|---|---|---|---|---|---|\n"
        "| 0 | bootstrap | n/a | 1 | local-cpu | 0 | 0 | 0 | a:0/h:1/hyb:0 | bootstrap | seed |\n"
    )
    al.append_cycle_log_row(log, "| 1 | P19-test | 1.0 → 1.0 | 0.1 | local-cpu | 0 | 0 | 0 | a:1/h:0/hyb:0 | no-change | smoke |")
    text = log.read_text()
    assert "| 0 | bootstrap" in text
    assert "| 1 | P19-test" in text
    # Newly appended is the last non-empty line
    lines = [l for l in text.splitlines() if l.strip()]
    assert lines[-1].startswith("| 1 |")


# ---------------- next_cycle_id ----------------


def test_next_cycle_id_reads_max(tmp_path: Path) -> None:
    log = tmp_path / "cycle-log.md"
    log.write_text(
        "## Cycles\n\n"
        "| # | ... |\n"
        "| 0 | bootstrap |\n"
        "| 1 | P19 |\n"
        "| 2 | P19 |\n"
        "| 4 | P5 |\n"   # gap is OK; we take max + 1
    )
    assert al.next_cycle_id(log) == 5


def test_next_cycle_id_empty_log_returns_zero(tmp_path: Path) -> None:
    log = tmp_path / "cycle-log.md"
    log.write_text("# Cycle log\n\n## Cycles\n\n| # | problem |\n|---|---|\n")
    assert al.next_cycle_id(log) == 0


# ---------------- orchestrator drive ----------------


def test_run_one_problem_dry_run_does_not_mutate(tmp_path: Path) -> None:
    pdir = _build_wiki_with_problems(tmp_path, [
        dict(problem_id=1, slug="alpha", tier="S", status="open"),
    ])
    log = tmp_path / "cycle-log.md"
    log.write_text("## Cycles\n\n| # | problem |\n|---|---|\n")
    pre_log = log.read_text()

    result = al.run_one_problem(
        problems_dir=pdir, cycle_log=log, dry_run=True,
        cycle_runner=None,
    )
    assert result.problem.problem_id == 1
    assert log.read_text() == pre_log  # dry-run wrote nothing


def test_run_one_problem_appends_row_and_calls_cycle_runner(tmp_path: Path) -> None:
    pdir = _build_wiki_with_problems(tmp_path, [
        dict(problem_id=1, slug="alpha", tier="S", status="open", score=1.5),
    ])
    log = tmp_path / "cycle-log.md"
    log.write_text("## Cycles\n\n| # | problem |\n|---|---|\n")

    called: dict = {}
    def fake_runner(cycle_id: int, problem_slug: str) -> int:
        called["cycle_id"] = cycle_id
        called["slug"] = problem_slug
        return 0

    result = al.run_one_problem(
        problems_dir=pdir, cycle_log=log, dry_run=False,
        cycle_runner=fake_runner,
    )
    assert called["slug"] == "1-alpha"
    text = log.read_text()
    assert "P1-alpha" in text or "1-alpha" in text


def test_acquire_lock_succeeds_when_free(tmp_path: Path) -> None:
    lockfile = tmp_path / "lock"
    fd = al._acquire_lock(lockfile)
    try:
        assert lockfile.is_file()
        content = lockfile.read_text()
        assert "pid=" in content
    finally:
        al._release_lock(fd, lockfile)
    assert not lockfile.exists()


def test_acquire_lock_raises_when_held(tmp_path: Path) -> None:
    lockfile = tmp_path / "lock"
    fd = al._acquire_lock(lockfile)
    try:
        with pytest.raises(al._LockHeld):
            al._acquire_lock(lockfile)
    finally:
        al._release_lock(fd, lockfile)


def test_has_recent_cycle_true_for_just_modified(tmp_path: Path) -> None:
    log = tmp_path / "cycle-log.md"
    log.write_text("# log")
    assert al._has_recent_cycle(log, minutes=60) is True


def test_has_recent_cycle_false_for_missing(tmp_path: Path) -> None:
    assert al._has_recent_cycle(tmp_path / "no-such.md", minutes=60) is False


def test_run_one_problem_no_active_problems_returns_none(tmp_path: Path) -> None:
    pdir = _build_wiki_with_problems(tmp_path, [
        dict(problem_id=1, slug="frozen", tier="S", status="frozen"),
    ])
    log = tmp_path / "cycle-log.md"
    log.write_text("## Cycles\n")
    result = al.run_one_problem(
        problems_dir=pdir, cycle_log=log, dry_run=True, cycle_runner=None,
    )
    assert result is None
