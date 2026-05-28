"""Tests for docs/tools/gap_search.py — staleness + diagnostic report (Goal 5 of
js/feat/research-synthesis).

Existing arxiv/enrichment paths are not unit-tested here (they shell out to the
public API). This file covers the staleness filter + report writer added in G5.
"""

from __future__ import annotations

import io
import sys
import textwrap
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "docs" / "tools"))

import gap_search as gs  # noqa: E402

# ---------------- cycles_since (git wrapper) ----------------


def test_cycles_since_invokes_correct_git_command(tmp_path: Path) -> None:
    """git log --since=<date> --format=%H -- <cycle_log_path>"""
    seen: dict = {}

    def runner(cmd, cwd):
        seen["cmd"] = list(cmd)
        seen["cwd"] = cwd
        return ""

    gs.cycles_since(tmp_path / "cycle-log.md", since_iso_date="2026-05-20", runner=runner)
    assert seen["cmd"][:3] == ["git", "log", "--since=2026-05-20"]
    assert "--format=%H" in seen["cmd"]
    assert seen["cmd"][-1] == str(tmp_path / "cycle-log.md")


def test_cycles_since_counts_commit_hashes() -> None:
    """Each non-empty line is one commit; empty output is 0."""

    def runner_three(cmd, cwd):
        return "aaa\nbbb\nccc\n"

    def runner_empty(cmd, cwd):
        return ""

    assert gs.cycles_since(Path("/tmp/x"), since_iso_date="2026-05-20", runner=runner_three) == 3
    assert gs.cycles_since(Path("/tmp/x"), since_iso_date="2026-05-20", runner=runner_empty) == 0


def test_cycles_since_returns_zero_when_runner_raises() -> None:
    """Git missing or any subprocess failure → 0, never propagate."""

    def runner(cmd, cwd):
        raise FileNotFoundError("git not found")

    assert gs.cycles_since(Path("/tmp/x"), since_iso_date="2026-05-20", runner=runner) == 0


# ---------------- is_stale ----------------


def _write_question(
    path: Path,
    *,
    drafted: str = "2026-05-20",
    status: str = "open",
    has_suggestions: bool = False,
) -> Path:
    suggestions = "\n\n## Suggested sources\n\n- foo\n" if has_suggestions else ""
    path.write_text(
        textwrap.dedent(f"""\
            ---
            type: question
            author: agent
            drafted: {drafted}
            status: {status}
            ---

            # A question
            {suggestions}
            """)
    )
    return path


def test_is_stale_below_threshold(tmp_path: Path) -> None:
    q = _write_question(tmp_path / "q1.md")
    cycles_runner = lambda cmd, cwd: "a\nb\n"  # 2 cycles  # noqa: E731
    stale, n = gs.is_stale(
        q, cycle_log_path=tmp_path / "cycle-log.md", threshold=3, runner=cycles_runner
    )
    assert n == 2
    assert stale is False


def test_is_stale_at_or_above_threshold(tmp_path: Path) -> None:
    q = _write_question(tmp_path / "q2.md")
    cycles_runner = lambda cmd, cwd: "a\nb\nc\n"  # 3 cycles  # noqa: E731
    stale, n = gs.is_stale(
        q, cycle_log_path=tmp_path / "cycle-log.md", threshold=3, runner=cycles_runner
    )
    assert n == 3
    assert stale is True


def test_is_stale_skips_answered(tmp_path: Path) -> None:
    q = _write_question(tmp_path / "q3.md", status="answered")
    cycles_runner = lambda cmd, cwd: "a\nb\nc\nd\n"  # noqa: E731
    stale, _ = gs.is_stale(q, tmp_path / "cycle-log.md", threshold=3, runner=cycles_runner)
    assert stale is False


def test_is_stale_skips_question_without_drafted_date(tmp_path: Path) -> None:
    p = tmp_path / "no-drafted.md"
    p.write_text("---\nstatus: open\n---\n\n# A question\n")
    cycles_runner = lambda cmd, cwd: "a\nb\nc\n"  # noqa: E731
    stale, n = gs.is_stale(p, tmp_path / "cycle-log.md", threshold=3, runner=cycles_runner)
    assert n == 0
    assert stale is False


def test_is_stale_skips_already_enriched(tmp_path: Path) -> None:
    """A question with ## Suggested sources is already enriched; not 'stale' for gap-search purposes."""
    q = _write_question(tmp_path / "q4.md", has_suggestions=True)
    cycles_runner = lambda cmd, cwd: "a\nb\nc\n"  # noqa: E731
    stale, _ = gs.is_stale(q, tmp_path / "cycle-log.md", threshold=3, runner=cycles_runner)
    assert stale is False


# ---------------- write_stale_report ----------------


def test_write_stale_report_emits_table(tmp_path: Path) -> None:
    q1 = _write_question(tmp_path / "q1.md", drafted="2026-05-01")
    q2 = _write_question(tmp_path / "q2.md", drafted="2026-05-02")
    report = tmp_path / "stale-questions.md"
    n = gs.write_stale_report(
        questions=[(q1, 5), (q2, 3)],
        threshold=3,
        report_path=report,
        today="2026-05-25",
    )
    assert n == 2
    md = report.read_text()
    assert "Stale open questions" in md
    assert "q1.md" in md
    assert "q2.md" in md
    assert "≥3" in md  # threshold noted


def test_write_stale_report_handles_empty(tmp_path: Path) -> None:
    report = tmp_path / "stale.md"
    n = gs.write_stale_report(questions=[], threshold=3, report_path=report, today="2026-05-25")
    assert n == 0
    md = report.read_text()
    assert "Stale open questions" in md
    assert "no stale" in md.lower() or "(none)" in md.lower()


def test_splice_into_meta_loop_report_creates_block(tmp_path: Path) -> None:
    """First splice writes the block between idempotent markers."""
    target = tmp_path / "meta-loop-report.md"
    target.write_text("# meta-loop diagnostic report\n\nsome existing content\n")
    gs.splice_meta_loop_section(
        target,
        section_body="| q | 5 |\n| r | 3 |\n",
        today="2026-05-25",
        threshold=3,
    )
    text = target.read_text()
    assert "<!-- gap_search:stale-questions:start -->" in text
    assert "<!-- gap_search:stale-questions:end -->" in text
    assert "5" in text
    # Original content preserved
    assert "some existing content" in text


def test_splice_into_meta_loop_report_replaces_existing(tmp_path: Path) -> None:
    """Second splice overwrites the block, leaves everything else intact."""
    target = tmp_path / "meta-loop-report.md"
    target.write_text(
        "preamble\n"
        "<!-- gap_search:stale-questions:start -->\n"
        "OLD CONTENT\n"
        "<!-- gap_search:stale-questions:end -->\n"
        "postamble\n"
    )
    gs.splice_meta_loop_section(
        target,
        section_body="NEW CONTENT\n",
        today="2026-05-25",
        threshold=3,
    )
    text = target.read_text()
    assert "OLD CONTENT" not in text
    assert "NEW CONTENT" in text
    assert "preamble" in text
    assert "postamble" in text


# ---------------- CLI: --only-stale ----------------


def test_only_stale_filters_fresh(tmp_path: Path, monkeypatch) -> None:
    """With --only-stale, fresh questions (cycles_open < threshold) are skipped."""
    q_dir = tmp_path / "questions"
    q_dir.mkdir()
    _write_question(q_dir / "fresh.md", drafted="2026-05-25")  # cycles 0
    _write_question(q_dir / "stale.md", drafted="2026-05-01")  # cycles 5

    # Track which questions enrich_question was called for
    called: list[str] = []

    def fake_enrich(path, max_results, dry_run):
        called.append(path.name)
        return True

    monkeypatch.setattr(gs, "enrich_question", fake_enrich)
    monkeypatch.setattr(gs, "QUESTIONS", q_dir)

    def cycles_runner(cmd, cwd):
        # Returns 5 cycles for any cycle-log query → both questions get full count
        # but fresh.md drafted today → is_stale returns False because today−drafted is 0,
        # actually our test runner returns 5 unconditionally. So we need to filter by drafted.
        # For this test, we'll use a custom runner that respects --since:
        joined = " ".join(cmd)
        if "--since=2026-05-25" in joined or "--since=2026-05-26" in joined:
            return ""  # nothing since today
        return "a\nb\nc\nd\nf\n"

    # Build argv as if invoked from CLI
    out = io.StringIO()
    rc = gs.run_cli(
        only_stale=True,
        stale_threshold=3,
        cycle_log_path=tmp_path / "cycle-log.md",
        runner=cycles_runner,
        dry_run=True,
        max_per_question=3,
        report_path=None,
        meta_loop_report_path=None,
        out_stream=out,
    )
    assert rc == 0
    # Only the stale one should be enriched
    assert "stale.md" in called
    assert "fresh.md" not in called


def test_no_only_stale_enriches_all(tmp_path: Path, monkeypatch) -> None:
    """Without --only-stale, existing behaviour: every open question eligible."""
    q_dir = tmp_path / "questions"
    q_dir.mkdir()
    _write_question(q_dir / "a.md", drafted="2026-05-25")
    _write_question(q_dir / "b.md", drafted="2026-05-01")

    called: list[str] = []
    monkeypatch.setattr(
        gs,
        "enrich_question",
        lambda path, max_results, dry_run: called.append(path.name) or True,
    )
    monkeypatch.setattr(gs, "QUESTIONS", q_dir)
    out = io.StringIO()
    rc = gs.run_cli(
        only_stale=False,
        stale_threshold=3,
        cycle_log_path=tmp_path / "cycle-log.md",
        runner=lambda cmd, cwd: "",
        dry_run=True,
        max_per_question=3,
        report_path=None,
        meta_loop_report_path=None,
        out_stream=out,
    )
    assert rc == 0
    assert set(called) == {"a.md", "b.md"}
