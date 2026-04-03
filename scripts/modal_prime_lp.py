"""Modal cloud LP solver for Problem 7 — Prime Number Theorem.

Solves the LP on a high-CPU cloud instance for N=2938 (matching top leaderboard).
Uses HiGHS via scipy with extended time limits.
"""

import modal
import json

app = modal.App("prime-lp")

image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install("numpy", "scipy", "highspy")
)


@app.function(
    image=image,
    cpu=8,
    memory=32768,
    timeout=7200,  # 2 hours
)
def solve_prime_lp(N: int = 2938, margin: float = 1e-6) -> dict:
    """Solve the PNT certificate LP on cloud compute."""
    import math
    import time
    import numpy as np
    from scipy.optimize import linprog

    def get_squarefree(N):
        sf = [True] * (N + 1)
        for p in range(2, int(math.isqrt(N)) + 1):
            for m in range(p * p, N + 1, p * p):
                sf[m] = False
        return [k for k in range(2, N + 1) if sf[k]]

    keys = get_squarefree(N)
    if len(keys) > 1999:
        keys = keys[:1999]
    n_vars = len(keys)
    max_key = keys[-1]
    max_n = 10 * max_key

    print(f"N={N}, vars={n_vars}, max_key={max_key}, constraints={max_n}")

    # Objective
    c_obj = np.array([math.log(k) / k for k in keys], dtype=np.float64)
    bounds = [(-10.0, 10.0)] * n_vars

    # Build full constraint matrix
    t0 = time.time()
    ns = np.arange(1, max_n + 1, dtype=np.int64)
    A = np.empty((max_n, n_vars), dtype=np.float64)
    for j, k in enumerate(keys):
        A[:, j] = (ns // k) - ns / k
    b = np.full(max_n, 1.0 - margin, dtype=np.float64)
    print(f"Matrix built: {max_n}x{n_vars} in {time.time()-t0:.1f}s")

    # Solve with generous time limit
    t0 = time.time()
    result = linprog(
        c_obj, A_ub=A, b_ub=b, bounds=bounds, method="highs",
        options={
            "time_limit": 6000,
            "primal_feasibility_tolerance": 1e-9,
            "dual_feasibility_tolerance": 1e-9,
        },
    )
    t_solve = time.time() - t0
    print(f"LP: status={result.status}, msg={result.message}, time={t_solve:.0f}s")

    if result.x is None:
        return {"error": result.message, "score": 0}

    score = float(-result.fun) if result.success else float(-c_obj @ result.x)
    f_vec = result.x

    # Build solution
    pf = {}
    for j, k in enumerate(keys):
        if abs(f_vec[j]) > 1e-15:
            pf[k] = float(f_vec[j])

    sum_fk = sum(pf.get(k, 0) / k for k in keys)
    f1 = max(-10.0, min(10.0, -sum_fk))
    pf[1] = f1

    # Verify constraints
    ka = np.array(sorted(pf.keys()), dtype=np.int64)
    va = np.array([pf[k] for k in sorted(pf.keys())])
    worst = -999
    for s in range(1, max_n + 1, 500000):
        e = min(s + 500000, max_n + 1)
        nsa = np.arange(s, e, dtype=np.float64)
        G = np.floor(nsa[:, None] / ka[None, :]) @ va
        worst = max(worst, float(np.max(G)))

    print(f"Score={score:.8f}, worst_G={worst:.8f}, keys={len(pf)}, f1={f1:.6f}")

    # MC validation
    rng = np.random.RandomState(42)
    x_max = 10.0 * max(pf.keys())
    x_samples = rng.uniform(1.0, x_max, size=10_000_000)
    mc_pass = True
    chunk = 500000
    for s in range(0, len(x_samples), chunk):
        e = min(s + chunk, len(x_samples))
        floors = np.floor(x_samples[s:e, None] / ka[None, :])
        G = floors @ va
        if np.any(G > 1.0 + 1e-12):
            mc_pass = False
            break

    if mc_pass:
        log_k = np.log(ka.astype(np.float64))
        mc_score = float(-np.sum(va * log_k / ka))
        print(f"MC(10M): {mc_score:.8f} PASS")
    else:
        mc_score = 0.0
        print("MC(10M): FAIL")

    return {
        "score": score,
        "mc_score": mc_score,
        "worst_G": worst,
        "n_keys": len(pf),
        "partial_function": {str(k): v for k, v in pf.items()},
        "solve_time": t_solve,
    }


@app.local_entrypoint()
def main():
    import os

    for N in [3287]:
        print(f"\n{'='*60}")
        print(f"Solving LP with N={N} on Modal cloud")
        print(f"{'='*60}")

        result = solve_prime_lp.remote(N=N, margin=1e-6)

        print(f"\nResult: score={result['score']:.8f}, MC={result['mc_score']:.8f}")
        print(f"  worst_G={result['worst_G']:.8f}, keys={result['n_keys']}")
        print(f"  solve_time={result.get('solve_time', 0):.0f}s")

        if result["mc_score"] > 0:
            os.makedirs("results/problem-7-prime", exist_ok=True)
            sol = {"partial_function": result["partial_function"]}
            with open(f"results/problem-7-prime/modal_N{N}.json", "w") as f:
                json.dump(sol, f)
            print(f"  Saved to results/problem-7-prime/modal_N{N}.json")

        if result["mc_score"] > 0:
            print(f"  Solution validated (MC passed)")
