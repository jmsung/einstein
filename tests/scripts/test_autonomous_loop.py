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
    # 2026-05-24: SKIP_STATUSES = {"retired"} only. Local status (frozen,
    # conquered, hidden, blocked, etc.) often drifts from arena state — a
    # powerful agent attempts every live problem and lets inner-loop logic
    # decide viability rather than gating at the queue.
    ("open", True),
    ("rank-1-tied", True),
    ("rank-2", True),
    ("rank-3", True),
    ("seed", True),
    ("conquered", True),        # arena may still be live; let inner loop decide
    ("rank-2-frozen", True),
    ("rank-5-frozen", True),
    ("frozen", True),
    ("blocked", True),
    ("hidden", True),
    ("shelved", True),
    ("rank-3-frozen-by-proximity-guard", True),
    # Only `retired` (5 dead pages archived 2026-05-23) is permanently inactive.
    ("retired", False),
])
def test_is_active_status_predicate(status: str, active: bool) -> None:
    p = al.Problem(problem_id=1, slug="x", tier="A", status=status,
                   score_current=None, path=Path("/nowhere"))
    assert al.is_active(p) is active


# ---------------- queue ordering ----------------


def test_queue_orders_by_problem_id_ascending(tmp_path: Path) -> None:
    """Tier-based prioritization was removed 2026-05-24 — id ascending only."""
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
    # Now: pure id ascending, regardless of tier
    assert [p.problem_id for p in ordered] == [2, 3, 5, 7, 9, 10]


def test_queue_filters_only_retired(tmp_path: Path) -> None:
    """conquered / frozen / blocked / hidden / etc. all stay in the queue;
    only `retired` is filtered."""
    pdir = _build_wiki_with_problems(tmp_path, [
        dict(problem_id=1, slug="active-s", tier="S", status="open"),
        dict(problem_id=2, slug="blocked", tier="S", status="blocked"),
        dict(problem_id=3, slug="frozen", tier="A", status="rank-2-frozen"),
        dict(problem_id=4, slug="active-a", tier="A", status="rank-1-tied"),
        dict(problem_id=5, slug="conquered", tier="S", status="conquered"),
        dict(problem_id=6, slug="retired", tier="C", status="retired"),
    ])
    problems = al.load_problems(pdir)
    ordered = al.build_queue(problems)
    # Everyone except retired survives, ordered by id
    assert [p.problem_id for p in ordered] == [1, 2, 3, 4, 5]


def test_queue_unknown_tier_does_not_affect_order() -> None:
    """Tier is purely informational now — queue order is id-only."""
    p_known = al.Problem(problem_id=2, slug="x", tier="A", status="open",
                         score_current=None, path=Path("/x"))
    p_unknown = al.Problem(problem_id=1, slug="y", tier="???", status="open",
                           score_current=None, path=Path("/y"))
    ordered = al.build_queue([p_known, p_unknown])
    # Pure id ascending — unknown tier still sorts by id
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
    """Only retired problems are inactive — use retired to test the no-active path."""
    pdir = _build_wiki_with_problems(tmp_path, [
        dict(problem_id=1, slug="dead", tier="S", status="retired"),
    ])
    log = tmp_path / "cycle-log.md"
    log.write_text("## Cycles\n")
    result = al.run_one_problem(
        problems_dir=pdir, cycle_log=log, dry_run=True, cycle_runner=None,
    )
    assert result is None


# ---------------- A3 integration: dispatch result → auto_submit ----------------


def test_inner_attempt_routes_dispatch_result_to_auto_submit() -> None:
    """When dispatch returns ok=True with a score+payload, inner_attempt must
    invoke auto_submit. Triple-verify is unwired (passed=False) so the gate
    chain rejects, but the call still happens — the wiring is the test target."""
    from types import SimpleNamespace

    problem = al.Problem(
        problem_id=14, slug="circle-packing-square", tier="B",
        status="rank-2-frozen", score_current=2.635, path=Path("/x"),
    )
    # Fake dispatcher: returns a successful dispatch result with score + payload
    fake_dispatch_result = SimpleNamespace(
        ok=True, optimizer="newton_max", score=2.636,
        payload={"vectors": [[1, 0]]}, runtime_seconds=12.3,
        error=None,
    )
    dispatcher = lambda problem_id, strategy: fake_dispatch_result
    # Fake auto_submitter: returns rejected (triple-verify failed)
    submit_calls: list = []

    def fake_submit(problem_id, payload, score, *, triple_verify, **kw):
        submit_calls.append({
            "problem_id": problem_id, "score": score,
            "tv_passed": triple_verify.get("passed"),
        })
        return SimpleNamespace(submitted=False, rejected_at_gate="triple-verify-failed")

    result = al.inner_attempt(
        problem, dry_run=False,
        dispatcher=dispatcher, auto_submitter=fake_submit,
    )

    # auto_submit was called with the dispatch's score+payload
    assert len(submit_calls) == 1
    assert submit_calls[0]["problem_id"] == 14
    assert submit_calls[0]["score"] == 2.636
    assert submit_calls[0]["tv_passed"] is False  # not wired yet
    # The cycle-log row notes capture the rejection
    assert "auto-submit-rejected@triple-verify-failed" in result["notes"]
    # Outcome remains the dispatch outcome (improved-local since 2.636 < 2.635
    # is FALSE; here it's no-change). Important: outcome is NOT "improved-and-submitted".
    assert result["outcome"] != "improved-and-submitted"
