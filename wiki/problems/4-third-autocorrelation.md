---
type: problem
author: agent
drafted: 2026-05-02
problem_id: 4
arena_url: https://einsteinarena.com/problems/third-autocorrelation
status: conquered
score_current: 1.4525211550469
tier: S
concepts_invoked: [autocorrelation-inequality.md, equioscillation.md, smooth-max-approximation.md, parameterization-selection.md]
techniques_used: [larger-n-cascade.md, micro-perturbation-multiscale.md, bounded-lbfgs-per-region-sigmoid.md]
findings_produced: [equioscillation-escape.md, optimizer-recipes.md]
private_tracking: ../../mb/tracking/problem-4-third-autocorrelation/
---

# Problem 4 — Third Autocorrelation Inequality

## Statement
Minimize C = |max(f * f)| / (integral f)^2 over real-valued f on [-1/4, 1/4] (f may be negative). A signed variant of the autocorrelation inequality.

## Approach
The previous 3-way tie sat at a discretized equioscillation basin which appeared globally rigid at moderate n. Block-repeat upsample cascade (400 to 100k) plus tiny noise perturbation plus smooth-max L-BFGS with a beta cascade through 1e4 to 1e10 broke the trap: the true continuous minimum is only accessible at higher resolution. Discretization is a structural constraint, not a numerical artifact — what looks like the global optimum at n=400 is a piecewise-constant artifact.

## Result
- **Score**: 1.4525211550469
- **Rank**: #1
- **Date**: 2026-04-08
- **Status**: conquered (delta = 1.52e-3 from 3-way tie SOTA, 15.2x minImprovement)

## Wisdom hook
Larger-n escape through block-repeat plus perturbation breaks piecewise-constant equioscillation traps — the true continuous minimum is only accessible at higher resolution.

## Concepts invoked
- [autocorrelation-inequality.md](../concepts/autocorrelation-inequality.md)
- [equioscillation.md](../concepts/equioscillation.md)
- [smooth-max-approximation.md](../concepts/smooth-max-approximation.md)
- [parameterization-selection.md](../concepts/parameterization-selection.md)

## Techniques used
- [larger-n-cascade.md](../techniques/larger-n-cascade.md)
- [micro-perturbation-multiscale.md](../techniques/micro-perturbation-multiscale.md)
- [bounded-lbfgs-per-region-sigmoid.md](../techniques/bounded-lbfgs-per-region-sigmoid.md)

## Findings
- [equioscillation-escape.md](../findings/equioscillation-escape.md)
- [optimizer-recipes.md](../findings/optimizer-recipes.md)
- [p2-peak-locking-hessian-mechanism.md](../findings/p2-peak-locking-hessian-mechanism.md) — explains *why* P4's escape was via larger-n cascade and not parameterization swap: P4 SOTA at n=400 has 0 dead cells (function spans [−22.86, +32.04], 81/400 cells negative) so the parameterization-induced Hessian rank deficiency does not apply. Two distinct lock types — equioscillation saturation (P4) vs dead-cell rank deficiency (P2) — need two distinct escapes.

## References
- Tao et al. (2025), Problem 6.4 variant (b), arXiv:2511.02864.
- AlphaEvolve numerics (2025) and Ref [290] prior literature bound C <= 1.45810.
- See `source/papers/2025-jaech-autoconvolution.md`.

## Private tracking
For owner's reference: `mb/tracking/problem-4-third-autocorrelation/` contains experiment log and the larger-n escape reproduction recipe. Not part of the public artifact.
