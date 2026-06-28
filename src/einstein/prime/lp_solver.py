"""Sieve-LP solver for Problem 7 (Prime Number Theorem) at large N.

The P7 base LP is:  minimize  Σ_k f(k)·log(k)/k
                    s.t.      Σ_k f(k)(⌊x/k⌋ − x/k) ≤ 1   for all integer x ≥ 1
                              −10 ≤ f(k) ≤ 10

**Why this module exists (the wisdom):** at N=16000 this LP is *massively degenerate* —
near the optimal (Möbius-like) solution the Mertens identity Σ μ(k)⌊x/k⌋ = 1 makes
~2600 constraints simultaneously binding on a ~2000-variable problem. `scipy.linprog`
(HiGHS via the default path, which runs crossover to a vertex) STALLS on that degenerate
optimal face and never returns — a single 5338×1999 solve fails to converge in 90s, and
the full N=16000 LP timed out repeatedly (branch js/feat/p7-nextension-reclaim, Exp 10,
wall-ledger 2026-06-28). The fix is to call HiGHS directly via `highspy` with
**IPM and crossover OFF**: we need the optimal interior `f` (to read off the score and
then scale to the tolerance band), not a basic/vertex solution, so skipping crossover
sidesteps exactly the step that hangs. With crossover off the same LP solves to Optimal
in ~320s.

The solver warm-starts the cutting-plane constraint set from a seed solution's
near-binding points (G_seed > 0.5) plus a sparse sample, then adds any violated integer
constraints found over the full x∈[1, xcap_mult·maxkey] range (the worst x sits at
~8·maxkey, so the range cannot be truncated — Exp 10).
"""

from __future__ import annotations

import math
import time

import numpy as np


def _build_rows(keys_arr: np.ndarray, ns: np.ndarray) -> np.ndarray:
    """Dense constraint block A[i,j] = floor(ns[i]/k_j) - ns[i]/k_j (all entries nonzero)."""
    ns = ns.reshape(-1, 1).astype(np.float64)
    return np.floor(ns / keys_arr.reshape(1, -1)) - ns / keys_arr.reshape(1, -1)


def _g_of_seed(seed_pf: dict[int, float], max_n: int) -> np.ndarray:
    keys = np.array(sorted(seed_pf), dtype=np.float64)
    vals = np.array([seed_pf[int(k)] for k in keys], dtype=np.float64)
    g = np.zeros(max_n + 1)
    for start in range(1, max_n + 1, 100_000):
        end = min(start + 100_000, max_n + 1)
        g[start:end] = _build_rows(keys, np.arange(start, end)) @ vals
    return g


def _violations(keys_arr: np.ndarray, f: np.ndarray, max_n: int, tol: float = 1e-12):
    worst = -1e18
    viols: list[int] = []
    for start in range(1, max_n + 1, 100_000):
        end = min(start + 100_000, max_n + 1)
        g = _build_rows(keys_arr, np.arange(start, end)) @ f
        worst = max(worst, float(g.max()))
        for idx in np.where(g > 1.0 + tol)[0]:
            viols.append(start + int(idx))
    return worst, viols


def _solve_cutting_plane(
    ka: np.ndarray,
    c: np.ndarray,
    active: list[int],
    max_n: int,
    *,
    ipm_tol: float,
    time_limit: int,
    max_rounds: int,
    log,
) -> dict:
    """Crossover-off HiGHS solve with integer-grid cutting planes over a fixed key set.

    Returns dict(f, score, worst, active, row_dual, feasible, rounds). `row_dual` is
    aligned to the returned `active` constraint order (for column-generation pricing).
    """
    import highspy

    n = len(ka)
    inf = highspy.kHighsInf
    h = highspy.Highs()
    for opt, val in [
        ("output_flag", False),
        ("solver", "ipm"),
        ("run_crossover", "off"),
        ("primal_feasibility_tolerance", 1e-7),
        ("dual_feasibility_tolerance", 1e-7),
        ("ipm_optimality_tolerance", ipm_tol),
        ("time_limit", float(time_limit)),
    ]:
        h.setOptionValue(opt, val)
    h.addCols(
        n, c, np.full(n, -10.0), np.full(n, 10.0), 0, np.array([]), np.array([]), np.array([])
    )

    def add_rows(ns: list[int]) -> None:
        a = _build_rows(ka, np.array(ns))
        r = a.shape[0]
        starts = np.arange(0, r * n, n)
        idx = np.tile(np.arange(n), r)
        h.addRows(r, np.full(r, -inf), np.full(r, 1.0), r * n, starts, idx, a.flatten())

    add_rows(active)
    # `best` always holds the highest-score grid-feasible point seen, so a feasible f is
    # never lost. `feasible` means *converged* (status Optimal): only converged points are
    # trustworthy as an optimum, so colgen gates its support-trim on this flag and never
    # selects keys from a non-converged (time-limited) solution.
    best = {"f": None, "score": -1e18, "worst": 0.0, "feasible": False, "active": list(active)}

    def capture(f, score, worst, active, sol, converged, rnd):
        best.update(
            f=f.copy(),
            score=score,
            worst=worst,
            active=list(active),
            row_dual=np.array(sol.row_dual),
            feasible=converged,
            rounds=rnd + 1,
        )

    for rnd in range(max_rounds):
        t0 = time.time()
        h.run()
        status = h.modelStatusToString(h.getModelStatus())
        sol = h.getSolution()
        f = np.array(sol.col_value)
        score = -float(c @ f)
        worst, viols = _violations(ka, f, max_n)
        log(
            f"  R{rnd}: status={status} base={score:.10f} worstG={worst:.10f} "
            f"viol={len(viols)} cons={len(active)} {time.time() - t0:.0f}s"
        )
        converged = "Optimal" in status
        grid_feasible = worst <= 1.0 + 1e-9
        # Keep the best grid-feasible point. Prefer a converged one; only let a
        # non-converged point fill an empty slot (never overwrite a converged best).
        if grid_feasible and (
            (converged and score > best["score"]) or (best["f"] is None and not best["feasible"])
        ):
            capture(f, score, worst, active, sol, converged, rnd)
        if not viols:
            best["active"] = list(active)
            best["row_dual"] = np.array(sol.row_dual)
            best["rounds"] = rnd + 1
            return best
        if not converged and best["f"] is not None:
            break
        new = [v for v in viols[:5000] if v not in set(active)]
        if not new:
            break
        active = sorted(set(active) | set(new))
        add_rows(new)
    best.setdefault("row_dual", np.zeros(len(best["active"])))
    best.setdefault("rounds", max_rounds)
    return best


def solve_sieve_lp(
    keys: list[int],
    seed_pf: dict[int, float],
    *,
    xcap_mult: int = 10,
    ipm_tol: float = 1e-8,
    time_limit: int = 1200,
    max_rounds: int = 12,
    log=print,
) -> tuple[np.ndarray | None, float, float, int]:
    """Solve the P7 sieve LP over `keys`, warm-started from `seed_pf`.

    Returns (f_vec, base_score, worst_G, n_rounds). f_vec is aligned to sorted(keys).
    Requires `highspy` (HiGHS Python interface) for the crossover-off IPM solve.
    """
    keys = sorted(keys)
    ka = np.array(keys, dtype=np.float64)
    max_n = xcap_mult * int(ka[-1])
    c = np.array([math.log(k) / k for k in keys], dtype=np.float64)
    g_seed = _g_of_seed(seed_pf, max_n)
    active = sorted(set(int(i) for i in np.where(g_seed > 0.5)[0]) | set(range(1, max_n + 1, 200)))
    log(f"  vars={len(keys)} maxkey={int(ka[-1])} range=[1,{max_n}] init_cons={len(active)}")
    r = _solve_cutting_plane(
        ka, c, active, max_n, ipm_tol=ipm_tol, time_limit=time_limit, max_rounds=max_rounds, log=log
    )
    return r["f"], r["score"], r["worst"], r["rounds"]


def colgen_sieve_lp(
    seed_pf: dict[int, float],
    candidate_keys: list[int],
    *,
    max_keys: int = 1999,
    add_per_round: int = 80,
    rounds: int = 8,
    xcap_mult: int = 10,
    time_limit: int = 600,
    log=print,
) -> tuple[dict[int, float] | None, float, float]:
    """Column generation on the P7 sieve LP.

    Start from the seed's support (warm/feasible), solve, then price every candidate
    key by dual reduced cost rc_k = c_k − Σ_i y_i·A_ik over the active constraints. Add
    the few |rc| largest improving keys (so few new violations appear), re-solve, trim
    to `max_keys` by post-solve objective contribution, repeat. Returns
    (pf_dict_over_keys, base_score, worst_G) for the best feasible solution found.

    Adding only a handful of well-priced columns per round avoids the constraint blow-up
    that kills bulk support-swaps (Exp 12): the new binding constraints are few.
    """
    support = sorted(k for k in seed_pf if k >= 2)
    cand = sorted(set(candidate_keys) - set(support))
    best_pf, best_score, best_worst = None, -1e18, 0.0

    for rnd in range(rounds):
        keys = sorted(support)
        ka = np.array(keys, dtype=np.float64)
        max_n = xcap_mult * int(ka[-1])
        c = np.array([math.log(k) / k for k in keys], dtype=np.float64)
        g_seed = _g_of_seed(seed_pf, max_n)
        active = sorted(
            set(int(i) for i in np.where(g_seed > 0.5)[0]) | set(range(1, max_n + 1, 200))
        )
        log(f"[colgen {rnd}] support={len(keys)} maxkey={int(ka[-1])}")
        res = _solve_cutting_plane(
            ka, c, active, max_n, ipm_tol=1e-8, time_limit=time_limit, max_rounds=10, log=log
        )
        if not res["feasible"]:
            log("  master infeasible/timeout — stop")
            break
        score, f = res["score"], res["f"]
        if score > best_score:
            best_pf = {k: float(v) for k, v in zip(keys, f) if abs(v) > 1e-15}
            best_score, best_worst = score, res["worst"]
        log(f"  master base={score:.10f} worstG={res['worst']:.10f} (best={best_score:.10f})")

        # Price candidate keys by dual reduced cost over the final active constraint set.
        ns = np.array(res["active"], dtype=np.float64)
        y = res["row_dual"]
        cand_arr = np.array(cand, dtype=np.float64)
        c_cand = np.log(cand_arr) / cand_arr
        # rc_k = c_k - Σ_i y_i (floor(n_i/k) - n_i/k); chunk candidates to bound memory.
        rc = np.empty(len(cand))
        step = max(1, 4_000_000 // max(1, len(ns)))
        for s in range(0, len(cand), step):
            e = min(s + step, len(cand))
            a = np.floor(ns[:, None] / cand_arr[None, s:e]) - ns[:, None] / cand_arr[None, s:e]
            rc[s:e] = c_cand[s:e] - a.T @ y
        order = np.argsort(-np.abs(rc))
        improving = [cand[i] for i in order[:add_per_round] if abs(rc[i]) > 1e-9]
        if not improving:
            log("  no improving columns — converged")
            break
        log(f"  +{len(improving)} columns (max|rc|={abs(rc[order[0]]):.2e})")

        # Add columns, then trim back to max_keys by post-solve contribution.
        grown = sorted(set(support) | set(improving))
        gka = np.array(grown, dtype=np.float64)
        gmax_n = xcap_mult * int(gka[-1])
        gc = np.log(gka) / gka
        g2 = _g_of_seed(seed_pf, gmax_n)
        gactive = sorted(
            set(int(i) for i in np.where(g2 > 0.5)[0]) | set(range(1, gmax_n + 1, 200))
        )
        res2 = _solve_cutting_plane(
            gka, gc, gactive, gmax_n, ipm_tol=1e-8, time_limit=time_limit, max_rounds=10, log=log
        )
        if not res2["feasible"]:
            log("  grown master infeasible/timeout — keep best, stop")
            break
        f2 = res2["f"]
        contrib = sorted(
            ((abs(f2[j]) * math.log(k) / k, k) for j, k in enumerate(grown)), reverse=True
        )
        support = sorted(k for _, k in contrib[:max_keys])
        cand = sorted(set(cand) - set(support))
        if res2["score"] > best_score:
            best_pf = {k: float(v) for k, v in zip(grown, f2) if abs(v) > 1e-15}
            best_score, best_worst = res2["score"], res2["worst"]
        log(f"  grown base={res2['score']:.10f} -> trimmed support={len(support)}")

    return best_pf, best_score, best_worst
