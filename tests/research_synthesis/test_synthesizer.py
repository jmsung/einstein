"""Tests for synthesizer.synthesize() — claude_headless orchestration."""

from __future__ import annotations

import json

from einstein.research_synthesis import synthesizer as Syn
from einstein.research_synthesis.schema import Hit, LiteratureSynthesis
from einstein.research_synthesis.synthesizer import _RunnerResult


def _sample_hits() -> tuple[list[Hit], list[Hit]]:
    src = [
        Hit(
            path="docs/source/2026-lee-meta-harness-end-to-end-optimization-model.md",
            score=0.88,
            snippet="filesystem-as-feedback",
            collection="einstein-wiki-source",
        ),
    ]
    wiki = [
        Hit(
            path="docs/wiki/concepts/equioscillation.md",
            score=0.71,
            snippet="Chebyshev criterion",
            collection="einstein-wiki",
        ),
    ]
    return src, wiki


def _ok_runner(payload: dict):
    """Stub runner that returns a successful HeadlessResult-shaped object."""

    def runner(**kwargs):
        return _RunnerResult(ok=True, stdout=json.dumps(payload))

    return runner


def _fail_runner(*, error_kind: str = "unavailable", stdout: str = ""):
    def runner(**kwargs):
        return _RunnerResult(
            ok=False,
            error_kind=error_kind,
            error_message=f"simulated {error_kind}",
            stdout=stdout,
        )

    return runner


def test_happy_path_returns_synthesis() -> None:
    src, wiki = _sample_hits()
    payload = {
        "problem_id": 14,
        "problem_slug": "circle-packing-square",
        "drafted_at": "2026-05-25",
        "queries": ["circle packing"],
        "top_sources": [
            {
                "path": "docs/source/X.md",
                "score": 0.5,
                "snippet": "s",
                "collection": "einstein-wiki-source",
            }
        ],
        "top_wiki": [],
        "cross_source_patterns": [
            {
                "name": "P1",
                "description": "d",
                "supporting_sources": ["docs/source/X.md"],
            }
        ],
        "proposed_approaches": [
            {
                "description": "try Y",
                "cited_sources": ["docs/source/X.md"],
                "rationale": "because",
            }
        ],
        "gaps_identified": ["g1"],
    }
    out = Syn.synthesize(
        problem_id=14,
        problem_slug="circle-packing-square",
        problem_context="ctx",
        source_hits=src,
        wiki_hits=wiki,
        drafted_at="2026-05-25",
        runner=_ok_runner(payload),
    )
    assert isinstance(out, LiteratureSynthesis)
    assert out.problem_id == 14
    assert out.cross_source_patterns[0].name == "P1"
    assert out.proposed_approaches[0].description == "try Y"


def test_returns_none_on_unavailable() -> None:
    src, wiki = _sample_hits()
    out = Syn.synthesize(
        problem_id=14,
        problem_slug="circle-packing-square",
        problem_context="ctx",
        source_hits=src,
        wiki_hits=wiki,
        runner=_fail_runner(error_kind="unavailable"),
    )
    assert out is None


def test_returns_none_on_timeout() -> None:
    src, wiki = _sample_hits()
    out = Syn.synthesize(
        problem_id=14,
        problem_slug="circle-packing-square",
        problem_context="ctx",
        source_hits=src,
        wiki_hits=wiki,
        runner=_fail_runner(error_kind="timeout"),
    )
    assert out is None


def test_returns_none_on_malformed_json() -> None:
    src, wiki = _sample_hits()

    def runner(**kwargs):
        return _RunnerResult(ok=True, stdout="not valid json {{{")

    out = Syn.synthesize(
        problem_id=14,
        problem_slug="circle-packing-square",
        problem_context="ctx",
        source_hits=src,
        wiki_hits=wiki,
        runner=runner,
    )
    assert out is None


def test_returns_none_on_schema_mismatch_missing_required() -> None:
    src, wiki = _sample_hits()
    # Missing problem_id
    bad = {"problem_slug": "x", "drafted_at": "2026-05-25"}
    out = Syn.synthesize(
        problem_id=14,
        problem_slug="circle-packing-square",
        problem_context="ctx",
        source_hits=src,
        wiki_hits=wiki,
        runner=_ok_runner(bad),
    )
    assert out is None


def test_prompt_includes_problem_context_and_hits() -> None:
    """build_prompt is internal, but we exercise via runner inspection."""
    src, wiki = _sample_hits()
    captured: dict = {}

    def runner(**kwargs):
        captured.update(kwargs)
        # Return a valid minimal payload so synthesize() doesn't fail
        return _RunnerResult(
            ok=True,
            stdout=json.dumps(
                {
                    "problem_id": 14,
                    "problem_slug": "circle-packing-square",
                    "drafted_at": "2026-05-25",
                }
            ),
        )

    Syn.synthesize(
        problem_id=14,
        problem_slug="circle-packing-square",
        problem_context="My problem context here",
        source_hits=src,
        wiki_hits=wiki,
        runner=runner,
    )
    prompt = captured["prompt"]
    assert "My problem context here" in prompt
    assert "P14" in prompt
    assert "circle-packing-square" in prompt
    assert "filesystem-as-feedback" in prompt  # snippet from source hit
    assert "Chebyshev criterion" in prompt  # snippet from wiki hit
    # JSON schema passed through
    assert captured["output_format"] == "json"
    assert "problem_id" in captured["json_schema"]


def test_max_budget_passed_through_when_set() -> None:
    src, wiki = _sample_hits()
    captured: dict = {}

    def runner(**kwargs):
        captured.update(kwargs)
        return _RunnerResult(ok=False, error_kind="non-zero")

    Syn.synthesize(
        problem_id=1,
        problem_slug="erdos-overlap",
        problem_context="",
        source_hits=src,
        wiki_hits=wiki,
        runner=runner,
        max_budget_usd=0.50,
    )
    assert captured["max_budget_usd"] == 0.50


def test_max_budget_omitted_when_unset() -> None:
    src, wiki = _sample_hits()
    captured: dict = {}

    def runner(**kwargs):
        captured.update(kwargs)
        return _RunnerResult(ok=False, error_kind="non-zero")

    Syn.synthesize(
        problem_id=1,
        problem_slug="erdos-overlap",
        problem_context="",
        source_hits=src,
        wiki_hits=wiki,
        runner=runner,
    )
    assert "max_budget_usd" not in captured
