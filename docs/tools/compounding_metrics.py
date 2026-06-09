#!/usr/bin/env python3
"""compounding_metrics.py — the "is the loop actually compounding?" scoreboard.

Phase 4 of `docs/agent/meta-learning-automation.md`. Computes the compounding
metrics the design names, cheaply, from artifacts the loop already writes:

- **time-to-record per problem** — cycles from first attempt to first record
  outcome (from `docs/agent/cycle-log.md`). ↓ over time = compounding.
- **technique hit-rate** — top3 / tried, from `docs/agent/skill-library.md`. ↑.
- **cite-reuse rate** — fraction of cycles (after the first to cite anything)
  that cite a source ALREADY cited in an earlier cycle. Direct evidence of
  compounding: a cycle standing on a prior cycle's reference. From
  `mb/logs/cited-sources.jsonl`.

The fourth design metric — **% cycles where recall preceded the winning move** —
is NOT computed here: it needs recall↔win correlation the current logs don't
capture honestly. We print it as `n/a (needs instrumentation)` rather than fake a
number — per the agent-stance "objective > subjective" rule.

`--write` splices the rendered block into `docs/agent/metrics.md` between the
`<!-- compounding:start -->` / `<!-- compounding:end -->` markers (added idempotently).

Usage::

    uv run python docs/tools/compounding_metrics.py            # print block
    uv run python docs/tools/compounding_metrics.py --write     # update metrics.md
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
DEFAULT_CYCLE_LOG = _REPO / "docs" / "agent" / "cycle-log.md"
DEFAULT_SKILL_LIBRARY = _REPO / "docs" / "agent" / "skill-library.md"
DEFAULT_CITED_SOURCES = _REPO.parent / "mb" / "logs" / "cited-sources.jsonl"
DEFAULT_METRICS = _REPO / "docs" / "agent" / "metrics.md"

START_MARKER = "<!-- compounding:start -->"
END_MARKER = "<!-- compounding:end -->"

# cycle-log rows are parsed by splitting on pipes (column index), which is more
# robust than one big regex against the 12-column schema.
_RECORD_OUTCOMES = {"improved-and-submitted", "conquered"}


# --------------------------------------------------------------- cycle-log


@dataclass
class CycleRow:
    cycle_id: int
    problem: str
    outcome: str


def parse_cycle_rows(text: str) -> list[CycleRow]:
    """Parse data rows from cycle-log.md. Skips header/separator rows."""
    rows: list[CycleRow] = []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cols = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cols) < 10:
            continue
        if not cols[0].isdigit():
            continue  # header / separator
        rows.append(CycleRow(cycle_id=int(cols[0]), problem=cols[1], outcome=cols[9]))
    return rows


def time_to_record(rows: list[CycleRow]) -> dict[str, int]:
    """Per problem: cycles from its first row to its first record outcome
    (inclusive). Only problems that reached a record appear."""
    first_seen: dict[str, int] = {}
    seq: dict[str, int] = {}  # per-problem attempt counter
    ttr: dict[str, int] = {}
    for r in rows:
        seq[r.problem] = seq.get(r.problem, 0) + 1
        first_seen.setdefault(r.problem, seq[r.problem])
        if r.problem not in ttr and r.outcome in _RECORD_OUTCOMES:
            ttr[r.problem] = seq[r.problem]
    return ttr


# --------------------------------------------------------------- skill-library


def technique_hit_rate(text: str) -> dict[str, tuple[int, int]]:
    """Map technique → (top3, tried) parsed from skill-library.md data rows.

    The live schema is positional:
    `| technique | category | tried | top3 | finding | last_used | hit_rate |`.
    Data rows carry bare numbers (no labels), so we read by column index. The
    header is located by name to find the `tried`/`top3` columns; falls back to
    the canonical indices (2, 3) if no header is found.
    """
    tried_i, top3_i = 2, 3
    rows: list[list[str]] = []
    for line in text.splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cols = [c.strip().strip("`") for c in line.strip().strip("|").split("|")]
        lowered = [c.lower() for c in cols]
        if "tried" in lowered and "top3" in lowered:
            tried_i, top3_i = lowered.index("tried"), lowered.index("top3")
            continue
        if all(set(c) <= set("-: ") for c in cols):
            continue  # separator row
        rows.append(cols)

    out: dict[str, tuple[int, int]] = {}
    for cols in rows:
        if len(cols) <= max(tried_i, top3_i):
            continue
        name = cols[0]
        if not name or name.lower() in {"technique", "skill", "name"}:
            continue
        if not (cols[tried_i].isdigit() and cols[top3_i].isdigit()):
            continue
        out[name] = (int(cols[top3_i]), int(cols[tried_i]))
    return out


def overall_hit_rate(hr: dict[str, tuple[int, int]]) -> float | None:
    total_top3 = sum(t for t, _ in hr.values())
    total_tried = sum(n for _, n in hr.values())
    return (total_top3 / total_tried) if total_tried else None


# --------------------------------------------------------------- cite-reuse


def cite_reuse_rate(records: list[dict]) -> tuple[float | None, int, int]:
    """Fraction of *eligible* cycles that cite a source already cited in an
    earlier cycle. Eligible = cycles after the first that cited anything.

    Returns (rate_or_None, reuse_cycles, eligible_cycles).
    """
    seen: set[str] = set()
    eligible = 0
    reuse = 0
    first_citing_passed = False
    for rec in records:
        cited = rec.get("cited_sources") or []
        if not cited:
            continue
        if not first_citing_passed:
            # First cycle that cites anything establishes the baseline.
            first_citing_passed = True
            seen.update(cited)
            continue
        eligible += 1
        if any(c in seen for c in cited):
            reuse += 1
        seen.update(cited)
    rate = (reuse / eligible) if eligible else None
    return rate, reuse, eligible


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    out: list[dict] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return out


# --------------------------------------------------------------- render


def render_block(
    *,
    cycle_log: Path = DEFAULT_CYCLE_LOG,
    skill_library: Path = DEFAULT_SKILL_LIBRARY,
    cited_sources: Path = DEFAULT_CITED_SOURCES,
) -> str:
    rows = parse_cycle_rows(cycle_log.read_text()) if cycle_log.exists() else []
    ttr = time_to_record(rows)
    hr = technique_hit_rate(skill_library.read_text()) if skill_library.exists() else {}
    rate, reuse, eligible = cite_reuse_rate(load_jsonl(cited_sources))

    median_ttr = _median(sorted(ttr.values())) if ttr else None
    ohr = overall_hit_rate(hr)

    lines = [
        START_MARKER,
        "## Compounding metrics (auto — Phase 4)",
        "",
        "_Computed by `docs/tools/compounding_metrics.py`. The signal of a loop that "
        "compounds, not just runs._",
        "",
        "| Metric | Value | Reading |",
        "|---|---|---|",
        f"| Records achieved | {len(ttr)} | problems that reached a record |",
        f"| Median time-to-record | {_fmt(median_ttr)} cycles | ↓ over time = compounding |",
        f"| Technique hit-rate (top3/tried) | {_fmt_pct(ohr)} | ↑ = picks getting better |",
        f"| Cite-reuse rate | {_fmt_pct(rate)} ({reuse}/{eligible}) | ↑ = cycles standing on prior cites |",
        "| % cycles recall-preceded-win | n/a (needs instrumentation) | honest gap — not faked |",
        "",
        END_MARKER,
    ]
    return "\n".join(lines)


def _median(xs: list[int]) -> float:
    n = len(xs)
    mid = n // 2
    return float(xs[mid]) if n % 2 else (xs[mid - 1] + xs[mid]) / 2


def _fmt(x: float | None) -> str:
    return "n/a" if x is None else (f"{x:.0f}" if float(x).is_integer() else f"{x:.1f}")


def _fmt_pct(x: float | None) -> str:
    return "n/a" if x is None else f"{x * 100:.0f}%"


def write_block(metrics: Path, block: str) -> None:
    """Idempotently splice `block` into metrics between the markers; append if absent."""
    text = metrics.read_text() if metrics.exists() else "# Metrics\n"
    if START_MARKER in text and END_MARKER in text:
        # Replacement via a function so `block` is treated literally — a metric
        # value containing a backslash would otherwise be read as a re escape.
        text = re.sub(
            re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER),
            lambda _m: block,
            text,
            flags=re.DOTALL,
        )
    else:
        text = text.rstrip() + "\n\n" + block + "\n"
    metrics.write_text(text)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    p.add_argument("--cycle-log", type=Path, default=DEFAULT_CYCLE_LOG)
    p.add_argument("--skill-library", type=Path, default=DEFAULT_SKILL_LIBRARY)
    p.add_argument("--cited-sources", type=Path, default=DEFAULT_CITED_SOURCES)
    p.add_argument("--metrics", type=Path, default=DEFAULT_METRICS)
    p.add_argument("--write", action="store_true", help="splice into metrics.md")
    args = p.parse_args(argv)
    block = render_block(
        cycle_log=args.cycle_log,
        skill_library=args.skill_library,
        cited_sources=args.cited_sources,
    )
    if args.write:
        write_block(args.metrics, block)
        print(f"wrote compounding block to {args.metrics}")
    else:
        print(block)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
