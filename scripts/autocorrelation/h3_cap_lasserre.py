"""H3-cap upper bound via Lasserre level-2 SDP relaxation.

Builds the moment SDP for:
  $\\sup_F (M(F) - \\lambda C(F))$
  where $M(F) = 8 \\sum_k \\hat{F}_k^4$, degree-4 polynomial in $\\hat{F}_k$.

Lasserre level $\\ell = 2$: introduce moments $y_\\alpha$ for $|\\alpha| \\leq 4$,
PSD moment matrix $M_2(y) \\succeq 0$ of size $\\binom{n+2}{2}$. The level-2
relaxation captures the rank-1 structure of $\\hat{F}_i \\hat{F}_j$ that v4
missed, and may break the trivial $S^* \\leq 1$ bound.

At T=4 (n=5): moment matrix 21x21, 126 moments. Tractable.
At T=8 (n=9): moment matrix 55x55, 715 moments. Tractable.
At T=16 (n=17): moment matrix 171x171, 4845 moments. Probably tractable.

Status: first-attempt implementation. May still hit trivial 1.0 if the
relaxation gap is fundamental.
"""

from __future__ import annotations

import sys
import time
from itertools import combinations_with_replacement
from math import comb

sys.path.insert(0, "src")

import numpy as np

try:
    import cvxpy as cp
    HAVE_CVXPY = True
except ImportError:
    HAVE_CVXPY = False


def all_multi_indices(n: int, max_degree: int) -> list[tuple[int, ...]]:
    """All multi-indices (a_0, ..., a_{n-1}) with sum <= max_degree."""
    if n == 0:
        return [()]
    result = []
    for a0 in range(max_degree + 1):
        for tail in all_multi_indices(n - 1, max_degree - a0):
            result.append((a0,) + tail)
    return result


def index_with_degree_at_most(n: int, max_degree: int) -> list[tuple[int, ...]]:
    """All multi-indices (a_0, ..., a_{n-1}) with sum <= max_degree, ordered."""
    return all_multi_indices(n, max_degree)


def moment_matrix_indices(n: int, level: int) -> tuple[list[tuple[int, ...]], dict]:
    """Return (monomial_list, monomial_index_map).

    monomial_list[i] = the i-th monomial of degree <= level
    monomial_index_map[alpha] = i.
    """
    mons = index_with_degree_at_most(n, level)
    return mons, {m: i for i, m in enumerate(mons)}


def add_indices(a: tuple, b: tuple) -> tuple:
    return tuple(x + y for x, y in zip(a, b))


def build_moment_matrix(y_vars: dict, mons: list, idx_map: dict) -> cp.Expression:
    """Build the level-l moment matrix M_l(y) where M[i,j] = y[mons[i] + mons[j]].

    Returns a CVXPY symmetric matrix expression.
    """
    K = len(mons)
    rows = []
    for i in range(K):
        row_entries = []
        for j in range(K):
            sum_idx = add_indices(mons[i], mons[j])
            row_entries.append(y_vars[sum_idx])
        rows.append(cp.hstack(row_entries))
    return cp.vstack(rows)


def build_localizing_matrix(y_vars: dict, poly_coeffs: dict, mons: list,
                             idx_map: dict) -> cp.Expression:
    """For polynomial constraint p(x) = sum_alpha poly_coeffs[alpha] * x^alpha >= 0,
    build the localizing matrix L[i,j] = sum_alpha poly_coeffs[alpha] * y[mons[i] + mons[j] + alpha].

    Lasserre PSD: L >> 0 implies the constraint at level (level - deg(p)/2).
    """
    K = len(mons)
    rows = []
    for i in range(K):
        row_entries = []
        for j in range(K):
            entry = 0
            for alpha, coeff in poly_coeffs.items():
                if coeff == 0:
                    continue
                sum_idx = add_indices(add_indices(mons[i], mons[j]), alpha)
                entry = entry + coeff * y_vars[sum_idx]
            row_entries.append(entry if isinstance(entry, cp.Expression) else cp.Constant(entry))
        rows.append(cp.hstack(row_entries))
    return cp.vstack(rows)


def solve_lasserre_level2(lam: float, T: int, level: int = 2,
                           solver: str = "CLARABEL",
                           verbose: bool = False) -> tuple[float, dict]:
    """Solve the Lasserre level-l relaxation of:

        max  M(F) - lam * C(F)
        s.t. hat_F[0] = 1/2,
             Toeplitz hat_F PSD (F >= 0),
             |hat_F[k]| <= 1/2,
             C - (F*F)(x) >= 0 on [-1, 1] (sup-norm via Toeplitz-Caratheodory),
             M(F) = 8 * (hat_F_0^4 + 2 sum_{k>=1} hat_F_k^4)

    Variables: hat_F_0, ..., hat_F_T (n = T+1 vars), C.

    Lasserre level-l: moments y_alpha for |alpha| <= 2l (in vars hat_F_0..hat_F_T,
    ignoring C since constraints involving C are linear).
    """
    if not HAVE_CVXPY:
        raise RuntimeError("cvxpy not installed")

    n = T + 1  # number of variables (hat_F_0, ..., hat_F_T)

    # Build all moments up to degree 2*level
    moms_full = index_with_degree_at_most(n, 2 * level)
    moms_full_set = set(moms_full)
    mons_l, idx_l = moment_matrix_indices(n, level)
    K = len(mons_l)
    print(f"  Lasserre level-{level} at T={T} (n={n}): "
          f"moment matrix {K}x{K}, {len(moms_full)} moments")

    # Decision variables
    y_dict = {alpha: cp.Variable() for alpha in moms_full}
    C = cp.Variable(nonneg=True)
    Q = cp.Variable((T + 1, T + 1), symmetric=True)  # Toeplitz-Caratheodory cert

    # Helpful aliases
    e = [tuple(1 if i == k else 0 for i in range(n)) for k in range(n)]  # unit vectors
    zero = tuple([0] * n)

    constraints = []

    # Normalization: y[0] = 1 (zero-degree moment is 1)
    constraints.append(y_dict[zero] == 1)

    # hat_F_0 = 1/2: moment y[e_0] == 1/2
    constraints.append(y_dict[e[0]] == 0.5)

    # Explicit moment bounds from |hat_F_k| <= 1/2 (implied by Toeplitz, but
    # the Lasserre SDP needs them explicit to avoid unboundedness):
    # |hat_F_0^{a_0} * ... * hat_F_T^{a_T}| <= (1/2)^|alpha|
    # For all moments alpha (with |alpha| > 0):
    for alpha in moms_full:
        if sum(alpha) == 0:
            continue
        bound = (0.5) ** sum(alpha)
        constraints.append(y_dict[alpha] <= bound)
        constraints.append(y_dict[alpha] >= -bound)

    # F >= 0 via Toeplitz-Caratheodory (correct constraint, not the simpler
    # Toeplitz-PSD which is only necessary):
    #   ∃ PSD G with trace(G) = hat_F_0 and sum_i G[i, i+k] = hat_F_k for k>=1
    G_F = cp.Variable((T + 1, T + 1), symmetric=True)
    constraints.append(G_F >> 0)
    constraints.append(cp.trace(G_F) == y_dict[e[0]])
    for k in range(1, T + 1):
        diag_sum = sum(G_F[i, i + k] for i in range(T + 1 - k))
        constraints.append(diag_sum == y_dict[e[k]])

    # Lasserre PSD constraint: M_l(y) >> 0
    M_l = build_moment_matrix(y_dict, mons_l, idx_l)
    constraints.append(M_l >> 0)

    # Toeplitz-Caratheodory for sup-norm:
    # P_C(x) = C - 2 y[2 e_0] - 4 sum_{k >= 1} y[2 e_k] cos(pi k x) >= 0 on [-1, 1]
    # In form  c_0 + 2 sum_{k >= 1} c_k cos(pi k x):
    #   c_0 = C - 2 y[2 e_0]
    #   c_k = -2 y[2 e_k]  for k >= 1
    constraints.append(Q >> 0)
    constraints.append(cp.trace(Q) == C - 2 * y_dict[add_indices(e[0], e[0])])
    for k in range(1, T + 1):
        diag_sum = sum(Q[i, i + k] for i in range(T + 1 - k))
        constraints.append(diag_sum == -2 * y_dict[add_indices(e[k], e[k])])

    # Objective: maximize M(F) - lam * C
    # M(F) = 8 * (hat_F_0^4 + 2 * sum_{k>=1} hat_F_k^4)
    M_expr = 8 * y_dict[tuple(4 if k == 0 else 0 for k in range(n))]
    for k in range(1, n):
        fourth_moment = tuple(4 if i == k else 0 for i in range(n))
        M_expr += 16 * y_dict[fourth_moment]

    objective = cp.Maximize(M_expr - lam * C)
    prob = cp.Problem(objective, constraints)

    t0 = time.time()
    try:
        prob.solve(solver=solver, verbose=verbose)
    except Exception as e_inner:
        return -1.0, {"status": "error", "msg": str(e_inner)}
    elapsed = time.time() - t0

    info = {"status": prob.status, "elapsed": elapsed,
            "n_moments": len(moms_full), "moment_matrix_size": K}
    if prob.status in ("optimal", "optimal_inaccurate"):
        info.update({
            "M_value": float(M_expr.value),
            "C_value": float(C.value),
            "S_implied": float(M_expr.value) / max(float(C.value), 1e-12),
            "g_lambda": float(prob.value),
        })
    return prob.value if prob.value is not None else float("nan"), info


def main():
    print("=" * 76)
    print("H3-cap Lasserre level-2 SDP")
    print("=" * 76)

    if not HAVE_CVXPY:
        print("ERROR: cvxpy not installed.")
        return

    # Try at T=4 first (small)
    print()
    print("--- Bisection at T=4, level=2 ---")
    lam_lo, lam_hi = 0.5, 1.5
    g_lo, info_lo = solve_lasserre_level2(lam_lo, T=4, level=2)
    g_hi, info_hi = solve_lasserre_level2(lam_hi, T=4, level=2)
    print(f"  g({lam_lo}) = {g_lo:.4e}  ({info_lo['status']}, {info_lo.get('elapsed',0):.1f}s)")
    if 'C_value' in info_lo:
        print(f"    M={info_lo['M_value']:.6f}  C={info_lo['C_value']:.6f}  S={info_lo['S_implied']:.6f}")
    print(f"  g({lam_hi}) = {g_hi:.4e}  ({info_hi['status']}, {info_hi.get('elapsed',0):.1f}s)")
    if 'C_value' in info_hi:
        print(f"    M={info_hi['M_value']:.6f}  C={info_hi['C_value']:.6f}  S={info_hi['S_implied']:.6f}")

    # Bisect
    history = [(lam_lo, g_lo), (lam_hi, g_hi)]
    if g_lo > 0 and g_hi <= 0:
        for _ in range(10):
            if lam_hi - lam_lo < 1e-3:
                break
            lam_mid = 0.5 * (lam_lo + lam_hi)
            g_mid, info_mid = solve_lasserre_level2(lam_mid, T=4, level=2)
            history.append((lam_mid, g_mid))
            s_str = f"S={info_mid['S_implied']:.4f}" if 'S_implied' in info_mid else ''
            print(f"  g({lam_mid:.6f}) = {g_mid:.4e}  ({info_mid['status']})  {s_str}")
            if g_mid > 0:
                lam_lo = lam_mid
            else:
                lam_hi = lam_mid
        print(f"  T=4 UB: {lam_hi:.6f}")
    else:
        print(f"  Bisection bounds invalid: g_lo={g_lo}, g_hi={g_hi}")
        print(f"  T=4 UB:  inconclusive")

    print()
    print("=" * 76)
    print("Comparison:")
    print(f"  v4 (Toeplitz-Caratheodory only):  1.000")
    if 'C_value' in info_lo and lam_hi != float('inf'):
        print(f"  Lasserre level-2 (this script): {lam_hi:.6f}")
    print(f"  Empirical lower bound:          0.96272")
    print(f"  Trivial Cauchy-Schwarz:         1.0")
    print("=" * 76)


if __name__ == "__main__":
    main()
