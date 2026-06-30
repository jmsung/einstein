#!/usr/bin/env python3
"""Multi-cell confirmatory driver for the persona-council ablation (JSAgent claim #1).

This is the inferential counterpart to `run_council_ablation.py` (the single-cell
smoke). It REUSES that script's validated single-cell logic verbatim — council
dispatch (`gather_council_questions`), block assembly (`build_council_block`), the
shared solver (`make_solve_fn`), the air-gap audit (`audit_checkout`), the paired
cold-init session spec (`build_session_spec`), and harness-side `gap_closed`. It does
NOT duplicate the solver.

It runs the experiment over a GRID of (problem_id, seed) cells, holding the solve
budget EQUAL across both arms (council-off vs council-on, the on-arm differing ONLY
by the injected council block in `problem.statement`), and aggregates the per-cell
`delta = gap_on - gap_off` into a mean with a bootstrap 95% CI.

Built for an overnight run: the loop is RESUMABLE. Every completed cell is appended
(flushed) to `<results-dir>/records.jsonl` immediately; on restart, any (problem_id,
seed) already in that file is skipped. `--dry-run` exercises the planning + bootstrap
aggregation paths on synthetic deltas WITHOUT any LLM call.
"""

from __future__ import annotations

import argparse
import dataclasses
import json
import random
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
# run_council_ablation.py is a script, not a package — put scripts/ on the path so we
# can import its validated single-cell helpers instead of duplicating them.
sys.path.insert(0, str(REPO / "scripts"))

from run_council_ablation import (  # noqa: E402
    CHECKOUT_ROOT,
    HEILBRONN_CONFIG,
    PROBLEM_CATEGORY,  # noqa: F401  (re-exported for callers/inspection)
    build_council_block,
    gather_council_questions,
)

from einstein.meta_loop.ablation_runner import (  # noqa: E402
    audit_checkout,
    make_solve_fn,
)
from einstein.meta_loop.compounding_ablation import (  # noqa: E402
    ARM_CONFIGS,
    Arm,
    build_session_spec,
    gap_closed,
    load_problems,
)


def bootstrap_ci(
    deltas: list[float], *, n_resamples: int = 10000, seed: int = 12345
) -> tuple[float, float, float]:
    """Pure-python paired bootstrap: mean + 95% percentile CI of the per-cell deltas.

    FIXED seed (default 12345) so the CI is reproducible. Returns (mean, lo, hi).
    """
    if not deltas:
        return (float("nan"), float("nan"), float("nan"))
    n = len(deltas)
    mean = sum(deltas) / n
    rng = random.Random(seed)
    means = []
    for _ in range(n_resamples):
        s = 0.0
        for _ in range(n):
            s += deltas[rng.randrange(n)]
        means.append(s / n)
    means.sort()
    lo = means[int(0.025 * (n_resamples - 1))]
    hi = means[int(0.975 * (n_resamples - 1))]
    return (mean, lo, hi)


def summarize(records: list[dict]) -> dict:
    """Aggregate completed-cell records into the summary dict (+ bootstrap CI)."""
    deltas = [r["delta"] for r in records]
    mean, lo, hi = bootstrap_ci(deltas)
    gaps_off = [r["gap_off"] for r in records]
    gaps_on = [r["gap_on"] for r in records]
    n_off_valid = sum(1 for r in records if r.get("off_ok"))
    n_on_valid = sum(1 for r in records if r.get("on_ok"))
    return {
        "n_cells": len(records),
        "mean_delta": mean,
        "ci_low": lo,
        "ci_high": hi,
        "mean_gap_off": (sum(gaps_off) / len(gaps_off)) if gaps_off else float("nan"),
        "mean_gap_on": (sum(gaps_on) / len(gaps_on)) if gaps_on else float("nan"),
        "n_off_valid": n_off_valid,
        "n_on_valid": n_on_valid,
        "cells": records,
    }


def print_summary(summary: dict) -> None:
    print("\n" + "=" * 72, flush=True)
    print("CONFIRMATORY SUMMARY", flush=True)
    print("=" * 72, flush=True)
    print(f"n_cells            = {summary['n_cells']}", flush=True)
    print(
        f"mean Δ (on - off)  = {summary['mean_delta']:+.4f}  "
        f"95% CI [{summary['ci_low']:+.4f}, {summary['ci_high']:+.4f}]",
        flush=True,
    )
    print(
        f"mean gap_closed    = off {summary['mean_gap_off']:.4f}  "
        f"on {summary['mean_gap_on']:.4f}",
        flush=True,
    )
    print(
        f"valid solves       = off {summary['n_off_valid']}/{summary['n_cells']}  "
        f"on {summary['n_on_valid']}/{summary['n_cells']}",
        flush=True,
    )
    ci_lo, ci_hi = summary["ci_low"], summary["ci_high"]
    if summary["n_cells"]:
        if ci_lo > 0:
            verdict = "council HELPS (CI strictly > 0)"
        elif ci_hi < 0:
            verdict = "council HURTS (CI strictly < 0)"
        else:
            verdict = "NULL (CI straddles 0)"
        print(f"verdict            = {verdict}", flush=True)


def load_done_cells(records_path: Path) -> tuple[list[dict], set[tuple[str, int]]]:
    """Read records.jsonl (if present) -> (records, set of done (problem_id, seed))."""
    records: list[dict] = []
    done: set[tuple[str, int]] = set()
    if records_path.exists():
        for line in records_path.read_text().splitlines():
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            records.append(rec)
            done.add((rec["problem_id"], rec["seed"]))
    return records, done


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--problem-ids", default="heil-n13,heil-n14")
    ap.add_argument("--seeds", default="1,2,3,4")
    ap.add_argument("--model", default="haiku", help="model for persona + solve sessions")
    ap.add_argument("--persona-timeout", type=int, default=120)
    ap.add_argument("--solve-timeout", type=int, default=600)
    ap.add_argument("--solve-cap", type=float, default=1.5)
    ap.add_argument("--results-dir", default=str(REPO / "results" / "council-confirmatory"))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    problem_ids = [s.strip() for s in args.problem_ids.split(",") if s.strip()]
    seeds = [int(s.strip()) for s in args.seeds.split(",") if s.strip()]
    results_dir = Path(args.results_dir)
    records_path = results_dir / "records.jsonl"
    summary_path = results_dir / "summary.json"

    problems = {p.problem_id: p for p in load_problems(HEILBRONN_CONFIG)}
    for pid in problem_ids:
        if pid not in problems:
            raise SystemExit(f"unknown problem {pid}; have {sorted(problems)}")

    print("=" * 72, flush=True)
    print("PERSONA-COUNCIL ABLATION — CONFIRMATORY (multi-cell)", flush=True)
    print("=" * 72, flush=True)
    print(f"problem_ids={problem_ids}  seeds={seeds}", flush=True)
    print(
        f"model={args.model}  solve_budget: timeout={args.solve_timeout}s "
        f"cap=${args.solve_cap}  (SAME for both arms)",
        flush=True,
    )
    print(f"results_dir={results_dir}", flush=True)

    # Resume: skip any (problem_id, seed) already in records.jsonl.
    results_dir.mkdir(parents=True, exist_ok=True)
    records, done = load_done_cells(records_path)
    planned: list[tuple[str, int]] = []
    for pid in problem_ids:
        for seed in seeds:
            if (pid, seed) in done:
                continue
            planned.append((pid, seed))

    print(f"\nalready done: {len(done)} cells {sorted(done)}", flush=True)
    print(f"planned this run: {len(planned)} cells", flush=True)
    for pid, seed in planned:
        # Pairing seed: the cold-init depends only on (n, seed), so off and on share
        # an identical cold baseline at the same seed — a paired comparison per cell.
        print(
            f"  cell problem={pid} n={problems[pid].n} seed={seed} "
            f"(paired cold-init by (n={problems[pid].n}, seed={seed}))",
            flush=True,
        )

    if args.dry_run:
        print("\n[dry-run] no LLM calls; exercising bootstrap + summary on synthetic deltas", flush=True)
        synth_deltas = [0.1, 0.3, -0.05, 0.2]
        synth_records = []
        for i, d in enumerate(synth_deltas):
            synth_records.append(
                {
                    "problem_id": "synthetic",
                    "n": 13,
                    "seed": i + 1,
                    "gap_off": 0.5,
                    "gap_on": 0.5 + d,
                    "delta": d,
                    "off_ok": True,
                    "on_ok": True,
                }
            )
        synth_summary = summarize(synth_records)
        print(
            f"[dry-run] synthetic deltas = {synth_deltas}",
            flush=True,
        )
        print_summary(synth_summary)
        print("\n[dry-run] OK — planning + aggregation paths exercised, no solve_fn / council called", flush=True)
        return 0

    # ---- Pre-flight: air-gap audit of the shared cold checkout ----
    cold_cwd = CHECKOUT_ROOT / "einstein-cold"
    audit = audit_checkout(cold_cwd)
    print(
        f"\nair-gap audit (einstein-cold): passed={audit['passed']} "
        f"web_tools={audit['web_tools_in_allowlist']} "
        f"leaked={audit['leaked_answer_key_files'][:3]}",
        flush=True,
    )
    if not audit["passed"]:
        raise SystemExit("air-gap audit FAILED — aborting (would invalidate the ablation)")

    # ---- ONE shared solver (identical for both arms; the only arm difference is the
    #      injected council block in problem.statement) ----
    solve_telem: list[dict] = []
    solve_fn = make_solve_fn(
        CHECKOUT_ROOT,
        model=args.model,
        timeout_seconds=args.solve_timeout,
        max_budget_usd=args.solve_cap,
        telemetry=solve_telem,
        drop_api_key=True,
    )
    cfg = ARM_CONFIGS[Arm.COLD]  # identical for BOTH arms (no lesson) — like the smoke

    for pid, seed in planned:
        problem = problems[pid]
        print("\n" + "-" * 72, flush=True)
        print(f"CELL problem={pid} n={problem.n} seed={seed}", flush=True)
        print("-" * 72, flush=True)

        # Council dispatch ONCE per cell (council-ON questions).
        print("[1] council dispatch (wiki-less personas writing questions)…", flush=True)
        questions, council_telem = gather_council_questions(
            statement=problem.statement,
            family=problem.family,
            n=problem.n,
            model=args.model,
            timeout_s=args.persona_timeout,
            cap_usd=0.50,
            cwd=cold_cwd,
        )
        council_block = build_council_block(questions)
        council_cost = sum((t["cost_usd"] or 0.0) for t in council_telem)
        council_wall = sum(t["wall_s"] for t in council_telem)
        print(
            f"    council: {len(questions)} personas, "
            f"{sum(1 for t in council_telem if t['ok'])} ok, "
            f"cost=${council_cost:.4f}, wall={council_wall:.1f}s",
            flush=True,
        )

        problem_off = problem
        problem_on = dataclasses.replace(
            problem, statement=problem.statement + "\n\n" + council_block
        )

        spec_off = build_session_spec(problem_off, Arm.COLD, seed, run_kb=None)
        spec_on = build_session_spec(problem_on, Arm.COLD, seed, run_kb=None)

        print("[2] COUNCIL-OFF solve…", flush=True)
        res_off = solve_fn(problem_off, cfg, seed, spec_off)
        print("[3] COUNCIL-ON solve…", flush=True)
        res_on = solve_fn(problem_on, cfg, seed, spec_on)

        gap_off = gap_closed(
            res_off.score_coldinit, res_off.score_final,
            problem.reference_optimum, minimize=problem.minimize,
        )
        gap_on = gap_closed(
            res_on.score_coldinit, res_on.score_final,
            problem.reference_optimum, minimize=problem.minimize,
        )
        paired = abs(res_off.score_coldinit - res_on.score_coldinit) < 1e-12

        # The last 2 telemetry entries are THIS cell's off then on (solve order above).
        off_t = solve_telem[-2]
        on_t = solve_telem[-1]

        rec = {
            "problem_id": pid,
            "n": problem.n,
            "seed": seed,
            "score_coldinit_off": res_off.score_coldinit,
            "score_coldinit_on": res_on.score_coldinit,
            "paired": paired,
            "gap_off": gap_off,
            "gap_on": gap_on,
            "delta": gap_on - gap_off,
            "wall_off": res_off.wall_clock_s,
            "wall_on": res_on.wall_clock_s,
            "council_cost": council_cost,
            "council_wall": council_wall,
            "off_ok": off_t.get("ok"),
            "off_kind": off_t.get("error_kind"),
            "off_verify": off_t.get("verify"),
            "on_ok": on_t.get("ok"),
            "on_kind": on_t.get("error_kind"),
            "on_verify": on_t.get("verify"),
        }

        # RESUMABILITY: append + flush this cell IMMEDIATELY (overnight crash-safe).
        with records_path.open("a") as fh:
            fh.write(json.dumps(rec) + "\n")
            fh.flush()
        records.append(rec)

        print(
            f"    paired={paired}  gap_off={gap_off:.4f}  gap_on={gap_on:.4f}  "
            f"Δ={rec['delta']:+.4f}  (off_ok={rec['off_ok']} on_ok={rec['on_ok']})",
            flush=True,
        )

    # ---- Aggregate over ALL completed cells (resumed + this run) ----
    summary = summarize(records)
    with summary_path.open("w") as fh:
        json.dump(summary, fh, indent=2)
    print(f"\nwrote {summary_path}", flush=True)
    print_summary(summary)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
