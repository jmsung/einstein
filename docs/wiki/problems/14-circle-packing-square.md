---
type: problem
author: agent
drafted: 2026-05-02
problem_id: 14
arena_url: https://einsteinarena.com/problems/circle-packing-square
status: rank-2-frozen
score_current: 2.6359830849175
tier: B
concepts_invoked: [sphere-packing.md, circle-packing.md, float64-ceiling.md, arena-tolerance-drift.md, basin-rigidity.md]
techniques_used: [slsqp-active-pair-polish.md, arena-tolerance-slsqp.md, uniform-radius-shrink-fallback.md, mpmath-ulp-polish.md]
findings_produced: [packing-techniques.md, arena-proximity-guard.md]
private_tracking: ../../mb/tracking/problem-14-circle-packing-square/
---

# Problem 14 — Circle Packing in Square (n=26)

## Statement
Pack 26 non-overlapping disks inside the unit square; maximize sum of radii.

## Approach
Known-optimal Packomania configuration for 30+ years. Ten parallel approaches launched from a downloaded warm-start: multistart, diverse init, topology mutate/enum, asymmetric-slack, Apollonian swap, flip-and-flow, Shinka init, Newton-max — all converged to the same basin under strict tol=0 verification. The arena verifier silently tolerates pair overlaps up to ~1e-9 with strict wall constraints; this creates an "arena-tolerance band" that some agents exploit for sub-ulp improvements. Triple-verify with strict tol=0 mpmath catches the trap (would-be 500-pt penalty if submitted under arena tolerance but rejected under strict).

## Result
- **Score**: 2.6359830849175
- **Rank**: #2 (1 ulp above tied cluster, below #1 ceiling)
- **Date**: as of 2026-04-08
- **Status**: basin-locked at float64 ceiling

## Wisdom hook
Arena tolerances drift per-problem and over time — always verify strict tol=0 before trusting "improvements" from arena-tol-exploiting optimizers.

## Concepts invoked
- [sphere-packing.md](../concepts/sphere-packing.md)
- [float64-ceiling.md](../concepts/float64-ceiling.md)
- [arena-tolerance-drift.md](../concepts/arena-tolerance-drift.md)
- [basin-rigidity.md](../concepts/basin-rigidity.md)

## Techniques used
- [slsqp-active-pair-polish.md](../techniques/slsqp-active-pair-polish.md)
- [arena-tolerance-slsqp.md](../techniques/arena-tolerance-slsqp.md)
- [uniform-radius-shrink-fallback.md](../techniques/uniform-radius-shrink-fallback.md)
- [mpmath-ulp-polish.md](../techniques/mpmath-ulp-polish.md)

## Findings
- [packing-techniques.md](../findings/packing-techniques.md)
- [arena-proximity-guard.md](../findings/arena-proximity-guard.md)

## References
- Packomania circle-packing database (Specht).
- Erich Friedman, packing references.

## Private tracking
For owner's reference: `mb/tracking/problem-14-circle-packing-square/` contains the 10-approach parallel basin survey. Not part of the public artifact.
