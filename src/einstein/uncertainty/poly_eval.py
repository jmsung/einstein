"""Fast polynomial-based evaluator for the Uncertainty Principle problem.

Uses mpmath for exact coefficient solving + monomial conversion, then
numpy.roots for companion-matrix root-finding. ~0.3s per evaluation,
correct for all k values (unlike the grid-based fast evaluator).
"""
import mpmath
import numpy as np


def _laguerre_mp(n, alpha, x):
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
    if n == 0:
        return mpmath.mpf(0)
    return -_laguerre_mp(n - 1, alpha + 1, x)


def _poly_mul_mp(a, b):
    result = [mpmath.mpf(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            result[i + j] += ai * bj
    return result


def poly_evaluate(zs, dps=100):
    """Evaluate score using mpmath polynomial construction + numpy.roots.

    Returns S = largest_sign_change / (2*pi), or np.inf on failure.
    ~0.3s per evaluation for k=19.
    """
    zs = list(zs)
    m = len(zs)
    if m == 0 or any(z <= 0 for z in zs) or any(z > 300 for z in zs):
        return np.inf

    mpmath.mp.dps = dps
    alpha = mpmath.mpf(-1) / 2
    degrees = list(range(0, 4 * m + 4, 2))

    # Solve linear system for Laguerre combination coefficients
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

    try:
        coeffs = mpmath.lu_solve(mat, b)
    except Exception:
        return np.inf

    # Build g(x) monomial coefficients: g_mono[k] = coeff of x^k
    max_deg = max(degrees)
    g_mono = [mpmath.mpf(0)] * (max_deg + 1)
    for j, deg in enumerate(degrees):
        c_j = coeffs[j]
        for k in range(deg + 1):
            binom = mpmath.binomial(deg + alpha, deg - k)
            mono_coeff = ((-1) ** k) * binom / mpmath.factorial(k)
            g_mono[k] += c_j * mono_coeff

    # Build divisor: x * prod((x - zi)^2)
    div = [mpmath.mpf(0), mpmath.mpf(1)]  # x
    for zi in zs:
        factor = [-mpmath.mpf(zi), mpmath.mpf(1)]  # (x - zi)
        sq = _poly_mul_mp(factor, factor)
        div = _poly_mul_mp(div, sq)

    # Polynomial division (highest-degree-first)
    g_rev = list(reversed(g_mono))
    d_rev = list(reversed(div))
    g_deg = max_deg
    d_deg = len(div) - 1
    q_deg = g_deg - d_deg

    if q_deg < 0 or abs(d_rev[0]) < mpmath.mpf(10) ** (-dps + 10):
        return np.inf

    quot = [mpmath.mpf(0)] * (q_deg + 1)
    remainder = list(g_rev)
    for i in range(q_deg + 1):
        quot[i] = remainder[i] / d_rev[0]
        for j in range(len(d_rev)):
            remainder[i + j] -= quot[i] * d_rev[j]

    # Convert to float and find roots via companion matrix
    quot_float = np.array([float(q) for q in quot])
    try:
        all_roots = np.roots(quot_float)
    except Exception:
        return np.inf

    # Filter for real positive sign changes
    eps = 1e-6
    largest_sign_change = 0.0
    for r in all_roots:
        if abs(r.imag) > 1e-6 or r.real <= 0:
            continue
        rv = r.real
        left = np.polyval(quot_float, rv - eps)
        right = np.polyval(quot_float, rv + eps)
        if np.isfinite(left) and np.isfinite(right) and np.sign(left) != np.sign(right):
            largest_sign_change = max(largest_sign_change, rv)

    if largest_sign_change == 0:
        return np.inf

    return float(largest_sign_change) / (2 * np.pi)
