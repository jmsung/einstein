"""Reproduce a P7 leader's clean base by re-solving the sieve LP on their exact support.

The recorded resolving move for the cutting-plane wall (finding
p7-n16000-degeneracy-crossover-off): pool wider than the target support explodes
constraint discovery; the leader's own support converges. Reproduced 0.9962211 at
maxkey=16000; this generalizes it to any leader file.

    uv run python scripts/prime/reproduce_leader_base.py --leader CHRONOS-0.9965177
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
from einstein.prime.evaluator import compute_score_only  # noqa: E402
from einstein.prime.lp_solver import solve_sieve_lp  # noqa: E402

MB_SOL = Path(__file__).resolve().parents[2] / ".mb/problems/7-prime-number-theorem/solutions"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--leader", default="CHRONOS-0.9965177")
    ap.add_argument("--time-limit", type=int, default=1800)
    args = ap.parse_args()

    matches = [f for f in glob.glob(str(MB_SOL / "leader-*.json")) if args.leader in f]
    if not matches:
        raise FileNotFoundError(f"no leader solution matching {args.leader!r}")
    raw = json.load(open(sorted(matches)[-1]))["partial_function"]
    seed = {int(k): float(v) for k, v in raw.items() if int(k) >= 2}
    seed[1] = float(np.clip(-sum(v / k for k, v in seed.items()), -10.0, 10.0))
    keys = sorted(k for k in seed if k >= 2)
    print(f"leader={args.leader} support={len(keys)} maxkey={keys[-1]}")

    f, base, worst, rounds = solve_sieve_lp(
        keys, seed, time_limit=args.time_limit, log=print
    )
    if f is None:
        print("INFEASIBLE / failed")
        return

    pf = {k: float(f[j]) for j, k in enumerate(keys)}
    pf[1] = float(np.clip(-sum(v / k for k, v in pf.items()), -10.0, 10.0))
    score = compute_score_only({k: v for k, v in pf.items() if k >= 2})
    seed_base = compute_score_only(dict(raw.items()) and {int(k): float(v) for k, v in raw.items() if int(k) >= 2})
    print(f"\nbase={base:.10f} evaluator_score={score:.10f} worstG={worst:.10f} rounds={rounds}")
    print(f"leader raw (rescaled) evaluator score for reference: {seed_base:.10f}")

    os.makedirs("results/problem-7-prime", exist_ok=True)
    out = f"results/problem-7-prime/base_{args.leader}_support.json"
    json.dump({"partial_function": {str(k): v for k, v in pf.items()}}, open(out, "w"))
    print(f"saved -> {out}")


if __name__ == "__main__":
    main()
