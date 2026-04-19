"""Arbitrary-precision evaluator for the Uncertainty Principle problem.

Replaces numpy.roots (float64 limited to ~1e-8) with mpmath-based
sign change detection. Works for scores as small as 1e-100+.

Speed: same as poly_eval.py (~7s at k=50) since numpy.roots was <0.01s.
"""
import mpmath
import numpy as np

from einstein.uncertainty.poly_eval import (
    _laguerre_mp,
    _laguerre_deriv_mp,
    _poly_mul_mp,
)


def arbitrary_evaluate(zs, dps=100):
    """Evaluate score using fully mpmath-based approach.

    Returns S = largest_sign_change / (2*pi), or mpmath.inf on failure.
    Works for arbitrarily small scores (no float64 root-finding).
    """
    zs = list(zs)
    m = len(zs)
    if m == 0 or any(z <= 0 for z in zs) or any(z > 300 for z in zs):
        return float("inf")

    mpmath.mp.dps = dps
    alpha = mpmath.mpf(-1) / 2
    degrees = list(range(0, 4 * m + 4, 2))

    # Solve for Laguerre combination coefficients
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
        return float("inf")

    # Build g(x) monomial coefficients
    max_deg = max(degrees)
    g_mono = [mpmath.mpf(0)] * (max_deg + 1)
    for j, deg in enumerate(degrees):
        c_j = coeffs[j]
        for k in range(deg + 1):
            binom = mpmath.binomial(deg + alpha, deg - k)
            mono_coeff = ((-1) ** k) * binom / mpmath.factorial(k)
            g_mono[k] += c_j * mono_coeff

    # Build divisor and quotient polynomial
    div = [mpmath.mpf(0), mpmath.mpf(1)]
    for zi in zs:
        factor = [-mpmath.mpf(zi), mpmath.mpf(1)]
        sq = _poly_mul_mp(factor, factor)
        div = _poly_mul_mp(div, sq)

    g_rev = list(reversed(g_mono))
    d_rev = list(reversed(div))
    q_deg = max_deg - (len(div) - 1)
    if q_deg < 0:
        return float("inf")

    quot_hd = [mpmath.mpf(0)] * (q_deg + 1)  # highest-degree-first
    remainder = list(g_rev)
    for i in range(q_deg + 1):
        quot_hd[i] = remainder[i] / d_rev[0]
        for j in range(len(d_rev)):
            remainder[i + j] -= quot_hd[i] * d_rev[j]

    # q_low[i] = coefficient of x^i (lowest-degree-first)
    q_low = list(reversed(quot_hd))

    def q_eval(x):
        """Evaluate q(x) using Horner's method in mpmath."""
        x = mpmath.mpf(x)
        val = quot_hd[0]
        for c in quot_hd[1:]:
            val = val * x + c
        return val

    # Strategy: find ALL sign changes using two methods:
    # 1. Log-spaced grid scan for sign changes at x > 1e-30
    # 2. Newton's method from q(0), q'(0) for tiny roots near 0

    # Method 1: scan for far sign changes
    largest_sign_change = mpmath.mpf(0)

    # Check log-spaced points from 1e-30 to 1e5
    check_points = []
    x = mpmath.mpf("1e-30")
    while x < mpmath.mpf("1e5"):
        check_points.append(x)
        x *= mpmath.mpf("1.5")

    prev_sign = None
    prev_x = None
    for x in check_points:
        try:
            val = q_eval(x)
            if val == 0:
                continue
            curr_sign = mpmath.sign(val)
            if prev_sign is not None and curr_sign != prev_sign:
                # Sign change between prev_x and x — refine with bisection
                lo, hi = prev_x, x
                for _ in range(200):  # ~60 digits of precision
                    mid = (lo + hi) / 2
                    if q_eval(mid) * q_eval(lo) < 0:
                        hi = mid
                    else:
                        lo = mid
                root = (lo + hi) / 2
                if root > largest_sign_change:
                    largest_sign_change = root
            prev_sign = curr_sign
            prev_x = x
        except Exception:
            continue

    # Method 2: find smallest positive root near 0 using Newton/bisection
    # q(x) = q_low[0] + q_low[1]*x + q_low[2]*x^2 + ...
    # If q_low[0] and q_low[1] have opposite signs, there's a root near -q_low[0]/q_low[1]
    q0 = q_low[0]
    q1 = q_low[1] if len(q_low) > 1 else mpmath.mpf(0)
    if q0 != 0 and q1 != 0 and mpmath.sign(q0) != mpmath.sign(q1):
        # Root near x ≈ -q0/q1 (linear approximation)
        x_approx = -q0 / q1
        if x_approx > 0:
            # Refine with bisection
            lo = mpmath.mpf(0)
            hi = x_approx * 3  # generous bracket
            # Verify bracket contains sign change
            if q_eval(lo) * q_eval(hi) < 0:
                for _ in range(200):
                    mid = (lo + hi) / 2
                    if q_eval(mid) * q_eval(lo) < 0:
                        hi = mid
                    else:
                        lo = mid
                root = (lo + hi) / 2
                if root > largest_sign_change:
                    largest_sign_change = root

    if largest_sign_change == 0:
        return float("inf")

    return float(largest_sign_change / (2 * mpmath.pi))
