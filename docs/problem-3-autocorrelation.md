# Problem 3: Second Autocorrelation Inequality


**Status**: JSAgent **#1** — C=0.9622135366

## Problem

Maximize $C = \|f \star f\|_2^2 / (\|f \star f\|_1 \cdot \|f \star f\|_\infty)$ where $f \geq 0$.

Higher C means a tighter lower bound on the inequality. No upper bound below C=1 is known.

## Our Result

- **Score**: C=0.96221 at n=100,000
- **Previous SOTA**: C=0.96199 (ClaudeExplorer)
- **Best published academic result**: C=0.941 (Jaech & Joseph, arXiv:2508.02803)
- **Reference**: Problem 6.3 of arXiv:2511.02864

## Approach

1. **Literature review**: 6 key papers studied, 5 optimization recipes extracted
2. **Breadth-first exploration**: 11 experiments across 5 methods (Adam, Dinkelbach, deautoconvolution, Fourier projections, Chebyshev basis)
3. **GPU optimization**: CUDA float64 Dinkelbach on cloud GPUs
4. **Novel basin discovery**: technique that escaped the known local maximum

## Key Findings

- The n=100k basin at C=0.96199 is a proven local maximum (Hessian all-negative)
- Resolution is non-monotonic: different n values have different basins
- From-scratch optimization caps at C≈0.916 regardless of method
- The 0.96+ barrier requires starting from a specific irregular block structure
- Adam with peak-flattening gradient naturally discovers sparse block structure

## Infrastructure

- `src/einstein/autocorrelation.py` — arena-matching evaluator (70 tests)
- `src/einstein/autocorrelation_fast.py` — FFT evaluator (100x+ speedup)
- `scripts/` — multiple optimization approaches
- Verification: 3 independent scoring methods agree to 1e-12

## References

- Jaech & Joseph (arXiv:2508.02803) — Adam optimizer, C=0.941
- Boyer & Li (arXiv:2506.16750) — Analytical construction, C=0.902
- Martin & O'Bryant (arXiv:0807.5121) — Sidon set connection
- Rechnitzer (arXiv:2602.07292) — 128-digit dual minimizer
- ClaudeExplorer (github.com/justinkang221/second-autocorrelation-inequality) — Open-source Dinkelbach

*Last updated: 2026-03-30*
