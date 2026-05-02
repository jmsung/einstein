---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P1, P2, P3, P4]
related_techniques: [larger-n-cascade.md, dinkelbach-fractional-programming.md]
related_findings: [equioscillation-escape.md, optimizer-recipes.md, sa-parallel-tempering.md]
cites:
  - ../findings/equioscillation-escape.md
  - ../findings/sa-parallel-tempering.md
---

# Smooth-Max Approximation (Log-Sum-Exp / β-Cascade)

## TL;DR

Replace `max_i x_i` with `LSE_β(x) = (1/β) log Σ_i exp(β x_i)`. As `β → ∞`, `LSE_β → max`. This unlocks gradient-based optimization on minimax / max-norm problems but requires a **β-cascade**: start small (`β = 1e4`) for broad descent, anneal to large (`β = 1e10`) for precision. Jumping to large β commits to the nearest local maximum of the smooth surrogate; jumping too slowly leaves the surrogate unfaithful to the true max. Works on minimax with finite-DOF parameterization. **Fails as a hinge surrogate** (P6 — see warning).

## What it is

The **log-sum-exp** (LSE) function is the canonical smooth surrogate for `max`:

```
LSE_β(x_1, ..., x_n) = (1/β) log Σ_i exp(β x_i)     →     max_i x_i  as β → ∞.
```

Properties:

- **Convex**, smooth, increasing in each `x_i`.
- `max_i x_i ≤ LSE_β(x) ≤ max_i x_i + (log n) / β` (uniform bound).
- Gradient `∂LSE / ∂x_i = exp(β x_i) / Σ_j exp(β x_j)` is the softmax — concentrated on the argmax for large `β`.

For minimax `min_f max_t g(f, t)`, LSE replaces the inner max:

```
min_f LSE_β,t [g(f, t)] = min_f (1/β) log Σ_t exp(β g(f, t)).
```

Now smooth in `f`, gradient-based optimizers apply. The **β-cascade** is essential:

1. Start `β = 1e4`: broad-descent regime; the surrogate smooths over fine structure; L-BFGS / Adam find a *region* containing the true minimax.
2. Increase to `β = 1e6, 1e8, 1e10`: progressively tighter approximation. Each stage warm-starts from the previous optimum.
3. Stop when β saturates float64 (around `β = 1e12`–`1e14`, the gradient zeros out; further increases destroy precision).

## When it applies

- **Minimax / L∞ minimization** with finite-DOF parameterization (autocorrelation P1, P2, P3, P4).
- **Continuous Chebyshev approximation** where Remez is infeasible due to active-constraint count.
- Whenever you need a **gradient** for `max` and the underlying problem is smooth-friendly (smooth `f → g(f, t)`).

**Does NOT apply to hinge-overlap losses** (P6 lesson #25). Replacing `max(0, T − ‖c_i − c_j‖)` with `softplus(β(T − d))/β` *changes the optimum* at low β and *flattens gradients* at high β. No β simultaneously approximates the loss and maintains useful gradient. Stay on the true hinge for kissing-tight problems.

## Why it works

Two mechanisms:

1. **Smoothness creates gradients**. Hard `max` has discontinuous gradient at active-constraint switches; LSE is `C^∞`. L-BFGS, Adam, CMA-ES all need gradients (or smooth function evaluations); LSE provides them.
2. **β-anneal escapes saddle points**. A high-β surrogate has many flat regions (where one `x_i` dominates exponentially). Starting at low β explores broad geometry and finds the *region* containing the global minimax; raising β progressively pins the gradient to the active set. This is essentially homotopy continuation from a smooth approximation to the hard max.

The trap: **jumping to high β immediately** commits to whichever local minimum the smooth surrogate has near the warm-start. The first-stage broad descent at low β is what discovers a good basin; without it, the optimizer is locked into the nearest one.

The other trap: **low β changes the objective**. At `β = 100`, `LSE_β(0, 0.01, 0.99) ≈ 0.99 + log 3 / 100 ≈ 1.01`, very different from `max = 0.99`. The error `(log n)/β` must be << `minImprovement` before submitting; this requires β reaching `β >> log n / minImprovement`.

## Classic examples

1. **P4 Third Autocorrelation** — block-repeat upsample to `n = 1600` + 1e-6 noise + L-BFGS smooth-max with **β-cascade `1e4 → 1e10`** dropped score by 4.7e-4 on first jump. Cascading through `n ∈ {3 200, ..., 100 000}` totaled `1.52e-3` (15× `minImprovement`). See [findings/equioscillation-escape.md](../findings/equioscillation-escape.md) lesson #51.
2. **P2 First Autocorrelation** — Adam peak-flattening on the LSE-smoothed `‖f ⋆ f‖_∞` discovers sparse block structure without explicit prior. β-cascade `1e4 → 1e8` for L-BFGS in the Dinkelbach inner loop.
3. **P6 Kissing d=11 (counter-example)** — `softplus(β·hinge)/β` tested at β ∈ [100, 5000], all made score worse (0.35–1.5 vs 0.156 SOTA). Smooth surrogate is a trap on hinge-overlap. See [findings/sa-parallel-tempering.md](../findings/sa-parallel-tempering.md) lesson #25.

## Related

- Concepts: [autocorrelation-inequality](autocorrelation-inequality.md), [equioscillation](equioscillation.md), [parameterization-selection](parameterization-selection.md), [hinge-overlap](hinge-overlap.md).
- Techniques: [larger-n-cascade](../techniques/larger-n-cascade.md), [dinkelbach-fractional-programming](../techniques/dinkelbach-fractional-programming.md).
- Findings: [equioscillation-escape](../findings/equioscillation-escape.md), [optimizer-recipes](../findings/optimizer-recipes.md), [sa-parallel-tempering](../findings/sa-parallel-tempering.md) (#25 — smooth-loss trap).
