#!/usr/bin/env python3
"""seed_ingest.py — bulk-ingest arxiv papers to fill wiki coverage gaps.

Two-step pipeline (human-gated between):

    1. propose:  concept-coverage.json  →  seed-candidates.json
       Walks `under-sourced` + `missing-page` rows; for each, runs
       gap_search.search_arxiv and writes the top-N hits with
       `approved: null` flags.

    2. apply:    seed-candidates.json   →  docs/source/<slug>.md
       For each candidate with `approved: true`, downloads the PDF
       to docs/raw/papers/<slug>.pdf, runs pdf_to_md to extract
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
import datetime as dt
import json
import logging
import re
import sys
import time
import urllib.request
from pathlib import Path

# Local imports — sibling tools
_TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(_TOOLS))

from gap_search import MATH_CATEGORIES, build_query, search_arxiv  # type: ignore[import-not-found]
import pdf_to_md  # type: ignore[import-not-found]

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
    """Construct the YAML frontmatter dict for a docs/source/ entry.

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

    Matches existing docs/source/ style: URLs + DOI strings stay unquoted
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


# ---------------- network I/O (mockable seams) ----------------


def _download_pdf(url: str, dst: Path) -> None:
    """Fetch URL to dst. Separate function so tests can patch it."""
    log.info("downloading %s → %s", url, dst.name)
    req = urllib.request.Request(url, headers={"User-Agent": "einstein-seed-ingest/1"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        dst.write_bytes(resp.read())


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
            vocab_path: Path | None = None) -> None:
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

        for r in results:
            r["slug"] = _slug_from_metadata(
                title=r["title"], year=r.get("year", ""), authors=r.get("authors", "")
            )
            r["approved"] = None

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
          dry_run: bool = False) -> list[Path]:
    """Step 2: download approved candidates + write source/ entries.

    Returns the list of source/ paths that were (or would be, if dry-run) created.
    """
    docs = (docs_root or (_REPO / "docs")).resolve()
    source_dir = docs / "source"
    raw_dir = docs / "raw"  # FLAT per docs/wiki/CLAUDE.md contract
    raw_dir.mkdir(parents=True, exist_ok=True)
    source_dir.mkdir(parents=True, exist_ok=True)

    data = json.loads(candidates_json.read_text())
    written: list[Path] = []

    # Blocks live under "concepts" key for both concept-bound and
    # general-knowledge entries. A block without a "concept" field (or with
    # `kind: general-knowledge`) is treated as topic-tagged.
    for block in data["concepts"]:
        concept = block.get("concept")
        refs = block.get("refs", [])
        topic = block.get("topic")  # for general-knowledge
        kind = block.get("kind", "")
        is_general = kind == "general-knowledge" or not concept

        for cand in block["candidates"]:
            if not cand.get("approved"):
                continue
            slug = cand["slug"]
            source_path = source_dir / f"{slug}.md"
            if source_path.exists():
                log.info("skip %s — %s exists", concept or topic, source_path.name)
                continue

            pdf_path = raw_dir / f"{slug}.pdf"
            written.append(source_path)

            if dry_run:
                log.info("[dry-run] would ingest %s → %s", cand["abs_url"], source_path.name)
                continue

            try:
                # General-knowledge candidates may carry a direct PDF URL
                # (e.g. cdn.openai.com); arxiv abs URLs get rewritten to pdf URL.
                download_url = cand.get("pdf_url") or _abs_to_pdf_url(cand["abs_url"])
                _download_pdf(download_url, pdf_path)
            except Exception as e:
                log.error("download failed for %s: %s", cand["abs_url"], e)
                written.pop()
                continue

            # Convert PDF to markdown body
            body_md = source_dir / f"{slug}.body.md"
            try:
                _run_pdf_to_md(pdf_path, body_md)
            except pdf_to_md.BackendMissing as e:
                log.error("pdf_to_md backend missing — aborting: %s", e)
                written.pop()
                raise
            except Exception as e:
                log.error("pdf_to_md failed for %s: %s", pdf_path, e)
                written.pop()
                continue

            body = body_md.read_text() if body_md.exists() else ""
            if body_md.exists():
                body_md.unlink()

            if is_general:
                fm = _build_source_frontmatter(
                    candidate=cand, topic=topic or "general-knowledge",
                    source_type=cand.get("source_type", "arxiv"),
                )
            else:
                fm = _build_source_frontmatter(
                    candidate=cand, concept=concept, problem_refs=refs,
                )
            source_path.write_text(_frontmatter_to_yaml(fm) + "\n" + body)
            log.info("wrote %s", source_path.relative_to(_REPO) if _REPO in source_path.parents else source_path)

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

    p_apply = sub.add_parser("apply", help="Download approved candidates + write source/ entries.")
    p_apply.add_argument("--candidates", type=Path, required=True)
    p_apply.add_argument("--docs-root", type=Path, default=None)
    p_apply.add_argument("--dry-run", action="store_true")

    args = parser.parse_args(argv)

    if args.cmd == "propose":
        propose(coverage_json=args.coverage, out_path=args.out, top_n=args.top_n,
                vocab_path=args.vocab)
    elif args.cmd == "apply":
        results = apply(candidates_json=args.candidates,
                        docs_root=args.docs_root, dry_run=args.dry_run)
        log.info("%s %d source/ entries",
                 "would write" if args.dry_run else "wrote", len(results))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
