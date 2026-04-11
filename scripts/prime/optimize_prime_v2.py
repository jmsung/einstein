"""Improved LP optimizer for Problem 7 — Prime Number Theorem.

Key improvement over v1: solve LP with MORE than 1999 squarefree keys
(larger N), then select the best 1999 for submission.

Two-phase approach:
  Phase 1: Solve LP with all squarefree keys up to large N (no key cap)
  Phase 2: Select top 1999 keys by |f(k)|, re-solve LP with those keys
"""

import json
import math
import os
import sys
import time

import numpy as np
from scipy.optimize import linprog


def log(msg=""):
    print(msg, flush=True)


def get_squarefree(N: int) -> list[int]:
    """Return all squarefree integers in [2, N]."""
    sf = [True] * (N + 1)
    for p in range(2, int(math.isqrt(N)) + 1):
        for m in range(p * p, N + 1, p * p):
            sf[m] = False
    return [k for k in range(2, N + 1) if sf[k]]


def build_dense_matrix(keys: list[int], ns: list[int]) -> np.ndarray:
    """Build dense constraint matrix. A[i,j] = floor(ns[i]/keys[j]) - ns[i]/keys[j]."""
    ns_arr = np.array(ns, dtype=np.float64).reshape(-1, 1)
    k_arr = np.array(keys, dtype=np.float64).reshape(1, -1)
    A = np.floor(ns_arr / k_arr) - ns_arr / k_arr  # (n_cons, n_vars)
    return A


def check_violations_fast(
    keys: list[int], f_vals: np.ndarray, max_n: int, tol: float = 1e-12
) -> list[tuple[int, float]]:
    """Find integer points where constraint is violated."""
    ka = np.array(keys, dtype=np.float64)
    va = f_vals.copy()

    violations = []
    chunk = 200_000
    for start in range(1, max_n + 1, chunk):
        end = min(start + chunk, max_n + 1)
        ns = np.arange(start, end, dtype=np.float64)
        G = (np.floor(ns[:, None] / ka[None, :]) - ns[:, None] / ka[None, :]) @ va
        mask = G > 1.0 + tol
        for idx in np.where(mask)[0]:
            violations.append((start + idx, float(G[idx])))

    violations.sort(key=lambda x: -x[1])
    return violations


def solve_cutting_plane(
    keys: list[int],
    *,
    margin: float = 1e-7,
    max_rounds: int = 60,
    constraint_mult: int = 10,
    time_limit: int = 600,
) -> tuple[np.ndarray | None, float]:
    """Solve the LP with cutting planes."""
    n_vars = len(keys)
    max_key = max(keys)
    max_n = constraint_mult * max_key

    log(f"  vars={n_vars}, max_key={max_key}, constraint_range=[1,{max_n}]")

    c_obj = np.array([math.log(k) / k for k in keys], dtype=np.float64)
    bounds = [(-10.0, 10.0)] * n_vars

    # Initial constraints: n=1..min(max_key, max_n) + every 100th up to max_n
    N = max_key
    active_ns = sorted(
        set(range(1, min(N + 1, max_n + 1)))
        | set(range(1, max_n + 1, 100))
    )

    best_f = None
    best_score = -float("inf")
    current_margin = margin

    for rnd in range(max_rounds):
        t0 = time.time()

        log(f"  Round {rnd}: building matrix ({len(active_ns)} × {n_vars})...")
        A = build_dense_matrix(keys, active_ns)
        b = np.full(len(active_ns), 1.0 - current_margin, dtype=np.float64)
        t_build = time.time() - t0
        mem_mb = A.nbytes / 1e6
        log(f"  Matrix built in {t_build:.1f}s ({mem_mb:.0f} MB)")

        t1 = time.time()
        result = linprog(
            c_obj,
            A_ub=A,
            b_ub=b,
            bounds=bounds,
            method="highs",
            options={
                "time_limit": time_limit,
                "primal_feasibility_tolerance": 1e-9,
                "dual_feasibility_tolerance": 1e-9,
            },
        )
        t_solve = time.time() - t1

        if not result.success:
            log(f"  Round {rnd}: LP failed ({result.message}), {t_solve:.0f}s")
            current_margin *= 2
            log(f"  Increasing margin to {current_margin:.2e}")
            if current_margin > 0.01:
                break
            continue

        score = -result.fun
        f_vec = result.x

        # Check ALL integer violations
        log(f"  Checking violations across [1, {max_n}]...")
        violations = check_violations_fast(keys, f_vec, max_n)
        n_viol = len(violations)
        worst_G = violations[0][1] if violations else 0.0

        log(
            f"  Round {rnd}: score={score:.10f}, cons={len(active_ns)}, "
            f"viol={n_viol}, worst_G={worst_G:.10f}, solve={t_solve:.1f}s"
        )

        if n_viol == 0:
            best_f = f_vec.copy()
            best_score = score
            log(f"  *** FEASIBLE at score={score:.10f} ***")
            break

        # Add violated points
        active_set = set(active_ns)
        new_ns = [n for n, _ in violations[:5000] if n not in active_set]
        if not new_ns:
            current_margin *= 2
            log(f"  No new cutting planes. Margin -> {current_margin:.2e}")
            if current_margin > 0.01:
                break
            continue

        active_ns = sorted(set(active_ns) | set(new_ns))
        log(f"  Added {len(new_ns)} cutting planes, total={len(active_ns)}")

    return best_f, best_score


def select_best_keys(
    keys: list[int], f_vals: np.ndarray, max_keys: int = 1999
) -> list[int]:
    """Select the top max_keys keys by contribution to the objective."""
    contributions = []
    for j, k in enumerate(keys):
        c = abs(f_vals[j]) * math.log(k) / k
        contributions.append((c, k, j))
    contributions.sort(reverse=True)
    selected = sorted([k for _, k, _ in contributions[:max_keys]])
    return selected


def build_solution(keys: list[int], f_vals: np.ndarray) -> dict[int, float]:
    """Build solution dict from LP output, add f(1) from normalization."""
    pf = {}
    for j, k in enumerate(keys):
        if abs(f_vals[j]) > 1e-15:
            pf[k] = float(f_vals[j])

    # Normalize: f(1) = -sum f(k)/k for k >= 2
    sum_fk_over_k = sum(v / k for k, v in pf.items())
    f1 = max(-10.0, min(10.0, -sum_fk_over_k))
    pf[1] = f1
    return pf


def evaluate_mc(pf: dict[int, float], n_samples: int = 10_000_000, seed: int = 42) -> float:
    """Evaluate solution using Monte Carlo (matches arena verifier)."""
    from einstein.prime.evaluator import evaluate
    sol = {"partial_function": {str(k): v for k, v in pf.items()}}
    return evaluate(sol, n_samples=n_samples, seed=seed)


def compute_score_only(pf: dict[int, float]) -> float:
    """Compute analytical score without constraint checking."""
    pf = dict(pf)
    keys = sorted(pf.keys())
    sum_fk_over_k = sum(pf.get(k, 0) / k for k in keys if k != 1)
    pf[1] = -sum_fk_over_k
    score = 0.0
    for k in keys:
        if k >= 2:
            score -= pf[k] * math.log(k) / k
    return score


def main():
    os.makedirs("results/problem-7-prime", exist_ok=True)

    current_best_score = 0.994726926034219  # Our current #1
    target_score = current_best_score + 1e-5

    log(f"Current #1: {current_best_score:.15f}")
    log(f"Target:     {target_score:.15f}")
    log(f"Improvement needed: >= 1e-05")
    log()

    best_pf = None
    best_score = 0.0

    for N in [4000, 5000, 6000]:
        all_keys = get_squarefree(N)
        n_keys = len(all_keys)
        log(f"\n{'='*70}")
        log(f"Phase 1: N={N}, total squarefree keys = {n_keys}")
        log(f"{'='*70}")

        if n_keys <= 1999:
            log(f"  Only {n_keys} keys — same as v1, skipping")
            continue

        # Phase 1: Solve LP with ALL keys
        log(f"  Solving LP with all {n_keys} keys...")
        f_vals, score = solve_cutting_plane(
            all_keys, margin=1e-7, time_limit=600
        )

        if f_vals is None:
            log("  Phase 1 failed — no feasible solution")
            continue

        log(f"\n  Phase 1 score (all {n_keys} keys): {score:.10f}")
        nonzero = np.sum(np.abs(f_vals) > 1e-10)
        log(f"  Non-zero keys: {nonzero} / {n_keys}")

        # Phase 2: Select best 1999 keys and re-solve
        selected_keys = select_best_keys(all_keys, f_vals, max_keys=1999)
        new_keys = [k for k in selected_keys if k > 3287]
        log(f"\n  Phase 2: Re-solving with top 1999 keys")
        log(f"  Key range: [{min(selected_keys)}, {max(selected_keys)}]")
        log(f"  Keys > 3287 (new in v2): {len(new_keys)}")
        if new_keys:
            log(f"  New keys sample: {new_keys[:10]}...")

        f_vals2, score2 = solve_cutting_plane(
            selected_keys, margin=1e-7, time_limit=600
        )

        if f_vals2 is None:
            log("  Phase 2 failed")
            continue

        pf = build_solution(selected_keys, f_vals2)
        analytical = compute_score_only(pf)
        log(f"\n  Phase 2 score (1999 selected): {score2:.10f}")
        log(f"  Analytical score:              {analytical:.10f}")

        # Quick MC validation
        mc_fast = evaluate_mc(pf, n_samples=100_000, seed=42)
        log(f"  MC(100k):                      {mc_fast:.10f} {'PASS' if mc_fast > 0 else 'FAIL'}")

        if mc_fast <= 0:
            log("  *** MC FAILED — constraint violated ***")
            continue

        improvement = analytical - current_best_score
        log(f"  Improvement over current #1:   {improvement:.2e}")
        log(f"  Meets minImprovement (1e-5)?   {'YES' if improvement >= 1e-5 else 'NO'}")

        if analytical > best_score:
            best_score = analytical
            best_pf = pf

            sol = {"partial_function": {str(k): v for k, v in pf.items()}}
            with open(f"results/problem-7-prime/lp_v2_N{N}.json", "w") as f:
                json.dump(sol, f)

            if improvement >= 1e-5:
                log(f"\n  *** TARGET MET! Improvement = {improvement:.2e} ***")

                # Full MC validation
                log("  Running full 10M MC validation...")
                mc_full = evaluate_mc(pf, n_samples=10_000_000, seed=42)
                log(f"  MC(10M, seed=42): {mc_full:.10f} {'PASS' if mc_full > 0 else 'FAIL'}")

                if mc_full > 0:
                    mc_cross = evaluate_mc(pf, n_samples=10_000_000, seed=123)
                    log(f"  MC(10M, seed=123): {mc_cross:.10f} {'PASS' if mc_cross > 0 else 'FAIL'}")

                    if mc_cross > 0:
                        with open("results/problem-7-prime/best_v2.json", "w") as f:
                            json.dump(sol, f)
                        log(f"\n  *** SOLUTION VALIDATED — ready for submission ***")
                        log(f"  Score: {mc_full:.15f}")
                        log(f"  Keys: {len(pf)}")

    # Summary
    log(f"\n{'='*70}")
    if best_pf:
        improvement = best_score - current_best_score
        log(f"Best v2 score: {best_score:.15f}")
        log(f"Improvement:   {improvement:.2e}")
        log(f"Target met:    {'YES' if improvement >= 1e-5 else 'NO'}")
    else:
        log("No improved solution found.")


if __name__ == "__main__":
    main()
