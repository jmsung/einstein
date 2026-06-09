"""Tests for docs/tools/capture_gate.py (Phase 0 of js/feat/meta-learning-automation).

Covers the pure parsers (frontmatter, attribution, cite) and the end-to-end gate
against real throwaway git repos — the gate's contract is "what changed since base".
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "docs" / "tools"))

import capture_gate as cg  # noqa: E402

# --------------------------------------------------------------- unit: parsers


def test_parse_frontmatter_inline_and_block_lists() -> None:
    text = (
        "---\n"
        "type: finding\n"
        "author: agent\n"
        "related_problems: [2, 19]\n"
        "cites:\n"
        "  - docs/source/a.md\n"
        "  - docs/source/b.md\n"
        "---\n"
        "body\n"
    )
    meta = cg.parse_frontmatter(text)
    assert meta["type"] == "finding"
    assert meta["author"] == "agent"
    assert meta["related_problems"] == ["2", "19"]
    assert meta["cites"] == ["docs/source/a.md", "docs/source/b.md"]


def test_parse_frontmatter_none_when_absent() -> None:
    assert cg.parse_frontmatter("# just a heading\n") == {}


def test_valid_frontmatter_requires_type_and_known_author() -> None:
    assert cg.has_valid_frontmatter({"type": "finding", "author": "agent"})
    assert cg.has_valid_frontmatter({"type": "concept", "author": "Hybrid"})
    assert not cg.has_valid_frontmatter({"type": "finding"})  # no author
    assert not cg.has_valid_frontmatter({"author": "agent"})  # no type
    assert not cg.has_valid_frontmatter({"type": "f", "author": "bot"})  # bad author


def test_has_cite_variants() -> None:
    assert cg.has_cite({"cites": ["docs/source/a.md"]}, "")
    assert cg.has_cite({"related_concepts": ["x"]}, "")
    assert cg.has_cite({}, "see docs/source/foo.md for details")
    assert cg.has_cite({}, "https://arxiv.org/abs/1234.5678")
    assert not cg.has_cite({"cites": []}, "no references here at all")


# ----------------------------------------------------------- helpers: git repo


def _run(repo: Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True)


def _init_repo(tmp_path: Path) -> Path:
    repo = tmp_path / "r"
    repo.mkdir()
    _run(repo, "init", "-q")
    _run(repo, "config", "user.email", "t@t.t")
    _run(repo, "config", "user.name", "t")
    _run(repo, "checkout", "-q", "-b", "main")
    (repo / "docs" / "agent").mkdir(parents=True)
    (repo / "docs" / "wiki" / "findings").mkdir(parents=True)
    (repo / "docs" / "wiki" / "concepts").mkdir(parents=True)
    (repo / "docs" / "agent" / "cycle-log.md").write_text(
        "# Cycle log\n\n| # | problem | notes |\n|---|---|---|\n| 0 | seed | x |\n"
    )
    _run(repo, "add", "-A")
    _run(repo, "commit", "-q", "-m", "seed")
    _run(repo, "checkout", "-q", "-b", "work")
    return repo


def _good_finding() -> str:
    return (
        "---\ntype: finding\nauthor: agent\ncites:\n  - docs/source/x.md\n---\n"
        "# Dead end\nwhy it failed\n"
    )


# --------------------------------------------------------------- gate: e2e


def test_gate_fails_when_nothing_captured(tmp_path: Path) -> None:
    repo = _init_repo(tmp_path)
    passed, reasons = cg.check_capture(repo, "main")
    assert not passed
    assert any("cycle-log" in r for r in reasons)
    assert any("findings" in r for r in reasons)


def test_gate_fails_with_row_but_no_finding(tmp_path: Path) -> None:
    repo = _init_repo(tmp_path)
    log = repo / "docs" / "agent" / "cycle-log.md"
    log.write_text(log.read_text() + "| 1 | P2-x | a record |\n")
    passed, reasons = cg.check_capture(repo, "main")
    assert not passed
    assert any("findings" in r for r in reasons)
    assert not any("cycle-log" in r for r in reasons)  # row IS present


def test_gate_fails_with_finding_but_no_cite(tmp_path: Path) -> None:
    repo = _init_repo(tmp_path)
    log = repo / "docs" / "agent" / "cycle-log.md"
    log.write_text(log.read_text() + "| 1 | P2-x | a record |\n")
    (repo / "docs" / "wiki" / "findings" / "d.md").write_text(
        "---\ntype: finding\nauthor: agent\n---\nno citation in body\n"
    )
    passed, reasons = cg.check_capture(repo, "main")
    assert not passed
    assert any("cite" in r for r in reasons)


def test_gate_passes_with_row_and_cited_finding(tmp_path: Path) -> None:
    repo = _init_repo(tmp_path)
    log = repo / "docs" / "agent" / "cycle-log.md"
    log.write_text(log.read_text() + "| 1 | P2-x | a record |\n")
    (repo / "docs" / "wiki" / "findings" / "d.md").write_text(_good_finding())
    passed, reasons = cg.check_capture(repo, "main")
    assert passed, reasons


def test_gate_passes_with_concept_too(tmp_path: Path) -> None:
    repo = _init_repo(tmp_path)
    log = repo / "docs" / "agent" / "cycle-log.md"
    log.write_text(log.read_text() + "| 9 | P2-x | x |\n")
    (repo / "docs" / "wiki" / "concepts" / "c.md").write_text(
        "---\ntype: concept\nauthor: hybrid\ncites:\n  - docs/wiki/findings/d.md\n---\nbody\n"
    )
    passed, _ = cg.check_capture(repo, "main")
    assert passed


def test_readme_does_not_satisfy_capture(tmp_path: Path) -> None:
    repo = _init_repo(tmp_path)
    log = repo / "docs" / "agent" / "cycle-log.md"
    log.write_text(log.read_text() + "| 1 | P2-x | x |\n")
    (repo / "docs" / "wiki" / "findings" / "README.md").write_text(_good_finding())
    passed, reasons = cg.check_capture(repo, "main")
    assert not passed
    assert any("findings" in r for r in reasons)


def test_committed_changes_count(tmp_path: Path) -> None:
    """Capture committed on the branch (not just working tree) still satisfies."""
    repo = _init_repo(tmp_path)
    log = repo / "docs" / "agent" / "cycle-log.md"
    log.write_text(log.read_text() + "| 1 | P2-x | x |\n")
    (repo / "docs" / "wiki" / "findings" / "d.md").write_text(_good_finding())
    _run(repo, "add", "-A")
    _run(repo, "commit", "-q", "-m", "capture")
    passed, reasons = cg.check_capture(repo, "main")
    assert passed, reasons


def test_gate_passes_on_git_error(tmp_path: Path) -> None:
    """Un-evaluable (bad base ref) must pass — never trap on infra failure."""
    repo = _init_repo(tmp_path)
    passed, reasons = cg.check_capture(repo, "no-such-ref-xyz")
    assert passed
    assert any("cannot evaluate" in r for r in reasons)


def test_main_exit_codes(tmp_path: Path, capsys) -> None:
    repo = _init_repo(tmp_path)
    assert cg.main(["--repo", str(repo), "--base", "main"]) == 1
    assert "NOT SATISFIED" in capsys.readouterr().out
    log = repo / "docs" / "agent" / "cycle-log.md"
    log.write_text(log.read_text() + "| 1 | P2-x | x |\n")
    (repo / "docs" / "wiki" / "findings" / "d.md").write_text(_good_finding())
    assert cg.main(["--repo", str(repo), "--base", "main"]) == 0
    assert "OK" in capsys.readouterr().out
