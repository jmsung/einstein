"""Tests for src/einstein/meta_loop/code_edit_context.py — Goal 1 extractor."""

from __future__ import annotations

import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein.meta_loop.code_edit_context import (  # noqa: E402
    MAX_SCRIPT_CHARS,
    gather_context,
)
from einstein.meta_loop.tool_gaps import ToolGap  # noqa: E402


def _gap(
    *,
    suggested: str | None = "mpmath-ulp-polish",
    problems: list[str] | None = None,
    questions: list[Path] | None = None,
) -> ToolGap:
    return ToolGap(
        canonical=f"manifest_gap:{suggested}" if suggested else "manifest_or_dispatch_gap",
        pattern="manifest_gap",
        suggested_tool=suggested,
        missing_manifest_entry=None,
        citing_cycles=[49, 50, 70],
        problem_ids=problems or ["P14", "P11"],
        open_questions=questions or [],
    )


def _write_manifest(root: Path) -> Path:
    """Minimal two-problem manifest with one problem-subdir script each."""
    (root / "scripts" / "circle_packing_square").mkdir(parents=True)
    (root / "scripts" / "tammes").mkdir(parents=True)
    (root / "scripts" / "circle_packing_square" / "slsqp_polish.py").write_text(
        "def slsqp_polish():\n    return 1.0  # rank-current P14 body\n"
    )
    (root / "scripts" / "tammes" / "optimize.py").write_text(
        "def optimize():\n    return 2.0  # rank-current P11 body\n"
    )
    # A shared top-level script that must be SKIPPED (not a technique exemplar).
    (root / "scripts" / "verify_seed.py").write_text("def verify_seed():\n    pass\n")
    manifest = root / "manifest.yaml"
    manifest.write_text(
        "14:\n"
        "  slug: circle-packing-square\n"
        "  optimizers:\n"
        "    slsqp_polish:\n"
        "      script: scripts/circle_packing_square/slsqp_polish.py\n"
        "    verify:\n"
        "      script: scripts/verify_seed.py\n"
        "11:\n"
        "  slug: tammes-n50\n"
        "  optimizers:\n"
        "    optimize:\n"
        "      script: scripts/tammes/optimize.py\n"
    )
    return manifest


def test_gather_collects_problem_subdir_scripts(tmp_path: Path) -> None:
    manifest = _write_manifest(tmp_path)
    ctx = gather_context(_gap(), repo_root=tmp_path, manifest_path=manifest)
    paths = {e.path for e in ctx.example_scripts}
    assert "scripts/circle_packing_square/slsqp_polish.py" in paths
    assert "scripts/tammes/optimize.py" in paths


def test_gather_skips_shared_toplevel_scripts(tmp_path: Path) -> None:
    """`scripts/verify_seed.py` is shared harness, not a technique exemplar."""
    manifest = _write_manifest(tmp_path)
    ctx = gather_context(_gap(), repo_root=tmp_path, manifest_path=manifest)
    assert all("verify_seed" not in e.path for e in ctx.example_scripts)


def test_gather_skips_own_suggested_tool(tmp_path: Path) -> None:
    """The body-writer shouldn't be fed a stub of the tool it's writing."""
    manifest = _write_manifest(tmp_path)
    # Add a mpmath_ulp_polish stub under P14 — must be excluded.
    (tmp_path / "scripts" / "circle_packing_square" / "mpmath_ulp_polish.py").write_text(
        "def mpmath_ulp_polish():\n    raise NotImplementedError\n"
    )
    manifest.write_text(
        manifest.read_text().replace(
            "    verify:\n      script: scripts/verify_seed.py\n",
            "    mpmath_ulp_polish:\n"
            "      script: scripts/circle_packing_square/mpmath_ulp_polish.py\n",
        )
    )
    ctx = gather_context(
        _gap(suggested="mpmath-ulp-polish"), repo_root=tmp_path, manifest_path=manifest
    )
    assert all("mpmath_ulp_polish" not in e.path for e in ctx.example_scripts)


def test_gather_reads_technique_page(tmp_path: Path) -> None:
    manifest = _write_manifest(tmp_path)
    tdir = tmp_path / "knowledge" / "wiki" / "techniques"
    tdir.mkdir(parents=True)
    (tdir / "mpmath-ulp-polish.md").write_text("# mpmath ulp polish\n\nULP-step descent.\n")
    ctx = gather_context(
        _gap(suggested="mpmath-ulp-polish"), repo_root=tmp_path, manifest_path=manifest
    )
    assert ctx.technique_page_path == "knowledge/wiki/techniques/mpmath-ulp-polish.md"
    assert "ULP-step descent" in (ctx.technique_page or "")


def test_gather_reads_open_questions(tmp_path: Path) -> None:
    manifest = _write_manifest(tmp_path)
    qdir = tmp_path / "knowledge" / "wiki" / "questions"
    qdir.mkdir(parents=True)
    qpath = qdir / "2026-05-31-p14-x.md"
    qpath.write_text("---\nstatus: open\n---\n\nWhat is the float64 ceiling for P14?\n")
    ctx = gather_context(
        _gap(questions=[Path("knowledge/wiki/questions/2026-05-31-p14-x.md")]),
        repo_root=tmp_path,
        manifest_path=manifest,
    )
    assert len(ctx.open_questions) == 1
    assert "float64 ceiling" in ctx.open_questions[0][1]


def test_render_prompt_context_includes_all_sections(tmp_path: Path) -> None:
    manifest = _write_manifest(tmp_path)
    tdir = tmp_path / "knowledge" / "wiki" / "techniques"
    tdir.mkdir(parents=True)
    (tdir / "mpmath-ulp-polish.md").write_text("# mpmath ulp polish\n")
    ctx = gather_context(_gap(), repo_root=tmp_path, manifest_path=manifest)
    rendered = ctx.render_prompt_context()
    assert "Rank-current optimizer bodies" in rendered
    assert "slsqp_polish" in rendered
    assert "target function name: `mpmath_ulp_polish`" in rendered
    assert "Technique page" in rendered


def test_gather_truncates_long_script(tmp_path: Path) -> None:
    (tmp_path / "scripts" / "big").mkdir(parents=True)
    big = "x = 1\n" * 5000  # well over MAX_SCRIPT_CHARS
    (tmp_path / "scripts" / "big" / "huge.py").write_text(big)
    manifest = tmp_path / "m.yaml"
    manifest.write_text("14:\n  optimizers:\n    huge:\n      script: scripts/big/huge.py\n")
    ctx = gather_context(_gap(problems=["P14"]), repo_root=tmp_path, manifest_path=manifest)
    assert len(ctx.example_scripts) == 1
    src = ctx.example_scripts[0].source
    assert len(src) <= MAX_SCRIPT_CHARS + 100  # truncation marker overhead
    assert "truncated" in src


def test_gather_empty_when_no_manifest_match(tmp_path: Path) -> None:
    manifest = tmp_path / "m.yaml"
    manifest.write_text("99:\n  optimizers: {}\n")
    ctx = gather_context(_gap(problems=["P14"]), repo_root=tmp_path, manifest_path=manifest)
    assert ctx.example_scripts == []
    # Render still works with the "(none wired)" branch.
    assert "none wired" in ctx.render_prompt_context()
