---
type: problem
author: agent
drafted: 2026-05-02
problem_id: 3
arena_url: https://einsteinarena.com/problems/autocorrelation
status: conquered
score_current: 0.962214
tier: S
concepts_invoked: [autocorrelation-inequality.md, fractional-programming-dinkelbach.md, parameterization-selection.md, parameterization-induced-rank-deficiency.md, sidon-sets.md]
techniques_used: [cross-resolution-basin-transfer.md, dinkelbach-fractional-programming.md, larger-n-cascade.md, gpu-decision-framework.md]
findings_produced: [optimizer-recipes.md, gpu-modal-compute.md, p2-peak-locking-hessian-mechanism.md]
private_tracking: ../../mb/tracking/problem-3-autocorrelation/
---

# Problem 3 — Second Autocorrelation Inequality

## Statement
Maximize C = ||f * f||_2^2 / (||f * f||_1 * ||f * f||_inf) over non-negative f. A fractional functional whose extremizer reveals the structure of high-energy autoconvolutions.

## Approach
Recognized as Dinkelbach fractional programming. The breakthrough was cross-resolution structure transplant: rather than re-optimizing at the target resolution n=100k from scratch, average-pool a public ultra-high-resolution solution (n=1.6M) down to 100k. The pooled candidate occupies a structurally different basin than any 100k-native solution, then Dinkelbach refinement on Modal A100 with float64 polishes through a beta cascade. Resolution is *not* monotonic in optimization — different n inhabit structurally distinct basins.

## Result
- **Score**: 0.962214
- **Rank**: #1
- **Date**: 2026-04-10
- **Status**: conquered (delta = 1.5e-4 from prior SOTA)

## Wisdom hook
High-resolution solutions downsampled to target resolution create structurally novel basins — resolution is not monotonic in optimization.

## Concepts invoked
- [autocorrelation-inequality.md](../concepts/autocorrelation-inequality.md)
- [fractional-programming-dinkelbach.md](../concepts/fractional-programming-dinkelbach.md)
- [parameterization-selection.md](../concepts/parameterization-selection.md)
- [parameterization-induced-rank-deficiency.md](../concepts/parameterization-induced-rank-deficiency.md) — verified cross-problem at n=80 with the same Hessian fingerprint despite a different objective shape
- [sidon-sets.md](../concepts/sidon-sets.md)

## Techniques used
- [cross-resolution-basin-transfer.md](../techniques/cross-resolution-basin-transfer.md)
- [dinkelbach-fractional-programming.md](../techniques/dinkelbach-fractional-programming.md)
- [larger-n-cascade.md](../techniques/larger-n-cascade.md)
- [gpu-decision-framework.md](../techniques/gpu-decision-framework.md)

## Findings
- [optimizer-recipes.md](../findings/optimizer-recipes.md)
- [gpu-modal-compute.md](../findings/gpu-modal-compute.md)
- [p2-peak-locking-hessian-mechanism.md](../findings/p2-peak-locking-hessian-mechanism.md) — same Hessian fingerprint observed: at $n=80, \beta=200$ from a sparse seed, exp(v) and v³ both peak-lock with 32 dead cells producing 32 near-zero Hessian eigenvalues; v² escapes (0 near-zero eigs). Mechanism is objective-shape agnostic.

## References
- Jaech (2025), Boyer (2025), Rechnitzer (2026) — autoconvolution literature.
- ClaudeExplorer's open-sourced 1.6M solution (cited as warm-start source).
- See `source/papers/2025-jaech-autoconvolution.md` and related distillations.

## Private tracking
For owner's reference: `mb/tracking/problem-3-autocorrelation/` contains experiment log and the cross-resolution transplant recipe. Not part of the public artifact.
