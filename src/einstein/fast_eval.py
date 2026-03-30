"""Fast numerical evaluator for the Uncertainty Principle problem.

Two-tier approach:
  - solve_coefficients_mp: mpmath for the ill-conditioned linear system
  - fast_evaluate: numba-JIT'd grid scan + brentq refinement

Performance: ~3-5x faster than pure scipy/numpy thanks to numba JIT.
"""
import numpy as np
from numba import njit, prange
from scipy.optimize import brentq
from scipy.special import eval_genlaguerre
import mpmath


def _laguerre_mp(n, alpha, x):
    """Evaluate generalized Laguerre polynomial L_n^alpha(x) with mpmath recurrence."""
    if n == 0:
        return mpmath.mpf(1)
    L_prev = mpmath.mpf(1)
    L_curr = 1 + alpha - x
    for k in range(1, n):
        L_next = ((2 * k + 1 + alpha - x) * L_curr - (k + alpha) * L_prev) / (k + 1)
        L_prev = L_curr
        L_curr = L_next
    return L_curr


def _laguerre_deriv_mp(n, alpha, x):
    """d/dx L_n^alpha(x) = -L_{n-1}^{alpha+1}(x)."""
    if n == 0:
        return mpmath.mpf(0)
    return -_laguerre_mp(n - 1, alpha + 1, x)


def solve_coefficients_mp(zs, dps=20):
    """Solve for Laguerre combination coefficients using mpmath."""
    mpmath.mp.dps = dps
    m = len(zs)
    alpha = mpmath.mpf(-1) / 2
    degrees = list(range(0, 4 * m + 4, 2))
    num_lps = len(degrees)
    num_conds = 2 * m + 2

    mat = mpmath.matrix(num_conds, num_lps)
    b = mpmath.matrix(num_conds, 1)
    b[1, 0] = mpmath.mpf(1)

    for j, deg in enumerate(degrees):
        mat[0, j] = _laguerre_mp(deg, alpha, mpmath.mpf(0))
        mat[1, j] = _laguerre_deriv_mp(deg, alpha, mpmath.mpf(0))

    for i in range(m):
        zi = mpmath.mpf(zs[i])
        for j, deg in enumerate(degrees):
            mat[2 * i + 2, j] = _laguerre_mp(deg, alpha, zi)
            mat[2 * i + 3, j] = _laguerre_deriv_mp(deg, alpha, zi)

    coeffs = mpmath.lu_solve(mat, b)
    return [float(coeffs[j]) for j in range(num_lps)], degrees


@njit(cache=True)
def _laguerre_val(n, alpha, x):
    """Evaluate generalized Laguerre L_n^alpha(x) via recurrence (numba-JIT'd)."""
    if n == 0:
        return 1.0
    L_prev = 1.0
    L_curr = 1.0 + alpha - x
    for k in range(1, n):
        L_next = ((2 * k + 1 + alpha - x) * L_curr - (k + alpha) * L_prev) / (k + 1)
        L_prev = L_curr
        L_curr = L_next
    return L_curr


@njit(cache=True, parallel=True)
def _eval_q_grid(coeffs, degrees, zs, xs):
    """Evaluate q(x) = g(x) / (x * prod(x-zi)^2) on the entire grid. JIT + parallel."""
    n = len(xs)
    q_vals = np.empty(n)
    alpha = -0.5
    for idx in prange(n):
        x = xs[idx]
        # g(x) = sum of c * L_deg^alpha(x)
        g = 0.0
        for j in range(len(coeffs)):
            g += coeffs[j] * _laguerre_val(degrees[j], alpha, x)
        # divisor = x * prod((x - zi)^2)
        div = x
        for j in range(len(zs)):
            diff = x - zs[j]
            div *= diff * diff
        if abs(div) > 1e-300:
            q_vals[idx] = g / div
        else:
            q_vals[idx] = np.inf
    return q_vals


@njit(cache=True)
def _q_scalar_jit(coeffs, degrees, zs, x):
    """Evaluate q(x) at a single point (JIT'd for brentq callbacks)."""
    alpha = -0.5
    g = 0.0
    for j in range(len(coeffs)):
        g += coeffs[j] * _laguerre_val(degrees[j], alpha, x)
    div = x
    for j in range(len(zs)):
        diff = x - zs[j]
        div *= diff * diff
    if abs(div) > 1e-300:
        return g / div
    return np.inf


def fast_evaluate(zs, dps=30):
    """Fast numerical evaluation. Returns S = largest_sign_change / (2*pi), or np.inf on failure."""
    zs = list(zs)
    m = len(zs)
    if m == 0 or any(z <= 0 for z in zs) or any(z > 300 for z in zs):
        return np.inf

    try:
        coeffs, degrees = solve_coefficients_mp(zs, dps=dps)
    except Exception:
        return np.inf

    # Scalar q function — used for brentq refinement and far-out checks
    coeffs_arr = np.array(coeffs)
    degrees_arr = np.array(degrees, dtype=np.int64)
    zs_arr = np.array(zs)

    def q_scalar(x):
        return _q_scalar_jit(coeffs_arr, degrees_arr, zs_arr, x)

    # Build scan grid: dense near roots, coarser far out
    max_root = max(zs)
    near_end = max_root + 50
    far_end = max(max_root * 3, 600)

    xs_near = np.linspace(0.1, near_end, 15000)
    xs_far = np.linspace(near_end, far_end, 5000)
    xs = np.concatenate([xs_near, xs_far[1:]])

    mask = np.ones(len(xs), dtype=bool)
    for zi in zs:
        mask &= np.abs(xs - zi) > 0.05
    xs = xs[mask]

    # JIT-compiled parallel grid evaluation (reuses arrays from above)
    q_vals = _eval_q_grid(coeffs_arr, degrees_arr, zs_arr, xs)

    # Find sign changes in the main grid
    finite = np.isfinite(q_vals)
    signs = np.sign(q_vals)

    sign_changes = []
    for i in range(len(q_vals) - 1):
        if finite[i] and finite[i + 1] and signs[i] != signs[i + 1] and signs[i] != 0:
            try:
                root = brentq(q_scalar, xs[i], xs[i + 1], xtol=1e-12, maxiter=200)
                sign_changes.append(root)
            except (ValueError, RuntimeError):
                sign_changes.append((xs[i] + xs[i + 1]) / 2)

    # CRITICAL: Check for sign changes beyond the main grid.
    # High-degree Laguerre polynomials can have sign changes at x >> max(roots).
    # We check exponentially-spaced points from the grid edge up to x=100,000.
    # Each q_scalar call is O(k) — cheap even with many checkpoints.
    last_finite_idx = len(q_vals) - 1
    while last_finite_idx >= 0 and not finite[last_finite_idx]:
        last_finite_idx -= 1

    if last_finite_idx >= 0:
        prev_x = xs[last_finite_idx]
        prev_sign = signs[last_finite_idx]
        # Exponential spacing: far_end, far_end*1.5, far_end*2.25, ... up to 100,000
        check_x = far_end
        while check_x < 100_000:
            check_x *= 1.5
            try:
                qv = q_scalar(check_x)
                if np.isfinite(qv) and qv != 0:
                    fc_sign = np.sign(qv)
                    if fc_sign != prev_sign and prev_sign != 0:
                        try:
                            root = brentq(q_scalar, prev_x, check_x, xtol=1e-8, maxiter=200)
                            sign_changes.append(root)
                        except (ValueError, RuntimeError):
                            sign_changes.append((prev_x + check_x) / 2)
                    prev_sign = fc_sign
                    prev_x = check_x
            except (OverflowError, ValueError):
                break

    if not sign_changes:
        return np.inf

    return max(sign_changes) / (2 * np.pi)


if __name__ == "__main__":
    import time

    best_roots = [
        3.1427440085666496, 4.469993893132148, 6.078689469782297,
        32.637646271046336, 38.265477818082566, 41.06153063739393,
        43.09262298321874, 50.81816373872074, 58.61770809389174,
        96.07661117430976, 111.48735817427675, 118.74229251036576,
        141.09580664199572,
    ]
    print(f"Testing k={len(best_roots)} roots...")
    t0 = time.time()
    score = fast_evaluate(best_roots)
    print(f"Fast score: {score} ({time.time() - t0:.1f}s)")
    print(f"Expected:   REDACTED")

    k6_roots = [3.64273649, 5.68246114, 33.00463486, 40.97185579, 50.1028231, 53.76768016]
    t0 = time.time()
    score6 = fast_evaluate(k6_roots)
    print(f"\nk=6 score: {score6} ({time.time() - t0:.1f}s)")
    print(f"Expected:  0.3282706174313453")

    # Benchmark: how many evals per second?
    print("\nBenchmark: 10 evaluations of k=13...")
    t0 = time.time()
    for _ in range(10):
        fast_evaluate(best_roots)
    dt = time.time() - t0
    print(f"  {dt:.1f}s total, {dt/10:.2f}s/eval, {10/dt:.1f} evals/sec")
