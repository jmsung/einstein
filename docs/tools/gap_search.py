#!/usr/bin/env python3
"""gap_search.py — auto-suggest source artifacts for open gap questions.

Closes the gap→ingest chain. Reads docs/wiki/questions/*.md with status: open,
builds a search query from the question's title + related_concepts frontmatter,
queries the arxiv API, and appends a "## Suggested sources" section to the
question file with the top hits. Human still has to approve + /wiki-ingest;
this just eliminates the search burden.

Append-only: if a question already has "## Suggested sources", we skip it
(keeps cycle-discipline's "questions are append-only" rule intact).

Usage:
    uv run python docs/tools/gap_search.py                # enrich all open
    uv run python docs/tools/gap_search.py --question <slug>   # enrich one
    uv run python docs/tools/gap_search.py --dry-run      # show what we'd add
    uv run python docs/tools/gap_search.py --max-per-question 3   # default 3

Per .claude/rules/cycle-discipline.md step 4.5: this runs at cycle-end after
wiki_graph.py --file-questions, before promotion-log review.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import logging
import re
import subprocess
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections.abc import Callable
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
QUESTIONS = _REPO / "docs" / "wiki" / "questions"
DEFAULT_CYCLE_LOG = _REPO / "docs" / "agent" / "cycle-log.md"
DEFAULT_STALE_REPORT = _REPO.parent / "mb" / "logs" / "stale-questions.md"
DEFAULT_META_LOOP_REPORT = _REPO.parent / "mb" / "logs" / "meta-loop-report.md"

log = logging.getLogger("gap_search")

ARXIV_API = "http://export.arxiv.org/api/query"
ATOM_NS = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
TITLE_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
EXISTING_SUGGESTIONS_RE = re.compile(r"^##\s+Suggested sources", re.MULTILINE)

# Goal 5 of js/feat/research-synthesis: idempotent markers around the
# meta-loop-report.md section gap_search writes.
META_LOOP_MARKER_START = "<!-- gap_search:stale-questions:start -->"
META_LOOP_MARKER_END = "<!-- gap_search:stale-questions:end -->"


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Return (frontmatter dict, body)."""
    m = FM_RE.match(text)
    if not m:
        return {}, text
    fm: dict = {}
    current_list = None
    for line in m.group(1).splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        if re.match(r"^\s+-\s+", line) and current_list:
            fm[current_list].append(re.sub(r"^\s+-\s+", "", line).strip().strip("\"'"))
            continue
        kv = re.match(r"^([a-zA-Z_]+):\s*(.*)$", line)
        if not kv:
            continue
        key, val = kv.group(1), kv.group(2).strip()
        if val == "":
            fm[key] = []
            current_list = key
        elif val.startswith("["):
            items = [s.strip().strip("\"'") for s in val.strip("[]").split(",") if s.strip()]
            fm[key] = items
            current_list = None
        else:
            fm[key] = val.strip().strip("\"'")
            current_list = None
    return fm, text[m.end() :]


MATH_CATEGORIES = ["math.NT", "math.CO", "math.OC", "math.MG", "math.PR", "math.CA", "math.NA"]


def _clean(s: str) -> str:
    """Strip slashes and other arxiv-query-breaking chars; collapse whitespace."""
    s = re.sub(r"[/\\:;,()]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def build_query(title: str, concepts: list[str], related_problems: list[str]) -> str:
    """Turn question title + concepts into an arxiv search query.

    Strategy: OR up to 2 concept slugs (strongest signal) plus 1 title-derived
    keyword phrase. AND that with the math-category filter. Each clause is
    quoted so multi-word phrases stay coherent.
    """
    keywords: list[str] = []

    for c in concepts[:2]:
        clean = _clean(re.sub(r"\.md$", "", c).replace("-", " ").replace("_", " "))
        if clean:
            keywords.append(clean)

    clean_title = re.sub(
        r"\?$|^(Could|Can|Is|Does|Why does|How does|What is|When does)\s+(a|the)?\s*",
        "",
        title,
        flags=re.IGNORECASE,
    )
    clean_title = re.sub(r"\bP\d+[a-z]?\b|\b\d+\.\d{3,}\b|\bbelow \d+\b", "", clean_title)
    clean_title = _clean(clean_title)
    # Take only the first ~6 words from the title — keeps the query focused
    title_phrase = " ".join(clean_title.split()[:6])
    if title_phrase:
        keywords.append(title_phrase)

    if not keywords:
        return ""

    # OR the keywords (any match counts), AND with math-category restriction
    kw_query = " OR ".join(f'all:"{k}"' for k in keywords)
    cat_query = " OR ".join(f"cat:{c}" for c in MATH_CATEGORIES)
    return f"({kw_query}) AND ({cat_query})"


def search_arxiv(query: str, max_results: int = 5) -> list[dict]:
    """Hit the arxiv API. Return list of {title, authors, year, abs_url, summary}."""
    params = urllib.parse.urlencode(
        {
            "search_query": query,
            "start": "0",
            "max_results": str(max_results),
            "sortBy": "relevance",
            "sortOrder": "descending",
        }
    )
    url = f"{ARXIV_API}?{params}"

    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            xml_text = resp.read().decode("utf-8")
    except Exception as e:
        print(f"  arxiv search failed: {e}", file=sys.stderr)
        return []

    root = ET.fromstring(xml_text)
    results = []
    for entry in root.findall("a:entry", ATOM_NS):
        title = (
            (entry.findtext("a:title", default="", namespaces=ATOM_NS) or "")
            .strip()
            .replace("\n", " ")
        )
        abs_url = entry.findtext("a:id", default="", namespaces=ATOM_NS) or ""
        summary = (
            (entry.findtext("a:summary", default="", namespaces=ATOM_NS) or "")
            .strip()
            .replace("\n", " ")
        )
        # Authors
        authors = [
            a.findtext("a:name", default="", namespaces=ATOM_NS)
            for a in entry.findall("a:author", ATOM_NS)
        ]
        # Year from published date
        published = entry.findtext("a:published", default="", namespaces=ATOM_NS) or ""
        year = published[:4] if published else ""

        results.append(
            {
                "title": title,
                "authors": ", ".join(a for a in authors if a)[:120],
                "year": year,
                "abs_url": abs_url,
                "summary": (summary[:280] + "...") if len(summary) > 280 else summary,
            }
        )
    return results


def format_suggestions(results: list[dict], query: str) -> str:
    """Render results as a markdown section appended to the question."""
    lines = [
        "",
        "## Suggested sources",
        "",
        f"*Auto-suggested by `docs/tools/gap_search.py` — arxiv query: `{query}`*",
        "",
        "Review and `/wiki-ingest <arxiv-url>` any that look relevant. "
        "If none fit, close the question with `status: superseded` and a one-line explanation.",
        "",
    ]
    if not results:
        lines.append("*(no results; broaden the search terms or query the web)*")
        return "\n".join(lines)

    for i, r in enumerate(results, 1):
        lines.append(f"### {i}. {r['title']} ({r['year']})")
        if r["authors"]:
            lines.append(f"**Authors:** {r['authors']}")
        lines.append(f"**URL:** {r['abs_url']}")
        lines.append(f"**Abstract:** {r['summary']}")
        lines.append("")
    return "\n".join(lines)


# ---------------- staleness (Goal 5) ----------------


GitRunner = Callable[[list[str], "Path | None"], str]


def _default_git_runner(cmd: list[str], cwd) -> str:
    """Run a git command; return stdout text. Raises on non-zero exit."""
    proc = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd, check=True, timeout=30)
    return proc.stdout or ""


def cycles_since(
    cycle_log_path: Path,
    *,
    since_iso_date: str,
    runner: GitRunner | None = None,
) -> int:
    """Count cycle-log.md commits since the given ISO date.

    Approximation: each commit roughly adds one cycle row (the autonomous loop
    appends per-cycle). Returns 0 on any subprocess failure — gap_search must
    never break the cycle, so missing git is a safe no-op.
    """
    runner_fn = runner or _default_git_runner
    cmd = ["git", "log", f"--since={since_iso_date}", "--format=%H", "--", str(cycle_log_path)]
    try:
        out = runner_fn(cmd, cycle_log_path.parent if cycle_log_path.parent.exists() else None)
    except Exception as e:  # noqa: BLE001
        log.warning("cycles_since: git failed (%s); treating as 0 cycles open", e)
        return 0
    lines = [ln for ln in (out or "").splitlines() if ln.strip()]
    return len(lines)


def is_stale(
    question_path: Path,
    cycle_log_path: Path,
    *,
    threshold: int = 3,
    runner: GitRunner | None = None,
) -> tuple[bool, int]:
    """Return ``(stale, cycles_open)`` for a question file.

    Stale = ``status: open`` AND ``cycles_open >= threshold`` AND no
    ``## Suggested sources`` block already present (already enriched).
    """
    text = question_path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)
    if fm.get("status", "") != "open":
        return False, 0
    drafted = fm.get("drafted", "")
    if not drafted:
        return False, 0
    if EXISTING_SUGGESTIONS_RE.search(body):
        return False, 0
    cycles_open = cycles_since(cycle_log_path, since_iso_date=str(drafted), runner=runner)
    return cycles_open >= threshold, cycles_open


def write_stale_report(
    *,
    questions: list[tuple[Path, int]],
    threshold: int,
    report_path: Path,
    today: str | None = None,
) -> int:
    """Write the stale-questions diagnostic markdown. Returns count written."""
    today = today or _dt.date.today().isoformat()
    lines = [
        "# Stale open questions",
        "",
        f"_Updated: {today}. Threshold: ≥{threshold} cycle(s) open._",
        "",
        (
            "Each open question below has accumulated ≥ threshold cycles in the "
            "cycle-log without being answered. `gap_search.py --only-stale` "
            "auto-enriches these with arxiv top-3 hits in their `## Suggested "
            "sources` block; human still approves + `/wiki-ingest`."
        ),
        "",
    ]
    if not questions:
        lines.extend(["_(no stale questions)_", ""])
    else:
        lines.extend(
            [
                "| Question | Cycles open | Suggested sources | Status |",
                "|---|---|---|---|",
            ]
        )
        for path, n in sorted(questions, key=lambda kv: (-kv[1], kv[0].name)):
            body = parse_frontmatter(path.read_text(encoding="utf-8"))[1]
            enriched = "yes" if EXISTING_SUGGESTIONS_RE.search(body) else "no"
            lines.append(f"| `{path.name}` | {n} | {enriched} | open |")
        lines.append("")
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines), encoding="utf-8")
    return len(questions)


def splice_meta_loop_section(
    target: Path,
    *,
    section_body: str,
    today: str,
    threshold: int,
) -> None:
    """Idempotently splice gap_search's stale-questions section into the meta-loop report.

    Wraps the section in
    ``<!-- gap_search:stale-questions:start --> ... :end -->`` markers so a
    re-run replaces the block in place without disturbing surrounding content.
    Appends if absent.
    """
    header = (
        f"## Stale open questions _(gap_search)_\n\n"
        f"_Updated: {today}. Threshold: ≥{threshold} cycle(s)._\n\n"
    )
    block = f"{META_LOOP_MARKER_START}\n{header}{section_body.rstrip()}\n{META_LOOP_MARKER_END}\n"
    if target.exists():
        text = target.read_text(encoding="utf-8")
    else:
        text = ""
        target.parent.mkdir(parents=True, exist_ok=True)
    if META_LOOP_MARKER_START in text and META_LOOP_MARKER_END in text:
        before, _, rest = text.partition(META_LOOP_MARKER_START)
        _, _, after = rest.partition(META_LOOP_MARKER_END + "\n")
        new_text = before + block + after
    else:
        sep = "" if not text or text.endswith("\n") else "\n"
        new_text = text + sep + "\n" + block
    target.write_text(new_text, encoding="utf-8")


def enrich_question(path: Path, max_results: int, dry_run: bool) -> bool:
    """Returns True if file was (or would be) updated."""
    text = path.read_text()
    fm, body = parse_frontmatter(text)

    status = fm.get("status", "")
    if status != "open":
        return False
    if "type" in fm and fm["type"] not in ("question", "gap"):
        return False
    if EXISTING_SUGGESTIONS_RE.search(body):
        return False  # already enriched

    tm = TITLE_RE.search(body)
    title = tm.group(1) if tm else path.stem
    concepts = fm.get("related_concepts", []) or []
    related_problems = fm.get("related_problems", []) or []

    query = build_query(title, concepts, related_problems)
    print(f"[{path.name}]")
    print(f"  query: {query}")

    if dry_run:
        print(f"  (dry-run; would search arxiv for up to {max_results} results)")
        return True

    results = search_arxiv(query, max_results=max_results)
    print(f"  found {len(results)} arxiv results")

    section = format_suggestions(results, query)
    new_text = text.rstrip() + "\n" + section + "\n"
    path.write_text(new_text)
    return True


def run_cli(
    *,
    question: str | None = None,
    only_stale: bool = False,
    stale_threshold: int = 3,
    cycle_log_path: Path = DEFAULT_CYCLE_LOG,
    runner: GitRunner | None = None,
    dry_run: bool = False,
    max_per_question: int = 3,
    report_path: Path | None = None,
    meta_loop_report_path: Path | None = None,
    out_stream=sys.stdout,
) -> int:
    """Pure-Python entry point — testable; takes injected git runner.

    Returns 0 on success, non-zero on resolution errors (single-question
    fuzzy-match ambiguity, missing).
    """
    if question:
        cand = QUESTIONS / question
        if not cand.exists() and not cand.name.endswith(".md"):
            cand = QUESTIONS / f"{question}.md"
        if not cand.exists():
            matches = list(QUESTIONS.glob(f"*{question}*.md"))
            if len(matches) == 1:
                cand = matches[0]
            elif not matches:
                print(f"No question found matching {question!r}", file=out_stream)
                return 1
            else:
                print(f"Ambiguous: {[m.name for m in matches]}", file=out_stream)
                return 1
        targets = [cand]
    else:
        targets = sorted(QUESTIONS.glob("*.md"))

    # Apply --only-stale filter; collect stale list for the report.
    stale_entries: list[tuple[Path, int]] = []
    if only_stale:
        filtered: list[Path] = []
        for path in targets:
            if path.name == "README.md":
                continue
            stale, n = is_stale(path, cycle_log_path, threshold=stale_threshold, runner=runner)
            if stale:
                filtered.append(path)
                stale_entries.append((path, n))
        targets = filtered

    updated = 0
    for path in targets:
        if path.name == "README.md":
            continue
        if enrich_question(path, max_per_question, dry_run):
            updated += 1

    label = "Would update" if dry_run else "Updated"
    print(f"\n{label} {updated} question(s).", file=out_stream)

    # Write the diagnostic report when stale mode is on, or whenever the user
    # explicitly asks for it.
    if report_path is not None or only_stale:
        report_target = report_path or DEFAULT_STALE_REPORT
        n_stale = write_stale_report(
            questions=stale_entries, threshold=stale_threshold, report_path=report_target
        )
        print(f"stale-questions report: {n_stale} entry/entries → {report_target}", file=out_stream)
        if meta_loop_report_path is not None:
            # Build a compact section_body (table excerpt) for the splice.
            if stale_entries:
                section_body = "| Question | Cycles open |\n|---|---|\n" + "\n".join(
                    f"| `{p.name}` | {n} |"
                    for p, n in sorted(stale_entries, key=lambda kv: (-kv[1], kv[0].name))
                )
            else:
                section_body = "_(no stale questions)_"
            splice_meta_loop_section(
                meta_loop_report_path,
                section_body=section_body,
                today=_dt.date.today().isoformat(),
                threshold=stale_threshold,
            )
            print(f"meta-loop-report.md spliced at {meta_loop_report_path}", file=out_stream)
    return 0


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--question", help="Enrich a single question (slug or path)")
    p.add_argument(
        "--max-per-question", type=int, default=3, help="arxiv results per question (default 3)"
    )
    p.add_argument(
        "--dry-run", action="store_true", help="Show what would be enriched, don't modify files"
    )
    # Goal 5 of js/feat/research-synthesis
    p.add_argument(
        "--only-stale",
        action="store_true",
        help="Only enrich open questions with cycles_open >= --stale-threshold",
    )
    p.add_argument(
        "--stale-threshold",
        type=int,
        default=3,
        help="Cycles-open threshold for --only-stale (default 3)",
    )
    p.add_argument(
        "--cycle-log",
        type=Path,
        default=DEFAULT_CYCLE_LOG,
        help="Path to cycle-log.md (used for staleness calculation)",
    )
    p.add_argument(
        "--report",
        type=Path,
        default=None,
        help=f"Write stale-questions diagnostic to this path (default: {DEFAULT_STALE_REPORT})",
    )
    p.add_argument(
        "--meta-loop-report",
        type=Path,
        nargs="?",
        const=DEFAULT_META_LOOP_REPORT,
        default=None,
        help="Also splice stale-questions section into the meta-loop report",
    )
    args = p.parse_args()
    return run_cli(
        question=args.question,
        only_stale=args.only_stale,
        stale_threshold=args.stale_threshold,
        cycle_log_path=args.cycle_log,
        dry_run=args.dry_run,
        max_per_question=args.max_per_question,
        report_path=args.report,
        meta_loop_report_path=args.meta_loop_report,
    )


if __name__ == "__main__":
    raise SystemExit(main())
