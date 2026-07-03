#!/usr/bin/env python3
"""inner_agent_gates.py — pre-cycle resource gates for the autonomous loop.

Goal 7.5 of `mb/active/feat-autonomous-loop.md`. Before every inner-agent
cycle, the orchestrator calls `precheck()` to confirm five conditions hold;
any single failure short-circuits the cycle into a skip with a reason.

  1. Kill switch off            — env `EINSTEIN_INNER_AGENT != "0"`
  2. No regression sentinel     — `mb/.inner-agent-disabled` missing
  3. Daily token budget not hit — today's row in `mb/logs/inner-agent-budget.md`
                                  under cap
  4. Network reachable          — HEAD on arxiv + arena under 5s
  5. the workstation not throttling      — `pmset -g therm` shows
                                  CPU_Speed_Limit == 100 (or no such line —
                                  meaning macOS hasn't recorded any thermal
                                  pressure)

Each check is its own pure-ish function so tests can drive them
individually. `precheck()` composes them in cheapest-first order so the
expensive network probe runs only if the local gates passed.

Companion ledger: `record_token_usage(budget_path, ...)` updates today's
row after a cycle completes. The ledger is markdown so the human can read
it; the parser only touches today's row.

NOT in scope here:
  - Per-cycle wall-clock cap — already on `claude_headless.run(timeout_seconds=N)`
  - Output-token cap — already on `claude -p --max-tokens` via headless wrapper
  - Input-token cap — enforced indirectly via prompt-budget caps in 7.1 inputs
"""

from __future__ import annotations

import datetime as dt
import logging
import os
import re
import subprocess
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path

log = logging.getLogger("inner_agent_gates")


# ---------------- defaults ----------------

KILL_SWITCH_ENV = "EINSTEIN_INNER_AGENT"
DEFAULT_DAILY_TOKEN_CAP = 5_000_000
DEFAULT_REACHABILITY_TIMEOUT_S = 5
DEFAULT_REACHABILITY_URLS = (
    "https://arxiv.org/",
    "https://einsteinarena.com/",
)
DEFAULT_THERMAL_CMD = ("pmset", "-g", "therm")


# ---------------- result types ----------------


@dataclass
class GateDecision:
    """Outcome of the precheck composite.

    `action`: "proceed" if cycles should run; "skip" if the visit must bail.
    `llm_enabled`: when True, the agent uses `claude -p`; when False, the
                   kill switch is active and the visit runs the mechanical
                   path (strategy_picker + optimizer_dispatch only).
    """

    action: str  # "proceed" | "skip"
    reason: str = ""
    llm_enabled: bool = True

    @property
    def proceed(self) -> bool:
        return self.action == "proceed"


# ---------------- individual checks ----------------


def is_kill_switch_set(env: dict[str, str] | os._Environ[str] | None = None) -> bool:
    """True iff `EINSTEIN_INNER_AGENT=0` is set in the environment.

    Any other value (including unset) means the kill switch is OFF.
    """
    e = env if env is not None else os.environ
    return e.get(KILL_SWITCH_ENV, "").strip() == "0"


def is_sentinel_present(sentinel_path: Path) -> bool:
    """True iff the regression-detect sentinel file exists.

    Goal 7.8 writes `mb/.inner-agent-disabled` on cycle_runner failure; a
    human `rm` re-enables the loop. The path itself is the signal — content
    is informational only.
    """
    return sentinel_path.is_file()


def write_sentinel(sentinel_path: Path, *, reason: str, cycle_id: int | None = None) -> Path:
    """Drop the regression-detect sentinel at `sentinel_path` (Goal 7.8c).

    The next cycle's `precheck()` will see it and skip until a human
    removes the file. Idempotent: re-writing rewrites the body but never
    raises on an existing file.

    Returns the path written.
    """
    sentinel_path.parent.mkdir(parents=True, exist_ok=True)
    cycle_blurb = f"cycle_id={cycle_id}\n" if cycle_id is not None else ""
    body = (
        "# Inner-agent disabled by regression-detect\n"
        f"timestamp: {dt.datetime.now().isoformat(timespec='seconds')}\n"
        f"{cycle_blurb}"
        f"reason: {reason}\n"
        "\n"
        "Remove this file (`rm`) to re-enable the autonomous loop.\n"
        "Review cycle-log + recent commits before doing so — the sentinel\n"
        "fired because cycle_runner.sh detected a hard regression\n"
        "(typically wiki_lint exiting non-zero).\n"
    )
    sentinel_path.write_text(body)
    return sentinel_path


def clear_sentinel(sentinel_path: Path) -> bool:
    """Remove the sentinel if present. Returns True iff a file was removed.

    Used by the human via `rm` directly; this Python entry point exists
    for tests + scripted recovery.
    """
    try:
        sentinel_path.unlink()
        return True
    except FileNotFoundError:
        return False


def is_reachable(url: str, timeout_s: int = DEFAULT_REACHABILITY_TIMEOUT_S) -> bool:
    """HEAD `url` with `timeout_s` seconds; True iff the request succeeds.

    Any HTTP response (even 4xx/5xx) means the host is reachable enough for
    our purposes — we just want to know the network isn't completely down.
    """
    try:
        req = urllib.request.Request(url, method="HEAD")
        with urllib.request.urlopen(req, timeout=timeout_s) as _resp:  # noqa: S310
            return True
    except urllib.error.HTTPError:
        # The server responded — that's reachable.
        return True
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        log.debug("reachability fail %s: %s", url, e)
        return False


def is_thermal_ok(
    cmd: tuple[str, ...] = DEFAULT_THERMAL_CMD,
    *,
    timeout_s: int = 3,
) -> tuple[bool, str]:
    """Run `pmset -g therm` and return (ok, detail).

    ok is False only when the output contains a `CPU_Speed_Limit` line with
    a value < 100. Absence of the line means macOS hasn't recorded thermal
    pressure → treat as ok. Missing `pmset` binary or non-macOS → ok (we
    can't tell, so don't block the loop).
    """
    try:
        out = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout_s,
            check=False,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired) as e:
        log.debug("thermal check unavailable (%s) — treating as ok", e)
        return True, "thermal-check-unavailable"
    return _parse_thermal_output(out.stdout + "\n" + out.stderr)


_THERMAL_LIMIT_RE = re.compile(r"CPU_Speed_Limit\s*=\s*(\d+)")


def _parse_thermal_output(text: str) -> tuple[bool, str]:
    m = _THERMAL_LIMIT_RE.search(text)
    if not m:
        return True, "no thermal pressure recorded"
    limit = int(m.group(1))
    if limit >= 100:
        return True, f"CPU_Speed_Limit={limit}"
    return False, f"CPU_Speed_Limit={limit} (throttled)"


# ---------------- budget ledger ----------------


_BUDGET_HEADER = (
    "# Inner-agent daily budget\n"
    "\n"
    "Tracked by `docs/tools/inner_agent_gates.py` (Goal 7.5). Per-cycle\n"
    "input + output token counts aggregated by local date. The autonomous\n"
    "loop's `precheck()` reads today's row and refuses to start a new\n"
    "cycle when total > cap.\n"
    "\n"
    "| date | input | output | total | cycles |\n"
    "|---|---|---|---|---|\n"
)

_ROW_RE = re.compile(
    r"^\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|" r"\s*(\d+)\s*\|\s*(\d+)\s*\|\s*$"
)


@dataclass
class BudgetRow:
    date: str  # ISO YYYY-MM-DD
    input: int
    output: int
    cycles: int

    @property
    def total(self) -> int:
        return self.input + self.output


def _today_iso(today: dt.date | None = None) -> str:
    return (today or dt.date.today()).isoformat()


def _parse_budget(text: str) -> dict[str, BudgetRow]:
    """Date → row. Lenient: ignores header / unrecognized lines."""
    rows: dict[str, BudgetRow] = {}
    for line in text.splitlines():
        m = _ROW_RE.match(line.strip())
        if not m:
            continue
        date, inp, out, _total, cyc = m.groups()
        rows[date] = BudgetRow(
            date=date,
            input=int(inp),
            output=int(out),
            cycles=int(cyc),
        )
    return rows


def read_today_total(
    budget_path: Path,
    *,
    today: dt.date | None = None,
) -> BudgetRow:
    """Return today's BudgetRow, creating a zero row if absent.

    Does NOT write — pure read. Use `record_token_usage` to mutate.
    """
    iso = _today_iso(today)
    if not budget_path.is_file():
        return BudgetRow(date=iso, input=0, output=0, cycles=0)
    rows = _parse_budget(budget_path.read_text())
    return rows.get(iso, BudgetRow(date=iso, input=0, output=0, cycles=0))


def is_under_budget(
    budget_path: Path,
    *,
    daily_cap: int = DEFAULT_DAILY_TOKEN_CAP,
    today: dt.date | None = None,
) -> tuple[bool, str]:
    """True iff today's total < daily_cap."""
    row = read_today_total(budget_path, today=today)
    ok = row.total < daily_cap
    detail = f"today={row.total} cap={daily_cap}"
    return ok, detail


def record_token_usage(
    budget_path: Path,
    *,
    input_tokens: int,
    output_tokens: int,
    today: dt.date | None = None,
) -> BudgetRow:
    """Add the given usage to today's row, creating header / file if needed.

    Returns the post-update BudgetRow. Idempotency is NOT guaranteed across
    parallel writers — the autonomous_loop's O_EXCL lockfile already
    serializes cycles so this is safe in practice.
    """
    # Diagnostic — see who is calling this so phantom double-counts can be
    # traced. Logs at INFO so the cycle's stderr captures it.
    log.info("record_token_usage: path=%s in=%d out=%d", budget_path, input_tokens, output_tokens)
    iso = _today_iso(today)
    rows: dict[str, BudgetRow]
    if budget_path.is_file():
        rows = _parse_budget(budget_path.read_text())
    else:
        budget_path.parent.mkdir(parents=True, exist_ok=True)
        rows = {}

    cur = rows.get(iso, BudgetRow(date=iso, input=0, output=0, cycles=0))
    updated = BudgetRow(
        date=iso,
        input=cur.input + input_tokens,
        output=cur.output + output_tokens,
        cycles=cur.cycles + 1,
    )
    rows[iso] = updated

    # Render: stable header + rows sorted by date (oldest first so today is
    # at the bottom and easy to read).
    out_lines = [_BUDGET_HEADER.rstrip("\n")]
    for date in sorted(rows.keys()):
        r = rows[date]
        out_lines.append(f"| {r.date} | {r.input} | {r.output} | {r.total} | {r.cycles} |")
    budget_path.write_text("\n".join(out_lines) + "\n")
    return updated


# ---------------- composite precheck ----------------


def precheck(
    *,
    budget_path: Path,
    sentinel_path: Path,
    env: dict[str, str] | os._Environ[str] | None = None,
    daily_cap: int = DEFAULT_DAILY_TOKEN_CAP,
    reachability_urls: tuple[str, ...] = DEFAULT_REACHABILITY_URLS,
    reachability_timeout_s: int = DEFAULT_REACHABILITY_TIMEOUT_S,
    skip_reachability: bool = False,
    skip_thermal: bool = False,
    thermal_cmd: tuple[str, ...] = DEFAULT_THERMAL_CMD,
    today: dt.date | None = None,
) -> GateDecision:
    """Compose the gates. Order: sentinel → kill-switch → LLM-only checks.

    - **Sentinel** (regression-detect, Goal 7.8) → skip *both* modes. Even
      the mechanical path is blocked because a sentinel means the last
      cycle broke something.
    - **Kill switch** → proceed but `llm_enabled=False`. The visit runs the
      mechanical path; LLM-only checks (budget, reach, thermal) are not
      relevant and are not run.
    - **LLM-only checks** (only when kill switch is OFF): budget under cap,
      arxiv + arena reachable, the workstation not throttling.

    `skip_reachability` / `skip_thermal` short-circuit the expensive checks
    for tests and CI.
    """
    if is_sentinel_present(sentinel_path):
        return GateDecision(
            "skip",
            f"sentinel present ({sentinel_path}) — regression-detect " f"requires human re-enable",
            llm_enabled=False,
        )

    if is_kill_switch_set(env):
        return GateDecision(
            "proceed",
            f"{KILL_SWITCH_ENV}=0 — mechanical path only",
            llm_enabled=False,
        )

    # LLM-mode checks below. These don't matter when running mechanically,
    # so they live after the kill-switch branch.

    under, detail = is_under_budget(
        budget_path,
        daily_cap=daily_cap,
        today=today,
    )
    if not under:
        return GateDecision(
            "skip",
            f"daily token budget hit — {detail}",
            llm_enabled=True,
        )

    if not skip_reachability:
        for url in reachability_urls:
            if not is_reachable(url, timeout_s=reachability_timeout_s):
                return GateDecision(
                    "skip",
                    f"unreachable: {url}",
                    llm_enabled=True,
                )

    if not skip_thermal:
        ok, detail = is_thermal_ok(thermal_cmd)
        if not ok:
            return GateDecision(
                "skip",
                f"thermal: {detail}",
                llm_enabled=True,
            )

    return GateDecision("proceed", llm_enabled=True)


# ---------------- CLI (Goal 7.8) ----------------


def _cli(argv: list[str] | None = None) -> int:
    """Shell-callable entry point for sentinel + budget operations.

    Usage:
        uv run python docs/tools/inner_agent_gates.py write-sentinel <path> --reason "..."
        uv run python docs/tools/inner_agent_gates.py clear-sentinel <path>
        uv run python docs/tools/inner_agent_gates.py budget <path>

    Designed for `cycle_runner.sh` (write-sentinel) and the human
    operator (clear-sentinel, budget).
    """
    import argparse

    p = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    sub = p.add_subparsers(dest="cmd", required=True)

    ps = sub.add_parser("write-sentinel", help="Drop the regression-detect sentinel.")
    ps.add_argument("path", type=Path)
    ps.add_argument(
        "--reason", required=True, help="One-line reason recorded in the sentinel body."
    )
    ps.add_argument("--cycle-id", type=int, default=None)

    pc = sub.add_parser("clear-sentinel", help="Remove the regression-detect sentinel.")
    pc.add_argument("path", type=Path)

    pb = sub.add_parser("budget", help="Print today's budget row from the ledger.")
    pb.add_argument("path", type=Path)

    args = p.parse_args(argv)

    if args.cmd == "write-sentinel":
        result_path = write_sentinel(
            args.path,
            reason=args.reason,
            cycle_id=args.cycle_id,
        )
        print(str(result_path))
        return 0

    if args.cmd == "clear-sentinel":
        removed = clear_sentinel(args.path)
        print("removed" if removed else "not-present")
        return 0 if removed else 1

    if args.cmd == "budget":
        row = read_today_total(args.path)
        print(
            f"date={row.date} input={row.input} output={row.output} "
            f"total={row.total} cycles={row.cycles}"
        )
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(_cli())
