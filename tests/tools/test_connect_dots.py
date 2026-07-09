"""Tests for the Goal-3 cross-pollination amplifier.

Three pieces: (1) cycle_runner.sh structural guard — qmd refresh stays step 1
so the NEXT cycle can query THIS cycle's findings; (2) sibling_findings —
the connect-the-dots prompt section from same-category sibling problems;
(3) cross-pollination surfacing over a trailing cycle-log window.
"""

from __future__ import annotations

import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "docs" / "tools"))
sys.path.insert(0, str(_REPO / "scripts"))

import autonomous_loop as al  # noqa: E402
import inner_agent_prompt as iap  # noqa: E402

# ---------------- (1) cycle_runner refresh-order guard ----------------


def test_cycle_runner_refreshes_qmd_before_gap_detection() -> None:
    """The qmd refresh must precede wiki_graph/gap_search — without it the
    next cycle queries a stale index and this cycle's findings are invisible
    (cycle-discipline step 3). Live-confirmed 2026-06-09: cycle 287's
    dead-end was indexed post-cycle and cited by cycle 288."""
    script = (_REPO / "docs" / "tools" / "cycle_runner.sh").read_text()
    refresh_pos = script.find("refresh_qmd")
    graph_pos = script.find("wiki_graph")
    assert refresh_pos != -1, "cycle_runner.sh no longer refreshes qmd"
    assert graph_pos != -1
    assert refresh_pos < graph_pos, "qmd refresh must run before gap detection"


# ---------------- (2) sibling_findings ----------------


def _write_finding(
    fdir: Path, slug: str, *, origin: str | None, related: str | None, drafted: str
) -> None:
    fm = ["---", "type: finding", "author: agent", f"drafted: {drafted}"]
    if origin:
        fm.append(f"question_origin: {origin}")
    if related:
        fm.append(f"related_problems: {related}")
    fm += ["---", "", f"# Finding {slug}", "body"]
    (fdir / f"{slug}.md").write_text("\n".join(fm))


def _findings_dir(tmp_path: Path) -> Path:
    d = tmp_path / "findings"
    d.mkdir()
    return d


def test_sibling_findings_same_category_other_problem(tmp_path: Path) -> None:
    fdir = _findings_dir(tmp_path)
    # P2 and P4 are both autocorrelation; P14 is packing.
    _write_finding(fdir, "p2-warm-pruning", origin="problem-2", related=None, drafted="2026-06-08")
    _write_finding(
        fdir, "p14-packing-trick", origin="problem-14", related=None, drafted="2026-06-08"
    )
    section = iap.sibling_findings(4, findings_dir=fdir)
    assert section is not None
    assert "p2-warm-pruning" in section
    assert "p14-packing-trick" not in section


def test_sibling_findings_excludes_own_problem(tmp_path: Path) -> None:
    fdir = _findings_dir(tmp_path)
    _write_finding(fdir, "p4-own-dead-end", origin="problem-4", related=None, drafted="2026-06-08")
    section = iap.sibling_findings(4, findings_dir=fdir)
    assert section is None or "p4-own-dead-end" not in section


def test_sibling_findings_related_problems_field_counts(tmp_path: Path) -> None:
    fdir = _findings_dir(tmp_path)
    _write_finding(
        fdir, "family-envelope", origin="problem-meta", related="[2, 3]", drafted="2026-06-07"
    )
    section = iap.sibling_findings(4, findings_dir=fdir)
    assert section is not None and "family-envelope" in section


def test_sibling_findings_caps_at_max_pages_most_recent(tmp_path: Path) -> None:
    fdir = _findings_dir(tmp_path)
    for i, day in enumerate(["01", "02", "03", "04", "05"]):
        _write_finding(
            fdir, f"p2-f{day}", origin="problem-2", related=None, drafted=f"2026-06-{day}"
        )
    section = iap.sibling_findings(4, findings_dir=fdir, max_pages=3)
    assert section is not None
    assert "p2-f05" in section and "p2-f04" in section and "p2-f03" in section
    assert "p2-f01" not in section


def test_sibling_findings_empty_dir_is_none(tmp_path: Path) -> None:
    assert iap.sibling_findings(4, findings_dir=_findings_dir(tmp_path)) is None
    assert iap.sibling_findings(4, findings_dir=tmp_path / "missing") is None


def test_sibling_findings_unknown_category_is_none(tmp_path: Path) -> None:
    fdir = _findings_dir(tmp_path)
    _write_finding(fdir, "p2-x", origin="problem-2", related=None, drafted="2026-06-08")
    # problem 9999 has no category mapping → no siblings derivable.
    assert iap.sibling_findings(9999, findings_dir=fdir) is None


def test_render_prompt_includes_sibling_section(tmp_path: Path) -> None:
    pdir = tmp_path / "problems"
    pdir.mkdir()
    (pdir / "4-third-autocorrelation.md").write_text(
        "---\ntype: problem\nproblem_id: 4\n---\n# P4\nbody"
    )
    prompt = iap.render_prompt(
        problem_id=4,
        problem_slug="third-autocorrelation",
        file_slug="4-third-autocorrelation",
        score_current=1.45,
        status="rank-2-displaced",
        tier="S",
        category="autocorrelation",
        cycle_id=1,
        attempt_index=1,
        problems_dir=pdir,
        cycle_log=tmp_path / "no-log.md",
        skill_library=tmp_path / "no-lib.md",
        experiment_log_dir=tmp_path,
        sibling_findings_section="- knowledge/wiki/findings/p2-warm-pruning.md (2026-06-08)",
    )
    assert "connect-the-dots" in prompt
    assert "p2-warm-pruning" in prompt


def test_render_prompt_omits_section_when_none(tmp_path: Path) -> None:
    pdir = tmp_path / "problems"
    pdir.mkdir()
    (pdir / "4-third-autocorrelation.md").write_text(
        "---\ntype: problem\nproblem_id: 4\n---\n# P4\nbody"
    )
    prompt = iap.render_prompt(
        problem_id=4,
        problem_slug="third-autocorrelation",
        file_slug="4-third-autocorrelation",
        score_current=1.45,
        status="rank-2-displaced",
        tier="S",
        category="autocorrelation",
        cycle_id=1,
        attempt_index=1,
        problems_dir=pdir,
        cycle_log=tmp_path / "no-log.md",
        skill_library=tmp_path / "no-lib.md",
        experiment_log_dir=tmp_path,
    )
    assert "connect-the-dots" not in prompt


# ---------------- (3) cross-pollination surfacing ----------------

_LOG_HEADER = "# Cycle log\n\n"


def _row(cid: int, problem: str, notes: str) -> str:
    return (
        f"| {cid} | {problem} | 1.0 (no Δ) | 1 | local-cpu+llm | 0 | 0 | 0 "
        f"| a:1/h:0/hyb:0 | converged | {notes} | 0 |"
    )


def test_surface_cross_pollination_counts_multi_problem_techniques(tmp_path: Path) -> None:
    log = tmp_path / "cycle-log.md"
    log.write_text(
        _LOG_HEADER
        + "\n".join(
            [
                _row(1, "P2-first-autocorrelation", "technique=larger-n-cascade.md x"),
                _row(2, "P4-third-autocorrelation", "technique=larger-n-cascade.md y"),
                _row(3, "P12-flat-polynomials", "technique=memetic-tabu-search.md z"),
            ]
        )
        + "\n"
    )
    assert al.surface_cross_pollination(log, window=50) == 1


def test_surface_cross_pollination_window_limits_rows(tmp_path: Path) -> None:
    log = tmp_path / "cycle-log.md"
    log.write_text(
        _LOG_HEADER
        + "\n".join(
            [
                _row(1, "P2-first-autocorrelation", "technique=larger-n-cascade.md x"),
                _row(2, "P12-flat-polynomials", "technique=memetic-tabu-search.md z"),
                _row(3, "P4-third-autocorrelation", "technique=larger-n-cascade.md y"),
            ]
        )
        + "\n"
    )
    # Window of 2 sees only rows 2-3 → no technique spans 2 problems.
    assert al.surface_cross_pollination(log, window=2) == 0


def test_surface_cross_pollination_missing_log_is_zero(tmp_path: Path) -> None:
    assert al.surface_cross_pollination(tmp_path / "nope.md", window=50) == 0
