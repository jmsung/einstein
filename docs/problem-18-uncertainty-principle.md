# Problem 18: Uncertainty Principle

**Status**: JSAgent **#1**

## Problem

Minimize S = largest_sign_change / (2π) of a Laguerre polynomial combination.

Given a set of "double roots" z₁, ..., zₖ (positive reals ≤ 300), construct a specific Laguerre polynomial combination g(x) and find its largest sign-changing root. Lower S is better.

## Our Result

- **Rank**: #1 on the arena leaderboard

## Approach

1. **Two-tier verification**: fast numerical evaluator for optimization loop, exact symbolic verifier as quality gate
2. **Multi-strategy optimization**: multiple strategies with adaptive selection
3. **Far sign-change detection**: scanning beyond the dense grid to catch hidden sign changes

## Key Findings

- Landscape is extremely deceptive — optimizers report fake improvements without exact verification
- Specific root structure matters — not all configurations are equal
- Hidden sign changes far from the root cluster can invalidate apparently good solutions

## Infrastructure

- `src/einstein/uncertainty/verifier.py` — exact symbolic verifier (sympy)
- `src/einstein/uncertainty/fast.py` — fast numerical evaluator (mpmath + numpy)
- `src/einstein/uncertainty/hybrid.py` — hybrid evaluator (sympy polynomial + numpy root-finding)
- `scripts/uncertainty/optimize_loop.py` — adaptive optimization loop
- `scripts/uncertainty/exact_hillclimb.py` — exact hill-climbing optimizer
- `scripts/uncertainty/k_climb_optimizer.py` — k-climb optimizer
- `scripts/uncertainty/submit.py` — arena submission script

## References

- Problem 9 in the arena (API ID 9)
- Laguerre polynomial combination with α = -1/2
- Solution format: `{"laguerre_double_roots": [z1, z2, ..., zk]}`

*Last updated: 2026-04-04*
