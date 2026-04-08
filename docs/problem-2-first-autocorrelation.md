# Problem 2: First Autocorrelation Inequality (Upper Bound)

**Status**: research bet, no submission

## Problem

For non-negative $f$ supported on $[-1/4, 1/4]$, define the autoconvolution
$f \star f$. The first autocorrelation constant is

$$
C(f) = \frac{\max_x (f \star f)(x)}{\left(\int f\right)^2}
$$

The arena task is to find $f$ minimizing $C(f)$. Lower $C$ means a tighter upper
bound on the inequality. The current public best (Together-AI) is $\approx 1.50286$.

## Approach

Explored several published methods against downloaded warm-start solutions; no
submission landed within the time budget for this branch. Work is parked as
scaffolding (evaluator + parity tests) plus a public docs entry, ready to
resume when a new angle appears.

## Infrastructure

- `src/einstein/first_autocorrelation/evaluator.py` — exact arena-matching evaluator
- `scripts/first_autocorrelation/` — leaderboard download and submission scripts
- `tests/first_autocorrelation/test_evaluator.py` — evaluator parity tests

## References

- AlphaEvolve (2025) — discovered constructions for autocorrelation problems ([arXiv:2511.02864](https://arxiv.org/abs/2511.02864))
- TTT-Discover (2026) — test-time training for mathematical discovery ([arXiv:2601.16175](https://arxiv.org/abs/2601.16175))
- Matolcsi & Vinuesa (2009) — improved bounds on the first autocorrelation inequality ([arXiv:0907.1379](https://arxiv.org/abs/0907.1379))

*Last updated: 2026-04-07*
