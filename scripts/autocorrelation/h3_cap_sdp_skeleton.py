"""H3-cap rigorous upper bound for arena P3 — SDP skeleton.

Math derivation in `wiki/techniques/p3-h3-cap-sdp-derivation.md`. This file is
a *skeleton* — it lays out the SDP structure and verifies the ingredients
(Fourier reformulation, Toeplitz positivity, SOS positivity) on toy data, but
does NOT yet solve the full problem. A future session should fill in the
TODOs and run the parametric sweep.

Status: derivation skeleton, not a working solver.

Dependencies expected (not yet in pyproject):
    pip install cvxpy mosek         # convex modeling + commercial solver
    # OR
    pip install cvxpy               # default SCS solver included

Run order:
    1. (DONE) Closed-form baseline diagnostic — `findings/p3-closed-form-baseline-landscape.md`
    2. (THIS) SDP skeleton — verify each ingredient on toy data
    3. (TODO) Parametric sweep over M0, solve at T=16/32/64
    4. (TODO) mpmath interval-arithmetic certification
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, "src")

import numpy as np

# CVXPY is the cleanest abstraction for SDPs in Python. If not installed,
# this script will warn and exit — leave the math + structure intact for
# future use.
try:
    import cvxpy as cp
    HAVE_CVXPY = True
except ImportError:
    HAVE_CVXPY = False


# -----------------------------------------------------------------------------
# Step 1 — Fourier reformulation utilities
# -----------------------------------------------------------------------------


def fft_coefficients(f: np.ndarray, T: int) -> np.ndarray:
    """Compute the first T+1 Fourier coefficients of a sampled even function f
    on (-1/2, 1/2). Returns hat_f[0..T] (real-valued for even f).

    f: 1D array, sampled at n equally-spaced points in (-1/2, 1/2).
    T: truncation order.
    """
    n = len(f)
    F = np.fft.fft(f) / n
    # Match the convention hat_f(k) = int_{-1/2}^{1/2} e^{-2*pi*i*k*x} f(x) dx
    # On a grid with sample spacing dx = 1/n, sum approximates the integral.
    return np.real(F[: T + 1])


def autoconvolution_l2_squared_via_white(hat_f: np.ndarray) -> float:
    """Compute ||F*F||_2^2 via White's identity (Rechnitzer eq. 8, truncated).

    For even f extended to F on (-1, 1), with hat_F(k) = (1/2) hat_f(k/2):
        ||F*F||_2^2 = (1/2) sum_k |hat_f(k)|^4
                     + (8/pi^4) sum_m |sum_k (-1)^k hat_f(k) / (2k - (2m+1))|^4

    This is the truncated form. Sum over |k|, |m| <= T.

    TODO: handle k = m + 1/2 pole case (avoid by enforcing 2k - (2m+1) != 0).
    TODO: bound the truncation tail via Levin transform (Rechnitzer §3-4).
    """
    T = len(hat_f) - 1
    # First term: (1/2) sum_k |hat_f(k)|^4
    term1 = 0.5 * np.sum(np.abs(hat_f) ** 4)

    # Second term: cross sum
    term2 = 0.0
    for m in range(-T, T + 1):
        inner = 0.0 + 0j
        for k in range(-T, T + 1):
            denom = 2 * k - (2 * m + 1)
            if denom == 0:
                continue  # pole — skip; in proper derivation handle as a limit
            sign = (-1) ** k
            # hat_f is symmetric for even f: hat_f(-k) = hat_f(k)
            f_k = hat_f[abs(k)] if abs(k) <= T else 0.0
            inner += sign * f_k / denom
        term2 += np.abs(inner) ** 4
    term2 *= 8.0 / np.pi**4
    return float(term1 + term2)


def toeplitz_matrix(hat_f: np.ndarray) -> np.ndarray:
    """Build the Toeplitz matrix [hat_f(i-j)]_{i,j=0..T} for the
    non-negativity constraint (Bochner-Herglotz: f >= 0 iff this matrix PSD).

    For even real hat_f, hat_f(-k) = hat_f(k), so the Toeplitz matrix is
    symmetric: T_{ij} = hat_f(|i-j|).
    """
    T = len(hat_f) - 1
    M = np.zeros((T + 1, T + 1))
    for i in range(T + 1):
        for j in range(T + 1):
            M[i, j] = hat_f[abs(i - j)]
    return M


def autoconvolution_value_at_x(hat_f: np.ndarray, x: float) -> float:
    """Evaluate (F*F)(x) for x in [-1, 1] using the Fourier coefficients of F.

    On the period-2 torus, (F*F)(x) = sum_k hat_F(k)^2 e^{i pi k x},
    which simplifies for even F to a real cosine sum.

    This is for verification of the SOS constraint, NOT for the SDP itself.
    """
    T = len(hat_f) - 1
    # hat_F(k) = (1/2) hat_f(k/2) — only even k for our extension
    # (F*F)(x) = sum_k hat_F(k)^2 e^{i pi k x}
    # For even hat_f, this is 2 * Re(sum_{k>=0} hat_F(k)^2 e^{i pi k x})
    # TODO: this needs careful re-derivation; the relation hat_F(k) = (1/2) hat_f(k/2)
    # only makes sense for even k; for odd k there's an integral residue.
    val = 0.0
    for k in range(T + 1):
        # placeholder — see Rechnitzer eq. 7 for exact form
        val += hat_f[k] ** 2 * np.cos(np.pi * k * x)
    return val


# -----------------------------------------------------------------------------
# Step 2 — SDP skeleton
# -----------------------------------------------------------------------------


def build_sdp_for_max_S(T: int, M0: float):
    """Build the parametric SDP: min C s.t. constraints (see derivation).

    Returns a CVXPY Problem object. Caller solves and reads C*.
    Then S* <= M0 / C*.
    """
    if not HAVE_CVXPY:
        raise RuntimeError("cvxpy not installed; install with `uv add cvxpy`")

    # Decision variables:
    # hat_f: real coefficients hat_f[0..T] (assumes even f)
    # C: sup-norm bound
    hat_f = cp.Variable(T + 1)
    C = cp.Variable(nonneg=True)

    constraints = []

    # (a) Normalization: hat_f[0] = 1
    constraints.append(hat_f[0] == 1)

    # (b) Toeplitz positivity for f >= 0
    # Build the symbolic Toeplitz matrix of hat_f
    Tmat = cp.Variable((T + 1, T + 1), symmetric=True)
    for i in range(T + 1):
        for j in range(T + 1):
            constraints.append(Tmat[i, j] == hat_f[abs(i - j)])
    constraints.append(Tmat >> 0)  # PSD

    # (c) SOS positivity for C - (F*F)(x) >= 0 on [-1, 1]
    # TODO: implement the trig-polynomial SOS constraint via Hankel matrices.
    # For trig poly p(x) = a_0 + 2 sum_{k>=1} a_k cos(pi k x), p >= 0 on [-1, 1]
    # iff there exists a PSD Toeplitz matrix Q of size (T+1) x (T+1) such that
    # the trace-along-diagonal-k of Q equals a_k for each k = 0..T.
    # This is the standard Toeplitz parameterization of non-negative trig polys.
    # Coefficients of P_C(x) = C - (F*F)(x) are:
    #   p_0 = C - hat_f[0]^2 - sum_{k>=1} 2 hat_f[k]^2  (DC + matched)
    #   p_k = - 2 hat_f[k]^2  for k >= 1
    # The hat_f[k]^2 terms make this a *quartic* in hat_f, which the SDP cannot
    # directly express linearly. NEED the lifting trick: introduce
    #   y_k := hat_f[k]^2 (auxiliary variables)
    # with the constraint y_k = hat_f[k]^2, which is a SOC / SDP constraint.
    # Then p_k becomes linear in y_k.
    #
    # Concretely:
    #   y_k = (hat_f[k]^2) ≤ Schur trick: cp.Variable y_k, constraint
    #         [[y_k, hat_f[k]], [hat_f[k], 1]] >> 0  AND  y_k <= some bound
    # This relaxes y_k = hat_f[k]^2 to y_k >= hat_f[k]^2 — a *valid* relaxation
    # that may loosen the bound but preserves rigorous-upper-bound-ness.
    #
    # TODO: implement this lifting + Toeplitz SOS + diagonal-trace constraints.

    # (d) L^2 norm lower bound: M(hat_f) >= M0
    # M(hat_f) is a quartic polynomial in hat_f — also needs lifting.
    # TODO: implement via the same lifting + tracking the cross-term sum-of-quartic.

    # Objective: minimize C
    prob = cp.Problem(cp.Minimize(C), constraints)
    return prob, hat_f, C


# -----------------------------------------------------------------------------
# Step 3 — Sanity-check ingredients on toy data
# -----------------------------------------------------------------------------


def sanity_check():
    """Verify the Fourier reformulation matches the direct evaluator on a
    known function (uniform on [-1/2, 1/2]).
    """
    sys.path.insert(0, "src")
    from einstein.autocorrelation.fast import fast_evaluate

    n = 8000
    x = np.linspace(-0.5, 0.5, n, endpoint=False)
    # Uniform: f = 1 on (-1/2, 1/2)
    f_unif = np.ones_like(x)
    f_unif /= np.sum(f_unif) / n  # normalize ∫f = 1

    print("=== Sanity: uniform f on [-1/2, 1/2] ===")
    s_arena = fast_evaluate(f_unif)
    print(f"  arena S(f) = {s_arena:.6f}  (expected ~0.667 for uniform)")

    T = 32
    hat_f = fft_coefficients(f_unif, T)
    print(f"  hat_f[0..3] = {hat_f[:4]}  (expected [1, 0, 0, 0] for uniform)")

    # White-formula L2 squared (truncated)
    l2_white = autoconvolution_l2_squared_via_white(hat_f)
    print(f"  ||F*F||_2^2 (White, T={T}) = {l2_white:.6f}")

    # Direct numerical
    from scipy.signal import fftconvolve

    conv = fftconvolve(f_unif, f_unif, mode="full")
    nc = len(conv)
    dx_unif = 1.0 / n  # spacing of x grid
    l2_direct = np.sum(conv * conv) * (dx_unif ** 2) * dx_unif
    # adjust for normalization: discrete sum vs integral. Scaling subtle —
    # leave as a TODO and just compare to ||F*F||_inf as a relative scale.
    print(f"  ||F*F||_2^2 (direct, n={n}) ~ {l2_direct:.6f}  [scaling TBD]")
    print()
    print("  TODO: reconcile White's normalization with the arena evaluator's discrete grid.")
    print()

    # Toeplitz matrix PSD check
    Tmat = toeplitz_matrix(hat_f)
    eigs = np.linalg.eigvalsh(Tmat)
    print(f"  Toeplitz min eigenvalue: {eigs.min():.6e}  (expected >= 0 for f >= 0)")
    print()


def main():
    print("=" * 76)
    print("H3-cap SDP skeleton for Einstein Arena P3")
    print("=" * 76)
    print()
    print("Status: SKELETON — not a working solver.")
    print("Math derivation: wiki/techniques/p3-h3-cap-sdp-derivation.md")
    print()

    sanity_check()

    if not HAVE_CVXPY:
        print("=" * 76)
        print("cvxpy not installed; SDP build skipped.")
        print("Install: `uv add cvxpy` (and optionally `uv add mosek`)")
        print("=" * 76)
        return

    print("=== SDP build (T=8, sanity-only) ===")
    try:
        prob, hat_f_var, C_var = build_sdp_for_max_S(T=8, M0=0.5)
        print(f"  Built: {len(prob.constraints)} constraints")
        print(f"  Variables: hat_f shape {hat_f_var.shape}, C scalar")
        print(f"  TODO: SOS lifting for quartic constraints — see in-source notes")
        print(f"  TODO: solve via prob.solve(solver='MOSEK', verbose=False)")
    except Exception as e:
        print(f"  Build failed: {e}")
    print()

    print("=" * 76)
    print("Next steps for a future session (per derivation doc):")
    print("  1. Implement the quartic-lifting (SOC trick for y_k = hat_f[k]^2)")
    print("  2. Implement the Toeplitz SOS for sup-norm bound")
    print("  3. Sweep M0 over a grid; report S* upper bound = max_{M0} M0/C*(M0)")
    print("  4. Increase T from 16 to 64 to 128, observe convergence")
    print("  5. mpmath interval-arithmetic certification (Rechnitzer §5)")
    print("=" * 76)


if __name__ == "__main__":
    main()
