"""Solve the UNCAPPED board LP at reach K to extract a near-optimal dual, then hand it
to ceiling_certify for a certified S*(K) upper bound.

Board primal (NO 2000-key cap): min_f  sum_k f(k) ln(k)/k
    s.t.  sum_k f(k)(floor(m/k) - m/k) <= TOL(=1.0001),  m = 1..10K-1
          f in [-10, 10]^{K-1}
Score = -objective. HiGHS row duals of the binding <=-rows give y >= 0; y feeds the
weak-duality box certificate B(y) = TOL*sum y + 10*sum_k |c_k - sum_m y_m A_{m,k}|.

This is the piece Russell/CHRONOS walled on at K=48000 (single monolithic LP). We use a
cutting-plane working set + crossover-off IPM so the dual comes from a small active row
set. Extends the certificate ladder past K=12000.

    uv run python scripts/prime/dual_solve.py --K 24000 --time-limit 3600
"""

from __future__ import annotations

import argparse
import math
import time

import numpy as np


def solve_uncapped_dual(K: int, TOL: float = 1.0001, xcap_mult: int = 10,
                        time_limit: int = 3600, max_rounds: int = 30, log=print):
    """Return (m_active, y_float, score_lp) — the dual on the working row set."""
    import highspy

    keys = np.arange(2, K + 1, dtype=np.int64)          # ALL integers (uncapped)
    n = len(keys)
    max_n = xcap_mult * K
    c = np.log(keys.astype(np.float64)) / keys          # minimize c@f  (score = -c@f)
    inf = highspy.kHighsInf

    def build_rows(ns):
        ns = np.asarray(ns, dtype=np.float64).reshape(-1, 1)
        return np.floor(ns / keys.reshape(1, -1)) - ns / keys.reshape(1, -1)

    h = highspy.Highs()
    for opt, val in [("output_flag", False), ("solver", "ipm"), ("run_crossover", "off"),
                     ("primal_feasibility_tolerance", 1e-8), ("dual_feasibility_tolerance", 1e-8),
                     ("time_limit", float(time_limit))]:
        h.setOptionValue(opt, val)
    h.addCols(n, c, np.full(n, -10.0), np.full(n, 10.0), 0, np.array([]), np.array([]), np.array([]))

    step = max(1, max_n // 8000) if max_n > 8000 else max(1, max_n // 500)  # coarse init even for small K
    active = sorted(set(range(1, max_n + 1, step)) | set(range(1, min(2000, max_n))))

    def add_rows(ns):
        a = build_rows(ns); r = a.shape[0]
        starts = np.arange(0, r * n, n); idx = np.tile(np.arange(n), r)
        h.addRows(r, np.full(r, -inf), np.full(r, TOL), r * n, starts, idx, a.flatten())

    add_rows(active)
    best = None
    for rnd in range(max_rounds):
        t0 = time.time()
        h.setOptionValue("time_limit", float(time_limit) * (rnd + 1))
        h.run()
        status = h.modelStatusToString(h.getModelStatus())
        sol = h.getSolution()
        f = np.array(sol.col_value)
        score = -float(c @ f)
        # violations over full grid
        worst, viols = -1e18, []
        for s in range(1, max_n + 1, 100_000):
            e = min(s + 100_000, max_n + 1)
            g = build_rows(np.arange(s, e)) @ f
            worst = max(worst, float(g.max()))
            for i in np.where(g > TOL + 1e-9)[0]:
                viols.append(s + int(i))
        log(f"  R{rnd}: {status} score={score:.10f} worstG={worst:.8f} viol={len(viols)} rows={len(active)} {time.time()-t0:.0f}s")
        if "Optimal" in status and worst <= TOL + 1e-9:
            best = (list(active), np.array(sol.row_dual), score)
            break
        if not viols:
            best = (list(active), np.array(sol.row_dual), score); break
        new = [v for v in viols[:8000] if v not in set(active)]
        if not new:
            best = (list(active), np.array(sol.row_dual), score); break
        active = sorted(set(active) | set(new)); add_rows(new)
    if best is None:
        return None
    active_rows, row_dual, score = best
    # HiGHS min-problem <=-row duals are <= 0 at binding rows; board y >= 0 is -row_dual,
    # clipped to >= 0 (any y >= 0 gives a valid bound; near-optimal dual makes it tight).
    y = np.clip(-row_dual, 0.0, None)
    return np.array(active_rows, dtype=np.int64), y, score


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--K", type=int, default=24000)
    ap.add_argument("--time-limit", type=int, default=3600)
    ap.add_argument("--denom-pow", type=int, default=48)
    args = ap.parse_args()

    out = solve_uncapped_dual(args.K, time_limit=args.time_limit)
    if out is None:
        print("dual solve did not converge"); return
    m, y, score_lp = out
    two_p = 1 << args.denom_pow
    Y = np.ceil(y * two_p).astype(object)               # round UP, keeps validity
    Y = np.where(Y < 0, 0, Y)
    import os
    os.makedirs("results/problem-7-prime", exist_ok=True)
    path = f"results/problem-7-prime/dual_K{args.K}.npz"
    np.savez(path, m=m, Y=np.array([int(v) for v in Y], dtype=object),
             denom_pow=args.denom_pow, K=args.K, TOL=1.0001, score_lp=score_lp)
    print(f"saved dual -> {path}  (rows={len(m)} score_lp={score_lp:.10f})")
    print(f"certify: uv run python scripts/prime/ceiling_certify.py --dual {path}")


if __name__ == "__main__":
    main()
