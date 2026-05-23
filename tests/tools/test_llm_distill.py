"""Tests for docs/tools/llm_distill.py — Claude Code-headless distillation."""
from __future__ import annotations

import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "docs" / "tools"))

import llm_distill as ld  # noqa: E402


SUMMARY = """# Distilled

## One-line
One sentence.

## Key claim
The claim.

## Method
The method.

## Result
The result.

## Why it matters here
It matters.

## Open questions / connections
- A connection.

## Key terms
a, b, c
"""


def test_build_prompt_includes_metadata_and_body() -> None:
    prompt = ld._build_prompt(
        extracted_md="### Abstract\nWe prove X.\n\n### Method\nWe use Y.",
        metadata={
            "title": "Paper Title",
            "authors": "A. Author, B. Author",
            "year": "2024",
            "source_url": "http://arxiv.org/abs/1.1",
        },
    )
    assert "Paper Title" in prompt
    assert "A. Author" in prompt
    assert "2024" in prompt
    assert "1.1" in prompt
    assert "We prove X" in prompt
    # Output schema must be in the prompt
    assert "One-line" in prompt
    assert "Key claim" in prompt
    assert "Why it matters" in prompt
    assert "Key terms" in prompt


def test_build_prompt_truncates_long_body() -> None:
    """A 200K char paper body should be truncated to fit in one claude -p invocation."""
    long_body = "blah " * 50000   # 250K chars
    prompt = ld._build_prompt(
        extracted_md=long_body,
        metadata={"title": "T", "authors": "A", "year": "2020",
                  "source_url": "http://x"},
    )
    # Should cap at the limit
    assert len(prompt) < 100_000


def test_distill_via_claude_code_runs_subprocess(tmp_path: Path) -> None:
    """Happy path: invoke claude -p, return stdout."""
    fake_result = MagicMock(returncode=0, stdout=SUMMARY, stderr="")
    with patch.object(ld.subprocess, "run", return_value=fake_result) as mock_run:
        result = ld.distill_via_claude_code(
            extracted_md="### Abstract\nshort",
            metadata={"title": "T", "authors": "A", "year": "2020",
                      "source_url": "http://x"},
            model="haiku",
        )
    assert result.startswith("# Distilled")
    # claude -p called with the right model
    args = mock_run.call_args[0][0]
    assert args[0] == "claude"
    assert "-p" in args
    assert "haiku" in args


def test_distill_via_claude_code_raises_on_nonzero_exit() -> None:
    fake_result = MagicMock(returncode=1, stdout="", stderr="error message")
    with patch.object(ld.subprocess, "run", return_value=fake_result):
        with pytest.raises(ld.DistillError, match="error message"):
            ld.distill_via_claude_code(
                extracted_md="x",
                metadata={"title": "T", "authors": "A", "year": "2020",
                          "source_url": "http://x"},
            )


def test_distill_strips_markdown_fence_if_present() -> None:
    """If claude returns ```markdown\n...\n```, the fences should be stripped."""
    fake_result = MagicMock(returncode=0,
                             stdout=f"```markdown\n{SUMMARY}\n```\n",
                             stderr="")
    with patch.object(ld.subprocess, "run", return_value=fake_result):
        result = ld.distill_via_claude_code(
            extracted_md="x",
            metadata={"title": "T", "authors": "A", "year": "2020",
                      "source_url": "http://x"},
    )
    assert "```" not in result
    assert result.startswith("# Distilled")


def test_distill_rejects_claude_session_limit_output() -> None:
    fake_result = MagicMock(
        returncode=0,
        stdout="You've hit your session limit · resets 5:20pm\n/usage-credits\n",
        stderr="",
    )
    with patch.object(ld.subprocess, "run", return_value=fake_result):
        with pytest.raises(ld.DistillError, match="Claude Code unavailable"):
            ld.distill_via_claude_code(
                extracted_md="x",
                metadata={"title": "T", "authors": "A", "year": "2020",
                          "source_url": "http://x"},
            )


def test_distill_rejects_malformed_output() -> None:
    fake_result = MagicMock(returncode=0, stdout="# not the schema\n", stderr="")
    with patch.object(ld.subprocess, "run", return_value=fake_result):
        with pytest.raises(ld.DistillError, match="missing required headings"):
            ld.distill_via_claude_code(
                extracted_md="x",
                metadata={"title": "T", "authors": "A", "year": "2020",
                          "source_url": "http://x"},
            )


def test_distill_batch_runs_concurrently(tmp_path: Path) -> None:
    """distill_batch processes N papers in parallel via ThreadPoolExecutor."""
    items = [
        {"slug": f"paper-{i}", "extracted_md": f"### Abstract\npaper {i}",
         "metadata": {"title": f"T{i}", "authors": "A", "year": "2020",
                       "source_url": f"http://x/{i}"}}
        for i in range(4)
    ]

    def fake_run(args, **kwargs):
        # Find slug encoded in the prompt
        prompt = args[-1] if isinstance(args[-1], str) else ""
        return MagicMock(returncode=0,
                          stdout=SUMMARY + f"\n<!-- {prompt[:50]} -->",
                          stderr="")

    with patch.object(ld.subprocess, "run", side_effect=fake_run):
        results = ld.distill_batch(items, model="haiku", max_workers=4)

    assert len(results) == 4
    for r in results:
        assert r["ok"] is True
        assert r["summary"].startswith("# Distilled")


def test_distill_batch_isolates_failures(tmp_path: Path) -> None:
    items = [
        {"slug": "ok", "extracted_md": "ok body",
         "metadata": {"title": "T", "authors": "A", "year": "2020",
                       "source_url": "http://x"}},
        {"slug": "fail", "extracted_md": "fail body",
         "metadata": {"title": "T", "authors": "A", "year": "2020",
                       "source_url": "http://x"}},
    ]

    def selective(args, **kwargs):
        prompt = args[-1] if isinstance(args[-1], str) else ""
        if "fail body" in prompt:
            return MagicMock(returncode=2, stdout="", stderr="boom")
        return MagicMock(returncode=0, stdout=SUMMARY, stderr="")

    with patch.object(ld.subprocess, "run", side_effect=selective):
        results = ld.distill_batch(items, model="haiku", max_workers=2)

    by_slug = {r["slug"]: r for r in results}
    assert by_slug["ok"]["ok"] is True
    assert by_slug["fail"]["ok"] is False
    assert "boom" in by_slug["fail"]["error"]
