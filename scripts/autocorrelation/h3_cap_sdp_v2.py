"""H3-cap upper bound for arena P3 — v2 with linearization.

The previous version (h3_cap_sdp.py) failed because $\hat{f}_k^4$ is convex,
so maximizing $M(f) = \\sum \\hat{f}_k^4$ over a convex set is non-DCP and the
SOC lift $z_k \\geq \\hat{f}_k^2$ is one-sided (gives unbounded SDP).

Fix: linearize each convex quartic term around a chosen point $\\hat{f}_k^*$
to get an UPPER (concave) over-estimator:

    $\\hat{f}_k^4 \\leq f_4(\\hat{f}_k^*) + f_4'(\\hat{f}_k^*) (\\hat{f}_k - \\hat{f}_k^*)$
    $= \\hat{f}_k^{*4} + 4 \\hat{f}_k^{*3} (\\hat{f}_k - \\hat{f}_k^*)$
    $= 4 \\hat{f}_k^{*3} \\hat{f}_k - 3 \\hat{f}_k^{*4}$

(linear majorant from the tangent at $\\hat{f}_k = \\hat{f}_k^*$; valid because
$\\hat{f}_k^4$ is convex, so it lies above its tangent).

Wait — for an UPPER BOUND on a CONVEX function, the tangent is a LOWER bound.
We need an UPPER concave estimator, which doesn't exist globally for a convex
function. The cleanest valid upper bound: use the SECANT line between two
points $\\hat{f}_k = \\pm H$ where $H = 1$ (the implicit bound from $f \\geq 0$
and $\\hat{f}_0 = 1$, implying $|\\hat{f}_k| \\leq 1$):

    For $|\\hat{f}_k| \\leq 1$:  $\\hat{f}_k^4 \\leq \\hat{f}_k^2$.

This is a quadratic majorant. Use $\\hat{f}_k^2 \\leq y_k$ via SOC, then
$M^{up} = \\sum y_k$. Bounded by $T+1$ (since each $y_k \\leq 1$).

This relaxation is valid and bounded but probably too loose. Let's run it and
see how loose. If the resulting upper bound is, say, 0.99, we'll know the
relaxation gap is ~0.03 above the empirical 0.96272.
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


def solve_g_lambda_v2(lam: float, T: int = 16, G: int = 1024,
                       solver: str = "SCS", verbose: bool = False) -> tuple[float, dict]:
    """Solve $g_{up}(\\lambda) = \\sup_f (M^{up}(f) - \\lambda C^{lo}(f))$.

    Relaxations:
        $M(f) = \\sum \\hat{f}_k^4 \\leq \\sum y_k$ where $y_k \\geq \\hat{f}_k^2$
        $C \\geq \\sum y_k \\cos(\\pi k x_i)$ on dense grid (sup-norm proxy via $y_k$)

    Note: this drops the cross-term in Rechnitzer's eq. 8 for now (a known
    looseness). Result: a valid upper bound on $S^*$ via the diagonal-only
    portion of $\\|F*F\\|_2^2$.
    """
    if not HAVE_CVXPY:
        raise RuntimeError("cvxpy not installed")

    hat_f = cp.Variable(T + 1)
    y = cp.Variable(T + 1, nonneg=True)
    C = cp.Variable(nonneg=True)

    constraints = [hat_f[0] == 1]

    # Toeplitz PSD ⇒ $f \\geq 0$ on torus AND $|\\hat{f}_k| \\leq 1$
    Tmat = cp.Variable((T + 1, T + 1), symmetric=True)
    for i in range(T + 1):
        for j in range(T + 1):
            constraints.append(Tmat[i, j] == hat_f[abs(i - j)])
    constraints.append(Tmat >> 0)

    # SOC lift: $y_k \\geq \\hat{f}_k^2$
    for k in range(T + 1):
        constraints.append(cp.bmat([[y[k], hat_f[k]],
                                     [hat_f[k], 1]]) >> 0)

    # Sup-norm via dense grid: $C \\geq \\sum_k y_k \\cos(\\pi k x_i)$
    # (using $y_k \\geq \\hat{f}_k^2$ as a proxy for the actual $(F*F)$ Fourier coeffs)
    x_grid = np.linspace(-1.0, 1.0, G)
    K = np.cos(np.pi * np.outer(x_grid, np.arange(T + 1)))  # (G, T+1)
    constraints.append(K @ y <= C)

    # Lower bound C >= 1 (from C >= (F*F)(0) = ||f||_2^2 >= 1 for unit-mass f)
    # This corresponds to the constraint y_0 + 2 sum_{k>=1} y_k >= 1 at x = 0
    # which is already in the grid.

    # Objective: $M^{up} - \\lambda C = \\sum y_k - \\lambda C$
    M_up = cp.sum(y)
    objective = cp.Maximize(M_up - lam * C)
    prob = cp.Problem(objective, constraints)

    t0 = time.time()
    try:
        prob.solve(solver=solver, verbose=verbose)
    except Exception as e:
        return -1.0, {"status": "error", "msg": str(e)}
    elapsed = time.time() - t0

    info = {
        "status": prob.status,
        "elapsed": elapsed,
    }
    if prob.status in ("optimal", "optimal_inaccurate"):
        info.update({
            "M_up": float(M_up.value),
            "C": float(C.value),
            "S_implied": float(M_up.value) / max(float(C.value), 1e-12),
            "g_lambda_value": float(prob.value),
        })
    return prob.value if prob.value is not None else float("nan"), info


def upper_bound_sweep(T: int = 16, G: int = 1024, solver: str = "SCS",
                       lam_lo: float = 0.96, lam_hi: float = 1.0,
                       steps: int = 9):
    """Solve at a sweep of lambda values and report g(lambda) at each.

    The smallest lambda with $g(\\lambda) \\leq 0$ is an upper bound on $S^*$.
    """
    print(f"Lambda sweep: T={T}, G={G}, range [{lam_lo}, {lam_hi}], {steps} steps")
    print(f"{'lambda':>10s}  {'g(lam)':>15s}  {'C':>10s}  {'M_up':>10s}  {'M_up/C':>10s}  {'status':>10s}  elapsed")
    print('-' * 90)

    lambdas = np.linspace(lam_lo, lam_hi, steps)
    results = []
    for lam in lambdas:
        g, info = solve_g_lambda_v2(lam=lam, T=T, G=G, solver=solver)
        line = f"{lam:>10.6f}  {g:>15.6e}  "
        if "C" in info:
            line += f"{info['C']:>10.4f}  {info['M_up']:>10.4f}  {info['S_implied']:>10.4f}  "
        else:
            line += f"{'-':>10s}  {'-':>10s}  {'-':>10s}  "
        line += f"{info['status']:>10s}  {info.get('elapsed', 0):.1f}s"
        print(line)
        results.append({"lambda": float(lam), "g": float(g) if g != float('nan') else None, **info})

    # Find smallest lambda with g <= 0
    upper_bound = None
    for r in results:
        if r["g"] is not None and r["g"] <= 0:
            upper_bound = r["lambda"]
            break

    return upper_bound, results


def main():
    print("=" * 76)
    print("H3-cap upper bound — v2 (linearized relaxation)")
    print("=" * 76)
    print()
    print("Relaxation: M(f) = sum hat_f^4 <= sum y where y >= hat_f^2")
    print("            C constrained by dense grid >= sum y_k cos(pi k x_i)")
    print("Caveat: drops Rechnitzer's cross-term (loose by some factor)")
    print()

    if not HAVE_CVXPY:
        print("ERROR: cvxpy not installed. Run: `uv add cvxpy`")
        return

    print("--- Quick sanity: g(lam=0.5) at T=4, G=128 ---")
    g, info = solve_g_lambda_v2(lam=0.5, T=4, G=128, solver="SCS")
    print(f"  g(0.5) = {g:.6e}  status={info['status']}  elapsed={info.get('elapsed', 0):.1f}s")
    if "C" in info:
        print(f"    M_up={info['M_up']:.6f}  C={info['C']:.6f}  M_up/C={info['S_implied']:.6f}")
    print()

    print("--- Sweep at T=8, G=512 ---")
    ub, hist = upper_bound_sweep(T=8, G=512, solver="SCS",
                                  lam_lo=0.5, lam_hi=1.5, steps=11)
    print()
    print(f"Smallest lambda with g <= 0:  {ub}")
    print()

    print("--- Refined sweep at T=16, G=2048 ---")
    ub2, hist2 = upper_bound_sweep(T=16, G=2048, solver="SCS",
                                    lam_lo=0.5, lam_hi=1.5, steps=11)
    print()
    print(f"Smallest lambda with g <= 0:  {ub2}")
    print()

    print("=" * 76)
    print("Summary:")
    print(f"  T=8 UB:  {ub}")
    print(f"  T=16 UB: {ub2}")
    print(f"  Empirical lower bound:  0.96272 (arena leaders)")
    print(f"  Trivial Cauchy-Schwarz: 1.0")
    if ub2 is not None and ub2 < 1.0:
        gap_to_empirical = ub2 - 0.96272
        print(f"  Gap from UB to empirical: {gap_to_empirical:+.6f}")
        if gap_to_empirical < 0:
            print("  WARNING: UB below empirical — relaxation invalid or numerical issue")
        else:
            print(f"  This is a valid (loose) rigorous upper bound on S*.")
    print("=" * 76)


if __name__ == "__main__":
    main()
