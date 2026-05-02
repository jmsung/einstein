---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P3]
related_techniques: [dinkelbach-fractional-programming.md]
related_findings: [optimizer-recipes.md]
cites:
  - ../findings/optimizer-recipes.md
  - ../source/papers/2025-jaech-autoconvolution.md
---

# Fractional Programming (Dinkelbach Transform)

## TL;DR

A ratio objective `C(f) = N(f) / D(f)` (often non-convex jointly) can be replaced by a parametric sequence of subtractive subproblems `max_f [N(f) − λ D(f)]`, with `λ` updated as `λ ← N(f*) / D(f*)` until fixed point. This is the **Dinkelbach transform**. The trick is that the parametric subproblem is often standard (concave-maximization, convex-minimization) even when the ratio is not. Foundational for autocorrelation P3.

This concept page is the **mathematical principle**; the [technique](../techniques/dinkelbach-fractional-programming.md) is the procedure with code.

## What it is

Setup: variable `f` in some space `F`, numerator `N: F → ℝ`, denominator `D: F → ℝ_{>0}` (positive on feasible set). The fractional program is

```
maximize  C(f) = N(f) / D(f)   subject to f ∈ F.
```

**Dinkelbach's theorem (1967)**: define `F(λ) = max_f [N(f) − λ D(f)]`. Then `F` is convex non-increasing in `λ`; `F(λ*) = 0` iff `λ* = max_f C(f)`. The iteration

```
λ_0  ← N(f_0) / D(f_0)            for some warm-start f_0
f_t  ← argmax [N(f) − λ_t D(f)]   (the subtractive subproblem)
λ_{t+1} ← N(f_t) / D(f_t)
```

converges superlinearly to `λ*` under standard regularity (continuity + boundedness).

The key structural property: even when `N/D` is non-convex / non-concave, the subtractive subproblem `N(f) − λ D(f)` is often well-behaved because:

- Linear combinations of convex/concave functions inherit the property.
- Adding a `−λ D` term to `N` does not introduce new non-convexity if `D` is convex (the extremum becomes a saddle of opposite character).

For autocorrelation problems, `N` and `D` are *quasiconcave* in `f` even when not concave; Dinkelbach exploits the **quasiconcavity** to convert the ratio into a sequence of well-posed problems.

## When it applies

- Objective is a ratio `N(f) / D(f)` with `D > 0` on the feasible set.
- `N − λ D` is a tractable optimization (convex / smooth / has good optimizers) for fixed `λ`.
- A smooth surrogate exists for any L-infinity factor inside `N` or `D` (LSE for `‖·‖_∞`).
- Variable count is large (`n ≥ 1000`); cutting-plane LP / Frank-Wolfe is infeasible.

Recognition pattern: any objective written as a *ratio of integrals/sums* — autocorrelation `‖f ⋆ f‖₂² / (‖f ⋆ f‖₁ · ‖f ⋆ f‖_∞)` (P3); or generalized Rayleigh quotients `(xᵀ A x) / (xᵀ B x)`; or efficiency / cost-effectiveness ratios.

## Why it works

Two reasons:

1. **Convexity preservation**. `N(f) − λ D(f)` for fixed `λ` inherits convexity-on-each-factor structure. If `N` is concave and `D` is convex (or affine), the subproblem is concave maximization. The ratio `N/D` is *quasiconcave* but not concave; Dinkelbach unfreezes the optimization by removing the ratio.
2. **Superlinear convergence**. `λ_t → λ*` quadratically near the optimum (standard analysis: the iteration is Newton's method on `F(λ) = 0`). For autocorrelation problems, ~10–20 outer iterations achieve `|λ_{t+1} − λ_t| < 1e-12` from a warm-start. Cost is dominated by inner subproblem.

The companion machinery for L∞-ratios:

- **β-cascade**: replace `‖·‖_∞` with `LSE_β = (1/β) log Σ exp(β · |·|)`. Start `β = 1e4` for broad descent, anneal to `β = 1e10` for precision. Avoid jumping to high β (commits to nearest local optimum).
- **Parameterization choice**: `f = v²` vs `f = exp(v)`. `exp(v)` peak-locks on autocorrelation problems; `v²` allows exact zeros and breaks the lock (P2 lesson #93). See [parameterization-selection](parameterization-selection.md).

## Classic examples

1. **P3 Second Autocorrelation** — `C = ‖f ⋆ f‖₂² / (‖f ⋆ f‖₁ · ‖f ⋆ f‖_∞)`. JSAgent rank #1 (`0.962214`, delta `1.5e-4` from ClaudeExplorer SOTA) via Dinkelbach cascade on average-pooled high-resolution source. ~10 outer iters × 5 β-stages × L-BFGS = ~6 min CPU per warm start. See [findings/optimizer-recipes.md](../findings/optimizer-recipes.md) "Dinkelbach Fractional Programming" section.
2. **Generalized Rayleigh quotient** (classical): `max (xᵀA x)/(xᵀB x)` is the first generalized eigenvalue. Dinkelbach iteration recovers the standard `Ax = λBx` eigenproblem.
3. **Jaech & Joseph 2025 autoconvolution paper** — `source/papers/2025-jaech-autoconvolution.md` — uses Dinkelbach-style λ-iteration for an autocorrelation ratio.

## Related

- Concepts: [autocorrelation-inequality](autocorrelation-inequality.md), [smooth-max-approximation](smooth-max-approximation.md), [parameterization-selection](parameterization-selection.md).
- Techniques: [dinkelbach-fractional-programming](../techniques/dinkelbach-fractional-programming.md) (the procedure with code).
- Findings: [optimizer-recipes](../findings/optimizer-recipes.md).
- Sources: `source/papers/2025-jaech-autoconvolution.md`. Dinkelbach 1967 "On nonlinear fractional programming" — foundational, not yet ingested.
