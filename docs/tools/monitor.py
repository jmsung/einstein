#!/usr/bin/env python3
"""monitor.py — autonomous-loop progress dashboard.

Reads `docs/agent/cycle-log.md` (and optionally `skill-library.md`) and
prints a quick status summary:

  - cumulative totals (cycles run, findings added, concepts added,
    author mix)
  - outcome distribution (conquered / improved / no-change / blocked /
    new-finding-no-improvement / scaffold-no-attempt / ...)
  - the last N cycles, one per line, for at-a-glance recent activity
  - problems touched across the whole log

Designed to be tailed under `/loop`, cron, or just invoked manually
between cycles to see what the autonomous loop has been doing.

Usage:
    uv run python docs/tools/monitor.py                # default: recent_n=10
    uv run python docs/tools/monitor.py --recent 5
    uv run python docs/tools/monitor.py --log docs/agent/cycle-log.md
"""
from __future__ import annotations

import argparse
import re
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
DEFAULT_LOG = _REPO / "docs" / "agent" / "cycle-log.md"


# ---------------- data model ----------------


@dataclass
class Cycle:
    cycle_id: int
    problem: str
    start_score: str
    end_score: str
    hours_raw: str
    compute: str
    wiki_citations: int
    findings_added: int
    concepts_added: int
    author_mix: dict[str, int]
    outcome: str
    notes: str


@dataclass
class Summary:
    total_cycles: int
    findings_added_total: int
    concepts_added_total: int
    outcome_counts: dict[str, int]
    author_mix_totals: dict[str, int]
    problems_touched: list[str]
    recent: list[Cycle]


# ---------------- parsing ----------------


# A cycle row starts with `| <integer> |` — the cycle id. Other table rows
# (the header `| # | problem | ...|` and any reference rows) won't match.
_ROW_RE = re.compile(r"^\|\s*(\d+)\s*\|")

_MIX_RE = re.compile(r"a:(\d+)/h:(\d+)/hyb:(\d+)")
_SCORE_PAIR_RE = re.compile(r"^(.+?)\s*(?:→|->|\(no Δ\))\s*(.+)$")


def _parse_int(s: str, default: int = 0) -> int:
    """Tolerant int parse — strips parens, finds the first integer."""
    m = re.search(r"-?\d+", s)
    if not m:
        return default
    try:
        return int(m.group(0))
    except ValueError:
        return default


def _parse_author_mix(cell: str) -> dict[str, int]:
    m = _MIX_RE.search(cell)
    if not m:
        return {"agent": 0, "human": 0, "hybrid": 0}
    return {
        "agent": int(m.group(1)),
        "human": int(m.group(2)),
        "hybrid": int(m.group(3)),
    }


def _parse_score_pair(cell: str) -> tuple[str, str]:
    cell = cell.strip()
    if "→" in cell:
        a, _, b = cell.partition("→")
        # Strip "(no Δ)" suffix if present
        b = re.sub(r"\(.*?\)", "", b).strip()
        return a.strip(), b.strip()
    if "(no Δ)" in cell:
        base = cell.replace("(no Δ)", "").strip()
        return base, base
    return cell, cell


def parse_cycle_log(path: Path) -> list[Cycle]:
    """Parse the cycle-log.md markdown table into Cycle records."""
    cycles: list[Cycle] = []
    for line in path.read_text().splitlines():
        if not _ROW_RE.match(line):
            continue
        # Split on '|' and trim cells; first and last entries are empty edges
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 11:
            continue
        try:
            cycle_id = int(cells[0])
        except ValueError:
            continue
        start_score, end_score = _parse_score_pair(cells[2])
        cycles.append(Cycle(
            cycle_id=cycle_id,
            problem=cells[1],
            start_score=start_score,
            end_score=end_score,
            hours_raw=cells[3],
            compute=cells[4],
            wiki_citations=_parse_int(cells[5]),
            findings_added=_parse_int(cells[6]),
            concepts_added=_parse_int(cells[7]),
            author_mix=_parse_author_mix(cells[8]),
            outcome=cells[9],
            notes=cells[10] if len(cells) > 10 else "",
        ))
    return cycles


# ---------------- summarize ----------------


def summarize(cycles: list[Cycle], *, recent_n: int = 10) -> Summary:
    outcome_counts: dict[str, int] = dict(Counter(c.outcome for c in cycles))
    mix_totals = {"agent": 0, "human": 0, "hybrid": 0}
    for c in cycles:
        for k in mix_totals:
            mix_totals[k] += c.author_mix.get(k, 0)
    problems_touched = sorted({c.problem for c in cycles})
    recent = cycles[-recent_n:] if cycles else []
    return Summary(
        total_cycles=len(cycles),
        findings_added_total=sum(c.findings_added for c in cycles),
        concepts_added_total=sum(c.concepts_added for c in cycles),
        outcome_counts=outcome_counts,
        author_mix_totals=mix_totals,
        problems_touched=problems_touched,
        recent=recent,
    )


# ---------------- render ----------------


def render(summary: Summary) -> str:
    lines: list[str] = []
    lines.append("=== Autonomous-loop monitor ===")
    lines.append("")
    lines.append("## Totals")
    lines.append(f"  cycles:           {summary.total_cycles}")
    lines.append(f"  findings added:   {summary.findings_added_total}")
    lines.append(f"  concepts added:   {summary.concepts_added_total}")
    lines.append(f"  author mix:       "
                 f"agent={summary.author_mix_totals['agent']}, "
                 f"human={summary.author_mix_totals['human']}, "
                 f"hybrid={summary.author_mix_totals['hybrid']}")
    lines.append(f"  problems touched: {len(summary.problems_touched)}")
    lines.append("")
    lines.append("## Outcomes")
    if summary.outcome_counts:
        # Sort by count descending
        for outcome, n in sorted(summary.outcome_counts.items(), key=lambda kv: -kv[1]):
            lines.append(f"  {outcome:<35} {n}")
    else:
        lines.append("  (no cycles)")
    lines.append("")
    lines.append(f"## Recent ({len(summary.recent)} cycle(s))")
    if summary.recent:
        for c in summary.recent:
            score = (f"{c.start_score} → {c.end_score}"
                     if c.start_score != c.end_score else c.start_score)
            lines.append(f"  #{c.cycle_id:>3}  {c.problem:<32}  {score:<32}  "
                         f"{c.outcome}")
    else:
        lines.append("  (none)")
    return "\n".join(lines)


# ---------------- CLI ----------------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--log", type=Path, default=DEFAULT_LOG)
    parser.add_argument("--recent", type=int, default=10,
                        help="Number of most-recent cycles to print (default 10).")
    args = parser.parse_args(argv)

    if not args.log.is_file():
        print(f"no cycle-log at {args.log}")
        return 1
    cycles = parse_cycle_log(args.log)
    summary = summarize(cycles, recent_n=args.recent)
    print(render(summary))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
