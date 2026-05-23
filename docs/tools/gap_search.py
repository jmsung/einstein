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
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
QUESTIONS = _REPO / "docs" / "wiki" / "questions"

ARXIV_API = "http://export.arxiv.org/api/query"
ATOM_NS = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
TITLE_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
EXISTING_SUGGESTIONS_RE = re.compile(r"^##\s+Suggested sources", re.MULTILINE)


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
    return fm, text[m.end():]


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
        "", title, flags=re.IGNORECASE
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
    params = urllib.parse.urlencode({
        "search_query": query,
        "start": "0",
        "max_results": str(max_results),
        "sortBy": "relevance",
        "sortOrder": "descending",
    })
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
        title = (entry.findtext("a:title", default="", namespaces=ATOM_NS) or "").strip().replace("\n", " ")
        abs_url = entry.findtext("a:id", default="", namespaces=ATOM_NS) or ""
        summary = (entry.findtext("a:summary", default="", namespaces=ATOM_NS) or "").strip().replace("\n", " ")
        # Authors
        authors = [a.findtext("a:name", default="", namespaces=ATOM_NS) for a in entry.findall("a:author", ATOM_NS)]
        # Year from published date
        published = entry.findtext("a:published", default="", namespaces=ATOM_NS) or ""
        year = published[:4] if published else ""

        results.append({
            "title": title,
            "authors": ", ".join(a for a in authors if a)[:120],
            "year": year,
            "abs_url": abs_url,
            "summary": (summary[:280] + "...") if len(summary) > 280 else summary,
        })
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


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--question", help="Enrich a single question (slug or path)")
    p.add_argument("--max-per-question", type=int, default=3, help="arxiv results per question (default 3)")
    p.add_argument("--dry-run", action="store_true", help="Show what would be enriched, don't modify files")
    args = p.parse_args()

    if args.question:
        # Resolve to path
        cand = QUESTIONS / args.question
        if not cand.exists() and not cand.name.endswith(".md"):
            cand = QUESTIONS / f"{args.question}.md"
        if not cand.exists():
            # Try fuzzy match
            matches = list(QUESTIONS.glob(f"*{args.question}*.md"))
            if len(matches) == 1:
                cand = matches[0]
            elif not matches:
                print(f"No question found matching '{args.question}'", file=sys.stderr)
                sys.exit(1)
            else:
                print(f"Ambiguous: {[m.name for m in matches]}", file=sys.stderr)
                sys.exit(1)
        targets = [cand]
    else:
        targets = sorted(QUESTIONS.glob("*.md"))

    updated = 0
    for path in targets:
        if path.name == "README.md":
            continue
        if enrich_question(path, args.max_per_question, args.dry_run):
            updated += 1

    print(f"\n{'Would update' if args.dry_run else 'Updated'} {updated} question(s).")


if __name__ == "__main__":
    main()
