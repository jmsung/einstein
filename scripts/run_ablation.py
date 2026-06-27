#!/usr/bin/env python
"""run_ablation.py — execute the Cold/Warm knowledge-compounding A/B test.

Drives the full 36-cell (problem x arm x seed) matrix: each cell is a fresh
headless `claude` session inside the air-gapped clean-room checkout, scored
independently by the harness. Resumable — re-running skips completed (arm, seed)
sequences. See docs/agent/ablations/RUNBOOK-knowledge-compounding.md.

Usage:
  scripts/run_ablation.py [--build] [--seeds 1,2,3] [--model M] [--timeout 1800]
      --build         build the clean-room checkouts first (build_ablation_repos.sh)
      --checkout-root dir holding einstein-cold/ einstein-warm/  (default: ablation-build)
      --config        problem set  (default: config/ablation_problems.yaml)
      --results-dir   output dir   (default: results/ablation-2026-06-26)
      --seeds         comma list   (default: 1,2,3)

This spawns real, billed sessions. Estimate ~36 sessions; see the runbook.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO / "src"))

from einstein.meta_loop import ablation_runner as ar  # noqa: E402
from einstein.meta_loop import compounding_ablation as ca  # noqa: E402


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", action="store_true")
    ap.add_argument("--checkout-root", default=str(_REPO / "ablation-build"))
    ap.add_argument("--config", default=str(_REPO / "config" / "ablation_problems.yaml"))
    ap.add_argument("--results-dir", default=str(_REPO / "results" / "ablation-2026-06-26"))
    ap.add_argument("--seeds", default="1,2,3")
    ap.add_argument("--model", default=None)
    ap.add_argument("--timeout", type=int, default=1800)
    ap.add_argument(
        "--max-budget-usd",
        type=float,
        default=None,
        help="per-session spend cap (held equal across arms) — the efficiency-DV lever",
    )
    ap.add_argument(
        "--use-api-key",
        action="store_true",
        help="use ANTHROPIC_API_KEY (pay-per-token) instead of the Claude Code login",
    )
    args = ap.parse_args(argv[1:])

    seeds = [int(s) for s in args.seeds.split(",") if s.strip()]
    checkout_root = Path(args.checkout_root)

    if args.build:
        print(f"building clean-room checkouts → {checkout_root}")
        subprocess.run(
            [
                "bash",
                str(_REPO / "scripts" / "build_ablation_repos.sh"),
                "HEAD",
                str(checkout_root),
            ],
            check=True,
        )
    for arm in ("cold", "warm"):
        if not (checkout_root / f"einstein-{arm}").is_dir():
            print(f"missing checkout {checkout_root}/einstein-{arm} — run with --build first")
            return 1

    problems = ca.load_problems(args.config)
    telemetry: list = []
    solve_fn = ar.make_solve_fn(
        checkout_root,
        model=args.model,
        timeout_seconds=args.timeout,
        max_budget_usd=args.max_budget_usd,
        telemetry=telemetry,
        drop_api_key=not args.use_api_key,
    )

    cap = f"${args.max_budget_usd}/session" if args.max_budget_usd else "uncapped"
    print(
        f"running {len(problems)} problems × 2 arms × {len(seeds)} seeds "
        f"= {len(problems) * 2 * len(seeds)} cells (resumable; budget {cap})"
    )
    summary = ar.run_experiment(
        problems,
        seeds,
        solve_fn,
        results_dir=args.results_dir,
        checkout_root=checkout_root,
    )

    print(f"\nran sequences:     {summary['ran'] or '(none — all complete)'}")
    print(f"skipped (done):    {summary['skipped'] or '(none)'}")
    print(f"total records:     {summary['n_records']}")

    # Persist per-cell telemetry (cost/wall = the efficiency-DV data) append-only.
    import json as _json

    tel_path = Path(args.results_dir) / "telemetry.jsonl"
    with tel_path.open("a") as fh:
        for c in telemetry:
            fh.write(_json.dumps(c) + "\n")

    cost = sum(c["cost_usd"] or 0.0 for c in telemetry)
    fails = [c for c in telemetry if not c["ok"]]
    print(f"session cost this run: ${cost:.2f}  ({len(telemetry)} cells, {len(fails)} failed)")
    if telemetry:
        import statistics as _st

        for arm in ("cold", "warm"):
            cells = [c for c in telemetry if c["arm"] == arm]
            if cells:
                mc = _st.fmean(c["cost_usd"] or 0.0 for c in cells)
                mw = _st.fmean(c["wall_clock_s"] for c in cells)
                print(
                    f"  {arm}: mean ${mc:.2f}/session, {mw:.0f}s  (efficiency DV → telemetry.jsonl)"
                )

    bad_audits = [a for a in summary["audits"] if not a["passed"]]
    if bad_audits:
        print(f"⚠ AIR-GAP RECEIPT FAILED for {len(bad_audits)} checkouts: {bad_audits}")
        return 2
    if summary["audits"]:
        print("air-gap receipts: all passed ✓")

    print(f"\nnext: scripts/analyze_ablation.py {Path(args.results_dir) / 'runs.jsonl'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
