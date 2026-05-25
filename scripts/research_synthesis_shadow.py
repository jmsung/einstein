#!/usr/bin/env python3
"""research_synthesis_shadow.py — Goal 6 CLI: shadow A/B for the synthesis step.

First consumer of `src/einstein/meta_loop/shadow.run_shadow()`. Wires:

- the `rule_edit` Proposal that toggles pre-cycle synthesis on
  (`make_synthesis_proposal()`),
- meta_loop's existing `setup_worktree` + `apply_proposal_to_worktree`
  + `compute_arm_metrics` + `append_shadow_log`,
- the citation-grounded promotion decision
  (`synthesis_promotion_decision`).

Usage::

    # Dry-run: construct the proposal + decision logic; no worktrees, no cycles.
    uv run python scripts/research_synthesis_shadow.py --dry-run

    # Real run (operator-initiated; heavy — runs N cycles per arm via
    # autonomous_loop.py): see README.
    uv run python scripts/research_synthesis_shadow.py --n-cycles 10 --execute

Per the G6 plan in `mb/active/js-feat-research-synthesis.md`:
  10 cycles × 2 arms on a fixed P1 / P9 / P14 / P19 subset (the four
  frozen/mediocre problems). Promotion: A wins iff findings_delta ≥ 0
  AND ≥1 citation-grounded cycle in arm A AND human signs off.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import logging
import sys
from pathlib import Path

from einstein.meta_loop import shadow as ml_shadow
from einstein.research_synthesis.shadow import (
    cycles_with_citations,
    make_synthesis_proposal,
    synthesis_promotion_decision,
)

log = logging.getLogger("research_synthesis_shadow")

_REPO = Path(__file__).resolve().parents[1]
DEFAULT_MB = _REPO.parent / "mb"
DEFAULT_SHADOW_LOG = DEFAULT_MB / "logs" / "research-synthesis-shadow.md"


def dry_run_summary(proposal_id: str, n_cycles: int, evidence_cycles: list[int]) -> str:
    """Return the dry-run report: what would happen, no side effects."""
    p = make_synthesis_proposal(proposal_id=proposal_id, evidence_cycles=evidence_cycles)
    lines = [
        "# research_synthesis_shadow dry-run",
        "",
        f"_Generated: {_dt.datetime.now(_dt.timezone.utc).isoformat()}_",
        "",
        "## Proposal",
        "",
        f"- id: `{p.id}`",
        f"- type: `{p.type}`",
        f"- target_path: `{p.target_path}`",
        f"- requires_shadow: `{p.requires_shadow}`",
        f"- confidence: `{p.confidence}`",
        f"- evidence_cycles: `{p.evidence_cycles}`",
        f"- predicted_regressions: `{p.predicted_regressions}`",
        "",
        "## Shadow plan",
        "",
        f"- n_cycles per arm: {n_cycles}",
        "- arm A: this proposal applied (pre-cycle synthesis on)",
        "- arm B: control (pre-cycle synthesis off)",
        "",
        "## Promotion gate (synthesis_promotion_decision)",
        "",
        "A wins iff ALL of:",
        "  1. findings_delta >= 0   (A authored ≥ B's per-cycle findings)",
        "  2. score_changed_delta >= 0   (A didn't regress on score moves)",
        "  3. cycles_with_citations_a >= 1   (citation-grounded improvement required)",
        "",
        "If any gate fails: decision = no-promote; human reviews the meta-shadow row.",
        "",
        "## Operator instructions",
        "",
        "Re-run with `--execute` to actually fork two worktrees and run cycles.",
        "Real run is heavy (each cycle is an LLM call). Default cycle_runner",
        "shells out to `scripts/autonomous_loop.py`; override with",
        "`--cycle-runner-stub` to substitute a no-op runner for smoke tests.",
        "",
    ]
    return "\n".join(lines)


def run_cli(
    *,
    n_cycles: int = 10,
    proposal_id: str = "rs-shadow-enable-synthesis",
    evidence_cycles: list[int] | None = None,
    dry_run: bool = True,
    execute: bool = False,
    shadow_log: Path = DEFAULT_SHADOW_LOG,
    out_stream=sys.stdout,
    cycle_runner=None,  # for tests + stubs
) -> int:
    """Pure-Python entry point with injectable cycle_runner."""
    evidence = evidence_cycles or []
    if dry_run or not execute:
        print(dry_run_summary(proposal_id, n_cycles, evidence), file=out_stream)
        return 0

    # --execute path: construct the proposal, invoke meta_loop.shadow.run_shadow.
    proposal = make_synthesis_proposal(proposal_id=proposal_id, evidence_cycles=evidence)
    if cycle_runner is None:
        cycle_runner = ml_shadow.default_cycle_runner
    repo_root = _REPO
    print(f"running shadow for proposal {proposal.id} with n_cycles={n_cycles}", file=out_stream)
    result = ml_shadow.run_shadow(
        proposal,
        repo_root=repo_root,
        n_cycles=n_cycles,
        cycle_runner=cycle_runner,
        shadow_log=shadow_log,
        cleanup=True,
    )
    if result.error:
        print(f"shadow error: {result.error}", file=out_stream)
        return 1
    delta = result.delta
    if delta is None:
        print(
            "shadow produced no delta (cycle_runner returned no rows in either arm)",
            file=out_stream,
        )
        return 1
    # Citation-grounded decision: re-compute over each arm's cycle-log.
    # Arms live at worktree_parent / cb-shadow-<id>-{A,B}; we passed default
    # (repo_root.parent). Use the same path convention to read the arm logs.
    arm_a_log = repo_root.parent / f"cb-shadow-{proposal.id}-A" / "docs" / "agent" / "cycle-log.md"
    arm_b_log = repo_root.parent / f"cb-shadow-{proposal.id}-B" / "docs" / "agent" / "cycle-log.md"
    cwc_a = cycles_with_citations(arm_a_log)
    cwc_b = cycles_with_citations(arm_b_log)
    decision = synthesis_promotion_decision(
        findings_delta=delta.findings_delta,
        score_changed_delta=delta.score_changed_delta,
        cycles_with_citations_a=cwc_a,
        cycles_with_citations_b=cwc_b,
    )
    print(f"meta_loop.shadow a_wins (heuristic): {result.a_wins}", file=out_stream)
    print(f"synthesis_promotion_decision: {decision.reason}", file=out_stream)
    print(f"shadow log row appended to {shadow_log}", file=out_stream)
    return 0 if decision.a_wins else 2


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0] if __doc__ else None)
    p.add_argument("--n-cycles", type=int, default=10)
    p.add_argument("--proposal-id", default="rs-shadow-enable-synthesis")
    p.add_argument(
        "--evidence-cycles",
        type=lambda s: [int(x) for x in s.split(",") if x.strip()],
        default=[],
        help="comma-separated cycle ids supporting the proposal (informational)",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="print proposal + plan; do not fork worktrees or run cycles (default)",
    )
    p.add_argument(
        "--execute",
        action="store_true",
        help=(
            "actually fork worktrees + run cycles. Heavy — each cycle is an "
            "LLM call. Operator must approve."
        ),
    )
    p.add_argument("--shadow-log", type=Path, default=DEFAULT_SHADOW_LOG)
    p.add_argument("-v", "--verbose", action="store_true")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO)
    return run_cli(
        n_cycles=args.n_cycles,
        proposal_id=args.proposal_id,
        evidence_cycles=args.evidence_cycles,
        dry_run=args.dry_run or not args.execute,
        execute=args.execute,
        shadow_log=args.shadow_log,
    )


if __name__ == "__main__":
    raise SystemExit(main())
