"""Discrete ulp-level coordinate-descent polisher for P6 Kissing Number.

Motivation
----------
Continuous gradient descent in mpmath + f64 rounding can only improve an
f64 lattice point when the gradient happens to align with a better lattice
neighbor. Once the starting point is a local minimum for that method,
gradient descent stalls.

This polisher works DIRECTLY on the f64 lattice. For each (i, k) coordinate,
it tries v[i][k] ± 1 ulp, ± 2 ulps, ± 4 ulps and measures the incremental
mpmath score change from the ~593 pairs involving vector i. Accept any
strict improvement. Sweep coordinates in priority order: pairs with the
largest per-pair mpmath gap first.

Incremental scoring
-------------------
When only v[i] changes, we only need to recompute:
  - c_i = 2 * v_i_new / ||v_i_new||
  - ||c_i - c_j|| for all j ≠ i  (593 pairs)
and the total mpmath score shifts by:
  delta = sum_{j ≠ i} [max(0, 2 - new_dist_ij) - max(0, 2 - old_dist_ij)]

Usage
-----
    uv run python scripts/kissing_number/polish_ulp_coord.py \
        --warm-start results/problem-6-kissing-number/solution_best_mpmath.json \
        --budget 1800 --max-ulps 4
"""

from __future__ import annotations

import argparse
import json
import os
import random
import time
from pathlib import Path

import numpy as np
from mpmath import mp, mpf, sqrt as mpsqrt

from einstein.kissing_number.evaluator import overlap_loss_mpmath

N = 594
D = 11
RESULTS = Path("results/problem-6-kissing-number")
MB_ROOT = os.environ.get("EINSTEIN_MB_ROOT")
MB_SOLUTIONS = (
    Path(MB_ROOT) / "docs/problem-6-kissing-number/solutions" if MB_ROOT else None
)


def load_vectors(path: str) -> list[list[float]]:
    with open(path) as f:
        data = json.load(f)
    if "data" in data and "vectors" in data["data"]:
        return data["data"]["vectors"]
    if "vectors" in data:
        return data["vectors"]
    raise ValueError(f"no vectors found in {path}")


def mp_centers(V_mp: list[list[mpf]]) -> list[list[mpf]]:
    """c_i = 2*v_i/||v_i|| in mpmath."""
    two = mpf(2)
    out = []
    for row in V_mp:
        nrm = mpsqrt(sum(x * x for x in row))
        out.append([two * x / nrm for x in row])
    return out


def mp_score_full(C: list[list[mpf]]) -> mpf:
    two = mpf(2)
    n = len(C)
    d = len(C[0])
    total = mpf(0)
    for i in range(n):
        Ci = C[i]
        for j in range(i + 1, n):
            Cj = C[j]
            diff2 = mpf(0)
            for k in range(d):
                t = Ci[k] - Cj[k]
                diff2 += t * t
            dist = mpsqrt(diff2)
            if dist < two:
                total += two - dist
    return total


def mp_row_pair_gaps(C: list[list[mpf]], i: int) -> list[mpf]:
    """Return the list of (2 - dist_ij) for all j != i (or 0 if inactive)."""
    two = mpf(2)
    Ci = C[i]
    n = len(C)
    d = len(Ci)
    out = [mpf(0)] * n
    for j in range(n):
        if j == i:
            continue
        Cj = C[j]
        diff2 = mpf(0)
        for k in range(d):
            t = Ci[k] - Cj[k]
            diff2 += t * t
        dist = mpsqrt(diff2)
        if dist < two:
            out[j] = two - dist
    return out


def mp_row_pair_gaps_with(Ci_new: list[mpf], C: list[list[mpf]], i: int) -> list[mpf]:
    """Same as mp_row_pair_gaps but with a provisional new Ci."""
    two = mpf(2)
    n = len(C)
    d = len(Ci_new)
    out = [mpf(0)] * n
    for j in range(n):
        if j == i:
            continue
        Cj = C[j]
        diff2 = mpf(0)
        for k in range(d):
            t = Ci_new[k] - Cj[k]
            diff2 += t * t
        dist = mpsqrt(diff2)
        if dist < two:
            out[j] = two - dist
    return out


def step_coord(v_ik: float, k_ulps: int) -> float:
    """Step v_ik by k ulps (sign-aware). Negative k_ulps → toward -inf."""
    if k_ulps == 0:
        return v_ik
    x = v_ik
    if k_ulps > 0:
        for _ in range(k_ulps):
            x = float(np.nextafter(x, np.inf))
    else:
        for _ in range(-k_ulps):
            x = float(np.nextafter(x, -np.inf))
    return x


def compute_row_mp(
    v_row_f64: np.ndarray, dps: int
) -> list[mpf]:
    """Lift an f64 row to mpmath centers c = 2*v/||v||."""
    mp.dps = dps
    V = [mpf(repr(float(x))) for x in v_row_f64]
    two = mpf(2)
    nrm = mpsqrt(sum(x * x for x in V))
    return [two * x / nrm for x in V]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--warm-start", type=str, required=True)
    parser.add_argument("--dps", type=int, default=50)
    parser.add_argument("--budget", type=int, default=1800)
    parser.add_argument(
        "--target",
        type=float,
        default=None,
        help="Optional score-to-beat for progress reporting (no default).",
    )
    parser.add_argument("--max-ulps", type=int, default=4)
    parser.add_argument("--max-sweeps", type=int, default=20)
    parser.add_argument(
        "--row-order",
        type=str,
        default="gap",
        choices=["gap", "random", "seq"],
        help="gap: process rows with largest total gap first; random: shuffled; seq: 0..N-1",
    )
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()

    target_str = f"target<{args.target:.4e}" if args.target is not None else "no target"
    print("=" * 78)
    print(f"ULP COORDINATE POLISHER  dps={args.dps}  {target_str}")
    print("=" * 78)

    mp.dps = args.dps
    rng = random.Random(args.seed)

    raw = load_vectors(args.warm_start)
    v = np.array(raw, dtype=np.float64)

    # Initial mpmath state
    V_mp = [[mpf(repr(float(v[i, k]))) for k in range(D)] for i in range(N)]
    C = mp_centers(V_mp)
    total = mp_score_full(C)
    print(f"Warm-start: {args.warm_start}")
    print(f"  initial mpmath score = {float(total):.10e}")
    if args.target is not None:
        print(f"  margin vs target     = {args.target - float(total):+.4e}")

    best_v = v.copy()
    best_score = total  # mpf

    # Build step candidates: ±1, ±2, ... ulps
    steps = list(range(-args.max_ulps, args.max_ulps + 1))
    steps.remove(0)

    t_start = time.time()
    total_tries = 0
    total_accepts = 0

    for sweep in range(args.max_sweeps):
        if time.time() - t_start > args.budget:
            print("budget exhausted")
            break

        # prioritize rows by total gap contribution
        row_gaps = []
        for i in range(N):
            row = mp_row_pair_gaps(C, i)
            row_gaps.append((i, sum(float(g) for g in row)))

        if args.row_order == "gap":
            row_gaps.sort(key=lambda x: -x[1])
        elif args.row_order == "random":
            rng.shuffle(row_gaps)
        # seq: leave as-is

        sweep_accepts = 0
        sweep_start_score = best_score
        print(f"\n--- sweep {sweep + 1}  (rows by {args.row_order}) ---", flush=True)
        last_print = time.time()

        for row_idx, (i, row_gap) in enumerate(row_gaps):
            if time.time() - t_start > args.budget:
                break
            if row_gap == 0:
                continue

            old_row = mp_row_pair_gaps(C, i)
            old_contrib = sum(old_row)  # mpf
            row_accepts = 0

            # One linear pass through coords × step magnitudes. Accept in place.
            # Do NOT restart — that was the previous stall.
            for k in range(D):
                cur_v_ik = float(best_v[i, k])
                best_step = 0
                best_delta = mpf(0)
                best_new_row = None
                best_Ci = None
                for s in steps:
                    new_v_ik = step_coord(cur_v_ik, s)
                    if new_v_ik == cur_v_ik:
                        continue
                    new_row_f64 = best_v[i].copy()
                    new_row_f64[k] = new_v_ik
                    Ci_new = compute_row_mp(new_row_f64, args.dps)
                    new_row = mp_row_pair_gaps_with(Ci_new, C, i)
                    new_contrib = sum(new_row)
                    total_tries += 1
                    delta = old_contrib - new_contrib  # positive = improvement
                    if delta > best_delta:
                        best_delta = delta
                        best_step = s
                        best_new_row = new_row
                        best_Ci = Ci_new
                if best_step != 0:
                    new_v_ik = step_coord(float(best_v[i, k]), best_step)
                    best_v[i, k] = new_v_ik
                    new_row_f64 = best_v[i]
                    V_mp[i] = [mpf(repr(float(x))) for x in new_row_f64]
                    C[i] = best_Ci
                    old_row = best_new_row
                    old_contrib = sum(best_new_row)
                    best_score = best_score - best_delta
                    sweep_accepts += 1
                    total_accepts += 1
                    row_accepts += 1

            if time.time() - last_print > 20:
                print(
                    f"  row {row_idx+1:4d}/{len(row_gaps)}  (i={i:3d})  "
                    f"score={float(best_score):.6e}  "
                    f"accepts={sweep_accepts}  tries={total_tries}  "
                    f"elapsed={time.time()-t_start:.0f}s",
                    flush=True,
                )
                last_print = time.time()

        sweep_delta = float(sweep_start_score - best_score)
        print(
            f"  SWEEP {sweep + 1} DONE  accepts={sweep_accepts}  "
            f"score={float(best_score):.10e}  Δ={sweep_delta:+.3e}",
            flush=True,
        )

        # Save after every sweep if improved
        if sweep_accepts > 0:
            v_out = best_v.copy()
            # verify via full evaluator
            verify_score = overlap_loss_mpmath(v_out, dps=args.dps)
            out = {
                "vectors": v_out.tolist(),
                "score": verify_score,
                "source": f"polish_ulp_coord:sweep{sweep+1}",
            }
            path = RESULTS / "solution_best_mpmath.json"
            try:
                with open(path) as f:
                    cur_best = json.load(f).get("score", float("inf"))
            except FileNotFoundError:
                cur_best = float("inf")
            if verify_score < cur_best:
                with open(path.with_suffix(".json.tmp"), "w") as f:
                    json.dump(out, f)
                os.replace(path.with_suffix(".json.tmp"), path)
                if MB_SOLUTIONS is not None:
                    MB_SOLUTIONS.mkdir(parents=True, exist_ok=True)
                    mb = MB_SOLUTIONS / f"ulp-coord-sweep{sweep+1}-{verify_score:.6e}.json"
                    with open(mb, "w") as f:
                        json.dump(out, f)
                print(f"  >>> SAVED {verify_score:.12e}", flush=True)

            if args.target is not None and verify_score < args.target:
                print(f"  TARGET MET: {verify_score:.10e} < {args.target:.10e}")
                # keep going — more margin is better

        if sweep_accepts == 0:
            print("  no improvements in sweep — converged")
            break

    print()
    print("=" * 78)
    print(f"FINAL score: {float(best_score):.15e}")
    print(f"Total accepts: {total_accepts}  tries: {total_tries}")
    print("=" * 78)


if __name__ == "__main__":
    main()
