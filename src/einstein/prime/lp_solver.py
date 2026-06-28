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
    import highspy

    keys = sorted(keys)
    ka = np.array(keys, dtype=np.float64)
    n = len(keys)
    max_n = xcap_mult * int(ka[-1])
    c = np.array([math.log(k) / k for k in keys], dtype=np.float64)

    g_seed = _g_of_seed(seed_pf, max_n)
    active = sorted(set(int(i) for i in np.where(g_seed > 0.5)[0]) | set(range(1, max_n + 1, 200)))
    log(f"  vars={n} maxkey={int(ka[-1])} range=[1,{max_n}] init_cons={len(active)}")

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
    best_f, best_score, best_worst = None, -1e18, 0.0
    for rnd in range(max_rounds):
        t0 = time.time()
        h.run()
        status = h.modelStatusToString(h.getModelStatus())
        f = np.array(h.getSolution().col_value)
        score = -float(c @ f)
        worst, viols = _violations(ka, f, max_n)
        log(
            f"  R{rnd}: status={status} base={score:.10f} worstG={worst:.10f} "
            f"viol={len(viols)} cons={len(active)} {time.time() - t0:.0f}s"
        )
        if "Optimal" not in status and best_f is not None:
            break
        if score > best_score and worst <= 1.0 + 1e-9:
            best_f, best_score, best_worst = f.copy(), score, worst
        if not viols:
            return f.copy(), score, worst, rnd + 1
        new = [v for v in viols[:5000] if v not in set(active)]
        if not new:
            break
        active = sorted(set(active) | set(new))
        add_rows(new)
    return best_f, best_score, best_worst, max_rounds
