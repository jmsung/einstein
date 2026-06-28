"""P7 reclaim — warm-start LP from a leader's N=16000 support, then push N.

Experiment 9 (2026-06-28) recon showed the live lever is base-LP N-extension to
~16000 with sparse key selection, NOT the (saturated) tolerance scale. The leaders
MAOJIASONG/CHRONOS reach maxkey=16000; we froze at 3349.

Solver lesson (this branch): a dense cutting-plane LP that starts from the FULL
1..16000 constraint set does not converge (HiGHS IPM timed out at 311s on an
18880x2990 dense matrix). The fix is `warm_extend.py`'s recipe — restrict the LP
VARIABLES to a leader's ~2000-key support (not all ~9700 squarefree to 16000) and
warm-start the CONSTRAINTS from that leader's tight points (G_seed > 0.5) plus a
sparse sample. That keeps the LP the size of the original successful N=3350 runs.

Pipeline:
  1. Load a seed solution (default: CHRONOS, unscaled, feasible at maxC~1.0).
  2. Variables = seed support, optionally extended with squarefree keys in
     (maxkey_seed, N] for the N-extension test.
  3. Warm-started sparse cutting-plane LP, margin=0 (solve to constraint <= 1).
  4. Scale by (1+ARENA_TOL)/worst_G to sit at the tolerance band; verify on the
     exact integer grid; report base + scaled score vs the leader.

Usage:
    uv run python scripts/prime/reclaim_nextension.py                       # re-solve CHRONOS support
    uv run python scripts/prime/reclaim_nextension.py --extend-n 20000      # push N past 16000
    uv run python scripts/prime/reclaim_nextension.py --seed MAOJIASONG
"""

from __future__ import annotations

import argparse
import glob
import json
import math
import os
import sys
import time
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from einstein.prime.evaluator import compute_score_only  # noqa: E402
from scripts.prime.optimize_prime_reclaim import build_solution, get_squarefree  # noqa: E402
from scripts.prime.warm_extend import build_sparse, check_viols  # noqa: E402

ARENA_TOL = 1e-4
LEADER_BASE = 0.9962211  # CHRONOS / MAOJIASONG unscaled base at N=16000
LEADER_SCALED = 0.9963197  # MAOJIASONG scaled
MB_SOL = Path(__file__).resolve().parents[2] / ".mb/problems/7-prime-number-theorem/solutions"


def log(msg: str = "") -> None:
    print(msg, flush=True)


def load_seed(name: str) -> dict[int, float]:
    """Load a saved leader solution by agent-name substring (k >= 2)."""
    matches = [f for f in glob.glob(str(MB_SOL / "leader-*.json")) if name in f]
    if not matches:
        raise FileNotFoundError(f"no leader solution matching {name!r} in {MB_SOL}")
    pf = json.load(open(sorted(matches)[-1]))["partial_function"]
    return {int(k): float(v) for k, v in pf.items() if int(k) >= 2}


def exact_max_constraint(pf: dict[int, float], xcap_mult: int = 10) -> float:
    keys = np.array(sorted(pf), dtype=np.int64)
    vals = np.array([pf[k] for k in keys], dtype=np.float64)
    x_max = xcap_mult * int(keys[-1])
    best = -np.inf
    for start in range(1, x_max + 1, 200_000):
        end = min(start + 200_000, x_max + 1)
        xs = np.arange(start, end, dtype=np.int64)
        g = (xs[:, None] // keys[None, :]).astype(np.float64) @ vals
        best = max(best, float(g.max()))
    return best


def g_of_seed(seed_pf: dict[int, float], max_n: int) -> np.ndarray:
    """G_seed(n) = sum f(k)(floor(n/k) - n/k) over the seed support, n in [0, max_n]."""
    keys = np.array(sorted(seed_pf), dtype=np.float64)
    vals = np.array([seed_pf[int(k)] for k in keys], dtype=np.float64)
    g = np.zeros(max_n + 1)
    for start in range(1, max_n + 1, 100_000):
        end = min(start + 100_000, max_n + 1)
        ns = np.arange(start, end, dtype=np.float64)
        a = np.floor(ns[:, None] / keys[None, :]) - ns[:, None] / keys[None, :]
        g[start:end] = a @ vals
    return g


def solve_warmstarted(
    keys: list[int],
    seed_pf: dict[int, float],
    *,
    xcap_mult: int = 10,
    time_limit: int = 600,
    max_rounds: int = 40,
) -> tuple[np.ndarray | None, float, float]:
    """Warm-started cutting-plane LP. Returns (f_vec, base_score, worst_G)."""
    n_vars = len(keys)
    max_key = max(keys)
    max_n = xcap_mult * max_key
    c_obj = np.array([math.log(k) / k for k in keys], dtype=np.float64)
    bounds = [(-10.0, 10.0)] * n_vars

    g_seed = g_of_seed(seed_pf, max_n)
    tight = [n for n in range(1, max_n + 1) if g_seed[n] > 0.5]
    active_ns = sorted(set(tight) | set(range(1, max_n + 1, 200)))
    log(
        f"  vars={n_vars} maxkey={max_key} range=[1,{max_n}] tight={len(tight)} init_cons={len(active_ns)}"
    )

    margin = 0.0
    best_f, best_score, best_worst = None, -np.inf, 0.0
    for rnd in range(max_rounds):
        t0 = time.time()
        a = build_sparse(keys, active_ns)
        b = np.full(len(active_ns), 1.0 - margin)
        res = linprog(
            c_obj,
            A_ub=a,
            b_ub=b,
            bounds=bounds,
            method="highs",
            options={
                "time_limit": time_limit,
                "primal_feasibility_tolerance": 1e-9,
                "dual_feasibility_tolerance": 1e-9,
            },
        )
        dt = time.time() - t0
        if not res.success:
            log(f"  R{rnd}: FAIL {res.message} ({dt:.0f}s); margin->")
            margin = max(margin * 2, 1e-8)
            if margin > 0.01:
                break
            continue
        score = -res.fun
        _, worst_G, viols = check_viols(keys, res.x, max_n)
        log(
            f"  R{rnd}: base={score:.10f} cons={len(active_ns)} viol={len(viols)} worstG={worst_G:.10f} {dt:.0f}s"
        )
        if not viols:
            return res.x.copy(), score, worst_G
        if score > best_score:
            best_f, best_score, best_worst = res.x.copy(), score, worst_G
        new = [n for n in viols[:5000] if n not in set(active_ns)]
        if not new:
            margin = max(margin * 2, 1e-8)
            if margin > 0.01:
                break
            continue
        active_ns = sorted(set(active_ns) | set(new))
    return best_f, best_score, best_worst


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", default="CHRONOS-0.9962211", help="leader solution name substring")
    ap.add_argument(
        "--extend-n", type=int, default=0, help="add squarefree keys in (maxkey_seed, N]"
    )
    ap.add_argument("--time-limit", type=int, default=600)
    args = ap.parse_args()

    seed_pf = load_seed(args.seed)
    seed_keys = sorted(seed_pf)
    keys = set(seed_keys)
    label = f"seed={args.seed}"
    if args.extend_n > max(seed_keys):
        ext = [k for k in get_squarefree(args.extend_n) if k > max(seed_keys)]
        keys |= set(ext)
        label += f"+sf({max(seed_keys)},{args.extend_n}]={len(ext)}"
    keys = sorted(keys)

    log(f"\n{'=' * 70}\n{label}: {len(keys)} vars\n{'=' * 70}")
    f, base, worst_G = solve_warmstarted(keys, seed_pf, time_limit=args.time_limit)
    if f is None or worst_G <= 0:
        log("  no feasible base solution")
        return

    safe_scale = 1.0 + 0.999 * ((1.0 + ARENA_TOL) / worst_G - 1.0)
    pf = build_solution(keys, f)
    base_chk = compute_score_only(pf)
    scaled_pf = {k: float(np.clip(v * safe_scale, -10.0, 10.0)) for k, v in pf.items()}
    scaled = compute_score_only(scaled_pf)
    mc_scaled = exact_max_constraint(scaled_pf)
    feasible = mc_scaled <= 1.0 + ARENA_TOL + 1e-9

    log(f"\n  base={base_chk:.10f}  worstG={worst_G:.10f}  scale={safe_scale:.7f}")
    log(
        f"  scaled={scaled:.10f}  exact maxC={mc_scaled:.10f}  feasible(<=1+{ARENA_TOL:g})={feasible}"
    )
    log(
        f"  vs leader: base Δ={base_chk - LEADER_BASE:+.2e}  scaled Δ={scaled - LEADER_SCALED:+.2e}"
    )

    os.makedirs("results/problem-7-prime", exist_ok=True)
    tag = (
        label.replace("=", "").replace("(", "").replace("]", "").replace(",", "_").replace(" ", "")
    )
    out = f"results/problem-7-prime/nextension_{tag}.json"
    json.dump({"partial_function": {str(k): v for k, v in scaled_pf.items()}}, open(out, "w"))
    log(f"  saved -> {out}")
    if scaled > LEADER_SCALED and feasible:
        log(
            f"  *** BEATS arena #1 {LEADER_SCALED:.7f} by {scaled - LEADER_SCALED:.2e} (pre triple-verify) ***"
        )


if __name__ == "__main__":
    main()
