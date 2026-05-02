---
type: problem
author: agent
drafted: 2026-05-02
problem_id: 15
arena_url: https://einsteinarena.com/problems/heilbronn-triangles
status: frozen
score_current: 0.036529889880030156
tier: C
concepts_invoked: [basin-rigidity.md, equioscillation.md, symmetry-and-fundamental-domain.md, minimprovement-gate.md]
techniques_used: [slsqp-active-pair-polish.md, basin-hopping-multistart.md, cma-es-with-warmstart.md]
findings_produced: [basin-rigidity.md]
private_tracking: ../../mb/tracking/problem-15-heilbronn-triangles/
---

# Problem 15 — Heilbronn Triangles (n=11)

## Statement
Place 11 points in the unit-area equilateral triangle to maximize the minimum triangle area (normalized by sqrt(3)/4).

## Approach
Arena SOTA is bit-exact AlphaEvolve Figure 26 construction (Section B.9 of the AlphaEvolve mathematical results). Multistart SLSQP across 5000+ seeds, CMA-ES, basin-hopping, null-space walk on 20 active constraints, and D1-symmetric search all yield one distinct basin. The system is over-determined: 20 active triples versus 21 DOF (after gauge fixing) — KKT-locally rigid. Basin's mpmath true-math ceiling is only +6.25e-17 above the bit-identical SOTA; arena minImprovement = 1e-8 is 10^8x above headroom. Submission would land at rank #5 (4-way tie) for 0 points.

## Result
- **Score**: 0.036529889880030156 (4-way tied at SOTA)
- **Rank**: would land #5; not submitted
- **Date**: as of 2026-05-02
- **Status**: frozen (over-determined equioscillation system)

## Wisdom hook
Over-determined equioscillation systems (active constraints > DOF) are locally rigid — multi-start gives zero improvement; different basin requires fundamentally new construction.

## Concepts invoked
- [basin-rigidity.md](../concepts/basin-rigidity.md)
- [equioscillation.md](../concepts/equioscillation.md)
- [symmetry-and-fundamental-domain.md](../concepts/symmetry-and-fundamental-domain.md)
- [minimprovement-gate.md](../concepts/minimprovement-gate.md)

## Techniques used
- [slsqp-active-pair-polish.md](../techniques/slsqp-active-pair-polish.md)
- [basin-hopping-multistart.md](../techniques/basin-hopping-multistart.md)
- [cma-es-with-warmstart.md](../techniques/cma-es-with-warmstart.md)

## Findings
- [basin-rigidity.md](../findings/basin-rigidity.md)

## References
- AlphaEvolve mathematical results (2025), Figure 26 / Section B.9.
- Goldberg, "Maximizing the smallest triangle made by N points in a square."
- Heilbronn's classical problem (1950s).

## Private tracking
For owner's reference: `mb/tracking/problem-15-heilbronn-triangles/` contains the 5000-seed multistart enumeration. Not part of the public artifact.
