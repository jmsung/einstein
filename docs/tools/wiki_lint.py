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
    uv run python docs/tools/wiki_lint.py --wiki knowledge/wiki/     # custom wiki dir
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
DEFAULT_WIKI = _REPO / "knowledge" / "wiki"

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
        return [s.strip().strip("\"'") for s in inline.group(1).split(",") if s.strip()]
    return []


# ---------------- check 3: orphans ----------------


def _wiki_pages(wiki: Path) -> list[Path]:
    """All .md pages under wiki/ minus housekeeping."""
    pages: list[Path] = []
    for p in wiki.rglob("*.md"):
        if p.name in _HOUSEKEEPING_BASENAMES:
            continue
        if p.name.startswith("_"):
            continue  # _synthesis.md and similar
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
                broken.append(
                    BrokenCite(
                        source_page=p,
                        cited_target=target,
                        reason="cite target does not exist on disk",
                    )
                )
    return broken


# ---------------- check 5: body link gaps ----------------


@dataclass
class BodyLinkGap:
    source_page: Path
    target: str  # the body-link path (verbatim)
    suggested_cite: str  # the cites: entry to add


def _is_same_dir_link(link_target: str) -> bool:
    """[[foo]] is same-dir; [[some/path]] or [[../sibling/x]] is cross-dir."""
    return "/" not in link_target and not link_target.startswith("..")


def check_body_link_gaps(wiki: Path) -> list[BodyLinkGap]:
    """For each cross-directory [[link]], verify the page has a matching cite."""
    gaps: list[BodyLinkGap] = []
    for p in _wiki_pages(wiki):
        text = p.read_text()
        body = text
        if m := _FM_RE.match(text):
            body = text[m.end() :]
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
            gaps.append(
                BodyLinkGap(
                    source_page=p,
                    target=link,
                    suggested_cite=link_with_md,
                )
            )
    return gaps


# ---------------- check 6 + 7: anti-bloat (Phase 4 of meta-learning-automation) ----

# Auto-capture (the Phase-0 gate) can incentivize low-value findings. These two
# checks are the anti-bloat counter: they SURFACE near-duplicate and stale-uncited
# findings for human merge/archival — they never auto-delete (merge stays human-
# gated, like promotion). Report-only: not part of strict-mode's failure count, so
# they don't block cycle_runner on a wiki that already carries some duplication.

_DRAFTED_RE = re.compile(r"^drafted:\s*(\d{4}-\d{2}-\d{2})", re.MULTILINE)
_WORD_RE = re.compile(r"[a-z0-9]{4,}")
# Default near-duplicate Jaccard threshold + default finding TTL.
DEFAULT_DUP_THRESHOLD = 0.80
DEFAULT_TTL_DAYS = 120


def _body_tokens(text: str) -> set[str]:
    """Lowercase word-set of a page body (frontmatter stripped) — for cheap
    Jaccard similarity. Words < 4 chars dropped to cut stop-word noise."""
    body = text
    if m := _FM_RE.match(text):
        body = text[m.end() :]
    return set(_WORD_RE.findall(body.lower()))


def _drafted_date(text: str) -> str | None:
    fm_m = _FM_RE.match(text)
    if not fm_m:
        return None
    m = _DRAFTED_RE.search(fm_m.group(1))
    return m.group(1) if m else None


def _findings_pages(wiki: Path) -> list[Path]:
    return [p for p in _wiki_pages(wiki) if p.parent.name == "findings"]


@dataclass
class NearDuplicate:
    page_a: Path
    page_b: Path
    similarity: float


def check_near_duplicates(
    wiki: Path, *, threshold: float = DEFAULT_DUP_THRESHOLD
) -> list[NearDuplicate]:
    """Findings/ page pairs whose body token-sets overlap ≥ `threshold` (Jaccard).
    O(n²) over ~100 findings — cheap. Candidates for human merge."""
    pages = _findings_pages(wiki)
    toks = {p: _body_tokens(p.read_text()) for p in pages}
    dups: list[NearDuplicate] = []
    for i, a in enumerate(pages):
        ta = toks[a]
        if not ta:
            continue
        for b in pages[i + 1 :]:
            tb = toks[b]
            if not tb:
                continue
            inter = len(ta & tb)
            if inter == 0:
                continue
            sim = inter / len(ta | tb)
            if sim >= threshold:
                dups.append(NearDuplicate(page_a=a, page_b=b, similarity=sim))
    return sorted(dups, key=lambda d: d.similarity, reverse=True)


@dataclass
class StaleFinding:
    page: Path
    drafted: str
    age_days: int


def _inbound_cite_targets(wiki: Path) -> set[Path]:
    """Every cite/body-link target that resolves inside wiki/ — the set of pages
    referenced by *another* page. Self-references are excluded so a self-citing
    stale finding can't escape the stale-uncited check."""
    referenced: set[Path] = set()
    for p in _wiki_pages(wiki):
        src = p.resolve()
        text = p.read_text()
        for c in _extract_cites(text):
            if c.startswith("http") or "*" in c:
                continue
            t = (p.parent / c).resolve()
            if t != src:
                referenced.add(t)
        body = text[m.end() :] if (m := _FM_RE.match(text)) else text
        for link in _BODY_LINK_RE.findall(body):
            link = link.strip()
            link = link if link.endswith(".md") else link + ".md"
            t = (p.parent / link).resolve()
            if t != src:
                referenced.add(t)
    return referenced


def check_stale_uncited(
    wiki: Path, *, ttl_days: int = DEFAULT_TTL_DAYS, today: str | None = None
) -> list[StaleFinding]:
    """Findings older than `ttl_days` with ZERO inbound cites — the bloat profile
    (old AND never reused). Surfaced for human archival/merge, never auto-deleted.
    `today` (YYYY-MM-DD) is injectable for tests; defaults to the system date."""
    import datetime as _dt

    now = _dt.date.fromisoformat(today) if today else _dt.date.today()
    referenced = _inbound_cite_targets(wiki)
    stale: list[StaleFinding] = []
    for p in _findings_pages(wiki):
        if p.resolve() in referenced:
            continue  # reused → not bloat
        drafted = _drafted_date(p.read_text())
        if not drafted:
            continue  # no date → can't age it; skip rather than false-flag
        try:
            age = (now - _dt.date.fromisoformat(drafted)).days
        except ValueError:
            continue
        if age > ttl_days:
            stale.append(StaleFinding(page=p, drafted=drafted, age_days=age))
    return sorted(stale, key=lambda s: s.age_days, reverse=True)


# ---------------- report + run ----------------


def report(wiki: Path, *, ttl_days: int = DEFAULT_TTL_DAYS, today: str | None = None) -> str:
    pages = _wiki_pages(wiki)
    orphans = check_orphans(wiki)
    broken = check_broken_cites(wiki)
    gaps = check_body_link_gaps(wiki)
    dups = check_near_duplicates(wiki)
    stale = check_stale_uncited(wiki, ttl_days=ttl_days, today=today)

    lines = [
        f"Wiki lint — {wiki}",
        f"  pages:            {len(pages)}",
        f"  orphans:          {len(orphans)}",
        f"  broken cites:     {len(broken)}",
        f"  body link gaps:   {len(gaps)}",
        f"  near-duplicates:  {len(dups)}   (anti-bloat; human merge)",
        f"  stale-uncited:    {len(stale)}   (>{ttl_days}d, 0 inbound cites)",
    ]
    if dups:
        lines.append("")
        lines.append("Near-duplicate findings (candidates for merge):")
        for d in dups[:10]:
            lines.append(
                f"  - {d.similarity:.2f}  {d.page_a.relative_to(wiki)}  ≈  "
                f"{d.page_b.relative_to(wiki)}"
            )
        if len(dups) > 10:
            lines.append(f"  ... and {len(dups) - 10} more")
    if stale:
        lines.append("")
        lines.append("Stale-uncited findings (candidates for archival):")
        for s in stale[:10]:
            lines.append(f"  - {s.age_days}d  {s.page.relative_to(wiki)}  (drafted {s.drafted})")
        if len(stale) > 10:
            lines.append(f"  ... and {len(stale) - 10} more")
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
            lines.append(
                f"  - {b.source_page.relative_to(wiki)} → {b.cited_target.relative_to(wiki)}"
            )
        if len(broken) > 10:
            lines.append(f"  ... and {len(broken) - 10} more")
    if gaps:
        lines.append("")
        lines.append("Body links missing from cites:")
        for g in gaps[:10]:
            lines.append(
                f"  - {g.source_page.relative_to(wiki)}  ↦ [[{g.target}]]  "
                f"(add `{g.suggested_cite}` to cites)"
            )
        if len(gaps) > 10:
            lines.append(f"  ... and {len(gaps) - 10} more")
    return "\n".join(lines)


def run(
    wiki: Path,
    *,
    strict: bool = False,
    ttl_days: int = DEFAULT_TTL_DAYS,
    today: str | None = None,
) -> int:
    """Print the lint report. Return nonzero in strict mode if STRUCTURAL findings
    exist. The anti-bloat checks (near-duplicate / stale-uncited) are advisory and
    deliberately excluded from the strict-mode failure count — they surface for
    human merge, they don't block the cycle."""
    print(report(wiki, ttl_days=ttl_days, today=today))
    if not strict:
        return 0
    n = len(check_orphans(wiki)) + len(check_broken_cites(wiki)) + len(check_body_link_gaps(wiki))
    return 0 if n == 0 else 1


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    p.add_argument("--wiki", type=Path, default=DEFAULT_WIKI)
    p.add_argument(
        "--strict",
        action="store_true",
        help="Exit nonzero on any STRUCTURAL findings (default: report-only).",
    )
    p.add_argument(
        "--ttl-days",
        type=int,
        default=DEFAULT_TTL_DAYS,
        help=f"Stale-finding TTL in days (default {DEFAULT_TTL_DAYS}).",
    )
    p.add_argument(
        "--today", default=None, help="Override 'today' (YYYY-MM-DD) for the stale check (testing)."
    )
    args = p.parse_args(argv)
    return run(args.wiki, strict=args.strict, ttl_days=args.ttl_days, today=args.today)


if __name__ == "__main__":
    raise SystemExit(main())
