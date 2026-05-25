#!/usr/bin/env python3
"""meta_loop — outer loop over cycle outcomes; gated proposals to the inner loop.

Subcommands (filled in across Goals 1–5 on `js/feat/meta-loop`):

  diagnose   read-only: parse cycle-log + skill-library + findings/questions,
             write a structured report to mb/logs/meta-loop-report.md.

Future subcommands (stubbed below; raise NotImplementedError):

  propose    agentic proposer that reads the diagnostic + raw filesystem and
             emits typed proposals to mb/proposals/pending/ (Goal 2).
  review     human-review CLI: list pending proposals as diffs; accept/reject (Goal 4).
  shadow     fork two worktrees on accept; run N inner cycles each arm; Δ metrics (Goal 5).

The CLI is deliberately thin — logic lives in `src/einstein/meta_loop/`.
"""

from __future__ import annotations

import argparse
import datetime as dt
import sys
from pathlib import Path

# Repo layout: scripts/ sits at cb root; src/ is its sibling
_REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO / "src"))

from einstein.meta_loop import diagnose, propose, review  # noqa: E402
from einstein.meta_loop.proposals import ProposalStore  # noqa: E402

# When running from a worktree (cb-<branch>/), `.mb` is a symlink to ../mb.
# `_REPO/.mb` resolves to the shared private workspace either way.
_DEFAULT_MB = _REPO / ".mb"


def _add_diagnose(sub: argparse._SubParsersAction) -> None:
    p = sub.add_parser(
        "diagnose",
        help="parse cycle-log + skill-library + findings; write structured report",
    )
    p.add_argument(
        "--cycle-log",
        type=Path,
        default=_REPO / "docs" / "agent" / "cycle-log.md",
        help="path to docs/agent/cycle-log.md",
    )
    p.add_argument(
        "--skill-library",
        type=Path,
        default=_REPO / "docs" / "agent" / "skill-library.md",
        help="path to docs/agent/skill-library.md",
    )
    p.add_argument(
        "--findings-dir",
        type=Path,
        default=_REPO / "docs" / "wiki" / "findings",
        help="path to docs/wiki/findings/",
    )
    p.add_argument(
        "--questions-dir",
        type=Path,
        default=_REPO / "docs" / "wiki" / "questions",
        help="path to docs/wiki/questions/",
    )
    p.add_argument(
        "--output",
        type=Path,
        default=_DEFAULT_MB / "logs" / "meta-loop-report.md",
        help="path for the structured report",
    )


def _add_propose(sub: argparse._SubParsersAction) -> None:
    p = sub.add_parser(
        "propose",
        help="invoke LLM proposer; write typed proposals to mb/proposals/pending/",
    )
    p.add_argument("--cycle-log", type=Path, default=_REPO / "docs" / "agent" / "cycle-log.md")
    p.add_argument(
        "--skill-library", type=Path, default=_REPO / "docs" / "agent" / "skill-library.md"
    )
    p.add_argument("--findings-dir", type=Path, default=_REPO / "docs" / "wiki" / "findings")
    p.add_argument("--questions-dir", type=Path, default=_REPO / "docs" / "wiki" / "questions")
    p.add_argument("--mb-logs-dir", type=Path, default=_DEFAULT_MB / "logs")
    p.add_argument("--proposals-root", type=Path, default=_DEFAULT_MB / "proposals")
    p.add_argument(
        "--output",
        type=Path,
        default=_DEFAULT_MB / "logs" / "meta-loop-report.md",
        help="diagnostic report destination (run() refreshes it)",
    )


def _cmd_propose(args: argparse.Namespace) -> int:
    result = propose.run(
        cycle_log=args.cycle_log,
        skill_library=args.skill_library,
        findings_dir=args.findings_dir,
        questions_dir=args.questions_dir,
        mb_logs_dir=args.mb_logs_dir,
        proposals_root=args.proposals_root,
        output=args.output,
    )
    if result.proposer_error:
        print(f"meta-loop propose — proposer failed: {result.proposer_error}", file=sys.stderr)
        return 1
    print(
        f"meta-loop propose — wrote {len(result.written)} proposal(s) "
        f"to {args.proposals_root / 'pending'}, "
        f"rejected {len(result.rejected_raw)} malformed candidate(s)"
    )
    for path in result.written:
        print(f"  + {path.name}")
    return 0


def _cmd_diagnose(args: argparse.Namespace) -> int:
    report = diagnose.run(
        cycle_log=args.cycle_log,
        skill_library=args.skill_library,
        findings_dir=args.findings_dir,
        questions_dir=args.questions_dir,
        output=args.output,
        now=dt.datetime.now(dt.timezone.utc),
    )
    print(f"meta-loop diagnose — wrote {args.output}")
    print(
        f"  cycles={report.cycles_total} "
        f"manifest_regressions={len(report.manifest_regressions)} "
        f"stagnations={len(report.stagnations)} "
        f"techniques={len(report.techniques)}"
    )
    return 0


def _stub(name: str):
    def _fn(args: argparse.Namespace) -> int:  # noqa: ARG001
        raise NotImplementedError(
            f"meta_loop.{name} — not yet implemented " "(scheduled later in js/feat/meta-loop)"
        )

    return _fn


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="meta_loop",
        description=(
            "Meta-loop: outer loop on cycle outcomes; gated proposals to inner loop. "
            "See mb/active/js-feat-meta-loop.md."
        ),
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    _add_diagnose(sub)
    _add_propose(sub)
    _add_review(sub)

    # Stub for forward-declared shadow subcommand.
    sub.add_parser("shadow", help="(Goal 5) shadow A/B harness; not yet implemented")

    args = parser.parse_args(argv)

    handlers = {
        "diagnose": _cmd_diagnose,
        "propose": _cmd_propose,
        "review": _cmd_review,
        "shadow": _stub("shadow"),
    }
    return handlers[args.cmd](args)


def _add_review(sub: argparse._SubParsersAction) -> None:
    p = sub.add_parser(
        "review",
        help="human-review CLI: list pending proposals; accept/reject/skip",
    )
    p.add_argument(
        "--proposals-root",
        type=Path,
        default=_DEFAULT_MB / "proposals",
    )
    p.add_argument(
        "--repo-root",
        type=Path,
        default=_REPO,
        help="repo root for git apply (defaults to cb worktree root)",
    )
    p.add_argument(
        "--list",
        action="store_true",
        help="list pending proposals and exit (no interactive review)",
    )


def _cmd_review(args: argparse.Namespace) -> int:
    store = ProposalStore(args.proposals_root)
    if args.list:
        print(review.list_pending(store), end="")
        return 0
    summary = review.review_pending(store, repo_root=args.repo_root)
    print(
        f"\nmeta-loop review — "
        f"{len(summary.accepted)} accepted, "
        f"{len(summary.rejected)} rejected, "
        f"{len(summary.skipped)} skipped, "
        f"{len(summary.errored)} errored"
    )
    for o in summary.accepted:
        print(
            f"  ✓ {o.proposal.id} → applied (commit {o.commit_sha[:10] if o.commit_sha else '?'})"
        )
    for o in summary.errored:
        print(f"  ! {o.proposal.id} → {o.error}", file=sys.stderr)
    return 0 if not summary.errored else 1


if __name__ == "__main__":
    raise SystemExit(main())
