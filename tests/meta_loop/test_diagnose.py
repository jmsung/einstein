"""Tests for src/einstein/meta_loop/diagnose.py — Goal 1 diagnostic."""

from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein.meta_loop import diagnose  # noqa: E402

UTC = dt.timezone.utc


# ---------------- fixtures ----------------


def _write_cycle_log(path: Path, *, with_p14_regression: bool = True) -> None:
    """Write a minimal cycle-log.md that exercises the patterns we care about.

    Includes the real P14 cycle 49–51 case (notes mention manifest-blocker
    + strict-tol) when with_p14_regression=True.
    """
    rows = [
        # cycle 1: real Δ — should NOT trigger stagnation
        (
            "1",
            "P19",
            "2.6 → 2.7",
            "1",
            "local-cpu",
            "5",
            "1",
            "0",
            "a:1/h:0",
            "improved",
            "made a real change",
        ),
        # cycles 2–4: P5 strategy-only, no Δ — stagnation but no dead-end (not flagged)
        (
            "2",
            "P5",
            "12.88 (no Δ)",
            "0",
            "none-strategy-only",
            "0",
            "0",
            "0",
            "a:1/h:0",
            "strategy-picked-no-execution",
            "cold scaffold",
        ),
        (
            "3",
            "P5",
            "12.88 (no Δ)",
            "0",
            "none-strategy-only",
            "0",
            "0",
            "0",
            "a:1/h:0",
            "strategy-picked-no-execution",
            "cold scaffold",
        ),
        (
            "4",
            "P5",
            "12.88 (no Δ)",
            "0",
            "none-strategy-only",
            "0",
            "0",
            "0",
            "a:1/h:0",
            "strategy-picked-no-execution",
            "cold scaffold",
        ),
    ]
    if with_p14_regression:
        # cycles 49–51: the real P14 regression — manifest blocker + strict-tol
        rows.extend(
            [
                (
                    "49",
                    "P14-circle-packing-square",
                    "2.6359 (no Δ)",
                    "0",
                    "local-cpu+llm",
                    "0",
                    "1",
                    "0",
                    "a:1/h:0",
                    "dead-end",
                    "manifest only exposes newton_max (strict-tol-failing per exp log); "
                    "mpmath-ulp-polish picked novel but unwired",
                ),
                (
                    "50",
                    "P14-circle-packing-square",
                    "2.6359 (no Δ)",
                    "0",
                    "local-cpu+llm",
                    "0",
                    "1",
                    "0",
                    "a:1/h:0",
                    "converged",
                    "P14 rank-2-frozen at float64 ceiling AND manifest-blocked "
                    "(default=newton_max is strict-tol-unsafe per cycle-49 finding)",
                ),
                (
                    "51",
                    "P14-circle-packing-square",
                    "2.6359 (no Δ)",
                    "0",
                    "local-cpu+llm",
                    "0",
                    "1",
                    "0",
                    "a:1/h:0",
                    "converged",
                    "cycle 50 manifest-wire-fix question filed",
                ),
            ]
        )

    header = (
        "# Cycle log — append-only\n\n"
        "## Cycles\n\n"
        "| # | problem | start → end score | hours | compute | wiki cites "
        "| findings+ | concepts+ | author mix | outcome | notes |\n"
        "|---|---|---|---|---|---|---|---|---|---|---|\n"
    )
    body = "".join("| " + " | ".join(r) + " |\n" for r in rows)
    path.write_text(header + body)


def _write_skill_library(path: Path) -> None:
    """Skill-library with one promote, one demote, one watchlist, one meta."""
    text = (
        "# Skill library\n\n"
        "| technique | category | tried | top3 | finding | last_used | hit_rate |\n"
        "|---|---|---|---|---|---|---|\n"
        "| `slsqp-active-pair-polish.md` | packing | 6 | 4 | 1 | 2026-04-12 | 0.67 |\n"
        "| `kronecker-search-decomposition.md` | discrete-combinatorics | 5 | 0 | 2 "
        "| 2026-05-02 | 0.00 |\n"
        "| `new-toy.md` | exploration | 1 | 0 | 0 | 2026-05-01 | 0.00 |\n"
        "| `gpu-decision-framework.md` | meta | 5 | (meta) | 2 | 2026-04-25 | (n/a) |\n"
    )
    path.write_text(text)


def _write_finding(path: Path, *, drafted: str, content: str = "body") -> None:
    path.write_text(f"---\ntype: finding\nauthor: agent\ndrafted: {drafted}\n---\n\n{content}\n")


def _write_question(path: Path, *, status: str) -> None:
    path.write_text(
        f"---\ntype: question\nauthor: agent\ndrafted: 2026-05-01\nstatus: {status}\n---\n\nbody\n"
    )


# ---------------- parsers ----------------


def test_parse_cycle_log_skips_header_and_picks_up_rows(tmp_path: Path) -> None:
    log = tmp_path / "cycle-log.md"
    _write_cycle_log(log)
    rows = diagnose.parse_cycle_log(log)
    # 4 baseline + 3 P14 = 7
    assert len(rows) == 7
    assert rows[0].cycle_id == 1
    assert rows[0].problem == "P19"
    assert rows[-1].cycle_id == 51


def test_parse_cycle_log_handles_missing_file(tmp_path: Path) -> None:
    assert diagnose.parse_cycle_log(tmp_path / "nope.md") == []


def test_score_changed_detection() -> None:
    # Direct CycleRow construction — exercise the property
    r_changed = diagnose.CycleRow(
        cycle_id=1,
        problem="P1",
        score_field="0.1 → 0.2",
        hours="0",
        compute="local",
        wiki_citations="0",
        findings_added="0",
        concepts_added="0",
        author_mix="a:1/h:0",
        outcome="improved",
        notes="",
    )
    r_same = diagnose.CycleRow(
        cycle_id=2,
        problem="P1",
        score_field="0.1 → 0.1",
        hours="0",
        compute="local",
        wiki_citations="0",
        findings_added="0",
        concepts_added="0",
        author_mix="a:1/h:0",
        outcome="no-change",
        notes="",
    )
    r_unparseable = diagnose.CycleRow(
        cycle_id=3,
        problem="P1",
        score_field="12.88 (no Δ)",
        hours="0",
        compute="local",
        wiki_citations="0",
        findings_added="0",
        concepts_added="0",
        author_mix="a:1/h:0",
        outcome="strategy-picked-no-execution",
        notes="",
    )
    assert r_changed.score_changed is True
    assert r_same.score_changed is False
    assert r_unparseable.score_changed is False


def test_parse_skill_library(tmp_path: Path) -> None:
    skl = tmp_path / "skill-library.md"
    _write_skill_library(skl)
    rows = diagnose.parse_skill_library(skl)
    techniques = {r.technique: r for r in rows}
    assert "slsqp-active-pair-polish.md" in techniques
    assert techniques["slsqp-active-pair-polish.md"].tried == 6
    # meta row preserved
    assert "gpu-decision-framework.md" in techniques
    assert techniques["gpu-decision-framework.md"].hit_rate == "(n/a)"


# ---------------- pattern detectors ----------------


def test_detect_stagnations_finds_p14_run(tmp_path: Path) -> None:
    log = tmp_path / "cycle-log.md"
    _write_cycle_log(log)
    stagnations = diagnose.detect_stagnations(diagnose.parse_cycle_log(log))
    # P5 run (cycles 2-4) AND P14 run (cycles 49-51) — both length 3, no Δ
    by_problem = {s.problem: s for s in stagnations}
    assert "P14-circle-packing-square" in by_problem
    assert by_problem["P14-circle-packing-square"].cycle_ids == [49, 50, 51]
    assert "P5" in by_problem


def test_p14_stagnation_is_flagged_but_p5_is_not(tmp_path: Path) -> None:
    """P14 has dead-end + converged — flagged. P5 is cold scaffold — not flagged."""
    log = tmp_path / "cycle-log.md"
    _write_cycle_log(log)
    stagnations = diagnose.detect_stagnations(diagnose.parse_cycle_log(log))
    by_problem = {s.problem: s for s in stagnations}
    assert by_problem["P14-circle-packing-square"].is_flagged()
    assert not by_problem["P5"].is_flagged()


def test_detect_manifest_regressions_surfaces_p14_cycles_49_51(tmp_path: Path) -> None:
    """The headline test — Goal 1 sign-off: P14 cycle 49–51 must surface."""
    log = tmp_path / "cycle-log.md"
    _write_cycle_log(log)
    regressions = diagnose.detect_manifest_regressions(diagnose.parse_cycle_log(log))
    cycle_ids = {r.cycle_id for r in regressions}
    assert 49 in cycle_ids
    assert 50 in cycle_ids
    # Cycle 51's notes do mention "manifest-wire-fix", so it should also surface
    assert 51 in cycle_ids
    # All matches are on the P14 problem
    assert {r.problem for r in regressions} == {"P14-circle-packing-square"}


def test_no_manifest_regression_when_absent(tmp_path: Path) -> None:
    log = tmp_path / "cycle-log.md"
    _write_cycle_log(log, with_p14_regression=False)
    regressions = diagnose.detect_manifest_regressions(diagnose.parse_cycle_log(log))
    assert regressions == []


# ---------------- technique heat map ----------------


def test_rank_techniques_buckets(tmp_path: Path) -> None:
    skl = tmp_path / "skill-library.md"
    _write_skill_library(skl)
    ranks = {t.technique: t for t in diagnose.rank_techniques(diagnose.parse_skill_library(skl))}
    assert ranks["slsqp-active-pair-polish.md"].bucket == "promote"
    assert ranks["kronecker-search-decomposition.md"].bucket == "demote"
    assert ranks["new-toy.md"].bucket == "watchlist"
    assert ranks["gpu-decision-framework.md"].bucket == "meta"


# ---------------- wiki counts ----------------


def test_count_wiki_recent_window(tmp_path: Path) -> None:
    findings = tmp_path / "findings"
    findings.mkdir()
    _write_finding(findings / "old.md", drafted="2025-01-01")
    _write_finding(findings / "dead-end-foo.md", drafted="2026-05-20")
    _write_finding(findings / "dead-end-bar.md", drafted="2026-05-24")
    questions = tmp_path / "questions"
    questions.mkdir()
    _write_question(questions / "q1.md", status="open")
    _write_question(questions / "q2.md", status="answered")
    _write_question(questions / "q3.md", status="open")

    counts = diagnose.count_wiki(findings, questions, now=dt.date(2026, 5, 25))
    assert counts.findings_total == 3
    assert counts.dead_ends_total == 2
    assert counts.findings_recent == 2  # only the two dead-ends fall in last 30d
    assert counts.questions_open == 2
    assert counts.questions_answered == 1
    assert counts.questions_total == 3


def test_count_wiki_handles_missing_dirs(tmp_path: Path) -> None:
    counts = diagnose.count_wiki(
        tmp_path / "no-findings",
        tmp_path / "no-questions",
        now=dt.date(2026, 5, 25),
    )
    assert counts.findings_total == 0
    assert counts.questions_total == 0


# ---------------- run() integration + report ----------------


@pytest.fixture
def sample_repo(tmp_path: Path) -> dict[str, Path]:
    cycle_log = tmp_path / "agent" / "cycle-log.md"
    skill_library = tmp_path / "agent" / "skill-library.md"
    findings_dir = tmp_path / "wiki" / "findings"
    questions_dir = tmp_path / "wiki" / "questions"
    for d in (cycle_log.parent, findings_dir, questions_dir):
        d.mkdir(parents=True, exist_ok=True)
    _write_cycle_log(cycle_log)
    _write_skill_library(skill_library)
    _write_finding(findings_dir / "dead-end-foo.md", drafted="2026-05-24")
    _write_question(questions_dir / "q1.md", status="open")
    return {
        "cycle_log": cycle_log,
        "skill_library": skill_library,
        "findings_dir": findings_dir,
        "questions_dir": questions_dir,
        "output": tmp_path / "logs" / "meta-loop-report.md",
    }


def test_run_writes_report_and_surfaces_p14(sample_repo: dict[str, Path]) -> None:
    """End-to-end: report file exists, mentions P14 manifest regression, and
    has a Surfaced regressions section."""
    report = diagnose.run(
        cycle_log=sample_repo["cycle_log"],
        skill_library=sample_repo["skill_library"],
        findings_dir=sample_repo["findings_dir"],
        questions_dir=sample_repo["questions_dir"],
        output=sample_repo["output"],
        now=dt.datetime(2026, 5, 25, 12, 0, 0, tzinfo=UTC),
    )
    text = sample_repo["output"].read_text()
    # Section headers present
    assert "## Cycles summary" in text
    assert "## Surfaced regressions" in text
    assert "## Stagnation patterns" in text
    assert "## Technique heat map" in text
    assert "## Wiki state" in text
    # P14 must appear in the regressions section
    assert "P14-circle-packing-square" in text
    # The cycle IDs from the regression must appear
    assert "| 49 |" in text or " 49 " in text
    # The matched token (strict-tol or manifest) must appear
    assert "strict-tol" in text or "manifest" in text
    # Report object is consistent
    assert report.cycles_total == 7
    assert any(r.cycle_id == 49 for r in report.manifest_regressions)


def test_run_renders_outcome_counter(sample_repo: dict[str, Path]) -> None:
    report = diagnose.run(
        cycle_log=sample_repo["cycle_log"],
        skill_library=sample_repo["skill_library"],
        findings_dir=sample_repo["findings_dir"],
        questions_dir=sample_repo["questions_dir"],
        output=sample_repo["output"],
        now=dt.datetime(2026, 5, 25, 12, 0, 0, tzinfo=UTC),
    )
    # strategy-picked-no-execution appears 3× in the fixture
    assert report.outcome_counts["strategy-picked-no-execution"] == 3
    assert report.outcome_counts["dead-end"] == 1
    assert report.outcome_counts["converged"] == 2
