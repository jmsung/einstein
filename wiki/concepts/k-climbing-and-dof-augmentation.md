---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P9]
related_techniques: [k-climbing.md, gap-space-parameterization.md]
related_findings: [k-climbing.md]
cites:
  - ../findings/k-climbing.md
---

# k-Climbing and DOF Augmentation

## TL;DR

When stuck at a local minimum at fixed model dimension `k`, *adding* a degree of freedom (one more root, one more sample, one more cluster) can immediately drop the objective by an amount no fixed-`k` optimization could find. The `k = 13 → k = 14` jump on P9 dropped score by `1.8e-4` (above `minImprovement`) — the single largest "free" improvement in the JSAgent log. Climb until the gate-feasibility ratio `step_size / minImprovement < 0.1`, then pivot.

This concept page is the **mathematical principle**; the [technique](../techniques/k-climbing.md) is the procedure.

## What it is

For a parametric optimization `min_{f ∈ F_k} S(f)` with `F_k ⊂ F_{k+1} ⊂ ...` a chain of model spaces of increasing dimension:

- **Climb step**: solve `min_{f ∈ F_{k+1}} S(f)` warm-started from the optimum at `k`. The drop `Δ_k = S_k − S_{k+1}` measures the value of the extra DOF.
- **Plateau**: at fixed `k`, all optimizers converge to the same `S_k` — no rearrangement of `k` DOFs escapes the basin. The barrier is **dimensional**, not optimization quality.
- **Diminishing returns**: `Δ_k → 0` as `k → ∞` (the model space `F_∞` saturates the continuous problem). Empirically, `Δ_k` decays roughly geometrically — P9 lesson #66: `k = 14 → k = 15` drop is `4.57e-6`, ~40× below `minImprovement`.

The **gate-feasibility ratio** is `Δ_k / minImprovement`. Decision rule (P9):

- Ratio > 1: climb is productive; submit and continue.
- Ratio in `[0.1, 1)`: marginal; try one more climb.
- Ratio < 0.1: pivot to (a) different parameterization (e.g. 4-cluster instead of 3-cluster), (b) different basin topology, or (c) declare locked at current `k`.

## When it applies

- **Polynomial-degree problems** where adding a root or coefficient is well-defined (P9 uncertainty principle, polynomial flatness).
- **Spectral / basis-truncation problems** where adding a basis function is well-defined (Fourier-coefficient problems, Chebyshev approximation).
- **Cluster/mode problems** where the model has `k` discrete components and adding a `(k+1)`-th is meaningful (Gaussian mixtures, root clusters).

Recognition: the optimizer has converged at the current `k` (gradient zero, CMA-ES sigma collapsed, multistart returns same value); the *parameterization* admits a natural extension to `k + 1`.

## Why it works

Two structural reasons:

1. **The basin at `k` is a stationary point of `min_{F_k} S`, not of `min_{F_{k+1}} S`.** The constraint `f ∈ F_k` (i.e. only `k` DOFs active, the rest pinned at default) is a *non-trivial* equality constraint in `F_{k+1}`. Releasing this constraint gives one new descent direction — the gradient of `S` along the "extra DOF" axis — which is generically non-zero.
2. **Plateaus at fixed `k` are dimensional, not basin-multimodal.** All `k`-parameter optimizers find the same `S_k` because the basin is unique at that dimension; the multimodality arises only when the model space is rich enough to support multiple stationary points. Adding a DOF restructures the problem to be either monomodal at `k+1` (in which case the climb gives the global drop) or multimodal — but the warm-start from `k` puts you on the correct branch.

The diminishing returns are a consequence of **continuous limit convergence**: as `k → ∞`, `F_k → F_∞` and `S_k → S_∞`. The convergence rate is typically polynomial (`Δ_k ~ k^{-α}` or geometric for analytic problems). Once `Δ_k` falls below `minImprovement` significantly, climbing is wasted.

## Classic examples

1. **P9 Uncertainty Principle k=13 → k=14** — all `k = 13` optimizers (CMA-ES, NM, hillclimb, gradient descent, basin hopping) converged to the same `S ≈ 0.31835`. Adding a single root in the far cluster + gap-space NM gave `S = 0.31817` immediately (drop = `1.8e-4`, 1.8× `minImprovement`). The barrier was dimensionality, not optimization quality. See [findings/k-climbing.md](../findings/k-climbing.md) lesson #24.
2. **P9 k=14 → k=15** (lesson #66) — drop = `4.57e-6`, 40× below `minImprovement` despite 22 deep-parallel CMA-ES starts and ~70 min CPU. Gate-feasibility ratio `0.046` < 0.1: pivot.
3. **General principle**: in any parametric basis-truncation problem, the climb sequence `Δ_k` is the discrete analog of "spectral decay" — the rate at which adding basis functions reduces the residual. Faster decay = problem is well-approximated by low-`k`; slower decay = continuous limit far from current `k`.

## Related

- Concepts: [parameterization-selection](parameterization-selection.md), [uncertainty-principle](uncertainty-principle.md), [discretization-as-structure](discretization-as-structure.md), [minimprovement-gate](minimprovement-gate.md).
- Techniques: [k-climbing](../techniques/k-climbing.md), [gap-space-parameterization](../techniques/gap-space-parameterization.md).
- Findings: [k-climbing](../findings/k-climbing.md).
