---
type: problem
author: agent
drafted: 2026-05-02
problem_id: 6
arena_url: https://einsteinarena.com/problems/kissing-number-d11
status: conquered
score_current: 0.0
tier: S
concepts_invoked: [sphere-packing.md, kissing-number.md, hinge-overlap.md, fractal-perturbation-landscape.md, basin-rigidity.md]
techniques_used: [parallel-tempering-sa.md, micro-perturbation-multiscale.md, slsqp-active-pair-polish.md, mpmath-ulp-polish.md, gpu-decision-framework.md, compute-router.md]
findings_produced: [perturbation-landscape.md, sa-parallel-tempering.md, hinge-overlap-rank3-squeeze.md, gpu-modal-compute.md, float64-polish.md]
private_tracking: ../../mb/tracking/problem-6-kissing-number/
---

# Problem 6 — Kissing Number in Dimension 11 (n=594)

## Statement
Place 594 unit vectors in R^11 so that every pair separates by at least 1 (i.e., 594 unit spheres each tangent to a central unit sphere with no pairwise overlap). Score = total hinge overlap; score 0 proves the kissing number kappa(11) >= 594.

## Approach
Hinge-loss landscapes are fractal at atomic scales — perturbations at 1e-14 can improve where 1e-10 cannot. Smooth optimizers see a flat plateau; multi-scale contribution-weighted micro-perturbation reveals structure invisible to gradient methods. Parallel tempering SA with 64 replicas on Modal A100 (geometric temperature ladder, periodic Metropolis exchange, perturbation magnitude weighted by per-vector contribution to the loss) achieved 730x speedup over greedy. Final descent: GPU fused-batch tempering plus exact subgradient on active pairs plus targeted multi-vector polish drove the loss to exactly 0.

## Result
- **Score**: 0.0 (theoretical minimum, unbeatable)
- **Rank**: #1
- **Date**: 2026-04-09
- **Status**: conquered. Proves kappa(11) >= 594.

## Wisdom hook
Hinge-loss landscapes are fractal at atomic scales (1e-14 can improve 1e-10) — contribution-weighted multi-scale perturbation with parallel tempering is essential for kissing-tight problems.

## Concepts invoked
- [sphere-packing.md](../concepts/sphere-packing.md)
- [kissing-number.md](../concepts/kissing-number.md)
- [hinge-overlap.md](../concepts/hinge-overlap.md)
- [fractal-perturbation-landscape.md](../concepts/fractal-perturbation-landscape.md)
- [basin-rigidity.md](../concepts/basin-rigidity.md)

## Techniques used
- [parallel-tempering-sa.md](../techniques/parallel-tempering-sa.md)
- [micro-perturbation-multiscale.md](../techniques/micro-perturbation-multiscale.md)
- [slsqp-active-pair-polish.md](../techniques/slsqp-active-pair-polish.md)
- [mpmath-ulp-polish.md](../techniques/mpmath-ulp-polish.md)
- [gpu-decision-framework.md](../techniques/gpu-decision-framework.md)
- [compute-router.md](../techniques/compute-router.md)

## Findings
- [perturbation-landscape.md](../findings/perturbation-landscape.md)
- [sa-parallel-tempering.md](../findings/sa-parallel-tempering.md)
- [hinge-overlap-rank3-squeeze.md](../findings/hinge-overlap-rank3-squeeze.md)
- [gpu-modal-compute.md](../findings/gpu-modal-compute.md)
- [float64-polish.md](../findings/float64-polish.md)

## References
- Conway and Sloane, "Sphere Packings, Lattices and Groups."
- Cohn-Elkies LP bounds for kissing numbers.
- Viazovska's optimality proofs (d=8, d=24) — context.
- See `source/papers/` distillations of the kissing-number literature.

## Private tracking
For owner's reference: `mb/tracking/problem-6-kissing-number/` contains the multi-scale perturbation calibration, the GPU tempering benchmark log, and the final solution that achieves loss = 0. Not part of the public artifact.
