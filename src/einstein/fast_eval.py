"""Fast numerical evaluator for the Uncertainty Principle problem.

Two-tier approach:
  - solve_coefficients_mp: mpmath for the ill-conditioned linear system (dps=20 is enough)
  - fast_evaluate: vectorized numpy q(x) scanning + brentq refinement
"""
import numpy as np
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


def _build_g_vectorized(coeffs, degrees, xs):
    """Evaluate g(x) at an array of x values using scipy."""
    alpha = -0.5
    result = np.zeros_like(xs)
    for c, d in zip(coeffs, degrees):
        result += c * eval_genlaguerre(d, alpha, xs)
    return result


def _build_divisor_vectorized(zs, xs):
    """Evaluate x * prod((x - zi)^2) at array of x values."""
    result = xs.copy()
    for zi in zs:
        result *= (xs - zi) ** 2
    return result


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

    # Build scan grid — must extend well beyond the last root to catch far sign changes
    max_scan = max(zs) * 2.0 + 100
    max_scan = min(max_scan, 700)
    xs = np.linspace(0.1, max_scan, 15000)
    mask = np.ones(len(xs), dtype=bool)
    for zi in zs:
        mask &= np.abs(xs - zi) > 0.05
    xs = xs[mask]

    # Vectorized evaluation of q(x) = g(x) / (x * prod(x-zi)^2)
    g_vals = _build_g_vectorized(coeffs, degrees, xs)
    div_vals = _build_divisor_vectorized(zs, xs)

    with np.errstate(divide="ignore", invalid="ignore"):
        q_vals = np.where(np.abs(div_vals) > 1e-300, g_vals / div_vals, np.inf)

    # Find sign changes
    finite = np.isfinite(q_vals)
    signs = np.sign(q_vals)

    sign_changes = []
    for i in range(len(q_vals) - 1):
        if finite[i] and finite[i + 1] and signs[i] != signs[i + 1] and signs[i] != 0:
            # Refine with scalar q function
            def q_scalar(x):
                gx = sum(c * eval_genlaguerre(d, -0.5, x) for c, d in zip(coeffs, degrees))
                div = x
                for zi in zs:
                    div *= (x - zi) ** 2
                return gx / div if abs(div) > 1e-300 else np.inf
            try:
                root = brentq(q_scalar, xs[i], xs[i + 1], xtol=1e-12, maxiter=200)
                sign_changes.append(root)
            except (ValueError, RuntimeError):
                sign_changes.append((xs[i] + xs[i + 1]) / 2)

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
