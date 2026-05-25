---
type: report
author: agent
generated_at: 2026-05-23
source: docs/tools/concept_inventory.py
---

# Concept coverage report

Programmatic view of concept/technique/finding references across `docs/wiki/problems/*.md` frontmatter, classified by wiki + source/ coverage. Drives `docs/tools/seed_ingest.py`.

## Summary

| Classification | Count |
|---|---|
| missing-page | 0 |
| under-sourced | 28 |
| well-covered | 23 |
| orphan-or-singleton | 26 |

## under-sourced (28)

| Kind | Name | Refs (problem ids) | Has page | Has source |
|---|---|---|---|---|
| technique | `slsqp-active-pair-polish.md` | P5, P6, P11, P14, P15, P16, P18, P22 | ✓ | · |
| technique | `warm-start-from-leader.md` | P2, P7, P11, P16, P17, P18 | ✓ | · |
| concept | `float64-ceiling.md` | P5, P11, P14, P17, P18 | ✓ | · |
| technique | `multistart-with-rotation-lottery.md` | P5, P11, P12, P13, P16 | ✓ | · |
| concept | `arena-tolerance-drift.md` | P7, P9, P14, P18 | ✓ | · |
| concept | `minimprovement-gate.md` | P5, P15, P16, P18 | ✓ | · |
| concept | `symmetry-and-fundamental-domain.md` | P10, P15, P16, P17 | ✓ | · |
| concept | `smooth-max-approximation.md` | P1, P2, P4 | ✓ | · |
| finding | `p2-peak-locking-hessian-mechanism.md` | P2, P3, P4 | ✓ | · |
| finding | `packing-techniques.md` | P14, P17, P18 | ✓ | · |
| technique | `bounded-lbfgs-per-region-sigmoid.md` | P2, P4, P13 | ✓ | · |
| technique | `larger-n-cascade.md` | P2, P3, P4 | ✓ | · |
| technique | `micro-perturbation-multiscale.md` | P4, P6, P22 | ✓ | · |
| concept | `contact-graph-rigidity.md` | P5, P11 | ✓ | · |
| concept | `first-order-link-tangent-test.md` | P22, P23 | ✓ | · |
| concept | `hinge-overlap.md` | P6, P22 | ✓ | · |
| concept | `k-climbing-and-dof-augmentation.md` | P9, P18 | ✓ | · |
| concept | `parameterization-induced-rank-deficiency.md` | P2, P3 | ✓ | · |
| finding | `float64-ceiling.md` | P5, P11 | ✓ | · |
| finding | `hinge-overlap-rank3-squeeze.md` | P6, P22 | ✓ | · |
| technique | `arena-tolerance-slsqp.md` | P14, P18 | ✓ | · |
| technique | `first-order-link-tangent-test.md` | P22, P23 | ✓ | · |
| technique | `gap-space-parameterization.md` | P9, P18 | ✓ | · |
| technique | `gpu-decision-framework.md` | P3, P6 | ✓ | · |
| technique | `k-climbing.md` | P9, P18 | ✓ | · |
| technique | `lp-cutting-plane-warmstart.md` | P2, P7 | ✓ | · |
| technique | `memetic-tabu-search.md` | P12, P19 | ✓ | · |
| technique | `uniform-radius-shrink-fallback.md` | P14, P18 | ✓ | · |

## well-covered (23)

| Kind | Name | Refs (problem ids) | Has page | Has source |
|---|---|---|---|---|
| concept | `basin-rigidity.md` | P5, P6, P10, P11, P12, P13, P14, P15, P16, P19, P22 | ✓ | ✓ |
| concept | `sphere-packing.md` | P5, P6, P10, P11, P14, P17, P18, P22, P23 | ✓ | ✓ |
| technique | `basin-hopping-multistart.md` | P1, P10, P12, P13, P15, P16, P17 | ✓ | ✓ |
| technique | `mpmath-ulp-polish.md` | P5, P6, P9, P10, P11, P14, P18 | ✓ | ✓ |
| concept | `equioscillation.md` | P1, P2, P4, P13, P15, P16 | ✓ | ✓ |
| concept | `parameterization-selection.md` | P2, P3, P4, P9, P13, P18 | ✓ | ✓ |
| finding | `optimizer-recipes.md` | P2, P3, P4, P13 | ✓ | ✓ |
| concept | `autocorrelation-inequality.md` | P2, P3, P4 | ✓ | ✓ |
| concept | `circle-packing.md` | P14, P17, P18 | ✓ | ✓ |
| concept | `kissing-number.md` | P6, P22, P23 | ✓ | ✓ |
| concept | `sidon-sets.md` | P2, P3, P19 | ✓ | ✓ |
| finding | `arena-proximity-guard.md` | P14, P16, P18 | ✓ | ✓ |
| finding | `basin-rigidity.md` | P5, P15, P16 | ✓ | ✓ |
| finding | `equioscillation-escape.md` | P1, P2, P4 | ✓ | ✓ |
| technique | `cma-es-with-warmstart.md` | P9, P15, P16 | ✓ | ✓ |
| technique | `parallel-tempering-sa.md` | P6, P10, P22 | ✓ | ✓ |
| concept | `bourgain-clozel-kahane.md` | P9, P18 | ✓ | ✓ |
| concept | `lp-duality.md` | P1, P7 | ✓ | ✓ |
| concept | `probabilistic-method.md` | P12, P19 | ✓ | ✓ |
| concept | `uncertainty-principle.md` | P9, P18 | ✓ | ✓ |
| finding | `discrete-optimization.md` | P12, P19 | ✓ | ✓ |
| finding | `gpu-modal-compute.md` | P3, P6 | ✓ | ✓ |
| finding | `verification-patterns.md` | P9, P18 | ✓ | ✓ |

## orphan-or-singleton (26)

| Kind | Name | Refs (problem ids) | Has page | Has source |
|---|---|---|---|---|
| concept | `discretization-as-structure.md` | P12 | ✓ | · |
| concept | `flag-algebra.md` | P13 | ✓ | ✓ |
| concept | `fractal-perturbation-landscape.md` | P6 | ✓ | · |
| concept | `fractional-programming-dinkelbach.md` | P3 | ✓ | · |
| concept | `kronecker-decomposition.md` | P19 | ✓ | · |
| concept | `n-extension-monotonicity.md` | P7 | ✓ | · |
| concept | `provable-floor-and-frozen-problems.md` | P10 | ✓ | · |
| concept | `sieve-theory-as-lp.md` | P7 | ✓ | · |
| concept | `turan-density.md` | P13 | ✓ | · |
| finding | `float64-polish.md` | P6 | ✓ | ✓ |
| finding | `frozen-problem-triage.md` | P10 | ✓ | · |
| finding | `lp-solver-scaling.md` | P7 | ✓ | ✓ |
| finding | `p22-d12-construction-survey.md` | P22 | ✓ | ✓ |
| finding | `perturbation-landscape.md` | P6 | ✓ | · |
| finding | `polish-race-dynamics.md` | P13 | ✓ | · |
| finding | `prime-number-theorem-lp.md` | P7 | ✓ | ✓ |
| finding | `sa-parallel-tempering.md` | P6 | ✓ | ✓ |
| technique | `bnb-exhaustive-w3.md` | P19 | ✓ | · |
| technique | `boundary-snap-for-kinks.md` | P13 | ✓ | · |
| technique | `compute-router.md` | P6 | ✓ | ✓ |
| technique | `cross-resolution-basin-transfer.md` | P3 | ✓ | · |
| technique | `dinkelbach-fractional-programming.md` | P3 | ✓ | ✓ |
| technique | `greedy-insert-cd-redistribute.md` | P13 | ✓ | · |
| technique | `kronecker-search-decomposition.md` | P19 | ✓ | · |
| technique | `remez-equioscillation-diagnostic.md` | P1 | ✓ | · |
| technique | `sdp-flag-algebra.md` | P1 | ✓ | ✓ |
