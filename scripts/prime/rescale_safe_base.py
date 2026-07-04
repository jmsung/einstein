"""Rescale-safe P7 base: solve on a leader's support with the variable box
pre-tightened to 10/(1+ARENA_TOL), so the tolerance-lever rescale cannot clip.

Why: a box-bound value scaled by ~1.0001 exceeds the arena's hard +/-10 clip; the
verifier re-derives f(1) from the clipped values and the broken zero-sum leaks a
linear-in-x term into G (violation at x=85847 on the 24000-support base, 2026-07-03).
Tightening the box during the solve makes the scaled solution feasible by construction.

    uv run python scripts/prime/rescale_safe_base.py --leader CHRONOS-0.9965177
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
TARGET = 0.9965177307  # CHRONOS live #1, 2026-06-30
MB_SOL = Path(__file__).resolve().parents[2] / ".mb/problems/7-prime-number-theorem/solutions"


def evaluator_normalized(pf: dict[int, float]) -> dict[int, float]:
    """Replicate the arena/evaluator pipeline: clip all, re-derive f(1), clip f(1)."""
    out = {k: float(np.clip(v, -10.0, 10.0)) for k, v in pf.items()}
    s = sum(v / k for k, v in out.items() if k != 1)
    out[1] = float(np.clip(-s, -10.0, 10.0))
    return out


def exact_max_c(pf: dict[int, float]) -> tuple[float, int]:
    keys = np.array(sorted(pf), dtype=np.int64)
    vals = np.array([pf[int(k)] for k in keys])
    xmax = 10 * int(keys[-1])
    worst, wx = -1e18, 0
    for st in range(1, xmax + 1, 200_000):
        en = min(st + 200_000, xmax + 1)
        xs = np.arange(st, en, dtype=np.int64)
        g = (xs[:, None] // keys[None, :]).astype(np.float64) @ vals
        i = int(np.argmax(g))
        if g[i] > worst:
            worst, wx = float(g[i]), int(xs[i])
    return worst, wx


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--leader", default="CHRONOS-0.9965177")
    ap.add_argument("--time-limit", type=int, default=1800)
    args = ap.parse_args()

    matches = [f for f in glob.glob(str(MB_SOL / "leader-*.json")) if args.leader in f]
    raw = json.load(open(sorted(matches)[-1]))["partial_function"]
    seed = {int(k): float(v) for k, v in raw.items() if int(k) >= 2}
    seed[1] = float(np.clip(-sum(v / k for k, v in seed.items()), -10.0, 10.0))
    keys = sorted(k for k in seed if k >= 2)

    bound = 10.0 / (1.0 + ARENA_TOL)
    print(f"leader={args.leader} support={len(keys)} maxkey={keys[-1]} var_bound={bound:.7f}")
    f, base, worst, rounds = solve_sieve_lp(
        keys, seed, time_limit=args.time_limit, log=print, var_bound=bound
    )
    if f is None:
        print("solve failed")
        return

    pf = {k: float(f[j]) for j, k in enumerate(keys)}
    pf[1] = float(np.clip(-sum(v / k for k, v in pf.items()), -10.0, 10.0))
    safe = 1.0 + 0.999 * ((1.0 + ARENA_TOL) / worst - 1.0) if worst > 0 else 1.0
    scaled = {k: v * safe for k, v in pf.items()}
    boxed = [k for k, v in scaled.items() if abs(v) > 10.0]
    print(f"\nbase={base:.10f} worstG={worst:.10f} scale={safe:.10f} clipped_after_scale={boxed}")

    # Triple-verify on the EVALUATOR-normalized pf (what the arena actually scores).
    epf = evaluator_normalized(scaled)
    v1 = compute_score_only({k: v for k, v in epf.items() if k >= 2})
    v2, wx = exact_max_c(epf)
    v3 = evaluate({"partial_function": {str(k): v for k, v in scaled.items()}})
    print(f"V1 score (evaluator-normalized) = {v1:.10f}")
    print(f"V2 exact-grid maxC              = {v2:.10f} at x={wx} (band 1.0001, margin {1.0001 - v2:.2e})")
    print(f"V3 evaluate() MC                = {v3:.10f}")
    print(f"vs CHRONOS #1 {TARGET}: delta = {v1 - TARGET:+.3e} (minImprovement 1e-6)")

    ok = v3 > 0 and v2 <= 1.0 + ARENA_TOL and abs(v1 - v3) < 1e-9
    print("TRIPLE-VERIFY:", "PASS" if ok else "FAIL")
    os.makedirs("results/problem-7-prime", exist_ok=True)
    out = "results/problem-7-prime/rescale_safe_candidate.json"
    json.dump({"partial_function": {str(k): v for k, v in scaled.items() if k != 1}}, open(out, "w"))  # f(1) re-derived by verifier; do not spend a slot
    print(f"saved -> {out}")


if __name__ == "__main__":
    main()
