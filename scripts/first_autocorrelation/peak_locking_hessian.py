"""Verify the peak-locking Hessian fingerprint at small n.

For the smooth-max P2 objective C_β(f) at a v-critical point under each parameterization:

  exp(v):  the Hessian is rank-deficient with one near-zero eigenvalue per
           "dead" cell (f_i ≈ 0). The dead-cell subspace is a flat sub-manifold
           of v-space — the optimizer cannot decisively prune those cells.

  v²:      the Hessian has full rank even with dead cells; each dead cell
           contributes a finite eigenvalue 2·∂C_β/∂f_i because ∂²f/∂v² = 2.
           The optimizer reaches a strictly better basin.

Reproduces the small-n verification cited in
  wiki/findings/p2-peak-locking-hessian-mechanism.md.

Tracks the analytical derivation: for f = φ(v),

    H_v = J_φ(v)ᵀ · H_f · J_φ(v) + diag( φ''(v) ⊙ ∇_f C_β )

at any v-critical point. The first term is rank-deficient on the dead-cell
subspace under both parameterizations (J_φ kills those rows). The second term
vanishes under exp (φ'' = exp(v) = f → 0 at dead cells) but is +2 ∇_f C_β
under v² (φ'' = 2 constant). That second term is the entire mechanism.
"""

from __future__ import annotations

import numpy as np
from scipy.optimize import minimize


def autoconv(f: np.ndarray) -> np.ndarray:
    return np.convolve(f, f, mode="full")


def smooth_max(z: np.ndarray, beta: float) -> float:
    z_max = z.max()
    return z_max + (1.0 / beta) * np.log(np.exp(beta * (z - z_max)).sum())


def C_beta(f: np.ndarray, beta: float, dx: float) -> float:
    a = autoconv(f) * dx
    integral = f.sum() * dx
    return smooth_max(a, beta) / (integral * integral)


def numerical_hessian(fn, x: np.ndarray, eps: float = 1e-5) -> np.ndarray:
    n = len(x)
    H = np.zeros((n, n))
    for i in range(n):
        ei = np.zeros(n); ei[i] = eps
        for j in range(i, n):
            ej = np.zeros(n); ej[j] = eps
            H[i, j] = (fn(x + ei + ej) - fn(x + ei - ej) - fn(x - ei + ej) + fn(x - ei - ej)) / (4 * eps * eps)
            H[j, i] = H[i, j]
    return H


def main() -> None:
    n = 80
    dx = 0.5 / n
    beta = 200.0

    np.random.seed(0)
    f_true = np.zeros(n)
    f_true[0:8] = np.linspace(0.5, 0.6, 8)
    f_true[60:80] = np.linspace(0.4, 1.0, 20)
    f_true[20:40] = 0.05 * np.random.rand(20)
    f_true /= f_true.sum() * dx

    C_v_exp = lambda v: C_beta(np.exp(v), beta, dx)
    C_v_sq  = lambda v: C_beta(v * v, beta, dx)

    v0_exp = np.log(np.maximum(f_true, 1e-300))
    v0_sq  = np.sqrt(f_true)
    r_exp = minimize(C_v_exp, v0_exp, method="L-BFGS-B", options=dict(maxiter=500, ftol=1e-14, gtol=1e-12))
    r_sq  = minimize(C_v_sq,  v0_sq,  method="L-BFGS-B", options=dict(maxiter=500, ftol=1e-14, gtol=1e-12))

    print(f"C at exp(v) critical: {r_exp.fun:.10f}")
    print(f"C at v^2   critical: {r_sq.fun:.10f}")

    H_exp = numerical_hessian(C_v_exp, r_exp.x)
    H_sq  = numerical_hessian(C_v_sq,  r_sq.x)
    eigs_exp = np.sort(np.linalg.eigvalsh(H_exp))
    eigs_sq  = np.sort(np.linalg.eigvalsh(H_sq))

    f_at_exp = np.exp(r_exp.x)
    f_at_sq  = r_sq.x ** 2
    dead_exp = int(np.sum(f_at_exp < 1e-8 * f_at_exp.max()))
    dead_sq  = int(np.sum(f_at_sq  < 1e-8 * f_at_sq.max()))

    print(f"exp(v): dead cells = {dead_exp}/{n}; near-zero eigs (|λ|<1e-6) = {int(np.sum(np.abs(eigs_exp) < 1e-6))}/{n}")
    print(f"v^2  : dead cells = {dead_sq}/{n}; near-zero eigs (|λ|<1e-6) = {int(np.sum(np.abs(eigs_sq) < 1e-6))}/{n}")
    print(f"exp(v) cond # (positive eigs only) ≈ {eigs_exp[-1] / max(eigs_exp[eigs_exp > 1e-12].min(), 1e-30):.2e}")
    print(f"v^2   cond # (positive eigs only) ≈ {eigs_sq[-1]  / max(eigs_sq[eigs_sq  > 1e-12].min(), 1e-30):.2e}")


if __name__ == "__main__":
    main()
