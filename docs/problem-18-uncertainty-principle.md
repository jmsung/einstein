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

- `src/einstein/verifier.py` — exact symbolic verifier (sympy)
- `src/einstein/fast_eval.py` — fast numerical evaluator (mpmath + numpy)
- `scripts/optimize_loop.py` — adaptive optimization loop

## References

- Problem 9 in the arena (API ID 9)
- Laguerre polynomial combination with α = -1/2
- Solution format: `{"laguerre_double_roots": [z1, z2, ..., zk]}`

*Last updated: 2026-03-31*
