#!/usr/bin/env python3
"""distill_paper.py — structural distillation of opendataloader-pdf output.

The wiki contract says `docs/source/*.md` should hold "1:1 LLM-distilled"
summaries, not raw extractions. opendataloader-pdf gives us the full text
of a paper (often 500–3000 lines); this module extracts a focused
**curated summary** suitable for qmd vector search: title, authors,
year, arxiv URL, abstract, optional conclusion, and an introduction
snippet.

The structure mirrors what an interactive `/wiki-ingest` skill run
would produce, but at zero LLM cost — opendataloader-pdf already
preserves section headers (`### Abstract`, `### Conclusion`), so we
can find them structurally.

Used by `seed_ingest.apply()` to compose the body of each source/
entry before writing. Also exposed as a standalone CLI that can
retroactively shrink already-ingested oversized source/ entries.

Usage:
    uv run python docs/tools/distill_paper.py --shrink docs/source/2007-foo.md
    uv run python docs/tools/distill_paper.py --shrink-all docs/source/
"""
from __future__ import annotations

import argparse
import logging
import re
from pathlib import Path

log = logging.getLogger("distill_paper")


# ---------------- section extraction ----------------

# Match section headers like:
#   ### Abstract
#   ## Abstract
#   ### 1. Conclusion
#   ### 5 Conclusion
_HEADER_RE = re.compile(r"^(#{2,6})\s+(?:\d+\.?\s+)?(.+?)\s*$", re.MULTILINE)


def _normalize(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", name.lower()).strip()


def _section_aliases(target: str) -> set[str]:
    """Common headers a paper uses for a target section name."""
    aliases = {
        "abstract": {"abstract"},
        "introduction": {"introduction", "intro"},
        "conclusion": {"conclusion", "conclusions", "concluding remarks",
                       "summary", "discussion", "discussion and conclusion"},
        "references": {"references", "bibliography", "works cited"},
        "method": {"method", "methods", "methodology", "our method", "approach"},
        "results": {"results", "experiments", "experimental results"},
    }
    return aliases.get(target, {target})


def _extract_section(md: str, section_name: str, *,
                     max_chars: int | None = None) -> str:
    """Return the body of `section_name` (between its header and the next header).

    Empty string if no matching header found. Trims to `max_chars` if given.
    """
    targets = {_normalize(a) for a in _section_aliases(section_name)}

    # Walk all headers
    headers = list(_HEADER_RE.finditer(md))
    for i, m in enumerate(headers):
        if _normalize(m.group(2)) in targets:
            start = m.end()
            end = headers[i + 1].start() if i + 1 < len(headers) else len(md)
            body = md[start:end].strip()
            if max_chars is not None and len(body) > max_chars:
                # Truncate at a word boundary
                trimmed = body[:max_chars]
                space = trimmed.rfind(" ")
                if space > max_chars * 0.7:
                    trimmed = trimmed[:space]
                body = trimmed.rstrip() + " …"
            return body
    return ""


# ---------------- distillation ----------------


def distill(extracted_md: str, metadata: dict, *,
            abstract_max_chars: int = 4000,
            intro_max_chars: int = 1500,
            conclusion_max_chars: int = 2500) -> str:
    """Produce a curated summary suitable for docs/source/<slug>.md body.

    Strategy:
      1. Header block from `metadata` (title / authors / year / arxiv URL).
      2. Abstract (full, truncated to abstract_max_chars).
      3. Introduction snippet (intro_max_chars) IF no abstract found.
      4. Conclusion / Summary section (truncated).
      5. Hard-discard References, Bibliography, raw body.

    Total output is typically 50–300 lines vs the 500–3000 of raw extraction.
    """
    title = metadata.get("title", "(no title)")
    authors = metadata.get("authors", "")
    year = metadata.get("year", "")
    source_url = metadata.get("source_url", "")

    parts: list[str] = [f"# {title}", ""]
    meta_lines: list[str] = []
    if authors:
        meta_lines.append(f"**Authors:** {authors}")
    if year:
        meta_lines.append(f"**Year:** {year}")
    if source_url:
        meta_lines.append(f"**Source:** {source_url}")
    if meta_lines:
        parts.append("\n".join(meta_lines))
        parts.append("")

    abstract = _extract_section(extracted_md, "abstract",
                                max_chars=abstract_max_chars)
    if abstract:
        parts.append("## Abstract")
        parts.append("")
        parts.append(abstract)
        parts.append("")
    else:
        # Fallback: snippet of intro or top-of-body
        intro = _extract_section(extracted_md, "introduction",
                                 max_chars=intro_max_chars)
        if intro:
            parts.append("## Introduction (excerpt — no abstract found)")
            parts.append("")
            parts.append(intro)
            parts.append("")
        else:
            # Last resort: first non-empty paragraph of body
            stripped = extracted_md.strip()
            if stripped:
                first_chunk = stripped[:intro_max_chars].rstrip()
                if len(stripped) > intro_max_chars:
                    first_chunk += " …"
                parts.append("## Excerpt (no Abstract / Introduction section found)")
                parts.append("")
                parts.append(first_chunk)
                parts.append("")

    conclusion = _extract_section(extracted_md, "conclusion",
                                  max_chars=conclusion_max_chars)
    if conclusion:
        parts.append("## Conclusion")
        parts.append("")
        parts.append(conclusion)
        parts.append("")

    return "\n".join(parts).rstrip() + "\n"


# ---------------- retroactive shrink ----------------


_FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def _parse_frontmatter(text: str) -> tuple[dict, str]:
    m = _FM_RE.match(text)
    if not m:
        return {}, text
    fm: dict = {}
    for line in m.group(1).splitlines():
        kv = re.match(r"^([a-zA-Z_]+):\s*(.*)$", line)
        if kv:
            fm[kv.group(1)] = kv.group(2).strip().strip("\"'")
    return fm, text[m.end():]


def shrink_source_entry(path: Path) -> bool:
    """Replace the body of `path` with a distilled summary.

    Returns True if shrunk (body was meaningfully larger than the
    distillation), False otherwise.
    """
    text = path.read_text()
    fm, body = _parse_frontmatter(text)
    if not fm:
        log.warning("no frontmatter — skipping %s", path.name)
        return False

    summary = distill(body, fm)
    # Recompose with the original frontmatter
    new_text = "---\n"
    for k, v in fm.items():
        new_text += f"{k}: {v}\n"
    new_text += "---\n\n" + summary

    if len(new_text) >= len(text) * 0.85:
        # Not a meaningful shrink — probably already small (≤ ~85% means
        # the body was mostly the header anyway)
        return False

    path.write_text(new_text)
    return True


# ---------------- CLI ----------------


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    p = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--shrink", type=Path,
                   help="Shrink one source/<slug>.md in place.")
    g.add_argument("--shrink-all", type=Path,
                   help="Shrink every *.md in the given directory.")
    args = p.parse_args(argv)

    if args.shrink:
        ok = shrink_source_entry(args.shrink)
        log.info("%s %s", "shrunk" if ok else "no-op", args.shrink)
        return 0

    targets = sorted(args.shrink_all.glob("*.md"))
    total_before = sum(t.stat().st_size for t in targets)
    n_shrunk = 0
    for t in targets:
        if t.name in ("INDEX.md", "README.md"):
            continue
        if shrink_source_entry(t):
            n_shrunk += 1
    total_after = sum(t.stat().st_size for t in targets)
    log.info("shrunk %d/%d entries; %d → %d KB (%.1f%% reduction)",
             n_shrunk, len(targets),
             total_before // 1024, total_after // 1024,
             100 * (1 - total_after / max(total_before, 1)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
