#!/usr/bin/env python3
"""wiki_graph.py — FLT-style gap-detector for the einstein wiki.

Builds the wiki as a graph (existing citation links) layered with a semantic
similarity layer (from qmd embeddings). The combination surfaces "missing
connection" candidates — pages that the wiki *thinks* are related but nobody
wrote down.

Five gap types detected:
- TYPE 1 — missing concept   : noun phrase mentioned ≥3 times, no own page
- TYPE 2 — missing connection: high semantic similarity, no explicit citation
- TYPE 4 — missing chain     : long shortest-path between high-similarity pages
- TYPE 5 — missing umbrella  : cluster of related pages with no abstracting concept

(TYPE 3 — structural analogy across problem statements — is LLM-only;
documented in `wiki/findings/finding-the-fertile-gaps.md` but not built here.)

Usage:
    uv run python tools/wiki_graph.py                      # full report -> stdout
    uv run python tools/wiki_graph.py --out agent/wiki-gaps-2026-05-02.md
    uv run python tools/wiki_graph.py --file-questions     # auto-file top-3 as wiki/questions/

Companion: cross-pollination-not-compute.md (the filter for which candidates
to keep). This tool says what to *consider*. Together = the discipline.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

WIKI = Path("/Users/jongmin/projects/einstein/cb/wiki")
SOURCE = Path("/Users/jongmin/projects/einstein/cb/source")
QUESTIONS = WIKI / "questions"
AGENT_OUT = Path("/Users/jongmin/projects/einstein/cb/agent")

SIMILARITY_THRESHOLD = 0.50  # qmd score above which we treat as latent edge
                              # (was 0.70 — first run found 0 hits; lowered to 0.50 per
                              # 2026-05-02 tuning. Documented in finding-the-fertile-gaps "Limits".)
LONG_PATH_THRESHOLD = 4  # path length > this between high-similarity pages = chain gap
UMBRELLA_CLUSTER_MIN = 4  # min pages in a tight cluster to flag as needing concept


def parse_page(path: Path) -> dict:
    """Parse a wiki page: extract title, frontmatter, outbound links."""
    text = path.read_text()
    out = {"path": path, "rel_path": str(path.relative_to(WIKI)), "frontmatter": {},
           "title": None, "body": text, "links_out": set(), "concepts_mentioned": set()}

    # Frontmatter
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if m:
        fm_text = m.group(1)
        out["body"] = text[m.end():]
        # Crude YAML parse — sufficient for our flat frontmatter
        fm = {}
        current_list = None
        for line in fm_text.splitlines():
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
                # inline list e.g. [a.md, b.md]
                items = [s.strip().strip("\"'") for s in val.strip("[]").split(",") if s.strip()]
                fm[key] = items
                current_list = None
            else:
                fm[key] = val.strip().strip("\"'")
                current_list = None
        out["frontmatter"] = fm
        # cites: are explicit edges
        for cite in fm.get("cites", []) or []:
            out["links_out"].add(_normalize_link(cite, path))
        for rel_field in ("related_techniques", "related_concepts", "related_findings",
                          "related_problems", "techniques_used", "concepts_invoked",
                          "findings_produced", "synthesized_into", "answer_finding"):
            v = fm.get(rel_field)
            if not v:
                continue
            if isinstance(v, list):
                for item in v:
                    out["links_out"].add(_normalize_link(item, path))
            elif isinstance(v, str):
                out["links_out"].add(_normalize_link(v, path))

    # Title from H1
    tm = re.search(r"^#\s+(.+?)$", out["body"], re.MULTILINE)
    if tm:
        out["title"] = tm.group(1).strip()
    else:
        out["title"] = path.stem

    # Body markdown links: [text](path.md) — only intra-wiki
    for href in re.findall(r"\]\(([^)]+\.md)[^)]*\)", out["body"]):
        out["links_out"].add(_normalize_link(href, path))

    # Body wiki-links: [[path/to/page]]
    for href in re.findall(r"\[\[([^\]]+)\]\]", out["body"]):
        out["links_out"].add(_normalize_link(href + ".md" if not href.endswith(".md") else href, path))

    # Concept mentions: capitalized noun phrases (heuristic — Type 1 detection)
    # Restrict to within-line matches (no newlines) and reasonable length.
    for cp in re.findall(r"\b([A-Z][a-z]+(?:[-–][A-Z][a-z]+)*(?:[ \t]+[A-Z][a-z]+){0,3})\b", out["body"]):
        if "\n" in cp or len(cp) > 60:
            continue
        out["concepts_mentioned"].add(cp)

    return out


def _normalize_link(target: str, source_path: Path) -> str | None:
    """Normalize a link to wiki-relative path. Returns None if external/unresolvable."""
    target = target.strip().strip("\"'").lstrip("./")
    # External
    if target.startswith(("http://", "https://", "mailto:")):
        return None
    # Strip P-prefix problem refs like "P19" — these are not pages
    if re.fullmatch(r"P\d+[a-z]?", target):
        return None
    # Strip anchor
    target = target.split("#")[0]
    if not target.endswith(".md"):
        return None
    # Resolve relative to source
    if target.startswith("../"):
        # Source is in WIKI/<category>/<file>; target is sibling
        full = (source_path.parent / target).resolve()
        try:
            return str(full.relative_to(WIKI))
        except ValueError:
            return None
    # Intra-category
    if "/" not in target:
        return f"{source_path.parent.name}/{target}"
    return target


def build_graph(wiki: Path) -> tuple[dict, dict]:
    """Parse all wiki/*.md and return (nodes, edges).
    nodes: {rel_path: page_dict}
    edges: {rel_path: set(target_rel_paths)} (only edges where target exists)
    """
    nodes = {}
    for path in sorted(wiki.rglob("*.md")):
        if path.name in ("CLAUDE.md",):
            continue
        page = parse_page(path)
        nodes[page["rel_path"]] = page

    # Resolve edges to existing pages only
    edges = {rp: set() for rp in nodes}
    for rp, page in nodes.items():
        for target in page["links_out"]:
            if target and target in nodes:
                edges[rp].add(target)
    return nodes, edges


def compute_explicit_stats(nodes, edges):
    """Type 5 partial + general stats: in-degree, orphans, components."""
    in_deg = Counter()
    for src, tgts in edges.items():
        for t in tgts:
            in_deg[t] += 1

    orphans = []  # in-degree 0, excluding entry-points (problems/, home, index, log, README, _synthesis, _inventory)
    entry_patterns = ("home.md", "index.md", "log.md", "README.md", "_synthesis", "_inventory")
    for rp in nodes:
        if any(p in rp for p in entry_patterns):
            continue
        if in_deg[rp] == 0:
            orphans.append(rp)
    orphans.sort()

    # Most cited (load-bearing)
    most_cited = sorted(((rp, c) for rp, c in in_deg.items()), key=lambda x: -x[1])[:15]

    # Out-degree (info-spreading pages)
    out_deg = {rp: len(tgts) for rp, tgts in edges.items()}
    most_outbound = sorted(out_deg.items(), key=lambda x: -x[1])[:10]

    return {"in_deg": in_deg, "out_deg": out_deg, "orphans": orphans,
            "most_cited": most_cited, "most_outbound": most_outbound}


def shortest_paths_undirected(nodes, edges):
    """Return adjacency as undirected for path computations."""
    adj = defaultdict(set)
    for src, tgts in edges.items():
        for t in tgts:
            adj[src].add(t)
            adj[t].add(src)
    return adj


def bfs_shortest_path(adj, src, tgt, max_depth=8):
    """BFS shortest-path length between two nodes; returns inf if disconnected/too long."""
    if src == tgt:
        return 0
    seen = {src}
    frontier = [(src, 0)]
    while frontier:
        node, d = frontier.pop(0)
        if d >= max_depth:
            continue
        for nbr in adj.get(node, ()):
            if nbr == tgt:
                return d + 1
            if nbr not in seen:
                seen.add(nbr)
                frontier.append((nbr, d + 1))
    return float("inf")


def compute_type1_concept_gaps(nodes, edges):
    """Type 1: noun phrases mentioned in 3+ pages with no own page.

    Heuristic: prefer multi-word phrases or hyphenated math-style terms.
    Filter out frontmatter keys, category names, and generic English words.
    Filter out problem-name false positives (these have problems/ pages,
    not concepts/ pages — the detector should not flag them as missing).
    """
    # Existing topic slugs across concepts/, techniques/, personas/
    # (the v2 detector only checked concepts/, so "frank-wolfe" was flagged even
    # after `techniques/frank-wolfe.md` existed).
    topic_slugs = set()
    for rp in nodes:
        if rp.startswith(("concepts/", "techniques/", "personas/")):
            topic_slugs.add(Path(rp).stem.lower())
    # Also pull source/ slugs (paper/blog references) — covers cases like
    # "erich friedman" where the topic exists at source/blog/friedman-packing-records
    # but isn't in concepts/. Walk the source/ tree and add stems.
    source_dir = WIKI.parent / "source"
    if source_dir.exists():
        for p in source_dir.rglob("*.md"):
            topic_slugs.add(p.stem.lower())
    # Problem index slugs with digit prefix stripped: "1-erdos-overlap.md" -> "erdos-overlap"
    problem_slugs = set()
    for rp in nodes:
        if not rp.startswith("problems/"):
            continue
        stem = Path(rp).stem
        # Strip leading digits + optional letter (e.g., "17a-circles-rectangle" -> "circles-rectangle")
        m = re.match(r"^\d+[a-z]?-(.+)$", stem)
        if m:
            problem_slugs.add(m.group(1).lower())
            problem_slugs.add(stem.lower())  # also keep original

    # v6: extract problem-title phrases from H1 lines so detector can skip phrases
    # that are problem-name fragments (e.g., "minimum overlap" from P1's
    # "Erdős Minimum Overlap"; "second autocorrelation" from P3's "Second
    # Autocorrelation Inequality"). Generates all 2-word substrings of each title.
    problem_title_phrases = set()
    for rp, page in nodes.items():
        if not rp.startswith("problems/"):
            continue
        for line in page["body"].splitlines():
            m = re.match(r"^#\s+Problem\s+\d+[a-z]?\s*[—–\-]\s*(.+?)\s*$", line)
            if not m:
                continue
            title_tail = m.group(1)
            # Strip trailing "(n=...)" or similar parentheticals
            title_tail = re.sub(r"\s*\([^)]*\)\s*$", "", title_tail).strip()
            # Lowercase + emit all contiguous 2-word substrings
            words = title_tail.lower().split()
            for i in range(len(words) - 1):
                problem_title_phrases.add(f"{words[i]} {words[i+1]}")
            for i in range(len(words) - 2):
                problem_title_phrases.add(f"{words[i]} {words[i+1]} {words[i+2]}")
            break  # one H1 per page

    # v6: extract author surnames from source/papers/ filenames (year-author-topic.md
    # convention). Filters out proper-name false positives like "erich friedman"
    # where the surname is in source/ but the full name isn't a concept.
    author_surnames = set()
    if source_dir.exists():
        for p in source_dir.rglob("*.md"):
            stem_parts = p.stem.lower().split("-")
            # Skip leading year (4-digit)
            if stem_parts and re.match(r"^\d{4}$", stem_parts[0]):
                stem_parts = stem_parts[1:]
            # Surnames likely sit in the first 1-2 components after year
            for i, part in enumerate(stem_parts[:2]):
                if len(part) >= 5 and part.isalpha():
                    author_surnames.add(part)

    STOPWORDS = {
        # frontmatter / structural
        "concepts", "techniques", "findings", "problems", "questions", "personas",
        "references", "related", "cites", "type", "author", "drafted", "source",
        "status", "related", "private", "compute", "wisdom", "always",
        # markdown / page structure
        "summary", "section", "table", "rule", "page", "wiki", "result",
        "data", "score", "sample", "test", "branch", "agent", "find",
        "key", "value", "list", "overall", "main", "common", "first",
        "second", "third", "lesson", "method", "step", "row", "classic",
        "procedure", "pitfalls", "dispatch", "yes", "no", "open", "closed",
        # arena / project nouns (have their own pages already)
        "tammes", "thomson", "wichmann", "kissing", "modal", "github", "arxiv",
        "einstein", "arena", "score",
        "problem", "problems", "score", "min", "max", "size", "true", "false",
        # parsing artifacts surfaced by v5 detector (2026-05-02 noise pass)
        "triggering", "structure", "uniform", "lattice", "lattices",
        "leech-sloane",  # proper-noun-as-author (paper ref); not a concept gap
        # operational / non-math
        "heartbeat", "worker", "modal-worker",
        # v6: generic abstract nouns surfaced by v5 noise pass (2026-05-03)
        "optimality",  # ends in -ality but is too generic to be a concept gap
    }
    # Multi-word phrase prefixes/suffixes that indicate parsing artifacts
    # (regex catches "For Problem", "The Hardin", etc. — first word is generic)
    PHRASE_PREFIX_NOISE = {"for", "the", "by", "from", "with", "and", "but"}
    PHRASE_SUFFIX_NOISE = {"lesson", "lessons", "rule", "rules", "section",
                           "result", "results", "tammes", "p19", "p22"}

    # Mentions tally
    mention_pages = defaultdict(set)
    for rp, page in nodes.items():
        for cp in page["concepts_mentioned"]:
            phrase = cp.lower()
            slug_form = phrase.replace(" ", "-").replace("–", "-").replace("—", "-")
            # Slug-aliasing: skip if phrase matches any concept/technique/persona slug
            # exactly OR is a substring of one (catches the case where I authored
            # `cohn-elkies-bound.md` to fill the `cohn-elkies` Type-1 gap).
            # Substring is safe within topic_slugs because we exclude problem slugs
            # (which would cause "circle packing" to false-match "circle-packing-square").
            if slug_form in topic_slugs:
                continue
            if any(slug_form in ts or ts in slug_form for ts in topic_slugs if len(ts) >= 6):
                continue
            if slug_form in problem_slugs:
                continue  # has a problems/ page, not a concept gap
            # Also skip if the phrase contains a problem-slug substring (e.g., "first autocorrelation"
            # is the slug of P2's problem page minus the digit prefix)
            if any(slug_form == ps or slug_form == ps.replace("-", " ") for ps in problem_slugs):
                continue
            # v6: skip phrases that are substrings of any problem H1 title
            # (catches "minimum overlap" from "Erdős Minimum Overlap", "second
            # autocorrelation" from "Second Autocorrelation Inequality", etc.)
            if phrase in problem_title_phrases:
                continue
            # v6: skip phrases where any word matches an author surname from source/
            # (catches "erich friedman" where source/blog/friedman-packing-records
            # documents the topic; not a concept gap)
            if any(w in author_surnames for w in phrase.split()):
                continue
            words = phrase.split()
            # Single words: stricter filter
            if len(words) == 1:
                if phrase in STOPWORDS or len(phrase) < 7:
                    continue
                # Single-word should look math-y: contains hyphen or ends in -ness/-tion/-ity/-set/-bound/-theorem/-conjecture
                math_suffixes = ("set", "sets", "bound", "bounds", "theorem", "lemma",
                                 "conjecture", "problem", "principle", "ality", "graph",
                                 "structure", "polynomial", "polynomials", "lattice",
                                 "lattices", "algebra", "algebras", "manifold", "topology",
                                 "ring", "rings", "form", "forms", "group", "groups",
                                 "field", "fields", "ruler", "rulers", "code", "codes")
                if not (any(phrase.endswith(s) for s in math_suffixes) or "-" in phrase):
                    continue
            else:
                # Multi-word: at least one word is math-y or proper-noun-like
                if all(w in STOPWORDS for w in words):
                    continue
                if len(phrase) < 8:
                    continue
                # Filter parsing-artifact prefixes/suffixes ("for problem", "the hardin", etc.)
                if words[0] in PHRASE_PREFIX_NOISE:
                    continue
                if words[-1] in PHRASE_SUFFIX_NOISE:
                    continue
            mention_pages[phrase].add(rp)
    candidates = [(p, len(srcs), sorted(srcs)[:3]) for p, srcs in mention_pages.items() if len(srcs) >= 3]
    candidates.sort(key=lambda x: -x[1])
    return candidates[:20]


def qmd_semantic_neighbors(query_text: str, k: int = 8) -> list[tuple[str, float]]:
    """Run qmd vsearch (vector-only, faster than full hybrid query) for the query.
    Returns [(rel_path, score), ...] over einstein-wiki collection.
    """
    try:
        result = subprocess.run(
            ["qmd", "vsearch", query_text, "-c", "einstein-wiki", "-n", str(k)],
            capture_output=True, text=True, timeout=15,
        )
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return []
    if result.returncode != 0:
        return []
    # Parse output: lines like "qmd://einstein-wiki/path:line ..." then "Score: NN%"
    neighbors = []
    cur_path = None
    for line in result.stdout.splitlines():
        m = re.match(r"qmd://einstein-wiki/([^\s:]+)(?::\d+)?", line)
        if m:
            cur_path = m.group(1)
            continue
        sm = re.match(r"\s*Score:\s+(\d+)%", line)
        if sm and cur_path:
            score = int(sm.group(1)) / 100.0
            neighbors.append((cur_path, score))
            cur_path = None
    return neighbors


def compute_type2_connection_gaps(nodes, edges, max_pages=80):
    """Type 2: high semantic similarity (qmd) but no explicit edge.

    For each page, query qmd for semantic neighbors. Pairs (A, B) with
    score ≥ SIMILARITY_THRESHOLD AND no edge in either direction = candidates.
    """
    adj = shortest_paths_undirected(nodes, edges)
    candidates = []
    seen_pairs = set()
    keys = list(nodes.keys())[:max_pages]  # cap for speed
    for i, rp in enumerate(keys):
        if not nodes[rp]["title"]:
            continue
        if i % 20 == 0:
            print(f"    qmd progress: {i}/{len(keys)}", file=sys.stderr)
        neighbors = qmd_semantic_neighbors(nodes[rp]["title"], k=6)
        for nbr_path, score in neighbors:
            if nbr_path == rp or nbr_path not in nodes:
                continue
            if score < SIMILARITY_THRESHOLD:
                continue
            # Check explicit edge in either direction
            if nbr_path in adj.get(rp, set()):
                continue
            pair = tuple(sorted([rp, nbr_path]))
            if pair in seen_pairs:
                continue
            seen_pairs.add(pair)
            candidates.append({"a": pair[0], "b": pair[1], "similarity": score})
    candidates.sort(key=lambda c: -c["similarity"])
    return candidates[:20]


def compute_type4_chain_gaps(nodes, edges, type2_candidates):
    """Type 4: long shortest-path between high-similarity pairs.

    For pairs from Type 2 (high semantic similarity, no edge), compute
    shortest explicit-path. Pairs with path > LONG_PATH_THRESHOLD = chain gaps.
    """
    adj = shortest_paths_undirected(nodes, edges)
    chains = []
    for c in type2_candidates:
        d = bfs_shortest_path(adj, c["a"], c["b"], max_depth=6)
        if d == float("inf") or d > LONG_PATH_THRESHOLD:
            chains.append({"a": c["a"], "b": c["b"], "similarity": c["similarity"],
                           "path_length": "∞" if d == float("inf") else d})
    return chains[:10]


def compute_type5_umbrella_gaps(nodes, edges):
    """Type 5: clusters of pages on same topic without an abstracting concept.

    Heuristic: groups of pages whose qmd-similar neighborhoods overlap heavily
    but no concept page sits at the cluster centroid.

    Implementation: for each finding/technique page, get its top-3 qmd neighbors.
    If those neighbors are NOT concept pages, this page is in a "loose" cluster
    that may need a concept umbrella.
    """
    candidates = []
    findings_techniques = [rp for rp in nodes if rp.startswith(("findings/", "techniques/"))][:60]
    for rp in findings_techniques:
        if not nodes[rp]["title"]:
            continue
        nbrs = qmd_semantic_neighbors(nodes[rp]["title"], k=6)  # k=6 to leave room after self-filter
        # Exclude self from neighbor list (self-cluster bug fix)
        nbr_paths = [n[0] for n in nbrs if n[0] != rp and n[1] >= 0.5]
        if len(nbr_paths) < 2:
            continue  # too few real neighbors to form a cluster
        concept_in_nbrs = any(p.startswith("concepts/") for p in nbr_paths)
        if concept_in_nbrs:
            continue
        # No concept in the top neighborhood → may need an umbrella
        candidates.append({"page": rp, "neighbors_no_concept": nbr_paths[:3]})
    return candidates[:10]


def write_report(stats, type1, type2, type4, type5, out_path: Path | None):
    """Write the gap-detector report as markdown."""
    today = dt.date.today().isoformat()
    lines = [
        f"---",
        f"type: gap-report",
        f"author: agent",
        f"drafted: {today}",
        f"tool: tools/wiki_graph.py",
        f"---",
        "",
        f"# Wiki gap report — {today}",
        "",
        "Generated by `tools/wiki_graph.py`. The cross-pollination-not-compute filter says *which* candidates to keep; this report says *which* candidates to even consider.",
        "",
        "## General stats",
        "",
        f"- Total pages: {sum(1 for _ in stats['in_deg']) + len(stats['orphans']) + 7}",
        f"- Orphan pages (in-degree 0, excluding entry-points): {len(stats['orphans'])}",
        f"- Most-cited (load-bearing) pages — top 5:",
    ]
    for rp, c in stats["most_cited"][:5]:
        lines.append(f"  - `{rp}` ({c} incoming citations)")
    lines.append("")

    # Type 1
    lines += ["## Type 1 — Missing concept (mentioned ≥3 times, no own page)", ""]
    if not type1:
        lines.append("_None detected._")
    for phrase, count, sample in type1[:15]:
        lines.append(f"- **`{phrase}`** — mentioned in {count} pages. Sample: {', '.join(sample)}")
    lines.append("")

    # Type 2
    lines += ["## Type 2 — Missing connection (high similarity, no explicit edge)", ""]
    if not type2:
        lines.append("_None detected._")
    for c in type2[:15]:
        lines.append(f"- `{c['a']}` ↔ `{c['b']}` (similarity {c['similarity']:.2f})")
    lines.append("")

    # Type 4
    lines += ["## Type 4 — Missing chain (long path between similar pages)", ""]
    if not type4:
        lines.append("_None detected._")
    for c in type4:
        lines.append(f"- `{c['a']}` → … → `{c['b']}` (similarity {c['similarity']:.2f}, current path length {c['path_length']})")
    lines.append("")

    # Type 5
    lines += ["## Type 5 — Missing umbrella (cluster of pages with no concept centroid)", ""]
    if not type5:
        lines.append("_None detected._")
    for c in type5:
        lines.append(f"- `{c['page']}` clusters with: {', '.join(c['neighbors_no_concept'])}")
    lines.append("")

    # Orphans (informational)
    lines += ["## Orphan pages (informational — many are by-design entry points)", ""]
    for o in stats["orphans"]:
        lines.append(f"- `{o}`")
    lines.append("")

    body = "\n".join(lines)
    if out_path:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(body)
        print(f"\n✓ Report written to {out_path}", file=sys.stderr)
    return body


def file_top_questions(type1, type2, today: str, n: int = 3) -> list[Path]:
    """File top-N gap candidates as wiki/questions/ pages for next cycle to pick up."""
    files_written = []
    QUESTIONS.mkdir(parents=True, exist_ok=True)
    rank = 0
    for c in type2[:n]:
        rank += 1
        slug = f"gap-{Path(c['a']).stem}-vs-{Path(c['b']).stem}"[:60]
        out = QUESTIONS / f"{today}-{slug}.md"
        out.write_text(
            f"---\n"
            f"type: question\n"
            f"author: agent\n"
            f"drafted: {today}\n"
            f"status: open\n"
            f"asked_by: gap-detector\n"
            f"related_pages: [{c['a']}, {c['b']}]\n"
            f"gap_type: type-2-missing-connection\n"
            f"similarity: {c['similarity']:.2f}\n"
            f"---\n"
            f"\n"
            f"# Connection gap: `{c['a']}` ↔ `{c['b']}`\n"
            f"\n"
            f"## Question\n"
            f"\n"
            f"qmd reports semantic similarity {c['similarity']:.2f} between these two pages, but there is no explicit citation in either direction. What is the missing connection?\n"
            f"\n"
            f"## Why it matters\n"
            f"\n"
            f"Per `wiki/findings/finding-the-fertile-gaps.md`: pages with high semantic similarity but no explicit link likely share an underlying concept that hasn't been articulated. Either:\n"
            f"\n"
            f"1. The connection is real and a bridge page should be authored, OR\n"
            f"2. The similarity is superficial (qmd false-positive) and we should note that.\n"
            f"\n"
            f"## Next step\n"
            f"\n"
            f"Read both pages. If a structural connection exists, file as `wiki/findings/<bridge-slug>.md`. If not, close this question with `status: superseded` and a one-line explanation.\n"
        )
        files_written.append(out)
    return files_written


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--out", help="Output report path (default: stdout)")
    p.add_argument("--file-questions", action="store_true",
                   help="Auto-file top-3 Type-2 candidates as wiki/questions/")
    p.add_argument("--no-qmd", action="store_true",
                   help="Skip semantic-similarity layer (faster; Types 1, 5 only)")
    args = p.parse_args()

    print("Building wiki graph from explicit citations...", file=sys.stderr)
    nodes, edges = build_graph(WIKI)
    print(f"  {len(nodes)} pages, {sum(len(e) for e in edges.values())} explicit edges", file=sys.stderr)

    print("Computing explicit-graph stats (orphans, in-degree)...", file=sys.stderr)
    stats = compute_explicit_stats(nodes, edges)

    print("Computing Type 1 — missing concept candidates...", file=sys.stderr)
    type1 = compute_type1_concept_gaps(nodes, edges)

    type2, type4, type5 = [], [], []
    if not args.no_qmd:
        print("Computing Type 2 — missing connection candidates (qmd vsearch)...", file=sys.stderr)
        type2 = compute_type2_connection_gaps(nodes, edges)
        print("Computing Type 4 — chain gap candidates...", file=sys.stderr)
        type4 = compute_type4_chain_gaps(nodes, edges, type2)
        print("Computing Type 5 — umbrella gap candidates...", file=sys.stderr)
        type5 = compute_type5_umbrella_gaps(nodes, edges)

    today = dt.date.today().isoformat()
    out_path = Path(args.out) if args.out else None
    body = write_report(stats, type1, type2, type4, type5, out_path)
    if not out_path:
        print(body)

    if args.file_questions and type2:
        files = file_top_questions(type1, type2, today, n=3)
        for f in files:
            print(f"  filed: {f}", file=sys.stderr)


if __name__ == "__main__":
    main()
