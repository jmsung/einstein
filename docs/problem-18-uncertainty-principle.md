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
- `scripts/uncertainty/k14_polish.py` — hybrid-verified hillclimb on k=14 solutions
- `scripts/uncertainty/k15_climb.py` — k=15 parallel multi-start climb from k=14 base
- `scripts/uncertainty/k15_broad.py` — k=15 broad search with short CMA-ES runs
- `scripts/uncertainty/k15_parallel_cma.py` — k=15 parallel CMA-ES with smooth penalty
- `scripts/uncertainty/k15_deep_parallel.py` — k=15 deep refine with CMA-ES phases
- `scripts/uncertainty/k15_refine.py` — k=15 deep CMA-ES + hillclimb refinement
- `scripts/uncertainty/submit.py` — arena submission script

## References

- Problem 9 in the arena (API ID 9)
- Laguerre polynomial combination with α = -1/2
- Solution format: `{"laguerre_double_roots": [z1, z2, ..., zk]}`

*Last updated: 2026-04-09*
