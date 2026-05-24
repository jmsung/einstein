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
import os
import re
import subprocess
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

_REPO = Path(__file__).resolve().parents[1]
DEFAULT_PROBLEMS_DIR = _REPO / "docs" / "wiki" / "problems"
DEFAULT_CYCLE_LOG = _REPO / "docs" / "agent" / "cycle-log.md"
DEFAULT_CYCLE_RUNNER = _REPO / "docs" / "tools" / "cycle_runner.sh"
DEFAULT_SKILL_LIBRARY = _REPO / "docs" / "agent" / "skill-library.md"
DEFAULT_LOCKFILE = _REPO / ".autonomous-loop.lock"

# Local imports — strategy_picker lives in docs/tools/
sys.path.insert(0, str(_REPO / "docs" / "tools"))
try:
    import strategy_picker  # type: ignore[import-not-found]
except ImportError:
    strategy_picker = None  # type: ignore[assignment]

log = logging.getLogger("autonomous_loop")

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
ROW_ID_RE = re.compile(r"^\|\s*(\d+)\s*\|")

# Statuses considered permanently inactive — only `retired` (the 5 dead pages
# archived 2026-05-23). Everything else — frozen, hidden, blocked, conquered,
# rank-N-frozen, shelved, rank-N-frozen-by-proximity-guard — is still a live
# arena problem. A more powerful agent should attempt every live problem in
# id order; let inner-loop convergence-detect / strategy-picker decide if
# real work is feasible. Local status often drifts from arena state anyway.
SKIP_STATUSES = {"retired"}


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
    """True unless the problem is permanently inactive (retired)."""
    return problem.status not in SKIP_STATUSES


def build_queue(problems: list[Problem]) -> list[Problem]:
    """Return live problems ordered by problem_id ascending.

    Goes through every live arena problem regardless of local status (frozen,
    conquered, blocked, hidden, etc.) — only `retired` is filtered. Tier-based
    prioritization removed: a powerful agent should attempt every problem in
    id order and let inner-loop logic decide viability.
    """
    return sorted(
        (p for p in problems if is_active(p)),
        key=lambda p: p.problem_id,
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
                  skill_library: Path = DEFAULT_SKILL_LIBRARY,
                  dispatcher: Callable[..., object] | None = None) -> dict:
    """Reflection chain for one cycle attempt.

    Order of operations:
      1. category lookup (problem_id → category)
      2. strategy_picker reads skill-library → (prior, novel) pick
      3. EXECUTE: optimizer_dispatch.dispatch(problem_id, strategy) — if the
         problem has a manifest entry, invoke its optimizer and parse score.
         If no manifest entry → fall through to strategy-picked-no-execution
         (placeholder outcome, was the only behavior pre-A0).

    `dispatcher` is a test seam — defaults to `optimizer_dispatch.dispatch`.
    """
    log.info("inner_attempt — problem=%s tier=%s status=%s",
             problem.display, problem.tier, problem.status)

    notes_parts: list[str] = []
    chosen_strategy: str | None = None
    if strategy_picker is None:
        log.warning("strategy_picker not importable — skipping strategy pick")
        notes_parts.append("strategy_picker unavailable")
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
            chosen_strategy = pick.prior.technique
        if pick.novel is not None:
            notes_parts.append(
                f"novel={pick.novel.technique}(finding_rate={pick.novel.finding_rate:.2f})"
            )
            # Novel takes precedence as the strategy name passed to dispatch
            chosen_strategy = pick.novel.technique
        if pick.prior is None and pick.novel is None:
            notes_parts.append("(no library matches — council needed)")

    # EXECUTE step — optimizer_dispatch
    start_score = problem.score_current
    end_score = problem.score_current
    outcome = "scaffold-no-attempt"
    runtime_hours = 0.0
    compute_tag = "none-strategy-only"

    if dispatcher is None:
        # Lazy import — dispatch lives in src/einstein, not docs/tools
        sys.path.insert(0, str(_REPO / "src"))
        try:
            from einstein.optimizer_dispatch import dispatch as _real_dispatch
            dispatcher = _real_dispatch
        except ImportError:
            log.warning("optimizer_dispatch unavailable — skipping execute")
            dispatcher = None

    if dispatcher is not None and not dry_run:
        result = dispatcher(problem_id=problem.problem_id, strategy=chosen_strategy)
        if getattr(result, "error", None) and "no manifest entry" in result.error:
            log.info("  no manifest entry for P%d — execute deferred",
                     problem.problem_id)
            notes_parts.append("dispatch: no-manifest-entry")
            outcome = "strategy-picked-no-execution"
        elif result.ok:
            log.info("  dispatch ok: optimizer=%s score=%s runtime=%.1fs",
                     result.optimizer, result.score, result.runtime_seconds)
            notes_parts.append(
                f"dispatch={result.optimizer} score={result.score}"
            )
            end_score = result.score
            runtime_hours = result.runtime_seconds / 3600.0
            compute_tag = "local-cpu"  # TODO: thread compute_router decision through
            if (start_score is not None
                    and result.score is not None
                    and result.score < start_score):  # type: ignore[operator]
                outcome = "improved-local"
            else:
                outcome = "no-change"
        else:
            log.warning("  dispatch failed: %s", result.error)
            notes_parts.append(f"dispatch-failed: {result.error}")
            outcome = "dispatch-failed"
    elif dry_run:
        notes_parts.append("dry-run (dispatch skipped)")

    notes = "autonomous_loop inner_attempt — " + "; ".join(notes_parts)

    return {
        "start_score": start_score if start_score is not None else "none",
        "end_score": end_score if end_score is not None else "none",
        "hours": runtime_hours,
        "compute": compute_tag,
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
    skip_problem_ids: set[int] | None = None,
) -> CycleResult | None:
    """Pick the top-priority active problem and run one cycle on it.

    Returns None if the queue is empty (no active problems).
    """
    problems = load_problems(problems_dir)
    queue = build_queue(problems)
    if skip_problem_ids:
        queue = [p for p in queue if p.problem_id not in skip_problem_ids]
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


# ---------------- concurrency lock ----------------


class _LockHeld(RuntimeError):
    """Raised when the lockfile already exists (another loop is running)."""


def _acquire_lock(lockfile: Path) -> int:
    """Acquire an exclusive lock by creating `lockfile` with O_CREAT|O_EXCL.

    Returns the file descriptor (caller is responsible for releasing). On
    contention, raises _LockHeld with the holding pid + age.
    """
    try:
        fd = os.open(lockfile, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o644)
    except FileExistsError:
        try:
            stale = lockfile.read_text().strip()
        except OSError:
            stale = "(unknown)"
        try:
            age = time.time() - lockfile.stat().st_mtime
            age_str = f"{age:.0f}s old"
        except OSError:
            age_str = "(age unknown)"
        raise _LockHeld(
            f"another autonomous_loop is running (lockfile {lockfile} "
            f"held by {stale}, {age_str}). Remove the lockfile if stale."
        )
    os.write(fd, f"pid={os.getpid()} started={dt.datetime.now().isoformat()}\n".encode())
    return fd


def _release_lock(fd: int, lockfile: Path) -> None:
    try:
        os.close(fd)
    except OSError:
        pass
    try:
        lockfile.unlink()
    except FileNotFoundError:
        pass


# ---------------- recency skip ----------------


def _has_recent_cycle(cycle_log: Path, *, minutes: int) -> bool:
    """Return True iff the cycle-log was modified within the last `minutes`.

    Used for cron/loop safety: skip running if a cycle landed very recently.
    """
    if not cycle_log.is_file():
        return False
    age_sec = time.time() - cycle_log.stat().st_mtime
    return age_sec < minutes * 60


def run_queue(
    *,
    problems_dir: Path = DEFAULT_PROBLEMS_DIR,
    cycle_log: Path = DEFAULT_CYCLE_LOG,
    max_problems: int = 1,
    dry_run: bool = False,
    cycle_runner: CycleRunner | None = None,
) -> list[CycleResult]:
    """Run up to `max_problems` cycles, one per distinct top-priority problem.

    Tracks problems already cycled in this invocation so each call to
    `run_one_problem` picks the next un-cycled problem (otherwise queue[0]
    would re-select the same problem every iteration).
    """
    results: list[CycleResult] = []
    done_ids: set[int] = set()
    for i in range(max_problems):
        r = run_one_problem(
            problems_dir=problems_dir, cycle_log=cycle_log, dry_run=dry_run,
            cycle_runner=cycle_runner,
            skip_problem_ids=done_ids,
        )
        if r is None:
            log.info("queue exhausted after %d cycles", i)
            break
        done_ids.add(r.problem.problem_id)
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
    parser.add_argument("--skip-if-recent", type=int, default=0, metavar="MINUTES",
                        help="Skip the run (exit 0) if cycle-log was modified within "
                             "MINUTES. Useful under cron / loop to avoid clobbering "
                             "an in-flight cycle.")
    parser.add_argument("--discipline-once", action="store_true",
                        help="For multi-cycle sweeps: skip per-cycle "
                             "cycle_runner.sh (refresh_qmd, wiki_graph, "
                             "gap_search, wiki_lint) and run it once at the "
                             "end with the last cycle's info. Saves ~5min/"
                             "cycle on full-queue sweeps where the wiki "
                             "doesn't change between cycles.")
    parser.add_argument("--no-lock", action="store_true",
                        help="Skip the concurrency lockfile (use for explicit "
                             "manual concurrent runs).")
    parser.add_argument("--lockfile", type=Path, default=DEFAULT_LOCKFILE,
                        help="Path to the concurrency lockfile.")
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

    # cron/loop safety: skip if a cycle just landed
    if args.skip_if_recent > 0 and _has_recent_cycle(args.cycle_log, minutes=args.skip_if_recent):
        log.info("cycle-log mtime within %d min — skipping run (cron/loop safety)",
                 args.skip_if_recent)
        return 0

    # concurrency lock
    fd: int | None = None
    if not args.no_lock and not args.dry_run:
        try:
            fd = _acquire_lock(args.lockfile)
        except _LockHeld as e:
            log.error("%s", e)
            return 75   # EX_TEMPFAIL — cron will retry next interval

    try:
        max_problems = 1 if args.one_problem else args.max_problems
        inner_runner: CycleRunner | None = None
        if args.discipline_once and max_problems > 1:
            inner_runner = lambda _cid, _slug: 0  # no-op for per-cycle
        results = run_queue(
            problems_dir=args.problems_dir,
            cycle_log=args.cycle_log,
            max_problems=max_problems,
            dry_run=args.dry_run,
            cycle_runner=inner_runner,
        )
        log.info("completed %d cycles", len(results))
        if args.discipline_once and results and not args.dry_run:
            last = results[-1]
            log.info("--discipline-once: running cycle_runner once at end "
                     "(cycle %d, %s)", last.cycle_id, last.problem.file_slug)
            rc = _shell_cycle_runner(last.cycle_id, last.problem.file_slug)
            if rc != 0:
                log.warning("end-of-sweep cycle_runner exited %d", rc)
        return 0
    finally:
        if fd is not None:
            _release_lock(fd, args.lockfile)


if __name__ == "__main__":
    raise SystemExit(main())
