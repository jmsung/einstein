"""Tests for scripts/autonomous_loop.py — outer orchestrator + queue."""

from __future__ import annotations

import sys
from pathlib import Path
from unittest.mock import patch

import pytest

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "scripts"))

import autonomous_loop as al  # noqa: E402

# ---------------- fixture builder ----------------


def _write_problem(
    dir_: Path,
    *,
    problem_id: int,
    slug: str,
    tier: str = "A",
    status: str = "open",
    score: float | None = None,
) -> None:
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
    pdir = _build_wiki_with_problems(
        tmp_path,
        [
            dict(problem_id=1, slug="alpha", tier="S", status="open", score=0.38),
            dict(problem_id=2, slug="beta", tier="A", status="rank-1-tied"),
        ],
    )
    problems = al.load_problems(pdir)
    by_id = {p.problem_id: p for p in problems}
    assert by_id[1].tier == "S"
    assert by_id[1].status == "open"
    assert by_id[1].slug == "alpha"
    assert by_id[1].score_current == pytest.approx(0.38)
    assert by_id[2].tier == "A"
    assert by_id[2].status == "rank-1-tied"


def test_load_problems_skips_readme_and_underscore_files(tmp_path: Path) -> None:
    pdir = _build_wiki_with_problems(
        tmp_path,
        [
            dict(problem_id=1, slug="alpha"),
        ],
    )
    problems = al.load_problems(pdir)
    assert [p.problem_id for p in problems] == [1]


# ---------------- is_active / skip predicate ----------------


@pytest.mark.parametrize(
    "status,active",
    [
        # 2026-05-24: SKIP_STATUSES = {"retired"} only. Local status (frozen,
        # conquered, hidden, blocked, etc.) often drifts from arena state — a
        # powerful agent attempts every live problem and lets inner-loop logic
        # decide viability rather than gating at the queue.
        ("open", True),
        ("rank-1-tied", True),
        ("rank-2", True),
        ("rank-3", True),
        ("seed", True),
        ("conquered", True),  # arena may still be live; let inner loop decide
        ("rank-2-frozen", True),
        ("rank-5-frozen", True),
        ("frozen", True),
        ("blocked", True),
        ("hidden", True),
        ("shelved", True),
        ("rank-3-frozen-by-proximity-guard", True),
        # Only `retired` (5 dead pages archived 2026-05-23) is permanently inactive.
        ("retired", False),
    ],
)
def test_is_active_status_predicate(status: str, active: bool) -> None:
    p = al.Problem(
        problem_id=1, slug="x", tier="A", status=status, score_current=None, path=Path("/nowhere")
    )
    assert al.is_active(p) is active


# ---------------- queue ordering ----------------


def test_queue_orders_by_problem_id_ascending(tmp_path: Path) -> None:
    """Tier-based prioritization was removed 2026-05-24 — id ascending only."""
    pdir = _build_wiki_with_problems(
        tmp_path,
        [
            dict(problem_id=10, slug="b-tier-late", tier="B"),
            dict(problem_id=3, slug="s-tier-early", tier="S"),
            dict(problem_id=7, slug="a-tier-late", tier="A"),
            dict(problem_id=2, slug="s-tier-late", tier="S"),
            dict(problem_id=5, slug="a-tier-early", tier="A"),
            dict(problem_id=9, slug="c-tier", tier="C"),
        ],
    )
    problems = al.load_problems(pdir)
    ordered = al.build_queue(problems)
    # Now: pure id ascending, regardless of tier
    assert [p.problem_id for p in ordered] == [2, 3, 5, 7, 9, 10]


def test_queue_filters_only_retired(tmp_path: Path) -> None:
    """conquered / frozen / blocked / hidden / etc. all stay in the queue;
    only `retired` is filtered."""
    pdir = _build_wiki_with_problems(
        tmp_path,
        [
            dict(problem_id=1, slug="active-s", tier="S", status="open"),
            dict(problem_id=2, slug="blocked", tier="S", status="blocked"),
            dict(problem_id=3, slug="frozen", tier="A", status="rank-2-frozen"),
            dict(problem_id=4, slug="active-a", tier="A", status="rank-1-tied"),
            dict(problem_id=5, slug="conquered", tier="S", status="conquered"),
            dict(problem_id=6, slug="retired", tier="C", status="retired"),
        ],
    )
    problems = al.load_problems(pdir)
    ordered = al.build_queue(problems)
    # Everyone except retired survives, ordered by id
    assert [p.problem_id for p in ordered] == [1, 2, 3, 4, 5]


def test_queue_unknown_tier_does_not_affect_order() -> None:
    """Tier is purely informational now — queue order is id-only."""
    p_known = al.Problem(
        problem_id=2, slug="x", tier="A", status="open", score_current=None, path=Path("/x")
    )
    p_unknown = al.Problem(
        problem_id=1, slug="y", tier="???", status="open", score_current=None, path=Path("/y")
    )
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
    # cited_sources defaults to () → trailing cites_src column reads 0
    last_cell = row.rstrip().rstrip("|").rstrip().split("|")[-1].strip()
    assert last_cell == "0"


def test_format_cycle_log_row_with_cited_sources_renders_count() -> None:
    """Goal 4 of js/feat/research-synthesis: cited_sources count is the rightmost column."""
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
        notes="smoke",
        cited_sources=[
            "docs/source/2026-lee-meta-harness.md",
            "docs/source/2024-baek-researchagent.md",
            "docs/source/2026-zhang-hyperagents.md",
        ],
    )
    last_cell = row.rstrip().rstrip("|").rstrip().split("|")[-1].strip()
    assert last_cell == "3"


def test_append_cycle_log_row(tmp_path: Path) -> None:
    log = tmp_path / "cycle-log.md"
    log.write_text(
        "# Cycle log\n\n"
        "## Cycles\n\n"
        "| # | problem | start → end | hours | compute | cites | findings+ | concepts+ | mix | outcome | notes |\n"
        "|---|---|---|---|---|---|---|---|---|---|---|\n"
        "| 0 | bootstrap | n/a | 1 | local-cpu | 0 | 0 | 0 | a:0/h:1/hyb:0 | bootstrap | seed |\n"
    )
    al.append_cycle_log_row(
        log,
        "| 1 | P19-test | 1.0 → 1.0 | 0.1 | local-cpu | 0 | 0 | 0 | a:1/h:0/hyb:0 | no-change | smoke |",
    )
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
        "| 4 | P5 |\n"  # gap is OK; we take max + 1
    )
    assert al.next_cycle_id(log) == 5


def test_next_cycle_id_empty_log_returns_zero(tmp_path: Path) -> None:
    log = tmp_path / "cycle-log.md"
    log.write_text("# Cycle log\n\n## Cycles\n\n| # | problem |\n|---|---|\n")
    assert al.next_cycle_id(log) == 0


# ---------------- orchestrator drive ----------------


def test_run_one_problem_dry_run_does_not_mutate(tmp_path: Path) -> None:
    pdir = _build_wiki_with_problems(
        tmp_path,
        [
            dict(problem_id=1, slug="alpha", tier="S", status="open"),
        ],
    )
    log = tmp_path / "cycle-log.md"
    log.write_text("## Cycles\n\n| # | problem |\n|---|---|\n")
    pre_log = log.read_text()

    result = al.run_one_problem(
        problems_dir=pdir,
        cycle_log=log,
        dry_run=True,
        cycle_runner=None,
    )
    assert result.problem.problem_id == 1
    assert log.read_text() == pre_log  # dry-run wrote nothing


def test_run_one_problem_appends_row_and_calls_cycle_runner(tmp_path: Path) -> None:
    pdir = _build_wiki_with_problems(
        tmp_path,
        [
            dict(problem_id=1, slug="alpha", tier="S", status="open", score=1.5),
        ],
    )
    log = tmp_path / "cycle-log.md"
    log.write_text("## Cycles\n\n| # | problem |\n|---|---|\n")

    called: dict = {}

    def fake_runner(cycle_id: int, problem_slug: str) -> int:
        called["cycle_id"] = cycle_id
        called["slug"] = problem_slug
        return 0

    result = al.run_one_problem(
        problems_dir=pdir,
        cycle_log=log,
        dry_run=False,
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
    pdir = _build_wiki_with_problems(
        tmp_path,
        [
            dict(problem_id=1, slug="dead", tier="S", status="retired"),
        ],
    )
    log = tmp_path / "cycle-log.md"
    log.write_text("## Cycles\n")
    result = al.run_one_problem(
        problems_dir=pdir,
        cycle_log=log,
        dry_run=True,
        cycle_runner=None,
    )
    assert result is None


# ---------------- A3 integration: dispatch result → auto_submit ----------------


def test_inner_attempt_routes_dispatch_result_to_auto_submit() -> None:
    """When dispatch returns ok=True with a score+payload, inner_attempt must
    invoke auto_submit. Triple-verify is unwired (passed=False) so the gate
    chain rejects, but the call still happens — the wiring is the test target."""
    from types import SimpleNamespace

    problem = al.Problem(
        problem_id=14,
        slug="circle-packing-square",
        tier="B",
        status="rank-2-frozen",
        score_current=2.635,
        path=Path("/x"),
    )
    # Fake dispatcher: returns a successful dispatch result with score + payload
    fake_dispatch_result = SimpleNamespace(
        ok=True,
        optimizer="newton_max",
        score=2.636,
        payload={"vectors": [[1, 0]]},
        runtime_seconds=12.3,
        error=None,
    )

    def dispatcher(problem_id, strategy):
        return fake_dispatch_result

    # Fake auto_submitter: returns rejected (triple-verify failed)
    submit_calls: list = []

    def fake_submit(problem_id, payload, score, *, triple_verify, **kw):
        submit_calls.append(
            {
                "problem_id": problem_id,
                "score": score,
                "tv_passed": triple_verify.get("passed"),
            }
        )
        return SimpleNamespace(submitted=False, rejected_at_gate="triple-verify-failed")

    result = al.inner_attempt(
        problem,
        dry_run=False,
        dispatcher=dispatcher,
        auto_submitter=fake_submit,
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


# ============================================================================
# Goal 7.4 — visit refactor
# ============================================================================


def test_inner_attempt_returns_chosen_techniques(tmp_path: Path) -> None:
    """inner_attempt's result dict must expose chosen_techniques (list[str])
    so run_one_visit can build the avoid set for attempt 2/3."""
    pdir = _build_wiki_with_problems(
        tmp_path,
        [
            dict(
                problem_id=14,
                slug="circle-packing-square",
                tier="A",
                status="rank-2-frozen",
                score=2.6,
            ),
        ],
    )
    problems = al.load_problems(pdir)
    p14 = next(p for p in problems if p.problem_id == 14)

    result = al.inner_attempt(p14, dry_run=True)
    assert "chosen_techniques" in result
    assert isinstance(result["chosen_techniques"], list)
    # Real skill-library should yield at least one technique for the
    # 'packing' category P14 maps to. Use a soft check so this test stays
    # robust to skill-library churn.
    if result["chosen_techniques"]:
        for t in result["chosen_techniques"]:
            assert isinstance(t, str) and t.strip()


def test_inner_attempt_honors_avoid_techniques(tmp_path: Path) -> None:
    """attempt_index>1 + avoid_techniques → strategy_picker must not pick
    any technique in the avoid set. Drive via skill-library injection."""
    pdir = _build_wiki_with_problems(
        tmp_path,
        [
            dict(
                problem_id=14,
                slug="circle-packing-square",
                tier="A",
                status="rank-2-frozen",
                score=2.6,
            ),
        ],
    )
    problems = al.load_problems(pdir)
    p14 = next(p for p in problems if p.problem_id == 14)

    # Two-technique library; avoiding both → no picks
    lib = tmp_path / "skill-library.md"
    lib.write_text(
        "| `tech-A` | packing | 5 | 2 | 1 | 2026-01-01 | 0.40 |\n"
        "| `tech-B` | packing | 3 | 1 | 2 | 2026-02-01 | 0.33 |\n"
    )

    # No avoid set → some technique gets picked
    r1 = al.inner_attempt(p14, dry_run=True, skill_library=lib, attempt_index=1)
    assert set(r1["chosen_techniques"]) <= {"tech-A", "tech-B"}
    assert r1["chosen_techniques"]  # non-empty

    # Avoiding tech-A → only tech-B can be the prior (no novel since only 1 left)
    r2 = al.inner_attempt(
        p14,
        dry_run=True,
        skill_library=lib,
        attempt_index=2,
        avoid_techniques={"tech-A"},
    )
    assert "tech-A" not in r2["chosen_techniques"]
    assert "tech-B" in r2["chosen_techniques"]
    assert "attempt=2" in r2["notes"]

    # Avoiding both → empty pick + the "council needed" note
    r3 = al.inner_attempt(
        p14,
        dry_run=True,
        skill_library=lib,
        attempt_index=3,
        avoid_techniques={"tech-A", "tech-B"},
    )
    assert r3["chosen_techniques"] == []
    assert "council needed" in r3["notes"]


def test_row_from_attempt_strips_chosen_techniques(tmp_path: Path) -> None:
    pdir = _build_wiki_with_problems(
        tmp_path,
        [
            dict(
                problem_id=14,
                slug="circle-packing-square",
                tier="A",
                status="rank-2-frozen",
                score=2.6,
            ),
        ],
    )
    problems = al.load_problems(pdir)
    p14 = next(p for p in problems if p.problem_id == 14)
    result = al.inner_attempt(p14, dry_run=True)

    row_kwargs = al._row_from_attempt(result)
    assert "chosen_techniques" not in row_kwargs
    # format_cycle_log_row should accept the stripped kwargs without error
    row = al.format_cycle_log_row(
        cycle_id=0,
        problem=p14.display,
        **row_kwargs,
    )
    assert "P14-circle-packing-square" in row


def test_run_one_visit_stops_when_strategy_picker_unavailable(tmp_path: Path) -> None:
    pdir = _build_wiki_with_problems(
        tmp_path,
        [
            dict(problem_id=1, slug="alpha", tier="S", status="open", score=1.5),
        ],
    )
    log = tmp_path / "cycle-log.md"
    log.write_text("## Cycles\n\n| # | problem |\n|---|---|\n")
    problem = al.load_problems(pdir)[0]

    runner_calls: list = []

    def fake_runner(cid, slug):
        runner_calls.append((cid, slug))
        return 0

    with patch.object(al, "strategy_picker", None):
        results = al.run_one_visit(
            problem,
            cycle_log=log,
            dry_run=False,
            cycle_runner=fake_runner,
            skip_gates=True,
        )
    assert len(results) == 1
    assert len(runner_calls) == 1


def test_run_one_visit_writes_one_row_per_attempt(tmp_path: Path) -> None:
    """With max_attempts=3 and no real progress, the visit runs until the
    convergence rule fires. Each cycle gets its own cycle-log row."""
    pdir = _build_wiki_with_problems(
        tmp_path,
        [
            dict(
                problem_id=14,
                slug="circle-packing-square",
                tier="A",
                status="rank-2-frozen",
                score=2.6,
            ),
        ],
    )
    log = tmp_path / "cycle-log.md"
    log.write_text("## Cycles\n\n| # | problem |\n|---|---|\n")
    problem = next(p for p in al.load_problems(pdir) if p.problem_id == 14)

    runner_calls: list = []
    results = al.run_one_visit(
        problem,
        cycle_log=log,
        dry_run=False,
        cycle_runner=lambda cid, slug: runner_calls.append((cid, slug)) or 0,
        max_attempts=3,
        skip_gates=True,
    )

    # 1 cycle minimum, ≤3 cycles; each cycle = one row + one cycle_runner call
    assert 1 <= len(results) <= 3
    assert len(runner_calls) == len(results)
    log_text = log.read_text()
    for cr in results:
        assert f"| {cr.cycle_id} |" in log_text


def test_run_one_visit_dry_run_does_not_mutate(tmp_path: Path) -> None:
    pdir = _build_wiki_with_problems(
        tmp_path,
        [
            dict(problem_id=1, slug="alpha", tier="S", status="open", score=1.5),
        ],
    )
    log = tmp_path / "cycle-log.md"
    log.write_text("## Cycles\n\n| # | problem |\n|---|---|\n")
    pre = log.read_text()
    problem = al.load_problems(pdir)[0]

    runner_calls: list = []
    al.run_one_visit(
        problem,
        cycle_log=log,
        dry_run=True,
        cycle_runner=lambda *_a: runner_calls.append(_a) or 0,
        max_attempts=3,
    )
    assert log.read_text() == pre
    # dry-run bypasses cycle_runner too
    assert runner_calls == []


def test_run_one_visit_grows_avoid_set_across_attempts(tmp_path: Path) -> None:
    """When attempt 1 picks technique X, attempt 2's inner_attempt must be
    called with avoid_techniques containing X."""
    pdir = _build_wiki_with_problems(
        tmp_path,
        [
            dict(
                problem_id=14,
                slug="circle-packing-square",
                tier="A",
                status="rank-2-frozen",
                score=2.6,
            ),
        ],
    )
    log = tmp_path / "cycle-log.md"
    log.write_text("## Cycles\n\n| # | problem |\n|---|---|\n")
    problem = next(p for p in al.load_problems(pdir) if p.problem_id == 14)

    seen_avoids: list[set[str] | None] = []
    real_inner = al.inner_attempt

    def spy_inner(p, **kw):
        seen_avoids.append(kw.get("avoid_techniques"))
        return real_inner(p, **kw)

    with patch.object(al, "inner_attempt", side_effect=spy_inner):
        results = al.run_one_visit(
            problem,
            cycle_log=log,
            dry_run=False,
            cycle_runner=lambda *_a: 0,
            max_attempts=3,
            skip_gates=True,
        )

    # Attempt 1 has no avoid set
    assert seen_avoids[0] is None
    # If there was a 2nd attempt, it must have avoid_techniques set
    if len(seen_avoids) >= 2:
        assert seen_avoids[1] is not None
        assert len(seen_avoids[1]) > 0
    # If there was a 3rd attempt, its avoid set is at least as large as #2's
    if len(seen_avoids) >= 3:
        assert len(seen_avoids[2]) >= len(seen_avoids[1])
    assert 1 <= len(results) <= 3


def test_run_one_visit_runs_3_cycles_when_score_improves(tmp_path: Path) -> None:
    """If the dispatcher reports score progress each attempt, convergence-
    detect keeps going up to max_attempts."""
    pdir = _build_wiki_with_problems(
        tmp_path,
        [
            dict(
                problem_id=14,
                slug="circle-packing-square",
                tier="A",
                status="rank-2-frozen",
                score=3.0,
            ),
        ],
    )
    log = tmp_path / "cycle-log.md"
    log.write_text("## Cycles\n\n| # | problem |\n|---|---|\n")
    problem = next(p for p in al.load_problems(pdir) if p.problem_id == 14)

    # Patch inner_attempt to simulate steady score progress (lower = better)
    scores = iter([2.9, 2.8, 2.7])
    fake_techniques = iter([["A"], ["B"], ["C"]])

    def stub_inner(p, **kw):
        return {
            "start_score": 3.0,
            "end_score": next(scores),
            "hours": 0.1,
            "compute": "local-cpu",
            "wiki_citations": 0,
            "findings_added": 0,
            "concepts_added": 0,
            "author_mix": {"agent": 1, "human": 0, "hybrid": 0},
            "outcome": "improved-local",
            "notes": f"stub attempt={kw.get('attempt_index')}",
            "chosen_techniques": next(fake_techniques),
        }

    with patch.object(al, "inner_attempt", side_effect=stub_inner):
        results = al.run_one_visit(
            problem,
            cycle_log=log,
            dry_run=False,
            cycle_runner=lambda *_a: 0,
            max_attempts=3,
            skip_gates=True,
        )
    assert len(results) == 3


def test_run_one_visit_stops_on_convergence(tmp_path: Path) -> None:
    """When score doesn't change AND no new gap surfaces, convergence-detect
    stops on the second attempt."""
    pdir = _build_wiki_with_problems(
        tmp_path,
        [
            dict(
                problem_id=14,
                slug="circle-packing-square",
                tier="A",
                status="rank-2-frozen",
                score=2.5,
            ),
        ],
    )
    log = tmp_path / "cycle-log.md"
    log.write_text("## Cycles\n\n| # | problem |\n|---|---|\n")
    problem = next(p for p in al.load_problems(pdir) if p.problem_id == 14)

    def flat_inner(p, **kw):
        # End score unchanged + no chosen techniques → avoid set empty.
        return {
            "start_score": 2.5,
            "end_score": 2.5,
            "hours": 0.0,
            "compute": "local-cpu",
            "wiki_citations": 0,
            "findings_added": 0,
            "concepts_added": 0,
            "author_mix": {"agent": 1, "human": 0, "hybrid": 0},
            "outcome": "no-change",
            "notes": "flat",
            "chosen_techniques": [],
        }

    with patch.object(al, "inner_attempt", side_effect=flat_inner):
        results = al.run_one_visit(
            problem,
            cycle_log=log,
            dry_run=False,
            cycle_runner=lambda *_a: 0,
            max_attempts=3,
            skip_gates=True,
        )
    # Cycle 1 always continues; cycle 2 stops (no progress + no gap)
    assert len(results) == 2


def test_run_queue_visits_each_problem_with_max_attempts(tmp_path: Path) -> None:
    """run_queue with max_problems=2, max_attempts_per_visit=2 → up to 4 cycles
    across 2 distinct problems."""
    pdir = _build_wiki_with_problems(
        tmp_path,
        [
            dict(problem_id=1, slug="alpha", tier="S", status="open", score=1.0),
            dict(problem_id=2, slug="beta", tier="A", status="open", score=2.0),
        ],
    )
    log = tmp_path / "cycle-log.md"
    log.write_text("## Cycles\n\n| # | problem |\n|---|---|\n")

    results = al.run_queue(
        problems_dir=pdir,
        cycle_log=log,
        max_problems=2,
        max_attempts_per_visit=2,
        dry_run=False,
        cycle_runner=lambda *_a: 0,
        skip_gates=True,
    )
    # Each distinct problem appears at least once and at most max_attempts times
    by_pid: dict[int, int] = {}
    for r in results:
        by_pid[r.problem.problem_id] = by_pid.get(r.problem.problem_id, 0) + 1
    assert set(by_pid.keys()) == {1, 2}
    for pid, cnt in by_pid.items():
        assert 1 <= cnt <= 2


def test_run_queue_max_attempts_1_is_backcompat(tmp_path: Path) -> None:
    """max_attempts_per_visit=1 recovers the pre-7.4 one-cycle-per-problem
    behavior (one cycle-log row per visited problem)."""
    pdir = _build_wiki_with_problems(
        tmp_path,
        [
            dict(problem_id=1, slug="alpha", tier="S", status="open", score=1.0),
            dict(problem_id=2, slug="beta", tier="A", status="open", score=2.0),
        ],
    )
    log = tmp_path / "cycle-log.md"
    log.write_text("## Cycles\n\n| # | problem |\n|---|---|\n")

    results = al.run_queue(
        problems_dir=pdir,
        cycle_log=log,
        max_problems=2,
        max_attempts_per_visit=1,
        dry_run=False,
        cycle_runner=lambda *_a: 0,
        skip_gates=True,
    )
    assert len(results) == 2
    assert {r.problem.problem_id for r in results} == {1, 2}


def test_pick_strategy_avoid_techniques_excludes_them(tmp_path: Path) -> None:
    """7.4 wiring at the strategy_picker level."""
    sys.path.insert(0, str(_REPO / "docs" / "tools"))
    import strategy_picker as sp  # noqa: E402

    lib = tmp_path / "skill-library.md"
    lib.write_text(
        "| `tech-A` | packing | 5 | 2 | 1 | 2026-01-01 | 0.80 |\n"
        "| `tech-B` | packing | 3 | 1 | 2 | 2026-02-01 | 0.40 |\n"
        "| `tech-C` | packing | 1 | 0 | 1 | 2026-03-01 | 0.10 |\n"
    )
    # No avoid → tech-A is prior (highest hit_rate)
    pick = sp.pick_strategy(lib, category="packing")
    assert pick.prior.technique == "tech-A"

    # Avoid tech-A → tech-B becomes prior
    pick = sp.pick_strategy(lib, category="packing", avoid_techniques={"tech-A"})
    assert pick.prior.technique == "tech-B"
    assert "avoided=['tech-A']" in pick.rationale

    # Avoid all → no picks
    pick = sp.pick_strategy(
        lib, category="packing", avoid_techniques={"tech-A", "tech-B", "tech-C"}
    )
    assert pick.prior is None and pick.novel is None
    assert "no techniques" in pick.rationale


# ============================================================================
# Goal 7.5 — gates wiring into run_one_visit
# ============================================================================


def test_run_one_visit_skips_when_precheck_returns_skip(tmp_path: Path) -> None:
    """Sentinel/budget/reach/thermal → gate-skipped row, no cycles run."""
    pdir = _build_wiki_with_problems(
        tmp_path,
        [
            dict(problem_id=1, slug="alpha", tier="S", status="open", score=1.5),
        ],
    )
    log = tmp_path / "cycle-log.md"
    log.write_text("## Cycles\n\n| # | problem |\n|---|---|\n")
    problem = al.load_problems(pdir)[0]

    from types import SimpleNamespace

    fake_decision = SimpleNamespace(
        action="skip",
        reason="sentinel present",
        llm_enabled=False,
    )
    runner_calls: list = []
    with patch.object(al.inner_agent_gates, "precheck", return_value=fake_decision):
        results = al.run_one_visit(
            problem,
            cycle_log=log,
            dry_run=False,
            cycle_runner=lambda *_a: runner_calls.append(_a) or 0,
            max_attempts=3,
            # skip_gates=False (default) → precheck runs
        )
    assert len(results) == 1
    assert results[0].outcome == "gate-skipped"
    assert "sentinel present" in results[0].notes
    # No cycle_runner.sh invocation on a skip
    assert runner_calls == []
    # The skip still writes one cycle-log row (cycle-discipline)
    assert "gate-skipped" in log.read_text()


def test_run_one_visit_proceeds_when_precheck_returns_proceed(tmp_path: Path) -> None:
    """Kill-switch / proceed-llm-enabled both run cycles normally for now."""
    pdir = _build_wiki_with_problems(
        tmp_path,
        [
            dict(
                problem_id=14,
                slug="circle-packing-square",
                tier="A",
                status="rank-2-frozen",
                score=2.6,
            ),
        ],
    )
    log = tmp_path / "cycle-log.md"
    log.write_text("## Cycles\n\n| # | problem |\n|---|---|\n")
    problem = next(p for p in al.load_problems(pdir) if p.problem_id == 14)

    from types import SimpleNamespace

    fake_decision = SimpleNamespace(
        action="proceed",
        reason="",
        llm_enabled=True,
    )
    runner_calls: list = []
    with patch.object(al.inner_agent_gates, "precheck", return_value=fake_decision):
        results = al.run_one_visit(
            problem,
            cycle_log=log,
            dry_run=False,
            cycle_runner=lambda *_a: runner_calls.append(_a) or 0,
            max_attempts=3,
        )
    assert all(r.outcome != "gate-skipped" for r in results)
    assert len(runner_calls) == len(results)


def test_run_one_visit_skip_gates_param_bypasses_precheck(tmp_path: Path) -> None:
    """skip_gates=True path must not call precheck at all."""
    pdir = _build_wiki_with_problems(
        tmp_path,
        [
            dict(
                problem_id=14,
                slug="circle-packing-square",
                tier="A",
                status="rank-2-frozen",
                score=2.6,
            ),
        ],
    )
    log = tmp_path / "cycle-log.md"
    log.write_text("## Cycles\n\n| # | problem |\n|---|---|\n")
    problem = next(p for p in al.load_problems(pdir) if p.problem_id == 14)

    # If precheck were called, this AssertionError would propagate
    with patch.object(
        al.inner_agent_gates, "precheck", side_effect=AssertionError("should not be called")
    ):
        results = al.run_one_visit(
            problem,
            cycle_log=log,
            dry_run=False,
            cycle_runner=lambda *_a: 0,
            max_attempts=2,
            skip_gates=True,
        )
    assert all(r.outcome != "gate-skipped" for r in results)


def test_run_one_visit_dry_run_bypasses_precheck(tmp_path: Path) -> None:
    """dry_run=True implies skip_gates — precheck would mutate nothing
    but its subprocess + network calls are inappropriate during a dry run."""
    pdir = _build_wiki_with_problems(
        tmp_path,
        [
            dict(
                problem_id=14,
                slug="circle-packing-square",
                tier="A",
                status="rank-2-frozen",
                score=2.6,
            ),
        ],
    )
    log = tmp_path / "cycle-log.md"
    log.write_text("## Cycles\n\n| # | problem |\n|---|---|\n")
    problem = next(p for p in al.load_problems(pdir) if p.problem_id == 14)
    pre = log.read_text()

    with patch.object(
        al.inner_agent_gates, "precheck", side_effect=AssertionError("should not be called")
    ):
        results = al.run_one_visit(
            problem,
            cycle_log=log,
            dry_run=True,
            cycle_runner=lambda *_a: 0,
            max_attempts=2,
        )
    assert all(r.outcome != "gate-skipped" for r in results)
    assert log.read_text() == pre


# ============================================================================
# Goal 7.6 — wiki/mb write audit (git delta in notes)
# ============================================================================


def _init_git_repo_with_paths(
    tmp_path: Path, *, tracked: list[str] = (), untracked: list[str] = (), modified: list[str] = ()
) -> Path:
    """Build a tmp git repo with specific status: tracked-committed, untracked,
    and tracked-but-modified files. Returns the repo root."""
    import subprocess as sp

    sp.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    sp.run(["git", "config", "user.email", "test@example.com"], cwd=tmp_path, check=True)
    sp.run(["git", "config", "user.name", "test"], cwd=tmp_path, check=True)
    # Make all to-be-tracked files first, commit them.
    for rel in list(tracked) + list(modified):
        p = tmp_path / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("original\n")
    if tracked or modified:
        sp.run(["git", "add", "-A"], cwd=tmp_path, check=True)
        sp.run(["git", "commit", "-q", "-m", "seed"], cwd=tmp_path, check=True)
    # Now make untracked + modify the modified ones.
    for rel in untracked:
        p = tmp_path / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("new\n")
    for rel in modified:
        (tmp_path / rel).write_text("changed\n")
    return tmp_path


def test_snapshot_wiki_mb_paths_captures_untracked(tmp_path: Path) -> None:
    repo = _init_git_repo_with_paths(
        tmp_path,
        tracked=["src/keep.py"],
        untracked=[
            "docs/wiki/findings/dead-end-x.md",
            "mb/problems/14/log.md",
            "scripts/should-be-ignored.py",
        ],
    )
    paths = al._snapshot_wiki_mb_paths(repo)
    assert "docs/wiki/findings/dead-end-x.md" in paths
    assert "mb/problems/14/log.md" in paths
    # Scope filter — untracked files outside wiki/mb don't appear
    assert "scripts/should-be-ignored.py" not in paths


def test_snapshot_wiki_mb_paths_captures_modified(tmp_path: Path) -> None:
    repo = _init_git_repo_with_paths(
        tmp_path,
        modified=["docs/wiki/concepts/foo.md", "mb/progress.md"],
    )
    paths = al._snapshot_wiki_mb_paths(repo)
    assert "docs/wiki/concepts/foo.md" in paths
    assert "mb/progress.md" in paths


def test_snapshot_wiki_mb_paths_empty_on_clean_repo(tmp_path: Path) -> None:
    repo = _init_git_repo_with_paths(tmp_path, tracked=["docs/wiki/x.md"])
    paths = al._snapshot_wiki_mb_paths(repo)
    assert paths == set()


def test_snapshot_wiki_mb_paths_empty_when_not_a_git_repo(tmp_path: Path) -> None:
    """No `git init` ran — git status returns non-zero; we return empty."""
    paths = al._snapshot_wiki_mb_paths(tmp_path)
    assert paths == set()


def test_snapshot_wiki_mb_paths_returns_empty_when_git_missing() -> None:
    """FileNotFoundError → empty set (audit is best-effort)."""
    with patch.object(al.subprocess, "run", side_effect=FileNotFoundError("git")):
        paths = al._snapshot_wiki_mb_paths(Path("/tmp"))
    assert paths == set()


# ---------------- _format_wiki_writes_note ----------------


def test_format_wiki_writes_note_empty() -> None:
    assert al._format_wiki_writes_note([]) == ""


def test_format_wiki_writes_note_single() -> None:
    out = al._format_wiki_writes_note(["docs/wiki/findings/a.md"])
    assert out == "wiki_writes=docs/wiki/findings/a.md"


def test_format_wiki_writes_note_at_cap() -> None:
    paths = [f"docs/wiki/x{i}.md" for i in range(5)]
    out = al._format_wiki_writes_note(paths)
    assert out.count(",") == 4
    assert "+more" not in out


def test_format_wiki_writes_note_over_cap() -> None:
    paths = [f"docs/wiki/x{i}.md" for i in range(8)]
    out = al._format_wiki_writes_note(paths)
    # Keeps first 5 + collapses tail
    assert "+3-more" in out
    assert "x0.md" in out and "x4.md" in out
    assert "x7.md" not in out


# ---------------- _run_one_cycle reorder + audit ----------------


def test_run_one_cycle_calls_cycle_runner_before_writing_row(tmp_path: Path) -> None:
    """7.6 reorder: cycle_runner runs BEFORE the cycle-log row is appended,
    so wiki_graph + gap_search auto-files land in the wiki_writes delta."""
    pdir = _build_wiki_with_problems(
        tmp_path,
        [
            dict(problem_id=1, slug="alpha", tier="S", status="open", score=1.5),
        ],
    )
    log = tmp_path / "cycle-log.md"
    log.write_text("## Cycles\n\n| # | problem |\n|---|---|\n")

    order: list[str] = []

    def runner(cid: int, slug: str) -> int:
        # When cycle_runner fires, no row should exist yet for this cycle_id
        order.append(f"runner({cid})")
        assert f"| {cid} |" not in log.read_text()
        return 0

    al.run_one_problem(
        problems_dir=pdir,
        cycle_log=log,
        dry_run=False,
        cycle_runner=runner,
    )
    assert order == ["runner(0)"]
    # And the row is present after the function returns
    assert "P1-alpha" in log.read_text()


def test_run_one_cycle_appends_wiki_writes_to_notes(tmp_path: Path) -> None:
    """When the snapshot delta is non-empty, notes get a `wiki_writes=…` suffix."""
    pdir = _build_wiki_with_problems(
        tmp_path,
        [
            dict(problem_id=1, slug="alpha", tier="S", status="open", score=1.5),
        ],
    )
    log = tmp_path / "cycle-log.md"
    log.write_text("## Cycles\n\n| # | problem |\n|---|---|\n")

    # First snapshot empty; second snapshot has two new paths → delta = both
    snapshots = iter(
        [
            set(),
            {"docs/wiki/findings/dead-end-x.md", "docs/wiki/questions/2026-05-24-y.md"},
        ]
    )
    with patch.object(
        al, "_snapshot_wiki_mb_paths", side_effect=lambda *_a, **_kw: next(snapshots)
    ):
        al.run_one_problem(
            problems_dir=pdir,
            cycle_log=log,
            dry_run=False,
            cycle_runner=lambda *_a: 0,
        )
    text = log.read_text()
    assert "wiki_writes=" in text
    assert "dead-end-x.md" in text
    assert "questions/2026-05-24-y.md" in text


def test_run_one_cycle_leaves_notes_clean_when_delta_empty(tmp_path: Path) -> None:
    pdir = _build_wiki_with_problems(
        tmp_path,
        [
            dict(problem_id=1, slug="alpha", tier="S", status="open", score=1.5),
        ],
    )
    log = tmp_path / "cycle-log.md"
    log.write_text("## Cycles\n\n| # | problem |\n|---|---|\n")

    # Both snapshots identical → delta = empty
    with patch.object(al, "_snapshot_wiki_mb_paths", return_value={"docs/wiki/existing.md"}):
        al.run_one_problem(
            problems_dir=pdir,
            cycle_log=log,
            dry_run=False,
            cycle_runner=lambda *_a: 0,
        )
    assert "wiki_writes=" not in log.read_text()


def test_run_one_cycle_dry_run_skips_audit_snapshot(tmp_path: Path) -> None:
    """dry_run mode never calls _snapshot_wiki_mb_paths."""
    pdir = _build_wiki_with_problems(
        tmp_path,
        [
            dict(problem_id=1, slug="alpha", tier="S", status="open", score=1.5),
        ],
    )
    log = tmp_path / "cycle-log.md"
    log.write_text("## Cycles\n\n| # | problem |\n|---|---|\n")
    pre = log.read_text()

    with patch.object(
        al, "_snapshot_wiki_mb_paths", side_effect=AssertionError("should not be called")
    ):
        al.run_one_problem(
            problems_dir=pdir,
            cycle_log=log,
            dry_run=True,
            cycle_runner=None,
        )
    assert log.read_text() == pre


# ============================================================================
# Goal 7.7 — LLM-path wiring inside inner_attempt + P14 smoke
# ============================================================================


def _make_llm_seams(
    *,
    strategy="rotation-lottery",
    score=2.5,
    payload=None,
    dead_end_finding=None,
    new_questions=(),
    wiki_writes=(),
    converged=False,
    notes_text="agent ran rotation-lottery",
):
    """Build the three function-shaped test seams + a parsed-response stub
    used by the LLM-path tests below."""
    from types import SimpleNamespace

    fake_response = SimpleNamespace(
        strategy=strategy,
        score=score,
        payload=payload,
        dead_end_finding=dead_end_finding,
        new_questions=list(new_questions),
        wiki_writes=list(wiki_writes),
        converged=converged,
        notes=notes_text,
    )
    fake_run_result = SimpleNamespace(
        ok=True,
        stdout='{"strategy":"...","..."}',
        stderr="",
        returncode=0,
        error_kind="",
        error_message="",
    )
    rendered_prompts: list[str] = []

    def fake_renderer(**kw):
        rendered_prompts.append(f"P{kw['problem_id']}/{kw['attempt_index']}")
        return rendered_prompts[-1]

    runner_calls: list[dict] = []

    def fake_runner(prompt, **kw):
        runner_calls.append({"prompt": prompt, **kw})
        return fake_run_result

    parser_calls: list[str] = []

    def fake_parser(text):
        parser_calls.append(text)
        return fake_response

    recorder_calls: list[dict] = []

    def fake_recorder(path, **kw):
        recorder_calls.append({"path": path, **kw})
        return None

    return {
        "renderer": fake_renderer,
        "runner": fake_runner,
        "parser": fake_parser,
        "recorder": fake_recorder,
        "rendered_prompts": rendered_prompts,
        "runner_calls": runner_calls,
        "parser_calls": parser_calls,
        "recorder_calls": recorder_calls,
    }


def test_inner_attempt_llm_path_happy(tmp_path: Path) -> None:
    """llm_enabled=True + working seams → LLM result threaded into cycle-log row."""
    problem = al.Problem(
        problem_id=14,
        slug="circle-packing-square",
        tier="A",
        status="rank-2-frozen",
        score_current=2.636,
        path=tmp_path,
    )
    seams = _make_llm_seams(
        strategy="basin-hopping",
        score=2.635,
        payload={"radii": [0.1]},
        converged=False,
        notes_text="basin-hop +0.001",
    )
    submit_calls: list = []

    def fake_submit(problem_id, payload, score, *, triple_verify, **kw):
        submit_calls.append(
            {
                "problem_id": problem_id,
                "score": score,
                "tv_passed": triple_verify.get("passed"),
            }
        )
        from types import SimpleNamespace

        return SimpleNamespace(submitted=False, rejected_at_gate="triple-verify-failed")

    result = al.inner_attempt(
        problem,
        dry_run=False,
        llm_enabled=True,
        prompt_renderer=seams["renderer"],
        headless_runner=seams["runner"],
        response_parser=seams["parser"],
        budget_recorder=seams["recorder"],
        auto_submitter=fake_submit,
        budget_path=tmp_path / "budget.md",
    )
    # Prompt rendered for P14, attempt 1
    assert seams["rendered_prompts"] == ["P14/1"]
    # Claude headless got the prompt + the autonomous-loop tool allow-list
    assert len(seams["runner_calls"]) == 1
    rc = seams["runner_calls"][0]
    assert "Bash(qmd:*)" in rc["allowed_tools"]
    assert "Task" in rc["allowed_tools"]
    # Parser received stdout
    assert seams["parser_calls"] == ['{"strategy":"...","..."}']
    # Budget ledger updated with positive estimates
    assert len(seams["recorder_calls"]) == 1
    assert seams["recorder_calls"][0]["input_tokens"] > 0
    # Result reflects LLM strategy + auto_submit gate (rejected at TV)
    assert result["chosen_techniques"] == ["basin-hopping"]
    assert result["compute"] == "local-cpu+llm"
    assert result["outcome"] == "improved-local"  # 2.635 < 2.636
    assert "llm-strategy=basin-hopping" in result["notes"]
    assert "agent=basin-hop +0.001" in result["notes"]
    # auto_submit got the LLM's score+payload with passed=False (per A3 wiring)
    assert len(submit_calls) == 1
    assert submit_calls[0]["score"] == 2.635
    assert submit_calls[0]["tv_passed"] is False
    assert "auto-submit-rejected@triple-verify-failed" in result["notes"]


def test_inner_attempt_llm_dead_end(tmp_path: Path) -> None:
    problem = al.Problem(
        problem_id=14,
        slug="circle-packing-square",
        tier="A",
        status="rank-2-frozen",
        score_current=2.636,
        path=tmp_path,
    )
    seams = _make_llm_seams(
        strategy="hexagonal-tiling",
        score=None,
        payload=None,
        dead_end_finding="docs/wiki/findings/dead-end-hexagonal-tiling.md",
    )
    result = al.inner_attempt(
        problem,
        dry_run=False,
        llm_enabled=True,
        prompt_renderer=seams["renderer"],
        headless_runner=seams["runner"],
        response_parser=seams["parser"],
        budget_recorder=seams["recorder"],
        budget_path=tmp_path / "budget.md",
    )
    assert result["outcome"] == "dead-end"
    assert result["findings_added"] == 1
    assert "dead_end=docs/wiki/findings/dead-end-hexagonal-tiling.md" in result["notes"]


def test_inner_attempt_llm_converged_overrides_score(tmp_path: Path) -> None:
    problem = al.Problem(
        problem_id=14,
        slug="circle-packing-square",
        tier="A",
        status="rank-2-frozen",
        score_current=2.636,
        path=tmp_path,
    )
    # Even with improvement, `converged=True` from the agent stops the loop.
    seams = _make_llm_seams(
        strategy="cma-es",
        score=2.620,
        payload={"x": 1},
        converged=True,
    )
    result = al.inner_attempt(
        problem,
        dry_run=False,
        llm_enabled=True,
        prompt_renderer=seams["renderer"],
        headless_runner=seams["runner"],
        response_parser=seams["parser"],
        budget_recorder=seams["recorder"],
        budget_path=tmp_path / "budget.md",
    )
    # Outcome priority: converged > improvement
    assert result["outcome"] == "converged"


def test_inner_attempt_llm_falls_back_when_claude_unavailable(tmp_path: Path) -> None:
    problem = al.Problem(
        problem_id=14,
        slug="circle-packing-square",
        tier="A",
        status="rank-2-frozen",
        score_current=2.636,
        path=tmp_path,
    )
    from types import SimpleNamespace

    def unavailable_runner(prompt, **kw):
        return SimpleNamespace(
            ok=False,
            stdout="",
            stderr="",
            error_kind="unavailable",
            error_message="Claude Code unavailable: auth/session-limit",
        )

    seams = _make_llm_seams()
    seams["runner"] = unavailable_runner

    result = al.inner_attempt(
        problem,
        dry_run=False,
        llm_enabled=True,
        prompt_renderer=seams["renderer"],
        headless_runner=unavailable_runner,
        response_parser=seams["parser"],
        budget_recorder=seams["recorder"],
        budget_path=tmp_path / "budget.md",
    )
    # Mechanical fallback ran — outcome from mechanical, not LLM
    assert result["compute"] != "local-cpu+llm"
    assert "llm-strategy=" not in result["notes"]


def test_inner_attempt_llm_falls_back_on_parse_error(tmp_path: Path) -> None:
    problem = al.Problem(
        problem_id=14,
        slug="circle-packing-square",
        tier="A",
        status="rank-2-frozen",
        score_current=2.636,
        path=tmp_path,
    )
    seams = _make_llm_seams()

    def bad_parser(_text):
        raise ValueError("malformed JSON")

    result = al.inner_attempt(
        problem,
        dry_run=False,
        llm_enabled=True,
        prompt_renderer=seams["renderer"],
        headless_runner=seams["runner"],
        response_parser=bad_parser,
        budget_recorder=seams["recorder"],
        budget_path=tmp_path / "budget.md",
    )
    assert result["compute"] != "local-cpu+llm"
    assert "llm-strategy=" not in result["notes"]


def test_inner_attempt_llm_disabled_skips_llm_components(tmp_path: Path) -> None:
    """llm_enabled=False: LLM seams must NOT be touched."""
    problem = al.Problem(
        problem_id=14,
        slug="circle-packing-square",
        tier="A",
        status="rank-2-frozen",
        score_current=2.636,
        path=tmp_path,
    )

    def boom(*_a, **_kw):
        raise AssertionError("LLM seam called despite llm_enabled=False")

    al.inner_attempt(
        problem,
        dry_run=False,
        llm_enabled=False,
        prompt_renderer=boom,
        headless_runner=boom,
        response_parser=boom,
        budget_recorder=boom,
    )


def test_inner_attempt_dry_run_skips_llm(tmp_path: Path) -> None:
    """dry_run=True bypasses LLM even when llm_enabled=True."""
    problem = al.Problem(
        problem_id=14,
        slug="circle-packing-square",
        tier="A",
        status="rank-2-frozen",
        score_current=2.636,
        path=tmp_path,
    )

    def boom(*_a, **_kw):
        raise AssertionError("LLM seam called despite dry_run")

    al.inner_attempt(
        problem,
        dry_run=True,
        llm_enabled=True,
        prompt_renderer=boom,
        headless_runner=boom,
        response_parser=boom,
        budget_recorder=boom,
    )


def test_run_one_visit_threads_llm_enabled_from_precheck(tmp_path: Path) -> None:
    """When precheck returns llm_enabled=True, run_one_visit must thread True
    into inner_attempt (so the LLM path is reached)."""
    pdir = _build_wiki_with_problems(
        tmp_path,
        [
            dict(
                problem_id=14,
                slug="circle-packing-square",
                tier="A",
                status="rank-2-frozen",
                score=2.6,
            ),
        ],
    )
    log = tmp_path / "cycle-log.md"
    log.write_text("## Cycles\n\n| # | problem |\n|---|---|\n")
    problem = next(p for p in al.load_problems(pdir) if p.problem_id == 14)

    from types import SimpleNamespace

    fake_decision = SimpleNamespace(
        action="proceed",
        reason="",
        llm_enabled=True,
    )

    seen_llm_flag: list[bool] = []
    real_inner = al.inner_attempt

    def spy_inner(p, **kw):
        seen_llm_flag.append(kw.get("llm_enabled"))
        # Suppress real LLM seams by forcing mechanical via dry_run-like
        # behavior: pass an unavailable headless_runner that surfaces "skip".
        kw["headless_runner"] = lambda *_a, **_kw: SimpleNamespace(
            ok=False,
            error_kind="unavailable",
            error_message="test",
            stdout="",
            stderr="",
            returncode=0,
        )
        kw["prompt_renderer"] = lambda **_kw: "prompt"
        kw["response_parser"] = lambda _t: None
        kw["budget_recorder"] = lambda *_a, **_kw: None
        return real_inner(p, **kw)

    with (
        patch.object(al.inner_agent_gates, "precheck", return_value=fake_decision),
        patch.object(al, "inner_attempt", side_effect=spy_inner),
    ):
        al.run_one_visit(
            problem,
            cycle_log=log,
            dry_run=False,
            cycle_runner=lambda *_a: 0,
            max_attempts=1,
        )
    assert seen_llm_flag and seen_llm_flag[0] is True


def test_run_one_visit_explicit_llm_enabled_overrides_precheck(tmp_path: Path) -> None:
    """Caller-explicit llm_enabled wins over precheck."""
    pdir = _build_wiki_with_problems(
        tmp_path,
        [
            dict(problem_id=1, slug="alpha", tier="S", status="open", score=1.5),
        ],
    )
    log = tmp_path / "cycle-log.md"
    log.write_text("## Cycles\n\n| # | problem |\n|---|---|\n")
    problem = al.load_problems(pdir)[0]

    from types import SimpleNamespace

    fake_decision = SimpleNamespace(
        action="proceed",
        reason="",
        llm_enabled=True,
    )
    seen: list[bool] = []

    def spy_inner(p, **kw):
        seen.append(kw.get("llm_enabled"))
        return {
            "start_score": 1.5,
            "end_score": 1.5,
            "hours": 0.0,
            "compute": "local-cpu",
            "wiki_citations": 0,
            "findings_added": 0,
            "concepts_added": 0,
            "author_mix": {"agent": 1, "human": 0, "hybrid": 0},
            "outcome": "no-change",
            "notes": "stub",
            "chosen_techniques": [],
        }

    with (
        patch.object(al.inner_agent_gates, "precheck", return_value=fake_decision),
        patch.object(al, "inner_attempt", side_effect=spy_inner),
    ):
        al.run_one_visit(
            problem,
            cycle_log=log,
            dry_run=False,
            cycle_runner=lambda *_a: 0,
            max_attempts=1,
            llm_enabled=False,
        )
    assert seen and seen[0] is False


# ---------------- P14 end-to-end smoke ----------------


def test_p14_smoke_run_one_visit_with_mocked_llm(tmp_path: Path) -> None:
    """End-to-end smoke on P14 with mocked claude_headless: render →
    headless → parse → auto_submit (rejected at TV) → cycle-log row +
    wiki-writes delta + token-budget update."""
    pdir = _build_wiki_with_problems(
        tmp_path,
        [
            dict(
                problem_id=14,
                slug="circle-packing-square",
                tier="A",
                status="rank-2-frozen",
                score=2.636,
            ),
        ],
    )
    log = tmp_path / "cycle-log.md"
    log.write_text("## Cycles\n\n| # | problem |\n|---|---|\n")
    budget = tmp_path / "inner-agent-budget.md"
    problem = next(p for p in al.load_problems(pdir) if p.problem_id == 14)

    from types import SimpleNamespace

    fake_response = SimpleNamespace(
        strategy="cma-es-with-rotation-lottery",
        score=2.635,
        payload={"vectors": [[1, 0]]},
        dead_end_finding=None,
        new_questions=[],
        wiki_writes=[],
        converged=False,
        notes="cma-es +0.001 improvement",
    )
    fake_run = SimpleNamespace(
        ok=True,
        stdout="<json>",
        stderr="",
        returncode=0,
        error_kind="",
        error_message="",
    )
    submit_calls: list = []

    def fake_submit(problem_id, payload, score, *, triple_verify, **kw):
        submit_calls.append((problem_id, score, triple_verify.get("passed")))
        return SimpleNamespace(submitted=False, rejected_at_gate="triple-verify-failed")

    cycle_runner_calls: list = []

    def fake_runner(cid, slug):
        cycle_runner_calls.append((cid, slug))
        return 0

    with patch.object(
        al,
        "inner_attempt",
        side_effect=lambda p, **kw: al._try_llm_path(
            problem=p,
            attempt_index=kw.get("attempt_index", 1),
            avoid_techniques=kw.get("avoid_techniques"),
            auto_submitter=fake_submit,
            headless_runner=lambda prompt, **_kw: fake_run,
            prompt_renderer=lambda **_kw: "rendered-prompt",
            response_parser=lambda _t: fake_response,
            budget_recorder=al.inner_agent_gates.record_token_usage,
            budget_path=budget,
        ),
    ):
        results = al.run_one_visit(
            problem,
            cycle_log=log,
            dry_run=False,
            cycle_runner=fake_runner,
            max_attempts=1,
            skip_gates=True,
            llm_enabled=True,
        )

    # Exactly one cycle ran on P14
    assert len(results) == 1
    assert results[0].problem.problem_id == 14
    assert "improved-local" in log.read_text()  # 2.635 < 2.636
    assert "cma-es-with-rotation-lottery" in log.read_text()
    # cycle_runner.sh was invoked once
    assert len(cycle_runner_calls) == 1
    # auto_submit got the score+payload with passed=False (A3 wiring)
    assert submit_calls == [(14, 2.635, False)]
    # Budget ledger picked up the call
    assert budget.is_file()
    text = budget.read_text()
    assert "Inner-agent daily budget" in text
    # At least one cycle counted
    assert "| 1 |" in text or "| 2 |" in text or "cycles" in text


# ---------------- 7.8c: milestone notification wiring ----------------


def test_call_auto_submit_fires_notifier_on_submitted() -> None:
    """When auto_submit returns submitted=True, the notifier callback is
    invoked with the problem_id + score."""
    from types import SimpleNamespace

    problem = al.Problem(
        problem_id=14,
        slug="circle-packing-square",
        tier="A",
        status="rank-2-frozen",
        score_current=2.636,
        path=Path("/x"),
    )

    def fake_submit(problem_id, payload, score, *, triple_verify, **kw):
        return SimpleNamespace(submitted=True)

    notifier_calls: list = []

    def fake_notifier(*, problem_id, score, **kw):
        notifier_calls.append((problem_id, score))
        return True

    notes: list[str] = []
    outcome = al._call_auto_submit(
        problem=problem,
        score=2.635,
        payload={"x": 1},
        auto_submitter=fake_submit,
        notes_parts=notes,
        notifier=fake_notifier,
    )
    assert outcome == "improved-and-submitted"
    assert notifier_calls == [(14, 2.635)]
    assert "SUBMITTED" in " ".join(notes)


def test_call_auto_submit_does_not_fire_notifier_on_reject() -> None:
    from types import SimpleNamespace

    problem = al.Problem(
        problem_id=14,
        slug="circle-packing-square",
        tier="A",
        status="rank-2-frozen",
        score_current=2.636,
        path=Path("/x"),
    )

    def fake_submit(problem_id, payload, score, *, triple_verify, **kw):
        return SimpleNamespace(submitted=False, rejected_at_gate="triple-verify-failed")

    notifier_calls: list = []

    def fake_notifier(**kw):
        notifier_calls.append(kw)
        return True

    notes: list[str] = []
    outcome = al._call_auto_submit(
        problem=problem,
        score=2.635,
        payload={"x": 1},
        auto_submitter=fake_submit,
        notes_parts=notes,
        notifier=fake_notifier,
    )
    assert outcome is None
    assert notifier_calls == []
    assert "auto-submit-rejected@triple-verify-failed" in " ".join(notes)


def test_call_auto_submit_notifier_failure_is_silent() -> None:
    """Notifier raising/returning False must not break the call chain."""
    from types import SimpleNamespace

    problem = al.Problem(
        problem_id=14,
        slug="circle-packing-square",
        tier="A",
        status="rank-2-frozen",
        score_current=2.636,
        path=Path("/x"),
    )

    def fake_submit(problem_id, payload, score, *, triple_verify, **kw):
        return SimpleNamespace(submitted=True)

    def explosive_notifier(**kw):
        raise RuntimeError("notify daemon dead")

    notes: list[str] = []
    outcome = al._call_auto_submit(
        problem=problem,
        score=2.635,
        payload={"x": 1},
        auto_submitter=fake_submit,
        notes_parts=notes,
        notifier=explosive_notifier,
    )
    # Submission outcome wasn't affected by the notification failure
    assert outcome == "improved-and-submitted"
    assert "SUBMITTED" in " ".join(notes)


# ---------------- Goal 8: pre-cycle synthesis hook ----------------


def _make_problem() -> "al.Problem":
    return al.Problem(
        problem_id=14,
        slug="circle-packing-square",
        tier="A",
        status="rank-2-frozen",
        score_current=2.636,
        path=Path("/x"),
    )


def test_pre_cycle_synthesis_enabled_when_marker_present(tmp_path: Path) -> None:
    """The marker heading toggles synthesis on."""
    rule = tmp_path / "cycle-discipline.md"
    rule.write_text(
        f"# Cycle discipline\n\n{al.PRE_CYCLE_SYNTHESIS_MARKER}\n\nRun synthesis before claude.\n"
    )
    assert al._pre_cycle_synthesis_enabled(rule_path=rule) is True


def test_pre_cycle_synthesis_enabled_when_marker_absent(tmp_path: Path) -> None:
    """Vanilla cycle-discipline.md → off."""
    rule = tmp_path / "cycle-discipline.md"
    rule.write_text("# Cycle discipline\n\nEvery cycle gets logged.\n")
    assert al._pre_cycle_synthesis_enabled(rule_path=rule) is False


def test_pre_cycle_synthesis_enabled_missing_file_returns_false(tmp_path: Path) -> None:
    """Missing rule file → opt-in by design, returns False."""
    assert al._pre_cycle_synthesis_enabled(rule_path=tmp_path / "missing.md") is False


def test_run_pre_cycle_synthesis_returns_content_on_success(tmp_path: Path) -> None:
    """Successful subprocess + output file written → return its contents."""
    problem = _make_problem()
    # Stub runner pretends scripts/research_synthesis.py wrote the output file
    expected_output = (
        (DEFAULT_MB_DIR_FOR_TEST := al.DEFAULT_MB_DIR)
        / "problems"
        / problem.file_slug
        / "literature-synthesis-stub.md"
    )

    class _StubProc:
        returncode = 0
        stderr = ""

    written: dict = {}

    def fake_runner(cmd, **kwargs):
        # Extract the --output path the CLI would write to
        idx = cmd.index("--output")
        out_path = Path(cmd[idx + 1])
        written["path"] = out_path
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text("# Literature synthesis stub\n\n## Top sources\n- foo\n")
        return _StubProc()

    result = al._run_pre_cycle_synthesis(problem, runner=fake_runner)
    try:
        assert result is not None
        assert "## Top sources" in result
        assert "foo" in result
    finally:
        # cleanup test artifact (lives under real mb/)
        p = written.get("path")
        if p and p.exists():
            p.unlink()


def test_run_pre_cycle_synthesis_returns_none_on_nonzero_exit() -> None:
    """Subprocess fails → graceful None, no crash."""
    problem = _make_problem()

    class _StubProc:
        returncode = 2
        stderr = "boom"

    def fake_runner(cmd, **kwargs):
        return _StubProc()

    assert al._run_pre_cycle_synthesis(problem, runner=fake_runner) is None


def test_run_pre_cycle_synthesis_returns_none_when_output_missing() -> None:
    """Subprocess returns ok but doesn't write the file → graceful None."""
    problem = _make_problem()

    class _StubProc:
        returncode = 0
        stderr = ""

    def fake_runner(cmd, **kwargs):
        # Don't write the output file
        return _StubProc()

    assert al._run_pre_cycle_synthesis(problem, runner=fake_runner) is None


def test_run_pre_cycle_synthesis_returns_none_on_runner_exception() -> None:
    """Subprocess raising → graceful None, no crash."""
    problem = _make_problem()

    def fake_runner(cmd, **kwargs):
        raise RuntimeError("boom")

    assert al._run_pre_cycle_synthesis(problem, runner=fake_runner) is None


def test_synthesis_skips_terminal_status_problems(monkeypatch, tmp_path):
    """G10 improvement: synthesis is skipped for conquered/retired/hidden problems
    (no headroom), but runs for frozen problems (the branch's unlock thesis)."""
    # Enable the marker check
    monkeypatch.setattr(al, "_pre_cycle_synthesis_enabled", lambda: True)

    invoked: list[int] = []
    monkeypatch.setattr(
        al,
        "_run_pre_cycle_synthesis",
        lambda problem, **kw: invoked.append(problem.problem_id) or "synthesis-content",
    )

    def _p(status: str, pid: int) -> "al.Problem":
        return al.Problem(
            problem_id=pid, slug="x", tier="A", status=status, score_current=1.0, path=Path("/x")
        )

    # Verify the gate logic directly via the substring set
    for terminal in ("conquered", "retired", "hidden", "rank-2-conquered"):
        assert any(s in terminal.lower() for s in al.SYNTHESIS_SKIP_STATUS_SUBSTRINGS), terminal
    for live in ("rank-3-frozen", "frozen", "open", "rank-5-frozen-by-proximity-guard"):
        assert not any(s in live.lower() for s in al.SYNTHESIS_SKIP_STATUS_SUBSTRINGS), live


# ---------------- Goal 2: skill-bandit routing ----------------


def _p14_with_packing_lib(tmp_path: Path):
    """P14 (category=packing) + a two-arm packing skill-library. Returns
    (problem, library_path). Shared by the bandit routing tests."""
    pdir = _build_wiki_with_problems(
        tmp_path,
        [dict(problem_id=14, slug="circle-packing-square", tier="A", status="open", score=2.6)],
    )
    p14 = next(p for p in al.load_problems(pdir) if p.problem_id == 14)
    lib = tmp_path / "skill-library.md"
    lib.write_text(
        "| `tech-A` | packing | 5 | 2 | 1 | 2026-01-01 | 0.40 |\n"
        "| `tech-B` | packing | 3 | 1 | 2 | 2026-02-01 | 0.33 |\n"
    )
    return p14, lib


def test_bandit_flag_routes_through_sampler(tmp_path: Path, monkeypatch) -> None:
    """EINSTEIN_BANDIT=1 → inner_attempt picks via the Thompson bandit, not
    the manifest strategy_picker."""
    p14, lib = _p14_with_packing_lib(tmp_path)
    monkeypatch.setenv("EINSTEIN_BANDIT", "1")
    r = al.inner_attempt(p14, dry_run=True, skill_library=lib)
    assert "strategy=thompson-bandit" in r["notes"]
    assert "technique=" in r["notes"]  # Goal 4 audit note
    assert set(r["chosen_techniques"]) <= {"tech-A", "tech-B"}
    assert r["chosen_techniques"]  # non-empty — an arm matched


def test_default_unset_uses_manifest_dispatcher(tmp_path: Path, monkeypatch) -> None:
    """Flag unset → existing strategy_picker path, no bandit involvement."""
    p14, lib = _p14_with_packing_lib(tmp_path)
    monkeypatch.delenv("EINSTEIN_BANDIT", raising=False)
    r = al.inner_attempt(p14, dry_run=True, skill_library=lib)
    assert "thompson-bandit" not in r["notes"]
    assert "prior=" in r["notes"]  # strategy_picker rationale note
    assert r["chosen_techniques"]


def test_bandit_pick_is_deterministic(tmp_path: Path, monkeypatch) -> None:
    """Same problem + attempt → same seed → same bandit pick."""
    p14, lib = _p14_with_packing_lib(tmp_path)
    monkeypatch.setenv("EINSTEIN_BANDIT", "1")
    r1 = al.inner_attempt(p14, dry_run=True, skill_library=lib, attempt_index=1)
    r2 = al.inner_attempt(p14, dry_run=True, skill_library=lib, attempt_index=1)
    assert r1["chosen_techniques"] == r2["chosen_techniques"]


def test_bandit_honors_avoid_set(tmp_path: Path, monkeypatch) -> None:
    """Bandit path respects avoid_techniques (multi-attempt visits)."""
    p14, lib = _p14_with_packing_lib(tmp_path)
    monkeypatch.setenv("EINSTEIN_BANDIT", "1")
    r = al.inner_attempt(
        p14, dry_run=True, skill_library=lib, attempt_index=2, avoid_techniques={"tech-A"}
    )
    assert "tech-A" not in r["chosen_techniques"]
    assert r["chosen_techniques"] == ["tech-B"]


def test_bandit_no_arms_for_category_leaves_strategy_none(tmp_path: Path, monkeypatch) -> None:
    """Category with no matching arm → no pick, council-needed note."""
    pdir = _build_wiki_with_problems(
        tmp_path,
        [dict(problem_id=2, slug="autocorr", tier="A", status="open", score=1.0)],
    )
    p2 = next(p for p in al.load_problems(pdir) if p.problem_id == 2)  # category=autocorrelation
    lib = tmp_path / "skill-library.md"
    lib.write_text("| `tech-A` | packing | 5 | 2 | 1 | 2026-01-01 | 0.40 |\n")
    monkeypatch.setenv("EINSTEIN_BANDIT", "1")
    r = al.inner_attempt(p2, dry_run=True, skill_library=lib)
    assert r["chosen_techniques"] == []
    assert "no bandit arms" in r["notes"]


# ---------------- Goal 3: bandit skill-library learning loop ----------------


def test_bandit_skill_update_bumps_chosen_techniques(tmp_path: Path) -> None:
    lib = tmp_path / "skill-library.md"
    lib.write_text("| `tech-A` | packing | 4 | 2 | 1 | 2026-01-01 | 0.50 |\n")
    ledger = tmp_path / "ledger.tsv"
    result = {"chosen_techniques": ["tech-A"], "outcome": "improved-local"}
    out = al._bandit_skill_update(result, 5, skill_library=lib, ledger_path=ledger)
    assert len(out) == 1 and out[0].applied
    assert out[0].tried == 5 and out[0].top3 == 3  # reward outcome bumps top3


def test_bandit_skill_update_no_reward_outcome(tmp_path: Path) -> None:
    lib = tmp_path / "skill-library.md"
    lib.write_text("| `tech-A` | packing | 4 | 2 | 1 | 2026-01-01 | 0.50 |\n")
    ledger = tmp_path / "ledger.tsv"
    result = {"chosen_techniques": ["tech-A"], "outcome": "no-change"}
    out = al._bandit_skill_update(result, 6, skill_library=lib, ledger_path=ledger)
    assert out[0].tried == 5 and out[0].top3 == 2  # tried bumps, top3 does not


def test_bandit_skill_update_idempotent(tmp_path: Path) -> None:
    lib = tmp_path / "skill-library.md"
    lib.write_text("| `tech-A` | packing | 4 | 2 | 1 | 2026-01-01 | 0.50 |\n")
    ledger = tmp_path / "ledger.tsv"
    result = {"chosen_techniques": ["tech-A"], "outcome": "improved-local"}
    al._bandit_skill_update(result, 9, skill_library=lib, ledger_path=ledger)
    snapshot = lib.read_text()
    again = al._bandit_skill_update(result, 9, skill_library=lib, ledger_path=ledger)
    assert not again[0].applied
    assert lib.read_text() == snapshot


def test_bandit_skill_update_empty_techniques(tmp_path: Path) -> None:
    lib = tmp_path / "skill-library.md"
    lib.write_text("| `tech-A` | packing | 4 | 2 | 1 | 2026-01-01 | 0.50 |\n")
    out = al._bandit_skill_update(
        {"chosen_techniques": [], "outcome": "no-change"}, 1, skill_library=lib
    )
    assert out == []


# ---------------- Goal 4: bandit choice audit note ----------------


def test_bandit_note_carries_prior_and_theta(tmp_path: Path, monkeypatch) -> None:
    """The cycle-log note must let a reader reconstruct the pick:
    `technique=… prior=Beta(a,b) sampled_θ=…`."""
    import re

    p14, lib = _p14_with_packing_lib(tmp_path)
    monkeypatch.setenv("EINSTEIN_BANDIT", "1")
    r = al.inner_attempt(p14, dry_run=True, skill_library=lib)
    notes = r["notes"]
    # full audit triplet present and well-formed
    m = re.search(r"technique=(\S+) prior=Beta\((\d+),(\d+)\) sampled_θ=([01]\.\d+)", notes)
    assert m is not None, notes
    assert m.group(1) in {"tech-A", "tech-B"}
    # tech-A is Beta(2+1, (5-2)+1)=Beta(3,4); tech-B is Beta(1+1,(3-1)+1)=Beta(2,3)
    assert (m.group(2), m.group(3)) in {("3", "4"), ("2", "3")}
    theta = float(m.group(4))
    assert 0.0 <= theta <= 1.0
