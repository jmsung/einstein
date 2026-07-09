#!/usr/bin/env python3
"""tool_autosynthesis_shadow.py — Goal 4/6 CLI: shadow A/B for code_edit.

Mirrors `scripts/research_synthesis_shadow.py`. Wires together:

- `meta_loop.tool_gaps.detect_recurring_tool_gaps` — read the cycle-log
  and surface threshold-passing gaps.
- `meta_loop.code_edit.make_code_edit_proposal` — draft the proposal.
- `meta_loop.sandbox.validate_proposed_tool` — ruff + import + unit tests
  before the shadow runs.
- `meta_loop.shadow.run_shadow` — A (control) vs B (graduated tool) over
  N cycles per arm.

Usage::

    # Dry-run: detect the gap, draft the proposal, run validator, print
    # the plan. No worktrees, no inner cycles.
    uv run python scripts/tool_autosynthesis_shadow.py --dry-run

    # Real run (operator-initiated; heavy):
    uv run python scripts/tool_autosynthesis_shadow.py --n-cycles 10 --execute

The Goal 6 live A/B uses ``--execute`` on the P12 flat-polynomials
algebraic-construction gap.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import logging
import sys
from pathlib import Path

from einstein.meta_loop import shadow as ml_shadow
from einstein.meta_loop.code_edit import make_code_edit_proposal
from einstein.meta_loop.sandbox import validate_proposed_tool
from einstein.meta_loop.tool_gaps import detect_recurring_tool_gaps

log = logging.getLogger("tool_autosynthesis_shadow")

_REPO = Path(__file__).resolve().parents[1]
DEFAULT_MB = _REPO.parent / "mb"
DEFAULT_CYCLE_LOG = _REPO / "docs" / "agent" / "cycle-log.md"
DEFAULT_QUESTIONS_DIR = _REPO / "knowledge" / "wiki" / "questions"
DEFAULT_SHADOW_LOG = DEFAULT_MB / "logs" / "tool-autosynthesis-shadow.md"


def dry_run_summary(
    *,
    cycle_log: Path,
    questions_dir: Path,
    n_cycles: int,
) -> str:
    """Build the dry-run report: detected gap → proposal → validator plan."""
    gaps = detect_recurring_tool_gaps(cycle_log, questions_dir)
    lines = [
        "# tool_autosynthesis_shadow dry-run",
        "",
        f"_Generated: {_dt.datetime.now(_dt.timezone.utc).isoformat()}_",
        "",
        f"_cycle_log: {cycle_log}_",
        f"_questions_dir: {questions_dir}_",
        "",
        "## Detected gaps (threshold-passing)",
        "",
    ]
    if not gaps:
        lines += [
            "_No threshold-passing tool gaps detected. The cycle-log shows",
            "no recurring `not yet wired` / `manifest only exposes` / dispatch",
            "failure patterns across ≥3 cycles + ≥2 problems. Either the inner",
            "agent is already covering the available tools, or the gap-detector",
            "needs a richer set of markers — see `tool_gaps._extract_signal`.",
        ]
        return "\n".join(lines)
    for g in gaps:
        lines += [
            f"### `{g.canonical}`",
            "",
            f"- pattern: {g.pattern}",
            f"- suggested_tool: {g.suggested_tool}",
            f"- missing_manifest_entry: {g.missing_manifest_entry}",
            f"- cycle_count: {g.cycle_count}",
            f"- problem_count: {g.problem_count}",
            f"- citing_cycles: {g.citing_cycles}",
            f"- problem_ids: {sorted(set(g.problem_ids))}",
            f"- open_questions: {[str(q) for q in g.open_questions]}",
            "",
        ]
    # Build a proposal for the top gap as illustration.
    top = gaps[0]
    proposal = make_code_edit_proposal(top)
    lines += [
        "## Top proposal",
        "",
        f"- id: `{proposal.id}`",
        f"- type: `{proposal.type}`",
        f"- target_path: `{proposal.target_path}`",
        f"- requires_shadow: `{proposal.requires_shadow}`",
        f"- confidence: `{proposal.confidence}`",
        f"- evidence_cycles: `{proposal.evidence_cycles}`",
        f"- proposer_id: `{proposal.proposer_id}`",
        "",
        "## Shadow plan",
        "",
        f"- n_cycles per arm: {n_cycles}",
        "- arm A: treatment — graduate proposal (`scripts/<slug>.py` +",
        "         manifest entries under every cited problem id)",
        "- arm B: control (existing manifest, no proposed tool)",
        "",
        "## Validator (Goal 3) — runs before shadow",
        "",
        "- ruff check, import in subprocess, optional colocated pytest",
        "- never dispatches against a live problem",
        "- result serialized to `mb/proposals/pending/<id>/validation.json`",
        "",
        "## Promotion gate (Goal 5)",
        "",
        "A wins iff ALL of:",
        "  1. validator passed",
        "  2. tool_invoked_cycles_A ≥ 1   (citation-grounded)",
        "  3. findings produced in those A cycles",
        "  4. no regression vs control (A_findings ≥ B_findings)",
        "  5. human approval (mandatory — no auto-merge)",
        "",
        "## Operator instructions",
        "",
        "Re-run with `--execute` to fork two real worktrees and run cycles.",
        "Each cycle is an LLM call; budget ~$X per arm at N=10.",
        "",
    ]
    return "\n".join(lines)


def run_cli(
    *,
    cycle_log: Path = DEFAULT_CYCLE_LOG,
    questions_dir: Path = DEFAULT_QUESTIONS_DIR,
    n_cycles: int = 10,
    execute: bool = False,
    write_body: bool = False,
) -> int:
    """Run the CLI. Dry-run prints; execute mode runs the real shadow.

    `write_body=True` opts into the LLM body-writer (Goal 2/3): the draft
    arrives with a real body instead of the NotImplementedError stub, and the
    validator adds the smoke-dispatch step that fails a stub-that-slipped-
    through before it reaches shadow.
    """
    if not execute:
        print(dry_run_summary(cycle_log=cycle_log, questions_dir=questions_dir, n_cycles=n_cycles))
        return 0

    gaps = detect_recurring_tool_gaps(cycle_log, questions_dir)
    if not gaps:
        log.error("no threshold-passing gaps — refusing to execute shadow")
        return 1
    top = gaps[0]
    proposal = make_code_edit_proposal(
        top, write_body=write_body, repo_root=_REPO if write_body else None
    )
    log.info(
        "drafted proposal id=%s for gap %s (proposer=%s)",
        proposal.id,
        top.canonical,
        proposal.proposer_id,
    )

    # Validator pre-check on the draft body (write to a temp path).
    import tempfile

    with tempfile.TemporaryDirectory(prefix="autosynth-validate-") as tmp:
        target = Path(tmp) / "scripts" / "proposed" / Path(proposal.target_path).name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(proposal.proposed_diff)
        report = validate_proposed_tool(target, repo_root=Path(tmp), smoke_dispatch=write_body)
        log.info("validator: passed=%s steps=%s", report.passed, [s.name for s in report.steps])
        if not report.passed:
            audit = DEFAULT_MB / "proposals" / "pending" / proposal.id / "validation.json"
            report.write_json(audit)
            log.error("validator FAILED — wrote %s; not running shadow", audit)
            return 2

    # Shadow A/B
    result = ml_shadow.run_shadow(
        proposal,
        repo_root=_REPO,
        n_cycles=n_cycles,
        cycle_runner=ml_shadow.default_cycle_runner,
        shadow_log=DEFAULT_SHADOW_LOG,
    )
    log.info("shadow result: error=%s a_wins=%s", result.error, result.a_wins)
    print(
        json.dumps(
            {
                "proposal_id": result.proposal_id,
                "error": result.error,
                "a_wins": result.a_wins,
                "delta": (
                    {
                        "arm_a_tool_invoked": result.delta.arm_a.tool_invoked_cycles,
                        "arm_b_tool_invoked": result.delta.arm_b.tool_invoked_cycles,
                        "findings_delta": result.delta.findings_delta,
                    }
                    if result.delta
                    else None
                ),
            },
            indent=2,
        )
    )
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Shadow A/B for tool autosynthesis (code_edit).")
    parser.add_argument("--cycle-log", type=Path, default=DEFAULT_CYCLE_LOG)
    parser.add_argument("--questions-dir", type=Path, default=DEFAULT_QUESTIONS_DIR)
    parser.add_argument("--n-cycles", type=int, default=10)
    parser.add_argument(
        "--execute", action="store_true", help="actually fork worktrees + run cycles (heavy)"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="default mode — print the plan without execution"
    )
    parser.add_argument(
        "--write-body",
        action="store_true",
        help="opt into the LLM body-writer (Goal 2/3): draft a real body + smoke-dispatch validate",
    )
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    return run_cli(
        cycle_log=args.cycle_log,
        questions_dir=args.questions_dir,
        n_cycles=args.n_cycles,
        execute=args.execute,
        write_body=args.write_body,
    )


if __name__ == "__main__":
    sys.exit(main())
