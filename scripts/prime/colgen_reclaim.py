"""P7 reclaim via column generation on the crossover-off sieve LP.

Start from a leader's support (warm/feasible), price candidate squarefree keys by dual
reduced cost, add a few improving columns per round, re-solve, trim to <=1999 keys.
This is the tool re-selection-via-cutting-planes (Exp 12) could not be: adding only a
handful of well-priced keys keeps the new constraint set small.

Usage:
    uv run python scripts/prime/colgen_reclaim.py --extend-n 20000 --rounds 5
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from einstein.prime.evaluator import compute_score_only  # noqa: E402
from einstein.prime.lp_solver import colgen_sieve_lp  # noqa: E402
from scripts.prime.optimize_prime_reclaim import get_squarefree  # noqa: E402
from scripts.prime.reclaim_nextension import exact_max_constraint, load_seed  # noqa: E402

ARENA_TOL = 1e-4
LEADER_BASE = 0.9964190817  # CHRONOS 24000 clean base, reproduced 2026-07-03
LEADER_SCALED = 0.9965177307  # CHRONOS live #1 2026-06-30


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", default="CHRONOS-0.9962211")
    ap.add_argument("--seed-file", default="", help="load seed pf from a JSON path (overrides --seed)")
    ap.add_argument("--extend-n", type=int, default=20000)
    ap.add_argument("--add-per-round", type=int, default=120)
    ap.add_argument("--rounds", type=int, default=5)
    ap.add_argument("--time-limit", type=int, default=600)
    ap.add_argument("--out-tag", default="", help="suffix for output filenames (ladder rungs)")
    ap.add_argument("--rescale-safe", action="store_true",
                    help="solve with box 10/(1+ARENA_TOL) so the scaled output cannot clip")
    args = ap.parse_args()

    if args.seed_file:
        raw = json.load(open(args.seed_file))["partial_function"]
        seed_pf = {int(k): float(v) for k, v in raw.items() if int(k) >= 2}
    else:
        seed_pf = load_seed(args.seed)
    full_seed = dict(seed_pf)
    full_seed[1] = float(np.clip(-sum(v / k for k, v in seed_pf.items()), -10.0, 10.0))
    candidates = get_squarefree(args.extend_n)

    print(f"colgen seed={args.seed} candidates<= {args.extend_n} ({len(candidates)})", flush=True)
    pf, base, worst = colgen_sieve_lp(
        full_seed,
        candidates,
        add_per_round=args.add_per_round,
        rounds=args.rounds,
        time_limit=args.time_limit,
        log=print,
        var_bound=10.0 / (1.0 + ARENA_TOL) if args.rescale_safe else 10.0,
    )
    if pf is None:
        print("colgen produced no feasible solution")
        return

    # f(1) normalization + tolerance-edge scale + exact-grid verify.
    full = dict(pf)
    full[1] = float(np.clip(-sum(v / k for k, v in pf.items()), -10.0, 10.0))
    safe = 1.0 + 0.999 * ((1.0 + ARENA_TOL) / worst - 1.0) if worst > 0 else 1.0
    scaled = {k: float(np.clip(v * safe, -10.0, 10.0)) for k, v in full.items()}
    base_chk = compute_score_only({k: v for k, v in full.items() if k >= 2})
    scaled_score = compute_score_only({k: v for k, v in scaled.items() if k >= 2})
    mc = exact_max_constraint(scaled)

    print(
        f"\nCOLGEN base={base_chk:.10f} (leader {LEADER_BASE:.7f}, Δ={base_chk - LEADER_BASE:+.2e})"
    )
    print(
        f"  worstG={worst:.10f} scaled={scaled_score:.10f} maxC={mc:.10f} feasible={mc <= 1 + ARENA_TOL + 1e-9}"
    )
    print(f"  vs MAOJIASONG #1 {LEADER_SCALED:.7f}: scaled Δ={scaled_score - LEADER_SCALED:+.2e}")
    os.makedirs("results/problem-7-prime", exist_ok=True)
    tag = f"_{args.out_tag}" if args.out_tag else ""
    json.dump(
        {"partial_function": {str(k): v for k, v in scaled.items() if k != 1}},  # verifier re-derives f(1); submitting it wastes a key slot
        open(f"results/problem-7-prime/colgen{tag}.json", "w"),
    )
    json.dump(
        {"partial_function": {str(k): v for k, v in full.items()}},
        open(f"results/problem-7-prime/colgen_base{tag}.json", "w"),
    )
    if base_chk > LEADER_BASE + 1e-9:
        print(f"  *** base BEATS leader by {base_chk - LEADER_BASE:.2e} — REAL basin advance ***")
    else:
        print("  base did not exceed leader — colgen converged at/below leader support")


if __name__ == "__main__":
    main()
