import sys
if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)
import numpy as np
import sympy


def evaluate(solution: dict) -> float:
    zs = solution["laguerre_double_roots"]
    if len(zs) == 0:
        raise ValueError("laguerre_double_roots must be non-empty.")
    if len(zs) > 50:
        raise ValueError("At most 50 roots allowed.")
    if any(z <= 0 for z in zs):
        raise ValueError("All roots must be positive.")
    if any(z > 300 for z in zs):
        raise ValueError("All roots must be <= 300.")

    g_fn = _find_laguerre_combination(zs)
    x = sympy.symbols("x")

    div = sympy.prod([(x - sympy.Rational(z)) ** 2 for z in zs]) * x
    gq_fn = sympy.exquo(g_fn, div)

    real_roots = sympy.real_roots(gq_fn, x)
    if not real_roots:
        raise ValueError("g has no sign changes.")

    gq_np = sympy.lambdify(x, gq_fn, modules="numpy")
    largest_sign_change = 0.0
    for root in real_roots:
        r_val = float(root.evalf(30))
        eps = 1e-6
        if np.sign(gq_np(r_val - eps)) != np.sign(gq_np(r_val + eps)):
            largest_sign_change = max(largest_sign_change, r_val)

    if largest_sign_change == 0:
        raise ValueError("No sign-changing roots found.")

    return float(largest_sign_change) / (2 * np.pi)


def _find_laguerre_combination(zs):
    m = len(zs)
    alpha = sympy.Rational(1, 2) - 1
    x = sympy.symbols("x")
    degrees = np.arange(0, 4 * m + 4, 2)
    lps = [
        sympy.polys.orthopolys.laguerre_poly(n=int(i), x=x, alpha=alpha, polys=False)
        for i in degrees
    ]
    num_lps = len(lps)
    num_conditions = 2 * m + 2

    mat = sympy.Matrix(num_conditions, num_lps, lambda i, j: 0)
    b = sympy.Matrix(num_conditions, 1, lambda i, j: 0)
    b[1] = 1

    for j in range(num_lps):
        mat[0, j] = lps[j].subs(x, 0)
        mat[1, j] = lps[j].diff(x).subs(x, 0)

    for i in range(m):
        zi = sympy.Rational(zs[i])
        for j in range(num_lps):
            mat[2 * i + 2, j] = lps[j].subs(x, zi)
            mat[2 * i + 3, j] = lps[j].diff(x).subs(x, zi)

    coeffs = mat.LUsolve(b)
    return sum(coeffs[i] * lps[i] for i in range(num_lps))


if __name__ == "__main__":
    # Together-AI's best k=13 roots (score 0.3188545891623888)
    best_roots = [
        3.1427440085666496,
        4.469993893132148,
        6.078689469782297,
        32.637646271046336,
        38.265477818082566,
        41.06153063739393,
        43.09262298321874,
        50.81816373872074,
        58.61770809389174,
        96.07661117430976,
        111.48735817427675,
        118.74229251036576,
        141.09580664199572,
    ]
    print(f"Testing k={len(best_roots)} roots...")
    score = evaluate({"laguerre_double_roots": best_roots})
    print(f"Score: {score}")
