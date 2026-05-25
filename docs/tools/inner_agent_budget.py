#!/usr/bin/env python3
"""inner_agent_budget.py — CLI for inspecting + adjusting the daily ledger.

Goal 7.8d. Thin wrapper over `inner_agent_gates`'s budget API so operators
can ask "where's today at?" or "reset today's row" without launching a
Python REPL.

The ledger itself is `mb/logs/inner-agent-budget.md` — markdown that humans can
read directly. This CLI is for ergonomic shell use:

    uv run python docs/tools/inner_agent_budget.py show           # today only
    uv run python docs/tools/inner_agent_budget.py show --all     # every day
    uv run python docs/tools/inner_agent_budget.py record \
        --input 10000 --output 2500                               # manual add
    uv run python docs/tools/inner_agent_budget.py reset 2026-05-24
                                                                  # zero a day

"Rollover at local midnight" is implicit: `record_token_usage` keys by
`datetime.date.today()`. There's no scheduled job — the next cycle's record
call writes the new day's row automatically.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
DEFAULT_BUDGET_PATH = _REPO.parent / "mb" / "logs" / "inner-agent-budget.md"

sys.path.insert(0, str(Path(__file__).resolve().parent))
import inner_agent_gates as iag  # noqa: E402

# ---------------- helpers ----------------


def _format_row(row: iag.BudgetRow, *, cap: int | None = None) -> str:
    pct = ""
    if cap is not None and cap > 0:
        pct = f"  ({100 * row.total / cap:.1f}% of {cap})"
    return (
        f"{row.date}  in={row.input:>10}  out={row.output:>10}  "
        f"total={row.total:>10}  cycles={row.cycles:>4}{pct}"
    )


# ---------------- commands ----------------


def cmd_show(args: argparse.Namespace) -> int:
    if not args.all:
        row = iag.read_today_total(args.path)
        print(_format_row(row, cap=args.cap))
        return 0

    if not args.path.is_file():
        print(f"(no ledger at {args.path})")
        return 0

    text = args.path.read_text()
    rows = iag._parse_budget(text)
    if not rows:
        print(f"(empty ledger at {args.path})")
        return 0
    for date in sorted(rows.keys()):
        print(_format_row(rows[date], cap=args.cap))
    return 0


def cmd_record(args: argparse.Namespace) -> int:
    if args.input < 0 or args.output < 0:
        print("error: token counts must be non-negative", file=sys.stderr)
        return 2
    row = iag.record_token_usage(
        args.path,
        input_tokens=args.input,
        output_tokens=args.output,
    )
    print(_format_row(row, cap=args.cap))
    return 0


_ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def cmd_reset(args: argparse.Namespace) -> int:
    """Zero out the row for `args.date`. Re-writes the ledger preserving other rows."""
    if not _ISO_DATE_RE.match(args.date):
        print(f"error: date must be YYYY-MM-DD; got {args.date!r}", file=sys.stderr)
        return 2
    if not args.path.is_file():
        print(f"(no ledger at {args.path} — nothing to reset)")
        return 0
    rows = iag._parse_budget(args.path.read_text())
    if args.date not in rows:
        print(f"(no row for {args.date} — nothing to reset)")
        return 0
    rows[args.date] = iag.BudgetRow(
        date=args.date,
        input=0,
        output=0,
        cycles=0,
    )
    # Re-write the ledger from header + sorted rows
    lines = [iag._BUDGET_HEADER.rstrip("\n")]
    for date in sorted(rows.keys()):
        r = rows[date]
        lines.append(f"| {r.date} | {r.input} | {r.output} | {r.total} | {r.cycles} |")
    args.path.write_text("\n".join(lines) + "\n")
    print(f"reset {args.date} → 0/0/0/0")
    return 0


# ---------------- CLI ----------------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument(
        "--path",
        type=Path,
        default=DEFAULT_BUDGET_PATH,
        help=f"Ledger path (default {DEFAULT_BUDGET_PATH}).",
    )
    parser.add_argument(
        "--cap",
        type=int,
        default=iag.DEFAULT_DAILY_TOKEN_CAP,
        help="Daily token cap (for the percent-of-cap display column).",
    )

    sub = parser.add_subparsers(dest="cmd", required=True)
    ps = sub.add_parser("show", help="Show today (or --all rows).")
    ps.add_argument(
        "--all", action="store_true", help="Show every recorded day instead of just today."
    )
    ps.set_defaults(func=cmd_show)

    pr = sub.add_parser("record", help="Manually add a record.")
    pr.add_argument("--input", type=int, required=True)
    pr.add_argument("--output", type=int, required=True)
    pr.set_defaults(func=cmd_record)

    px = sub.add_parser("reset", help="Zero out one day's row.")
    px.add_argument("date", help="YYYY-MM-DD")
    px.set_defaults(func=cmd_reset)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
