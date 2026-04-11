"""P7 reclaim optimizer — explore non-squarefree keys within existing max_key range.

Strategy: Use ALL integers [2, 3287] as LP variables (3286 vars). This keeps
max_key=3287 (same constraint range), but adds 1287 non-squarefree keys as
extra degrees of freedom. Then select top 1999 and re-solve.

Also tries larger N with key selection.
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
    sf = [True] * (N + 1)
    for p in range(2, int(math.isqrt(N)) + 1):
        for m in range(p * p, N + 1, p * p):
            sf[m] = False
    return [k for k in range(2, N + 1) if sf[k]]


def solve_cutting_plane_fast(
    keys: list[int],
    *,
    margin: float = 1e-7,
    max_rounds: int = 60,
    constraint_mult: int = 10,
    time_limit: int = 600,
) -> tuple[np.ndarray | None, float]:
    """Cutting-plane LP solver using dense matrices and HiGHS."""
    n_vars = len(keys)
    max_key = max(keys)
    max_n = constraint_mult * max_key

    log(f"  vars={n_vars}, max_key={max_key}, constraint_range=[1,{max_n}]")

    c_obj = np.array([math.log(k) / k for k in keys], dtype=np.float64)
    bounds = [(-10.0, 10.0)] * n_vars
    k_arr = np.array(keys, dtype=np.float64)

    # Initial constraints: n=1..max_key + sparse beyond
    active_ns = sorted(
        set(range(1, min(max_key + 1, max_n + 1)))
        | set(range(max_key + 1, max_n + 1, 50))
    )
    current_margin = margin

    best_f = None
    best_score = -float("inf")

    for rnd in range(max_rounds):
        t0 = time.time()
        ns_arr = np.array(active_ns, dtype=np.float64)

        log(f"  Round {rnd}: building matrix ({len(active_ns)} × {n_vars})...")
        A = np.floor(ns_arr[:, None] / k_arr[None, :]) - ns_arr[:, None] / k_arr[None, :]
        b = np.full(len(active_ns), 1.0 - current_margin)
        mem_mb = A.nbytes / 1e6
        log(f"  Matrix: {A.shape}, {mem_mb:.0f} MB")

        t1 = time.time()
        result = linprog(
            c_obj, A_ub=A, b_ub=b, bounds=bounds, method="highs-ipm",
            options={
                "time_limit": time_limit,
                "primal_feasibility_tolerance": 1e-9,
                "dual_feasibility_tolerance": 1e-9,
                "ipm_optimality_tolerance": 1e-10,
            },
        )
        t_solve = time.time() - t1

        if not result.success:
            log(f"  Round {rnd}: LP status: {result.message}, {t_solve:.0f}s")
            # If timed out with feasible solution, try using it
            if "Time limit" in str(result.message) and result.x is not None:
                log(f"  Using time-limited feasible solution...")
                f_vec = result.x
                score = -c_obj @ f_vec
            else:
                current_margin *= 2
                log(f"  Increasing margin to {current_margin:.2e}")
                if current_margin > 0.01:
                    break
                continue
        else:
            score = -result.fun
            f_vec = result.x

        # Check ALL integer violations
        log(f"  Checking violations across [1, {max_n}]...")
        violations = []
        chunk = 200_000
        for start in range(1, max_n + 1, chunk):
            end = min(start + chunk, max_n + 1)
            ns_check = np.arange(start, end, dtype=np.float64)
            G = (np.floor(ns_check[:, None] / k_arr[None, :]) - ns_check[:, None] / k_arr[None, :]) @ f_vec
            mask = G > 1.0 + 1e-12
            for idx in np.where(mask)[0]:
                violations.append((start + idx, float(G[idx])))

        violations.sort(key=lambda x: -x[1])
        n_viol = len(violations)
        worst_G = violations[0][1] if violations else 0.0

        log(f"  score={score:.10f}, viol={n_viol}, worst_G={worst_G:.10f}, solve={t_solve:.1f}s")

        if n_viol == 0:
            best_f = f_vec.copy()
            best_score = score
            log(f"  *** FEASIBLE at score={score:.10f} ***")
            break

        new_ns = [n for n, _ in violations[:5000] if n not in set(active_ns)]
        if not new_ns:
            current_margin *= 2
            log(f"  No new cutting planes. Margin -> {current_margin:.2e}")
            if current_margin > 0.01:
                break
            continue

        active_ns = sorted(set(active_ns) | set(new_ns))
        log(f"  Added {len(new_ns)} cutting planes, total={len(active_ns)}")

    return best_f, best_score


def select_best_keys(keys: list[int], f_vals: np.ndarray, max_keys: int = 1999) -> list[int]:
    contributions = []
    for j, k in enumerate(keys):
        c = abs(f_vals[j]) * math.log(k) / k
        contributions.append((c, k, j))
    contributions.sort(reverse=True)
    return sorted([k for _, k, _ in contributions[:max_keys]])


def build_solution(keys: list[int], f_vals: np.ndarray) -> dict[int, float]:
    pf = {}
    for j, k in enumerate(keys):
        if abs(f_vals[j]) > 1e-15:
            pf[k] = float(f_vals[j])
    sum_fk_over_k = sum(v / k for k, v in pf.items())
    pf[1] = max(-10.0, min(10.0, -sum_fk_over_k))
    return pf


def compute_score_only(pf: dict[int, float]) -> float:
    pf = dict(pf)
    keys = sorted(pf.keys())
    sum_fk_over_k = sum(pf.get(k, 0) / k for k in keys if k != 1)
    pf[1] = -sum_fk_over_k
    return -sum(pf[k] * math.log(k) / k for k in keys if k >= 2)


def evaluate_mc(pf: dict[int, float], n_samples: int = 10_000_000, seed: int = 42) -> float:
    from einstein.prime.evaluator import evaluate
    sol = {"partial_function": {str(k): v for k, v in pf.items()}}
    return evaluate(sol, n_samples=n_samples, seed=seed)


def main():
    os.makedirs("results/problem-7-prime", exist_ok=True)

    current_best = 0.994726926034219
    target = current_best + 1e-5
    log(f"Current #1: {current_best:.15f}")
    log(f"Target:     {target:.15f}")
    log(f"Need improvement >= 1e-05\n")

    best_pf = None
    best_score = 0.0

    experiments = [
        # (label, keys)
        ("all_int_3287", list(range(2, 3288))),  # All integers [2,3287] = 3286 keys
        ("sf_4000", get_squarefree(4000)),        # SF up to 4000 = 2432 keys
        ("sf_5000", get_squarefree(5000)),        # SF up to 5000 = 3041 keys
    ]

    for label, all_keys in experiments:
        log(f"\n{'='*70}")
        log(f"Experiment: {label} ({len(all_keys)} keys)")
        log(f"{'='*70}")

        # Phase 1: Solve LP with all keys
        log(f"\nPhase 1: Solve LP with all {len(all_keys)} keys")
        f_vals, score1 = solve_cutting_plane_fast(
            all_keys, margin=1e-7, time_limit=300
        )

        if f_vals is None:
            log("  Phase 1 failed — no feasible solution")
            continue

        log(f"\n  Phase 1 score (all keys): {score1:.10f}")
        nonzero = np.sum(np.abs(f_vals) > 1e-10)
        log(f"  Non-zero keys: {nonzero} / {len(all_keys)}")

        # Phase 2: Select best 1999 and re-solve
        selected = select_best_keys(all_keys, f_vals, max_keys=1999)
        new_max = max(selected)
        log(f"\n  Phase 2: Re-solving with top 1999 keys (max_key={new_max})")

        # How many are non-squarefree?
        def is_sf(n):
            for p in range(2, int(math.isqrt(n))+1):
                if n % (p*p) == 0: return False
            return True
        nsf = sum(1 for k in selected if not is_sf(k))
        if nsf > 0:
            log(f"  Non-squarefree keys in selection: {nsf}")

        f_vals2, score2 = solve_cutting_plane_fast(
            selected, margin=1e-7, time_limit=300
        )

        if f_vals2 is None:
            log("  Phase 2 failed")
            continue

        pf = build_solution(selected, f_vals2)
        analytical = compute_score_only(pf)
        log(f"\n  Phase 2 score:    {score2:.10f}")
        log(f"  Analytical score: {analytical:.10f}")

        # Quick MC
        mc_fast = evaluate_mc(pf, n_samples=100_000, seed=42)
        log(f"  MC(100k):         {mc_fast:.10f} {'PASS' if mc_fast > 0 else 'FAIL'}")

        if mc_fast <= 0:
            log("  *** MC FAILED ***")
            continue

        improvement = analytical - current_best
        log(f"  Improvement:      {improvement:.2e}")
        log(f"  Meets 1e-5 gate:  {'YES' if improvement >= 1e-5 else 'NO'}")

        if analytical > best_score:
            best_score = analytical
            best_pf = pf
            sol = {"partial_function": {str(k): v for k, v in pf.items()}}
            with open(f"results/problem-7-prime/reclaim_{label}.json", "w") as f:
                json.dump(sol, f)

            if improvement >= 1e-5:
                log(f"\n  *** TARGET MET! ***")
                log(f"  Running full 10M MC validation...")
                mc_full = evaluate_mc(pf, n_samples=10_000_000, seed=42)
                log(f"  MC(10M, seed=42):  {mc_full:.15f} {'PASS' if mc_full > 0 else 'FAIL'}")

                if mc_full > 0:
                    mc_cross = evaluate_mc(pf, n_samples=10_000_000, seed=123)
                    log(f"  MC(10M, seed=123): {mc_cross:.15f} {'PASS' if mc_cross > 0 else 'FAIL'}")

                    if mc_cross > 0:
                        with open("results/problem-7-prime/reclaim_best.json", "w") as f:
                            json.dump(sol, f)
                        log(f"\n  *** SOLUTION VALIDATED — ready for submission ***")
                        log(f"  Score: {mc_full:.15f}")
                        log(f"  Keys: {len(pf)}")
                        return  # Early exit on success

    # Summary
    log(f"\n{'='*70}")
    if best_pf:
        improvement = best_score - current_best
        log(f"Best reclaim score: {best_score:.15f}")
        log(f"Improvement:        {improvement:.2e}")
        log(f"Target met:         {'YES' if improvement >= 1e-5 else 'NO'}")
    else:
        log("No improved solution found.")


if __name__ == "__main__":
    main()
