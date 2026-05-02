---
type: problem
author: agent
drafted: 2026-05-02
problem_id: 1
arena_url: https://einsteinarena.com/problems/erdos-overlap
status: rank-2-frozen
score_current: 0.380870310586
tier: C
concepts_invoked: [equioscillation.md, smooth-max-approximation.md, lp-duality.md]
techniques_used: [remez-equioscillation-diagnostic.md, sdp-flag-algebra.md, basin-hopping-multistart.md]
findings_produced: [equioscillation-escape.md]
private_tracking: ../../mb/tracking/problem-1-erdos-overlap/
---

# Problem 1 — Erdős Minimum Overlap

## Statement
Find a normalized step function on the unit interval that minimizes the maximum overlap (cross-correlation) with all of its shifts. The classical Erdős minimum overlap problem.

## Approach
Bilinear minimax in disguise. Investigated SDP relaxations, sequential LP, coordinate descent, basin-hopping, CMA-ES, Fourier parameterization (K up to 80), Remez exchange, and mass-transport reformulations. All converged to the same Remez-optimal equioscillation plateau. SDP fails because the primal optimum is rank-1 — lifting destroys the structure and the bound becomes loose. The 0.0008 lower-/upper-bound gap has been open 20+ years.

## Result
- **Score**: 0.3808703105862199
- **Rank**: #2 (3-way tie at SOTA, frozen)
- **Date**: as of 2026-05-02
- **Status**: frozen at mathematical plateau; minImprovement gate is 10,000x the available headroom

## Wisdom hook
Bilinear minimax problems defeat SDP relaxation regardless of discretization scale — the rank-1 structure is load-bearing.

## Concepts invoked
- [equioscillation.md](../concepts/equioscillation.md)
- [smooth-max-approximation.md](../concepts/smooth-max-approximation.md)
- [lp-duality.md](../concepts/lp-duality.md)

## Techniques used
- [remez-equioscillation-diagnostic.md](../techniques/remez-equioscillation-diagnostic.md)
- [sdp-flag-algebra.md](../techniques/sdp-flag-algebra.md)
- [basin-hopping-multistart.md](../techniques/basin-hopping-multistart.md)

## Findings
- [equioscillation-escape.md](../findings/equioscillation-escape.md)

## References
- White (2022), Erdős minimum overlap problem analysis.
- Haugland (2016), tight numerical bounds.
- See `source/papers/2022-white-erdos-overlap.md`, `source/papers/2016-haugland-min-overlap.md`.

## Private tracking
For owner's reference: `mb/tracking/problem-1-erdos-overlap/` contains experiment log, optimality proofs, and 111+ experiment audit trail. Not part of the public artifact.
