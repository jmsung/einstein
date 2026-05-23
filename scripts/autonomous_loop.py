#!/usr/bin/env python3
"""autonomous_loop.py — outer loop over the 23 Einstein Arena problems.

Architecture (this file = OUTER loop only; the inner attempt is filled
by Goal 4):

    1. Load problem queue (docs/wiki/problems/*.md frontmatter)
    2. Filter by status (skip blocked / hidden / shelved / frozen / conquered)
    3. Sort by tier (S>A>B>C) then problem_id ascending
    4. For each problem in the queue:
       a. inner_attempt(problem)  — placeholder for Goal 4
       b. record_cycle_row(...)   — append to docs/agent/cycle-log.md
       c. cycle_runner.sh(cycle_id, problem)  — discipline (refresh_qmd,
          wiki_graph, gap_search, promotion check)

Usage:
    uv run python scripts/autonomous_loop.py --one-problem
    uv run python scripts/autonomous_loop.py --one-problem --dry-run
    uv run python scripts/autonomous_loop.py --max-problems 3
    uv run python scripts/autonomous_loop.py --queue-only      # just print

Per .claude/rules/cycle-discipline.md: every cycle gets exactly one row in
docs/agent/cycle-log.md. This module is the row-writer for autonomous
cycles; human-driven cycles still hand-author their rows.
"""
from __future__ import annotations

import argparse
import datetime as dt
import logging
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

_REPO = Path(__file__).resolve().parents[1]
DEFAULT_PROBLEMS_DIR = _REPO / "docs" / "wiki" / "problems"
DEFAULT_CYCLE_LOG = _REPO / "docs" / "agent" / "cycle-log.md"
DEFAULT_CYCLE_RUNNER = _REPO / "docs" / "tools" / "cycle_runner.sh"
DEFAULT_SKILL_LIBRARY = _REPO / "docs" / "agent" / "skill-library.md"

# Local imports — strategy_picker lives in docs/tools/
sys.path.insert(0, str(_REPO / "docs" / "tools"))
try:
    import strategy_picker  # type: ignore[import-not-found]
except ImportError:
    strategy_picker = None  # type: ignore[assignment]

log = logging.getLogger("autonomous_loop")

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
ROW_ID_RE = re.compile(r"^\|\s*(\d+)\s*\|")

TIER_ORDER = {"S": 0, "A": 1, "B": 2, "C": 3}
# Statuses considered "ready to attempt". Anything else (frozen, conquered,
# blocked, hidden, shelved, proximity-guard) is skipped by default.
ACTIVE_STATUSES = {"open", "seed"}
ACTIVE_PATTERNS = (
    re.compile(r"^rank-\d+$"),         # rank-1, rank-2, rank-3
    re.compile(r"^rank-\d+-tied$"),    # rank-1-tied
)


# ---------------- data model ----------------


@dataclass
class Problem:
    problem_id: int
    slug: str
    tier: str
    status: str
    score_current: float | None
    path: Path
    extra: dict = field(default_factory=dict)

    @property
    def display(self) -> str:
        return f"P{self.problem_id}-{self.slug}"

    @property
    def file_slug(self) -> str:
        return f"{self.problem_id}-{self.slug}"


@dataclass
class CycleResult:
    cycle_id: int
    problem: Problem
    outcome: str
    notes: str


# ---------------- frontmatter parsing ----------------


def _parse_frontmatter(text: str) -> dict | None:
    m = FM_RE.match(text)
    if not m:
        return None
    fm: dict = {}
    for line in m.group(1).splitlines():
        kv = re.match(r"^([a-zA-Z_]+):\s*(.*)$", line)
        if not kv:
            continue
        key, val = kv.group(1), kv.group(2).strip()
        fm[key] = val.strip().strip("\"'")
    return fm


def load_problems(problems_dir: Path) -> list[Problem]:
    """Parse every problem page in `problems_dir`. Skips _*.md and README.md."""
    problems: list[Problem] = []
    for path in sorted(problems_dir.glob("*.md")):
        name = path.name
        if name.startswith("_") or name == "README.md":
            continue
        fm = _parse_frontmatter(path.read_text())
        if not fm or "problem_id" not in fm:
            log.warning("skipping %s — no/invalid frontmatter", path.name)
            continue
        try:
            pid = int(fm["problem_id"])
        except ValueError:
            continue

        # Slug derived from filename: '1-erdos-overlap.md' → 'erdos-overlap'
        stem = path.stem  # '1-erdos-overlap'
        slug_match = re.match(r"^(\d+[a-z]?)-(.+)$", stem)
        slug = slug_match.group(2) if slug_match else stem

        score: float | None = None
        if fm.get("score_current"):
            try:
                score = float(fm["score_current"])
            except ValueError:
                pass

        problems.append(Problem(
            problem_id=pid,
            slug=slug,
            tier=fm.get("tier", "?"),
            status=fm.get("status", "unknown"),
            score_current=score,
            path=path,
            extra=fm,
        ))
    return problems


# ---------------- queue ----------------


def is_active(problem: Problem) -> bool:
    """True if the problem is ready to attempt; False if frozen/conquered/etc."""
    s = problem.status
    if s in ACTIVE_STATUSES:
        return True
    return any(p.fullmatch(s) for p in ACTIVE_PATTERNS)


def build_queue(problems: list[Problem]) -> list[Problem]:
    """Return active problems ordered by tier (S→C) then problem_id ascending."""
    active = [p for p in problems if is_active(p)]
    return sorted(
        active,
        key=lambda p: (TIER_ORDER.get(p.tier, 99), p.problem_id),
    )


# ---------------- cycle-log row ----------------


def _author_mix(d: dict[str, int]) -> str:
    return f"a:{d.get('agent', 0)}/h:{d.get('human', 0)}/hyb:{d.get('hybrid', 0)}"


def format_cycle_log_row(
    *,
    cycle_id: int,
    problem: str,
    start_score: float | str,
    end_score: float | str,
    hours: float,
    compute: str,
    wiki_citations: int,
    findings_added: int,
    concepts_added: int,
    author_mix: dict[str, int],
    outcome: str,
    notes: str,
) -> str:
    """Produce one markdown table row matching docs/agent/cycle-log.md schema."""
    def _fmt_score(s: float | str) -> str:
        if isinstance(s, (int, float)):
            # 14 sig figs preserves problem scores like 2.6390274695 and
            # 1.5028616283497658 without truncation.
            return f"{s:.14g}"
        return str(s)

    s_start = _fmt_score(start_score)
    s_end = _fmt_score(end_score)
    score_pair = f"{s_start} → {s_end}" if s_start != s_end else f"{s_start} (no Δ)"
    return (
        f"| {cycle_id} | {problem} | {score_pair} | {hours:g} | {compute} | "
        f"{wiki_citations} | {findings_added} | {concepts_added} | "
        f"{_author_mix(author_mix)} | {outcome} | {notes} |"
    )


def append_cycle_log_row(cycle_log: Path, row: str) -> None:
    """Append `row` (no newline) to the end of `cycle_log`."""
    text = cycle_log.read_text() if cycle_log.exists() else ""
    if text and not text.endswith("\n"):
        text += "\n"
    text += row + "\n"
    cycle_log.write_text(text)


def next_cycle_id(cycle_log: Path) -> int:
    """Read existing cycle ids from the log; return max + 1, or 0 if empty."""
    if not cycle_log.exists():
        return 0
    max_id = -1
    for line in cycle_log.read_text().splitlines():
        m = ROW_ID_RE.match(line)
        if m:
            try:
                max_id = max(max_id, int(m.group(1)))
            except ValueError:
                continue
    return max_id + 1


# ---------------- inner attempt placeholder ----------------


def inner_attempt(problem: Problem, dry_run: bool = False,
                  skill_library: Path = DEFAULT_SKILL_LIBRARY) -> dict:
    """Reflection chain for one cycle attempt.

    Order of operations:
      1. category lookup (problem_id → category)
      2. strategy_picker reads skill-library → (prior, novel) pick per the
         autoresearch 1+1 rule
      3. Execute step is intentionally a placeholder — per-problem optimizer
         integration is Phase-5 work (the orchestrator can't know how to
         invoke `scripts/<problem>/optimize.py` without the per-problem
         entry point being canonicalized).

    The cycle-log row captures whatever signal we did produce: the strategy
    pick and the rationale. A subsequent Phase-5 commit will replace the
    placeholder execute with a real per-problem dispatch.
    """
    log.info("inner_attempt — problem=%s tier=%s status=%s",
             problem.display, problem.tier, problem.status)

    notes_parts: list[str] = []
    if strategy_picker is None:
        log.warning("strategy_picker not importable — skipping strategy pick")
        notes_parts.append("strategy_picker unavailable")
        outcome = "scaffold-no-attempt"
    else:
        category = strategy_picker.category_for(problem.problem_id)
        log.info("  category=%s", category)
        pick = strategy_picker.pick_strategy(skill_library, category=category)
        log.info("  %s", pick.rationale)
        notes_parts.append(f"category={category}")
        if pick.prior is not None:
            notes_parts.append(
                f"prior={pick.prior.technique}({pick.prior.hit_rate:.2f})"
            )
        if pick.novel is not None:
            notes_parts.append(
                f"novel={pick.novel.technique}(finding_rate={pick.novel.finding_rate:.2f})"
            )
        if pick.prior is None and pick.novel is None:
            outcome = "scaffold-no-attempt"
            notes_parts.append("(no library matches — council needed)")
        else:
            outcome = "strategy-picked-no-execution"

    notes = "autonomous_loop inner_attempt — " + "; ".join(notes_parts) + (
        ". Execute step deferred to Phase 5 per-problem optimizer integration."
    )

    return {
        "start_score": problem.score_current if problem.score_current is not None else "none",
        "end_score": problem.score_current if problem.score_current is not None else "none",
        "hours": 0.0,
        "compute": "none-strategy-only",
        "wiki_citations": 0,
        "findings_added": 0,
        "concepts_added": 0,
        "author_mix": {"agent": 1, "human": 0, "hybrid": 0},
        "outcome": outcome,
        "notes": notes,
    }


# ---------------- single-cycle drive ----------------


CycleRunner = Callable[[int, str], int]


def _shell_cycle_runner(cycle_id: int, problem_slug: str) -> int:
    """Invoke docs/tools/cycle_runner.sh; return its exit code."""
    script = DEFAULT_CYCLE_RUNNER
    if not script.is_file():
        log.warning("cycle_runner.sh not at %s — skipping discipline step", script)
        return 0
    return subprocess.run(
        ["bash", str(script), str(cycle_id), problem_slug],
        cwd=_REPO,
        check=False,
    ).returncode


def run_one_problem(
    *,
    problems_dir: Path = DEFAULT_PROBLEMS_DIR,
    cycle_log: Path = DEFAULT_CYCLE_LOG,
    dry_run: bool = False,
    cycle_runner: CycleRunner | None = None,
) -> CycleResult | None:
    """Pick the top-priority active problem and run one cycle on it.

    Returns None if the queue is empty (no active problems).
    """
    problems = load_problems(problems_dir)
    queue = build_queue(problems)
    if not queue:
        log.info("queue empty — no active problems")
        return None

    problem = queue[0]
    cycle_id = next_cycle_id(cycle_log)
    log.info("cycle %d → %s (tier %s, status %s)",
             cycle_id, problem.display, problem.tier, problem.status)

    result = inner_attempt(problem, dry_run=dry_run)
    if dry_run:
        log.info("[dry-run] would append cycle %d row to %s and call cycle_runner",
                 cycle_id, cycle_log.name)
        return CycleResult(cycle_id=cycle_id, problem=problem,
                           outcome=result["outcome"], notes=result["notes"])

    row = format_cycle_log_row(
        cycle_id=cycle_id,
        problem=problem.display,
        **result,
    )
    append_cycle_log_row(cycle_log, row)

    runner = cycle_runner or _shell_cycle_runner
    rc = runner(cycle_id, problem.file_slug)
    if rc != 0:
        log.warning("cycle_runner exited %d for cycle %d", rc, cycle_id)

    return CycleResult(cycle_id=cycle_id, problem=problem,
                       outcome=result["outcome"], notes=result["notes"])


def run_queue(
    *,
    problems_dir: Path = DEFAULT_PROBLEMS_DIR,
    cycle_log: Path = DEFAULT_CYCLE_LOG,
    max_problems: int = 1,
    dry_run: bool = False,
) -> list[CycleResult]:
    """Run up to `max_problems` cycles, one per top-priority problem."""
    results: list[CycleResult] = []
    for i in range(max_problems):
        r = run_one_problem(
            problems_dir=problems_dir, cycle_log=cycle_log, dry_run=dry_run,
        )
        if r is None:
            log.info("queue exhausted after %d cycles", i)
            break
        results.append(r)
    return results


# ---------------- CLI ----------------


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--problems-dir", type=Path, default=DEFAULT_PROBLEMS_DIR)
    parser.add_argument("--cycle-log", type=Path, default=DEFAULT_CYCLE_LOG)
    parser.add_argument("--one-problem", action="store_true",
                        help="Run a single cycle on the top-priority active problem.")
    parser.add_argument("--max-problems", type=int, default=1,
                        help="Maximum cycles to run in one invocation (default 1).")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print plan only; do not append cycle-log or call cycle_runner.")
    parser.add_argument("--queue-only", action="store_true",
                        help="Print the current active queue and exit.")
    args = parser.parse_args(argv)

    if args.queue_only:
        problems = load_problems(args.problems_dir)
        queue = build_queue(problems)
        log.info("active queue (%d problems):", len(queue))
        for p in queue:
            score = f"{p.score_current:.6g}" if p.score_current is not None else "—"
            print(f"  tier={p.tier}  id={p.problem_id:>2}  "
                  f"score={score:>14}  status={p.status:<30}  {p.slug}")
        return 0

    max_problems = 1 if args.one_problem else args.max_problems
    results = run_queue(
        problems_dir=args.problems_dir,
        cycle_log=args.cycle_log,
        max_problems=max_problems,
        dry_run=args.dry_run,
    )
    log.info("completed %d cycles", len(results))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
