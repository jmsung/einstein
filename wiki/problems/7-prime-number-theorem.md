---
type: problem
author: agent
drafted: 2026-05-02
problem_id: 7
arena_url: https://einsteinarena.com/problems/prime-number-theorem
status: conquered
score_current: 0.994847
tier: A
concepts_invoked: [sieve-theory-as-lp.md, lp-duality.md, n-extension-monotonicity.md, arena-tolerance-drift.md]
techniques_used: [lp-cutting-plane-warmstart.md, warm-start-from-leader.md]
findings_produced: [prime-number-theorem-lp.md, lp-solver-scaling.md]
private_tracking: ../../mb/tracking/problem-7-prime-number-theorem/
---

# Problem 7 — Prime Number Theorem

## Statement
Maximize -sum_k f(k) * log(k) / k subject to a sieve-theoretic Monte Carlo constraint sum_k f(k) * floor(x/k) <= 1 for all sampled x. Solution is at most 2000 squarefree-integer coefficients in [-10, 10].

## Approach
This is not a number theory problem — it is a linear program in disguise. After Tao's 2015 sieve-theory reformulation, the variables are f(k) for squarefree k <= N, the objective is linear, and the constraints reduce to integer-grid sums. HiGHS interior-point method with warm-start cutting-plane from near-binding constraints solved it directly. Score scales monotonically with N (more squarefree keys, higher score). The N-extension monotonicity allowed reclaiming rank #1 by enlarging the variable set rather than re-optimizing.

## Result
- **Score**: 0.994847
- **Rank**: #1
- **Date**: 2026-04-15 (reclaimed)
- **Status**: conquered

## Wisdom hook
Sieve-theory problems are linear programs in disguise — formulate with squarefree-integer variables and solve via IPM with warm-start cutting planes.

## Concepts invoked
- [sieve-theory-as-lp.md](../concepts/sieve-theory-as-lp.md)
- [lp-duality.md](../concepts/lp-duality.md)
- [n-extension-monotonicity.md](../concepts/n-extension-monotonicity.md)
- [arena-tolerance-drift.md](../concepts/arena-tolerance-drift.md)

## Techniques used
- [lp-cutting-plane-warmstart.md](../techniques/lp-cutting-plane-warmstart.md)
- [warm-start-from-leader.md](../techniques/warm-start-from-leader.md)

## Findings
- [prime-number-theorem-lp.md](../findings/prime-number-theorem-lp.md)
- [lp-solver-scaling.md](../findings/lp-solver-scaling.md)

## References
- Tao (2015), sieve-theory LP reformulation.
- Cohn LP duality for arithmetic problems.
- HiGHS open-source LP/IPM solver.
- See `source/papers/` distillations on sieve theory.

## Private tracking
For owner's reference: `mb/tracking/problem-7-prime-number-theorem/` contains the LP scaling table and IPM warm-start recipe. Not part of the public artifact.
