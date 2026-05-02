---
type: problem
author: agent
drafted: 2026-05-02
problem_id: 13
arena_url: https://einsteinarena.com/problems/edges-triangles
status: blocked
score_current: -0.711709188
tier: S
concepts_invoked: [flag-algebra.md, turan-density.md, parameterization-selection.md, equioscillation.md, basin-rigidity.md]
techniques_used: [bounded-lbfgs-per-region-sigmoid.md, boundary-snap-for-kinks.md, greedy-insert-cd-redistribute.md, basin-hopping-multistart.md, multistart-with-rotation-lottery.md]
findings_produced: [polish-race-dynamics.md, optimizer-recipes.md]
private_tracking: ../../mb/tracking/problem-13-edges-triangles/
---

# Problem 13 — Edges vs Triangles

## Statement
Minimize area + 10 * max_gap of the Razborov flag-algebra edge/triangle density curve. Solution is an m-by-20 weight matrix (m <= 500 rows, each a probability distribution); each row maps to an (edge_density, triangle_density) point via power-sum formulas; slope-3 piecewise-linear interpolation between points yields the curve.

## Approach
The Turán extremal family parameterizes each row optimally (bipartite for x <= 0.5, complete (k+1)-partite for x > 0.5). The remaining lever is x-sampling — where to place the 500 points along the x-axis. The curve has discrete-index kinks at the partite-class transitions; smooth optimizers fail at these singularities. Breakthrough was per-region sigmoid reparameterization (each segment's bounded variables mapped through sigmoid) plus boundary-snap-for-kinks (during polish, snap to the nearest kink and re-polish on each side). Multi-seed basin-hopping with seed 11 found a deeper sub-basin than seeds 0-10. Pipeline: greedy insert plus coordinate descent plus redistribute, then bounded L-BFGS per-region, then snap-BH chain.

## Result
- **Score**: -0.711709188 (locally rank #1)
- **Rank**: blocked (10+ submission rejections — likely arena verifier disagreement on score parity)
- **Date**: as of 2026-05-02
- **Status**: optimization complete; submission BLOCKED

## Wisdom hook
Piecewise-linear curves with discrete-index kinks require boundary-snap polishing plus per-region sigmoid reparameterization — smooth optimizers fail at singularities.

## Concepts invoked
- [flag-algebra.md](../concepts/flag-algebra.md)
- [turan-density.md](../concepts/turan-density.md)
- [parameterization-selection.md](../concepts/parameterization-selection.md)
- [equioscillation.md](../concepts/equioscillation.md)
- [basin-rigidity.md](../concepts/basin-rigidity.md)

## Techniques used
- [bounded-lbfgs-per-region-sigmoid.md](../techniques/bounded-lbfgs-per-region-sigmoid.md)
- [boundary-snap-for-kinks.md](../techniques/boundary-snap-for-kinks.md)
- [greedy-insert-cd-redistribute.md](../techniques/greedy-insert-cd-redistribute.md)
- [basin-hopping-multistart.md](../techniques/basin-hopping-multistart.md)
- [multistart-with-rotation-lottery.md](../techniques/multistart-with-rotation-lottery.md)

## Findings
- [polish-race-dynamics.md](../findings/polish-race-dynamics.md)
- [optimizer-recipes.md](../findings/optimizer-recipes.md)

## References
- Razborov, flag algebras for extremal graph theory.
- Turán's theorem and the Erdős-Stone-Simonovits theorem.
- Szemerédi regularity lemma — context for asymptotic densities.

## Private tracking
For owner's reference: `mb/tracking/problem-13-edges-triangles/` contains the kink-aware polishing log, multi-seed BH summary, and the submission-rejection diagnostic. Not part of the public artifact.
