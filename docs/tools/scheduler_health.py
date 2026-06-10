#!/usr/bin/env python3
"""scheduler_health.py — health monitor for the unattended loop (Phase 3 Goal 4).

Mirrors the prior autonomous-record-campaign monitor, but for the *scheduled*
loop: instead of summarizing cycle outcomes (that's `monitor.py`), this reads
the operational ledgers and answers one question — **is the unattended loop
healthy right now?** — with reasons and a cron-friendly exit code.

Checks (each maps to a readiness criterion or scheduler guard):

- **runs ledger** (`mb/logs/scheduler-runs.log`, written by scheduled_cycle):
  last real run not older than `--max-age-hours` (cadence watchdog), and no
  `--max-consecutive-failures` streak of non-zero exits. Exit 75 (lock held,
  EX_TEMPFAIL) is benign and ignored on both checks.
- **telemetry** (`mb/logs/inner-agent-telemetry.jsonl`): trailing-window
  fallback rate ≤ R2's 0.20, and no single cycle above the runaway-cost
  ceiling (R5's $5 default). Missing telemetry is informational, not an
  alert (fresh deploy).
- **sentinel** (`mb/.inner-agent-disabled`): presence means the loop is
  self-disabled and a human hasn't noticed — alert.

Exit codes: 0 = HEALTHY, 1 = UNHEALTHY (reasons printed). Designed to be
cron'd alongside the loop (see docs/agent/unattended-runbook.md):

    uv run python docs/tools/scheduler_health.py || <notify>
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
DEFAULT_MB_DIR = _REPO.parent / "mb"
DEFAULT_RUNS_LEDGER = DEFAULT_MB_DIR / "logs" / "scheduler-runs.log"
DEFAULT_TELEMETRY = DEFAULT_MB_DIR / "logs" / "inner-agent-telemetry.jsonl"
DEFAULT_SENTINEL = DEFAULT_MB_DIR / ".inner-agent-disabled"

DEFAULT_MAX_AGE_HOURS = 6
DEFAULT_MAX_CONSECUTIVE_FAILURES = 3
DEFAULT_MAX_FALLBACK_RATE = 0.20  # R2
DEFAULT_MAX_COST_USD = 5.0  # R5 runaway ceiling
DEFAULT_TELEMETRY_WINDOW = 50

_RUN_RE = re.compile(r"^(\S+)\s+exit=(\S+)\s+dur=")
_BENIGN_EXITS = {"0", "75"}  # 75 = EX_TEMPFAIL (lock held; cron retries)


def _parse_iso(ts: str) -> dt.datetime | None:
    try:
        return dt.datetime.fromisoformat(ts.replace("Z", "+00:00"))
    except ValueError:
        return None


def check_runs(
    ledger: Path,
    *,
    now_iso: str,
    max_age_hours: float,
    max_consecutive_failures: int,
) -> list[str]:
    """Cadence watchdog + failure-streak detector over the runs ledger."""
    try:
        lines = [ln for ln in ledger.read_text().splitlines() if ln.strip()]
    except OSError:
        return ["no scheduler runs ledger — loop has never run (or wrong path)"]
    parsed = [m for ln in lines if (m := _RUN_RE.match(ln))]
    if not parsed:
        return ["no scheduler runs ledger — loop has never run (or wrong path)"]

    issues: list[str] = []
    now = _parse_iso(now_iso)
    last_ts = _parse_iso(parsed[-1].group(1))
    if now is not None and last_ts is not None:
        age_h = (now - last_ts).total_seconds() / 3600.0
        if age_h > max_age_hours:
            issues.append(
                f"stale: last run {age_h:.1f}h ago (> {max_age_hours}h) — cadence broken?"
            )

    streak = 0
    for m in reversed(parsed):
        if m.group(2) in _BENIGN_EXITS:
            break
        streak += 1
    if streak >= max_consecutive_failures:
        issues.append(
            f"{streak} consecutive failed runs (≥ {max_consecutive_failures}) — "
            "check scheduler.log + telemetry error kinds"
        )
    return issues


def check_telemetry(
    telemetry: Path,
    *,
    window: int,
    max_fallback_rate: float,
    max_cost_usd: float,
) -> list[str]:
    """R2 fallback-rate + R5 runaway-cost over the trailing telemetry window."""
    try:
        lines = [ln for ln in telemetry.read_text().splitlines() if ln.strip()]
    except OSError:
        return []  # fresh deploy — informational, not an alert
    records = []
    for ln in lines[-window:]:
        try:
            records.append(json.loads(ln))
        except ValueError:
            continue
    if not records:
        return []

    issues: list[str] = []
    fallbacks = sum(1 for r in records if r.get("path_taken") == "fallback")
    rate = fallbacks / len(records)
    if rate > max_fallback_rate:
        issues.append(
            f"fallback rate {rate:.2f} over last {len(records)} cycles "
            f"(> R2 bar {max_fallback_rate:.2f})"
        )
    worst = max((float(r.get("cost_usd", 0.0)) for r in records), default=0.0)
    if worst > max_cost_usd:
        issues.append(f"cycle cost ${worst:.2f} exceeded runaway ceiling ${max_cost_usd:.2f}")
    return issues


def check_sentinel(sentinel: Path) -> list[str]:
    if sentinel.exists():
        return [
            f"sentinel present ({sentinel.name}) — loop self-disabled; "
            "investigate then remove the file to re-enable"
        ]
    return []


def main(argv: list[str] | None = None, *, now_iso: str | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--runs-ledger", type=Path, default=DEFAULT_RUNS_LEDGER)
    parser.add_argument("--telemetry", type=Path, default=DEFAULT_TELEMETRY)
    parser.add_argument("--sentinel", type=Path, default=DEFAULT_SENTINEL)
    parser.add_argument("--max-age-hours", type=float, default=DEFAULT_MAX_AGE_HOURS)
    parser.add_argument(
        "--max-consecutive-failures", type=int, default=DEFAULT_MAX_CONSECUTIVE_FAILURES
    )
    parser.add_argument("--max-fallback-rate", type=float, default=DEFAULT_MAX_FALLBACK_RATE)
    parser.add_argument("--max-cost-usd", type=float, default=DEFAULT_MAX_COST_USD)
    parser.add_argument("--window", type=int, default=DEFAULT_TELEMETRY_WINDOW)
    args = parser.parse_args(argv)

    if now_iso is None:
        now_iso = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    issues = (
        check_runs(
            args.runs_ledger,
            now_iso=now_iso,
            max_age_hours=args.max_age_hours,
            max_consecutive_failures=args.max_consecutive_failures,
        )
        + check_telemetry(
            args.telemetry,
            window=args.window,
            max_fallback_rate=args.max_fallback_rate,
            max_cost_usd=args.max_cost_usd,
        )
        + check_sentinel(args.sentinel)
    )

    if issues:
        print(f"UNHEALTHY ({len(issues)} issue(s)) as of {now_iso}:")
        for i in issues:
            print(f"  - {i}")
        return 1
    print(f"HEALTHY as of {now_iso}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
