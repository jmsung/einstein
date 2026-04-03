"""LP optimizer for Problem 7 — Prime Number Theorem certificate.

Uses cutting-plane LP: start with few constraints, iteratively add violated ones.
This scales to large N where the full constraint matrix would be too big.

Key identity: floor(x/k) = floor(floor(x)/k) — only integer points matter.
After normalization: constraint becomes sum f(k)*(floor(n/k) - n/k) <= 1.
"""

import json
import math
import os
import time

import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix


def get_squarefree(N: int) -> list[int]:
    sf = [True] * (N + 1)
    for p in range(2, int(math.isqrt(N)) + 1):
        for m in range(p * p, N + 1, p * p):
            sf[m] = False
    return [k for k in range(2, N + 1) if sf[k]]


def build_constraint_rows(keys: list[int], ns: list[int]) -> coo_matrix:
    """Build sparse constraint matrix for given integer points n."""
    n_cons = len(ns)
    n_vars = len(keys)
    rows, cols, data = [], [], []
    for j, k in enumerate(keys):
        for i, n in enumerate(ns):
            val = (n // k) - n / k  # floor(n/k) - n/k
            if abs(val) > 1e-15:
                rows.append(i)
                cols.append(j)
                data.append(val)
    return coo_matrix(
        (np.array(data), (np.array(rows), np.array(cols))),
        shape=(n_cons, n_vars),
    ).tocsc()


def check_violations(pf: dict[int, float], max_n: int) -> list[tuple[int, float]]:
    """Find all integer points where G(n) > 1."""
    keys = sorted(pf.keys())
    ka = np.array(keys, dtype=np.int64)
    va = np.array([pf[k] for k in keys], dtype=np.float64)

    violations = []
    chunk = 500_000
    for start in range(1, max_n + 1, chunk):
        end = min(start + chunk, max_n + 1)
        ns = np.arange(start, end, dtype=np.float64)
        G = np.floor(ns[:, None] / ka[None, :]) @ va
        mask = G > 1.0 + 1e-12
        for idx in np.where(mask)[0]:
            violations.append((start + idx, float(G[idx])))

    violations.sort(key=lambda x: -x[1])
    return violations


def solve_cutting_plane(
    N: int,
    *,
    max_keys: int = 1999,
    constraint_mult: int = 10,
    margin: float = 1e-6,
    max_rounds: int = 50,
    verbose: bool = True,
) -> tuple[dict[int, float] | None, float]:
    keys = get_squarefree(N)
    if len(keys) > max_keys:
        keys = keys[:max_keys]
    n_vars = len(keys)
    max_key = keys[-1]
    max_n = constraint_mult * max_key

    if verbose:
        print(f"  vars={n_vars}, max_key={max_key}, constraint_range=[1,{max_n}]")

    c_obj = np.array([math.log(k) / k for k in keys], dtype=np.float64)
    bounds = [(-10.0, 10.0)] * n_vars

    # Initial constraints: n = 1..N (where constraints are tightest)
    # Plus every 100th integer up to max_n for coverage
    active_ns = sorted(set(range(1, min(N + 1, max_n + 1))) | set(range(1, max_n + 1, 100)))
    best_pf = None
    best_score = -float("inf")

    for rnd in range(max_rounds):
        t0 = time.time()

        A = build_constraint_rows(keys, active_ns)
        b = np.full(len(active_ns), 1.0 - margin, dtype=np.float64)

        result = linprog(
            c_obj, A_ub=A, b_ub=b, bounds=bounds, method="highs",
            options={"time_limit": 300, "primal_feasibility_tolerance": 1e-9},
        )
        t_solve = time.time() - t0

        if not result.success:
            if verbose:
                print(f"  Round {rnd}: LP failed ({result.message}), {t_solve:.0f}s")
            margin *= 2
            if verbose:
                print(f"  Increasing margin to {margin:.2e}")
            if margin > 0.01:
                break
            continue

        score = -result.fun
        f_vec = result.x

        # Build solution
        pf = {k: float(f_vec[j]) for j, k in enumerate(keys) if abs(f_vec[j]) > 1e-15}
        sum_fk = sum(pf.get(k, 0.0) / k for k in keys)
        f1 = max(-10.0, min(10.0, -sum_fk))
        pf[1] = f1

        # Check ALL integer violations
        violations = check_violations(pf, max_n)
        n_viol = len(violations)
        worst_G = violations[0][1] if violations else 0.0

        if verbose:
            print(
                f"  Round {rnd}: score={score:.8f}, cons={len(active_ns)}, "
                f"viol={n_viol}, worst_G={worst_G:.8f}, {t_solve:.0f}s"
            )

        if n_viol == 0:
            best_pf = dict(pf)
            best_score = score
            if verbose:
                print(f"  *** FEASIBLE at score={score:.8f} ***")
            break

        # Add violated points
        new_ns = [n for n, _ in violations[:5000] if n not in set(active_ns)]
        if not new_ns:
            margin *= 2
            if verbose:
                print(f"  No new cutting planes. Margin -> {margin:.2e}")
            if margin > 0.01:
                break
            continue

        active_ns = sorted(set(active_ns) | set(new_ns))
        if verbose:
            print(f"  Added {len(new_ns)} cutting planes")

    return best_pf, best_score


def evaluate_mc(pf: dict[int, float], n_samples: int = 10_000_000, seed: int = 42) -> float:
    from einstein.prime import evaluate
    sol = {"partial_function": {str(k): v for k, v in pf.items()}}
    return evaluate(sol, n_samples=n_samples, seed=seed)


def main():
    os.makedirs("results/problem-7-prime", exist_ok=True)
    best_overall = None
    best_overall_score = 0

    for N in [1000, 1500, 2000, 2500, 3000, 4000, 5000]:
        print(f"\n{'='*60}")
        print(f"N={N}")
        print(f"{'='*60}")

        pf, score = solve_cutting_plane(N, margin=1e-6, verbose=True)

        if pf is None:
            print("  No solution")
            continue

        # Score check
        from einstein.prime import compute_score_only
        s_analytical = compute_score_only(pf)

        # Quick MC
        s_mc_fast = evaluate_mc(pf, n_samples=100_000, seed=42)
        print(f"  Analytical: {s_analytical:.8f}")
        print(f"  MC(100k):   {s_mc_fast:.8f} {'PASS' if s_mc_fast > 0 else 'FAIL'}")

        # Save
        sol = {"partial_function": {str(k): v for k, v in pf.items()}}
        with open(f"results/problem-7-prime/lp_N{N}.json", "w") as f:
            json.dump(sol, f)

        if s_mc_fast > 0 and s_mc_fast > best_overall_score:
            # Full MC validation
            print("  Full 10M MC validation...")
            s_full = evaluate_mc(pf, n_samples=10_000_000, seed=42)
            print(f"  MC(10M):    {s_full:.8f} {'PASS' if s_full > 0 else 'FAIL'}")

            if s_full > best_overall_score:
                best_overall = pf
                best_overall_score = s_full

                with open("results/problem-7-prime/best.json", "w") as f:
                    json.dump(sol, f)
                print(f"  *** New best: {s_full:.8f} ***")

    # Summary
    print(f"\n{'='*60}")
    print(f"Best score: {best_overall_score:.8f}")


if __name__ == "__main__":
    main()
