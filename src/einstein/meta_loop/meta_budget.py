"""meta_loop.meta_budget — separate token-budget ledger for the meta-loop.

Distinct from `mb/logs/inner-agent-budget.md` (handled by
`docs/tools/inner_agent_budget.py`). The meta-loop runs much less
frequently than the inner loop; an independent ledger makes its compute
visible and prevents the two budgets from being confused.

Per HyperAgents (Zhang et al. 2026), one of the emergent meta-improvements
their DGM-H discovered was *compute-aware iteration budgeting* — a
separate per-loop ledger is the structural enabling primitive.

Format mirrors inner-agent-budget.md for operator familiarity:

    | date | input | output | total | runs |
    |---|---|---|---|---|
    | 2026-05-25 | 8400 | 320 | 8720 | 1 |

`runs` counts propose() invocations (not proposals — one propose call
may emit 0..3 proposals).
"""

from __future__ import annotations

import datetime as dt
import re
from dataclasses import dataclass
from pathlib import Path

_HEADER = (
    "# meta-loop daily budget\n\n"
    "Per-day token usage for the meta-loop's agentic proposer (Goal 2).\n"
    "Separate from `inner-agent-budget.md` — see meta_loop.meta_budget.\n\n"
    "| date | input | output | total | runs |\n"
    "|---|---|---|---|---|\n"
)


@dataclass
class BudgetRow:
    date: dt.date
    input: int
    output: int
    runs: int

    @property
    def total(self) -> int:
        return self.input + self.output


# Match data rows: `| YYYY-MM-DD | <int> | <int> | <int> | <int> |`
_ROW_RE = re.compile(
    r"^\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|"
)


def _parse(text: str) -> dict[dt.date, BudgetRow]:
    rows: dict[dt.date, BudgetRow] = {}
    for line in text.splitlines():
        m = _ROW_RE.match(line)
        if not m:
            continue
        try:
            d = dt.date.fromisoformat(m.group(1))
        except ValueError:
            continue
        rows[d] = BudgetRow(
            date=d,
            input=int(m.group(2)),
            output=int(m.group(3)),
            runs=int(m.group(5)),
        )
    return rows


def _render(rows: dict[dt.date, BudgetRow]) -> str:
    out = _HEADER
    for d in sorted(rows.keys()):
        r = rows[d]
        out += f"| {r.date} | {r.input} | {r.output} | {r.total} | {r.runs} |\n"
    return out


def read_today(path: Path, *, today: dt.date | None = None) -> BudgetRow:
    """Return today's row (zeroed if not yet present)."""
    today = today or dt.date.today()
    if not path.is_file():
        return BudgetRow(date=today, input=0, output=0, runs=0)
    rows = _parse(path.read_text())
    return rows.get(today, BudgetRow(date=today, input=0, output=0, runs=0))


def record(
    path: Path,
    *,
    input_tokens: int,
    output_tokens: int,
    today: dt.date | None = None,
) -> BudgetRow:
    """Add one run's tokens to today's row. Creates the file if absent.

    Returns the updated row.
    """
    if input_tokens < 0 or output_tokens < 0:
        raise ValueError("token counts must be non-negative")

    today = today or dt.date.today()
    path.parent.mkdir(parents=True, exist_ok=True)

    rows = _parse(path.read_text()) if path.is_file() else {}
    cur = rows.get(today, BudgetRow(date=today, input=0, output=0, runs=0))
    updated = BudgetRow(
        date=today,
        input=cur.input + input_tokens,
        output=cur.output + output_tokens,
        runs=cur.runs + 1,
    )
    rows[today] = updated
    path.write_text(_render(rows))
    return updated


def read_all(path: Path) -> list[BudgetRow]:
    if not path.is_file():
        return []
    return [v for _, v in sorted(_parse(path.read_text()).items())]


__all__ = [
    "BudgetRow",
    "read_all",
    "read_today",
    "record",
]
