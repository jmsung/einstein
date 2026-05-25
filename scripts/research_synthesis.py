#!/usr/bin/env python3
"""research_synthesis.py — pre-cycle literature synthesis CLI.

Goal 2 of `js/feat/research-synthesis`. Reads `mb/problems/<id>-<slug>/strategy.md`,
issues a small number of qmd queries against `einstein-wiki-source` +
`einstein-wiki`, asks claude (via claude_headless) to produce a typed
`LiteratureSynthesis`, and writes the result as
`mb/problems/<id>-<slug>/literature-synthesis-<YYYY-MM-DD>.md`.

Design anchor: `docs/wiki/findings/research-synthesis-design.md` (Patterns A/B/C/D).
Schema: `einstein.research_synthesis.schema.LiteratureSynthesis`.

Usage::

    uv run python scripts/research_synthesis.py --problem-id 14
    uv run python scripts/research_synthesis.py --problem-id 14 --dry-run   # print prompt, no claude call

Soft budgets: ~30s qmd, ~30K tokens claude. Hard caps via claude_headless
``timeout_seconds`` and ``--max-budget-usd`` flag.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import logging
import sys
from collections.abc import Callable
from pathlib import Path

from einstein.research_synthesis.query import gather
from einstein.research_synthesis.schema import LiteratureSynthesis
from einstein.research_synthesis.synthesizer import _build_prompt, synthesize

log = logging.getLogger("research_synthesis")

_REPO = Path(__file__).resolve().parents[1]
DEFAULT_MB = _REPO.parent / "mb"
PROBLEM_CONTEXT_CHARS = 500


def resolve_slug(problem_id: int, mb_dir: Path) -> str | None:
    """Find the unique mb/problems/<id>-<slug>/ directory for the given id.

    Returns the slug (without the leading "<id>-") if exactly one match;
    raises ValueError if multiple candidates exist (e.g. P17 has both
    "circles-rectangle" and "hexagon-packing" in some snapshots).
    """
    problems_dir = mb_dir / "problems"
    if not problems_dir.is_dir():
        return None
    candidates = sorted(
        p for p in problems_dir.iterdir() if p.is_dir() and p.name.startswith(f"{problem_id}-")
    )
    if not candidates:
        return None
    if len(candidates) > 1:
        names = ", ".join(c.name for c in candidates)
        raise ValueError(
            f"multiple mb/problems/ dirs match id={problem_id}: {names}. "
            f"Pass --slug to disambiguate."
        )
    name = candidates[0].name
    return name.split("-", 1)[1] if "-" in name else ""


def read_strategy(mb_dir: Path, problem_id: int, slug: str) -> str:
    """Read the first PROBLEM_CONTEXT_CHARS of mb/problems/<id>-<slug>/strategy.md."""
    path = mb_dir / "problems" / f"{problem_id}-{slug}" / "strategy.md"
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")[:PROBLEM_CONTEXT_CHARS]


def derive_queries(problem_id: int, slug: str, strategy_text: str) -> list[str]:
    """Generate 3-5 qmd queries from the problem's slug + strategy keywords.

    Keep it deterministic — no LLM call for query formulation. Good enough
    coverage for the gather step; the synthesizer's job is the deep work.
    """
    base = slug.replace("-", " ")
    queries = [
        f"P{problem_id} {base}",
        base,
    ]
    # Pull a couple of distinctive nouns from the first lines of strategy.md
    for line in strategy_text.splitlines()[:20]:
        line = line.strip().lstrip("#").strip()
        if 8 < len(line) < 80 and not line.startswith("---"):
            queries.append(line)
        if len(queries) >= 5:
            break
    return queries[:5]


def build_output_path(mb_dir: Path, problem_id: int, slug: str, drafted_at: str) -> Path:
    return mb_dir / "problems" / f"{problem_id}-{slug}" / f"literature-synthesis-{drafted_at}.md"


def run_cli(
    args: argparse.Namespace,
    *,
    qmd_runner: Callable | None = None,
    claude_runner: Callable | None = None,
    out_stream=sys.stdout,
) -> int:
    """Pure-Python entry point with injectable runners (used by tests)."""
    mb_dir: Path = args.mb_dir
    drafted_at: str = args.drafted_at or _dt.date.today().isoformat()
    # Resolve slug
    try:
        slug = args.slug or resolve_slug(args.problem_id, mb_dir)
    except ValueError as e:
        print(f"error: {e}", file=out_stream)
        return 1
    if not slug:
        print(
            f"error: no mb/problems/{args.problem_id}-* directory found under {mb_dir}",
            file=out_stream,
        )
        return 1
    strategy_text = read_strategy(mb_dir, args.problem_id, slug)
    queries = derive_queries(args.problem_id, slug, strategy_text)
    source_hits, wiki_hits = gather(
        queries,
        n_per_query=10,
        top_k_source=args.top_k_source,
        top_k_wiki=args.top_k_wiki,
        runner=qmd_runner,
    )
    if args.dry_run:
        prompt = _build_prompt(
            problem_id=args.problem_id,
            problem_slug=slug,
            problem_context=strategy_text,
            source_hits=source_hits,
            wiki_hits=wiki_hits,
            drafted_at=drafted_at,
        )
        print("--- DRY RUN: prompt below ---", file=out_stream)
        print(prompt, file=out_stream)
        print(
            f"--- would write: {build_output_path(mb_dir, args.problem_id, slug, drafted_at)} ---",
            file=out_stream,
        )
        return 0
    result: LiteratureSynthesis | None = synthesize(
        problem_id=args.problem_id,
        problem_slug=slug,
        problem_context=strategy_text,
        source_hits=source_hits,
        wiki_hits=wiki_hits,
        drafted_at=drafted_at,
        runner=claude_runner,
        max_budget_usd=args.max_budget_usd,
    )
    if result is None:
        print("error: synthesis failed (see logs)", file=out_stream)
        return 1
    output_path = args.output or build_output_path(mb_dir, args.problem_id, slug, drafted_at)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result.to_markdown(), encoding="utf-8")
    print(f"wrote: {output_path}", file=out_stream)
    return 0


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0] if __doc__ else None)
    p.add_argument("--problem-id", type=int, required=True)
    p.add_argument("--slug", help="override slug (else auto-resolved from mb/problems/)")
    p.add_argument("--top-k-source", type=int, default=50)
    p.add_argument("--top-k-wiki", type=int, default=20)
    p.add_argument(
        "--output",
        type=Path,
        help="output markdown path (default: mb/problems/<id>-<slug>/literature-synthesis-<date>.md)",
    )
    p.add_argument("--mb-dir", type=Path, default=DEFAULT_MB)
    p.add_argument("--drafted-at", help="YYYY-MM-DD (default: today)")
    p.add_argument("--max-budget-usd", type=float, default=None)
    p.add_argument(
        "--dry-run", action="store_true", help="print prompt and exit before calling claude"
    )
    p.add_argument("-v", "--verbose", action="store_true")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO)
    return run_cli(args)


if __name__ == "__main__":
    raise SystemExit(main())
