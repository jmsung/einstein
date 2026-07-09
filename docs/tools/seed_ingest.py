#!/usr/bin/env python3
"""seed_ingest.py — bulk-ingest arxiv papers to fill wiki coverage gaps.

Two-step pipeline (human-gated between):

    1. propose:  concept-coverage.json  →  seed-candidates.json
       Walks `under-sourced` + `missing-page` rows; for each, runs
       gap_search.search_arxiv and writes the top-N hits with
       `approved: null` flags.

    2. apply:    seed-candidates.json   →  knowledge/source/<slug>.md
       For each candidate with `approved: true`, downloads the PDF
       to knowledge/raw/papers/<slug>.pdf, runs pdf_to_md to extract
       markdown, and writes the source/ entry with proper
       frontmatter (author: agent, cites, ingested_for_concept).

Between (1) and (2) the human reviews the candidates JSON and sets
`approved: true` for the rows they want. Re-running `propose` is
safe — existing approval flags are preserved.

Usage:
    # Step 1 — propose
    uv run python docs/tools/seed_ingest.py propose \\
        --coverage docs/agent/concept-coverage.json \\
        --out docs/agent/seed-candidates.json \\
        --top-n 5

    # (human reviews + sets approved: true in seed-candidates.json)

    # Step 2 — apply
    uv run python docs/tools/seed_ingest.py apply \\
        --candidates docs/agent/seed-candidates.json
    uv run python docs/tools/seed_ingest.py apply \\
        --candidates docs/agent/seed-candidates.json --dry-run
"""
from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import json
import logging
import re
import sys
import time
import urllib.request
from pathlib import Path
from urllib.error import HTTPError, URLError

# Local imports — sibling tools
_TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(_TOOLS))

from gap_search import MATH_CATEGORIES, build_query, search_arxiv  # type: ignore[import-not-found]
import pdf_to_md  # type: ignore[import-not-found]

try:
    import llm_distill  # type: ignore[import-not-found]
except ImportError:  # pragma: no cover
    llm_distill = None  # type: ignore[assignment]

try:
    import yaml  # type: ignore[import-not-found]
except ImportError:  # pragma: no cover — pyyaml is a project dep
    yaml = None  # type: ignore[assignment]

_REPO = Path(__file__).resolve().parents[2]  # cb/ root
log = logging.getLogger("seed_ingest")

ACTIONABLE_CLASSIFICATIONS = {"under-sourced", "missing-page"}
MAX_SLUG_LEN = 60
ARXIV_RATE_LIMIT_SECONDS = 3.5  # arxiv.org policy: ≥3 s between API hits
DEFAULT_VOCAB_PATH = _TOOLS / "concept-search-terms.yaml"
DEFAULT_AUTHORS_PATH = _TOOLS / "seed-authors.yaml"


# ---------------- pure helpers ----------------


def _slug_from_metadata(*, title: str, year: str, authors: str) -> str:
    """Build a `<year>-<author-surname>-<topic>` slug for source/ filename.

    Conservative: kebab-case, lowercase, alnum + hyphen only, length-capped.
    """
    # First-author surname: grab the last whitespace-separated token of the first comma-segment
    first_author = authors.split(",")[0].strip() if authors else ""
    parts = first_author.split()
    surname = parts[-1] if parts else "anon"
    surname = re.sub(r"[^a-zA-Z]", "", surname).lower() or "anon"

    # Title → first ~4 informative words
    cleaned = re.sub(r"[^a-zA-Z0-9\s-]", " ", title.lower())
    words = [w for w in cleaned.split() if len(w) >= 3]
    stop = {"the", "and", "for", "with", "from", "via", "into", "over",
            "this", "that", "these", "those", "are", "was", "were"}
    words = [w for w in words if w not in stop]
    topic = "-".join(words[:4]) or "untitled"

    year_clean = re.sub(r"[^0-9]", "", year)[:4] or "0000"
    slug = f"{year_clean}-{surname}-{topic}"
    slug = re.sub(r"-+", "-", slug).strip("-")
    if len(slug) > MAX_SLUG_LEN:
        slug = slug[:MAX_SLUG_LEN].rstrip("-")
    return slug


def _abs_to_pdf_url(url: str) -> str:
    """arxiv abs URL → pdf URL; passes through non-abs URLs."""
    if "/abs/" in url:
        return url.replace("/abs/", "/pdf/") + (".pdf" if not url.endswith(".pdf") else "")
    return url


def _build_source_frontmatter(*, candidate: dict, concept: str | None = None,
                              problem_refs: list[int] | None = None,
                              topic: str | None = None,
                              source_type: str = "arxiv") -> dict:
    """Construct the YAML frontmatter dict for a knowledge/source/ entry.

    Two modes:
      - concept-bound: `concept` + `problem_refs` set. Frontmatter cites the
        concept page and per-problem stubs.
      - general-knowledge: `concept=None`. `topic` (e.g. 'agentic-harness',
        'math-by-ai') replaces `ingested_for_concept`.
    """
    today = dt.date.today().isoformat()
    cites: list[str] = []
    if concept:
        cites.append(f"../wiki/concepts/{concept}")
        for pid in problem_refs or []:
            cites.append(f"../wiki/problems/{pid}-*.md")

    fm: dict = {
        "type": "source",
        "kind": "paper",
        "title": candidate["title"],
        "authors": candidate.get("authors", ""),
        "year": candidate.get("year", ""),
        "author": "agent",
        "drafted": today,
        "ingested_at": today,
        "source_type": source_type,
        "source_url": candidate["abs_url"],
        "source_local": f"../raw/{candidate['slug']}.pdf",
    }
    if concept:
        fm["ingested_for_concept"] = concept
    if topic:
        fm["topic"] = topic
    fm["cites"] = cites
    return fm


def _frontmatter_to_yaml(fm: dict) -> str:
    """Tiny YAML serializer for our flat frontmatter dicts (no nesting).

    Matches existing knowledge/source/ style: URLs + DOI strings stay unquoted
    (a bare `:` is fine in YAML unless followed by space); titles with
    `: ` get quoted; leading/trailing whitespace forces quoting.
    """
    lines = ["---"]
    for k, v in fm.items():
        if isinstance(v, list):
            lines.append(f"{k}:")
            for item in v:
                lines.append(f"  - {item}")
        else:
            sval = str(v)
            needs_quote = (
                ": " in sval
                or sval.startswith(("#", "&", "*", "!", "|", ">", "[", "{", "@", "`"))
                or sval != sval.strip()
            )
            if needs_quote:
                escaped = sval.replace('"', '\\"')
                lines.append(f'{k}: "{escaped}"')
            else:
                lines.append(f"{k}: {sval}")
    lines.append("---")
    return "\n".join(lines) + "\n"


# ---------------- relevance scoring ----------------


def _relevance_score(*, candidate: dict, phrases: list[str]) -> float:
    """Heuristic [0, 1] relevance of an arxiv candidate to the search phrases.

    Composed of:
      - keyword overlap (0..0.85): fraction of phrase words appearing in
        title + summary, weighted: title hits 2x summary hits.
      - recency bonus (0..0.15): newer papers get a small lift.

    Heuristic by design — the goal is a useful auto-approve threshold,
    not a perfect ranker. Threshold tuning happens at the caller.
    """
    title = candidate.get("title", "").lower()
    summary = candidate.get("summary", "").lower()
    year_raw = candidate.get("year", "0")
    try:
        year = int(re.sub(r"[^0-9]", "", year_raw)[:4] or "0")
    except ValueError:
        year = 0

    # Tokenize phrases into words (excluding stop-y short ones)
    words: set[str] = set()
    for p in phrases:
        for w in re.split(r"[^a-zA-Z0-9]+", p.lower()):
            if len(w) >= 3:
                words.add(w)
    if not words:
        return 0.0

    # Count weighted hits
    title_hits = sum(1 for w in words if w in title)
    summary_hits = sum(1 for w in words if w in summary)
    # Title weighted 2x; max possible = 3 * len(words)
    weighted_hits = 2 * title_hits + summary_hits
    overlap_score = min(weighted_hits / (3 * len(words)), 1.0)

    # Recency: linear bonus for papers from 2020+, capped at 2026.
    if year >= 2020:
        recency_score = min((year - 2020) / 6.0, 1.0)
    else:
        recency_score = 0.0

    return 0.85 * overlap_score + 0.15 * recency_score


# ---------------- vocab mapping ----------------


def _load_vocab(path: Path) -> dict[str, list[str]]:
    """Load slug → list[phrase] mapping from YAML; empty dict if file absent."""
    if not Path(path).is_file():
        return {}
    if yaml is None:  # pragma: no cover
        log.warning("PyYAML not installed; ignoring vocab file %s", path)
        return {}
    data = yaml.safe_load(Path(path).read_text()) or {}
    out: dict[str, list[str]] = {}
    for k, v in data.items():
        if v is None:
            out[k] = []
        elif isinstance(v, list):
            out[k] = [str(p) for p in v]
        else:
            log.warning("vocab entry %s has non-list value (%r); ignoring", k, v)
    return out


def _build_vocab_query(phrases: list[str]) -> str:
    """OR each phrase in arxiv `all:"..."` form; AND with the math-category filter."""
    cleaned = [re.sub(r'[\\"]', "", p).strip() for p in phrases if p and p.strip()]
    if not cleaned:
        return ""
    kw_query = " OR ".join(f'all:"{p}"' for p in cleaned)
    cat_query = " OR ".join(f"cat:{c}" for c in MATH_CATEGORIES)
    return f"({kw_query}) AND ({cat_query})"


# ---------------- citation-graph crawl ----------------

S2_API_BASE = "https://api.semanticscholar.org/graph/v1/paper"
S2_REFERENCES_FIELDS = "externalIds,title,abstract,year,authors"


def _collect_arxiv_ids(source_dir: Path) -> list[str]:
    """Scan knowledge/source/*.md frontmatter for arxiv ids — version-stripped."""
    ids: set[str] = set()
    if not source_dir.is_dir():
        return []
    arxiv_re = re.compile(r"arxiv\.org/(?:abs|pdf)/([^v\s\"'?#]+(?:\.[^v\s\"'?#]+)?)")
    for path in source_dir.glob("*.md"):
        try:
            text = path.read_text()
        except OSError:
            continue
        m = arxiv_re.search(text)
        if m:
            stem = re.sub(r"v\d+$", "", m.group(1))
            stem = re.sub(r"\.pdf$", "", stem)
            ids.add(stem)
    return sorted(ids)


def _s2_refs_to_candidates(refs: list[dict]) -> list[dict]:
    """Map semanticscholar reference records → seed_ingest candidate dicts.

    Drops references without an arxiv id (s2 includes DOI-only papers we
    can't fetch via arxiv).
    """
    out: list[dict] = []
    for r in refs:
        ext_ids = r.get("externalIds") or {}
        arxiv_id = ext_ids.get("ArXiv") or ext_ids.get("arxiv")
        if not arxiv_id:
            continue
        title = (r.get("title") or "").strip()
        if not title:
            continue
        authors_list = r.get("authors") or []
        authors_str = ", ".join(a.get("name", "") for a in authors_list if a.get("name"))
        year_raw = r.get("year")
        year = str(year_raw) if year_raw else ""
        abs_url = f"https://arxiv.org/abs/{arxiv_id}"
        cand = {
            "title": title,
            "authors": authors_str,
            "year": year,
            "abs_url": abs_url,
            "summary": (r.get("abstract") or "")[:500],
        }
        cand["slug"] = _slug_from_metadata(title=title, year=year, authors=authors_str)
        out.append(cand)
    return out


def _s2_fetch_references(arxiv_id: str) -> list[dict]:
    """Fetch the 'references' list for an arxiv paper via semanticscholar.

    Returns a list of s2 reference records. On failure, returns empty list.
    """
    url = f"{S2_API_BASE}/ARXIV:{arxiv_id}/references?fields={S2_REFERENCES_FIELDS}&limit=200"
    req = urllib.request.Request(url, headers={
        "User-Agent": "einstein-seed-ingest/1",
        "Accept": "application/json",
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
    except HTTPError as e:
        if e.code == 429:
            log.warning("s2 429 for %s — back off + retry", arxiv_id)
            time.sleep(8)
            try:
                with urllib.request.urlopen(req, timeout=30) as resp:
                    data = json.loads(resp.read())
            except Exception as e2:
                log.error("s2 retry failed for %s: %s", arxiv_id, e2)
                return []
        else:
            log.warning("s2 HTTP %d for %s: %s", e.code, arxiv_id, e)
            return []
    except (URLError, json.JSONDecodeError, TimeoutError) as e:
        log.warning("s2 fetch failed for %s: %s", arxiv_id, e)
        return []

    # s2 wraps each reference as {"citedPaper": {...}}
    refs: list[dict] = []
    for entry in data.get("data", []):
        cited = entry.get("citedPaper") or {}
        if cited:
            refs.append(cited)
    return refs


def citation_crawl(
    *,
    arxiv_ids: list[str],
    source_dir: Path,
    rate_limit_seconds: float = 1.0,
    max_refs_per_paper: int = 200,
) -> list[dict]:
    """Crawl semanticscholar references for each arxiv id; dedup against existing.

    Returns a flat list of candidate dicts (approved=None) ready to be
    folded into a candidates JSON. Rate-limited politely; semanticscholar
    is more permissive than arxiv (often 100 req/sec with API key) so the
    default delay is conservative-1s without an API key.
    """
    existing_seen = _existing_source_urls(source_dir)
    # Also dedup against arxiv IDs we just crawled (a ref appearing in two source
    # papers should only show up once in the candidates).
    seen_arxiv: set[str] = set()
    for url in existing_seen:
        stem = _arxiv_id_stem(url)
        if stem:
            seen_arxiv.add(stem)

    candidates: list[dict] = []
    for i, aid in enumerate(arxiv_ids):
        log.info("[%d/%d] citation-crawl: %s", i + 1, len(arxiv_ids), aid)
        refs = _s2_fetch_references(aid)[:max_refs_per_paper]
        cand_dicts = _s2_refs_to_candidates(refs)
        fresh = 0
        for c in cand_dicts:
            stem = _arxiv_id_stem(c["abs_url"])
            if stem in seen_arxiv:
                continue
            seen_arxiv.add(stem)
            c["approved"] = None
            c["relevance"] = round(
                _relevance_score(candidate=c, phrases=["mathematics", "optimization"]), 4
            )
            candidates.append(c)
            fresh += 1
        log.info("    %d refs → %d fresh", len(cand_dicts), fresh)
        if i + 1 < len(arxiv_ids) and rate_limit_seconds > 0:
            time.sleep(rate_limit_seconds)
    log.info("citation_crawl: %d fresh candidates across %d source papers",
             len(candidates), len(arxiv_ids))
    return candidates


# ---------------- author + category sweep helpers ----------------


def _load_authors(path: Path) -> dict[str, list[str]]:
    """{category: [author-name, ...]} — same shape as vocab loader."""
    if not Path(path).is_file():
        return {}
    if yaml is None:  # pragma: no cover
        return {}
    data = yaml.safe_load(Path(path).read_text()) or {}
    return {k: [str(a) for a in v] for k, v in data.items() if isinstance(v, list)}


def _build_author_query(author: str) -> str:
    """Build an arxiv query: au:"Name" AND (cat:math.* OR ...)."""
    cat_query = " OR ".join(f"cat:{c}" for c in MATH_CATEGORIES)
    return f'au:"{author}" AND ({cat_query})'


def _arxiv_id_stem(abs_url: str) -> str:
    """Pull the bare arxiv id from any abs/pdf URL — drops vN suffix.

    'http://arxiv.org/abs/1234.5678v1' → '1234.5678'
    'https://arxiv.org/pdf/2604.25850.pdf' → '2604.25850'
    """
    m = re.search(r"arxiv\.org/(?:abs|pdf)/([^v?.]+(?:\.[^v?]+)?)", abs_url)
    if not m:
        return abs_url
    stem = m.group(1)
    # Strip trailing version suffix like v1, v2
    stem = re.sub(r"v\d+$", "", stem)
    # Strip pdf extension
    stem = re.sub(r"\.pdf$", "", stem)
    return stem


def _existing_source_urls(source_dir: Path) -> set[str]:
    """Scan knowledge/source/*.md frontmatter for arxiv ids already ingested."""
    seen: set[str] = set()
    if not source_dir.is_dir():
        return seen
    for path in source_dir.glob("*.md"):
        try:
            text = path.read_text()
        except OSError:
            continue
        m = re.search(r"^source_url:\s*(.+)$", text, re.MULTILINE)
        if not m:
            continue
        url = m.group(1).strip().strip("\"'")
        seen.add(url)
        # Also store the bare arxiv id for loose-match
        stem = _arxiv_id_stem(url)
        if stem and stem != url:
            seen.add(stem)
            seen.add(f"arxiv:{stem}")
    return seen


def _filter_already_ingested(candidates: list[dict], seen: set[str]) -> list[dict]:
    """Drop candidates whose arxiv abs URL (or id stem) is already in `seen`."""
    fresh: list[dict] = []
    for c in candidates:
        url = c.get("abs_url", "")
        stem = _arxiv_id_stem(url)
        # Check both raw URL and stem (versions diverge: v1 vs v2 same paper)
        if url in seen:
            continue
        if stem and any(stem in s or s in stem for s in seen):
            continue
        fresh.append(c)
    return fresh


def author_sweep(
    *,
    authors_yaml: Path,
    out_path: Path,
    top_n: int = 5,
    rate_limit_seconds: float = ARXIV_RATE_LIMIT_SECONDS,
    source_dir: Path | None = None,
    auto_approve_threshold: float | None = None,
) -> None:
    """Iterate over (category, author) pairs from authors yaml; arxiv au: search
    per author; filter against existing source/; write candidates JSON.

    Output shape matches `propose()` so `apply()` can consume it directly:
    each (category, author) becomes one block with `kind: author-sweep`.
    """
    authors = _load_authors(authors_yaml)
    if not authors:
        log.warning("no authors loaded from %s", authors_yaml)
        return

    src_dir = source_dir if source_dir is not None else (_REPO / "knowledge" / "source")
    seen = _existing_source_urls(src_dir)
    log.info("author-sweep: %d known source URLs to dedup against", len(seen))

    pairs: list[tuple[str, str]] = [(cat, a) for cat, authors_list in authors.items() for a in authors_list]
    log.info("author-sweep: %d (category, author) queries", len(pairs))

    blocks: list[dict] = []
    for i, (category, author) in enumerate(pairs):
        query = _build_author_query(author)
        log.info("[%d/%d] %s — %s", i + 1, len(pairs), author, category)
        try:
            results = search_arxiv(query, max_results=top_n)
        except Exception as e:
            log.error("    search failed: %s", e)
            results = []

        # Sort newest first so the top-N is the latest work
        results.sort(key=lambda r: r.get("year", ""), reverse=True)
        fresh = _filter_already_ingested(results, seen)
        log.info("    %d hits → %d new", len(results), len(fresh))

        n_auto = 0
        for r in fresh:
            r["slug"] = _slug_from_metadata(
                title=r["title"], year=r.get("year", ""), authors=r.get("authors", "")
            )
            r["approved"] = None
            r["relevance"] = round(
                _relevance_score(candidate=r, phrases=[author, category.replace("-", " ")]),
                4,
            )
            if auto_approve_threshold is not None and r["relevance"] >= auto_approve_threshold:
                r["approved"] = True
                r["auto_approved"] = True
                n_auto += 1
        if auto_approve_threshold is not None and n_auto:
            log.info("    auto-approved %d/%d", n_auto, len(fresh))

        # Track every fresh URL so the next author's results don't double-up
        for r in fresh:
            seen.add(r["abs_url"])
            seen.add(_arxiv_id_stem(r["abs_url"]))

        blocks.append({
            "kind": "author-sweep",
            "category": category,
            "author": author,
            "query": query,
            "candidates": fresh,
        })

        if i + 1 < len(pairs) and rate_limit_seconds > 0:
            time.sleep(rate_limit_seconds)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps({
        "generated_at": dt.date.today().isoformat(),
        "concepts": blocks,
    }, indent=2) + "\n")
    total = sum(len(b["candidates"]) for b in blocks)
    log.info("author-sweep complete: %d fresh candidates across %d blocks → %s",
             total, len(blocks), out_path)


# ---------------- problem-sweep (8.2) ----------------

# Problem statuses for which problem-sweep SKIPS arxiv querying.
# Only `retired` (removed from arena) is in the default skip-list — local
# `conquered` often means "JSAgent reached its internal target," not "arena
# floor hit"; other agents may still compete. Caller passes `--exclude P6`
# for the rare arena-theoretical-floor case (e.g. score=0 on kissing-d11).
PROBLEM_SWEEP_SKIP_STATUSES = {"retired"}


def _parse_problem_frontmatter(path: Path) -> dict | None:
    """Pull a minimal problem-page record from frontmatter.

    Returns dict with keys: problem_id (int|None), status (str), slug (str),
    concepts_invoked (list[str]), techniques_used (list[str]), path (Path).
    Returns None if the file is not a parseable problem page.
    """
    try:
        text = path.read_text()
    except OSError:
        return None
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end < 0:
        return None
    fm_block = text[3:end].strip()

    def _scalar(key: str) -> str | None:
        m = re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", fm_block, re.MULTILINE)
        return m.group(1).strip() if m else None

    def _list(key: str) -> list[str]:
        m = re.search(rf"^{re.escape(key)}:\s*\[(.*?)\]\s*$", fm_block, re.MULTILINE | re.DOTALL)
        if not m:
            return []
        raw = m.group(1).strip()
        if not raw:
            return []
        items: list[str] = []
        for piece in raw.split(","):
            piece = piece.strip().strip("\"'")
            if piece:
                items.append(piece)
        return items

    pid_raw = _scalar("problem_id")
    try:
        problem_id = int(pid_raw) if pid_raw and pid_raw.isdigit() else None
    except ValueError:
        problem_id = None

    status = _scalar("status") or ""

    # Slug from filename (strip leading <id>- if present, drop .md)
    stem = path.stem
    slug = re.sub(r"^\d+-", "", stem)

    return {
        "path": path,
        "problem_id": problem_id,
        "status": status,
        "slug": slug,
        "concepts_invoked": _list("concepts_invoked"),
        "techniques_used": _list("techniques_used"),
    }


def _collect_active_problems(problems_dir: Path,
                             skip_statuses: set[str],
                             exclude_ids: set[int]) -> list[dict]:
    """Walk problems_dir, return parsed records for non-skipped, non-excluded problems."""
    records: list[dict] = []
    for p in sorted(problems_dir.glob("[0-9]*.md")):
        rec = _parse_problem_frontmatter(p)
        if rec is None:
            continue
        if rec["status"] in skip_statuses:
            log.info("    skip %s (status=%s)", p.name, rec["status"])
            continue
        if rec["problem_id"] in exclude_ids:
            log.info("    skip %s (excluded)", p.name)
            continue
        records.append(rec)
    return records


def _build_problem_query(*, concepts: list[str], techniques: list[str],
                         vocab: dict[str, list[str]]) -> tuple[str, list[str]]:
    """Build an arxiv query from a problem's concepts+techniques via vocab YAML.

    Returns (query_string, phrase_list). Phrases used for relevance scoring.
    """
    phrases: list[str] = []
    for slug in (*concepts, *techniques):
        phrases.extend(vocab.get(slug, []))
    # Drop empties + dedup, preserve order
    seen_p: set[str] = set()
    deduped: list[str] = []
    for p in phrases:
        if p and p not in seen_p:
            seen_p.add(p)
            deduped.append(p)
    return _build_vocab_query(deduped), deduped


def problem_sweep(
    *,
    problems_dir: Path,
    out_path: Path,
    top_n: int = 10,
    vocab_path: Path | None = None,
    source_dir: Path | None = None,
    exclude: list[int] | None = None,
    skip_statuses: set[str] | None = None,
    auto_approve_threshold: float | None = None,
    rate_limit_seconds: float = ARXIV_RATE_LIMIT_SECONDS,
) -> None:
    """Per-problem arxiv sweep: walks problems_dir, queries arxiv with each
    problem's concept+technique phrase set, writes apply()-compatible JSON.

    Skips retired/conquered problems by default (configurable via skip_statuses).
    Output shape matches author_sweep so apply() can consume it directly.
    """
    vocab_p = vocab_path if vocab_path is not None else DEFAULT_VOCAB_PATH
    vocab = _load_vocab(vocab_p)
    if not vocab:
        log.warning("problem-sweep: empty vocab (%s); queries will be empty", vocab_p)

    src_dir = source_dir if source_dir is not None else (_REPO / "knowledge" / "source")
    seen = _existing_source_urls(src_dir)
    log.info("problem-sweep: %d known source URLs to dedup against", len(seen))

    exclude_set: set[int] = set(exclude or [])
    statuses = skip_statuses if skip_statuses is not None else PROBLEM_SWEEP_SKIP_STATUSES

    records = _collect_active_problems(problems_dir, statuses, exclude_set)
    log.info("problem-sweep: %d active problems to query", len(records))

    blocks: list[dict] = []
    for i, rec in enumerate(records):
        query, phrases = _build_problem_query(
            concepts=rec["concepts_invoked"],
            techniques=rec["techniques_used"],
            vocab=vocab,
        )
        log.info("[%d/%d] P%s — %s (%d phrases)",
                 i + 1, len(records), rec["problem_id"], rec["slug"], len(phrases))

        if not phrases:
            log.info("    no phrases; skipping arxiv query")
            results = []
        else:
            try:
                results = search_arxiv(query, max_results=top_n)
            except Exception as e:
                log.error("    search failed: %s", e)
                results = []

        fresh = _filter_already_ingested(results, seen)
        log.info("    %d hits → %d new", len(results), len(fresh))

        n_auto = 0
        for r in fresh:
            r["slug"] = _slug_from_metadata(
                title=r["title"], year=r.get("year", ""), authors=r.get("authors", "")
            )
            r["approved"] = None
            r["relevance"] = round(_relevance_score(candidate=r, phrases=phrases), 4)
            if auto_approve_threshold is not None and r["relevance"] >= auto_approve_threshold:
                r["approved"] = True
                r["auto_approved"] = True
                n_auto += 1
        if auto_approve_threshold is not None and n_auto:
            log.info("    auto-approved %d/%d", n_auto, len(fresh))

        # Track every fresh URL so the next problem's results don't double-up
        for r in fresh:
            seen.add(r["abs_url"])
            seen.add(_arxiv_id_stem(r["abs_url"]))

        blocks.append({
            "kind": "problem-sweep",
            "problem_id": rec["problem_id"],
            "problem_slug": rec["slug"],
            "query": query,
            "candidates": fresh,
        })

        if i + 1 < len(records) and rate_limit_seconds > 0:
            time.sleep(rate_limit_seconds)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps({
        "generated_at": dt.date.today().isoformat(),
        "concepts": blocks,
    }, indent=2) + "\n")
    total = sum(len(b["candidates"]) for b in blocks)
    log.info("problem-sweep complete: %d fresh candidates across %d problems → %s",
             total, len(blocks), out_path)


# ---------------- category-sweep (8.4) ----------------


def _build_category_query(min_year: int) -> str:
    """Build an arxiv query: math.* categories AND submittedDate ≥ min_year.

    arxiv submittedDate format: YYYYMMDDHHMM. Open-ended end via 999912312359.
    """
    cat_clause = " OR ".join(f"cat:{c}" for c in MATH_CATEGORIES)
    date_clause = f"submittedDate:[{min_year}01010000 TO 999912312359]"
    return f"({cat_clause}) AND {date_clause}"


def _search_arxiv_paged(*, query: str, start: int, max_results: int) -> list[dict]:
    """Hit arxiv with explicit `start` parameter for pagination.

    Separate from gap_search.search_arxiv (which hardcodes start=0) so we can
    page across thousands of math.* submissions without changing gap_search's
    public API. Format-compatible with search_arxiv: returns list of dicts
    with {title, authors, year, abs_url, summary}.
    """
    import urllib.parse  # local; gap_search has its own import

    params = urllib.parse.urlencode({
        "search_query": query,
        "start": str(start),
        "max_results": str(max_results),
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    })
    url = f"http://export.arxiv.org/api/query?{params}"
    req = urllib.request.Request(url, headers={"User-Agent": "einstein-seed-ingest/1"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        body = resp.read().decode("utf-8", errors="replace")

    # Minimal feedparser-free Atom parse — gap_search uses feedparser but
    # we want this module self-contained for paginated bulk pulls.
    import re as _re
    entries = _re.findall(r"<entry>(.*?)</entry>", body, _re.DOTALL)
    out: list[dict] = []
    for entry in entries:
        title_m = _re.search(r"<title>(.*?)</title>", entry, _re.DOTALL)
        sum_m = _re.search(r"<summary>(.*?)</summary>", entry, _re.DOTALL)
        id_m = _re.search(r"<id>(.*?)</id>", entry, _re.DOTALL)
        pub_m = _re.search(r"<published>(\d{4})", entry)
        authors = _re.findall(r"<name>(.*?)</name>", entry)
        if not (title_m and id_m):
            continue
        out.append({
            "title": _re.sub(r"\s+", " ", title_m.group(1)).strip(),
            "summary": _re.sub(r"\s+", " ", sum_m.group(1)).strip() if sum_m else "",
            "abs_url": id_m.group(1).strip(),
            "year": pub_m.group(1) if pub_m else "",
            "authors": ", ".join(authors),
        })
    return out


def category_sweep(
    *,
    out_path: Path,
    vocab_path: Path | None = None,
    source_dir: Path | None = None,
    min_year: int = 2022,
    min_relevance: float = 0.20,
    max_pages: int = 5,
    page_size: int = 100,
    auto_approve_threshold: float | None = None,
    rate_limit_seconds: float = ARXIV_RATE_LIMIT_SECONDS,
) -> None:
    """Bulk math.* category sweep: paginate arxiv, score against the full
    concept vocabulary, keep candidates with relevance ≥ min_relevance.

    Dedups against existing source/. Writes apply()-compatible JSON with a
    single block kind=category-sweep.
    """
    vocab_p = vocab_path if vocab_path is not None else DEFAULT_VOCAB_PATH
    vocab = _load_vocab(vocab_p)
    # Flat phrase list across all concepts — broad relevance signal.
    all_phrases: list[str] = []
    seen_phrase: set[str] = set()
    for phrases in vocab.values():
        for p in phrases:
            if p and p not in seen_phrase:
                seen_phrase.add(p)
                all_phrases.append(p)
    if not all_phrases:
        log.warning("category-sweep: empty vocab (%s); cannot score relevance", vocab_p)

    src_dir = source_dir if source_dir is not None else (_REPO / "knowledge" / "source")
    seen = _existing_source_urls(src_dir)
    log.info("category-sweep: %d known source URLs to dedup against", len(seen))

    query = _build_category_query(min_year=min_year)
    log.info("category-sweep: query=%s", query[:120] + ("…" if len(query) > 120 else ""))

    raw_hits: list[dict] = []
    for page in range(max_pages):
        start = page * page_size
        log.info("[%d/%d] page start=%d", page + 1, max_pages, start)
        try:
            results = _search_arxiv_paged(query=query, start=start, max_results=page_size)
        except Exception as e:
            log.error("    page failed: %s", e)
            break
        log.info("    %d entries", len(results))
        if not results:
            break
        raw_hits.extend(results)
        if page + 1 < max_pages and rate_limit_seconds > 0:
            time.sleep(rate_limit_seconds)

    # Dedup against existing source/ first (cheap, before scoring)
    fresh = _filter_already_ingested(raw_hits, seen)
    log.info("category-sweep: %d raw hits → %d after dedup", len(raw_hits), len(fresh))

    kept: list[dict] = []
    n_auto = 0
    for r in fresh:
        r["slug"] = _slug_from_metadata(
            title=r["title"], year=r.get("year", ""), authors=r.get("authors", "")
        )
        r["approved"] = None
        r["relevance"] = round(_relevance_score(candidate=r, phrases=all_phrases), 4)
        if r["relevance"] < min_relevance:
            continue
        if auto_approve_threshold is not None and r["relevance"] >= auto_approve_threshold:
            r["approved"] = True
            r["auto_approved"] = True
            n_auto += 1
        kept.append(r)

    if auto_approve_threshold is not None and n_auto:
        log.info("    auto-approved %d/%d", n_auto, len(kept))
    log.info("category-sweep: %d kept at relevance ≥ %.2f", len(kept), min_relevance)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps({
        "generated_at": dt.date.today().isoformat(),
        "concepts": [{
            "kind": "category-sweep",
            "min_year": min_year,
            "min_relevance": min_relevance,
            "query": query,
            "candidates": kept,
        }],
    }, indent=2) + "\n")
    log.info("category-sweep complete: → %s", out_path)


# ---------------- network I/O (mockable seams) ----------------


def _download_pdf(url: str, dst: Path) -> None:
    """Fetch URL to dst. Separate function so tests can patch it."""
    log.info("downloading %s → %s", url, dst.name)
    req = urllib.request.Request(url, headers={"User-Agent": "einstein-seed-ingest/1"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        dst.write_bytes(resp.read())


def _download_with_retry(url: str, dst: Path, *,
                         max_retries: int = 3,
                         base_delay: float = 1.0) -> None:
    """Wrap `_download_pdf` with exponential backoff on transient errors.

    Retries on URLError/HTTPError. HTTP 429 uses a longer base delay
    (caller-tunable via base_delay arg). Raises the last exception if
    all attempts fail. `max_retries` is the number of retries AFTER the
    first attempt — so max_retries=3 makes up to 4 total attempts.
    """
    last_exc: Exception | None = None
    for attempt in range(max_retries + 1):
        try:
            _download_pdf(url, dst)
            return
        except HTTPError as e:
            last_exc = e
            # 429 → wait longer; 4xx other than 429 → don't retry
            if e.code == 429:
                wait = base_delay * (2 ** attempt) * 4  # 4x multiplier for rate-limit
                log.warning("HTTP 429 for %s — sleep %.1fs (attempt %d/%d)",
                            url, wait, attempt + 1, max_retries + 1)
                time.sleep(wait)
                continue
            if 400 <= e.code < 500:
                raise   # not transient
            wait = base_delay * (2 ** attempt)
            log.warning("HTTP %d for %s — sleep %.1fs (attempt %d/%d)",
                        e.code, url, wait, attempt + 1, max_retries + 1)
            time.sleep(wait)
        except (URLError, TimeoutError, ConnectionError) as e:
            last_exc = e
            wait = base_delay * (2 ** attempt)
            log.warning("network error for %s: %s — sleep %.1fs (attempt %d/%d)",
                        url, e, wait, attempt + 1, max_retries + 1)
            time.sleep(wait)
    assert last_exc is not None
    raise last_exc


def _parallel_download(
    items: list[tuple[str, Path]],
    *,
    max_workers: int = 10,
    max_retries: int = 3,
    base_delay: float = 1.0,
) -> list[tuple[bool, Path, str | None]]:
    """Download many (url, dst) pairs concurrently.

    Returns a list of (success, dst, error_message) tuples in the same
    order as `items`. Failures are isolated — one bad URL does not
    affect the others.
    """
    results: list[tuple[bool, Path, str | None] | None] = [None] * len(items)

    def _one(idx: int, url: str, dst: Path) -> tuple[int, bool, Path, str | None]:
        try:
            _download_with_retry(url, dst, max_retries=max_retries, base_delay=base_delay)
            return (idx, True, dst, None)
        except Exception as e:
            return (idx, False, dst, f"{type(e).__name__}: {e}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as ex:
        futures = [ex.submit(_one, i, url, dst) for i, (url, dst) in enumerate(items)]
        for fut in concurrent.futures.as_completed(futures):
            idx, ok, path, err = fut.result()
            results[idx] = (ok, path, err)

    # No item should be None by here
    return [r for r in results if r is not None]


def _run_pdf_to_md(pdf: Path, out_md: Path) -> None:
    """Run pdf_to_md.convert_pdf. Separate function so tests can patch it.

    Uses deterministic mode (hybrid=None) — `docling-fast` requires a separate
    server at localhost:5002 that isn't part of the basic install. Trade-off:
    LaTeX formulas may not extract perfectly, but no extra infra needed.
    """
    pdf_to_md.convert_pdf(pdf, out_md, hybrid=None, overwrite=False)


# ---------------- propose step ----------------


def _load_existing_candidates(path: Path) -> dict[str, dict]:
    """Return {concept_name: existing_entry} from a prior candidates.json (if any).

    Used to preserve human-set approval flags across re-runs of `propose`.
    """
    if not path.is_file():
        return {}
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError:
        return {}
    return {c["concept"]: c for c in data.get("concepts", [])}


def _merge_preserve_approvals(existing: dict, fresh_candidates: list[dict]) -> list[dict]:
    """For each fresh candidate, copy `approved` flag from a matching prior entry (by abs_url)."""
    if not existing:
        return fresh_candidates
    prior_by_url = {c["abs_url"]: c for c in existing.get("candidates", [])}
    merged = []
    for fc in fresh_candidates:
        prior = prior_by_url.get(fc["abs_url"])
        if prior is not None and prior.get("approved") is not None:
            fc = {**fc, "approved": prior["approved"]}
        merged.append(fc)
    return merged


def propose(*, coverage_json: Path, out_path: Path, top_n: int = 5,
            rate_limit_seconds: float = ARXIV_RATE_LIMIT_SECONDS,
            vocab_path: Path | None = None,
            auto_approve_threshold: float | None = None) -> None:
    """Step 1: search arxiv for each actionable coverage row; write candidates JSON.

    If `vocab_path` is provided (or `concept-search-terms.yaml` sits next to this
    file), use the YAML's slug → phrase mapping to construct queries that use
    literature vocabulary instead of the project's internal slug. Slugs mapped
    to an empty list are marked `vocab_status: intentionally-unmapped` and not
    queried. Unmapped slugs fall back to the slug-as-phrase fallback.
    """
    coverage = json.loads(coverage_json.read_text())
    existing = _load_existing_candidates(out_path)
    vocab = _load_vocab(vocab_path if vocab_path is not None else DEFAULT_VOCAB_PATH)

    concepts_out: list[dict] = []
    actionable = [r for r in coverage["rows"] if r["classification"] in ACTIONABLE_CLASSIFICATIONS]
    log.info("propose: %d actionable rows (%d vocab entries loaded)",
             len(actionable), len(vocab))

    n_searched = 0
    for i, row in enumerate(actionable):
        name = row["name"]
        refs = row["refs"]
        block: dict = {"concept": name, "kind": row["kind"], "refs": refs}

        if name in vocab:
            phrases = vocab[name]
            if not phrases:
                # Intentionally unmapped — record but skip the network call
                log.info("[%d/%d] %s — unmapped (skipped)", i + 1, len(actionable), name)
                block.update({
                    "query": "",
                    "vocab_status": "intentionally-unmapped",
                    "candidates": [],
                })
                concepts_out.append(block)
                continue
            query = _build_vocab_query(phrases)
            block["vocab_status"] = "mapped"
        else:
            # Fallback: slug-as-phrase. Documented in
            # findings/dead-end-slug-as-arxiv-phrase-query.md — usually 0 hits.
            query = build_query(title="", concepts=[name], related_problems=[])
            block["vocab_status"] = "fallback-slug-as-phrase"

        log.info("[%d/%d] %s — %s", i + 1, len(actionable), name, query)
        results = search_arxiv(query, max_results=top_n)
        n_searched += 1
        log.info("    %d hits", len(results))

        phrases = vocab.get(name) or [name.removesuffix(".md").replace("-", " ")]
        n_auto = 0
        for r in results:
            r["slug"] = _slug_from_metadata(
                title=r["title"], year=r.get("year", ""), authors=r.get("authors", "")
            )
            r["approved"] = None
            r["relevance"] = round(_relevance_score(candidate=r, phrases=phrases), 4)
            if auto_approve_threshold is not None and r["relevance"] >= auto_approve_threshold:
                r["approved"] = True
                r["auto_approved"] = True
                n_auto += 1
        if auto_approve_threshold is not None and n_auto:
            log.info("    auto-approved %d/%d (relevance ≥ %.2f)",
                     n_auto, len(results), auto_approve_threshold)

        merged = _merge_preserve_approvals(existing.get(name, {}), results)
        block.update({"query": query, "candidates": merged})
        concepts_out.append(block)

        # Rate-limit: arxiv API policy is ≥3 s between hits. Skip wait for
        # the last iteration and for unmapped-skip rows (no network call).
        if i + 1 < len(actionable) and rate_limit_seconds > 0:
            time.sleep(rate_limit_seconds)

    out = {
        "generated_at": dt.date.today().isoformat(),
        "concepts": concepts_out,
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2) + "\n")
    log.info("wrote %d concept blocks to %s",
             len(concepts_out), out_path.relative_to(_REPO) if _REPO in out_path.parents else out_path)


# ---------------- apply step ----------------


def apply(*, candidates_json: Path, docs_root: Path | None = None,
          dry_run: bool = False,
          download_workers: int = 10,
          download_retries: int = 3,
          llm_distill_enabled: bool = True,
          llm_model: str = "claude-opus-4-7[1m]",
          llm_workers: int = 4,
          llm_delay_seconds: float = 0) -> list[Path]:
    """Step 2: download approved candidates + write source/ entries.

    Refactored from one-PDF-at-a-time to:
      1. Collect all approved + not-already-in-source candidates
      2. Download all PDFs in parallel (ThreadPoolExecutor) with retry
      3. One pdf_to_md.convert_batch call across all downloads
         (single JVM, amortized startup) — only if backend supports batch
      4. Compose source/ frontmatter + body, write each entry

    Returns the list of source/ paths that were (or would be, dry-run) created.
    """
    docs = (docs_root or (_REPO / "docs")).resolve()
    source_dir = docs / "source"
    raw_dir = docs / "raw"  # FLAT per knowledge/wiki/CLAUDE.md contract
    raw_dir.mkdir(parents=True, exist_ok=True)
    source_dir.mkdir(parents=True, exist_ok=True)

    data = json.loads(candidates_json.read_text())

    # Phase 1: collect work items
    work: list[dict] = []
    seen_slugs: set[str] = set()
    for block in data["concepts"]:
        concept = block.get("concept")
        refs = block.get("refs", [])
        topic = block.get("topic")
        kind = block.get("kind", "")
        is_general = kind in ("general-knowledge", "author-sweep") or not concept

        for cand in block["candidates"]:
            if not cand.get("approved"):
                continue
            slug = cand["slug"]
            if slug in seen_slugs:
                log.info("skip duplicate candidate slug — %s", slug)
                continue
            seen_slugs.add(slug)
            source_path = source_dir / f"{slug}.md"
            if source_path.exists():
                log.info("skip %s — %s exists", concept or topic or "author-sweep", source_path.name)
                continue
            pdf_path = raw_dir / f"{slug}.pdf"
            work.append({
                "cand": cand, "block": block, "slug": slug,
                "source_path": source_path, "pdf_path": pdf_path,
                "concept": concept, "refs": refs, "topic": topic,
                "is_general": is_general, "kind": kind,
            })

    if not work:
        log.info("nothing to apply (all approved candidates already in source/ or no approvals)")
        return []

    if dry_run:
        for w in work:
            log.info("[dry-run] would ingest %s → %s",
                     w["cand"]["abs_url"], w["source_path"].name)
        return [w["source_path"] for w in work]

    # Phase 2: parallel download
    download_items = [
        (w["cand"].get("pdf_url") or _abs_to_pdf_url(w["cand"]["abs_url"]), w["pdf_path"])
        for w in work
    ]
    log.info("phase 2: parallel download of %d PDFs (%d workers, %d retries)",
             len(download_items), download_workers, download_retries)
    results = _parallel_download(download_items, max_workers=download_workers,
                                 max_retries=download_retries)

    # Mark download outcomes back onto the work items
    successful: list[dict] = []
    for w, (ok, _path, err) in zip(work, results):
        if ok:
            w["download_ok"] = True
            successful.append(w)
        else:
            w["download_ok"] = False
            w["download_error"] = err
            log.error("download failed for %s: %s", w["cand"]["abs_url"], err)
    log.info("phase 2: %d/%d downloads succeeded", len(successful), len(work))

    if not successful:
        return []

    # Phase 3: batch PDF→md (one JVM startup amortized over all PDFs)
    log.info("phase 3: pdf_to_md.convert_batch — %d PDFs through one JVM", len(successful))
    body_temp = source_dir / "_pdf_to_md_tmp"
    body_temp.mkdir(exist_ok=True)
    try:
        pdf_to_md.convert_batch(
            [w["pdf_path"] for w in successful],
            body_temp,
            hybrid=None,        # deterministic mode — no docling server needed
            overwrite=True,
        )
    except pdf_to_md.BackendMissing as e:
        log.error("pdf_to_md backend missing — aborting: %s", e)
        raise
    except Exception as e:
        log.error("pdf_to_md.convert_batch failed: %s — falling back to per-PDF", e)
        # Fall back: per-PDF conversion so a single bad PDF doesn't sink the batch
        for w in successful:
            body_md = body_temp / f"{w['slug']}.md"
            try:
                _run_pdf_to_md(w["pdf_path"], body_md)
            except Exception as e2:
                log.error("pdf_to_md failed for %s: %s", w["pdf_path"], e2)
                w["pdf_to_md_ok"] = False

    # Phase 3.5: LLM-distill the extracted markdowns (Karpathy llm-wiki style)
    # via Claude Code's headless `claude -p` — runs under the user's Claude Code
    # subscription, no API key needed. One-shot, parallelized via ThreadPool.
    distilled: dict[str, str] = {}     # slug → distilled summary text
    if llm_distill_enabled and llm_distill is not None:
        distill_items: list[dict] = []
        for w in successful:
            body_md_path = body_temp / f"{w['slug']}.md"
            if not body_md_path.is_file():
                continue
            cand = w["cand"]
            distill_items.append({
                "slug": w["slug"],
                "extracted_md": body_md_path.read_text(),
                "metadata": {
                    "title": cand.get("title", ""),
                    "authors": cand.get("authors", ""),
                    "year": cand.get("year", ""),
                    "source_url": cand["abs_url"],
                },
            })

        if distill_items:
            log.info("phase 3.5: LLM-distill %d papers via claude -p (model %s, "
                     "%d workers, %.1fs delay between calls)",
                     len(distill_items), llm_model, llm_workers, llm_delay_seconds)
            distill_results = llm_distill.distill_batch(
                distill_items, model=llm_model, max_workers=llm_workers,
                delay_seconds=llm_delay_seconds,
            )
            for r in distill_results:
                if r["ok"]:
                    distilled[r["slug"]] = r["summary"]
                else:
                    log.error("llm-distill failed for %s: %s", r["slug"], r["error"])
            fatal_errors = [
                r for r in distill_results
                if not r["ok"] and "Claude Code unavailable" in r.get("error", "")
            ]
            if fatal_errors:
                raise RuntimeError(
                    "LLM distillation unavailable; aborting apply before writing "
                    "raw fallbacks. Resume after Claude Code quota/auth recovers."
                )

    # Phase 4: write source/ entries (frontmatter + body — distilled if available,
    # else falling back to raw extraction so we never lose the paper outright)
    written: list[Path] = []
    for w in successful:
        if w.get("pdf_to_md_ok") is False:
            continue
        body_md = body_temp / f"{w['slug']}.md"
        if not body_md.is_file():
            log.warning("body markdown missing for %s — skipping", w["slug"])
            continue

        body = distilled.get(w["slug"])
        if not body:
            # No distillation (either disabled or failed) — keep raw extraction
            # as fallback. Better to have an oversized entry than no entry.
            body = body_md.read_text()
            log.warning("no LLM distillation for %s — using raw extraction", w["slug"])
        body_md.unlink()

        cand = w["cand"]
        if w["is_general"]:
            topic = w["topic"] or (w["kind"] if w["kind"] in ("author-sweep",) else "general-knowledge")
            fm = _build_source_frontmatter(
                candidate=cand, topic=topic,
                source_type=cand.get("source_type", "arxiv"),
            )
        else:
            fm = _build_source_frontmatter(
                candidate=cand, concept=w["concept"], problem_refs=w["refs"],
            )
        w["source_path"].write_text(_frontmatter_to_yaml(fm) + "\n" + body)
        log.info("wrote %s", w["source_path"].relative_to(_REPO)
                 if _REPO in w["source_path"].parents else w["source_path"])
        written.append(w["source_path"])

    # Clean up the temp body dir. We hard-remove it (including any
    # leftover files from interrupted runs) so knowledge/source/_pdf_to_md_tmp
    # never accumulates as a stale subdirectory.
    if body_temp.is_dir():
        for stray in body_temp.glob("*"):
            try:
                stray.unlink()
            except OSError:
                pass
        try:
            body_temp.rmdir()
        except OSError:
            pass

    return written


# ---------------- CLI ----------------


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_propose = sub.add_parser("propose", help="Search arxiv for actionable concepts; write candidates JSON.")
    p_propose.add_argument("--coverage", type=Path, required=True)
    p_propose.add_argument("--out", type=Path, required=True)
    p_propose.add_argument("--top-n", type=int, default=5)
    p_propose.add_argument("--vocab", type=Path, default=None,
                           help=f"Slug → search-phrase YAML (default: {DEFAULT_VOCAB_PATH.name}).")
    p_propose.add_argument("--auto-approve-above", type=float, default=None,
                           metavar="THRESHOLD",
                           help="Auto-flag candidates with relevance ≥ THRESHOLD "
                                "as approved (skip human gate for high-confidence "
                                "matches). Typical: 0.5.")

    p_author = sub.add_parser("author-sweep",
                              help="Search arxiv per author (seed-authors.yaml); "
                                   "dedup against existing source/; write candidates.")
    p_author.add_argument("--authors", type=Path, default=DEFAULT_AUTHORS_PATH)
    p_author.add_argument("--out", type=Path, required=True)
    p_author.add_argument("--top-n", type=int, default=5)
    p_author.add_argument("--source-dir", type=Path, default=None)
    p_author.add_argument("--auto-approve-above", type=float, default=None,
                          metavar="THRESHOLD")

    p_citation = sub.add_parser("citation-crawl",
                                help="For each arxiv id in source/, fetch semanticscholar "
                                     "references and emit fresh candidates JSON.")
    p_citation.add_argument("--out", type=Path, required=True)
    p_citation.add_argument("--source-dir", type=Path, default=None)
    p_citation.add_argument("--rate-limit", type=float, default=1.0)
    p_citation.add_argument("--max-refs-per-paper", type=int, default=200)
    p_citation.add_argument("--auto-approve-above", type=float, default=None,
                            metavar="THRESHOLD")
    p_citation.add_argument("--arxiv-ids", type=str, default=None,
                            metavar="ID1,ID2,...",
                            help="Comma-separated arxiv IDs to crawl instead of "
                                 "scanning all of source/. Useful for survey-paper "
                                 "bibliography expansion (8.3).")

    p_problem = sub.add_parser("problem-sweep",
                               help="Per-problem arxiv sweep: walks knowledge/wiki/problems/ "
                                    "frontmatter and queries arxiv per active problem.")
    p_problem.add_argument("--problems-dir", type=Path,
                           default=_REPO / "knowledge" / "wiki" / "problems")
    p_problem.add_argument("--out", type=Path, required=True)
    p_problem.add_argument("--top-n", type=int, default=10)
    p_problem.add_argument("--vocab", type=Path, default=None,
                           help=f"Slug → search-phrase YAML (default: {DEFAULT_VOCAB_PATH.name}).")
    p_problem.add_argument("--source-dir", type=Path, default=None)
    p_problem.add_argument("--exclude", type=str, default=None,
                           metavar="P6,P22",
                           help="Comma-separated problem IDs to skip (e.g. 'P6' or '6').")
    p_problem.add_argument("--auto-approve-above", type=float, default=None,
                           metavar="THRESHOLD")

    p_category = sub.add_parser("category-sweep",
                                help="Bulk math.* category sweep with date + relevance filter.")
    p_category.add_argument("--out", type=Path, required=True)
    p_category.add_argument("--vocab", type=Path, default=None,
                            help=f"Phrase YAML for relevance scoring (default: {DEFAULT_VOCAB_PATH.name}).")
    p_category.add_argument("--source-dir", type=Path, default=None)
    p_category.add_argument("--min-year", type=int, default=2022)
    p_category.add_argument("--min-relevance", type=float, default=0.20)
    p_category.add_argument("--max-pages", type=int, default=5)
    p_category.add_argument("--page-size", type=int, default=100)
    p_category.add_argument("--auto-approve-above", type=float, default=None,
                            metavar="THRESHOLD")

    p_apply = sub.add_parser("apply", help="Download approved candidates + write source/ entries.")
    p_apply.add_argument("--candidates", type=Path, required=True)
    p_apply.add_argument("--docs-root", type=Path, default=None)
    p_apply.add_argument("--dry-run", action="store_true")
    p_apply.add_argument("--no-llm", action="store_true",
                         help="Skip LLM distillation (raw extraction goes to source/). "
                              "Default: LLM-distill via claude -p.")
    p_apply.add_argument("--llm-model", default="claude-opus-4-7[1m]",
                         help="Model alias for claude -p distillation.")
    p_apply.add_argument("--llm-workers", type=int, default=4,
                         help="Parallel claude -p invocations during distillation.")
    p_apply.add_argument("--llm-delay-seconds", type=float, default=0,
                         help="Sleep N seconds between successive claude -p submissions. "
                              "Use to throttle Claude Code session-quota burn. "
                              "Typical: --llm-workers 1 --llm-delay-seconds 240 (one paper "
                              "every 4 min, safe over a multi-hour session).")

    args = parser.parse_args(argv)

    if args.cmd == "propose":
        propose(coverage_json=args.coverage, out_path=args.out, top_n=args.top_n,
                vocab_path=args.vocab,
                auto_approve_threshold=args.auto_approve_above)
    elif args.cmd == "author-sweep":
        author_sweep(
            authors_yaml=args.authors, out_path=args.out, top_n=args.top_n,
            source_dir=args.source_dir,
            auto_approve_threshold=args.auto_approve_above,
        )
    elif args.cmd == "citation-crawl":
        src = args.source_dir if args.source_dir is not None else (_REPO / "knowledge" / "source")
        if args.arxiv_ids:
            arxiv_ids = [s.strip() for s in args.arxiv_ids.split(",") if s.strip()]
            log.info("citation-crawl: %d arxiv ids from --arxiv-ids", len(arxiv_ids))
        else:
            arxiv_ids = _collect_arxiv_ids(src)
            log.info("citation-crawl: %d arxiv ids found in source/", len(arxiv_ids))
        candidates = citation_crawl(
            arxiv_ids=arxiv_ids, source_dir=src,
            rate_limit_seconds=args.rate_limit,
            max_refs_per_paper=args.max_refs_per_paper,
        )
        threshold = args.auto_approve_above
        if threshold is not None:
            n_auto = 0
            for c in candidates:
                if c.get("relevance", 0) >= threshold:
                    c["approved"] = True
                    c["auto_approved"] = True
                    n_auto += 1
            log.info("auto-approved %d/%d (relevance ≥ %.2f)",
                     n_auto, len(candidates), threshold)
        out = {
            "generated_at": dt.date.today().isoformat(),
            "concepts": [{
                "kind": "citation-crawl",
                "candidates": candidates,
            }],
        }
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(out, indent=2) + "\n")
        log.info("wrote %d candidates → %s", len(candidates), args.out)
    elif args.cmd == "problem-sweep":
        exclude_ids: list[int] = []
        if args.exclude:
            for tok in args.exclude.split(","):
                tok = tok.strip().lstrip("Pp")
                if tok.isdigit():
                    exclude_ids.append(int(tok))
        problem_sweep(
            problems_dir=args.problems_dir, out_path=args.out, top_n=args.top_n,
            vocab_path=args.vocab, source_dir=args.source_dir,
            exclude=exclude_ids if exclude_ids else None,
            auto_approve_threshold=args.auto_approve_above,
        )
    elif args.cmd == "category-sweep":
        category_sweep(
            out_path=args.out, vocab_path=args.vocab, source_dir=args.source_dir,
            min_year=args.min_year, min_relevance=args.min_relevance,
            max_pages=args.max_pages, page_size=args.page_size,
            auto_approve_threshold=args.auto_approve_above,
        )
    elif args.cmd == "apply":
        results = apply(
            candidates_json=args.candidates,
            docs_root=args.docs_root, dry_run=args.dry_run,
            llm_distill_enabled=not args.no_llm,
            llm_model=args.llm_model,
            llm_workers=args.llm_workers,
            llm_delay_seconds=args.llm_delay_seconds,
        )
        log.info("%s %d source/ entries",
                 "would write" if args.dry_run else "wrote", len(results))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
