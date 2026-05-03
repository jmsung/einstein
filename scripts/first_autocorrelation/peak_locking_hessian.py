"""Verify the peak-locking Hessian fingerprint at small n across a parameterization sweep.

For the smooth-max P2 objective C_β(f) at a v-critical point under each parameterization
f = φ(v), the Hessian decomposes as

    H_v = J_φ(v)ᵀ · H_f · J_φ(v) + diag( φ''(v) ⊙ ∇_f C_β )

The first term is rank-deficient on the dead-cell subspace whenever φ'(0) = 0. The second
term is the load-bearing factor: it vanishes when φ''(0) = 0 (exp, v^p for p ≥ 3) and
gives a finite eigenvalue 2·∂C_β/∂f_i when φ''(0) = 2 (v² only).

Empirical sweep at n=80, β=200, sparse SOTA-like seed:

  param          C_crit         dead  near0_eigs  cond #
  exp(v)         1.9539951034   32    32          1.03e5
  v²             1.7817122319   32     0          4.55e4
  v³             1.8107106179   32    32          6.68e4
  v⁴             1.8310046542   32    32          2.40e4
  v⁶             1.8846429515   32    32          4.54e4
  U*sigmoid(v)   2.0994322618   36    52          9.98e6

v² is the only escape. v^p for p ≥ 3 peak-locks like exp despite being polynomial.
**U*sigmoid(v) is *more* rank-deficient than exp** — it has TWO boundary saturations
(σ→0 at v→-∞ and σ→1 at v→+∞), each contributing rank deficiency, so the optimizer
can't even reach exp's basin. Basin C tracks the vanishing order of φ at boundaries.

The sigmoid result rules out a tempting cross-problem hypothesis: P13's documented
sigmoid-based escape (lesson #68) is NOT the parameterization-rank-deficiency mechanism.
That escape works for a different reason — replacing hard L-BFGS-B box walls with
smooth interior gradients, which is structurally distinct.

Sufficient condition (sharpened): parameterization-induced basin escape requires (a)
the optimum's boundary indices map to FINITE v-coordinates (not v=±∞), AND (b) at
those finite coordinates, φ'(v) = 0 with φ''(v) ≠ 0. v² satisfies both at v=0;
exp, v^p (p≥3), and sigmoid all fail one or both conditions.

Reproduces the verification cited in
  wiki/findings/p2-peak-locking-hessian-mechanism.md.
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

    C_exp = lambda v: C_beta(np.exp(v), beta, dx)
    def make_C_vp(p):
        return lambda v: C_beta(np.abs(v) ** p, beta, dx)
    # Sigmoid: f = U * σ(v); reaches f=0 at v→-∞ and f=U at v→+∞ (both finite-image boundaries
    # where σ' and σ'' BOTH vanish — same structural family as exp at the f=0 boundary).
    U = 5.0  # generous upper bound, doesn't bind on this seed's f
    def C_sig(v): return C_beta(U / (1.0 + np.exp(-v)), beta, dx)
    clamped = np.clip(f_true, 1e-300, U - 1e-12)
    v0_sig = np.log(clamped / (U - clamped))

    cases = [
        ("exp(v)",       "-", C_exp,        np.log(np.maximum(f_true, 1e-300))),
        ("v**2",         "2", make_C_vp(2), np.abs(f_true) ** (1.0 / 2)),
        ("v**3",         "3", make_C_vp(3), np.abs(f_true) ** (1.0 / 3)),
        ("v**4",         "4", make_C_vp(4), np.abs(f_true) ** (1.0 / 4)),
        ("v**6",         "6", make_C_vp(6), np.abs(f_true) ** (1.0 / 6)),
        ("U*sigmoid(v)", "s", C_sig,        v0_sig),
    ]

    print(f"{'param':>10} {'p':>4} {'C_crit':>14} {'dead':>6} {'near0eig':>10} {'smallest>0':>12} {'largest':>12} {'cond':>10}")
    print("-" * 90)

    for label, pstr, fn, v0 in cases:
        r = minimize(fn, v0, method="L-BFGS-B", options=dict(maxiter=500, ftol=1e-14, gtol=1e-12))
        H = numerical_hessian(fn, r.x)
        eigs = np.sort(np.linalg.eigvalsh(H))

        if label == "exp(v)":
            f_at = np.exp(r.x)
        elif label == "U*sigmoid(v)":
            f_at = U / (1.0 + np.exp(-r.x))
        else:
            p_int = int(pstr)
            f_at = np.abs(r.x) ** p_int

        dead = int(np.sum(f_at < 1e-8 * f_at.max()))
        near0 = int(np.sum(np.abs(eigs) < 1e-6))
        pos = eigs[eigs > 1e-12]
        smallest = pos.min() if len(pos) else float("nan")
        largest = eigs[-1]
        cond = largest / smallest if smallest > 0 else float("inf")
        print(f"{label:>10} {pstr:>4} {r.fun:>14.10f} {dead:>6} {near0:>10} {smallest:>12.4e} {largest:>12.4e} {cond:>10.2e}")


if __name__ == "__main__":
    main()
