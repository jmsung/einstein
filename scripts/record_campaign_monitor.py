#!/usr/bin/env python3
"""record_campaign_monitor.py — health monitor for the autonomous record campaign.

Reads the three signals the 24/7 loop emits and raises an alert (macOS
notification via ``docs/tools/notify_milestone.py``) when any of these fire:

  (a) **triple-verify mismatch** — a genuine evaluator disagreement (axiom A1).
      Source: ``mb/logs/auto-submit.md`` rows whose reason names a triple-verify
      failure that is NOT the "not yet wired" placeholder, OR the regression
      sentinel ``mb/.inner-agent-disabled`` being present (the loop already
      tripped its own kill switch).
  (b) **≥5 dispatch failures in a row on the same problem** — a problem the loop
      cannot make progress on. Source: consecutive ``outcome: blocked`` rows for
      the same problem in ``docs/agent/cycle-log.md``.
  (c) **auto-submit rate exceeds the daily cap** — more ``submitted`` rows today
      than the cap (axioms gate 4, default 5). Source: ``mb/logs/auto-submit.md``.

Each detector is a pure function over log *text* so it is unit-testable without
touching the filesystem. ``main()`` wires the real paths, runs the checks, fires
a notification per alert, and exits non-zero if any alert fired (so cron/launchd
surface the failure).

Usage:
    uv run python scripts/record_campaign_monitor.py            # check + notify
    uv run python scripts/record_campaign_monitor.py --quiet    # exit code only
    uv run python scripts/record_campaign_monitor.py --cap 3 --dispatch-threshold 4
"""

from __future__ import annotations

import argparse
import importlib.util
import logging
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

log = logging.getLogger("record_campaign_monitor")

_REPO = Path(__file__).resolve().parents[1]
_MB = _REPO.parent / "mb"
DEFAULT_AUTO_SUBMIT = _MB / "logs" / "auto-submit.md"
DEFAULT_CYCLE_LOG = _REPO / "docs" / "agent" / "cycle-log.md"
DEFAULT_SENTINEL = _MB / ".inner-agent-disabled"
DEFAULT_DAILY_CAP = 5
DEFAULT_DISPATCH_THRESHOLD = 5


@dataclass
class Alert:
    kind: str  # "triple-verify" | "dispatch-failures" | "auto-submit-rate"
    severity: str  # "critical" | "warning"
    message: str
    detail: dict = field(default_factory=dict)


# ---------------- markdown table parsing ----------------


def _table_rows(text: str) -> list[list[str]]:
    """Yield cell-lists for every pipe-table data row (skips header + separator).

    A data row is any line starting with ``|`` whose first cell is not a header
    label and which is not the ``|---|`` separator.
    """
    rows: list[list[str]] = []
    for line in text.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if not cells:
            continue
        joined = "".join(cells)
        if set(joined) <= set("-: "):  # separator row like |---|---|
            continue
        rows.append(cells)
    return rows


_AUTO_SUBMIT_COLS = (
    "timestamp_utc",
    "problem_id",
    "score",
    "decision",
    "reason",
    "http_status",
    "arena_id",
)


def parse_auto_submit_rows(text: str) -> list[dict]:
    """Parse ``auto-submit.md`` into dicts keyed by the 7 audit columns.

    Header and separator rows are skipped; the literal header row (first cell
    ``timestamp_utc``) is detected and dropped.
    """
    out: list[dict] = []
    for cells in _table_rows(text):
        if cells[0] == "timestamp_utc":  # header
            continue
        if len(cells) < len(_AUTO_SUBMIT_COLS):
            continue
        out.append(dict(zip(_AUTO_SUBMIT_COLS, cells)))
    return out


def parse_cycle_outcomes(text: str) -> list[tuple[str, str]]:
    """Return ``[(problem, outcome), ...]`` in cycle order from the cycle log.

    The cycle-log schema puts ``problem`` in column 2 and ``outcome`` in the
    second-to-last column (``notes`` is last). Header rows (first cell ``#``)
    are skipped.
    """
    out: list[tuple[str, str]] = []
    for cells in _table_rows(text):
        if cells[0] in {"#", "Column"}:  # header rows
            continue
        if len(cells) < 4:
            continue
        problem = cells[1]
        outcome = cells[-2]
        out.append((problem, outcome))
    return out


# ---------------- detectors ----------------


# Markers that identify a triple-verify-failed row as a scaffold/test artifact
# rather than a genuine 2-way numeric disagreement (axiom A1). A safety monitor
# must not cry wolf on these every 30 min, or alert fatigue defeats it. Keep
# this list honest — a real mismatch reason should NOT match any of these.
_TV_PLACEHOLDERS = ("not yet wired", "not_yet_wired", "synthetic", "placeholder", "scaffold")


def _is_genuine_triple_verify_failure(reason: str) -> bool:
    r = reason.lower()
    names_tv = "triple-verify" in r or "triple_verify" in r
    placeholder = any(m in r for m in _TV_PLACEHOLDERS)
    return names_tv and not placeholder


def check_triple_verify(rows: list[dict], *, sentinel_present: bool) -> list[Alert]:
    """Alert on a genuine triple-verify disagreement or a tripped sentinel."""
    alerts: list[Alert] = []
    if sentinel_present:
        alerts.append(
            Alert(
                kind="triple-verify",
                severity="critical",
                message="regression sentinel mb/.inner-agent-disabled is present — loop self-disabled",
                detail={"source": "sentinel"},
            )
        )
    bad = [r for r in rows if _is_genuine_triple_verify_failure(r.get("reason", ""))]
    if bad:
        last = bad[-1]
        alerts.append(
            Alert(
                kind="triple-verify",
                severity="critical",
                message=(
                    f"triple-verify mismatch on P{last.get('problem_id', '?')}: "
                    f"{last.get('reason', '')[:160]}"
                ),
                detail={"count": len(bad), "rows": bad},
            )
        )
    return alerts


def check_dispatch_failures(
    outcomes: list[tuple[str, str]], *, threshold: int = DEFAULT_DISPATCH_THRESHOLD
) -> list[Alert]:
    """Alert when a problem accrues ``threshold`` consecutive ``blocked`` cycles.

    "Consecutive" is over the cycle order; a cycle on a different problem resets
    the run for the prior problem.
    """
    alerts: list[Alert] = []
    run_problem: str | None = None
    run_len = 0
    fired: set[str] = set()
    for problem, outcome in outcomes:
        if outcome == "blocked":
            if problem == run_problem:
                run_len += 1
            else:
                run_problem, run_len = problem, 1
        else:
            run_problem, run_len = None, 0
        if run_problem and run_len >= threshold and run_problem not in fired:
            fired.add(run_problem)
            alerts.append(
                Alert(
                    kind="dispatch-failures",
                    severity="warning",
                    message=f"{run_problem}: {run_len} consecutive blocked cycles (≥{threshold})",
                    detail={"problem": run_problem, "run": run_len},
                )
            )
    return alerts


def count_submitted_today(rows: list[dict], *, today: str) -> int:
    return sum(
        1
        for r in rows
        if r.get("decision") == "submitted" and r.get("timestamp_utc", "").startswith(today)
    )


def check_auto_submit_rate(
    rows: list[dict], *, today: str, cap: int = DEFAULT_DAILY_CAP
) -> list[Alert]:
    """Alert when today's ``submitted`` count exceeds the daily cap."""
    n = count_submitted_today(rows, today=today)
    if n > cap:
        return [
            Alert(
                kind="auto-submit-rate",
                severity="warning",
                message=f"auto-submit rate {n} exceeds daily cap {cap} (UTC {today})",
                detail={"count": n, "cap": cap, "date": today},
            )
        ]
    return []


def run_checks(
    *,
    auto_submit_text: str,
    cycle_text: str,
    sentinel_present: bool,
    today: str,
    cap: int = DEFAULT_DAILY_CAP,
    dispatch_threshold: int = DEFAULT_DISPATCH_THRESHOLD,
) -> list[Alert]:
    """Run all three detectors and return the combined alert list."""
    rows = parse_auto_submit_rows(auto_submit_text)
    outcomes = parse_cycle_outcomes(cycle_text)
    alerts: list[Alert] = []
    alerts += check_triple_verify(rows, sentinel_present=sentinel_present)
    alerts += check_dispatch_failures(outcomes, threshold=dispatch_threshold)
    alerts += check_auto_submit_rate(rows, today=today, cap=cap)
    return alerts


# ---------------- notification side effect ----------------


def _load_notify():
    """Import notify_milestone.py by path (docs/tools is not a package)."""
    path = _REPO / "docs" / "tools" / "notify_milestone.py"
    spec = importlib.util.spec_from_file_location("notify_milestone", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def fire_alerts(alerts: list[Alert], *, runner=None) -> None:
    """Fire one macOS notification per alert via notify_milestone.notify.

    ``runner`` is the subprocess seam (passed through to ``notify``) so tests can
    assert without spawning ``osascript``.
    """
    if not alerts:
        return
    notify = _load_notify()
    for a in alerts:
        notify.notify(
            title=f"Record campaign — {a.kind} ({a.severity})",
            message=a.message,
            subtitle="record_campaign_monitor",
            runner=runner,
        )


def _read(path: Path) -> str:
    try:
        return path.read_text()
    except FileNotFoundError:
        return ""


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    p = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    p.add_argument("--auto-submit", type=Path, default=DEFAULT_AUTO_SUBMIT)
    p.add_argument("--cycle-log", type=Path, default=DEFAULT_CYCLE_LOG)
    p.add_argument("--sentinel", type=Path, default=DEFAULT_SENTINEL)
    p.add_argument("--cap", type=int, default=DEFAULT_DAILY_CAP)
    p.add_argument("--dispatch-threshold", type=int, default=DEFAULT_DISPATCH_THRESHOLD)
    p.add_argument(
        "--quiet", action="store_true", help="Do not fire notifications; exit code only."
    )
    args = p.parse_args(argv)

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    alerts = run_checks(
        auto_submit_text=_read(args.auto_submit),
        cycle_text=_read(args.cycle_log),
        sentinel_present=args.sentinel.is_file(),
        today=today,
        cap=args.cap,
        dispatch_threshold=args.dispatch_threshold,
    )

    if not alerts:
        log.info("record-campaign monitor: all clear (UTC %s)", today)
        return 0

    for a in alerts:
        log.warning("[%s/%s] %s", a.kind, a.severity, a.message)
    if not args.quiet:
        fire_alerts(alerts)
    return 1


if __name__ == "__main__":
    sys.exit(main())
