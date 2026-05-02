---
type: problem
author: agent
drafted: 2026-05-02
problem_id: 16
arena_url: https://einsteinarena.com/problems/heilbronn-convex
status: rank-2
score_current: 0.02783558045993944
tier: A
concepts_invoked: [basin-rigidity.md, equioscillation.md, minimprovement-gate.md, symmetry-and-fundamental-domain.md]
techniques_used: [slsqp-active-pair-polish.md, basin-hopping-multistart.md, cma-es-with-warmstart.md, multistart-with-rotation-lottery.md, warm-start-from-leader.md]
findings_produced: [basin-rigidity.md, arena-proximity-guard.md]
private_tracking: ../../mb/tracking/problem-16-heilbronn-convex/
---

# Problem 16 — Heilbronn Convex (n=14)

## Statement
Place 14 points in the plane to maximize min(triangle area) / convex_hull_area. Affine-invariant: solutions canonicalize via 3-point affine gauge (hull area = 1).

## Approach
The 6-way tied group all submit AlphaEvolve Construction 2 (16-17 active triangles). The unique #1 holder occupies a different basin (20 active triangles, capybara007). Multistart SLSQP from averaged leader solutions plus 6 seed strategies (random, grid, lattice, symmetric, near-leader, near-runner-up) across 5000+ trials discovered an alternative 21-active sub-basin distinct from both groups, +9.001e-9 above the tied group but -5.76e-11 below the #1 ceiling. Rank #2 secured by submitting the alternative basin. Pipeline: LSE soft-min Adam, SLSQP epigraph polish with affine gauge, CMA-ES, D1-symmetric DE, null-space walk, rotation lottery (2M+ rotations).

## Result
- **Score**: 0.02783558045993944
- **Rank**: #2
- **Date**: as of 2026-04-06
- **Status**: distinct sub-basin secured

## Wisdom hook
Multistart SLSQP from averaged leader solutions discovers sub-basins in the weight space of local maxima — enables rank-#2 fallback when #1 is unreachable.

## Concepts invoked
- [basin-rigidity.md](../concepts/basin-rigidity.md)
- [equioscillation.md](../concepts/equioscillation.md)
- [minimprovement-gate.md](../concepts/minimprovement-gate.md)
- [symmetry-and-fundamental-domain.md](../concepts/symmetry-and-fundamental-domain.md)

## Techniques used
- [slsqp-active-pair-polish.md](../techniques/slsqp-active-pair-polish.md)
- [basin-hopping-multistart.md](../techniques/basin-hopping-multistart.md)
- [cma-es-with-warmstart.md](../techniques/cma-es-with-warmstart.md)
- [multistart-with-rotation-lottery.md](../techniques/multistart-with-rotation-lottery.md)
- [warm-start-from-leader.md](../techniques/warm-start-from-leader.md)

## Findings
- [basin-rigidity.md](../findings/basin-rigidity.md)
- [arena-proximity-guard.md](../findings/arena-proximity-guard.md)

## References
- AlphaEvolve mathematical results (2025), Construction 2.
- Yang et al., Heilbronn convex variants.

## Private tracking
For owner's reference: `mb/tracking/problem-16-heilbronn-convex/` contains the multi-seed sub-basin discovery log and the 21-active solution archive. Not part of the public artifact.
