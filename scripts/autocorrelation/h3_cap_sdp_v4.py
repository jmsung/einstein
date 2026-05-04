"""H3-cap upper bound, v4 — Toeplitz-Carathéodory sup-norm SOS.

KEY INSIGHT (from re-reading Rechnitzer eq. 8 more carefully):

  Working directly with the Fourier-series coefficients $\\hat{F}(k)$ on the
  period-2 torus ($\\hat{F}(0) = 1/2$ for unit-mass $f$ extended by 0):

      $\\|F * F\\|_2^2 = 8 \\sum_k |\\hat{F}(k)|^4$

  No cross-term! The cross-term in Rechnitzer's eq. 8 only appears under the
  *change of variables* $\\hat{F}(k) = (1/2) \\hat{f}(k/2)$ where $\\hat{f}$ is
  the continuous Fourier transform on $\\mathbb{R}$. By staying in the
  $\\hat{F}$ formulation, we avoid that piece entirely.

  Similarly the autoconvolution Fourier on torus:
      $(F*F)(x) = 2 \\hat{F}_0^2 + 4 \\sum_{k \\geq 1} \\hat{F}_k^2 \\cos(\\pi k x)$

  Sup-norm $\\|F*F\\|_\\infty \\leq C$ becomes a trig-poly positivity
  constraint, exactly Toeplitz-Carathéodory.

The remaining issue: $\\hat{F}_k^4$ is convex, maximizing → non-DCP. Use:
  $\\hat{F}_k^4 = (\\hat{F}_k^2)^2 \\leq y_k \\cdot |\\hat{F}_k^2|$
  with $y_k \\geq \\hat{F}_k^2$ (SOC) and $|\\hat{F}_k| \\leq 1/2$ (from
  Toeplitz PSD with $\\hat{F}_0 = 1/2$):
  $\\Rightarrow \\hat{F}_k^4 \\leq (1/4) y_k$.

So $M^{up} = 8 \\hat{F}_0^4 + 16 \\sum_{k \\geq 1} (1/4) y_k = 1/2 + 4 \\sum_{k \\geq 1} y_k$.

The SDP balances: large $y_k$ inflates $M^{up}$ (good for max), but also
violates the Toeplitz-Carathéodory sup-norm constraint (forcing $C$ up).

This is a *real* coupled SDP. Run and see.
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


def solve_g_lambda_v4(lam: float, T: int = 8, solver: str = "SCS",
                      verbose: bool = False) -> tuple[float, dict]:
    """Solve $g_{up}(\\lambda) = \\sup_{F} (M^{up}(F) - \\lambda C(F))$
    with proper Toeplitz-Carathéodory sup-norm SOS constraint.

    Variables:
      hat_F:   real, shape (T+1,). hat_F[0] = 1/2 fixed.
      y:       real, shape (T+1,). y_k >= hat_F[k]^2 (SOC).
      C:       scalar, sup-norm bound.
      Q:      real symmetric (T+1, T+1), PSD (Toeplitz-Carathéodory cert).

    Constraints:
      hat_F[0] = 1/2
      Toeplitz of hat_F PSD (for F >= 0 on torus, hence f >= 0 on [-1/2, 1/2])
      [[y_k, hat_F[k]], [hat_F[k], 1]] >> 0   (SOC: y_k >= hat_F[k]^2)
      Q >> 0
      diag(Q) sum == C - 2 y_0           (constant coefficient of P_C)
      sum_{i} Q[i, i+k] == -2 y_k        for k = 1..T  (cos coefficient)
      |hat_F_k| <= 1/2                    (implicit from Toeplitz; add explicitly for tightness)

    Objective: maximize M^{up} - lam * C  where  M^{up} = 1/2 + 4 sum_{k>=1} y_k.
    """
    if not HAVE_CVXPY:
        raise RuntimeError("cvxpy not installed")

    hat_F = cp.Variable(T + 1)
    y = cp.Variable(T + 1, nonneg=True)
    C = cp.Variable(nonneg=True)
    Q = cp.Variable((T + 1, T + 1), symmetric=True)

    constraints = [hat_F[0] == 0.5]

    # Toeplitz of hat_F PSD: F >= 0 on torus
    Tmat = cp.Variable((T + 1, T + 1), symmetric=True)
    for i in range(T + 1):
        for j in range(T + 1):
            constraints.append(Tmat[i, j] == hat_F[abs(i - j)])
    constraints.append(Tmat >> 0)

    # SOC lift: y_k >= hat_F[k]^2
    for k in range(T + 1):
        constraints.append(cp.bmat([[y[k], hat_F[k]],
                                     [hat_F[k], 1]]) >> 0)

    # Toeplitz-Carathéodory for sup-norm:
    # P_C(x) = C - 2 y_0 - 4 sum_{k>=1} y_k cos(pi k x) >= 0 on torus
    # In the form  c_0 + 2 sum_{k>=1} c_k cos(pi k x) >= 0:
    #   c_0 = C - 2 y_0
    #   c_k = -2 y_k for k >= 1
    # Toeplitz-Carathéodory: ∃ PSD Q with trace(Q) = c_0, sum_{i} Q[i, i+k] = c_k
    constraints.append(Q >> 0)
    constraints.append(cp.trace(Q) == C - 2 * y[0])
    for k in range(1, T + 1):
        # sum of k-th super-diagonal of Q
        diag_sum = sum(Q[i, i + k] for i in range(T + 1 - k))
        constraints.append(diag_sum == -2 * y[k])

    # Explicit |hat_F_k| <= 1/2 (from Toeplitz, but cvxpy may not propagate)
    for k in range(1, T + 1):
        constraints.append(hat_F[k] <= 0.5)
        constraints.append(hat_F[k] >= -0.5)

    # M^{up} using bound hat_F_k^4 <= y_k / 4 (since y_k >= hat_F_k^2 and |hat_F_k| <= 1/2)
    # M(F) = 8 sum_k hat_F_k^4 = 8 * hat_F_0^4 + 16 * sum_{k>=1} hat_F_k^4
    #      <= 8 * (1/2)^4 + 16 * sum_{k>=1} (y_k / 4)
    #      = 1/2 + 4 * sum_{k>=1} y_k
    M_up = 0.5 + 4 * cp.sum(y[1:])

    objective = cp.Maximize(M_up - lam * C)
    prob = cp.Problem(objective, constraints)

    t0 = time.time()
    try:
        prob.solve(solver=solver, verbose=verbose)
    except Exception as e:
        return -1.0, {"status": "error", "msg": str(e)}
    elapsed = time.time() - t0

    info = {"status": prob.status, "elapsed": elapsed}
    if prob.status in ("optimal", "optimal_inaccurate"):
        info.update({
            "M_up": float(M_up.value),
            "C": float(C.value),
            "S_implied": float(M_up.value) / max(float(C.value), 1e-12),
            "g_lambda_value": float(prob.value),
            "y": y.value,
            "hat_F": hat_F.value,
        })
    return prob.value if prob.value is not None else float("nan"), info


def upper_bound_bisect_v4(T: int = 8, solver: str = "SCS",
                          lam_lo: float = 0.5, lam_hi: float = 1.0,
                          tol: float = 1e-3) -> dict:
    """Bisect on lambda to find smallest lambda with $g(\\lambda) \\leq 0$.

    Returns dict with keys 'upper_bound', 'history'.
    """
    print(f"v4 bisection at T={T}, range [{lam_lo}, {lam_hi}], tol={tol}")
    g_lo, info_lo = solve_g_lambda_v4(lam_lo, T, solver)
    g_hi, info_hi = solve_g_lambda_v4(lam_hi, T, solver)
    print(f"  g({lam_lo:.4f}) = {g_lo:.4e}  ({info_lo['status']}, {info_lo.get('elapsed', 0):.1f}s)")
    if "C" in info_lo:
        print(f"    C={info_lo['C']:.4f}  M_up={info_lo['M_up']:.4f}  S={info_lo['S_implied']:.4f}")
    print(f"  g({lam_hi:.4f}) = {g_hi:.4e}  ({info_hi['status']}, {info_hi.get('elapsed', 0):.1f}s)")
    if "C" in info_hi:
        print(f"    C={info_hi['C']:.4f}  M_up={info_hi['M_up']:.4f}  S={info_hi['S_implied']:.4f}")

    if g_lo <= 0:
        print(f"  g(lo) <= 0 already. UB <= {lam_lo}")
        return {"upper_bound": lam_lo, "history": [(lam_lo, g_lo), (lam_hi, g_hi)]}
    if g_hi > 0:
        print(f"  g(hi) > 0. Need higher lam_hi.")
        return {"upper_bound": float("inf"), "history": [(lam_lo, g_lo), (lam_hi, g_hi)]}

    history = [(lam_lo, g_lo), (lam_hi, g_hi)]
    for _ in range(15):
        if lam_hi - lam_lo < tol:
            break
        lam_mid = 0.5 * (lam_lo + lam_hi)
        g_mid, info_mid = solve_g_lambda_v4(lam_mid, T, solver)
        history.append((lam_mid, g_mid))
        s_str = f"S={info_mid['S_implied']:.4f}" if "S_implied" in info_mid else ""
        print(f"  g({lam_mid:.6f}) = {g_mid:.4e}  ({info_mid['status']})  {s_str}")
        if g_mid > 0:
            lam_lo = lam_mid
        else:
            lam_hi = lam_mid

    return {"upper_bound": lam_hi, "history": history}


def main():
    print("=" * 76)
    print("H3-cap upper bound — v4 (Toeplitz-Carathéodory sup-norm SOS)")
    print("=" * 76)
    print()
    if not HAVE_CVXPY:
        print("ERROR: cvxpy not installed.")
        return

    # First diagnostic: check the SDP at a single lam value.
    print("--- Single solve at lam=0.7, T=4 (smoke test) ---")
    g, info = solve_g_lambda_v4(lam=0.7, T=4, solver="SCS")
    print(f"  g(0.7) = {g:.6f}")
    if "C" in info:
        print(f"  M_up={info['M_up']:.6f}  C={info['C']:.6f}  S_implied={info['S_implied']:.6f}")
        print(f"  hat_F = {info['hat_F']}")
        print(f"  y     = {info['y']}")
    print()

    print("--- Bisection at T=4 ---")
    r4 = upper_bound_bisect_v4(T=4, solver="SCS", lam_lo=0.5, lam_hi=1.5, tol=1e-3)
    print(f"  T=4 UB:  {r4['upper_bound']:.6f}")
    print()

    print("--- Bisection at T=8 ---")
    r8 = upper_bound_bisect_v4(T=8, solver="SCS", lam_lo=0.5, lam_hi=1.5, tol=1e-3)
    print(f"  T=8 UB:  {r8['upper_bound']:.6f}")
    print()

    print("--- Bisection at T=16 ---")
    r16 = upper_bound_bisect_v4(T=16, solver="SCS", lam_lo=0.5, lam_hi=1.5, tol=1e-3)
    print(f"  T=16 UB: {r16['upper_bound']:.6f}")
    print()

    print("=" * 76)
    print("Summary:")
    print(f"  T=4 UB:  {r4['upper_bound']:.6f}")
    print(f"  T=8 UB:  {r8['upper_bound']:.6f}")
    print(f"  T=16 UB: {r16['upper_bound']:.6f}")
    print(f"  Empirical lower bound:  0.96272 (arena leaders)")
    print(f"  Trivial Cauchy-Schwarz: 1.0")
    if r16["upper_bound"] != float("inf") and r16["upper_bound"] < 1.0:
        gap = r16["upper_bound"] - 0.96272
        print(f"  T=16 UB gap to empirical: {gap:+.6f}")
        print("  *** SDP UB IS BELOW TRIVIAL — first non-trivial bound on S* ***")
    print("=" * 76)


if __name__ == "__main__":
    main()
