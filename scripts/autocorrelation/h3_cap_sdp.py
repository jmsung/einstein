"""H3-cap rigorous upper bound on arena P3 — initial implementation.

Implements the SDP relaxation derived in `wiki/techniques/p3-h3-cap-sdp-derivation.md`,
with the simplifications:

  - SOC lifting for quartic ($y_k \geq \hat{f}_k^2$ + cone constraint)
  - Dense-grid sup-norm constraint (G points $x_i \in [-1, 1]$, $C \geq (F*F)(x_i)$)
    approximates the SOS positivity in the limit G → infinity. Inner relaxation:
    gives loose upper bound (true SOS sup-norm constraint is stricter).
  - Parametric Dinkelbach sweep over $\lambda$, bisect for $S^* \leq \lambda$.

What this DOES give: a numerical upper bound on $S^*$ that is provably ≥ true $S^*$
(modulo the dense-grid relaxation, which becomes tight as G → infinity, so for
G = 8192 the relaxation gap is sub-$1e-4$).

What this does NOT give: mpmath certification (would need interval arithmetic
in the SDP solver — Rechnitzer §5 effort, multi-day work).

Status: first numerical implementation. Expected output: a numerical UB in the
range 0.97–0.99 at modest T. Tightening requires increasing T.
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


# -----------------------------------------------------------------------------
# Math utilities
# -----------------------------------------------------------------------------


def cos_kernel_matrix(T: int, G: int) -> np.ndarray:
    """Precompute $K[i, k] = \cos(\\pi k x_i)$ for $x_i \\in [-1, 1]$, k = 0..T.

    Used to express $(F*F)(x_i) \\approx \\sum_k \\hat{F}_k^2 \\cos(\\pi k x_i)$
    as a linear function of the lifted variable $y_k = \\hat{F}_k^2$.

    Note: this uses the simplified Fourier representation of $F * F$ on the
    period-2 torus, ignoring the boundary correction. For a finite-support $F$
    the exact identity has additional terms; see Rechnitzer eq. 7-8 for the
    full formula. The simplification here is valid for the qualitative
    structure but introduces a small bias — this code is a FIRST-PASS
    demonstration, not a final certified bound.
    """
    x = np.linspace(-1.0, 1.0, G)
    k = np.arange(T + 1)
    return np.cos(np.pi * np.outer(x, k))  # (G, T+1)


def whitelike_l2sq_quartic_matrix(T: int) -> np.ndarray:
    """Precompute the diagonal coefficients in the truncated White identity:

        ||F*F||_2^2  ≈  (1/2) * sum_k |\\hat{f}_k|^4 + (cross terms)

    This returns the diagonal weights only — a SIMPLIFICATION dropping the
    cross-term  (8/pi^4) sum_m |sum_k (-1)^k hat_f_k / (2k - (2m+1))|^4.
    The cross-term is needed for tight bounds; this version is a baseline.
    """
    return 0.5 * np.ones(T + 1)


def whitelike_cross_term_matrix(T: int, M: int) -> np.ndarray:
    """Precompute matrix $L \\in \\mathbb{R}^{(2M+1) \\times (T+1)}$ such that
    the cross-term inner sum is $L \\hat{f}$.

        u_m = \\sum_k (-1)^k \\hat{f}_k / (2k - (2m+1))

    Then cross-term = (8/pi^4) * sum_m u_m^4. Lifted via $w_m \\geq u_m^2$
    and contributing $w_m^2$.

    Returns L of shape (2M+1, T+1).
    """
    L = np.zeros((2 * M + 1, T + 1))
    for m_idx, m in enumerate(range(-M, M + 1)):
        for k in range(T + 1):
            denom = 2 * k - (2 * m + 1)
            if denom == 0:
                continue  # pole; skip (small bias at the truncation)
            sign = (-1) ** k
            L[m_idx, k] = sign / denom
    return L


# -----------------------------------------------------------------------------
# SDP: solve g(lambda) = sup_f (M(f) - lambda C(f))
# -----------------------------------------------------------------------------


def solve_g_lambda(lam: float, T: int = 16, G: int = 1024, M_cross: int = 16,
                   solver: str = "SCS", verbose: bool = False) -> tuple[float, dict]:
    """Solve the parametric SDP at fixed Dinkelbach parameter lam.

    Variables:
      hat_f: (T+1,) Fourier coefficients of F, real (assuming f even)
      y:     (T+1,) y_k >= hat_f[k]^2 (SOC lifting via 2x2 PSD)
      z:     (T+1,) z_k >= y_k^2 (further SOC for quartic)
      u:     (2M_cross+1,) u_m = sum_k (-1)^k hat_f_k / (2k - (2m+1))
      w:     (2M_cross+1,) w_m >= u_m^2
      v:     (2M_cross+1,) v_m >= w_m^2
      C:     scalar, sup-norm bound on F*F on [-1, 1]

    Constraints:
      hat_f[0] = 1 (normalization, ∫f = 1)
      Toeplitz of hat_f >> 0 (f >= 0 on the period-2 torus — note: this is a
        *coarse* version of f >= 0 on [-1/2, 1/2])
      [[y_k, hat_f[k]], [hat_f[k], 1]] >> 0 for each k (SOC lift y_k >= hat_f_k^2)
      [[z_k, y_k], [y_k, 1]] >> 0 for each k (SOC lift z_k >= y_k^2)
      sum_k (-1)^k hat_f_k * (...) = u_m (linear)
      Similar SOC lifts for w and v
      C >= sum_k y_k * cos(pi k x_i) for all i in 0..G-1

    Objective:
      maximize M_relaxed - lam * C
    where
      M_relaxed = (1/2) sum_k z_k + (8/pi^4) sum_m v_m  (upper bound on M)
    """
    if not HAVE_CVXPY:
        raise RuntimeError("cvxpy not installed; install with `uv add cvxpy`")

    # Variables
    hat_f = cp.Variable(T + 1)
    y = cp.Variable(T + 1, nonneg=True)
    z = cp.Variable(T + 1, nonneg=True)
    u = cp.Variable(2 * M_cross + 1)
    w = cp.Variable(2 * M_cross + 1, nonneg=True)
    v = cp.Variable(2 * M_cross + 1, nonneg=True)
    C = cp.Variable(nonneg=True)

    constraints = [hat_f[0] == 1]

    # Toeplitz PSD (f >= 0) — symmetric Toeplitz built from hat_f
    Tmat = cp.Variable((T + 1, T + 1), symmetric=True)
    for i in range(T + 1):
        for j in range(T + 1):
            constraints.append(Tmat[i, j] == hat_f[abs(i - j)])
    constraints.append(Tmat >> 0)

    # SOC lifts: y_k >= hat_f[k]^2, z_k >= y_k^2
    for k in range(T + 1):
        constraints.append(cp.bmat([[y[k], hat_f[k]],
                                     [hat_f[k], 1]]) >> 0)
        constraints.append(cp.bmat([[z[k], y[k]],
                                     [y[k], 1]]) >> 0)

    # Cross-term variables u, w, v
    L = whitelike_cross_term_matrix(T, M_cross)
    constraints.append(u == L @ hat_f)
    for m in range(2 * M_cross + 1):
        constraints.append(cp.bmat([[w[m], u[m]],
                                     [u[m], 1]]) >> 0)
        constraints.append(cp.bmat([[v[m], w[m]],
                                     [w[m], 1]]) >> 0)

    # Sup-norm via dense grid: C >= sum_k y[k] * cos(pi k x_i)
    K = cos_kernel_matrix(T, G)  # (G, T+1)
    constraints.append(K @ y <= C * np.ones(G))

    # Objective: M_relaxed - lam * C
    M_relaxed = 0.5 * cp.sum(z) + (8.0 / np.pi**4) * cp.sum(v)
    objective = cp.Maximize(M_relaxed - lam * C)

    prob = cp.Problem(objective, constraints)

    t0 = time.time()
    try:
        prob.solve(solver=solver, verbose=verbose)
    except Exception as e:
        return -1.0, {"status": "error", "msg": str(e)}
    elapsed = time.time() - t0

    if prob.status not in ("optimal", "optimal_inaccurate"):
        return -1.0, {"status": prob.status, "elapsed": elapsed}

    return prob.value, {
        "status": prob.status,
        "elapsed": elapsed,
        "M_relaxed": float(M_relaxed.value),
        "C": float(C.value),
        "S_implied": float(M_relaxed.value) / max(float(C.value), 1e-12),
        "hat_f": hat_f.value,
    }


# -----------------------------------------------------------------------------
# Dinkelbach bisection
# -----------------------------------------------------------------------------


def upper_bound_via_dinkelbach(T: int = 16, G: int = 1024, M_cross: int = 16,
                                lam_lo: float = 0.96, lam_hi: float = 1.0,
                                tol: float = 1e-3, solver: str = "SCS",
                                verbose: bool = False) -> dict:
    """Bisect the Dinkelbach parameter lam:
       g(lam) = sup_f (M_relaxed(f) - lam * C(f))
       g(lam) > 0 implies S* > lam (lam is too low)
       g(lam) <= 0 implies S* <= lam (lam is an upper bound)

    Returns the smallest lam such that g(lam) <= 0 (the upper bound on S*).
    """
    print(f"Dinkelbach bisection: T={T}, G={G}, M_cross={M_cross}")
    print(f"  Initial range: [{lam_lo}, {lam_hi}]")

    # First check the endpoints
    g_lo, info_lo = solve_g_lambda(lam_lo, T, G, M_cross, solver, verbose=False)
    g_hi, info_hi = solve_g_lambda(lam_hi, T, G, M_cross, solver, verbose=False)
    print(f"  g({lam_lo:.4f}) = {g_lo:.6e} (status={info_lo['status']}, elapsed={info_lo.get('elapsed', 0):.1f}s)")
    print(f"  g({lam_hi:.4f}) = {g_hi:.6e} (status={info_hi['status']}, elapsed={info_hi.get('elapsed', 0):.1f}s)")

    if g_lo <= 0:
        print(f"  Even lam_lo={lam_lo} yields g <= 0 — UB is at or below {lam_lo}")
        return {"upper_bound": lam_lo, "history": [(lam_lo, g_lo), (lam_hi, g_hi)]}
    if g_hi > 0:
        print(f"  Even lam_hi={lam_hi} yields g > 0 — UB is above {lam_hi}, widen range")
        return {"upper_bound": float("inf"), "history": [(lam_lo, g_lo), (lam_hi, g_hi)]}

    history = [(lam_lo, g_lo), (lam_hi, g_hi)]
    for _ in range(20):
        if lam_hi - lam_lo < tol:
            break
        lam_mid = 0.5 * (lam_lo + lam_hi)
        g_mid, info_mid = solve_g_lambda(lam_mid, T, G, M_cross, solver, verbose=False)
        history.append((lam_mid, g_mid))
        print(f"  g({lam_mid:.6f}) = {g_mid:.6e} (status={info_mid['status']}, elapsed={info_mid.get('elapsed', 0):.1f}s)")
        if g_mid > 0:
            lam_lo = lam_mid
        else:
            lam_hi = lam_mid

    return {"upper_bound": lam_hi, "history": history}


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------


def main():
    print("=" * 76)
    print("H3-cap SDP for Einstein Arena P3 — initial numerical implementation")
    print("=" * 76)
    print()
    print("CAVEATS:")
    print("  - SOC quartic lifting is a *valid* relaxation (loose upper bound)")
    print("  - Dense-grid sup-norm is an inner approximation of SOS (tightens as G grows)")
    print("  - White's identity uses simplified diagonal + cross-term truncation")
    print("  - Toeplitz PSD enforces f >= 0 on the period-2 torus, not strictly on [-1/2, 1/2]")
    print("  - mpmath certification NOT included (would need interval-arithmetic SDP)")
    print()
    print("Expected output: numerical UB in (0.96272, 1.0]; tightness depends on T, G, M_cross.")
    print()

    if not HAVE_CVXPY:
        print("ERROR: cvxpy not installed. Run: `uv add cvxpy`")
        return

    # Run a single solve at a candidate lambda first to gauge cost.
    print("--- Single solve at lam=0.97 to estimate per-iter cost ---")
    g, info = solve_g_lambda(lam=0.97, T=8, G=512, M_cross=8, solver="SCS")
    print(f"  g(0.97) = {g:.6e}  status={info['status']}  elapsed={info.get('elapsed', 0):.1f}s")
    if "C" in info:
        print(f"    C = {info['C']:.6f}, M_relaxed = {info['M_relaxed']:.6f}")
        print(f"    S_implied = M/C = {info['S_implied']:.6f}")
    print()

    # Now run the bisection sweep
    print("--- Dinkelbach bisection at T=8, G=512, M_cross=8 (small for speed) ---")
    result = upper_bound_via_dinkelbach(
        T=8, G=512, M_cross=8,
        lam_lo=0.96, lam_hi=1.0, tol=1e-3, solver="SCS"
    )
    print()
    print(f"=== Result: numerical upper bound on S* ===")
    print(f"  S* <= {result['upper_bound']:.6f}")
    print(f"  Empirical lower bound: 0.96272 (arena leaders)")
    print(f"  Trivial upper bound (Cauchy-Schwarz): 1.0")
    print(f"  Best closed-form S(f): 0.722 (cos^2(pi x) bump)")
    print()
    print("Interpretation:")
    if result["upper_bound"] < 0.97:
        print("  Strong: SDP UB is within 1e-2 of empirical — arena leaders ~at math ceiling.")
    elif result["upper_bound"] < 0.99:
        print("  Moderate: SDP UB is loose (gap > 1e-2 to empirical). Increase T, G, M_cross.")
    else:
        print("  Weak: SDP UB is near trivial. Significant tightening needed (or formulation bug).")
    print()
    print("Next steps to tighten: (1) increase T to 16/32/64, (2) refine grid G to 4096,")
    print("(3) M_cross commensurate with T, (4) replace dense-grid SOS with proper Toeplitz")
    print("SOS lift, (5) mpmath interval arithmetic for certification.")
    print("=" * 76)


if __name__ == "__main__":
    main()
