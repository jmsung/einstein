"""Tests for docs/tools/concept_inventory.py.

The inventory walks docs/wiki/problems/*.md, aggregates the
`concepts_invoked` / `techniques_used` / `findings_produced` frontmatter
fields, cross-checks existence against the wiki + source/ layers, and
classifies each referent by coverage status. The output drives bulk
seed-ingest.
"""
from __future__ import annotations

import json
from pathlib import Path

import pytest

# Path setup — docs/tools is not a package; import via sys.path
import sys

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "docs" / "tools"))

import concept_inventory as ci  # noqa: E402


# ---------------- fixture builders ----------------


def _write_problem(dir_: Path, name: str, *, concepts: list[str], techniques: list[str],
                   findings: list[str] | None = None, problem_id: int = 1, tier: str = "A") -> None:
    findings = findings or []
    body = (
        "---\n"
        "type: problem\n"
        "author: agent\n"
        "drafted: 2026-05-02\n"
        f"problem_id: {problem_id}\n"
        f"tier: {tier}\n"
        f"concepts_invoked: [{', '.join(concepts)}]\n"
        f"techniques_used: [{', '.join(techniques)}]\n"
        f"findings_produced: [{', '.join(findings)}]\n"
        "---\n\n"
        f"# Problem {problem_id} — {name}\n"
    )
    (dir_ / f"{problem_id}-{name}.md").write_text(body)


def _build_wiki(tmp_path: Path, *, concept_pages: list[str], technique_pages: list[str],
                finding_pages: list[str], sources: list[tuple[str, str]] | None = None) -> Path:
    """Create a tmp wiki tree; return the docs/ root."""
    docs = tmp_path / "docs"
    (docs / "wiki" / "problems").mkdir(parents=True)
    (docs / "wiki" / "concepts").mkdir()
    (docs / "wiki" / "techniques").mkdir()
    (docs / "wiki" / "findings").mkdir()
    (docs / "source").mkdir()
    for c in concept_pages:
        (docs / "wiki" / "concepts" / c).write_text(f"# {c}\n")
    for t in technique_pages:
        (docs / "wiki" / "techniques" / t).write_text(f"# {t}\n")
    for f in finding_pages:
        (docs / "wiki" / "findings" / f).write_text(f"# {f}\n")
    for fname, body in sources or []:
        (docs / "source" / fname).write_text(body)
    return docs


# ---------------- tests: parse + aggregate ----------------


def test_parse_problem_frontmatter_concepts(tmp_path: Path) -> None:
    docs = _build_wiki(tmp_path, concept_pages=[], technique_pages=[], finding_pages=[])
    _write_problem(
        docs / "wiki" / "problems", "alpha",
        concepts=["equioscillation.md", "lp-duality.md"],
        techniques=["basin-hopping.md"],
        problem_id=1,
    )
    pages = ci.load_problem_pages(docs / "wiki" / "problems")
    assert len(pages) == 1
    p = pages[0]
    assert p.problem_id == 1
    assert p.concepts == ["equioscillation.md", "lp-duality.md"]
    assert p.techniques == ["basin-hopping.md"]


def test_aggregate_counts_across_problems(tmp_path: Path) -> None:
    docs = _build_wiki(tmp_path, concept_pages=[], technique_pages=[], finding_pages=[])
    pdir = docs / "wiki" / "problems"
    _write_problem(pdir, "alpha", concepts=["equioscillation.md", "lp-duality.md"],
                   techniques=[], problem_id=1)
    _write_problem(pdir, "beta", concepts=["equioscillation.md"],
                   techniques=[], problem_id=2)
    _write_problem(pdir, "gamma", concepts=["sidon-sets.md"],
                   techniques=[], problem_id=3)

    pages = ci.load_problem_pages(pdir)
    agg = ci.aggregate_references(pages)

    # equioscillation referenced by P1 + P2; lp-duality by P1 only; sidon-sets by P3
    assert sorted(agg.concepts["equioscillation.md"]) == [1, 2]
    assert agg.concepts["lp-duality.md"] == [1]
    assert agg.concepts["sidon-sets.md"] == [3]


def test_aggregate_ignores_underscore_files_and_readme(tmp_path: Path) -> None:
    docs = _build_wiki(tmp_path, concept_pages=[], technique_pages=[], finding_pages=[])
    pdir = docs / "wiki" / "problems"
    _write_problem(pdir, "alpha", concepts=["foo.md"], techniques=[], problem_id=1)
    # These should be ignored:
    (pdir / "_inventory.md").write_text("---\ntype: inventory\n---\n# inventory\n")
    (pdir / "README.md").write_text("# readme\n")

    pages = ci.load_problem_pages(pdir)
    assert [p.problem_id for p in pages] == [1]


def test_parse_handles_broken_frontmatter_gracefully(tmp_path: Path, caplog: pytest.LogCaptureFixture) -> None:
    docs = _build_wiki(tmp_path, concept_pages=[], technique_pages=[], finding_pages=[])
    pdir = docs / "wiki" / "problems"
    _write_problem(pdir, "alpha", concepts=["foo.md"], techniques=[], problem_id=1)
    # File with no frontmatter at all
    (pdir / "2-broken.md").write_text("no frontmatter here, just text\n")

    with caplog.at_level("WARNING"):
        pages = ci.load_problem_pages(pdir)
    # Broken file is skipped (no problem_id); good file is kept
    assert [p.problem_id for p in pages] == [1]
    assert any("2-broken" in r.message for r in caplog.records)


# ---------------- tests: classification ----------------


def test_classify_well_covered(tmp_path: Path) -> None:
    docs = _build_wiki(
        tmp_path,
        concept_pages=["equioscillation.md"],
        technique_pages=[],
        finding_pages=[],
        sources=[("2020-foo.md", "# foo\n\nequioscillation is core to ...")],
    )
    pdir = docs / "wiki" / "problems"
    _write_problem(pdir, "alpha", concepts=["equioscillation.md"], techniques=[], problem_id=1)
    _write_problem(pdir, "beta", concepts=["equioscillation.md"], techniques=[], problem_id=2)

    report = ci.build_report(docs)
    row = next(r for r in report.rows if r.name == "equioscillation.md")
    assert row.kind == "concept"
    assert row.refs == [1, 2]
    assert row.has_page is True
    assert row.has_source is True
    assert row.classification == "well-covered"


def test_classify_under_sourced_when_no_paper(tmp_path: Path) -> None:
    docs = _build_wiki(
        tmp_path,
        concept_pages=["equioscillation.md"],  # page exists
        technique_pages=[],
        finding_pages=[],
        sources=[],  # but no source paper cites it
    )
    pdir = docs / "wiki" / "problems"
    _write_problem(pdir, "alpha", concepts=["equioscillation.md"], techniques=[], problem_id=1)
    _write_problem(pdir, "beta", concepts=["equioscillation.md"], techniques=[], problem_id=2)

    report = ci.build_report(docs)
    row = next(r for r in report.rows if r.name == "equioscillation.md")
    assert row.classification == "under-sourced"


def test_classify_missing_page_for_multi_referenced(tmp_path: Path) -> None:
    docs = _build_wiki(tmp_path, concept_pages=[], technique_pages=[], finding_pages=[])
    pdir = docs / "wiki" / "problems"
    _write_problem(pdir, "alpha", concepts=["parameterization-selection.md"], techniques=[], problem_id=1)
    _write_problem(pdir, "beta", concepts=["parameterization-selection.md"], techniques=[], problem_id=2)
    _write_problem(pdir, "gamma", concepts=["parameterization-selection.md"], techniques=[], problem_id=3)

    report = ci.build_report(docs)
    row = next(r for r in report.rows if r.name == "parameterization-selection.md")
    assert row.classification == "missing-page"
    assert row.has_page is False
    assert len(row.refs) == 3


def test_classify_orphan_when_singleton(tmp_path: Path) -> None:
    docs = _build_wiki(
        tmp_path,
        concept_pages=["niche.md"],
        technique_pages=[],
        finding_pages=[],
    )
    pdir = docs / "wiki" / "problems"
    _write_problem(pdir, "alpha", concepts=["niche.md"], techniques=[], problem_id=1)

    report = ci.build_report(docs)
    row = next(r for r in report.rows if r.name == "niche.md")
    # single ref + page exists, but doesn't pass the ≥2-ref bar for the seeding pipeline
    assert row.classification == "orphan-or-singleton"


def test_techniques_and_findings_are_separately_classified(tmp_path: Path) -> None:
    docs = _build_wiki(
        tmp_path,
        concept_pages=[],
        technique_pages=["basin-hopping.md"],
        finding_pages=[],
    )
    pdir = docs / "wiki" / "problems"
    _write_problem(pdir, "alpha", concepts=[], techniques=["basin-hopping.md", "mystery.md"], problem_id=1)
    _write_problem(pdir, "beta", concepts=[], techniques=["mystery.md"], problem_id=2)

    report = ci.build_report(docs)
    by_name = {r.name: r for r in report.rows}
    assert by_name["basin-hopping.md"].kind == "technique"
    assert by_name["basin-hopping.md"].classification == "orphan-or-singleton"
    assert by_name["mystery.md"].kind == "technique"
    assert by_name["mystery.md"].classification == "missing-page"


# ---------------- tests: JSON + markdown output ----------------


def test_emit_json_round_trip(tmp_path: Path) -> None:
    docs = _build_wiki(tmp_path, concept_pages=[], technique_pages=[], finding_pages=[])
    pdir = docs / "wiki" / "problems"
    _write_problem(pdir, "alpha", concepts=["foo.md", "bar.md"], techniques=[], problem_id=1)
    _write_problem(pdir, "beta", concepts=["foo.md"], techniques=[], problem_id=2)

    report = ci.build_report(docs)
    out_json = tmp_path / "out.json"
    ci.emit_json(report, out_json)

    data = json.loads(out_json.read_text())
    assert "generated_at" in data
    assert "rows" in data
    names = {r["name"] for r in data["rows"]}
    assert {"foo.md", "bar.md"} <= names


def test_emit_markdown_contains_tables(tmp_path: Path) -> None:
    docs = _build_wiki(tmp_path, concept_pages=[], technique_pages=[], finding_pages=[])
    pdir = docs / "wiki" / "problems"
    _write_problem(pdir, "alpha", concepts=["foo.md"], techniques=["t.md"], problem_id=1)

    report = ci.build_report(docs)
    out_md = tmp_path / "out.md"
    ci.emit_markdown(report, out_md)
    text = out_md.read_text()
    assert "Concept coverage" in text
    assert "foo.md" in text
    assert "t.md" in text
