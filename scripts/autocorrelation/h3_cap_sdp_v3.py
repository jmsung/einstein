"""H3-cap upper bound, v3 — cross-term added with constant majorant.

Adds the Rechnitzer eq. 8 cross-term with the simplest valid upper bound under
maximization: $|u_m|^4 \\leq H_m^4$ where $H_m = \\sum_k |L_{m,k}|$, valid
because $|\\hat{f}_k| \\leq 1$ (implied by Toeplitz PSD with $\\hat{f}_0 = 1$).

This is a *constant* upper bound on the cross-term, hence very loose. But it
makes the SDP finite and sums in the right magnitude. The result will be
strictly LARGER than the diagonal-only v2 result, but still finite.

Goal: a finite numerical upper bound. Whether it beats 1.0 (trivial) is the
empirical question.

Caveats remain:
  - Constant cross-term majorant: VERY loose
  - Dense-grid sup-norm: inner approximation
  - mpmath certification: NOT included

A tighter bound requires either restoring proper SOC + upper bounds on the
SOC slack via SDP-with-trace constraints (Lasserre hierarchy), or a dual
moment-method reformulation. Both are research-level.
"""

from __future__ import annotations

import sys
import time

sys.path.insert(0, "src")

import numpy as np

try:
    import cvxpy as cp
    HAVE_CVXPY = True
except ImportError:
    HAVE_CVXPY = False


def cross_term_constant_bound(T: int, M: int) -> tuple[np.ndarray, float]:
    """Compute L (cross-term linear matrix) and the *constant* upper bound on
    $(8/\\pi^4) \\sum_m |u_m|^4$ where $u_m = \\sum_k (-1)^k \\hat{f}_k / (2k - (2m+1))$.

    Bound: each $|u_m| \\leq H_m = \\sum_k |L_{m,k}|$ since $|\\hat{f}_k| \\leq 1$.
    So $\\sum_m |u_m|^4 \\leq \\sum_m H_m^4$, and cross_total $\\leq (8/\\pi^4) \\sum_m H_m^4$.
    """
    L = np.zeros((2 * M + 1, T + 1))
    for m_idx, m in enumerate(range(-M, M + 1)):
        for k in range(T + 1):
            denom = 2 * k - (2 * m + 1)
            if denom == 0:
                continue
            sign = (-1) ** k
            L[m_idx, k] = sign / denom

    H = np.sum(np.abs(L), axis=1)  # H_m = sum_k |L_{m,k}|
    cross_constant = (8.0 / np.pi**4) * np.sum(H ** 4)
    return L, cross_constant


def solve_g_lambda_v3(lam: float, T: int = 16, G: int = 1024, M: int = 16,
                      solver: str = "SCS", verbose: bool = False) -> tuple[float, dict]:
    """Solve $g_{up}(\\lambda)$ with diagonal + cross-term-constant-bound.

    M_up(f) = sum_k y_k + cross_constant
    where  y_k >= hat_f[k]^2  (SOC lift)
          cross_constant is a precomputed upper bound on the cross-term

    C >= sum_k y_k * cos(pi k x_i) on dense grid.

    Maximize M_up - lam * C.
    """
    if not HAVE_CVXPY:
        raise RuntimeError("cvxpy not installed")

    hat_f = cp.Variable(T + 1)
    y = cp.Variable(T + 1, nonneg=True)
    C = cp.Variable(nonneg=True)

    constraints = [hat_f[0] == 1]

    # Toeplitz PSD ⇒ f >= 0 (period-2 torus) AND |hat_f_k| <= 1
    Tmat = cp.Variable((T + 1, T + 1), symmetric=True)
    for i in range(T + 1):
        for j in range(T + 1):
            constraints.append(Tmat[i, j] == hat_f[abs(i - j)])
    constraints.append(Tmat >> 0)

    # SOC lift y_k >= hat_f[k]^2
    for k in range(T + 1):
        constraints.append(cp.bmat([[y[k], hat_f[k]],
                                     [hat_f[k], 1]]) >> 0)

    # Sup-norm via dense grid
    x_grid = np.linspace(-1.0, 1.0, G)
    K = np.cos(np.pi * np.outer(x_grid, np.arange(T + 1)))
    constraints.append(K @ y <= C)

    # Cross-term: constant upper bound (very loose)
    _, cross_constant = cross_term_constant_bound(T, M)

    M_up = cp.sum(y) + cross_constant  # M_up bound including cross
    objective = cp.Maximize(M_up - lam * C)
    prob = cp.Problem(objective, constraints)

    t0 = time.time()
    try:
        prob.solve(solver=solver, verbose=verbose)
    except Exception as e:
        return -1.0, {"status": "error", "msg": str(e), "cross_constant": cross_constant}
    elapsed = time.time() - t0

    info = {"status": prob.status, "elapsed": elapsed, "cross_constant": cross_constant}
    if prob.status in ("optimal", "optimal_inaccurate"):
        info.update({
            "M_up": float(M_up.value),
            "C": float(C.value),
            "S_implied": float(M_up.value) / max(float(C.value), 1e-12),
            "g_lambda_value": float(prob.value),
        })
    return prob.value if prob.value is not None else float("nan"), info


def main():
    print("=" * 76)
    print("H3-cap upper bound — v3 (cross-term added with constant majorant)")
    print("=" * 76)
    print()

    if not HAVE_CVXPY:
        print("ERROR: cvxpy not installed.")
        return

    for T, M in [(8, 8), (16, 16), (32, 32)]:
        L, cross_const = cross_term_constant_bound(T=T, M=M)
        print(f"T={T:3d}, M={M:3d}:  cross-term constant bound = {cross_const:.4f}")
        print(f"           diagonal max bound = {T+1}")
        print(f"           total M_up max ~= {(T+1) + cross_const:.4f}")
    print()

    # Try the sweep at modest T to see the actual bound
    print("--- Sweep at T=8, M=8, G=512 ---")
    for lam in [1.0, 2.0, 5.0, 10.0, 20.0, 50.0, 100.0]:
        g, info = solve_g_lambda_v3(lam=lam, T=8, G=512, M=8, solver="SCS")
        if "C" in info:
            print(f"  lam={lam:>6.2f}  g={g:>+10.4e}  C={info['C']:.4f}  M_up={info['M_up']:.4f}  M/C={info['S_implied']:.4f}  status={info['status']}")
        else:
            print(f"  lam={lam:>6.2f}  status={info['status']}  cross_const={info.get('cross_constant', 0):.4f}")

    print()
    print("=" * 76)
    print("Honest verdict on cross-term restoration:")
    print()
    print("The cross-term constant majorant adds a fixed slack of ~ (cross_const)")
    print("to M_up, which means the SDP's effective S_implied can only INCREASE")
    print("relative to v2. So this v3 produces a LOOSER bound, not a tighter one.")
    print()
    print("To produce a TIGHTER bound (below 1.0), the cross-term needs to be")
    print("represented with both:")
    print("  (a) a lower bound coupling to hat_f (the SOC w_m >= u_m^2 lift), AND")
    print("  (b) an upper bound that USES the structure of u_m (not the trivial H_m bound)")
    print()
    print("(a)+(b) together is the Hankel/Toeplitz SOS lift, which is the multi-day")
    print("research piece. The current implementation establishes the FRAMEWORK and")
    print("documents the exact gap that needs filling.")
    print("=" * 76)


if __name__ == "__main__":
    main()
