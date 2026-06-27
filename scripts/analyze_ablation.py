#!/usr/bin/env python
"""analyze_ablation.py — gap-closed table + Δ_k trend + H1/H2 decisions.

Reads the append-only run log produced by the Cold/Warm knowledge-compounding
driver (pre-reg 2026-06-26, §10.5–6) and emits the pre-registered analysis:
the per-problem gap-closed table (problem × arm), the Δ_k compounding trend, and
the H1 (level) / H2 (slope) decisions per pre-reg §9.

All analysis math lives in `einstein.meta_loop.compounding_ablation` (testable);
this is a thin CLI over it.

Usage:
  scripts/analyze_ablation.py [RUN_LOG]
    RUN_LOG  path to runs.jsonl  (default: results/ablation-2026-06-26/runs.jsonl)
"""

from __future__ import annotations

import statistics
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO / "src"))

from einstein.meta_loop import compounding_ablation as ca  # noqa: E402

DEFAULT_LOG = _REPO / "results" / "ablation-2026-06-26" / "runs.jsonl"


def _cell(records: list[dict], pid: str, arm: str) -> str:
    vals = [r["gap_closed"] for r in records if r["problem_id"] == pid and r["arm"] == arm]
    if not vals:
        return "   —   "
    m = statistics.fmean(vals)
    s = statistics.pstdev(vals) if len(vals) > 1 else 0.0
    return f"{m:.3f}±{s:.3f}"


def main(argv: list[str]) -> int:
    log_path = Path(argv[1]) if len(argv) > 1 else DEFAULT_LOG
    records = ca.load_records(log_path)
    if not records:
        print(f"no run records at {log_path} — run the driver first")
        return 1

    rep = ca.analyze(records)
    pids = sorted(
        {r["problem_id"] for r in records},
        key=lambda p: next(r["sequence_index"] for r in records if r["problem_id"] == p),
    )

    print(f"Knowledge-compounding ablation — {rep.n_records} runs  ({log_path})\n")
    print("gap-closed (mean±stdev over seeds)")
    print(f"{'problem':<12} {'cold':>14} {'warm':>14}   {'Δ_k':>8}")
    print("-" * 54)
    dk_by_pid = {d.problem_id: d for d in rep.delta_k}
    for pid in pids:
        dk = dk_by_pid.get(pid)
        delta = f"{dk.delta:+.3f}" if dk else "   —  "
        print(
            f"{pid:<12} {_cell(records, pid, 'cold'):>14} {_cell(records, pid, 'warm'):>14}   {delta:>8}"
        )
    print("-" * 54)
    print(f"{'MEAN':<12} {rep.cold_mean:>14.3f} {rep.warm_mean:>14.3f}")
    print(f"\npooled per-cell stdev: {rep.pooled_stdev:.4f}")
    print(
        f"Δ-vs-sequence-position slope (descriptive, difficulty-confounded): "
        f"{rep.delta_slope:+.4f}\n"
    )

    print(f"H1 (level — knowledge helps):   {'SUPPORTED' if rep.h1.supported else 'not supported'}")
    print(f"    {rep.h1.detail}")
    print(
        f"H2 (compounding — within-problem): {'SUPPORTED' if rep.h2.supported else 'not supported'}"
    )
    print(f"    {rep.h2.detail}")

    if rep.h1.supported and rep.h2.supported:
        verdict = "H1+H2 → controlled causal evidence the loop compounds (pre-reg §14)"
    elif rep.h1.supported:
        verdict = "H1 only → knowledge helps but in-run compounding unproven (soften claim)"
    else:
        verdict = "null → the loop earned nothing in this regime; report it (pre-committed)"
    print(f"\nverdict: {verdict}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
