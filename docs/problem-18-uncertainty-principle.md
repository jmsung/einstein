# Problem 18: Uncertainty Principle

**Status**: JSAgent **#1** — S=0.3183526317

## Problem

Minimize S = largest_sign_change / (2π) of a Laguerre polynomial combination.

Given a set of "double roots" z₁, ..., zₖ (positive reals ≤ 300), construct a specific Laguerre polynomial combination g(x) and find its largest sign-changing root. Lower S is better.

## Our Result

- **Score**: S=0.31835 with k=13 roots
- **Previous SOTA**: S=0.31885 (REDACTED)
- **Improvement**: -0.00050 (lower is better)

## Approach

1. **Two-tier verification**: fast numerical evaluator (mpmath + numpy) for optimization loop, exact symbolic verifier (sympy) as quality gate
2. **Multi-phase hillclimb**: coordinate-wise perturbation → random multi-coordinate → fine polish → try k+1
3. **Adaptive step sizes**: per-coordinate steps that shrink on convergence
4. **Far sign-change detection**: exponential scan beyond the dense grid to catch hidden sign changes at x >> max(roots)

## Key Findings

- Landscape is extremely deceptive — optimizers report fake improvements without exact verification
- Specific root structure matters — not all configurations are equal
- Nelder-Mead thrives on this non-smooth landscape; gradient methods fail
- Hidden sign changes far from the root cluster can invalidate apparently good solutions

## Infrastructure

- `src/einstein/verifier.py` — exact symbolic verifier (sympy)
- `src/einstein/fast_eval.py` — fast numerical evaluator (mpmath + numpy)
- `scripts/optimize.py` — hillclimb optimizer

## References

- Problem 9 in the arena (API ID 9)
- Laguerre polynomial combination with α = -1/2
- Solution format: `{"laguerre_double_roots": [z1, z2, ..., zk]}`

*Last updated: 2026-03-30*
