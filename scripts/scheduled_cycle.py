"""Cron entry point for the autonomous loop — Phase 3 Goal 2.

Thin wrapper around `autonomous_loop.py --one-problem --by-priority` adding
the scheduler-level guards the loop itself doesn't have:

- **runs/day cap** (`--max-runs-per-day`, default 8) via the run ledger
  `mb/logs/scheduler-runs.log` — one line per real run, dry runs excluded.
- **hard wall-clock timeout** (`--timeout-s`, default 7200) — the loop's own
  1800s cap is per-`claude -p` call; a visit (≤3 attempts + post-cycle
  discipline) needs an outer bound for cron hygiene.
- **run ledger** — `<iso-ts> exit=<code|timeout> dur=<s>s` per run, for the
  Goal-4 health monitor.

Everything else stays where it already lives (deliberately NOT duplicated
here): kill switches `EINSTEIN_INNER_AGENT=0` / `EINSTEIN_AUTO_SUBMIT=0` and
the sentinel `mb/.inner-agent-disabled` are read by the loop's precheck; the
5M-token/day budget, network reachability, and thermal throttle gates fire
there too; `--skip-if-recent` + the lockfile (exit 75 = EX_TEMPFAIL, cron
retries next interval) guard concurrency. This wrapper passes the
environment through untouched.

Goal-0 lesson baked in: the command must NOT use `--skip-gates` — the
precheck is what enables the LLM path (skipping it silently degrades every
scheduled run to the mechanical path).

## Cron spec (do NOT install until Goal 5's promote-to-unattended verdict)

Every 2h, via the harness `schedule` skill / CronCreate or crontab:

    0 */2 * * *  cd <cb> && uv run python scripts/scheduled_cycle.py >> <mb>/logs/scheduler.log 2>&1

Disarm: `EINSTEIN_INNER_AGENT=0` (mechanical only), `touch mb/.inner-agent-disabled`
(skip everything), or remove the cron entry. Auto-submit policy per axioms.md.
"""

from __future__ import annotations

import argparse
import datetime as dt
import logging
import subprocess
import sys
from pathlib import Path
from typing import Callable

_REPO = Path(__file__).resolve().parents[1]
DEFAULT_MB_DIR = _REPO.parent / "mb"
DEFAULT_LEDGER = DEFAULT_MB_DIR / "logs" / "scheduler-runs.log"
DEFAULT_MAX_RUNS_PER_DAY = 8
DEFAULT_TIMEOUT_S = 7200
DEFAULT_SKIP_IF_RECENT_MIN = 45

log = logging.getLogger("scheduled_cycle")

Runner = Callable[[list[str], int], int]


def build_command(*, skip_if_recent_min: int, dry_run: bool = False) -> list[str]:
    """The exact loop invocation a scheduled run executes."""
    cmd = [
        sys.executable,
        str(_REPO / "scripts" / "autonomous_loop.py"),
        "--one-problem",
        "--by-priority",
        "--skip-if-recent",
        str(skip_if_recent_min),
    ]
    if dry_run:
        cmd.append("--dry-run")
    return cmd


def runs_today(ledger: Path, *, today: str) -> int:
    """Count ledger lines stamped with today's date (YYYY-MM-DD prefix)."""
    try:
        text = ledger.read_text()
    except OSError:
        return 0
    return sum(1 for line in text.splitlines() if line.startswith(today))


def should_run(ledger: Path, *, max_runs_per_day: int, today: str) -> bool:
    return runs_today(ledger, today=today) < max_runs_per_day


def record_run(ledger: Path, *, exit_code: int | str, duration_s: float, ts: str) -> None:
    try:
        ledger.parent.mkdir(parents=True, exist_ok=True)
        with ledger.open("a") as f:
            f.write(f"{ts} exit={exit_code} dur={duration_s:.1f}s\n")
    except OSError as e:
        log.warning("run-ledger append failed: %s", e)


def _default_runner(cmd: list[str], timeout: int) -> int:
    return subprocess.run(cmd, timeout=timeout, check=False).returncode


def main(
    argv: list[str] | None = None,
    *,
    runner: Runner | None = None,
    today: str | None = None,
    now_iso: str | None = None,
) -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER)
    parser.add_argument("--max-runs-per-day", type=int, default=DEFAULT_MAX_RUNS_PER_DAY)
    parser.add_argument("--timeout-s", type=int, default=DEFAULT_TIMEOUT_S)
    parser.add_argument("--skip-if-recent", type=int, default=DEFAULT_SKIP_IF_RECENT_MIN)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Pass --dry-run to the loop; not counted against the daily cap.",
    )
    args = parser.parse_args(argv)

    if runner is None:
        runner = _default_runner
    now = dt.datetime.now(dt.timezone.utc)
    if today is None:
        today = now.strftime("%Y-%m-%d")
    if now_iso is None:
        now_iso = now.strftime("%Y-%m-%dT%H:%M:%SZ")

    if not args.dry_run and not should_run(
        args.ledger, max_runs_per_day=args.max_runs_per_day, today=today
    ):
        log.info(
            "daily cap reached (%d runs today ≥ %d) — skipping (clean exit for cron)",
            runs_today(args.ledger, today=today),
            args.max_runs_per_day,
        )
        return 0

    cmd = build_command(skip_if_recent_min=args.skip_if_recent, dry_run=args.dry_run)
    log.info("scheduled run: %s (timeout %ds)", " ".join(cmd), args.timeout_s)
    start = dt.datetime.now(dt.timezone.utc)
    try:
        rc: int | str = runner(cmd, args.timeout_s)
    except subprocess.TimeoutExpired:
        rc = "timeout"
        log.error("loop exceeded %ds wall-clock — killed", args.timeout_s)
    duration = (dt.datetime.now(dt.timezone.utc) - start).total_seconds()

    if not args.dry_run:
        record_run(args.ledger, exit_code=rc, duration_s=duration, ts=now_iso)
    return rc if isinstance(rc, int) else 124  # 124 = conventional timeout code


if __name__ == "__main__":
    raise SystemExit(main())
