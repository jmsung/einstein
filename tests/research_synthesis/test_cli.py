"""End-to-end CLI tests for scripts/research_synthesis.py.

All claude + qmd subprocess paths are mocked via injectable runners.
"""

from __future__ import annotations

import io
import json
import sys
import textwrap
from pathlib import Path

import pytest

# Add scripts dir to sys.path so we can `import research_synthesis as script`
_SCRIPTS = Path(__file__).resolve().parents[2] / "scripts"
sys.path.insert(0, str(_SCRIPTS))

import research_synthesis as script  # noqa: E402

from einstein.research_synthesis.query import RunnerResult  # noqa: E402
from einstein.research_synthesis.synthesizer import _RunnerResult  # noqa: E402


@pytest.fixture
def mb_layout(tmp_path: Path) -> Path:
    """Build a tmp mb/ layout with one problem dir + strategy.md."""
    pdir = tmp_path / "problems" / "14-circle-packing-square"
    pdir.mkdir(parents=True)
    (pdir / "strategy.md").write_text(
        textwrap.dedent("""\
            # P14 — circle packing in unit square

            Strict tol=0; n=50; SLSQP polish.
            Known basin: Hardin-Sloane.
            """)
    )
    return tmp_path


def _stub_qmd_runner(stdout: str = "") -> object:
    def runner(cmd, env):
        return RunnerResult(returncode=0, stdout=stdout)

    return runner


def _ok_claude_runner(payload: dict):
    def runner(**kwargs):
        return _RunnerResult(ok=True, stdout=json.dumps(payload))

    return runner


def _fail_claude_runner():
    def runner(**kwargs):
        return _RunnerResult(ok=False, error_kind="unavailable", error_message="x")

    return runner


def test_resolve_slug_finds_unique(mb_layout: Path) -> None:
    assert script.resolve_slug(14, mb_layout) == "circle-packing-square"


def test_resolve_slug_missing_returns_none(mb_layout: Path) -> None:
    assert script.resolve_slug(99, mb_layout) is None


def test_resolve_slug_ambiguous_raises(mb_layout: Path) -> None:
    # Create second 14-foo dir
    (mb_layout / "problems" / "14-other-variant").mkdir()
    with pytest.raises(ValueError, match="multiple"):
        script.resolve_slug(14, mb_layout)


def test_derive_queries_yields_base_and_strategy_lines() -> None:
    strategy = "# P14 — circle packing in unit square\n\nStrict tol=0; n=50; SLSQP polish.\n"
    qs = script.derive_queries(14, "circle-packing-square", strategy)
    assert qs[0] == "P14 circle packing square"
    assert qs[1] == "circle packing square"
    assert len(qs) <= 5


def test_derive_queries_strips_leading_bullets_g10_take4_regression() -> None:
    """G10 take 4 diagnostic: qmd rejects args starting with '-' or empty.

    Strategy.md lines like '- **Submitted**: ...' would yield queries with
    a leading dash, which qmd's argparse interprets as a flag and prints
    'Usage: qmd query ...'. _clean_query strips leading bullet markers.
    """
    strategy = (
        "# P1 — Erdős Minimum Overlap\n\n"
        "- **Submitted**: #2 at 0.3808703105862199 (tied SOTA)\n"
        "* Best local: 0.3808703104931\n"
        "- Status: DONE — unbridgeable\n"
    )
    qs = script.derive_queries(1, "erdos-overlap", strategy)
    # None of the queries start with '-' or '*' (would confuse qmd)
    for q in qs:
        assert not q.startswith("-"), f"query starts with '-': {q!r}"
        assert not q.startswith("*"), f"query starts with '*': {q!r}"
        # Non-empty (no whitespace-only)
        assert q.strip() == q
        assert q


def test_derive_queries_dedupes_and_filters_empties() -> None:
    """Whitespace-only / empty lines from strategy.md are skipped."""
    strategy = "# title\n\n   \n\n# title\n"  # duplicate "title" + a blank
    qs = script.derive_queries(7, "prime-number-theorem", strategy)
    # Base entries always present
    assert "P7 prime number theorem" in qs
    # No duplicates
    assert len(qs) == len(set(qs))
    # No empties
    assert all(q for q in qs)


def test_dry_run_prints_prompt_and_does_not_write(mb_layout: Path) -> None:
    args = script._parse_args(
        [
            "--problem-id",
            "14",
            "--mb-dir",
            str(mb_layout),
            "--dry-run",
            "--drafted-at",
            "2026-05-25",
        ]
    )
    out = io.StringIO()
    rc = script.run_cli(args, qmd_runner=_stub_qmd_runner(""), out_stream=out)
    assert rc == 0
    s = out.getvalue()
    assert "DRY RUN" in s
    assert "P14" in s
    assert "circle-packing-square" in s
    # No file written
    files = list((mb_layout / "problems" / "14-circle-packing-square").iterdir())
    assert all("literature-synthesis" not in f.name for f in files)


def test_full_run_writes_markdown(mb_layout: Path) -> None:
    payload = {
        "problem_id": 14,
        "problem_slug": "circle-packing-square",
        "drafted_at": "2026-05-25",
        "queries": ["P14 circle packing square"],
        "top_sources": [
            {
                "path": "knowledge/source/X.md",
                "score": 0.7,
                "snippet": "s",
                "collection": "einstein-wiki-source",
            }
        ],
        "top_wiki": [],
        "cross_source_patterns": [
            {
                "name": "P14-specific pattern",
                "description": "d",
                "supporting_sources": ["knowledge/source/X.md"],
            }
        ],
        "proposed_approaches": [
            {
                "description": "approach 1",
                "cited_sources": ["knowledge/source/X.md"],
                "rationale": "because",
            }
        ],
        "gaps_identified": ["gap1"],
    }
    args = script._parse_args(
        [
            "--problem-id",
            "14",
            "--mb-dir",
            str(mb_layout),
            "--drafted-at",
            "2026-05-25",
        ]
    )
    out = io.StringIO()
    rc = script.run_cli(
        args,
        qmd_runner=_stub_qmd_runner(""),
        claude_runner=_ok_claude_runner(payload),
        out_stream=out,
    )
    assert rc == 0
    output_path = (
        mb_layout / "problems" / "14-circle-packing-square" / "literature-synthesis-2026-05-25.md"
    )
    assert output_path.exists()
    md = output_path.read_text()
    assert "Literature synthesis: P14 — circle-packing-square" in md
    assert "P14-specific pattern" in md
    assert "approach 1" in md
    assert "gap1" in md


def test_claude_failure_returns_nonzero(mb_layout: Path) -> None:
    args = script._parse_args(
        [
            "--problem-id",
            "14",
            "--mb-dir",
            str(mb_layout),
            "--drafted-at",
            "2026-05-25",
        ]
    )
    out = io.StringIO()
    rc = script.run_cli(
        args,
        qmd_runner=_stub_qmd_runner(""),
        claude_runner=_fail_claude_runner(),
        out_stream=out,
    )
    assert rc == 1
    assert "synthesis failed" in out.getvalue()


def test_unknown_problem_id_returns_nonzero(mb_layout: Path) -> None:
    args = script._parse_args(
        [
            "--problem-id",
            "99",
            "--mb-dir",
            str(mb_layout),
        ]
    )
    out = io.StringIO()
    rc = script.run_cli(args, qmd_runner=_stub_qmd_runner(""), out_stream=out)
    assert rc == 1
    assert "no mb/problems/99" in out.getvalue()


def test_output_override(mb_layout: Path, tmp_path: Path) -> None:
    payload = {
        "problem_id": 14,
        "problem_slug": "circle-packing-square",
        "drafted_at": "2026-05-25",
    }
    custom = tmp_path / "custom" / "out.md"
    args = script._parse_args(
        [
            "--problem-id",
            "14",
            "--mb-dir",
            str(mb_layout),
            "--drafted-at",
            "2026-05-25",
            "--output",
            str(custom),
        ]
    )
    out = io.StringIO()
    rc = script.run_cli(
        args,
        qmd_runner=_stub_qmd_runner(""),
        claude_runner=_ok_claude_runner(payload),
        out_stream=out,
    )
    assert rc == 0
    assert custom.exists()
