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

from einstein.meta_loop import diagnose  # noqa: E402

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

    # Stubs for forward-declared subcommands so `--help` lists them and so
    # an agent doesn't accidentally believe they exist yet.
    sub.add_parser("propose", help="(Goal 2) emit typed proposals; not yet implemented")
    sub.add_parser("review", help="(Goal 4) human-review CLI; not yet implemented")
    sub.add_parser("shadow", help="(Goal 5) shadow A/B harness; not yet implemented")

    args = parser.parse_args(argv)

    handlers = {
        "diagnose": _cmd_diagnose,
        "propose": _stub("propose"),
        "review": _stub("review"),
        "shadow": _stub("shadow"),
    }
    return handlers[args.cmd](args)


if __name__ == "__main__":
    raise SystemExit(main())
