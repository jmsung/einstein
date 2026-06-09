"""Tests for docs/tools/wiki_lint.py — structural wiki health checks.

Covers the agent-native subset of the wiki-lint skill: orphans (pages
not in index.md), broken cites (frontmatter cite paths that don't
resolve), and body link gaps (`[[cross-dir/foo]]` wiki links without
matching cites: entries).
"""

from __future__ import annotations

import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "docs" / "tools"))

import wiki_lint  # noqa: E402


def _make_wiki(tmp_path: Path) -> Path:
    wiki = tmp_path / "wiki"
    (wiki / "concepts").mkdir(parents=True)
    (wiki / "techniques").mkdir()
    (wiki / "findings").mkdir()
    return wiki


def test_check_orphans_lists_pages_not_in_index(tmp_path: Path) -> None:
    wiki = _make_wiki(tmp_path)
    (wiki / "index.md").write_text(
        "# Index\n\n- [foo](concepts/foo.md)\n- [bar](concepts/bar.md)\n"
    )
    (wiki / "concepts" / "foo.md").write_text("---\ntype: concept\n---\n# foo")
    (wiki / "concepts" / "bar.md").write_text("---\ntype: concept\n---\n# bar")
    (wiki / "concepts" / "orphan.md").write_text("---\ntype: concept\n---\n# orphan")
    orphans = wiki_lint.check_orphans(wiki)
    paths = {p.name for p in orphans}
    assert "orphan.md" in paths
    assert "foo.md" not in paths
    assert "bar.md" not in paths


def test_check_orphans_skips_index_readme_and_underscored(tmp_path: Path) -> None:
    wiki = _make_wiki(tmp_path)
    (wiki / "index.md").write_text("# Index")
    (wiki / "README.md").write_text("# Readme")
    (wiki / "concepts" / "_synthesis.md").write_text("---\ntype: concept\n---")
    (wiki / "home.md").write_text("# Home")  # also commonly an index variant
    orphans = wiki_lint.check_orphans(wiki)
    # These housekeeping pages should never be flagged
    assert all("index" not in p.name for p in orphans)
    assert all("README" not in p.name for p in orphans)
    assert all("_synthesis" not in p.name for p in orphans)


def test_check_broken_cites_finds_dangling_references(tmp_path: Path) -> None:
    wiki = _make_wiki(tmp_path)
    (wiki / "concepts" / "foo.md").write_text(
        "---\n"
        "type: concept\n"
        "cites:\n"
        "  - ../findings/exists.md\n"
        "  - ../findings/missing.md\n"
        "  - ../techniques/also-missing.md\n"
        "---\n# foo\n"
    )
    (wiki / "findings" / "exists.md").write_text("---\ntype: finding\n---\n# exists")
    broken = wiki_lint.check_broken_cites(wiki)
    targets = sorted([str(b.cited_target) for b in broken])
    assert any("missing.md" in t for t in targets)
    assert any("also-missing.md" in t for t in targets)
    assert not any("exists.md" in t for t in targets)


def test_check_broken_cites_ignores_external_paths(tmp_path: Path) -> None:
    wiki = _make_wiki(tmp_path)
    (wiki / "concepts" / "foo.md").write_text(
        "---\n"
        "type: concept\n"
        "cites:\n"
        "  - ../../source/some-paper.md\n"
        "  - ../findings/missing.md\n"
        "  - https://example.com/external\n"
        "  - ../wiki/problems/5-*.md\n"
        "---\n"
    )
    broken = wiki_lint.check_broken_cites(wiki)
    # Glob-stubs (5-*.md) and external URLs shouldn't be flagged
    targets = [str(b.cited_target) for b in broken]
    assert not any("example.com" in t for t in targets)
    assert not any("5-*.md" in t for t in targets)
    # source/ cites with no matching file: tolerated (outside wiki/)
    # missing.md in wiki/findings/: flagged
    assert any("missing.md" in t for t in targets)


def test_check_body_link_gaps_finds_uncited_wiki_links(tmp_path: Path) -> None:
    wiki = _make_wiki(tmp_path)
    (wiki / "concepts" / "foo.md").write_text(
        "---\n"
        "type: concept\n"
        "cites:\n"
        "  - ../findings/cited.md\n"
        "---\n"
        "# foo\n"
        "See [[../findings/cited]] for details.\n"
        "Also see [[../techniques/uncited]] which is referenced but not cited.\n"
    )
    (wiki / "findings" / "cited.md").write_text("# cited")
    (wiki / "techniques" / "uncited.md").write_text("# uncited")
    gaps = wiki_lint.check_body_link_gaps(wiki)
    suggested = [(g.source_page.name, str(g.target)) for g in gaps]
    assert any("uncited" in t for _, t in suggested)
    assert not any("cited" in t and "uncited" not in t for _, t in suggested)


def test_check_body_link_gaps_ignores_same_dir_links(tmp_path: Path) -> None:
    """Sibling references like [[other-concept]] in same dir don't need cites."""
    wiki = _make_wiki(tmp_path)
    (wiki / "concepts" / "foo.md").write_text(
        "---\ntype: concept\ncites: []\n---\n# foo\nSee [[other-concept]] in the same directory.\n"
    )
    (wiki / "concepts" / "other-concept.md").write_text("# other")
    gaps = wiki_lint.check_body_link_gaps(wiki)
    assert not any("other-concept" in str(g.target) for g in gaps)


def test_report_summary(tmp_path: Path) -> None:
    wiki = _make_wiki(tmp_path)
    (wiki / "index.md").write_text("# Index")
    (wiki / "concepts" / "orphan.md").write_text("---\ntype: concept\n---\n# x")
    out = wiki_lint.report(wiki)
    assert "pages" in out.lower()
    assert "orphan" in out.lower()


def test_run_returns_zero_when_clean(tmp_path: Path) -> None:
    wiki = _make_wiki(tmp_path)
    (wiki / "index.md").write_text(
        "# Index\n\n- [foo](concepts/foo.md)\n- [bar](findings/bar.md)\n"
    )
    (wiki / "concepts" / "foo.md").write_text(
        "---\ntype: concept\ncites:\n  - ../findings/bar.md\n---\n# foo\n"
    )
    (wiki / "findings" / "bar.md").write_text("# bar")
    rc = wiki_lint.run(wiki, strict=True)
    assert rc == 0


def test_run_returns_nonzero_when_strict_and_findings(tmp_path: Path) -> None:
    wiki = _make_wiki(tmp_path)
    (wiki / "index.md").write_text("# Index")
    (wiki / "concepts" / "orphan.md").write_text("---\ntype: concept\n---\n# x")
    rc = wiki_lint.run(wiki, strict=True)
    assert rc != 0


def test_run_returns_zero_when_lax_even_with_findings(tmp_path: Path) -> None:
    """Default (non-strict) mode warns but returns 0 — cycle_runner uses this."""
    wiki = _make_wiki(tmp_path)
    (wiki / "index.md").write_text("# Index")
    (wiki / "concepts" / "orphan.md").write_text("---\ntype: concept\n---\n# x")
    rc = wiki_lint.run(wiki, strict=False)
    assert rc == 0


# ---------------- anti-bloat checks (Phase 4 of meta-learning-automation) ----


def _finding(words: str, *, drafted: str | None = None, cites: str = "") -> str:
    fm = "---\ntype: finding\nauthor: agent\n"
    if drafted:
        fm += f"drafted: {drafted}\n"
    if cites:
        fm += f"cites:\n  - {cites}\n"
    fm += "---\n"
    return fm + "# F\n" + words + "\n"


def test_near_duplicates_flags_high_overlap(tmp_path: Path) -> None:
    wiki = _make_wiki(tmp_path)
    shared = "warm self pruning compact support basin floor parameterization rank deficiency"
    (wiki / "findings" / "a.md").write_text(_finding(shared + " alpha extra one"))
    (wiki / "findings" / "b.md").write_text(_finding(shared + " alpha extra one"))
    (wiki / "findings" / "c.md").write_text(
        _finding("completely different content sphere packing kissing number lattice")
    )
    dups = wiki_lint.check_near_duplicates(wiki, threshold=0.8)
    names = {(d.page_a.name, d.page_b.name) for d in dups}
    assert ("a.md", "b.md") in names
    assert all("c.md" not in pair for pair in names)


def test_near_duplicates_respects_threshold(tmp_path: Path) -> None:
    wiki = _make_wiki(tmp_path)
    (wiki / "findings" / "a.md").write_text(_finding("alpha beta gamma delta epsilon"))
    (wiki / "findings" / "b.md").write_text(_finding("alpha beta zeta theta iota kappa"))
    assert wiki_lint.check_near_duplicates(wiki, threshold=0.9) == []


def test_stale_uncited_flags_old_and_unreferenced(tmp_path: Path) -> None:
    wiki = _make_wiki(tmp_path)
    (wiki / "findings" / "old.md").write_text(
        _finding("lonely old finding text", drafted="2026-01-01")
    )
    stale = wiki_lint.check_stale_uncited(wiki, ttl_days=120, today="2026-06-08")
    assert [s.page.name for s in stale] == ["old.md"]
    assert stale[0].age_days > 120


def test_stale_uncited_skips_recent_and_reused(tmp_path: Path) -> None:
    wiki = _make_wiki(tmp_path)
    # recent → not stale
    (wiki / "findings" / "recent.md").write_text(_finding("recent text", drafted="2026-06-01"))
    # old but cited by another page → reused, not bloat
    (wiki / "findings" / "old-cited.md").write_text(
        _finding("old but useful", drafted="2026-01-01")
    )
    (wiki / "concepts" / "ref.md").write_text(
        "---\ntype: concept\nauthor: agent\ncites:\n  - ../findings/old-cited.md\n---\n# ref\n"
    )
    stale = wiki_lint.check_stale_uncited(wiki, ttl_days=120, today="2026-06-08")
    assert stale == []


def test_anti_bloat_excluded_from_strict_failure(tmp_path: Path) -> None:
    """Near-dup / stale are advisory: they must NOT make strict mode fail."""
    wiki = _make_wiki(tmp_path)
    (wiki / "index.md").write_text("# Index")
    dup = "shared tokens one two three four five six seven eight nine"
    (wiki / "findings" / "a.md").write_text(_finding(dup))
    (wiki / "findings" / "b.md").write_text(_finding(dup))
    # index references both → no orphans; no broken cites; no body gaps.
    (wiki / "index.md").write_text("# Index\n- [a](findings/a.md)\n- [b](findings/b.md)\n")
    assert wiki_lint.check_near_duplicates(wiki, threshold=0.8)  # dups exist
    assert wiki_lint.run(wiki, strict=True) == 0  # but strict still passes
