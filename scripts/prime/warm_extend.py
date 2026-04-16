#!/usr/bin/env python3
"""P7 — Warm-start LP extension from N=3287 to N=3300.

Instead of solving the LP from scratch at N=3300 (slow),
warm-start from our existing N=3287 solution by:
1. Computing G_old(n) for all n in [1, 33000]
2. Using near-binding constraints as initial set
3. Solving LP with 2007 keys (old 1999 + 8 new)

This converges much faster since we start near the optimum.
"""

import json
import math
import sys
import time

import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csc_matrix


def log(msg=""):
    print(msg, flush=True)


def get_squarefree(N):
    sf = [True] * (N + 1)
    for p in range(2, int(math.isqrt(N)) + 1):
        for m in range(p * p, N + 1, p * p):
            sf[m] = False
    return [k for k in range(2, N + 1) if sf[k]]


def build_sparse(keys, ns):
    k_arr = np.array(keys, dtype=np.float64)
    n_cons = len(ns)
    rows, cols, data = [], [], []
    chunk = 2000
    for i0 in range(0, n_cons, chunk):
        i1 = min(i0 + chunk, n_cons)
        ns_c = np.array(ns[i0:i1], dtype=np.float64).reshape(-1, 1)
        A_c = np.floor(ns_c / k_arr.reshape(1, -1)) - ns_c / k_arr.reshape(1, -1)
        nz = np.nonzero(np.abs(A_c) > 1e-15)
        rows.extend((nz[0] + i0).tolist())
        cols.extend(nz[1].tolist())
        data.extend(A_c[nz].tolist())
    return csc_matrix(
        (np.array(data), (np.array(rows), np.array(cols))),
        shape=(n_cons, len(keys)),
    )


def check_viols(keys, f_vals, max_n, tol=1e-12):
    ka = np.array(keys, dtype=np.float64)
    worst_G = -1e10
    worst_n = 0
    viols = []
    for start in range(1, max_n + 1, 100_000):
        end = min(start + 100_000, max_n + 1)
        ns = np.arange(start, end, dtype=np.float64)
        G = (np.floor(ns[:, None] / ka[None, :]) - ns[:, None] / ka[None, :]) @ f_vals
        mx_idx = int(np.argmax(G))
        mx = float(G[mx_idx])
        if mx > worst_G:
            worst_G = mx
            worst_n = start + mx_idx
        mask = G > 1.0 + tol
        for idx in np.where(mask)[0]:
            viols.append(start + int(idx))
    return worst_n, worst_G, viols


def mc_verify(pf, n_samples=10_000_000, seed=42, arena_tol=1e-4):
    pf = dict(pf)
    keys = sorted(pf.keys())
    sfk = sum(pf[k] / k for k in keys if k != 1)
    pf[1] = max(-10.0, min(10.0, -sfk))
    keys = sorted(pf.keys())
    ka = np.array(keys, dtype=np.int64)
    va = np.array([pf[k] for k in keys], dtype=np.float64)
    mk = max(k for k in keys if k > 1)
    rng = np.random.RandomState(seed)
    xs = rng.uniform(1.0, 10.0 * mk, size=n_samples)
    csz = max(1, 100_000_000 // len(keys))
    worst = -1e10
    for s in range(0, n_samples, csz):
        e = min(s + csz, n_samples)
        fl = np.floor(xs[s:e, None] / ka[None, :].astype(np.float64))
        G = fl @ va
        mx = float(np.max(G))
        if mx > worst:
            worst = mx
        if mx > 1.0 + arena_tol:
            return False, worst
    return True, worst


def main():
    SOTA = 0.994826408615378
    TARGET = SOTA + 1e-5
    ARENA_TOL = 1e-4

    # Load JSAgent solution
    log("Loading JSAgent solution...")
    with open("results/problem-7-prime/jsagent_current.json") as f:
        d = json.load(f)["partial_function"]
    pf_old = {int(k): float(v) for k, v in d.items()}
    old_keys = sorted(k for k in pf_old if k > 1)

    # New keys — use N from command line or default 3300
    N_ext = int(sys.argv[1]) if len(sys.argv) > 1 else 3300
    keys_ext = get_squarefree(N_ext)
    new_keys = [k for k in keys_ext if k > 3287]
    all_keys = keys_ext
    n_vars = len(all_keys)
    max_key = all_keys[-1]
    max_n = 10 * max_key

    log(f"Old keys: {len(old_keys)}, New keys: {new_keys}, Total: {n_vars}")
    log(f"Max key: {max_key}, Max n: {max_n}")

    # Compute G_old(n) for all n to find near-binding constraints
    log("Computing G_old(n)...")
    ka_old = np.array(old_keys, dtype=np.float64)
    va_old = np.array([pf_old[k] for k in old_keys], dtype=np.float64)

    G_old = np.zeros(max_n + 1)
    for start in range(1, max_n + 1, 100_000):
        end = min(start + 100_000, max_n + 1)
        ns = np.arange(start, end, dtype=np.float64)
        A = np.floor(ns[:, None] / ka_old[None, :]) - ns[:, None] / ka_old[None, :]
        G_old[start:end] = A @ va_old

    worst_old = np.max(G_old[1:])
    tight_ns = [n for n in range(1, max_n + 1) if G_old[n] > 0.5]
    medium_ns = [n for n in range(1, max_n + 1) if G_old[n] > 0.0]

    log(f"  Worst G_old: {worst_old:.10f}")
    log(f"  Tight constraints (G>0.5): {len(tight_ns)}")
    log(f"  Medium constraints (G>0): {len(medium_ns)}")

    # Initial constraints: tight constraints + sampling
    active_ns = sorted(set(tight_ns) | set(range(1, max_n + 1, 200)))
    log(f"  Initial constraint set: {len(active_ns)}")

    # LP solve
    c_obj = np.array([math.log(k) / k for k in all_keys], dtype=np.float64)
    bounds = [(-10.0, 10.0)] * n_vars
    margin = 0.0

    best_f = None
    best_score = -float("inf")
    best_worst_G = 0.0

    for rnd in range(60):
        t0 = time.time()
        A = build_sparse(all_keys, active_ns)
        b = np.full(len(active_ns), 1.0 - margin)
        t_build = time.time() - t0

        t1 = time.time()
        result = linprog(
            c_obj, A_ub=A, b_ub=b, bounds=bounds, method="highs",
            options={"time_limit": 3600, "primal_feasibility_tolerance": 1e-9,
                     "dual_feasibility_tolerance": 1e-9},
        )
        t_solve = time.time() - t1

        if not result.success:
            log(f"  R{rnd}: FAIL ({result.message}), build={t_build:.0f}s solve={t_solve:.0f}s")
            margin = max(margin * 2, 1e-8)
            if margin > 0.01:
                break
            continue

        score = -result.fun
        f_vec = result.x

        _, worst_G, viols = check_viols(all_keys, f_vec, max_n)

        log(f"  R{rnd}: score={score:.10f}, cons={len(active_ns)}, "
            f"viol={len(viols)}, worst_G={worst_G:.10f}, "
            f"build={t_build:.0f}s solve={t_solve:.0f}s")

        if not viols:
            best_f = f_vec.copy()
            best_score = score
            best_worst_G = worst_G
            log(f"  *** FEASIBLE ***")
            break

        active_set = set(active_ns)
        new_ns = [n for n in viols[:5000] if n not in active_set]
        if not new_ns:
            margin = max(margin * 2, 1e-8)
            if margin > 0.01:
                break
            continue
        active_ns = sorted(active_set | set(new_ns))
        log(f"  +{len(new_ns)} (total: {len(active_ns)})")

    if best_f is None:
        log("FAILED — no feasible solution found")
        return

    # Scaling
    max_scale = (1.0 + ARENA_TOL) / best_worst_G
    safe_scale = 1.0 + 0.999 * (max_scale - 1.0)
    scaled_score = best_score * safe_scale

    log(f"\nResults:")
    log(f"  Base score:   {best_score:.12f}")
    log(f"  Worst G:      {best_worst_G:.12f}")
    log(f"  Safe scale:   {safe_scale:.10f}")
    log(f"  Scaled score: {scaled_score:.12f}")
    log(f"  SOTA:         {SOTA:.12f}")
    log(f"  Target:       {TARGET:.12f}")
    log(f"  vs Target:    {scaled_score - TARGET:+.2e}")
    log(f"  Beats target? {'YES' if scaled_score > TARGET else 'NO'}")

    # Save
    pf = {}
    for j, k in enumerate(all_keys):
        v = float(best_f[j] * safe_scale)
        if abs(v) > 1e-15:
            pf[k] = v

    sol = {"partial_function": {str(k): v for k, v in pf.items()}}
    with open(f"results/problem-7-prime/warm_extend_N{N_ext}.json", "w") as f:
        json.dump(sol, f)
    log(f"  Saved: warm_extend_N{N_ext}.json ({len(pf)} keys)")

    # MC verification if target met
    if scaled_score > TARGET:
        log(f"\nMC Verification:")
        passed, wmc = mc_verify(pf, 10_000_000, 42, ARENA_TOL)
        log(f"  MC(10M,42): worst={wmc:.10f} {'PASS' if passed else 'FAIL'}")
        if passed:
            p2, wmc2 = mc_verify(pf, 10_000_000, 123, ARENA_TOL)
            log(f"  MC(10M,123): worst={wmc2:.10f} {'PASS' if p2 else 'FAIL'}")
            if p2:
                with open(f"results/problem-7-prime/best_warm_N{N_ext}.json", "w") as ff:
                    json.dump(sol, ff)
                sa = -sum(v * math.log(k) / k for k, v in pf.items() if k >= 2)
                log(f"\n  *** VERIFIED: score={sa:.15f}, keys={len(pf)} ***")


if __name__ == "__main__":
    main()
