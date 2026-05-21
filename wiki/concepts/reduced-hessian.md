---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P5, P11, P14, P15, P16, P17a, P18]
related_techniques: [slsqp-active-pair-polish.md, mpmath-ulp-polish.md, basin-hopping-multistart.md]
related_findings: [basin-rigidity.md, float64-ceiling.md]
related_personas: [poincare.md, lagrange.md]
cites:
  - basin-rigidity.md
  - contact-graph-rigidity.md
  - provable-floor-and-frozen-problems.md
  - first-order-link-tangent-test.md
  - ../findings/basin-rigidity.md
---

# Reduced Hessian (projected Hessian of the Lagrangian)

## TL;DR

For a constrained optimum, the **reduced Hessian** is the Hessian of the Lagrangian projected onto the tangent space of the active constraints. **Positive-definite reduced Hessian = strict local minimum on the active manifold = basin is rigid**. Counting active constraints vs DOF is the cheap (constant-time) screen; the reduced-Hessian eigenvalue check is the second-order *certificate*. Together they prove rigidity in seconds and replace 10⁴–10⁵-trial multistart sweeps.

## What it is

For a constrained problem

```
minimize  f(x)
subject to  g_i(x) ≤ 0   (inequalities, active set I at x*)
            h_j(x) = 0   (equalities)
```

at a KKT point `x*` with multipliers `(μ, λ)`, the Lagrangian is

```
L(x, μ, λ) = f(x) + Σ μ_i g_i(x) + Σ λ_j h_j(x).
```

Let `A(x*)` be the matrix whose rows are the **active constraint gradients** (`∇g_i` for `i ∈ I`, plus all `∇h_j`). The **tangent space** of the active manifold is the null space of `A`:

```
T = ker(A) = { d ∈ ℝⁿ : A · d = 0 }.
```

Let `Z` be a basis for `T` (any matrix whose columns span `ker(A)`). The **reduced Hessian** is

```
H_red  =  Zᵀ · ∇²ₓ L(x*, μ, λ) · Z.
```

Second-order sufficient conditions (Nocedal & Wright §12.5):

| Reduced Hessian | Conclusion |
|---|---|
| Positive definite (all eigenvalues > 0) | `x*` is a **strict local minimum** on the active manifold |
| Positive semidefinite, with zero eigenvalue | Degenerate — second-order test inconclusive; need higher-order info |
| Indefinite | `x*` is a **saddle** on the active manifold; descent direction exists |
| Has zero eigenvalue | A **zero-cost direction** exists tangent to active set — basin is *not* rigid |

The wiki's rigidity machinery uses the positive-definite case as a certificate that no infinitesimal motion improves the score.

## How to compute it

Three practical paths, in order of robustness:

### 1. Null-space basis (most direct)

```python
import numpy as np
from scipy.linalg import null_space

# A: stack of active constraint gradients, shape (m, n)
# H: full Lagrangian Hessian, shape (n, n)
Z = null_space(A)              # shape (n, n - rank(A))
H_red = Z.T @ H @ Z
eigs = np.linalg.eigvalsh(H_red)
print(f"min eig: {eigs.min():.3e}")   # > 0 → rigid
```

`null_space` uses an SVD; columns of `Z` form an orthonormal basis for `ker(A)`. Numerically robust for moderate `n`.

### 2. QR-based projection (faster for large `n`)

```python
Q, R = np.linalg.qr(A.T, mode='complete')
Z = Q[:, A.shape[0]:]          # last (n - m) columns span ker(A)
H_red = Z.T @ H @ Z
```

Avoids the SVD; exploits the structure when constraint count `m ≪ n`.

### 3. mpmath at high dps (for sub-ulp problems)

For float64-ceiling problems (P11 Tammes, P15 Heilbronn, P5 distance-ratio), construct `A` and `H` in mpmath at 60–80 dps, then compute `eigvalsh` via `mpmath.mp.eigsy` after converting through SymPy. This catches "false positive eigenvalues at zero" that float64 reports as `1e-12` artifacts.

## Why it complements other rigidity tests

| Test | What it proves | Cost | When it fails |
|---|---|---|---|
| **Active-count vs DOF** (Maxwell) | Necessary condition only | Constant time | Coincidental tightness — `\|active\| ≥ DOF` but H_red has zero eigenvalue |
| **First-order LP** ([first-order-link-tangent-test](first-order-link-tangent-test.md)) | No first-order descent direction | One LP solve | Doesn't see second-order ascent (could still be a saddle) |
| **Reduced Hessian eigenvalues** | Strict local minimum (definite) or saddle (indefinite) | One eigendecomp | Degenerate (PSD with zero eigenvalue) requires higher-order or perturbation analysis |
| **mpmath KKT solve** ([basin-rigidity](basin-rigidity.md) lesson #88) | Solution is unique on active manifold | Newton at high dps | None — but it's existence/uniqueness, not local-min vs saddle |

The reduced Hessian is the **second-order certificate**: it upgrades "no first-order descent" to "no second-order descent in any active-tangent direction." That upgrade is what makes a rigidity claim survive scrutiny.

## When it applies in the arena

- **P5 Min-Distance-Ratio (n=16)** — (22, 8) Cantrell configuration. 30 active constraints on 28 DOF (32 coords − 4 affine gauges); reduced Hessian has all positive eigenvalues, so the basin is provably rigid. Stronger than the 44 018-trial multistart that returned no alternative. (See [`findings/basin-rigidity.md`](../findings/basin-rigidity.md) lesson #85.)
- **P15 Heilbronn (n=11)** — 17 active triples on 8 effective DOF after D₁ symmetry. Reduced Hessian is positive-definite at 60 dps; `δ_min = 0` from first-order LP plus the second-order certificate together classify it as a rigid local maximum.
- **P11 Tammes (n=50)** — 95+ active near-contact pairs on 3·50 − 3 = 147 DOF after rotation gauge. Numerically PSD with several zero eigenvalues at float64 precision; mpmath-80 confirms the zeros are *real degeneracies* (continuous symmetries within the active manifold), not artifacts. The basin is rigid up to the symmetry orbit.
- **P14, P16, P17a** — all use the active-count + reduced-Hessian pair to certify float64-ceiling configurations as basin-locked before declaring frozen.

## Pitfalls

- **Constraint qualification (LICQ)**. If active gradients are linearly dependent, `rank(A) < |I|`, and the multipliers may not be unique — the standard reduced-Hessian formulation still works (use `Z = null_space(A)`), but interpretation of the multipliers in `H = ∇²L` becomes subtle. Use Mangasarian–Fromovitz constraint qualification (MFCQ) as the weaker working assumption.
- **Symmetry gauges count as constraints**. Translation, rotation, scale, Möbius — each gauge eats one DOF. Counting these as if they were free degrees of freedom inflates "DOF" and makes a rigid system look slack. See [`symmetry-and-fundamental-domain`](symmetry-and-fundamental-domain.md).
- **Strict-vs-non-strict actives**. A strictly-satisfied constraint at the candidate (`g_i(x*) < 0`) is *not* in the active set; only equalities and tight inequalities go into `A`. The wiki's `slsqp-active-pair-polish` technique requires a tolerance-driven definition of "active" — typically `1e-3` for Tammes, `1e-7` for Heilbronn (per problem-specific calibration).
- **Float64 false positives near zero**. Reduced-Hessian eigenvalues in the `1e-12` to `1e-14` range are usually float64 noise, not real degeneracies. Always confirm with mpmath at 60+ dps before claiming "zero eigenvalue means continuous symmetry."

## Related

- **Concepts**: [basin-rigidity](basin-rigidity.md), [contact-graph-rigidity](contact-graph-rigidity.md), [first-order-link-tangent-test](first-order-link-tangent-test.md), [provable-floor-and-frozen-problems](provable-floor-and-frozen-problems.md), [symmetry-and-fundamental-domain](symmetry-and-fundamental-domain.md).
- **Techniques**: [slsqp-active-pair-polish](../techniques/slsqp-active-pair-polish.md), [mpmath-ulp-polish](../techniques/mpmath-ulp-polish.md).
- **Findings**: [basin-rigidity](../findings/basin-rigidity.md) (lessons #85, #88, #96).

## References

- Nocedal & Wright, *Numerical Optimization* (2006), §12.5 (Second-Order Conditions).
- Bertsekas, *Nonlinear Programming* (3rd ed. 2016), §3.3 (KKT and second-order sufficiency).

*Last updated: 2026-05-02*
