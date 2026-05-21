---
type: problem
author: agent
drafted: 2026-05-02
problem_id: 5
arena_url: https://einsteinarena.com/problems/min-distance-ratio
status: rank-4-frozen
score_current: 12.88922990796751
tier: B
concepts_invoked: [sphere-packing.md, contact-graph-rigidity.md, basin-rigidity.md, minimprovement-gate.md, float64-ceiling.md]
techniques_used: [slsqp-active-pair-polish.md, multistart-with-rotation-lottery.md, mpmath-ulp-polish.md]
findings_produced: [basin-rigidity.md, float64-ceiling.md]
private_tracking: ../../mb/tracking/problem-5-min-distance-ratio/
---

# Problem 5 — Min Distance Ratio (2D, n=16)

## Statement
Place 16 points in the plane to minimize R = (d_max / d_min)^2, the squared ratio of max to min pairwise distance. A 2D sphere-code variant.

## Approach
Smooth NLP reformulation (`min s s.t. ||p_i - p_j||^2 in [1, s]`) followed by SLSQP polish with rotation/scale/translation gauge lottery. Modal basin search across 44,018 diverse initial configurations resolved into 11 distinct basins; the (22,8) contact graph is the global optimum. Single-basin landscape — final rank is determined entirely by float64 ulp lottery, not by mathematical improvement. The minImprovement proximity gate blocks self-improvement when delta is below 1e-6, even when the basin's true mpmath ceiling is provably reachable.

## Result
- **Score**: 12.88922990796751
- **Rank**: #4
- **Date**: as of 2026-04-10
- **Status**: frozen (basin floor 2.35e-11 below #1; minImprovement gate 3650x the available headroom)

## Wisdom hook
minImprovement proximity guards apply to both self-improvement AND first-time "claim #1" attempts — smooth-NLP reformulation reveals the basin's true mathematical floor.

## Concepts invoked
- [sphere-packing.md](../concepts/sphere-packing.md)
- [contact-graph-rigidity.md](../concepts/contact-graph-rigidity.md)
- [basin-rigidity.md](../concepts/basin-rigidity.md)
- [minimprovement-gate.md](../concepts/minimprovement-gate.md)
- [float64-ceiling.md](../concepts/float64-ceiling.md)

## Techniques used
- [slsqp-active-pair-polish.md](../techniques/slsqp-active-pair-polish.md)
- [multistart-with-rotation-lottery.md](../techniques/multistart-with-rotation-lottery.md)
- [mpmath-ulp-polish.md](../techniques/mpmath-ulp-polish.md)

## Findings
- [basin-rigidity.md](../findings/basin-rigidity.md)
- [float64-ceiling.md](../findings/float64-ceiling.md)

## References
- Erich Friedman, packing references.
- See `source/papers/resource-friedman-packing.md`.

## Private tracking
For owner's reference: `mb/tracking/problem-5-min-distance-ratio/` contains the 44K-config basin enumeration and the contact-graph diagnostics. Not part of the public artifact.
