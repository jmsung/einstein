"""Tests for Goal 4 — shadow wiring for code_edit proposals.

Covers:
- apply_proposal_to_worktree graduates `scripts/proposed/<slug>.py`
  to `scripts/<slug>.py` + adds stub manifest entries for cited problems.
- compute_arm_metrics with `tool_slug` counts B-arm cycles whose notes
  mention the tool.
- Dry-run: applied proposal → manifest entry visible, scripts/proposed/
  empty.
"""

from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein.meta_loop import shadow as ml_shadow  # noqa: E402
from einstein.meta_loop.code_edit import make_code_edit_proposal  # noqa: E402
from einstein.meta_loop.diagnose import CycleRow  # noqa: E402
from einstein.meta_loop.tool_gaps import ToolGap  # noqa: E402

UTC = dt.timezone.utc


def _gap(suggested: str = "mpmath-ulp-polish") -> ToolGap:
    return ToolGap(
        canonical=f"manifest_gap:{suggested}",
        pattern="manifest_gap",
        suggested_tool=suggested,
        missing_manifest_entry="newton_max",
        citing_cycles=[49, 50, 70],
        problem_ids=["P14", "P12"],
        open_questions=[],
    )


def _make_fake_runner():
    """Record git calls; return RunResult.ok=True for each. Acts like git."""
    calls = []

    def runner(args, cwd, stdin):
        calls.append({"args": list(args), "cwd": str(cwd) if cwd else None})
        return ml_shadow.RunResult(ok=True, stdout="ok", stderr="", returncode=0)

    return runner, calls


def _make_arm_spec(tmp_path: Path) -> ml_shadow.WorktreeSpec:
    arm_dir = tmp_path / "cb-shadow-test-B"
    arm_dir.mkdir(parents=True)
    return ml_shadow.WorktreeSpec(arm="B", path=arm_dir, branch="meta-shadow/test/B")


def _seed_manifest(arm_path: Path, problem_ids: list[int]) -> Path:
    """Write a minimal optimizer_manifest.yaml with the given problem blocks."""
    blocks = []
    for n in problem_ids:
        blocks.append(
            f"{n}:\n"
            f"  slug: problem-{n}\n"
            f"  default: existing_optimizer\n"
            f"  optimizers:\n"
            f"    existing_optimizer:\n"
            f"      script: scripts/problem_{n}/existing.py\n"
            f"      cli_args: []\n"
            f"      timeout_seconds: 60\n"
            f"      result_file: results/problem_{n}/existing_result.json\n"
            f"      result_parser: json_score_payload\n"
        )
    path = arm_path / "src" / "einstein" / "optimizer_manifest.yaml"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("# manifest\n\n" + "\n".join(blocks))
    return path


# ---------------- graduation ----------------


def test_apply_code_edit_graduates_to_scripts_root(tmp_path: Path) -> None:
    spec = _make_arm_spec(tmp_path)
    _seed_manifest(spec.path, [12, 14])
    proposal = make_code_edit_proposal(_gap(), now=dt.datetime(2026, 5, 31, tzinfo=UTC))
    runner, calls = _make_fake_runner()
    res = ml_shadow.apply_proposal_to_worktree(proposal, spec, runner=runner)
    assert res.ok, res.stderr
    # Graduated file exists at scripts/<slug>.py
    graduated = spec.path / "scripts" / "mpmath-ulp-polish.py"
    assert graduated.is_file()
    # scripts/proposed/ stays empty — the draft was graduated, not drafted
    proposed = spec.path / "scripts" / "proposed"
    assert not proposed.exists() or not any(proposed.iterdir())


def test_apply_code_edit_wires_manifest_for_cited_problems(tmp_path: Path) -> None:
    spec = _make_arm_spec(tmp_path)
    manifest_path = _seed_manifest(spec.path, [12, 14])
    proposal = make_code_edit_proposal(_gap(), now=dt.datetime(2026, 5, 31, tzinfo=UTC))
    runner, _ = _make_fake_runner()
    ml_shadow.apply_proposal_to_worktree(proposal, spec, runner=runner)
    manifest_body = manifest_path.read_text()
    # Stub entry appears under BOTH problem blocks
    assert "mpmath_ulp_polish:" in manifest_body
    # Verify it's nested under both 12: and 14:
    p12_block = manifest_body.split("\n12:\n", 1)[1].split("\n14:\n", 1)[0]
    p14_block = manifest_body.split("\n14:\n", 1)[1]
    assert "mpmath_ulp_polish:" in p12_block
    assert "mpmath_ulp_polish:" in p14_block
    assert "scripts/mpmath-ulp-polish.py" in manifest_body


def test_apply_code_edit_skips_uncited_problem(tmp_path: Path) -> None:
    spec = _make_arm_spec(tmp_path)
    # Cite only P14 + P12 (from _gap), seed manifest with an extra P9 block
    manifest_path = _seed_manifest(spec.path, [9, 12, 14])
    proposal = make_code_edit_proposal(_gap(), now=dt.datetime(2026, 5, 31, tzinfo=UTC))
    runner, _ = _make_fake_runner()
    ml_shadow.apply_proposal_to_worktree(proposal, spec, runner=runner)
    manifest_body = manifest_path.read_text()
    # P9 block should NOT have the stub entry
    p9_block = manifest_body.split("\n9:\n", 1)[1].split("\n12:\n", 1)[0]
    assert "mpmath_ulp_polish:" not in p9_block


def test_apply_code_edit_refuses_existing_scripts_target(tmp_path: Path) -> None:
    spec = _make_arm_spec(tmp_path)
    _seed_manifest(spec.path, [12, 14])
    (spec.path / "scripts").mkdir(parents=True)
    (spec.path / "scripts" / "mpmath-ulp-polish.py").write_text("# existing\n")
    proposal = make_code_edit_proposal(_gap(), now=dt.datetime(2026, 5, 31, tzinfo=UTC))
    runner, _ = _make_fake_runner()
    res = ml_shadow.apply_proposal_to_worktree(proposal, spec, runner=runner)
    assert not res.ok
    assert "already exists" in res.stderr


def test_apply_code_edit_no_manifest_still_succeeds(tmp_path: Path) -> None:
    """If the worktree has no manifest, write the script but skip wiring."""
    spec = _make_arm_spec(tmp_path)
    # No manifest seeded.
    proposal = make_code_edit_proposal(_gap(), now=dt.datetime(2026, 5, 31, tzinfo=UTC))
    runner, _ = _make_fake_runner()
    res = ml_shadow.apply_proposal_to_worktree(proposal, spec, runner=runner)
    assert res.ok
    graduated = spec.path / "scripts" / "mpmath-ulp-polish.py"
    assert graduated.is_file()


# ---------------- skill-library + techniques-page coupling (Goal 6+) ----------------


def _seed_skill_library(arm_path: Path) -> Path:
    """Write a minimal skill-library.md so the coupling step has a target."""
    path = arm_path / "docs" / "agent" / "skill-library.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "# Skill library\n\n"
        "| technique | category | tried | top3 | finding | last_used | hit_rate |\n"
        "|---|---|---|---|---|---|---|\n"
        "| `existing.md` | packing | 5 | 2 | 1 | 2026-04-12 | 0.40 |\n"
    )
    return path


def _seed_problem_category_map(arm_path: Path) -> Path:
    """Drop a strategy_picker.py with a minimal _PROBLEM_CATEGORY so the
    coupling step can look up categories. Keeps the test self-contained."""
    path = arm_path / "docs" / "tools" / "strategy_picker.py"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "# minimal strategy_picker stub for tests\n"
        "_PROBLEM_CATEGORY = {\n"
        "    1: 'functional-inequality',\n"
        "    9: 'functional-inequality',\n"
        "    12: 'discrete-combinatorics',\n"
        "    14: 'packing',\n"
        "}\n"
    )
    return path


def test_apply_code_edit_appends_skill_library_row(tmp_path: Path) -> None:
    spec = _make_arm_spec(tmp_path)
    _seed_manifest(spec.path, [12, 14])
    library = _seed_skill_library(spec.path)
    _seed_problem_category_map(spec.path)
    proposal = make_code_edit_proposal(_gap(), now=dt.datetime(2026, 5, 31, tzinfo=UTC))
    runner, _ = _make_fake_runner()
    res = ml_shadow.apply_proposal_to_worktree(proposal, spec, runner=runner)
    assert res.ok, res.stderr
    body = library.read_text()
    # New row with the slug + the cited problems' categories
    assert "`mpmath-ulp-polish.md`" in body
    # Categories joined with " / " — both packing (P14) and
    # discrete-combinatorics (P12) appear
    assert "packing" in body.splitlines()[-1]
    assert "discrete-combinatorics" in body.splitlines()[-1]
    # Counts seeded at 0
    assert "| 0 | 0 | 0 |" in body.splitlines()[-1]


def test_apply_code_edit_skill_library_idempotent(tmp_path: Path) -> None:
    spec = _make_arm_spec(tmp_path)
    _seed_manifest(spec.path, [12, 14])
    library = _seed_skill_library(spec.path)
    _seed_problem_category_map(spec.path)
    proposal = make_code_edit_proposal(_gap(), now=dt.datetime(2026, 5, 31, tzinfo=UTC))
    runner, _ = _make_fake_runner()
    ml_shadow.apply_proposal_to_worktree(proposal, spec, runner=runner)
    first = library.read_text()

    # Simulate reapply by removing the script (avoid the existing-script guard)
    (spec.path / "scripts" / "mpmath-ulp-polish.py").unlink()
    ml_shadow.apply_proposal_to_worktree(proposal, spec, runner=runner)
    second = library.read_text()

    assert first == second
    # Exactly one row for the slug
    assert second.count("`mpmath-ulp-polish.md`") == 1


def test_apply_code_edit_writes_techniques_page(tmp_path: Path) -> None:
    spec = _make_arm_spec(tmp_path)
    _seed_manifest(spec.path, [12, 14])
    _seed_skill_library(spec.path)
    _seed_problem_category_map(spec.path)
    proposal = make_code_edit_proposal(_gap(), now=dt.datetime(2026, 5, 31, tzinfo=UTC))
    runner, _ = _make_fake_runner()
    ml_shadow.apply_proposal_to_worktree(proposal, spec, runner=runner)
    page = spec.path / "knowledge" / "wiki" / "techniques" / "mpmath-ulp-polish.md"
    assert page.is_file()
    body = page.read_text()
    assert "type: technique" in body
    assert "autosynth-stub" in body
    # Cite block surfaces the canonical gap
    assert "manifest_gap:mpmath-ulp-polish" in body


def test_apply_code_edit_no_skill_library_still_succeeds(tmp_path: Path) -> None:
    """If the worktree has no skill-library, write the script + manifest stub
    but skip the coupling row. Mirrors `no_manifest_still_succeeds`."""
    spec = _make_arm_spec(tmp_path)
    _seed_manifest(spec.path, [12, 14])
    # No skill-library seeded.
    _seed_problem_category_map(spec.path)
    proposal = make_code_edit_proposal(_gap(), now=dt.datetime(2026, 5, 31, tzinfo=UTC))
    runner, _ = _make_fake_runner()
    res = ml_shadow.apply_proposal_to_worktree(proposal, spec, runner=runner)
    assert res.ok


def test_apply_code_edit_idempotent_on_manifest_reapply(tmp_path: Path) -> None:
    """Reapplying the same proposal must NOT duplicate the manifest entry."""
    spec = _make_arm_spec(tmp_path)
    manifest_path = _seed_manifest(spec.path, [12, 14])
    proposal = make_code_edit_proposal(_gap(), now=dt.datetime(2026, 5, 31, tzinfo=UTC))

    # First apply
    runner, _ = _make_fake_runner()
    ml_shadow.apply_proposal_to_worktree(proposal, spec, runner=runner)
    first = manifest_path.read_text()

    # Simulate a re-apply by removing the script (so the apply doesn't trip
    # the "already exists" guard) but leaving the manifest entries.
    (spec.path / "scripts" / "mpmath-ulp-polish.py").unlink()
    ml_shadow.apply_proposal_to_worktree(proposal, spec, runner=runner)
    second = manifest_path.read_text()

    # Manifest unchanged on second apply
    assert first == second
    # Each block has exactly one entry
    assert first.count("mpmath_ulp_polish:") == 2  # one per problem


# ---------------- compute_arm_metrics with tool_slug ----------------


def _row(cid: int, notes: str, *, score_changed: bool = False) -> CycleRow:
    return CycleRow(
        cycle_id=cid,
        problem="P14-circle-packing-square",
        score_field="2.6 → 2.7" if score_changed else "2.6 (no Δ)",
        hours="0",
        compute="local-cpu+llm",
        wiki_citations="0",
        findings_added="0",
        concepts_added="0",
        author_mix="a:1/h:0",
        outcome="converged",
        notes=notes,
    )


def test_compute_arm_metrics_no_slug_returns_zero_invocations() -> None:
    rows = [_row(1, "ran a cycle"), _row(2, "another cycle")]
    m = ml_shadow.compute_arm_metrics(rows)
    assert m.tool_invoked_cycles == 0


def test_compute_arm_metrics_counts_slug_matches_in_notes() -> None:
    rows = [
        _row(1, "llm-strategy=mpmath-ulp-polish; tokens=in:4185"),
        _row(2, "no tool of interest"),
        _row(3, "mpmath-ulp-polish reached float64 ceiling"),
    ]
    m = ml_shadow.compute_arm_metrics(rows, tool_slug="mpmath-ulp-polish")
    assert m.tool_invoked_cycles == 2


def test_compute_arm_metrics_case_insensitive_slug() -> None:
    rows = [_row(1, "MPMATH-ULP-POLISH was selected")]
    m = ml_shadow.compute_arm_metrics(rows, tool_slug="mpmath-ulp-polish")
    assert m.tool_invoked_cycles == 1


# ---------------- end-to-end dry-run via run_shadow + stubbed runners ----------------


def test_run_shadow_dispatches_tool_slug_for_code_edit(tmp_path: Path) -> None:
    """run_shadow extracts the slug from the proposal and counts invocations."""
    spec_parent = tmp_path / "worktrees"
    spec_parent.mkdir()
    repo_root = tmp_path / "repo"
    repo_root.mkdir()

    proposal = make_code_edit_proposal(_gap(), now=dt.datetime(2026, 5, 31, tzinfo=UTC))

    # Fake git runner — every git command "succeeds"
    git_runner, _ = _make_fake_runner()

    # Cycle runner: A produces 0 mentions of the slug; B produces 2 mentions.
    def cycle_runner(arm_path: Path, n: int) -> list[CycleRow]:
        if "A" in str(arm_path):
            return [
                _row(100, "ran without the tool"),
                _row(101, "did something else"),
            ]
        return [
            _row(200, "llm-strategy=mpmath-ulp-polish; tokens=in:1000"),
            _row(201, "mpmath-ulp-polish reached float64 ceiling — dead-end"),
        ]

    result = ml_shadow.run_shadow(
        proposal,
        repo_root=repo_root,
        n_cycles=2,
        worktree_parent=spec_parent,
        cycle_runner=cycle_runner,
        git_runner=git_runner,
        cleanup=False,  # fake worktrees — no real git, skip cleanup
        clock=lambda: dt.datetime(2026, 5, 31, 12, 0, 0, tzinfo=UTC),
    )
    assert result.error is None or "tool_invoked_cycles" not in (result.error or "")
    assert result.delta is not None
    assert result.delta.arm_a.tool_invoked_cycles == 0
    assert result.delta.arm_b.tool_invoked_cycles == 2
