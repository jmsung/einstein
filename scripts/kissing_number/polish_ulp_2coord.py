"""Intra-row 2-coordinate joint ulp polisher for P6 Kissing Number.

Extension of polish_ulp_coord.py: after single-coord descent converges,
try simultaneous perturbations on two coordinates of the same row. This
escapes local minima where no single-coord move helps but a joint pair move
does (e.g., rotating the vector slightly in a 2D subspace).

For each row i, we try all C(11,2)=55 coordinate pairs and all
(±1, ±1), (±1, ±2), (±2, ±1), (±2, ±2) step combinations, totaling 55×16=880
trials per row — 20× slower than single-coord but explores joint moves.

Usage:
    uv run python scripts/kissing_number/polish_ulp_2coord.py \
        --warm-start results/problem-6-kissing-number/solution_best_mpmath.json \
        --budget 1800
"""

from __future__ import annotations

import argparse
import itertools
import json
import os
import time
from pathlib import Path

import numpy as np
from mpmath import mp, mpf, sqrt as mpsqrt

from einstein.kissing_number.evaluator import overlap_loss_mpmath

N = 594
D = 11
RESULTS = Path("results/problem-6-kissing-number")
POLISH_TRAIL = RESULTS / "polish-trail"


def load_vectors(path: str) -> list[list[float]]:
    with open(path) as f:
        data = json.load(f)
    if "data" in data and "vectors" in data["data"]:
        return data["data"]["vectors"]
    if "vectors" in data:
        return data["vectors"]
    raise ValueError(f"no vectors found in {path}")


def mp_centers(V_mp: list[list[mpf]]) -> list[list[mpf]]:
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


def mp_row_contrib(C: list[list[mpf]], i: int) -> mpf:
    """Sum of (2 - dist) over all active pairs involving row i."""
    two = mpf(2)
    Ci = C[i]
    n = len(C)
    d = len(Ci)
    total = mpf(0)
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
            total += two - dist
    return total


def mp_row_contrib_with(Ci_new: list[mpf], C: list[list[mpf]], i: int) -> mpf:
    two = mpf(2)
    n = len(C)
    d = len(Ci_new)
    total = mpf(0)
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
            total += two - dist
    return total


def step_coord(v_ik: float, k_ulps: int) -> float:
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


def compute_row_centers(v_row_f64: np.ndarray, dps: int) -> list[mpf]:
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
    parser.add_argument("--max-ulps", type=int, default=2)
    parser.add_argument("--max-sweeps", type=int, default=3)
    parser.add_argument("--row-order", type=str, default="gap",
                        choices=["gap", "seq"])
    parser.add_argument("--top-rows", type=int, default=200,
                        help="Process only top-N rows by gap contribution each sweep")
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()

    print("=" * 78)
    print(f"2-COORD ULP POLISHER  dps={args.dps}  max_ulps={args.max_ulps}  "
          f"top_rows={args.top_rows}")
    print("=" * 78)

    mp.dps = args.dps

    raw = load_vectors(args.warm_start)
    v = np.array(raw, dtype=np.float64)

    V_mp = [[mpf(repr(float(v[i, k]))) for k in range(D)] for i in range(N)]
    C = mp_centers(V_mp)
    total = mp_score_full(C)
    print(f"Warm-start: {args.warm_start}")
    print(f"  initial mpmath score = {float(total):.12e}")

    best_v = v.copy()
    best_score = total

    # Build step patterns: all non-zero 2-tuples of ulps, excluding (0, 0)
    ulp_range = list(range(-args.max_ulps, args.max_ulps + 1))
    step_pairs = [(s1, s2) for s1 in ulp_range for s2 in ulp_range if (s1, s2) != (0, 0)]
    coord_pairs = list(itertools.combinations(range(D), 2))
    print(f"  step patterns: {len(step_pairs)}  coord pairs/row: {len(coord_pairs)}")
    print(f"  trials per row: {len(step_pairs) * len(coord_pairs)}")

    t_start = time.time()
    total_tries = 0
    total_accepts = 0

    for sweep in range(args.max_sweeps):
        if time.time() - t_start > args.budget:
            print("budget exhausted")
            break

        # prioritize rows by current gap contribution
        row_contribs = [(i, float(mp_row_contrib(C, i))) for i in range(N)]
        if args.row_order == "gap":
            row_contribs.sort(key=lambda x: -x[1])

        # limit to top-rows
        rows_to_process = row_contribs[: args.top_rows]

        sweep_accepts = 0
        sweep_start = best_score
        print(f"\n--- sweep {sweep + 1}  ({len(rows_to_process)} rows) ---", flush=True)
        last_print = time.time()

        for ridx, (i, rc) in enumerate(rows_to_process):
            if time.time() - t_start > args.budget:
                break
            if rc == 0:
                continue

            old_contrib = mp_row_contrib(C, i)
            row_accepts = 0

            for k1, k2 in coord_pairs:
                best_delta = mpf(0)
                best_pair = None
                best_Ci = None
                for s1, s2 in step_pairs:
                    cur_k1 = float(best_v[i, k1])
                    cur_k2 = float(best_v[i, k2])
                    new_k1 = step_coord(cur_k1, s1)
                    new_k2 = step_coord(cur_k2, s2)
                    if new_k1 == cur_k1 and new_k2 == cur_k2:
                        continue
                    new_row = best_v[i].copy()
                    new_row[k1] = new_k1
                    new_row[k2] = new_k2
                    Ci_new = compute_row_centers(new_row, args.dps)
                    new_contrib = mp_row_contrib_with(Ci_new, C, i)
                    total_tries += 1
                    delta = old_contrib - new_contrib
                    if delta > best_delta:
                        best_delta = delta
                        best_pair = (s1, s2, new_k1, new_k2)
                        best_Ci = Ci_new

                if best_pair is not None:
                    s1, s2, new_k1, new_k2 = best_pair
                    best_v[i, k1] = new_k1
                    best_v[i, k2] = new_k2
                    V_mp[i] = [mpf(repr(float(x))) for x in best_v[i]]
                    C[i] = best_Ci
                    old_contrib -= best_delta
                    best_score = best_score - best_delta
                    sweep_accepts += 1
                    total_accepts += 1
                    row_accepts += 1

            if time.time() - last_print > 20:
                print(
                    f"  row {ridx+1:4d}/{len(rows_to_process)}  (i={i:3d})  "
                    f"score={float(best_score):.10e}  "
                    f"accepts={sweep_accepts}  tries={total_tries}  "
                    f"elapsed={time.time()-t_start:.0f}s",
                    flush=True,
                )
                last_print = time.time()

        sweep_delta = float(sweep_start - best_score)
        print(
            f"  SWEEP {sweep + 1} DONE  accepts={sweep_accepts}  "
            f"score={float(best_score):.12e}  Δ={sweep_delta:+.3e}",
            flush=True,
        )

        if sweep_accepts > 0:
            v_out = best_v.copy()
            verify_score = overlap_loss_mpmath(v_out, dps=args.dps)
            out = {
                "vectors": v_out.tolist(),
                "score": verify_score,
                "source": f"polish_ulp_2coord:sweep{sweep+1}",
            }
            path = RESULTS / "solution_best_mpmath.json"
            try:
                with open(path) as f:
                    cur = json.load(f).get("score", float("inf"))
            except FileNotFoundError:
                cur = float("inf")
            if verify_score < cur:
                with open(path.with_suffix(".json.tmp"), "w") as f:
                    json.dump(out, f)
                os.replace(path.with_suffix(".json.tmp"), path)
                POLISH_TRAIL.mkdir(parents=True, exist_ok=True)
                trail = POLISH_TRAIL / f"ulp-2coord-sweep{sweep+1}-{verify_score:.6e}.json"
                with open(trail, "w") as f:
                    json.dump(out, f)
                print(f"  >>> SAVED {verify_score:.12e}", flush=True)

        if sweep_accepts == 0:
            print("  no improvements — converged")
            break

    print()
    print("=" * 78)
    print(f"FINAL: {float(best_score):.15e}")
    print(f"accepts={total_accepts}  tries={total_tries}")
    print("=" * 78)


if __name__ == "__main__":
    main()
