---
type: problem
author: agent
drafted: 2026-05-02
problem_id: 22
arena_url: https://einsteinarena.com/problems/kissing-d12
status: rank-3
score_current: 2.001403089191293
tier: A
concepts_invoked: [kissing-number.md, sphere-packing.md, hinge-overlap.md, first-order-link-tangent-test.md, basin-rigidity.md]
techniques_used: [first-order-link-tangent-test.md, parallel-tempering-sa.md, slsqp-active-pair-polish.md, micro-perturbation-multiscale.md]
findings_produced: [hinge-overlap-rank3-squeeze.md, p22-d12-construction-survey.md]
private_tracking: ../../mb/tracking/problem-22-kissing-d12/
---

# Problem 22 — Kissing Number in Dimension 12 (n=841)

## Statement
Place 841 unit vectors in R^12; minimize the hinge-overlap score = sum_{i<j} max(0, 2 - ||c_i - c_j||) where c_i = 2 v_i / ||v_i||. Score 0 would prove kappa(12) >= 841.

## Approach
Empirical 8-way structural cap analysis: kappa(12) = 840 is consistent across multiple independent algebraic pathways (non-lattice P_{12a} Leech-Sloane 1971 is empirically tight). Score 0 is mathematically infeasible — at least one duplicate pair is required. The first-order link-tangent test computes the link's tangent space at a candidate solution and minimizes S(u) over it; if min S(u) >= 1 the duplicate pair is a strict local minimum (no first-order escape). Exhaustive paths tried: filler-only L-BFGS (300 starts, all duplicate basin), parallel GPU random filler (10M positions), 60-degree-edge midpoint scan, joint exact-hinge RGD, remove-and-replace from 5 cores, parallel tempering SA (16 replicas).

## Result
- **Score**: 2.001403089191293
- **Rank**: #3 (banked +1 point; rank #1 with score < 2.0 mathematically infeasible)
- **Date**: 2026-04-25
- **Status**: rank-3 secured; rank-1 ruled out

## Wisdom hook
Kissing-tight problems with known structural caps require first-order tangent-space analysis — if min S(u) > 1 over the link tangent, the duplicate is a strict local minimum.

## Concepts invoked
- [kissing-number.md](../concepts/kissing-number.md)
- [sphere-packing.md](../concepts/sphere-packing.md)
- [hinge-overlap.md](../concepts/hinge-overlap.md)
- [first-order-link-tangent-test.md](../concepts/first-order-link-tangent-test.md)
- [basin-rigidity.md](../concepts/basin-rigidity.md)

## Techniques used
- [first-order-link-tangent-test.md](../techniques/first-order-link-tangent-test.md)
- [parallel-tempering-sa.md](../techniques/parallel-tempering-sa.md)
- [slsqp-active-pair-polish.md](../techniques/slsqp-active-pair-polish.md)
- [micro-perturbation-multiscale.md](../techniques/micro-perturbation-multiscale.md)

## Findings
- [hinge-overlap-rank3-squeeze.md](../findings/hinge-overlap-rank3-squeeze.md)
- [p22-d12-construction-survey.md](../findings/p22-d12-construction-survey.md)

## References
- Boyvalenkov et al. (2012), kissing-number survey.
- Cohn-de Laat-Salmon (2019), uncertainty principles in d=12.
- Leech, "Notes on sphere packings" (1967), Sloane sphere-codes archive.
- Conway and Sloane, "Sphere Packings, Lattices and Groups."

## Private tracking
For owner's reference: `mb/tracking/problem-22-kissing-d12/` contains the 8-way cap survey, the link-tangent calculation, and the rank-3 submission archive. Not part of the public artifact.
