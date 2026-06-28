"""P7 reclaim — warm-start the N=16000 sieve LP (crossover-off HiGHS), re-select keys.

Experiment 9 (2026-06-28) recon showed the live lever is base-LP N-extension to ~16000
with sparse key selection, NOT the (saturated) tolerance scale. Experiment 10 hit a
solver wall: scipy.linprog stalls on the degenerate N=16000 LP. The fix lives in
`einstein.prime.lp_solver.solve_sieve_lp` (HiGHS IPM, crossover OFF) — it solves the
same LP to Optimal in ~320s.

Pipeline:
  1. Pool of candidate keys = union of leader supports (and/or squarefree to N).
  2. Phase 1: solve the LP on the full pool.
  3. Phase 2: select the top <=1999 keys by objective contribution, re-solve (the
     cardinality cap is <=2000 squarefree coefficients).
  4. Scale by (1+ARENA_TOL)/worst_G to the tolerance band; verify on the exact integer
     grid; report base + scaled vs the leader.

Usage:
    uv run python scripts/prime/reclaim_nextension.py                 # union of leaders
    uv run python scripts/prime/reclaim_nextension.py --extend-n 20000
"""

from __future__ import annotations

import argparse
import glob
import json
import math
import os
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from einstein.prime.evaluator import compute_score_only  # noqa: E402
from einstein.prime.lp_solver import solve_sieve_lp  # noqa: E402
from scripts.prime.optimize_prime_reclaim import build_solution, get_squarefree  # noqa: E402

ARENA_TOL = 1e-4
LEADER_BASE = 0.9962211
LEADER_SCALED = 0.9963197
MB_SOL = Path(__file__).resolve().parents[2] / ".mb/problems/7-prime-number-theorem/solutions"


def log(msg: str = "") -> None:
    print(msg, flush=True)


def load_seed(name: str) -> dict[int, float]:
    matches = [f for f in glob.glob(str(MB_SOL / "leader-*.json")) if name in f]
    if not matches:
        raise FileNotFoundError(f"no leader solution matching {name!r}")
    pf = json.load(open(sorted(matches)[-1]))["partial_function"]
    return {int(k): float(v) for k, v in pf.items() if int(k) >= 2}


def all_leader_keys() -> set[int]:
    keys: set[int] = set()
    for fn in glob.glob(str(MB_SOL / "leader-*.json")):
        pf = json.load(open(fn))["partial_function"]
        keys.update(int(k) for k in pf if int(k) >= 2)
    return keys


def exact_max_constraint(pf: dict[int, float], xcap_mult: int = 10) -> float:
    keys = np.array(sorted(pf), dtype=np.int64)
    vals = np.array([pf[k] for k in keys], dtype=np.float64)
    x_max = xcap_mult * int(keys[-1])
    best = -np.inf
    for start in range(1, x_max + 1, 200_000):
        end = min(start + 200_000, x_max + 1)
        xs = np.arange(start, end, dtype=np.int64)
        best = max(best, float(((xs[:, None] // keys[None, :]).astype(np.float64) @ vals).max()))
    return best


def select_top(keys: list[int], f: np.ndarray, max_keys: int = 1999) -> list[int]:
    contrib = sorted(((abs(f[j]) * math.log(k) / k, k) for j, k in enumerate(keys)), reverse=True)
    return sorted(k for _, k in contrib[:max_keys])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", default="CHRONOS-0.9962211", help="warm-start seed solution")
    ap.add_argument(
        "--extend-n", type=int, default=0, help="add squarefree keys up to N to the pool"
    )
    ap.add_argument("--time-limit", type=int, default=1200)
    args = ap.parse_args()

    seed_pf = load_seed(args.seed)
    full_seed = dict(seed_pf)
    full_seed[1] = float(np.clip(-sum(v / k for k, v in seed_pf.items()), -10.0, 10.0))

    pool = all_leader_keys()
    label = f"union-leaders({len(pool)})"
    if args.extend_n:
        pool |= set(get_squarefree(args.extend_n))
        label = f"union+sf<={args.extend_n}({len(pool)})"
    pool = sorted(pool)

    log(f"\n{'=' * 70}\n{label}: pool={len(pool)} vars (seed={args.seed})\n{'=' * 70}")
    log("Phase 1: solve LP on full pool")
    f1, base1, worst1, _ = solve_sieve_lp(pool, full_seed, time_limit=args.time_limit, log=log)
    if f1 is None:
        log("  phase-1 infeasible")
        return
    selected = select_top(pool, f1, 1999)
    log(f"Phase 2: re-solve on top {len(selected)} keys (maxkey={max(selected)})")
    f2, base2, worst2, _ = solve_sieve_lp(selected, full_seed, time_limit=args.time_limit, log=log)
    if f2 is None:
        log("  phase-2 infeasible")
        return

    pf = build_solution(selected, f2)
    base = compute_score_only({k: v for k, v in pf.items() if k >= 2})
    safe = 1.0 + 0.999 * ((1.0 + ARENA_TOL) / worst2 - 1.0) if worst2 > 0 else 1.0
    scaled_pf = {k: float(np.clip(v * safe, -10.0, 10.0)) for k, v in pf.items()}
    scaled = compute_score_only({k: v for k, v in scaled_pf.items() if k >= 2})
    mc = exact_max_constraint(scaled_pf)
    feasible = mc <= 1.0 + ARENA_TOL + 1e-9

    log(f"\n  base={base:.10f} (leader {LEADER_BASE:.7f}, Δ={base - LEADER_BASE:+.2e})")
    log(f"  scale={safe:.7f} scaled={scaled:.10f} exact maxC={mc:.10f} feasible={feasible}")
    log(f"  vs MAOJIASONG #1 {LEADER_SCALED:.7f}: scaled Δ={scaled - LEADER_SCALED:+.2e}")

    os.makedirs("results/problem-7-prime", exist_ok=True)
    out = f"results/problem-7-prime/nextension_{args.seed}_{label.split('(')[0]}.json"
    json.dump({"partial_function": {str(k): v for k, v in scaled_pf.items()}}, open(out, "w"))
    log(f"  saved -> {out}")
    if base > LEADER_BASE + 1e-9 and feasible:
        log(f"  *** base BEATS leader by {base - LEADER_BASE:.2e} — real basin advance ***")
    elif scaled > LEADER_SCALED and feasible:
        log("  *** scaled edges #1 (tolerance lever) — verify before any submit ***")


if __name__ == "__main__":
    main()
