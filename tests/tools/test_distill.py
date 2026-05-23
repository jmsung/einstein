"""Tests for docs/tools/distill_paper.py — structural distillation of
opendataloader-pdf output into a qmd-friendly summary."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "docs" / "tools"))

import distill_paper as dp  # noqa: E402


def _sample_extracted_md() -> str:
    return """# arXiv:2604.25850v4[cs.CL]18May2026

## Agentic Harness Engineering: Observability-Driven Automatic Evolution

##### Jiahang Lin, Shichun Liu, Chengjun Pan
1Fudan University

### Abstract
This is the abstract. It explains the problem and the contribution
in a couple of sentences. The system achieves 77.0% pass@1 on
Terminal-Bench 2.

### 1 Introduction
The introduction starts here. We motivate the work and explain the
intuition behind the approach.

Some more intro text. Multiple paragraphs.

### 2 Related Work
This section discusses prior work.

### 3 Method
Description of the method.

### 4 Experiments
Results tables would be here.

### 5 Conclusion
We conclude that the system works. Future work includes extending
the framework to more domains.

### References
[1] Some Paper
[2] Another Paper
"""


def test_extract_abstract() -> None:
    md = _sample_extracted_md()
    abstract = dp._extract_section(md, "abstract")
    assert "achieves 77.0%" in abstract
    # Should NOT include the next section
    assert "introduction" not in abstract.lower()


def test_extract_conclusion() -> None:
    md = _sample_extracted_md()
    conclusion = dp._extract_section(md, "conclusion")
    assert "system works" in conclusion
    assert "references" not in conclusion.lower()


def test_extract_introduction_snippet() -> None:
    md = _sample_extracted_md()
    intro = dp._extract_section(md, "introduction", max_chars=200)
    assert "motivate" in intro
    # Truncated
    assert len(intro) <= 200 + 20   # +small slack for word-boundary


def test_extract_missing_section_returns_empty() -> None:
    md = _sample_extracted_md()
    assert dp._extract_section(md, "future work") == ""


def test_distill_produces_curated_summary() -> None:
    md = _sample_extracted_md()
    metadata = {
        "title": "Agentic Harness Engineering",
        "authors": "Jiahang Lin, Shichun Liu, Chengjun Pan",
        "year": "2026",
        "source_url": "https://arxiv.org/abs/2604.25850",
    }
    summary = dp.distill(md, metadata)

    # Required structure
    assert "# Agentic Harness Engineering" in summary
    assert "Lin" in summary
    assert "2026" in summary
    assert "arxiv.org/abs/2604.25850" in summary
    # Sections we expect
    assert "## Abstract" in summary
    assert "## Conclusion" in summary
    # Should NOT include the references list
    assert "[1] Some Paper" not in summary
    # Significantly smaller than input
    assert len(summary) < len(md) * 0.7


def test_distill_falls_back_when_no_abstract(tmp_path: Path) -> None:
    """Even without an Abstract section, distill emits header + intro snippet."""
    md = "# Paper title\n\nSome body text without section markers."
    metadata = {"title": "X", "authors": "Y", "year": "2020",
                "source_url": "http://arxiv.org/abs/1.1"}
    summary = dp.distill(md, metadata)
    assert "# X" in summary
    # Falls back to a body excerpt
    assert "Some body text" in summary or "no abstract" in summary.lower()


def test_distill_omits_long_references() -> None:
    """A real-paper References section should never appear in the summary."""
    md = _sample_extracted_md() + "\n" + "ref content " * 1000
    metadata = {"title": "X", "authors": "Y", "year": "2020",
                "source_url": "http://arxiv.org/abs/1.1"}
    summary = dp.distill(md, metadata)
    # The 1000-rep ref content shouldn't bloat the summary
    assert "ref content ref content ref content" not in summary
    assert len(summary) < 3000


def test_distill_preserves_math_notation() -> None:
    """Inline LaTeX in the abstract should survive distillation."""
    md = """### Abstract
We prove the bound $\\kappa(11) \\leq 552$ using LP duality. The constant
is sharp up to lower-order terms.

### 1 Introduction
intro text
"""
    metadata = {"title": "X", "authors": "Y", "year": "2020",
                "source_url": "http://x"}
    summary = dp.distill(md, metadata)
    assert "$\\kappa(11)" in summary or r"$\kappa(11)" in summary
