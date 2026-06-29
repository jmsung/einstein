"""Cross-family transfer ablation runner (pre-reg §0b PRIMARY design).

Phase 1 builds+freezes KB_A on family A (Warm). Phase 2 solves family B Cold vs
Warm-transfer (carrying frozen KB_A), paired on the shared cold-init. Near
(Heilbronn→Tammes) vs far (Heilbronn→autocorrelation) — the distance gradient is the
finding. A separate `--probe` mode runs the §3 headroom screen.

LLM-GATED: do not launch the LLM runs until #4's clean verdict lands AND the shared
Claude rate limit is free (see mb/active/js-feat-ablation-v3-crossfamily.md). With no
real model wired this is a dry-run scaffold; `make_solve_fn` supplies the production
solve_fn when a model + checkout are given.

Usage:
    # dry structural check (no LLM): prints the planned cells
    uv run python scripts/run_transfer_ablation.py --dry-run \
        --family-a heilbronn_triangle --family-b tammes_sphere

    # headroom screen for a model
    uv run python scripts/run_transfer_ablation.py --probe --model haiku \
        --config config/ablation_transfer.yaml
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO / "src"))

from einstein.meta_loop import ablation_runner as ar  # noqa: E402
from einstein.meta_loop import compounding_ablation as ca  # noqa: E402


def _load(config: str, family_filter: str | None) -> list[ca.Problem]:
    problems = ca.load_problems(config)
    return [p for p in problems if family_filter is None or p.family == family_filter]


def _config_frozen(config: str) -> bool:
    """Pre-reg §3 freeze gate: a config is runnable for REAL cells only when it declares
    `frozen: true` — set after the headroom screen fixes the instances + reference_optima.
    The template ships `frozen: false`, so it can only drive --probe / --dry-run."""
    import yaml

    return bool(yaml.safe_load(Path(config).read_text()).get("frozen", False))


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default=str(_REPO / "config" / "ablation_transfer.template.yaml"))
    ap.add_argument("--family-a", default="heilbronn_triangle")
    ap.add_argument("--family-b", default="tammes_sphere")
    ap.add_argument("--results-dir", default=str(_REPO / "results" / "ablation-transfer"))
    ap.add_argument("--checkout-root", default=str(_REPO / "ablation-build"))
    ap.add_argument("--seeds", default="1,2,3")
    ap.add_argument("--model", default=None)
    ap.add_argument("--timeout", type=int, default=1800)
    ap.add_argument("--max-budget-usd", type=float, default=None)
    ap.add_argument("--max-lesson-chars", type=int, default=None)
    ap.add_argument("--replicates", type=int, default=1)
    ap.add_argument("--use-api-key", action="store_true")
    ap.add_argument("--probe", action="store_true", help="run the §3 headroom screen only")
    ap.add_argument("--dry-run", action="store_true", help="print planned cells; no solves")
    args = ap.parse_args(argv)

    seeds = [int(s) for s in args.seeds.split(",") if s.strip()]
    results_dir = Path(args.results_dir)

    a = _load(args.config, args.family_a)
    b = _load(args.config, args.family_b)

    if args.dry_run:
        plan = {
            "phase1_build_KB_A": {"family": args.family_a, "problems": [p.problem_id for p in a]},
            "phase2_transfer": {
                "family": args.family_b,
                "problems": [p.problem_id for p in b],
                "arms": ["cold", "warm_transfer"],
                "seeds": seeds,
                "cells": 2 * len(b) * len(seeds),
            },
        }
        print(json.dumps(plan, indent=2))
        return 0

    solve_fn = ar.make_solve_fn(
        args.checkout_root,
        model=args.model,
        timeout_seconds=args.timeout,
        max_budget_usd=args.max_budget_usd,
        drop_api_key=not args.use_api_key,
        transcripts_dir=str(results_dir / "transcripts"),
    )

    if args.probe:
        probe_problems = _load(args.config, None)
        out = ca.headroom_probe(probe_problems, solve_fn, seeds, results_dir=results_dir / "probe")
        print(json.dumps({"eligible": out["eligible"], "band": out["band"]}, indent=2))
        return 0

    # Pre-reg §3 freeze gate — no real transfer cell against an unfrozen config.
    if not _config_frozen(args.config):
        print(
            f"REFUSED: {args.config} is not frozen (frozen: false).\n"
            "Real transfer cells require a FROZEN config — run --probe first, fix the\n"
            "instances + reference_optima from the headroom screen, set `frozen: true`,\n"
            "and commit it before any cell (pre-reg §3). Use --probe / --dry-run to plan.",
            file=sys.stderr,
        )
        return 2

    records: list[ca.TransferRecord] = []
    out = ca.run_transfer_experiment(
        a,
        b,
        seeds,
        solve_fn,
        results_dir=results_dir,
        max_lesson_chars=args.max_lesson_chars,
        replicates=args.replicates,
        on_record=records.append,
    )
    results_dir.mkdir(parents=True, exist_ok=True)
    (results_dir / "transfer-records.json").write_text(
        json.dumps([r.__dict__ for r in out["records"]], indent=2, default=list)
    )
    n_cold = sum(1 for r in out["records"] if r.arm == "cold")
    n_warm = len(out["records"]) - n_cold
    print(f"transfer done: {args.family_a} -> {args.family_b}; {n_cold} cold, {n_warm} warm cells")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
