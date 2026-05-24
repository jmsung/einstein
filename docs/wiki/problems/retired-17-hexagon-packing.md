---
type: problem
author: agent
drafted: 2026-05-02
problem_id: 17
arena_url: https://einsteinarena.com/problems/hexagon-packing
status: retired
retired_at: 2026-05-23
status_when_retired: rank-1-tied
successor: null
score_current: 3.9416523
tier: C
concepts_invoked: [sphere-packing.md, circle-packing.md, symmetry-and-fundamental-domain.md, float64-ceiling.md]
techniques_used: [warm-start-from-leader.md, basin-hopping-multistart.md]
findings_produced: [packing-techniques.md]
private_tracking: ../../mb/problems/17-hexagon-packing/
---

> **⚠ Retired from arena 2026-05-23.** Hexagon-packing (n=12 hexagons in a hexagonal container) is no longer hosted at `einsteinarena.com/problems/hexagon-packing` (HTTP 404). No direct successor on the live arena, but the packing-techniques wisdom transfers to **[Problem 14 — Circle Packing in Square](14-circle-packing-square.md)** and **[Problem 18 — Circles in Rectangle](18-circles-rectangle.md)**.

# Problem 17a — Hexagon Packing (n=12)  *(retired)*

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
For owner's reference: `mb/problems/17-hexagon-packing/` contains the warm-start polish log. Not part of the public artifact.
