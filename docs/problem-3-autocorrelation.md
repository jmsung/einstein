# Problem 3: Second Autocorrelation Inequality

**Status**: JSAgent **#1**

## Problem

Maximize $C = \|f \star f\|_2^2 / (\|f \star f\|_1 \cdot \|f \star f\|_\infty)$ where $f \geq 0$.

Higher C means a tighter lower bound on the inequality. No upper bound below C=1 is known.

## Our Result

- **Rank**: #1 on the arena leaderboard
- **Reference**: Problem 6.3 of arXiv:2511.02864

## Approach

1. **Literature review**: key papers studied, multiple optimization recipes extracted
2. **Breadth-first exploration**: experiments across multiple methods
3. **GPU optimization**: CUDA float64 on cloud GPUs
4. **Iterative refinement**: multi-resolution optimization

## Infrastructure

- `src/einstein/autocorrelation.py` — arena-matching evaluator (70 tests)
- `src/einstein/autocorrelation_fast.py` — FFT evaluator (100x+ speedup)
- `scripts/` — multiple optimization approaches
- Verification: 3 independent scoring methods agree to 1e-12

## References

- Jaech & Joseph (arXiv:2508.02803) — Adam optimizer approach
- Boyer & Li (arXiv:2506.16750) — Analytical construction
- Martin & O'Bryant (arXiv:0807.5121) — Sidon set connection
- Rechnitzer (arXiv:2602.07292) — High-precision dual minimizer

*Last updated: 2026-03-31*
