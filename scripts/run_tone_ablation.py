#!/usr/bin/env python3
"""Prompt-tone ablation confirmatory driver (JSAgent claim #8).

Tests whether the system-prompt PREAMBLE moves outcomes — effort vs efficiency vs
null (prereg
docs/agent/ablations/2026-06-28-prompt-tone-effort-vs-efficiency-preregistration.md).
Two arms differ in exactly ONE variable: the verbatim tone preamble prepended to
the solve prompt (`prompt_tone`):

- NEUTRAL (control)     — the FROZEN §4 length-matched filler (no motivational
  semantics, length-matched to ENCOURAGING so tone cannot also buy raw tokens).
- ENCOURAGING (treated) — the human's frozen "never give up, push to rank 1" string.

Everything else is held identical: same air-gapped checkout, same Cold arm config,
same paired cold-init per (problem, seed) (built ONCE and reused for both arms via
`build_session_spec(..., Arm.COLD, seed)`), same model, budget, tools, solver. The
harness scores (triple-verified `gap_closed`), never the agent's self-report. The
primary DV is the paired delta `gap_encouraging - gap_neutral` per cell.

This mirrors the council smoke's solve-cell pattern (`run_council_ablation.py`) but
the council had an injected QUESTIONS block in `problem.statement`; here the ONLY
arm difference is `prompt_tone` bound into the solve_fn — the statement/spec are
byte-identical across arms.

SMOKE/CONFIRMATORY: defaults to heil-n13,heil-n14 × seeds 1-4 (8 paired cells).
Resumable: each completed cell is appended to records.jsonl immediately; a restart
skips (problem_id, seed) already present. `--dry-run` exercises the plan +
bootstrap with NO LLM calls.
"""

from __future__ import annotations

import argparse
import json
import random
import time
from pathlib import Path

from einstein.meta_loop.ablation_runner import (
    audit_checkout,
    make_solve_fn,
)
from einstein.meta_loop.compounding_ablation import (
    ARM_CONFIGS,
    Arm,
    build_session_spec,
    gap_closed,
    load_problems,
)
from einstein.meta_loop.prompt_tone import PREAMBLES, PromptTone

REPO = Path(__file__).resolve().parents[1]
CHECKOUT_ROOT = REPO / "ablation-build"


# ---------------- bootstrap (pure python) ----------------


def _mean(xs: list[float]) -> float:
    return sum(xs) / len(xs) if xs else 0.0


def bootstrap_ci(
    deltas: list[float], *, n_boot: int = 10000, seed: int = 12345
) -> tuple[float, float, float]:
    """Mean delta + 95% percentile bootstrap CI (pure-python, fixed RNG).

    Resamples `deltas` with replacement `n_boot` times; returns
    (mean_delta, ci_low, ci_high) where the CI is the 2.5/97.5 percentile band of
    the resampled means. Deterministic via `random.Random(seed)`.
    """
    mean_delta = _mean(deltas)
    if len(deltas) < 2:
        return mean_delta, mean_delta, mean_delta
    rng = random.Random(seed)
    n = len(deltas)
    means: list[float] = []
    for _ in range(n_boot):
        sample = [deltas[rng.randrange(n)] for _ in range(n)]
        means.append(_mean(sample))
    means.sort()
    lo = means[int(0.025 * n_boot)]
    hi = means[int(0.975 * n_boot)]
    return mean_delta, lo, hi


# ---------------- planning / resume ----------------


def planned_cells(problem_ids: list[str], seeds: list[int]) -> list[tuple[str, int]]:
    return [(pid, s) for pid in problem_ids for s in seeds]


def load_done(records_path: Path) -> set[tuple[str, int]]:
    """Set of (problem_id, seed) already logged in records.jsonl (resume support)."""
    done: set[tuple[str, int]] = set()
    if not records_path.exists():
        return done
    for line in records_path.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            o = json.loads(line)
        except json.JSONDecodeError:
            continue
        done.add((o["problem_id"], int(o["seed"])))
    return done


def aggregate(records: list[dict]) -> dict:
    deltas = [r["delta"] for r in records]
    mean_delta, lo, hi = bootstrap_ci(deltas)
    return {
        "n_cells": len(records),
        "mean_delta": mean_delta,
        "ci_low": lo,
        "ci_high": hi,
        "mean_gap_neutral": _mean([r["gap_neutral"] for r in records]),
        "mean_gap_encouraging": _mean([r["gap_encouraging"] for r in records]),
        "cells": records,
    }


def print_arm_strings() -> None:
    neutral = PREAMBLES[PromptTone.NEUTRAL]
    enc = PREAMBLES[PromptTone.ENCOURAGING]
    print("FROZEN arm strings (§4, the ONE variable):", flush=True)
    print(f"  NEUTRAL     ({len(neutral):3d} chars): {neutral!r}", flush=True)
    print(f"  ENCOURAGING ({len(enc):3d} chars): {enc!r}", flush=True)


# ---------------- dry run ----------------


def do_dry_run(cells: list[tuple[str, int]]) -> int:
    print("=" * 72, flush=True)
    print("PROMPT-TONE ABLATION — DRY RUN (no LLM calls)", flush=True)
    print("=" * 72, flush=True)
    print(f"planned cells (after resume-skip): {len(cells)}", flush=True)
    for pid, s in cells:
        print(f"  - {pid} seed={s}  arms: NEUTRAL vs ENCOURAGING (paired cold-init)", flush=True)
    print("", flush=True)
    print_arm_strings()

    # Exercise the bootstrap on synthetic deltas (deterministic).
    print("\nsynthetic bootstrap check (NOT real data):", flush=True)
    rng = random.Random(7)
    synth = [rng.gauss(0.03, 0.05) for _ in range(len(cells))]
    synth_records = [
        {
            "problem_id": pid,
            "seed": s,
            "gap_neutral": 0.40,
            "gap_encouraging": 0.40 + d,
            "delta": d,
        }
        for (pid, s), d in zip(cells, synth, strict=True)
    ]
    summary = aggregate(synth_records)
    print(
        f"  n_cells={summary['n_cells']} mean_delta={summary['mean_delta']:+.4f} "
        f"95% CI=[{summary['ci_low']:+.4f}, {summary['ci_high']:+.4f}]",
        flush=True,
    )
    print(
        f"  mean_gap_neutral={summary['mean_gap_neutral']:.4f} "
        f"mean_gap_encouraging={summary['mean_gap_encouraging']:.4f}",
        flush=True,
    )
    print("\nDRY RUN OK — no LLM calls made.", flush=True)
    return 0


# ---------------- main ----------------


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--config",
        default=str(REPO / "config" / "ablation_heilbronn_problems.yaml"),
    )
    ap.add_argument("--problem-ids", default="heil-n13,heil-n14")
    ap.add_argument("--seeds", default="1,2,3,4")
    ap.add_argument("--model", default="haiku")
    ap.add_argument("--solve-timeout", type=int, default=600)
    ap.add_argument("--solve-cap", type=float, default=1.5)
    ap.add_argument("--results-dir", default=str(REPO / "results" / "tone"))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    problem_ids = [p.strip() for p in args.problem_ids.split(",") if p.strip()]
    seeds = [int(s) for s in args.seeds.split(",") if s.strip()]
    results_dir = Path(args.results_dir)
    records_path = results_dir / "records.jsonl"

    problems = {p.problem_id: p for p in load_problems(args.config)}
    unknown = [pid for pid in problem_ids if pid not in problems]
    if unknown:
        raise SystemExit(f"unknown problem_ids {unknown}; have {sorted(problems)}")

    done = load_done(records_path)
    cells = [c for c in planned_cells(problem_ids, seeds) if c not in done]

    if args.dry_run:
        return do_dry_run(cells)

    # ---- real run ----
    results_dir.mkdir(parents=True, exist_ok=True)
    cold_cwd = CHECKOUT_ROOT / "einstein-cold"

    print("=" * 72, flush=True)
    print("PROMPT-TONE ABLATION — CONFIRMATORY (paired NEUTRAL vs ENCOURAGING)", flush=True)
    print("=" * 72, flush=True)
    print(
        f"problems={problem_ids} seeds={seeds} model={args.model} "
        f"solve_budget: timeout={args.solve_timeout}s cap=${args.solve_cap} (SAME both arms)",
        flush=True,
    )
    print_arm_strings()
    print(
        f"\nresume: {len(done)} cell(s) already logged; {len(cells)} remaining.",
        flush=True,
    )

    # Pre-flight air-gap hard gate (both arms run in einstein-cold).
    audit = audit_checkout(cold_cwd)
    print(
        f"air-gap audit (einstein-cold): passed={audit['passed']} "
        f"web_tools={audit['web_tools_in_allowlist']} "
        f"leaked={audit['leaked_answer_key_files'][:3]}",
        flush=True,
    )
    assert audit["passed"], f"air-gap breached: {audit}"

    # Two tone-bound solve_fns, identical except prompt_tone; each its own telemetry.
    neutral_telem: list[dict] = []
    enc_telem: list[dict] = []
    common = dict(
        model=args.model,
        timeout_seconds=args.solve_timeout,
        max_budget_usd=args.solve_cap,
        drop_api_key=True,
    )
    solve_neutral = make_solve_fn(
        CHECKOUT_ROOT, telemetry=neutral_telem, prompt_tone=PromptTone.NEUTRAL, **common
    )
    solve_enc = make_solve_fn(
        CHECKOUT_ROOT, telemetry=enc_telem, prompt_tone=PromptTone.ENCOURAGING, **common
    )

    cfg = ARM_CONFIGS[Arm.COLD]  # both arms: read_kb=False, write_kb=False (identical config)

    for pid, seed in cells:
        problem = problems[pid]
        # SAME spec for both arms (cold-init depends only on (n, seed) -> paired).
        spec = build_session_spec(problem, Arm.COLD, seed, run_kb=None)

        print(f"\n[{pid} seed={seed}] NEUTRAL solve…", flush=True)
        t0 = time.monotonic()
        res_n = solve_neutral(problem, cfg, seed, spec)
        wall_n = time.monotonic() - t0

        print(f"[{pid} seed={seed}] ENCOURAGING solve…", flush=True)
        t0 = time.monotonic()
        res_e = solve_enc(problem, cfg, seed, spec)
        wall_e = time.monotonic() - t0

        gap_n = gap_closed(
            res_n.score_coldinit, res_n.score_final, problem.reference_optimum,
            minimize=problem.minimize,
        )
        gap_e = gap_closed(
            res_e.score_coldinit, res_e.score_final, problem.reference_optimum,
            minimize=problem.minimize,
        )
        paired = abs(res_n.score_coldinit - res_e.score_coldinit) < 1e-15

        tn = neutral_telem[-1] if neutral_telem else {}
        te = enc_telem[-1] if enc_telem else {}
        record = {
            "problem_id": pid,
            "n": problem.n,
            "seed": seed,
            "paired": paired,
            "gap_neutral": gap_n,
            "gap_encouraging": gap_e,
            "delta": gap_e - gap_n,
            "wall_neutral": wall_n,
            "wall_encouraging": wall_e,
            "neutral_ok": tn.get("ok"),
            "neutral_kind": tn.get("error_kind", ""),
            "neutral_verify": tn.get("verify", ""),
            "enc_ok": te.get("ok"),
            "enc_kind": te.get("error_kind", ""),
            "enc_verify": te.get("verify", ""),
        }
        with records_path.open("a") as fh:
            fh.write(json.dumps(record) + "\n")
            fh.flush()
        print(
            f"  paired={paired} gap_neutral={gap_n:.4f} gap_encouraging={gap_e:.4f} "
            f"delta={record['delta']:+.4f}",
            flush=True,
        )

    # Aggregate over ALL logged cells (this run + resumed).
    all_records = [
        json.loads(line)
        for line in records_path.read_text().splitlines()
        if line.strip()
    ]
    summary = aggregate(all_records)
    (results_dir / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")

    print("\n" + "=" * 72, flush=True)
    print("SUMMARY", flush=True)
    print("=" * 72, flush=True)
    print(
        f"n_cells={summary['n_cells']} mean_delta(enc-neutral)={summary['mean_delta']:+.4f} "
        f"95% CI=[{summary['ci_low']:+.4f}, {summary['ci_high']:+.4f}]",
        flush=True,
    )
    print(
        f"mean_gap_neutral={summary['mean_gap_neutral']:.4f} "
        f"mean_gap_encouraging={summary['mean_gap_encouraging']:.4f}",
        flush=True,
    )
    print("\nper-cell:", flush=True)
    for r in summary["cells"]:
        print(
            f"  {r['problem_id']} seed={r['seed']} paired={r['paired']} "
            f"delta={r['delta']:+.4f} (n={r['gap_neutral']:.3f} e={r['gap_encouraging']:.3f})",
            flush=True,
        )
    print(f"\nwrote {results_dir / 'summary.json'}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
