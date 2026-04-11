"""P7 column generation — add keys with negative reduced cost to improve LP.

1. Solve LP with current 1999 squarefree keys (N=3287) using cutting planes
2. Extract dual variables from the LP solution
3. Evaluate reduced cost for candidate keys (non-SF in [2,3287] and SF in [3288,10000])
4. Swap in improving keys, re-solve
5. Select best 1999 keys, final re-solve
"""

import json
import math
import os
import time

import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix, vstack


def log(msg=""):
    print(msg, flush=True)


def get_squarefree(N: int) -> list[int]:
    sf = [True] * (N + 1)
    for p in range(2, int(math.isqrt(N)) + 1):
        for m in range(p * p, N + 1, p * p):
            sf[m] = False
    return [k for k in range(2, N + 1) if sf[k]]


def build_sparse_matrix(keys: list[int], ns: list[int]) -> csr_matrix:
    """Build sparse constraint matrix. A[i,j] = floor(ns[i]/keys[j]) - ns[i]/keys[j]."""
    n_cons = len(ns)
    n_vars = len(keys)
    rows, cols, data = [], [], []
    for j, k in enumerate(keys):
        for i, n in enumerate(ns):
            val = (n // k) - n / k
            if abs(val) > 1e-15:
                rows.append(i)
                cols.append(j)
                data.append(val)
    return csr_matrix(
        (np.array(data), (np.array(rows), np.array(cols))),
        shape=(n_cons, n_vars),
    )


def check_violations(keys: list[int], f_vals: np.ndarray, max_n: int) -> list[tuple[int, float]]:
    """Find integer points where G(n) > 1."""
    ka = np.array(keys, dtype=np.float64)
    violations = []
    chunk = 200_000
    for start in range(1, max_n + 1, chunk):
        end = min(start + chunk, max_n + 1)
        ns = np.arange(start, end, dtype=np.float64)
        G = (np.floor(ns[:, None] / ka[None, :]) - ns[:, None] / ka[None, :]) @ f_vals
        mask = G > 1.0 + 1e-12
        for idx in np.where(mask)[0]:
            violations.append((start + idx, float(G[idx])))
    violations.sort(key=lambda x: -x[1])
    return violations


def solve_lp_cutting_plane(
    keys: list[int], *, margin: float = 1e-7, max_rounds: int = 40,
    constraint_mult: int = 10, time_limit: int = 300,
) -> tuple[np.ndarray | None, float, list[int]]:
    """Solve LP with cutting planes. Returns (f_vals, score, active_ns)."""
    n_vars = len(keys)
    max_key = max(keys)
    max_n = constraint_mult * max_key

    c_obj = np.array([math.log(k) / k for k in keys], dtype=np.float64)
    bounds = [(-10.0, 10.0)] * n_vars

    # Start with constraints at n=1..max_key/2 + every 50th
    active_ns = sorted(
        set(range(1, min(max_key // 2 + 1, max_n + 1)))
        | set(range(1, max_n + 1, 50))
    )

    for rnd in range(max_rounds):
        t0 = time.time()
        A = build_sparse_matrix(keys, active_ns)
        b = np.full(len(active_ns), 1.0 - margin)

        result = linprog(
            c_obj, A_ub=A, b_ub=b, bounds=bounds, method="highs",
            options={"time_limit": time_limit, "primal_feasibility_tolerance": 1e-9},
        )
        t_solve = time.time() - t0

        if not result.success:
            log(f"  Round {rnd}: FAILED ({result.message}), {t_solve:.0f}s")
            break

        score = -result.fun
        f_vec = result.x

        violations = check_violations(keys, f_vec, max_n)
        n_viol = len(violations)
        worst_G = violations[0][1] if violations else 0.0

        log(f"  Round {rnd}: score={score:.10f}, cons={len(active_ns)}, "
            f"viol={n_viol}, worst_G={worst_G:.8f}, {t_solve:.0f}s")

        if n_viol == 0:
            log(f"  *** FEASIBLE ***")
            return f_vec, score, active_ns

        new_ns = [n for n, _ in violations[:5000] if n not in set(active_ns)]
        if not new_ns:
            log(f"  No new cutting planes — converged")
            return f_vec, score, active_ns

        active_ns = sorted(set(active_ns) | set(new_ns))

    return None, 0.0, active_ns


def compute_reduced_costs(
    candidate_keys: list[int], active_ns: list[int],
    dual_approx: np.ndarray, c_obj_base: np.ndarray, keys_base: list[int],
) -> list[tuple[float, int]]:
    """Compute reduced costs for candidate keys using dual approximation."""
    reduced_costs = []
    for k_new in candidate_keys:
        # Objective coefficient for k_new
        c_new = math.log(k_new) / k_new

        # Constraint column for k_new: A[:,new] = [floor(n/k_new) - n/k_new for n in active_ns]
        col = np.array([(n // k_new) - n / k_new for n in active_ns])

        # Reduced cost = c_new - dual^T @ col
        # Negative reduced cost means adding this variable would improve the LP
        rc = c_new - dual_approx @ col
        reduced_costs.append((rc, k_new))

    reduced_costs.sort()  # Most negative first = most improving
    return reduced_costs


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
    log(f"Target:     {target:.15f}\n")

    # Step 1: Solve base LP with current key set
    log("=" * 70)
    log("Step 1: Solve base LP (1999 SF keys, N=3287)")
    log("=" * 70)

    base_keys = get_squarefree(3287)
    assert len(base_keys) == 1999, f"Expected 1999 keys, got {len(base_keys)}"

    f_base, score_base, active_ns = solve_lp_cutting_plane(
        base_keys, margin=1e-7, time_limit=300
    )

    if f_base is None:
        log("Base LP failed!")
        return

    pf_base = build_solution(base_keys, f_base)
    analytical_base = compute_score_only(pf_base)
    log(f"\nBase LP score:      {score_base:.10f}")
    log(f"Base analytical:    {analytical_base:.10f}")
    log(f"Active constraints: {len(active_ns)}\n")

    # Step 2: Evaluate candidate keys via approximate reduced costs
    log("=" * 70)
    log("Step 2: Evaluate candidate keys")
    log("=" * 70)

    # Candidates: non-squarefree in [2, 3287] + squarefree in [3288, 10000]
    sf_set = set(base_keys)
    nonsf_candidates = [k for k in range(2, 3288) if k not in sf_set]
    sf_beyond = get_squarefree(10000)
    sf_beyond = [k for k in sf_beyond if k > 3287]

    all_candidates = nonsf_candidates + sf_beyond
    log(f"Non-squarefree candidates [2,3287]: {len(nonsf_candidates)}")
    log(f"Squarefree candidates [3288,10000]: {len(sf_beyond)}")
    log(f"Total candidates: {len(all_candidates)}")

    # Approximate dual via perturbation analysis
    # For each active constraint n, compute the constraint slack
    ka = np.array(base_keys, dtype=np.float64)
    ns_arr = np.array(active_ns, dtype=np.float64)
    G_vals = (np.floor(ns_arr[:, None] / ka[None, :]) - ns_arr[:, None] / ka[None, :]) @ f_base
    slacks = 1.0 - 1e-7 - G_vals

    # Binding constraints (slack < 1e-6) have non-zero duals
    binding_mask = slacks < 1e-4
    n_binding = np.sum(binding_mask)
    log(f"Binding constraints (slack < 1e-4): {n_binding}")

    # Heuristic reduced cost: for each candidate key k_new, compute
    # how much adding it COULD help. The max score contribution is
    # |f_max| * log(k)/k where f_max = 10 (bound). The constraint
    # impact is max over binding n of |floor(n/k_new) - n/k_new|.
    log("\nEvaluating reduced costs for candidates...")
    candidate_scores = []
    for k_new in all_candidates:
        # Max objective contribution if f(k_new) = ±10
        obj_potential = math.log(k_new) / k_new

        # Check constraint impact at binding points
        binding_ns = [active_ns[i] for i in range(len(active_ns)) if binding_mask[i]]
        max_constraint_impact = max(
            abs((n // k_new) - n / k_new) for n in binding_ns[:200]
        ) if binding_ns else 0

        # Score: high obj_potential, low constraint_impact = good candidate
        if max_constraint_impact > 0:
            ratio = obj_potential / max_constraint_impact
        else:
            ratio = obj_potential * 100  # No constraint impact = great

        candidate_scores.append((ratio, obj_potential, max_constraint_impact, k_new))

    candidate_scores.sort(reverse=True)

    # Top candidates
    log("\nTop 50 candidate keys by potential/constraint ratio:")
    for ratio, obj, cons, k in candidate_scores[:50]:
        is_sf = k not in sf_set and k <= 3287
        label = "nonsf" if is_sf else ("sf>3287" if k > 3287 else "sf")
        log(f"  k={k:6d} ({label:>8s}): obj={obj:.6f}, cons_impact={cons:.6f}, ratio={ratio:.4f}")

    # Step 3: Try adding top candidates in batches
    log("\n" + "=" * 70)
    log("Step 3: Column generation — add best candidates")
    log("=" * 70)

    best_pf = None
    best_score = analytical_base

    # Try adding top N candidates (replacing weakest current keys)
    for n_add in [10, 50, 100, 200]:
        top_candidates = [k for _, _, _, k in candidate_scores[:n_add]]

        # Merge with base keys
        merged = sorted(set(base_keys) | set(top_candidates))
        if len(merged) > 1999:
            # Need to drop some — drop the weakest from base
            # Compute contribution of each base key
            base_contributions = []
            for j, k in enumerate(base_keys):
                c = abs(f_base[j]) * math.log(k) / k
                base_contributions.append((c, k))
            base_contributions.sort()
            n_drop = len(merged) - 1999
            keys_to_drop = set(k for _, k in base_contributions[:n_drop])
            merged = sorted(k for k in merged if k not in keys_to_drop)

        assert len(merged) <= 1999

        new_max = max(merged)
        log(f"\n  Adding {n_add} candidates, total keys={len(merged)}, max_key={new_max}")

        f_new, score_new, _ = solve_lp_cutting_plane(
            merged, margin=1e-7, time_limit=300
        )

        if f_new is None:
            log(f"  LP failed with {n_add} candidates")
            continue

        pf_new = build_solution(merged, f_new)
        analytical = compute_score_only(pf_new)
        improvement = analytical - current_best

        log(f"  LP score:     {score_new:.10f}")
        log(f"  Analytical:   {analytical:.10f}")
        log(f"  Improvement:  {improvement:.2e}")
        log(f"  Meets 1e-5:   {'YES' if improvement >= 1e-5 else 'NO'}")

        if analytical > best_score:
            best_score = analytical
            best_pf = pf_new

            sol = {"partial_function": {str(k): v for k, v in pf_new.items()}}
            with open(f"results/problem-7-prime/colgen_add{n_add}.json", "w") as f:
                json.dump(sol, f)

            if improvement >= 1e-5:
                log(f"\n  *** TARGET MET! Running MC validation... ***")
                mc = evaluate_mc(pf_new, n_samples=100_000, seed=42)
                log(f"  MC(100k): {mc:.10f} {'PASS' if mc > 0 else 'FAIL'}")

                if mc > 0:
                    mc_full = evaluate_mc(pf_new, n_samples=10_000_000, seed=42)
                    log(f"  MC(10M):  {mc_full:.15f} {'PASS' if mc_full > 0 else 'FAIL'}")

                    if mc_full > 0:
                        with open("results/problem-7-prime/colgen_best.json", "w") as f:
                            json.dump(sol, f)
                        log(f"  *** VALIDATED — ready for submission ***")
                        return

    # Summary
    log(f"\n{'='*70}")
    if best_pf:
        improvement = best_score - current_best
        log(f"Best colgen score: {best_score:.15f}")
        log(f"Improvement:       {improvement:.2e}")
        log(f"Target met:        {'YES' if improvement >= 1e-5 else 'NO'}")
    else:
        log("No improvement found via column generation.")


if __name__ == "__main__":
    main()
