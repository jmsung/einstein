#!/usr/bin/env python3
"""wiki_lint.py — agent-native subset of the wiki-lint skill.

Runs the three structural checks from `harness/skills/wiki-lint/SKILL.md`
that don't need an LLM: orphans, broken cites, body link gaps. The
semantic checks (contradictions, stale claims) stay in the human-driven
`/wiki-lint` skill.

Designed to be called from `docs/tools/cycle_runner.sh` so every
autonomous-loop cycle ends with a structural wiki health check.
Default mode prints a report and returns 0 — strict mode returns
nonzero if any findings exist.

Usage:
    uv run python docs/tools/wiki_lint.py                       # report only
    uv run python docs/tools/wiki_lint.py --strict              # nonzero exit on findings
    uv run python docs/tools/wiki_lint.py --wiki docs/wiki/     # custom wiki dir
"""
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
DEFAULT_WIKI = _REPO / "docs" / "wiki"

# Pages that look like indices / housekeeping and should never count as orphans.
_HOUSEKEEPING_BASENAMES = {"index.md", "home.md", "README.md", "log.md"}


# ---------------- frontmatter parsing ----------------


_FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
_CITES_BLOCK_RE = re.compile(r"^cites:\s*\n((?:\s+-\s+.+\n)+)", re.MULTILINE)
_CITES_INLINE_RE = re.compile(r"^cites:\s*\[(.*?)\]\s*$", re.MULTILINE)
# `[[some/path]]` body link
_BODY_LINK_RE = re.compile(r"\[\[([^\]\|]+)(?:\|[^\]]+)?\]\]")


def _extract_cites(text: str) -> list[str]:
    """Parse a wiki page's `cites:` frontmatter into a list of path strings."""
    fm_m = _FM_RE.match(text)
    if not fm_m:
        return []
    fm_text = fm_m.group(1)

    # Block-style:
    #   cites:
    #     - ../findings/x.md
    #     - ../findings/y.md
    block = _CITES_BLOCK_RE.search(fm_text + "\n")
    if block:
        items = [
            line.strip().lstrip("- ").strip().strip("\"'")
            for line in block.group(1).splitlines()
            if line.strip().startswith("- ")
        ]
        return [i for i in items if i]

    # Inline:  cites: [a.md, b.md]
    inline = _CITES_INLINE_RE.search(fm_text)
    if inline:
        return [
            s.strip().strip("\"'")
            for s in inline.group(1).split(",")
            if s.strip()
        ]
    return []


# ---------------- check 3: orphans ----------------


def _wiki_pages(wiki: Path) -> list[Path]:
    """All .md pages under wiki/ minus housekeeping."""
    pages: list[Path] = []
    for p in wiki.rglob("*.md"):
        if p.name in _HOUSEKEEPING_BASENAMES:
            continue
        if p.name.startswith("_"):
            continue   # _synthesis.md and similar
        pages.append(p)
    return sorted(pages)


def _index_referenced_paths(wiki: Path) -> set[Path]:
    """Read index.md and resolve every relative-link target to an absolute Path."""
    idx = wiki / "index.md"
    if not idx.is_file():
        return set()
    text = idx.read_text()
    targets: set[Path] = set()
    for m in re.finditer(r"\]\(([^)]+\.md)\)", text):
        rel = m.group(1)
        # Skip external / anchor-only
        if rel.startswith("http") or rel.startswith("#"):
            continue
        # Resolve relative to wiki/
        resolved = (wiki / rel).resolve()
        targets.add(resolved)
    return targets


def check_orphans(wiki: Path) -> list[Path]:
    """Pages on disk in wiki/ that are NOT referenced from index.md."""
    referenced = _index_referenced_paths(wiki)
    orphans = [p for p in _wiki_pages(wiki) if p.resolve() not in referenced]
    return orphans


# ---------------- check 4: broken cites ----------------


@dataclass
class BrokenCite:
    source_page: Path
    cited_target: Path
    reason: str


def check_broken_cites(wiki: Path) -> list[BrokenCite]:
    """For every cites: entry pointing inside wiki/, verify the target exists."""
    broken: list[BrokenCite] = []
    for p in _wiki_pages(wiki):
        text = p.read_text()
        for c in _extract_cites(text):
            # Skip externals
            if c.startswith("http://") or c.startswith("https://"):
                continue
            # Skip glob stubs (5-*.md) — agent-friendly placeholders
            if "*" in c:
                continue
            target = (p.parent / c).resolve()
            # Only count as broken if the target *would* be inside wiki/
            try:
                target.relative_to(wiki.resolve())
            except ValueError:
                # Outside wiki/ — e.g. ../../source/foo.md or ../scripts/x.py;
                # tolerated since wiki_lint scope is wiki-internal hygiene.
                continue
            if not target.is_file():
                broken.append(BrokenCite(
                    source_page=p, cited_target=target,
                    reason="cite target does not exist on disk",
                ))
    return broken


# ---------------- check 5: body link gaps ----------------


@dataclass
class BodyLinkGap:
    source_page: Path
    target: str         # the body-link path (verbatim)
    suggested_cite: str   # the cites: entry to add


def _is_same_dir_link(link_target: str) -> bool:
    """[[foo]] is same-dir; [[some/path]] or [[../sibling/x]] is cross-dir."""
    return "/" not in link_target and not link_target.startswith("..")


def check_body_link_gaps(wiki: Path) -> list[BodyLinkGap]:
    """For each cross-directory [[link]], verify the page has a matching cite."""
    gaps: list[BodyLinkGap] = []
    for p in _wiki_pages(wiki):
        text = p.read_text()
        body = text
        if (m := _FM_RE.match(text)):
            body = text[m.end():]
        cites = set(_extract_cites(text))

        for link in _BODY_LINK_RE.findall(body):
            link = link.strip()
            if _is_same_dir_link(link):
                continue
            # Normalize: body links typically omit `.md`
            link_with_md = link if link.endswith(".md") else link + ".md"
            # If any cite entry contains the link tail, consider it satisfied.
            tail = link_with_md.split("/")[-1]
            if any(tail in c or link_with_md in c or link in c for c in cites):
                continue
            gaps.append(BodyLinkGap(
                source_page=p, target=link,
                suggested_cite=link_with_md,
            ))
    return gaps


# ---------------- report + run ----------------


def report(wiki: Path) -> str:
    pages = _wiki_pages(wiki)
    orphans = check_orphans(wiki)
    broken = check_broken_cites(wiki)
    gaps = check_body_link_gaps(wiki)

    lines = [
        f"Wiki lint — {wiki}",
        f"  pages:            {len(pages)}",
        f"  orphans:          {len(orphans)}",
        f"  broken cites:     {len(broken)}",
        f"  body link gaps:   {len(gaps)}",
    ]
    if orphans:
        lines.append("")
        lines.append("Orphan pages (in wiki/ but missing from index.md):")
        for o in orphans[:10]:
            lines.append(f"  - {o.relative_to(wiki)}")
        if len(orphans) > 10:
            lines.append(f"  ... and {len(orphans) - 10} more")
    if broken:
        lines.append("")
        lines.append("Broken cites:")
        for b in broken[:10]:
            lines.append(f"  - {b.source_page.relative_to(wiki)} → {b.cited_target.relative_to(wiki)}")
        if len(broken) > 10:
            lines.append(f"  ... and {len(broken) - 10} more")
    if gaps:
        lines.append("")
        lines.append("Body links missing from cites:")
        for g in gaps[:10]:
            lines.append(f"  - {g.source_page.relative_to(wiki)}  ↦ [[{g.target}]]  "
                         f"(add `{g.suggested_cite}` to cites)")
        if len(gaps) > 10:
            lines.append(f"  ... and {len(gaps) - 10} more")
    return "\n".join(lines)


def run(wiki: Path, *, strict: bool = False) -> int:
    """Print the lint report. Return nonzero in strict mode if findings exist."""
    print(report(wiki))
    if not strict:
        return 0
    n = (len(check_orphans(wiki)) + len(check_broken_cites(wiki))
         + len(check_body_link_gaps(wiki)))
    return 0 if n == 0 else 1


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    p.add_argument("--wiki", type=Path, default=DEFAULT_WIKI)
    p.add_argument("--strict", action="store_true",
                   help="Exit nonzero on any findings (default: report-only, exit 0).")
    args = p.parse_args(argv)
    return run(args.wiki, strict=args.strict)


if __name__ == "__main__":
    raise SystemExit(main())
