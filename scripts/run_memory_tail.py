#!/usr/bin/env python
"""run_memory_tail.py — §6.5 "tail estimand" (Test 1): the heavy-tail test.

The mean Cold-vs-Warm ablation can come back NULL (warm ≈ cold on average) while
memory still changes the *shape* of the outcome distribution: a banked lesson that
usually does nothing but occasionally unlocks a near-solve FATTENS THE UPPER TAIL
without moving the mean. This script re-runs the same Cold/Warm memory ablation
(REUSING `compounding_ablation.run_arm_sequence` + the production `solve_fn` from
`ablation_runner.make_solve_fn` — no duplicate solver) over a SHORT Heilbronn
sequence across MANY seeds, then analyzes the pooled per-cell `gap_closed` with
TAIL statistics (p90, max, near-solve rate) instead of the mean.

Headline question: does warm's UPPER tail (p90 / max / near-solve rate) exceed
cold's even when the means are close? If yes → memory fattens the tail (heavy-tail
hypothesis supported). If the means and the tails both tie → genuine null.

Design (defaults):
  - Heilbronn sequence heil-n13,heil-n14,heil-n15 (warm needs >=2 problems so it
    has banked lessons before the later ones), seeds 1..20, --solve-timeout 400,
    --model haiku.
  - Per arm: `run_arm_sequence` (which already drops transient/offline cells via
    `fair_attempt` and is resumable via skip_done + on_record). Each RunRecord is
    appended (flushed) to <results-dir>/records.jsonl; skip_done is rebuilt from
    that jsonl on startup → RESUMABLE.
  - Tail DV: pool the per-cell gap_closed per arm; report mean, p90, max, and
    P(gap_closed >= 0.9) (near-solve rate). Warm-minus-Cold for each, each with a
    95% pure-python bootstrap CI (10000 resamples, fixed random.Random(12345),
    per-arm pools resampled independently).

Usage:
  scripts/run_memory_tail.py --dry-run
  scripts/run_memory_tail.py --seeds 1..20 --solve-timeout 400 --model haiku

--dry-run lists the planned (arm, problem, seed) cells and exercises the tail-DV +
bootstrap on SYNTHETIC per-cell gap arrays (cold low-ish, warm = cold with a
fattened tail), prints the synthetic tail table, makes NO LLM calls, exits 0.
"""

from __future__ import annotations

import argparse
import json
import random
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO / "src"))

from einstein.meta_loop import ablation_runner as ar  # noqa: E402
from einstein.meta_loop import compounding_ablation as ca  # noqa: E402

NEAR_SOLVE_THRESHOLD = 0.9  # gap_closed >= this counts as a "near-solve" (upper-tail mass)
BOOTSTRAP_RESAMPLES = 10000
BOOTSTRAP_SEED = 12345


# ---------------- tail statistics (the §6.5 DV) ----------------


def _percentile(values: list[float], q: float) -> float:
    """Linear-interpolated q-th percentile (q in [0,100]) of `values`. Empty → 0.0."""
    if not values:
        return 0.0
    xs = sorted(values)
    if len(xs) == 1:
        return xs[0]
    pos = (q / 100.0) * (len(xs) - 1)
    lo = int(pos)
    hi = min(lo + 1, len(xs) - 1)
    frac = pos - lo
    return xs[lo] + (xs[hi] - xs[lo]) * frac


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _near_solve_rate(values: list[float], threshold: float = NEAR_SOLVE_THRESHOLD) -> float:
    """P(gap_closed >= threshold) — fraction of cells that landed in the upper tail."""
    if not values:
        return 0.0
    return sum(1 for v in values if v >= threshold) / len(values)


def _max(values: list[float]) -> float:
    return max(values) if values else 0.0


# stat_name -> callable(pool) -> float. The TAIL DVs: mean is the baseline that the
# mean-ablation already reports; p90/max/near-solve are the upper-tail instruments.
TAIL_STATS: dict[str, object] = {
    "mean": _mean,
    "p90": lambda v: _percentile(v, 90.0),
    "max": _max,
    "near-solve(>=0.9)": _near_solve_rate,
}


def _bootstrap_delta_ci(
    cold: list[float],
    warm: list[float],
    stat,
    *,
    n_boot: int = BOOTSTRAP_RESAMPLES,
    seed: int = BOOTSTRAP_SEED,
) -> tuple[float, float, float]:
    """Point estimate + 95% percentile bootstrap CI of Δ = stat(warm) − stat(cold).

    Pure-python, fixed-seed. The two per-arm pools are resampled INDEPENDENTLY with
    replacement (the cells are not paired here — this is a pooled, distribution-shape
    test), and the statistic is recomputed on each resample so the CI is valid for
    percentile/max statistics, not just the mean."""
    point = stat(warm) - stat(cold)
    if not cold or not warm:
        return point, 0.0, 0.0
    rng = random.Random(seed)
    nc, nw = len(cold), len(warm)
    boots: list[float] = []
    for _ in range(n_boot):
        bc = [cold[rng.randrange(nc)] for _ in range(nc)]
        bw = [warm[rng.randrange(nw)] for _ in range(nw)]
        boots.append(stat(bw) - stat(bc))
    boots.sort()
    lo = boots[int(0.025 * n_boot)]
    hi = boots[int(0.975 * n_boot)]
    return point, lo, hi


def compute_tail_summary(cold: list[float], warm: list[float]) -> dict:
    """Per-arm tail stats + warm−cold Δ with 95% bootstrap CI, for every TAIL_STAT."""
    out: dict[str, dict] = {}
    for name, stat in TAIL_STATS.items():
        cold_v = stat(cold)
        warm_v = stat(warm)
        delta, lo, hi = _bootstrap_delta_ci(cold, warm, stat)
        out[name] = {
            "cold": cold_v,
            "warm": warm_v,
            "delta": delta,
            "ci95": [lo, hi],
        }
    return {
        "stats": out,
        "n_cold": len(cold),
        "n_warm": len(warm),
        "near_solve_threshold": NEAR_SOLVE_THRESHOLD,
    }


def print_tail_table(summary: dict, *, title: str) -> None:
    """Readable table: stat | cold | warm | Δ(warm−cold) | 95% CI."""
    print(f"\n=== {title} (HEAVY-TAIL TEST — does memory fatten the UPPER tail?) ===", flush=True)
    print(
        f"  pooled cells: cold n={summary['n_cold']}, warm n={summary['n_warm']}  "
        f"(near-solve = gap_closed >= {summary['near_solve_threshold']})",
        flush=True,
    )
    header = f"  {'stat':<18} {'cold':>9} {'warm':>9} {'Δ(w−c)':>10}  {'95% CI':>22}"
    print(header, flush=True)
    print("  " + "-" * (len(header) - 2), flush=True)
    for name, row in summary["stats"].items():
        ci = f"[{row['ci95'][0]:+.4f}, {row['ci95'][1]:+.4f}]"
        print(
            f"  {name:<18} {row['cold']:>9.4f} {row['warm']:>9.4f} "
            f"{row['delta']:>+10.4f}  {ci:>22}",
            flush=True,
        )
    # Verdict on the upper tail (the headline): any of p90/max/near-solve has a
    # Δ whose 95% CI excludes 0 on the high side → warm's upper tail genuinely exceeds.
    upper = ["p90", "max", "near-solve(>=0.9)"]
    fattened = [k for k in upper if k in summary["stats"] and summary["stats"][k]["ci95"][0] > 0]
    if fattened:
        print(
            f"  → UPPER TAIL FATTENED by memory on: {', '.join(fattened)} "
            "(Δ 95% CI excludes 0) — heavy-tail hypothesis SUPPORTED.",
            flush=True,
        )
    else:
        print(
            "  → no upper-tail statistic has a Δ 95% CI excluding 0 — "
            "heavy-tail hypothesis NOT supported by this pool.",
            flush=True,
        )


# ---------------- planned cells ----------------


def _parse_seeds(spec: str) -> list[int]:
    """'1..20' → [1..20]; '1,2,3' → [1,2,3]; mix allowed ('1..3,7')."""
    out: list[int] = []
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if ".." in part:
            a, b = part.split("..", 1)
            out.extend(range(int(a), int(b) + 1))
        else:
            out.append(int(part))
    return out


def planned_cells(problems, seeds) -> list[tuple[str, str, int]]:
    """Every (arm, problem_id, seed) cell that will be run, in execution order
    (per arm, per seed, problems in sequence_index order)."""
    ordered = sorted(problems, key=lambda p: p.sequence_index)
    cells: list[tuple[str, str, int]] = []
    for arm in ca.Arm:
        for seed in seeds:
            for p in ordered:
                cells.append((arm.value, p.problem_id, seed))
    return cells


# ---------------- resume ----------------


def _load_done(records_path: Path) -> dict[tuple[str, int], set[str]]:
    """Rebuild skip_done from the append-only records.jsonl: (arm, seed) → solved
    problem_ids. A crashed batch resumes by skipping these cells."""
    done: dict[tuple[str, int], set[str]] = {}
    if not records_path.exists():
        return done
    for line in records_path.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        r = json.loads(line)
        done.setdefault((r["arm"], int(r["seed"])), set()).add(r["problem_id"])
    return done


def _pools_from_records(records_path: Path) -> tuple[list[float], list[float], list[dict]]:
    """Read records.jsonl → (cold_gaps, warm_gaps, all_record_dicts)."""
    cold: list[float] = []
    warm: list[float] = []
    recs: list[dict] = []
    if not records_path.exists():
        return cold, warm, recs
    for line in records_path.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        r = json.loads(line)
        recs.append(r)
        (warm if r["arm"] == "warm" else cold).append(float(r["gap_closed"]))
    return cold, warm, recs


# ---------------- synthetic dry-run pools ----------------


def _synthetic_pools(n: int = 60) -> tuple[list[float], list[float]]:
    """Synthetic per-cell gap arrays for --dry-run: cold is low-ish (Beta-like mass
    near 0, thin upper tail); warm = the SAME bulk with a fattened upper tail (a
    fraction of cells pushed toward 1.0). Same mean-ish bulk, heavier warm tail —
    exactly the heavy-tail signal the real test looks for."""
    rng = random.Random(2026)
    cold: list[float] = []
    warm: list[float] = []
    for _ in range(n):
        # Beta-ish low: product of two uniforms skews toward 0.
        base = rng.random() * rng.random()
        cold.append(min(1.0, base))
        # Warm: same base, but ~25% of cells get a tail kick toward a near-solve.
        if rng.random() < 0.25:
            warm.append(min(1.0, 0.9 + 0.1 * rng.random()))
        else:
            warm.append(min(1.0, base))
    return cold, warm


# ---------------- main ----------------


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--config",
        default=str(_REPO / "config" / "ablation_heilbronn_problems.yaml"),
        help="problem set (the Heilbronn family with confirmed Haiku headroom)",
    )
    ap.add_argument(
        "--problem-ids",
        default="heil-n13,heil-n14,heil-n15",
        help="comma list of problem_ids to use (subset of --config); warm needs >=2",
    )
    ap.add_argument("--seeds", default="1..20", help="seed spec, e.g. '1..20' or '1,2,3'")
    ap.add_argument(
        "--solve-timeout",
        type=int,
        default=400,
        help="per-session solve budget in seconds (held equal across arms)",
    )
    ap.add_argument("--model", default="haiku")
    ap.add_argument("--results-dir", default=str(_REPO / "results" / "memory-tail"))
    ap.add_argument("--checkout-root", default=str(_REPO / "ablation-build"))
    ap.add_argument(
        "--max-lesson-chars",
        type=int,
        default=None,
        help="cap on Warm's accumulated-lesson context (equal max context across arms)",
    )
    ap.add_argument("--dry-run", action="store_true", help="plan + synthetic tail demo; no LLM")
    args = ap.parse_args(argv[1:])

    seeds = _parse_seeds(args.seeds)
    wanted = [pid.strip() for pid in args.problem_ids.split(",") if pid.strip()]
    all_problems = ca.load_problems(args.config)
    by_id = {p.problem_id: p for p in all_problems}
    missing = [pid for pid in wanted if pid not in by_id]
    if missing:
        print(f"unknown problem_ids {missing}; config has {sorted(by_id)}", flush=True)
        return 1
    problems = [by_id[pid] for pid in wanted]

    cells = planned_cells(problems, seeds)
    print(
        f"plan: {len(problems)} problems × {len(seeds)} seeds × 2 arms = {len(cells)} cells "
        f"(model={args.model}, solve-timeout={args.solve_timeout}s, resumable)",
        flush=True,
    )
    print(f"  problems: {[p.problem_id for p in problems]}", flush=True)
    print(f"  seeds:    {seeds}", flush=True)
    print("  planned (arm, problem, seed) cells:", flush=True)
    for arm, pid, seed in cells:
        print(f"    {arm:<5} {pid:<10} seed={seed}", flush=True)

    if args.dry_run:
        print(
            "\n[dry-run] NO LLM calls. Exercising tail-DV + bootstrap on SYNTHETIC pools "
            "(cold low-ish; warm = cold bulk with a fattened upper tail).",
            flush=True,
        )
        cold, warm = _synthetic_pools()
        summary = compute_tail_summary(cold, warm)
        print_tail_table(summary, title="SYNTHETIC tail demo")
        print("\n[dry-run] done — no records written, no sessions launched.", flush=True)
        return 0

    # ---- real run (resumable) ----
    checkout_root = Path(args.checkout_root)
    for arm in ("cold", "warm"):
        if not (checkout_root / f"einstein-{arm}").is_dir():
            print(
                f"missing clean-room checkout {checkout_root}/einstein-{arm} — "
                "build it first (scripts/build_ablation_repos.sh), as run_ablation.py does",
                flush=True,
            )
            return 1

    results_dir = Path(args.results_dir)
    results_dir.mkdir(parents=True, exist_ok=True)
    records_path = results_dir / "records.jsonl"
    done = _load_done(records_path)

    telemetry: list = []
    solve_fn = ar.make_solve_fn(
        checkout_root,
        model=args.model,
        timeout_seconds=args.solve_timeout,
        telemetry=telemetry,
        transcripts_dir=results_dir / "transcripts",
    )

    def on_record(rec) -> None:
        with records_path.open("a") as fh:
            fh.write(json.dumps(rec.to_dict()) + "\n")
            fh.flush()

    for arm in ca.Arm:
        for seed in seeds:
            skip = done.get((arm.value, seed), set())
            if {p.problem_id for p in problems}.issubset(skip):
                print(f"[skip] {arm.value} seed={seed} — all cells already recorded", flush=True)
                continue
            kb = ca.RunKB(results_dir / "run-kb" / f"{arm.value}-{seed}")
            print(f"[run] {arm.value} seed={seed} (skip_done={sorted(skip) or '∅'})", flush=True)
            ca.run_arm_sequence(
                arm,
                seed,
                problems,
                solve_fn,
                kb,
                max_lesson_chars=args.max_lesson_chars,
                order=ca.cyclic_order(problems, seed),
                skip_done=skip or None,
                on_record=on_record,
            )

    # ---- tail analysis over the full pool ----
    cold, warm, recs = _pools_from_records(records_path)
    summary = compute_tail_summary(cold, warm)
    summary["records"] = recs
    summary["problem_ids"] = wanted
    summary["seeds"] = seeds
    summary["solve_timeout_s"] = args.solve_timeout
    summary["model"] = args.model
    out_path = results_dir / "tail-summary.json"
    out_path.write_text(json.dumps(summary, indent=2))
    print_tail_table(summary, title="Heilbronn cold-vs-warm")
    print(f"\nwrote {out_path}  ({len(recs)} per-cell records)", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
