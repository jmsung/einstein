---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P2, P3, P9, P13]
related_techniques: [gap-space-parameterization.md, bounded-lbfgs-per-region-sigmoid.md, dinkelbach-fractional-programming.md, larger-n-cascade.md]
related_findings: [optimizer-recipes.md, equioscillation-escape.md, k-climbing.md]
cites:
  - ../findings/optimizer-recipes.md
  - ../findings/equioscillation-escape.md
---

# Parameterization Selection

## TL;DR

The choice of parameterization `f = φ(v)` defines the optimization landscape — its critical points, gradient geometry, and basin walls — at least as much as the choice of optimizer does. Before scaling compute, test ≥ 2 structurally different parameterizations of the same objective. Breakthroughs are often free; intensity escalation is not.

## What it is

For a given objective `C(f)` over a function/configuration space `F`, a parameterization is a map `φ: ℝᵈ → F` with optimization performed over `v ∈ ℝᵈ` instead of `f ∈ F`. Different `φ` give the same global optimum but different:

- **Critical-point sets**. Local minima of `C(φ(v))` in `v` need not project to local minima of `C(f)`.
- **Gradient geometry**. `∇_v (C ∘ φ) = J_φ(v)ᵀ ∇_f C(φ(v))` rescales coordinates by the Jacobian of `φ`.
- **Implicit constraints**. Range of `φ` can encode positivity, ordering, support membership, region containment.

Common families:

| Family | Form | Effect |
|---|---|---|
| Exponential | `f = exp(v)` | strict positivity; non-vanishing gradient; peak-locks |
| Square | `f = v²` | non-negativity with exact zeros allowed; `df/dv = 2v` vanishes at zero |
| Per-region sigmoid | `f_i = lo_i + (hi_i − lo_i)·σ(v_i)` | enforces per-element box without breaking gradients at the boundary |
| Gap-space | `g_i = z_{i+1} − z_i > 0` | enforces ordering, decorrelates positions |
| Fourier basis | `f(x) = Σ a_k φ_k(x)` | spectrum-natural variables for harmonic problems |

## When it applies

Whenever the optimizer stalls at a level above the suspected basin floor, and especially when:

- Multiple optimizers (L-BFGS, Adam, CMA-ES) all stall at the same value (universal peak-locking — the basin is parameterization-induced, not optimizer-induced).
- The objective has implicit constraints (positivity, ordering, region membership) that the current parameterization either ignores or enforces with hard bounds.
- The current parameterization has non-vanishing gradients at constraint surfaces the true optimum lies on (e.g. `exp(v)` cannot reach an exact zero).

## Why it works

Two mechanisms:

1. **Gradient alignment with the true optimum's constraint set.** If the true optimum has `f_i = 0` for some `i`, `f = exp(v)` requires `v → −∞` (asymptote, never reached); `f = v²` reaches zero at `v = 0` with `df/dv → 0` — this is a stationary point of the parameterized problem precisely where the true problem wants sparsity.
2. **Implicit ordering / boundary handling.** Hard bounds (`scipy L-BFGS-B`) zero gradients at the boundary, locking the optimizer there. A sigmoid `σ(v)` keeps `dσ/dv = σ(1−σ) > 0` everywhere inside the box, so L-BFGS can take long unconstrained steps in `v` while the image stays feasible.

The formal statement: for a smooth `φ` with full-rank Jacobian, critical points of `C ∘ φ` correspond to critical points of `C` only on the relative interior of the image; at boundary critical points of the image, the parameterization changes whether the gradient *sees* the boundary. This is why `v²` exposes a zero-support stationary point that `exp(v)` cannot.

## Classic examples

1. **P2 First Autocorrelation** — `exp(v)` peak-locked universally at delta ≈ 5.25e-8 from SOTA across all `n ∈ [30k, 300k]` and all optimizers. Switch to `f = v²` at `n = 90 000` immediately broke through to delta = 1.23e-6 (rank #1). Three mechanisms identified: exact zeros allowed, vanishing gradient at zero encourages sparsity, different Hessian curvature routes L-BFGS to a different stationary point. See [findings/optimizer-recipes.md](../findings/optimizer-recipes.md) lesson #93.
2. **P9 Uncertainty Principle** — root positions are an ordered tuple. Position-space Nelder-Mead converges to the wrong stationary point at `k = 14`; gap-space NM (`g_i = z_{i+1} − z_i`) reaches `S = 0.31817` and breaks the `k = 13` plateau. See [findings/k-climbing.md](../findings/k-climbing.md) lesson #24, technique [gap-space-parameterization.md](../techniques/gap-space-parameterization.md).
3. **P13 Edges vs Triangles** — sample points must each lie inside their assigned scallop `[1 − 1/k, 1 − 1/(k+1)]`. `scipy L-BFGS-B` with hard bounds either crosses boundaries or stalls; per-element sigmoid in raw-space + L-BFGS on `v` unlocks +1.4e-7. See [findings/optimizer-recipes.md](../findings/optimizer-recipes.md) lesson #68.

## Related

- Concepts: [smooth-max-approximation](smooth-max-approximation.md), [discretization-as-structure](discretization-as-structure.md), [symmetry-and-fundamental-domain](symmetry-and-fundamental-domain.md).
- Techniques: [gap-space-parameterization](../techniques/gap-space-parameterization.md), [bounded-lbfgs-per-region-sigmoid](../techniques/bounded-lbfgs-per-region-sigmoid.md), [dinkelbach-fractional-programming](../techniques/dinkelbach-fractional-programming.md), [larger-n-cascade](../techniques/larger-n-cascade.md).
- Findings: [optimizer-recipes](../findings/optimizer-recipes.md) (#93, #67, #68), [equioscillation-escape](../findings/equioscillation-escape.md) (#94), [k-climbing](../findings/k-climbing.md) (#26).
