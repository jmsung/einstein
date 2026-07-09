#!/usr/bin/env python3
"""concept_inventory.py — generate the wiki's concept coverage matrix.

Walks `knowledge/wiki/problems/*.md`, aggregates the `concepts_invoked`,
`techniques_used`, and `findings_produced` frontmatter lists, then
cross-checks each referent against:

  1. its own page in `knowledge/wiki/{concepts,techniques,findings}/`
  2. a citing entry in `knowledge/source/` (substring match on body)

Each referent is classified:

  - `well-covered`       : page exists AND ≥1 source/ paper mentions it
  - `under-sourced`      : page exists, no source/ paper
  - `missing-page`       : ≥2 problems reference it, no own page
  - `orphan-or-singleton`: 1-problem reference, page may or may not exist

The `missing-page` and `under-sourced` rows are the seed-ingest input.

Outputs:
  - `docs/agent/concept-coverage.md`   : human-readable tables
  - `docs/agent/concept-coverage.json` : machine-readable for seed_ingest.py

Usage:
    uv run python docs/tools/concept_inventory.py
    uv run python docs/tools/concept_inventory.py --md-out path.md --json-out path.json
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import logging
import re
from dataclasses import dataclass, field, asdict
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]  # cb/ root
DEFAULT_DOCS = _REPO / "docs"

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
LIST_FIELD_RE = re.compile(r"^([a-zA-Z_]+):\s*\[(.*?)\]\s*$")
SCALAR_FIELD_RE = re.compile(r"^([a-zA-Z_]+):\s*(.*)$")

log = logging.getLogger("concept_inventory")


# ---------------- data classes ----------------


@dataclass
class ProblemPage:
    path: Path
    problem_id: int
    concepts: list[str] = field(default_factory=list)
    techniques: list[str] = field(default_factory=list)
    findings: list[str] = field(default_factory=list)


@dataclass
class Aggregate:
    concepts: dict[str, list[int]] = field(default_factory=dict)
    techniques: dict[str, list[int]] = field(default_factory=dict)
    findings: dict[str, list[int]] = field(default_factory=dict)


@dataclass
class CoverageRow:
    name: str
    kind: str          # concept | technique | finding
    refs: list[int]    # problem ids
    has_page: bool
    has_source: bool
    classification: str  # well-covered | under-sourced | missing-page | orphan-or-singleton


@dataclass
class Report:
    generated_at: str
    rows: list[CoverageRow] = field(default_factory=list)


# ---------------- parsing ----------------


def _parse_frontmatter(text: str) -> dict | None:
    m = FM_RE.match(text)
    if not m:
        return None
    fm: dict = {}
    for line in m.group(1).splitlines():
        line = line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        m_list = LIST_FIELD_RE.match(line)
        if m_list:
            key = m_list.group(1)
            items = [s.strip().strip("\"'") for s in m_list.group(2).split(",") if s.strip()]
            fm[key] = items
            continue
        m_scalar = SCALAR_FIELD_RE.match(line)
        if m_scalar:
            fm[m_scalar.group(1)] = m_scalar.group(2).strip().strip("\"'")
    return fm


def load_problem_pages(problems_dir: Path) -> list[ProblemPage]:
    """Parse all problem pages; skip `_*.md` / `README.md` / unparseable."""
    pages: list[ProblemPage] = []
    for path in sorted(problems_dir.glob("*.md")):
        name = path.name
        if name.startswith("_") or name == "README.md":
            continue
        fm = _parse_frontmatter(path.read_text())
        if fm is None:
            log.warning("skipping %s — no frontmatter", path.name)
            continue
        pid_raw = fm.get("problem_id")
        if pid_raw is None:
            log.warning("skipping %s — frontmatter missing problem_id", path.name)
            continue
        try:
            pid = int(pid_raw)
        except (TypeError, ValueError):
            log.warning("skipping %s — problem_id not int: %r", path.name, pid_raw)
            continue
        pages.append(ProblemPage(
            path=path,
            problem_id=pid,
            concepts=list(fm.get("concepts_invoked") or []),
            techniques=list(fm.get("techniques_used") or []),
            findings=list(fm.get("findings_produced") or []),
        ))
    return pages


def aggregate_references(pages: list[ProblemPage]) -> Aggregate:
    """Build {referent_name -> [problem_ids]} per kind."""
    agg = Aggregate()
    for p in pages:
        for c in p.concepts:
            agg.concepts.setdefault(c, []).append(p.problem_id)
        for t in p.techniques:
            agg.techniques.setdefault(t, []).append(p.problem_id)
        for f in p.findings:
            agg.findings.setdefault(f, []).append(p.problem_id)
    # Dedup + sort problem ids
    for d in (agg.concepts, agg.techniques, agg.findings):
        for k in d:
            d[k] = sorted(set(d[k]))
    return agg


# ---------------- existence checks ----------------


def _page_exists(name: str, wiki_subdir: Path) -> bool:
    return (wiki_subdir / name).is_file()


def _source_cites_concept(name: str, source_index: dict[str, str]) -> bool:
    """Cheap substring search: concept slug (sans .md) in any source/ body.

    Source/ entries are 1:1 distillations — if a paper cites a concept,
    its slug usually appears verbatim either in the title, the cites:
    list, or the body. False positives are tolerable (over-counts
    coverage, which is the safe direction for triage).
    """
    needle = name.removesuffix(".md").replace("-", " ")
    needle_lower = needle.lower()
    slug_lower = name.removesuffix(".md").lower()
    for body in source_index.values():
        body_lower = body.lower()
        if slug_lower in body_lower or needle_lower in body_lower:
            return True
    return False


def _load_source_index(source_dir: Path) -> dict[str, str]:
    """{path-stem: body} for every source/*.md."""
    if not source_dir.is_dir():
        return {}
    return {p.stem: p.read_text() for p in source_dir.glob("*.md")}


# ---------------- classification ----------------


def _classify(refs: list[int], has_page: bool, has_source: bool) -> str:
    # Singletons are always low-priority — page state is irrelevant for the
    # seeding pipeline. Only multi-referenced rows are actionable.
    if len(refs) < 2:
        return "orphan-or-singleton"
    if not has_page:
        return "missing-page"
    if not has_source:
        return "under-sourced"
    return "well-covered"


def build_report(docs_dir: Path) -> Report:
    """Run the full pipeline; return Report."""
    problems_dir = docs_dir / "wiki" / "problems"
    concepts_dir = docs_dir / "wiki" / "concepts"
    techniques_dir = docs_dir / "wiki" / "techniques"
    findings_dir = docs_dir / "wiki" / "findings"
    source_index = _load_source_index(docs_dir / "source")

    pages = load_problem_pages(problems_dir)
    agg = aggregate_references(pages)

    rows: list[CoverageRow] = []
    for kind, table, wiki_sub in (
        ("concept", agg.concepts, concepts_dir),
        ("technique", agg.techniques, techniques_dir),
        ("finding", agg.findings, findings_dir),
    ):
        for name, refs in table.items():
            has_page = _page_exists(name, wiki_sub)
            has_source = _source_cites_concept(name, source_index)
            rows.append(CoverageRow(
                name=name,
                kind=kind,
                refs=refs,
                has_page=has_page,
                has_source=has_source,
                classification=_classify(refs, has_page, has_source),
            ))

    # Sort: missing-page first (high priority), then under-sourced, then by ref count desc
    priority = {"missing-page": 0, "under-sourced": 1, "well-covered": 2, "orphan-or-singleton": 3}
    rows.sort(key=lambda r: (priority[r.classification], -len(r.refs), r.kind, r.name))

    return Report(
        generated_at=dt.date.today().isoformat(),
        rows=rows,
    )


# ---------------- output ----------------


def emit_json(report: Report, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": report.generated_at,
        "rows": [asdict(r) for r in report.rows],
    }
    path.write_text(json.dumps(payload, indent=2) + "\n")


def emit_markdown(report: Report, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    by_class: dict[str, list[CoverageRow]] = {}
    for r in report.rows:
        by_class.setdefault(r.classification, []).append(r)

    lines: list[str] = []
    lines.append("---")
    lines.append("type: report")
    lines.append("author: agent")
    lines.append(f"generated_at: {report.generated_at}")
    lines.append("source: docs/tools/concept_inventory.py")
    lines.append("---")
    lines.append("")
    lines.append("# Concept coverage report")
    lines.append("")
    lines.append(
        "Programmatic view of concept/technique/finding references across "
        "`knowledge/wiki/problems/*.md` frontmatter, classified by wiki + source/ coverage. "
        "Drives `docs/tools/seed_ingest.py`."
    )
    lines.append("")

    # Summary
    lines.append("## Summary")
    lines.append("")
    lines.append("| Classification | Count |")
    lines.append("|---|---|")
    for cls in ("missing-page", "under-sourced", "well-covered", "orphan-or-singleton"):
        lines.append(f"| {cls} | {len(by_class.get(cls, []))} |")
    lines.append("")

    # Tables per classification (action-ordered)
    for cls in ("missing-page", "under-sourced", "well-covered", "orphan-or-singleton"):
        rows = by_class.get(cls, [])
        if not rows:
            continue
        lines.append(f"## {cls} ({len(rows)})")
        lines.append("")
        lines.append("| Kind | Name | Refs (problem ids) | Has page | Has source |")
        lines.append("|---|---|---|---|---|")
        for r in rows:
            refs_str = ", ".join(f"P{i}" for i in r.refs)
            lines.append(
                f"| {r.kind} | `{r.name}` | {refs_str} | "
                f"{'✓' if r.has_page else '·'} | {'✓' if r.has_source else '·'} |"
            )
        lines.append("")

    path.write_text("\n".join(lines))


# ---------------- CLI ----------------


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument(
        "--docs", type=Path, default=DEFAULT_DOCS,
        help="Path to docs/ root (default: derived from this file's location).",
    )
    parser.add_argument(
        "--md-out", type=Path, default=None,
        help="Markdown output path (default: <docs>/agent/concept-coverage.md).",
    )
    parser.add_argument(
        "--json-out", type=Path, default=None,
        help="JSON output path (default: <docs>/agent/concept-coverage.json).",
    )
    args = parser.parse_args(argv)

    docs = args.docs.resolve()
    md_out = args.md_out or docs / "agent" / "concept-coverage.md"
    json_out = args.json_out or docs / "agent" / "concept-coverage.json"

    report = build_report(docs)
    emit_markdown(report, md_out)
    emit_json(report, json_out)

    counts: dict[str, int] = {}
    for r in report.rows:
        counts[r.classification] = counts.get(r.classification, 0) + 1
    log.info("rows: %d (%s)", len(report.rows),
             ", ".join(f"{k}={v}" for k, v in counts.items()))
    log.info("wrote %s", md_out.relative_to(_REPO))
    log.info("wrote %s", json_out.relative_to(_REPO))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
