#!/usr/bin/env python3
"""promotion_candidates.py — surface source/ pages cited ≥N times cross-cycle.

Goal 4 of `js/feat/research-synthesis`. Reads the per-cycle citation sidecar
(`mb/logs/cited-sources.jsonl`), counts citations per `docs/source/<file>.md`
path, and writes `mb/logs/promotion-candidates.md` listing any path that
crossed the threshold (default 3 distinct cycles).

The human reviews the candidates file and decides which sources to promote to
`docs/wiki/concepts/<file>.md` (per `.claude/rules/wiki-attribution.md`).

**Meta-loop integration (deferred)**: when the meta-loop branch lands, each
candidate above the threshold will additionally be emitted as a `rule_edit`
proposal of the shape::

    {"kind": "promote_source_to_concept", "source": "docs/source/X.md",
     "rationale": "cited in N cycles across M problems"}

so the meta-loop's existing gate chain + review CLI processes it without a
parallel codepath. This script writes the markdown file today; the JSON-shape
emission is one diff away on merge.

Usage::

    uv run python docs/tools/promotion_candidates.py
    uv run python docs/tools/promotion_candidates.py --threshold 5
    uv run python docs/tools/promotion_candidates.py --dry-run    # print, no write
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import logging
import sys
from collections import defaultdict
from pathlib import Path

log = logging.getLogger("promotion_candidates")

_REPO = Path(__file__).resolve().parents[2]
DEFAULT_JSONL = _REPO.parent / "mb" / "logs" / "cited-sources.jsonl"
DEFAULT_OUTPUT = _REPO.parent / "mb" / "logs" / "promotion-candidates.md"
DEFAULT_THRESHOLD = 3


def _read_jsonl(path: Path) -> list[dict]:
    """Parse JSONL; skip malformed lines with a warning."""
    if not path.exists():
        log.info("citation sidecar not found at %s — no candidates", path)
        return []
    records: list[dict] = []
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line:
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError as e:
            log.warning("skipping malformed line %d in %s: %s", i, path, e)
    return records


def _tally(records: list[dict]) -> dict[str, dict]:
    """Return ``{source_path: {count, cycles, problems, first_cycle, last_cycle}}``."""
    by_source: dict[str, dict] = defaultdict(
        lambda: {
            "count": 0,
            "cycles": [],
            "problems": set(),
            "first_cycle": None,
            "last_cycle": None,
        }
    )
    for rec in records:
        cycle_id = rec.get("cycle_id")
        problem = rec.get("problem", "?")
        for src in rec.get("cited_sources", []) or []:
            entry = by_source[src]
            entry["count"] += 1
            if cycle_id is not None and cycle_id not in entry["cycles"]:
                entry["cycles"].append(cycle_id)
            entry["problems"].add(problem)
            if entry["first_cycle"] is None or (
                cycle_id is not None and cycle_id < entry["first_cycle"]
            ):
                entry["first_cycle"] = cycle_id
            if entry["last_cycle"] is None or (
                cycle_id is not None and cycle_id > entry["last_cycle"]
            ):
                entry["last_cycle"] = cycle_id
    return by_source


def _render_markdown(by_source: dict[str, dict], threshold: int) -> tuple[str, int]:
    """Return ``(markdown, n_candidates)``."""
    candidates = sorted(
        ((src, info) for src, info in by_source.items() if info["count"] >= threshold),
        key=lambda kv: (-kv[1]["count"], kv[0]),
    )
    today = _dt.date.today().isoformat()
    lines = [
        "# Promotion candidates",
        "",
        f"_Updated: {today}. Threshold: ≥{threshold} cite(s) cross-cycle._",
        "",
        (
            "Each `docs/source/<file>.md` below has been declared as a "
            "load-bearing citation in ≥3 distinct inner-agent cycles. Per "
            "`.claude/rules/wiki-attribution.md`, the next step is human "
            "review: read the source distillation, decide whether to author "
            "a `docs/wiki/concepts/<file>.md` page that synthesizes its claims "
            "into the project's vocabulary."
        ),
        "",
    ]
    if not candidates:
        lines.append("_(no candidates above threshold)_")
        lines.append("")
        return "\n".join(lines), 0
    lines.extend(
        [
            "| Source | Count | Cycles | Problems | First cited | Status |",
            "|---|---|---|---|---|---|",
        ]
    )
    for src, info in candidates:
        cycles_str = ", ".join(str(c) for c in sorted(info["cycles"]))
        problems_str = ", ".join(sorted(info["problems"]))
        first = str(info["first_cycle"]) if info["first_cycle"] is not None else "?"
        lines.append(
            f"| `{src}` | {info['count']} | {cycles_str} | {problems_str} | {first} | proposed |"
        )
    lines.append("")
    return "\n".join(lines), len(candidates)


def run(
    *,
    jsonl: Path,
    output: Path,
    threshold: int = DEFAULT_THRESHOLD,
    dry_run: bool = False,
    out_stream=sys.stdout,
) -> int:
    """Tally citations from the sidecar JSONL; write/print candidates markdown.

    Returns the number of candidates that crossed the threshold.
    """
    records = _read_jsonl(jsonl)
    by_source = _tally(records)
    md, n = _render_markdown(by_source, threshold)
    if dry_run:
        print(md, file=out_stream)
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(md, encoding="utf-8")
        print(
            f"promotion_candidates: {n} candidate(s) above threshold {threshold} → {output}",
            file=out_stream,
        )
    return n


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0] if __doc__ else None)
    p.add_argument("--jsonl", type=Path, default=DEFAULT_JSONL)
    p.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    p.add_argument("--threshold", type=int, default=DEFAULT_THRESHOLD)
    p.add_argument("--dry-run", action="store_true", help="print to stdout, do not write")
    p.add_argument("-v", "--verbose", action="store_true")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO)
    run(
        jsonl=args.jsonl,
        output=args.output,
        threshold=args.threshold,
        dry_run=args.dry_run,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
