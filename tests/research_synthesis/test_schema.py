"""Tests for the LiteratureSynthesis schema + markdown formatter."""

from __future__ import annotations

import json

import pytest

from einstein.research_synthesis import schema as S


@pytest.fixture
def sample() -> S.LiteratureSynthesis:
    return S.LiteratureSynthesis(
        problem_id=14,
        problem_slug="circle-packing-square",
        drafted_at="2026-05-25",
        queries=["circle packing square optimal", "newton max polish strict tol"],
        top_sources=[
            S.Hit(
                path="docs/source/2026-lee-meta-harness-end-to-end-optimization-model.md",
                score=0.88,
                snippet="filesystem-as-feedback over prior candidates",
                collection="einstein-wiki-source",
            ),
            S.Hit(
                path="docs/source/2024-baek-researchagent-iterative-research-idea.md",
                score=0.83,
                snippet="entity co-occurrence retrieval surfaces cross-domain",
                collection="einstein-wiki-source",
            ),
        ],
        top_wiki=[
            S.Hit(
                path="docs/wiki/concepts/equioscillation.md",
                score=0.71,
                snippet="Chebyshev equioscillation criterion",
                collection="einstein-wiki",
            ),
        ],
        cross_source_patterns=[
            S.CrossSourcePattern(
                name="A: raw artifact > summary",
                description="Meta-Harness +15pt traces-over-summary ablation supports keeping full distillation",
                supporting_sources=[
                    "docs/source/2026-lee-meta-harness-end-to-end-optimization-model.md",
                ],
            ),
        ],
        proposed_approaches=[
            S.ProposedApproach(
                description="Try Newton-max polish with strict tol=0",
                cited_sources=[
                    "docs/source/2026-lee-meta-harness-end-to-end-optimization-model.md",
                ],
                rationale="Filesystem-of-prior-attempts pattern; precedent for additive over destructive edits",
            ),
        ],
        gaps_identified=["No prior work on P14 with N=50 polish + active-pair detection"],
    )


def test_roundtrip_json(sample: S.LiteratureSynthesis) -> None:
    """Dataclass survives a JSON round-trip exactly."""
    js = sample.to_json()
    parsed = json.loads(js)
    restored = S.LiteratureSynthesis.from_json(json.dumps(parsed))
    assert restored == sample


def test_from_json_rejects_missing_required(sample: S.LiteratureSynthesis) -> None:
    """Missing required field raises ValueError, not KeyError."""
    d = sample.to_dict()
    del d["problem_id"]
    with pytest.raises(ValueError, match="problem_id"):
        S.LiteratureSynthesis.from_json(json.dumps(d))


def test_from_json_rejects_malformed_json() -> None:
    """Garbage input raises ValueError, not bare JSONDecodeError."""
    with pytest.raises(ValueError, match="JSON"):
        S.LiteratureSynthesis.from_json("not json at all {")


def test_to_markdown_contains_required_sections(sample: S.LiteratureSynthesis) -> None:
    md = sample.to_markdown()
    # Frontmatter
    assert md.startswith("---\n")
    assert "type: literature-synthesis" in md
    assert "author: agent" in md
    assert "problem_id: 14" in md
    assert "drafted: 2026-05-25" in md
    # Body sections
    assert "# Literature synthesis: P14 — circle-packing-square" in md
    assert "## Queries" in md
    assert "## Top sources" in md
    assert "## Cross-source patterns" in md
    assert "## Proposed approaches" in md
    assert "## Gaps identified" in md
    # Specific content
    assert "2026-lee-meta-harness" in md
    assert "Chebyshev equioscillation" in md
    assert "A: raw artifact > summary" in md


def test_to_markdown_handles_empty_patterns(sample: S.LiteratureSynthesis) -> None:
    """Empty pattern/approach lists should not crash and should mark explicitly."""
    sample.cross_source_patterns = []
    sample.proposed_approaches = []
    md = sample.to_markdown()
    assert "## Cross-source patterns" in md
    assert "_None identified._" in md
    assert "## Proposed approaches" in md


def test_json_schema_is_valid_json() -> None:
    """JSON schema constant parses as JSON (sanity check for --json-schema use)."""
    sch = S.JSON_SCHEMA
    parsed = json.loads(sch) if isinstance(sch, str) else sch
    assert parsed["type"] == "object"
    assert "problem_id" in parsed["properties"]
    assert "cross_source_patterns" in parsed["properties"]


def test_hit_ordering_by_score() -> None:
    """Hits sort descending by score (used in gather/dedupe)."""
    a = S.Hit(path="a.md", score=0.5, snippet="a", collection="einstein-wiki")
    b = S.Hit(path="b.md", score=0.9, snippet="b", collection="einstein-wiki")
    c = S.Hit(path="c.md", score=0.7, snippet="c", collection="einstein-wiki")
    ordered = sorted([a, b, c], key=lambda h: h.score, reverse=True)
    assert [h.path for h in ordered] == ["b.md", "c.md", "a.md"]
