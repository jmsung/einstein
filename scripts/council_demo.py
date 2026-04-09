"""Show how the mathematician council dispatches for a given problem.

The council package parses persona definitions from a private config
file and returns the personas to deploy as parallel research subagents
during the Recon goal.

This script is integration sketch only — it prints the dispatched
personas and a stub of the prompt that would be fed to each subagent.
No subagents are spawned here.

Usage:
    uv run python scripts/council_demo.py kissing_number
    uv run python scripts/council_demo.py graph_theory
    uv run python scripts/council_demo.py autocorrelation --problem-id 3
"""

from __future__ import annotations

import argparse
import sys
import textwrap

from einstein.council import Persona, dispatch
from einstein.council.personas import COUNCIL_PATH


def build_subagent_prompt(persona: Persona, problem_id: int | None) -> str:
    """Render the seed prompt that would be passed to a research subagent.

    The actual subagent invocation happens elsewhere; this just shows
    how the persona's fields compose into a prompt body.
    """
    header = f"You are channelling {persona.name} ({persona.perspective})."
    pid = f"Problem {problem_id}" if problem_id is not None else "the target problem"
    return textwrap.dedent(
        f"""\
        {header}

        Task: Approach {pid} with your characteristic perspective.

        Real expertise: {persona.expertise}

        Approach: {persona.prompt_seed}

        Recommended literature: {persona.literature}

        Worked example: {persona.example_insight}
        """
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "category",
        help="Problem category, e.g. kissing_number, graph_theory, autocorrelation",
    )
    parser.add_argument(
        "--problem-id",
        type=int,
        default=None,
        help="Optional problem ID to inject into prompts",
    )
    parser.add_argument(
        "--show-prompts",
        action="store_true",
        help="Print the full subagent prompt body for each persona",
    )
    args = parser.parse_args()

    if COUNCIL_PATH is None:
        print(
            "ERROR: council config not found. "
            "Set EINSTEIN_COUNCIL_PATH to the private config file.",
            file=sys.stderr,
        )
        return 1

    print(f"Loading council from: {COUNCIL_PATH}")
    print(f"Dispatching for category: {args.category}\n")

    personas = dispatch(args.category)
    if not personas:
        print("No personas dispatched (council file empty or unreadable).")
        return 1

    core = [p for p in personas if p.tier == "core"]
    bench = [p for p in personas if p.tier == "bench"]

    print(f"Core council ({len(core)}):")
    for p in core:
        print(f"  - {p.name} — {p.perspective}")

    print(f"\nTriggered specialists ({len(bench)}):")
    if not bench:
        print("  (none)")
    for p in bench:
        triggers = ", ".join(sorted(p.trigger_categories))
        print(f"  - {p.name} — {p.perspective}  [{triggers}]")

    if args.show_prompts:
        print("\n" + "=" * 72)
        for p in personas:
            print(f"\n--- {p.name} ({p.tier}) ---")
            print(build_subagent_prompt(p, args.problem_id))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
