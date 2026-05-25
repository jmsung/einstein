#!/usr/bin/env python3
"""pdf_to_md.py — wrap opendataloader-pdf for math-aware ingestion.

Why this exists: /wiki-ingest's default PDF→md path reads the PDF
directly with an LLM, which loses inline LaTeX in math-heavy papers.
opendataloader-pdf (Java backend, hybrid Docling mode) is the
benchmark leader for table + formula extraction.

This module is a thin wrapper:
  - hides the JVM-per-call cost behind `convert_batch()` (single
    backend invocation produces N output files)
  - normalizes the backend's `<out_dir>/<stem>/<stem>.md` layout to
    `<out_dir>/<stem>.md`
  - isolates the import so tests + downstream code can mock it
    without requiring the package + Java 11 installed

Install:
    uv add opendataloader-pdf       # add to project deps
    # requires Java 11+ on PATH

Usage:
    uv run python docs/tools/pdf_to_md.py paper.pdf --out paper.md
    uv run python docs/tools/pdf_to_md.py docs/raw/papers/*.pdf --out-dir docs/source-md/
"""
from __future__ import annotations

import argparse
import logging
import shutil
import sys
import tempfile
from pathlib import Path

log = logging.getLogger("pdf_to_md")

DEFAULT_FORMAT = "markdown"
DEFAULT_HYBRID = "docling-fast"  # unlocks LaTeX formula extraction; None = deterministic only


class BackendMissing(RuntimeError):
    """Raised when `opendataloader_pdf` is not importable."""


def _load_backend():
    """Return the upstream `convert` callable, or raise BackendMissing.

    Indirection point so tests can patch this without installing Java.
    """
    try:
        import opendataloader_pdf  # type: ignore[import-not-found]
    except ImportError as e:  # pragma: no cover — exercised via mock
        raise BackendMissing(
            "opendataloader-pdf not installed.\n"
            "Install with: uv add opendataloader-pdf\n"
            "Also requires Java 11+ on PATH.\n"
            f"(import error: {e})"
        ) from e
    return opendataloader_pdf.convert


# ---------------- core API ----------------


def convert_pdf(
    pdf: Path,
    out_md: Path,
    *,
    hybrid: str | None = DEFAULT_HYBRID,
    overwrite: bool = False,
) -> Path:
    """Convert one PDF to a single .md file. Returns out_md.

    Internally a one-element batch; use `convert_batch` directly for
    multiple PDFs to share one JVM startup.
    """
    pdf = Path(pdf)
    out_md = Path(out_md)
    if not pdf.is_file():
        raise FileNotFoundError(f"PDF not found: {pdf}")
    if out_md.exists() and not overwrite:
        raise FileExistsError(
            f"refusing to overwrite {out_md} (pass overwrite=True or remove first)"
        )

    out_md.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        tmp_dir = Path(tmp)
        convert = _load_backend()
        convert(
            input_path=[str(pdf)],
            output_dir=str(tmp_dir),
            format=DEFAULT_FORMAT,
            hybrid=hybrid,
        )
        produced = _find_produced_md(tmp_dir, pdf.stem)
        if produced is None:
            raise RuntimeError(
                f"opendataloader-pdf did not produce a .md for {pdf} "
                f"in {tmp_dir} (contents: {list(tmp_dir.rglob('*'))})"
            )
        if out_md.exists():
            out_md.unlink()
        shutil.move(str(produced), out_md)
    return out_md


def convert_batch(
    pdfs: list[Path],
    out_dir: Path,
    *,
    hybrid: str | None = DEFAULT_HYBRID,
    overwrite: bool = False,
) -> list[Path]:
    """Convert N PDFs to <out_dir>/<stem>.md, single backend call.

    Skips PDFs whose target already exists unless overwrite=True. Returns
    the list of target paths (including pre-existing ones).
    """
    pdfs = [Path(p) for p in pdfs]
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    targets: list[Path] = []
    to_process: list[Path] = []
    for p in pdfs:
        if not p.is_file():
            raise FileNotFoundError(f"PDF not found: {p}")
        target = out_dir / f"{p.stem}.md"
        targets.append(target)
        if target.exists() and not overwrite:
            log.info("skip %s — %s exists", p.name, target.name)
            continue
        to_process.append(p)

    if not to_process:
        return targets

    with tempfile.TemporaryDirectory() as tmp:
        tmp_dir = Path(tmp)
        convert = _load_backend()
        convert(
            input_path=[str(p) for p in to_process],
            output_dir=str(tmp_dir),
            format=DEFAULT_FORMAT,
            hybrid=hybrid,
        )
        for p in to_process:
            target = out_dir / f"{p.stem}.md"
            produced = _find_produced_md(tmp_dir, p.stem)
            if produced is None:
                raise RuntimeError(
                    f"opendataloader-pdf did not produce a .md for {p}"
                )
            if target.exists():
                target.unlink()
            shutil.move(str(produced), target)

    return targets


def _find_produced_md(tmp_dir: Path, stem: str) -> Path | None:
    """Locate the backend's output. Default layout: tmp/<stem>/<stem>.md.

    Some backend versions / modes may flatten — fall back to a glob.
    """
    candidate = tmp_dir / stem / f"{stem}.md"
    if candidate.is_file():
        return candidate
    matches = list(tmp_dir.rglob(f"{stem}.md"))
    return matches[0] if matches else None


# ---------------- CLI ----------------


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("pdf", nargs="+", type=Path, help="PDF file(s) to convert.")
    out_group = parser.add_mutually_exclusive_group(required=True)
    out_group.add_argument("--out", type=Path, help="Single-output .md path (one PDF only).")
    out_group.add_argument("--out-dir", type=Path, help="Batch output directory.")
    parser.add_argument(
        "--hybrid", default=DEFAULT_HYBRID,
        help=f"Hybrid mode for the backend (default {DEFAULT_HYBRID!r}). "
             "Pass '' / 'none' to force deterministic-only.",
    )
    parser.add_argument(
        "--overwrite", action="store_true",
        help="Overwrite existing .md outputs.",
    )
    args = parser.parse_args(argv)

    hybrid: str | None = args.hybrid
    if hybrid in ("", "none", "None"):
        hybrid = None

    try:
        if args.out:
            if len(args.pdf) != 1:
                parser.error("--out takes exactly one PDF; use --out-dir for batch")
            convert_pdf(args.pdf[0], args.out, hybrid=hybrid, overwrite=args.overwrite)
            log.info("wrote %s", args.out)
        else:
            results = convert_batch(args.pdf, args.out_dir, hybrid=hybrid, overwrite=args.overwrite)
            log.info("wrote %d files to %s", len(results), args.out_dir)
    except BackendMissing as e:
        log.error("%s", e)
        return 2
    except (FileNotFoundError, FileExistsError) as e:
        log.error("%s", e)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
