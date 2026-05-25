"""Tests for docs/tools/pdf_to_md.py — opendataloader-pdf wrapper.

The wrapper isolates the upstream import so tests can run without the
dep installed. The real Java backend is exercised by an opt-in
integration test (marked slow) gated on the tool being present.
"""
from __future__ import annotations

import shutil
import sys
import textwrap
from pathlib import Path
from unittest.mock import patch

import pytest

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "docs" / "tools"))

import pdf_to_md  # noqa: E402


# ---------------- helpers ----------------


def _stub_convert_factory(produced_md_text: str):
    """Return a fake `convert()` that writes a .md file shaped like the real backend."""
    def fake_convert(*, input_path, output_dir, format, hybrid=None, **_unused):
        # Real backend writes <output_dir>/<input_stem>/<input_stem>.md
        for p in input_path:
            stem = Path(p).stem
            sub = Path(output_dir) / stem
            sub.mkdir(parents=True, exist_ok=True)
            (sub / f"{stem}.md").write_text(produced_md_text)
    return fake_convert


# ---------------- tests: tool detection ----------------


def test_clean_error_when_backend_missing(tmp_path: Path) -> None:
    """If opendataloader_pdf import fails, raise BackendMissing with install hint."""
    pdf = tmp_path / "fake.pdf"
    pdf.write_bytes(b"%PDF-1.4 stub")

    with patch.object(pdf_to_md, "_load_backend", side_effect=pdf_to_md.BackendMissing(
        "opendataloader-pdf not installed. Run: uv add opendataloader-pdf")):
        with pytest.raises(pdf_to_md.BackendMissing, match="opendataloader-pdf"):
            pdf_to_md.convert_pdf(pdf, tmp_path / "out.md")


# ---------------- tests: convert one file ----------------


def test_convert_writes_md_to_target_path(tmp_path: Path) -> None:
    pdf = tmp_path / "paper.pdf"
    pdf.write_bytes(b"%PDF-1.4 stub")
    out_md = tmp_path / "out" / "paper.md"

    stub = _stub_convert_factory("# Paper\n\nbody with $x^2$ math.\n")
    with patch.object(pdf_to_md, "_load_backend", return_value=stub):
        result = pdf_to_md.convert_pdf(pdf, out_md)

    assert result == out_md
    assert out_md.is_file()
    assert "math" in out_md.read_text()
    # LaTeX preservation
    assert "$x^2$" in out_md.read_text()


def test_convert_refuses_to_overwrite_unless_flag(tmp_path: Path) -> None:
    pdf = tmp_path / "paper.pdf"
    pdf.write_bytes(b"%PDF-1.4 stub")
    out_md = tmp_path / "out.md"
    out_md.write_text("existing\n")

    stub = _stub_convert_factory("new\n")
    with patch.object(pdf_to_md, "_load_backend", return_value=stub):
        with pytest.raises(FileExistsError):
            pdf_to_md.convert_pdf(pdf, out_md)
        # With overwrite=True it should succeed
        pdf_to_md.convert_pdf(pdf, out_md, overwrite=True)
    assert out_md.read_text() == "new\n"


def test_convert_errors_on_missing_pdf(tmp_path: Path) -> None:
    pdf = tmp_path / "does-not-exist.pdf"
    out_md = tmp_path / "out.md"
    stub = _stub_convert_factory("body\n")
    with patch.object(pdf_to_md, "_load_backend", return_value=stub):
        with pytest.raises(FileNotFoundError):
            pdf_to_md.convert_pdf(pdf, out_md)


def test_convert_passes_hybrid_flag_through(tmp_path: Path) -> None:
    """`hybrid="docling-fast"` is what unlocks LaTeX-aware extraction."""
    pdf = tmp_path / "paper.pdf"
    pdf.write_bytes(b"%PDF-1.4 stub")
    out_md = tmp_path / "out.md"

    received: dict = {}

    def spy(*, input_path, output_dir, format, hybrid=None, **_unused):
        received["hybrid"] = hybrid
        received["format"] = format
        for p in input_path:
            stem = Path(p).stem
            sub = Path(output_dir) / stem
            sub.mkdir(parents=True, exist_ok=True)
            (sub / f"{stem}.md").write_text("ok\n")

    with patch.object(pdf_to_md, "_load_backend", return_value=spy):
        pdf_to_md.convert_pdf(pdf, out_md, hybrid="docling-fast")

    assert received["hybrid"] == "docling-fast"
    assert "markdown" in received["format"]


# ---------------- tests: batch ----------------


def test_convert_batch_amortizes_jvm(tmp_path: Path) -> None:
    """One backend invocation should produce N output files."""
    pdfs = []
    for i in range(3):
        p = tmp_path / f"paper-{i}.pdf"
        p.write_bytes(b"%PDF-1.4 stub")
        pdfs.append(p)
    out_dir = tmp_path / "out"

    call_count = {"n": 0}

    def stub(*, input_path, output_dir, format, hybrid=None, **_unused):
        call_count["n"] += 1
        for p in input_path:
            stem = Path(p).stem
            sub = Path(output_dir) / stem
            sub.mkdir(parents=True, exist_ok=True)
            (sub / f"{stem}.md").write_text(f"body for {stem}\n")

    with patch.object(pdf_to_md, "_load_backend", return_value=stub):
        results = pdf_to_md.convert_batch(pdfs, out_dir)

    assert call_count["n"] == 1, "batch must invoke backend once, not per-file"
    assert len(results) == 3
    for r in results:
        assert r.is_file()


def test_convert_batch_skips_existing_unless_overwrite(tmp_path: Path) -> None:
    pdfs = [tmp_path / "a.pdf", tmp_path / "b.pdf"]
    for p in pdfs:
        p.write_bytes(b"%PDF-1.4 stub")
    out_dir = tmp_path / "out"
    out_dir.mkdir()
    (out_dir / "a.md").write_text("preexisting\n")

    received_paths: list[list[str]] = []

    def stub(*, input_path, output_dir, format, hybrid=None, **_unused):
        received_paths.append([str(p) for p in input_path])
        for p in input_path:
            stem = Path(p).stem
            sub = Path(output_dir) / stem
            sub.mkdir(parents=True, exist_ok=True)
            (sub / f"{stem}.md").write_text("body\n")

    with patch.object(pdf_to_md, "_load_backend", return_value=stub):
        results = pdf_to_md.convert_batch(pdfs, out_dir)

    # Only b.pdf was sent to the backend; a.md was kept
    assert received_paths == [[str(pdfs[1])]]
    assert (out_dir / "a.md").read_text() == "preexisting\n"
    assert (out_dir / "b.md").is_file()
    assert len(results) == 2
