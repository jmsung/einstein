"""Tests for docs/tools/seed_ingest.py.

Two-step pipeline:
  propose:  coverage.json + arxiv  →  candidates.json (approved: null)
  apply:    candidates.json + Internet + pdf_to_md  →  docs/source/*.md

Tests cover (a) pure helpers (slug, frontmatter, abs→pdf url),
(b) propose with mocked arxiv, (c) apply with mocked download + pdf_to_md.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from unittest.mock import patch

import pytest

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "docs" / "tools"))

import seed_ingest as si  # noqa: E402


# ---------------- helper fixtures ----------------


def _make_coverage(tmp_path: Path, rows: list[dict]) -> Path:
    """Write a minimal coverage.json fixture."""
    path = tmp_path / "coverage.json"
    path.write_text(json.dumps({
        "generated_at": "2026-05-23",
        "rows": rows,
    }))
    return path


def _coverage_row(name: str, kind: str = "concept", refs: list[int] | None = None,
                  classification: str = "under-sourced") -> dict:
    return {
        "name": name,
        "kind": kind,
        "refs": refs or [1, 2],
        "has_page": True,
        "has_source": False,
        "classification": classification,
    }


# ---------------- pure helpers ----------------


def test_slug_from_metadata_kebab_and_year_first() -> None:
    slug = si._slug_from_metadata(
        title="On the autocorrelation inequality for Sidon sets",
        year="2019",
        authors="A. B. Smith, C. Jones",
    )
    assert slug.startswith("2019-")
    # First author surname appears
    assert "smith" in slug
    # Kebab-case, lowercase, no punctuation
    assert slug == slug.lower()
    assert " " not in slug
    assert "." not in slug


def test_slug_truncates_to_reasonable_length() -> None:
    slug = si._slug_from_metadata(
        title="A very long title that goes on and on and on and on and on and on and on",
        year="2020",
        authors="X. Y. Z.",
    )
    assert len(slug) <= 60


def test_abs_url_to_pdf_url() -> None:
    assert si._abs_to_pdf_url("http://arxiv.org/abs/1234.5678v1") == "http://arxiv.org/pdf/1234.5678v1.pdf"
    assert si._abs_to_pdf_url("https://arxiv.org/abs/2306.00001") == "https://arxiv.org/pdf/2306.00001.pdf"
    # Already-pdf URLs pass through
    assert si._abs_to_pdf_url("http://arxiv.org/pdf/foo.pdf") == "http://arxiv.org/pdf/foo.pdf"


def test_build_source_frontmatter_required_fields() -> None:
    fm = si._build_source_frontmatter(
        candidate={
            "title": "Test Paper",
            "authors": "A. Smith",
            "year": "2019",
            "abs_url": "http://arxiv.org/abs/1234.5678",
            "summary": "abstract",
            "slug": "2019-smith-test",
        },
        concept="basin-rigidity.md",
        problem_refs=[5, 6, 7],
    )
    assert fm["type"] == "source"
    assert fm["kind"] == "paper"
    assert fm["title"] == "Test Paper"
    assert fm["author"] == "agent"
    assert fm["source_type"] == "arxiv"
    assert fm["source_url"] == "http://arxiv.org/abs/1234.5678"
    assert fm["ingested_for_concept"] == "basin-rigidity.md"
    assert "../wiki/problems/5-" in " ".join(fm["cites"]) or any("problem-5" in c or "5-" in c for c in fm["cites"])
    # cites includes the concept page
    assert any("basin-rigidity" in c for c in fm["cites"])


# ---------------- propose ----------------


def test_load_vocab_yaml(tmp_path: Path) -> None:
    yaml_path = tmp_path / "vocab.yaml"
    yaml_path.write_text(
        "basin-rigidity.md:\n"
        "  - \"first-order rigidity\"\n"
        "  - \"isolated local minimum\"\n"
        "arena-tolerance-drift.md: []\n"
    )
    vocab = si._load_vocab(yaml_path)
    assert vocab["basin-rigidity.md"] == ["first-order rigidity", "isolated local minimum"]
    assert vocab["arena-tolerance-drift.md"] == []


def test_load_vocab_missing_file_returns_empty(tmp_path: Path) -> None:
    vocab = si._load_vocab(tmp_path / "no-such.yaml")
    assert vocab == {}


def test_build_vocab_query_ors_phrases() -> None:
    q = si._build_vocab_query(["first-order rigidity", "isolated local minimum"])
    assert 'all:"first-order rigidity"' in q
    assert 'all:"isolated local minimum"' in q
    assert " OR " in q
    assert "cat:math." in q


def test_propose_uses_vocab_when_slug_mapped(tmp_path: Path) -> None:
    """When the YAML maps a slug, propose should call search_arxiv with the
    vocab-derived query (containing the mapped phrases), not the slug as phrase."""
    coverage = _make_coverage(tmp_path, [
        _coverage_row("basin-rigidity.md", refs=[1, 2, 3]),
    ])
    out = tmp_path / "candidates.json"
    vocab_path = tmp_path / "vocab.yaml"
    vocab_path.write_text(
        "basin-rigidity.md:\n"
        "  - \"first-order rigidity\"\n"
        "  - \"isolated local minimum\"\n"
    )

    captured_queries: list[str] = []

    def fake_search(query: str, max_results: int = 5):
        captured_queries.append(query)
        return [{"title": "T", "authors": "A", "year": "2020",
                 "abs_url": "http://arxiv.org/abs/1.1", "summary": "S"}]

    with patch.object(si, "search_arxiv", side_effect=fake_search):
        si.propose(coverage_json=coverage, out_path=out, top_n=3,
                   rate_limit_seconds=0, vocab_path=vocab_path)

    assert len(captured_queries) == 1
    assert 'all:"first-order rigidity"' in captured_queries[0]
    assert 'all:"isolated local minimum"' in captured_queries[0]
    # Should NOT be the slug-as-phrase form
    assert 'all:"basin rigidity"' not in captured_queries[0]


def test_propose_skips_empty_vocab_mapping(tmp_path: Path) -> None:
    """When YAML maps slug → empty list, propose should record the row but
    skip the arxiv call (intentional 'unmapped' marker)."""
    coverage = _make_coverage(tmp_path, [
        _coverage_row("arena-tolerance-drift.md", refs=[7, 14]),
    ])
    out = tmp_path / "candidates.json"
    vocab_path = tmp_path / "vocab.yaml"
    vocab_path.write_text("arena-tolerance-drift.md: []\n")

    with patch.object(si, "search_arxiv") as mock_search:
        si.propose(coverage_json=coverage, out_path=out, top_n=3,
                   rate_limit_seconds=0, vocab_path=vocab_path)

    mock_search.assert_not_called()
    data = json.loads(out.read_text())
    block = data["concepts"][0]
    assert block["concept"] == "arena-tolerance-drift.md"
    assert block["candidates"] == []
    assert block.get("vocab_status") == "intentionally-unmapped"


def test_propose_falls_back_to_slug_when_vocab_silent(tmp_path: Path) -> None:
    """Slugs not present in YAML use the original build_query fallback."""
    coverage = _make_coverage(tmp_path, [
        _coverage_row("never-heard-of.md", refs=[1, 2]),
    ])
    out = tmp_path / "candidates.json"
    vocab_path = tmp_path / "vocab.yaml"
    vocab_path.write_text("other-slug.md:\n  - \"phrase\"\n")

    captured_queries: list[str] = []

    def fake_search(query: str, max_results: int = 5):
        captured_queries.append(query)
        return []

    with patch.object(si, "search_arxiv", side_effect=fake_search):
        si.propose(coverage_json=coverage, out_path=out, top_n=3,
                   rate_limit_seconds=0, vocab_path=vocab_path)

    assert len(captured_queries) == 1
    # Fallback uses slug-as-phrase
    assert "never heard of" in captured_queries[0]


def test_propose_filters_to_under_sourced_and_missing_page(tmp_path: Path) -> None:
    coverage = _make_coverage(tmp_path, [
        _coverage_row("alpha.md", classification="under-sourced", refs=[1, 2]),
        _coverage_row("beta.md", classification="well-covered", refs=[1, 2]),
        _coverage_row("gamma.md", classification="missing-page", refs=[1, 2]),
        _coverage_row("delta.md", classification="orphan-or-singleton", refs=[1]),
    ])
    out = tmp_path / "candidates.json"

    fake_results = [{"title": "T", "authors": "A", "year": "2020",
                     "abs_url": "http://arxiv.org/abs/1.1", "summary": "S"}]
    with patch.object(si, "search_arxiv", return_value=fake_results) as mock_search:
        si.propose(coverage_json=coverage, out_path=out, top_n=3, rate_limit_seconds=0)

    data = json.loads(out.read_text())
    concepts = {c["concept"] for c in data["concepts"]}
    assert concepts == {"alpha.md", "gamma.md"}  # under-sourced + missing-page only
    # search was called once per actionable concept
    assert mock_search.call_count == 2


def test_propose_writes_approved_null_per_candidate(tmp_path: Path) -> None:
    coverage = _make_coverage(tmp_path, [
        _coverage_row("alpha.md", refs=[1, 2]),
    ])
    out = tmp_path / "candidates.json"
    fake_results = [
        {"title": "T1", "authors": "A", "year": "2020", "abs_url": "http://arxiv.org/abs/1.1", "summary": "S1"},
        {"title": "T2", "authors": "B", "year": "2021", "abs_url": "http://arxiv.org/abs/1.2", "summary": "S2"},
    ]
    with patch.object(si, "search_arxiv", return_value=fake_results):
        si.propose(coverage_json=coverage, out_path=out, top_n=5, rate_limit_seconds=0)

    data = json.loads(out.read_text())
    cands = data["concepts"][0]["candidates"]
    assert len(cands) == 2
    for c in cands:
        assert c["approved"] is None
        assert "slug" in c


def test_propose_preserves_existing_approvals_on_rerun(tmp_path: Path) -> None:
    """Re-running propose should not overwrite human-set approval flags."""
    coverage = _make_coverage(tmp_path, [_coverage_row("alpha.md", refs=[1, 2])])
    out = tmp_path / "candidates.json"

    # First run
    fake_results = [{"title": "T", "authors": "A", "year": "2020",
                     "abs_url": "http://arxiv.org/abs/1.1", "summary": "S"}]
    with patch.object(si, "search_arxiv", return_value=fake_results):
        si.propose(coverage_json=coverage, out_path=out, top_n=3, rate_limit_seconds=0)

    # Human approves
    data = json.loads(out.read_text())
    data["concepts"][0]["candidates"][0]["approved"] = True
    out.write_text(json.dumps(data))

    # Re-run propose with the same arxiv hit; approval should survive
    with patch.object(si, "search_arxiv", return_value=fake_results):
        si.propose(coverage_json=coverage, out_path=out, top_n=3, rate_limit_seconds=0)

    data2 = json.loads(out.read_text())
    assert data2["concepts"][0]["candidates"][0]["approved"] is True


# ---------------- apply ----------------


def _candidates_doc(*, approved: bool, slug: str = "2020-smith-test") -> dict:
    return {
        "generated_at": "2026-05-23",
        "concepts": [
            {
                "concept": "alpha.md",
                "kind": "concept",
                "refs": [1, 2],
                "query": "(all:\"alpha\") AND (cat:math.NT)",
                "candidates": [
                    {
                        "title": "Test paper", "authors": "A. Smith", "year": "2020",
                        "abs_url": "http://arxiv.org/abs/1234.5678",
                        "summary": "abstract", "slug": slug,
                        "approved": approved,
                    }
                ],
            }
        ],
    }


def test_apply_skips_unapproved(tmp_path: Path) -> None:
    docs = tmp_path / "docs"
    (docs / "source").mkdir(parents=True)
    (docs / "raw").mkdir(parents=True)
    cand_path = tmp_path / "candidates.json"
    cand_path.write_text(json.dumps(_candidates_doc(approved=False)))

    with patch.object(si, "_download_pdf") as mock_dl, \
         patch.object(si, "_run_pdf_to_md") as mock_p2m:
        results = si.apply(candidates_json=cand_path, docs_root=docs)

    assert results == []
    mock_dl.assert_not_called()
    mock_p2m.assert_not_called()


def test_apply_downloads_and_writes_source_for_approved(tmp_path: Path) -> None:
    docs = tmp_path / "docs"
    (docs / "source").mkdir(parents=True)
    (docs / "raw").mkdir(parents=True)
    cand_path = tmp_path / "candidates.json"
    cand_path.write_text(json.dumps(_candidates_doc(approved=True)))

    # Mock the download to just create a fake pdf at the target path
    def fake_download(url: str, dst: Path) -> None:
        dst.write_bytes(b"%PDF-1.4 stub")

    # Mock pdf_to_md to write body content
    def fake_p2m(pdf: Path, out_md: Path) -> None:
        out_md.write_text("# Test paper\n\nbody with $x$ math.\n")

    with patch.object(si, "_download_pdf", side_effect=fake_download), \
         patch.object(si, "_run_pdf_to_md", side_effect=fake_p2m):
        results = si.apply(candidates_json=cand_path, docs_root=docs)

    assert len(results) == 1
    source_path = results[0]
    assert source_path == docs / "source" / "2020-smith-test.md"
    text = source_path.read_text()
    # Frontmatter
    assert text.startswith("---\n")
    assert "type: source" in text
    assert "author: agent" in text
    assert "source_url: http://arxiv.org/abs/1234.5678" in text
    assert "ingested_for_concept: alpha.md" in text
    # Body preserved
    assert "$x$ math" in text
    # Pdf retained in raw/ (FLAT per wiki contract)
    assert (docs / "raw" / "2020-smith-test.pdf").is_file()


def test_apply_idempotent_skip_if_source_exists(tmp_path: Path) -> None:
    docs = tmp_path / "docs"
    (docs / "source").mkdir(parents=True)
    (docs / "raw").mkdir(parents=True)
    # Pre-existing source file
    (docs / "source" / "2020-smith-test.md").write_text("preexisting\n")

    cand_path = tmp_path / "candidates.json"
    cand_path.write_text(json.dumps(_candidates_doc(approved=True)))

    with patch.object(si, "_download_pdf") as mock_dl, \
         patch.object(si, "_run_pdf_to_md") as mock_p2m:
        results = si.apply(candidates_json=cand_path, docs_root=docs)

    assert results == []
    mock_dl.assert_not_called()
    mock_p2m.assert_not_called()
    # Pre-existing file untouched
    assert (docs / "source" / "2020-smith-test.md").read_text() == "preexisting\n"


def test_apply_dry_run_writes_nothing(tmp_path: Path) -> None:
    docs = tmp_path / "docs"
    (docs / "source").mkdir(parents=True)
    (docs / "raw").mkdir(parents=True)
    cand_path = tmp_path / "candidates.json"
    cand_path.write_text(json.dumps(_candidates_doc(approved=True)))

    with patch.object(si, "_download_pdf") as mock_dl, \
         patch.object(si, "_run_pdf_to_md") as mock_p2m:
        results = si.apply(candidates_json=cand_path, docs_root=docs, dry_run=True)

    assert len(results) == 1  # plan reported
    mock_dl.assert_not_called()
    mock_p2m.assert_not_called()
    # No source file written
    assert not (docs / "source" / "2020-smith-test.md").exists()
