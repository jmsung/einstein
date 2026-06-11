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
import json
import logging
import subprocess
import sys
from pathlib import Path
from typing import Callable

_REPO = Path(__file__).resolve().parents[1]
DEFAULT_MB_DIR = _REPO.parent / "mb"
DEFAULT_LEDGER = DEFAULT_MB_DIR / "logs" / "scheduler-runs.log"
DEFAULT_TELEMETRY = DEFAULT_MB_DIR / "logs" / "inner-agent-telemetry.jsonl"
DEFAULT_COOLDOWN_FILE = DEFAULT_MB_DIR / "logs" / "scheduler-cooldown.txt"
DEFAULT_MAX_RUNS_PER_DAY = 8
DEFAULT_TIMEOUT_S = 7200
DEFAULT_SKIP_IF_RECENT_MIN = 45
# Rate-limit backoff: `claude_headless` tags auth/quota/429/overload as
# `error_kind="unavailable"`. When a run logs ≥ this many such cycles we've hit
# the Pro/Max rolling window — cool down rather than spin mechanical cycles. The
# window is ~5h; on expiry the next scheduled run auto-resumes (in_cooldown → None).
DEFAULT_COOLDOWN_AFTER = 2
DEFAULT_COOLDOWN_HOURS = 5.0

log = logging.getLogger("scheduled_cycle")

Runner = Callable[[list[str], int], int]


def _parse_iso(ts: str) -> dt.datetime | None:
    try:
        return dt.datetime.fromisoformat(ts.replace("Z", "+00:00"))
    except (ValueError, AttributeError):
        return None


def count_unavailable_since(telemetry: Path, since: dt.datetime) -> int:
    """Count telemetry rows with error_kind='unavailable' stamped at/after `since`.

    The rate-limit signal for the current run: callers pass the run's start time.
    """
    try:
        lines = telemetry.read_text().splitlines()
    except OSError:
        return 0
    n = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            r = json.loads(line)
        except ValueError:
            continue
        ts = _parse_iso(str(r.get("ts", "")))
        if ts is not None and ts >= since and r.get("llm_error_kind") == "unavailable":
            n += 1
    return n


def read_cooldown_until(cooldown_file: Path) -> dt.datetime | None:
    """The active cooldown deadline, or None if absent/unparseable."""
    try:
        return _parse_iso(cooldown_file.read_text().strip())
    except OSError:
        return None


def in_cooldown(cooldown_file: Path, *, now: dt.datetime) -> dt.datetime | None:
    """Return the deadline if we're still cooling down, else None (expired/absent)."""
    until = read_cooldown_until(cooldown_file)
    return until if (until is not None and now < until) else None


def set_cooldown(cooldown_file: Path, *, until: dt.datetime) -> None:
    try:
        cooldown_file.parent.mkdir(parents=True, exist_ok=True)
        cooldown_file.write_text(until.isoformat() + "\n")
    except OSError as e:
        log.warning("cooldown write failed: %s", e)


def clear_cooldown(cooldown_file: Path) -> None:
    cooldown_file.unlink(missing_ok=True)


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
    parser.add_argument("--telemetry", type=Path, default=DEFAULT_TELEMETRY)
    parser.add_argument("--cooldown-file", type=Path, default=DEFAULT_COOLDOWN_FILE)
    parser.add_argument("--cooldown-hours", type=float, default=DEFAULT_COOLDOWN_HOURS)
    parser.add_argument(
        "--cooldown-after",
        type=int,
        default=DEFAULT_COOLDOWN_AFTER,
        help="≥ this many 'unavailable' cycles in a run → cool down (0 disables).",
    )
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

    # Rate-limit cooldown: if a prior run hit the subscription window, skip until
    # it resets (clean exit; not counted as a run). Auto-resumes on expiry.
    if not args.dry_run:
        until = in_cooldown(args.cooldown_file, now=now)
        if until is not None:
            mins = (until - now).total_seconds() / 60.0
            log.info(
                "rate-limit cooldown active until %s (~%.0f min) — skipping (clean exit)",
                until.isoformat(),
                mins,
            )
            return 0

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
        # Rate-limit detection: count this run's 'unavailable' cycles. Trip the
        # cooldown if we saturated the window; clear it on a clean run so the next
        # saturation re-trips fresh.
        if args.cooldown_after > 0:
            unavail = count_unavailable_since(args.telemetry, start)
            if unavail >= args.cooldown_after:
                until = now + dt.timedelta(hours=args.cooldown_hours)
                set_cooldown(args.cooldown_file, until=until)
                log.warning(
                    "%d 'unavailable' cycles this run (≥ %d) — subscription window hit; "
                    "cooling down until %s",
                    unavail,
                    args.cooldown_after,
                    until.isoformat(),
                )
            else:
                clear_cooldown(args.cooldown_file)
    return rc if isinstance(rc, int) else 124  # 124 = conventional timeout code


if __name__ == "__main__":
    raise SystemExit(main())
