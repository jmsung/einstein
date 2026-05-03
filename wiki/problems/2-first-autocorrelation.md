---
type: problem
author: agent
drafted: 2026-05-02
problem_id: 2
arena_url: https://einsteinarena.com/problems/first-autocorrelation
status: conquered
score_current: 1.5028616283497658
tier: S
concepts_invoked: [autocorrelation-inequality.md, equioscillation.md, parameterization-selection.md, sidon-sets.md, smooth-max-approximation.md]
techniques_used: [larger-n-cascade.md, lp-cutting-plane-warmstart.md, bounded-lbfgs-per-region-sigmoid.md, warm-start-from-leader.md]
findings_produced: [optimizer-recipes.md, equioscillation-escape.md, p2-peak-locking-hessian-mechanism.md, p2-lower-bound-research-state.md]
private_tracking: ../../mb/tracking/problem-2-first-autocorrelation/
---

# Problem 2 — First Autocorrelation Inequality

## Statement
Minimize C = max(f * f) / (integral f)^2 over non-negative functions f on [-1/4, 1/4]. Equivalently, find the tightest constant in the autoconvolution inequality.

## Approach
The previous SOTA (9-way tie) sat in a piecewise-constant equioscillation basin pinned by the standard exp(v) parameterization — exponential parameterizations peak-lock and resist polishing. Switching to the square parameterization f = v^2 unlocked a fundamentally different optimization geometry: ultra-aggressive low-beta L-BFGS on the smooth-max objective at n=90000 escaped the tie basin and converged to a strictly lower C. Method also explored cutting-plane LP (Kolountzakis-Matolcsi), Adam peak-flattening, larger-n cascade, Frank-Wolfe, and multi-active subgradient — the parameterization swap was the load-bearing change.

## Result
- **Score**: 1.5028616283497658
- **Rank**: #1 (sole)
- **Date**: 2026-04-15
- **Status**: conquered (delta = 1.23e-6, which is 12.3x minImprovement)

## Wisdom hook
Peak-locking via exp(v) parameterization is fundamental to equioscillation basins — escape requires parameterization change, not optimization intensity.

## Concepts invoked
- [autocorrelation-inequality.md](../concepts/autocorrelation-inequality.md)
- [equioscillation.md](../concepts/equioscillation.md)
- [parameterization-selection.md](../concepts/parameterization-selection.md)
- [sidon-sets.md](../concepts/sidon-sets.md)
- [smooth-max-approximation.md](../concepts/smooth-max-approximation.md)

## Techniques used
- [larger-n-cascade.md](../techniques/larger-n-cascade.md)
- [lp-cutting-plane-warmstart.md](../techniques/lp-cutting-plane-warmstart.md)
- [bounded-lbfgs-per-region-sigmoid.md](../techniques/bounded-lbfgs-per-region-sigmoid.md)
- [warm-start-from-leader.md](../techniques/warm-start-from-leader.md)

## Findings
- [optimizer-recipes.md](../findings/optimizer-recipes.md)
- [equioscillation-escape.md](../findings/equioscillation-escape.md)

## References
- Matolcsi-Kolountzakis (2010), autoconvolution inequalities.
- Cloninger-Steinerberger (2017), autoconvolution and Sidon sets.
- Jaech (2025), Boyer (2025), Rechnitzer (2026) — recent autoconvolution numerics.
- See `source/papers/2010-matolcsi-autoconvolution.md` and related distillations.

## Private tracking
For owner's reference: `mb/tracking/problem-2-first-autocorrelation/` contains experiment log, v3 reproduction recipe, and breakthrough notes. Not part of the public artifact.
