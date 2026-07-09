"""Construct the AKC multiscale family at a target reach and solve it box-aware.

Family (published by Agent-Knowledge-Cycle, thread 244, 2026-07-03): dense squarefree
prefix (<=1800) + geometric squarefree tail to `reach`, 2000 keys, honest RHS=1.
We calibrate the tail count from their live 32001-key payload, regenerate the tail
geometrically to the new reach, solve with the rescale-safe box, and triple-verify.

    uv run python scripts/prime/family_reach.py --reach 48000
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from einstein.prime.evaluator import compute_score_only, evaluate  # noqa: E402
from einstein.prime.lp_solver import solve_sieve_lp  # noqa: E402

ARENA_TOL = 1e-4
PREFIX_MAX = 1800
MB_SOL = Path(__file__).resolve().parents[2] / ".mb/problems/7-prime-number-theorem/solutions"


def squarefree_up_to(n: int) -> list[int]:
    sieve = np.ones(n + 1, dtype=bool)
    d = 2
    while d * d <= n:
        sieve[d * d :: d * d] = False
        d += 1
    return [int(k) for k in range(2, n + 1) if sieve[k]]


def nearest_squarefree(x: int, sf_set: set[int], hi: int) -> int | None:
    for off in range(0, 200):
        for cand in (x - off, x + off):
            if 2 <= cand <= hi and cand in sf_set:
                return cand
    return None


def build_support(reach: int, calibrate_from: str, alpha: float = 1.0) -> list[int]:
    matches = [f for f in glob.glob(str(MB_SOL / "leader-*.json")) if calibrate_from in f]
    raw = json.load(open(sorted(matches)[-1]))["partial_function"]
    akc = sorted(int(k) for k in raw if int(k) >= 2)
    prefix = [k for k in akc if k <= PREFIX_MAX]
    n_tail = 2000 - len(prefix)  # use the full 2000-key budget (AKC used 1999)
    sf = squarefree_up_to(reach)
    sf_set = set(sf)
    lo = PREFIX_MAX + 1
    # c-probe tail law: k_i = lo * (reach/lo) ** ((i/n)^alpha).
    # alpha = 1.0 -> pure geometric (AKC's published family, the control);
    # alpha < 1 -> denser toward the far end; alpha > 1 -> denser near the prefix.
    tail: list[int] = []
    used = set(prefix)
    span = reach / lo
    for i in range(n_tail):
        t = ((i + 0.5) / n_tail) ** alpha
        k = nearest_squarefree(int(round(lo * span ** t)), sf_set, reach)
        if k is not None and k not in used:
            tail.append(k)
            used.add(k)
    # top up from the largest unused squarefree if geometric snapping fell short
    for k in reversed(sf):
        if len(tail) >= n_tail:
            break
        if k > PREFIX_MAX and k not in used:
            tail.append(k)
            used.add(k)
    support = sorted(set(prefix) | set(tail))
    print(f"support: {len(support)} keys  prefix<= {PREFIX_MAX}: {len(prefix)}  "
          f"tail: {len(tail)} (alpha={alpha})  maxkey={support[-1]}")
    return support


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--reach", type=int, default=48000)
    ap.add_argument("--calibrate-from", default="AKC-0.9971452")
    ap.add_argument("--time-limit", type=int, default=3600)
    ap.add_argument("--alpha", type=float, default=1.3, help="tail density exponent (1.0 = geometric)")
    args = ap.parse_args()

    support = build_support(args.reach, args.calibrate_from, alpha=args.alpha)

    # Warm the active set from AKC's pf (shared prefix dominates the binding structure).
    matches = [f for f in glob.glob(str(MB_SOL / "leader-*.json")) if args.calibrate_from in f]
    raw = json.load(open(sorted(matches)[-1]))["partial_function"]
    seed = {int(k): float(v) for k, v in raw.items() if int(k) >= 2}
    seed[1] = float(np.clip(-sum(v / k for k, v in seed.items()), -10.0, 10.0))

    bound = 10.0 / (1.0 + ARENA_TOL)
    f, base, worst, rounds = solve_sieve_lp(
        support, seed, time_limit=args.time_limit, max_rounds=20, log=print, var_bound=bound,
        prune_cap=40000, keep_margin=0.8,  # keep g>0.2 rows — 0.5 dropped rows that re-violated at 144k
    )
    if f is None:
        print("solve failed")
        return

    pf = {k: float(f[j]) for j, k in enumerate(support)}
    pf[1] = float(np.clip(-sum(v / k for k, v in pf.items()), -10.0, 10.0))
    safe = 1.0 + 0.999 * ((1.0 + ARENA_TOL) / worst - 1.0) if worst > 0 else 1.0
    scaled = {k: v * safe for k, v in pf.items()}
    import math as _m
    print(f"\nbase={base:.10f} worstG={worst:.10f} scale={safe:.10f} rounds={rounds}")
    print(f"c = (1-base)*ln(10*reach) = {(1.0 - base) * _m.log(10 * args.reach):.6f}  (alpha={args.alpha})")

    epf = {k: float(np.clip(v, -10.0, 10.0)) for k, v in scaled.items()}
    s = sum(v / k for k, v in epf.items() if k != 1)
    epf[1] = float(np.clip(-s, -10.0, 10.0))
    v1 = compute_score_only({k: v for k, v in epf.items() if k >= 2})
    v3 = evaluate({"partial_function": {str(k): v for k, v in scaled.items() if k != 1}})
    print(f"V1={v1:.10f} V3={v3:.10f} agree={abs(v1-v3)<1e-9}")

    os.makedirs("results/problem-7-prime", exist_ok=True)
    tag = "" if args.alpha == 1.0 else f"_a{args.alpha}"
    out = f"results/problem-7-prime/family_reach_{args.reach}{tag}.json"
    json.dump({"partial_function": {str(k): v for k, v in scaled.items() if k != 1}}, open(out, "w"))
    print(f"saved -> {out}  (run gate_and_submit.py --file {out} --live to submit)")


if __name__ == "__main__":
    main()
