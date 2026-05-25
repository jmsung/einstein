#!/usr/bin/env python3
"""select_top.py — promote the top-N candidates in a seed-ingest JSON to approved=true.

After running `seed_ingest.py author-sweep` (or `propose`), you typically
want the top-N by relevance auto-approved without hand-editing the JSON.
This script does that: sort all candidates by relevance descending,
mark the top-N as approved=true, keep the rest at approved=null
(human gate preserved).

Usage:
    uv run python docs/tools/select_top.py --candidates docs/agent/author-sweep-candidates.json --top 100
    uv run python docs/tools/select_top.py --candidates ... --top 100 --min-year 2018 --min-relevance 0.05
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def select_top(*, candidates_json: Path, top_n: int,
               min_year: int | None = None,
               min_relevance: float | None = None) -> int:
    data = json.loads(candidates_json.read_text())
    # Collect all candidates with their parent block
    all_cands: list[tuple[dict, dict]] = []
    for block in data["concepts"]:
        for cand in block["candidates"]:
            all_cands.append((cand, block))

    # Filter by year / relevance floor
    if min_year is not None:
        all_cands = [(c, b) for c, b in all_cands
                     if str(c.get("year", "0")).isdigit() and int(c["year"]) >= min_year]
    if min_relevance is not None:
        all_cands = [(c, b) for c, b in all_cands
                     if c.get("relevance", 0) >= min_relevance]

    # Skip already-approved (preserve existing approvals)
    pending = [(c, b) for c, b in all_cands if not c.get("approved")]
    already_approved = [c for c, _ in all_cands if c.get("approved") is True]

    # Sort pending by relevance desc, then year desc as tiebreaker
    pending.sort(key=lambda x: (
        -x[0].get("relevance", 0),
        -int(x[0].get("year", "0")) if str(x[0].get("year", "0")).isdigit() else 0,
    ))

    # Promote up to top_n total approved (counting existing)
    headroom = max(0, top_n - len(already_approved))
    promoted = pending[:headroom]
    for cand, _block in promoted:
        cand["approved"] = True
        cand["auto_approved"] = True

    candidates_json.write_text(json.dumps(data, indent=2) + "\n")

    print(f"already approved: {len(already_approved)}")
    print(f"newly promoted:   {len(promoted)}")
    print(f"target top:       {top_n}")
    print(f"total approved:   {len(already_approved) + len(promoted)}")
    if promoted:
        print()
        print("newly-promoted titles (sorted by relevance):")
        for c, b in promoted[:20]:
            cat = b.get("category", "?")
            print(f"  {c.get('relevance', 0):.3f}  [{c.get('year', '?')}]  "
                  f"({cat:<22}) {c.get('title', '?')[:80]}")
        if len(promoted) > 20:
            print(f"  ... and {len(promoted) - 20} more")

    return len(already_approved) + len(promoted)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    p.add_argument("--candidates", type=Path, required=True)
    p.add_argument("--top", type=int, default=100)
    p.add_argument("--min-year", type=int, default=None)
    p.add_argument("--min-relevance", type=float, default=None)
    args = p.parse_args(argv)
    select_top(candidates_json=args.candidates, top_n=args.top,
               min_year=args.min_year, min_relevance=args.min_relevance)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
