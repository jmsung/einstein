---
type: problem
author: agent
drafted: 2026-05-02
problem_id: 17
arena_url: https://einsteinarena.com/problems/hexagon-packing
status: rank-1-tied
score_current: 3.9416523
tier: C
concepts_invoked: [sphere-packing.md, symmetry-and-fundamental-domain.md, float64-ceiling.md]
techniques_used: [warm-start-from-leader.md, basin-hopping-multistart.md]
findings_produced: [packing-techniques.md]
private_tracking: ../../mb/tracking/problem-17-hexagon-packing/
---

# Problem 17a — Hexagon Packing (n=12)

## Statement
Pack 12 unit hexagons (each free to rotate) inside a larger hexagon; minimize the outer hexagon's side length.

## Approach
All top-10 agents share identical hexagon positions — the basin is unique. Pipeline: warm-start from public SOTA, Nelder-Mead on the 4 outer-hexagon parameters (side length, center, angle), differential evolution across all 40 parameters (12 hexagons x 3 plus outer params), Nelder-Mead polish, hillclimb with adaptive step sizes. Rank determined by float64-ceiling precision, not optimizer choice.

## Result
- **Score**: 3.9416523
- **Rank**: #1 (tied)
- **Date**: as of 2026-05-02
- **Status**: tied at known-optimal basin

## Wisdom hook
Symmetric packing problems converge to a unique basin — rank determined by float64-ceiling precision, not optimizer choice.

## Concepts invoked
- [sphere-packing.md](../concepts/sphere-packing.md)
- [symmetry-and-fundamental-domain.md](../concepts/symmetry-and-fundamental-domain.md)
- [float64-ceiling.md](../concepts/float64-ceiling.md)

## Techniques used
- [warm-start-from-leader.md](../techniques/warm-start-from-leader.md)
- [basin-hopping-multistart.md](../techniques/basin-hopping-multistart.md)

## Findings
- [packing-techniques.md](../findings/packing-techniques.md)

## References
- Erich Friedman, packing references.
- Specht hexagonal packing tables.

## Private tracking
For owner's reference: `mb/tracking/problem-17-hexagon-packing/` contains the warm-start polish log. Not part of the public artifact.
