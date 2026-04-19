# Problem 3: Second Autocorrelation Inequality (Lower Bound)

**Status**: JSAgent **#1**

## Problem

Maximize C = ‖f ⋆ f‖₂² / (‖f ⋆ f‖₁ · ‖f ⋆ f‖∞) where f ≥ 0.

Higher C means a tighter lower bound on the inequality. No upper bound below C = 1 is known. This is Problem 6.3 of arXiv:2511.02864.

## Arena Details

- **API ID**: 3
- **Direction**: maximize
- **Solution format**: `{"values": [floats]}` — discretized f (non-negative)
- **Scoring**: ‖f ⋆ f‖₂² / (‖f ⋆ f‖₁ · ‖f ⋆ f‖∞)
- **minImprovement**: 1e-4

## Approach

### Strategy Overview

The breakthrough came from two key ideas: (1) treating this as a **Dinkelbach fractional program** rather than direct ratio optimization, and (2) discovering that different discretization resolutions access fundamentally different basins via **cross-resolution basin transfer**.

### Dinkelbach Fractional Programming

The ratio objective C = N/D is converted to a parametric problem: maximize N − λD, updating λ iteratively. This turns the non-convex ratio into a sequence of simpler subproblems.

- **Beta cascade**: The LogSumExp approximation to max uses a temperature parameter β. Starting at low β (≈1e4) gives a smooth landscape for global search; cascading to high β (≈1e10) sharpens to the true objective. Jumping directly to high β gets trapped.
- **w² parameterization**: Optimize w where f = w², enforcing non-negativity without explicit constraints. Gradients flow through naturally via the chain rule.
- **Adam optimizer**: Adam's per-coordinate adaptive learning rate naturally concentrates updates on the highest-magnitude coordinates (peaks), effectively discovering sparse block structure without being told to look for it.

### Cross-Resolution Basin Transfer

The key breakthrough: optimizing at high resolution (n ≈ 1.6M) then compressing to the target resolution (n ≈ 100k) via block averaging creates a starting point in a *different basin* than what native 100k optimization finds from scratch.

High-resolution optimization discovers fine structure that, when averaged down, preserves low-frequency features otherwise unreachable at the target resolution.

### What Worked

- **Dinkelbach with beta cascade** — the right framework for ratio objectives
- **Cross-resolution transplant** — high-res → low-res block averaging breaks out of the native basin
- **w² parameterization** — clean non-negativity with good gradient flow
- **Triple verification** — three independent scoring methods agree to 1e-12

### What Didn't Work

- **Direct ratio optimization** — landscape is poorly conditioned when optimizing N/D directly
- **Single-resolution from-scratch** — converges to suboptimal basin at every fixed n
- **Low-frequency Fourier regularization** — hurts performance because the optimal solution has spiky high-frequency structure

## Key Insights

- **Ratio objectives need Dinkelbach**: Direct optimization of N/D ratios is poorly conditioned. The Dinkelbach parameterization (N − λD) with iterative λ update is dramatically more effective.
- **Resolution creates different basins**: n is not just a discretization parameter — different values of n access fundamentally different solution basins. Always explore multiple resolutions.
- **Beta cascade is essential**: For LogSumExp smooth-max surrogates, a low-to-high β cascade avoids trapping. This lesson transfers to any problem using smooth approximations to max/min.
- **Adam discovers structure**: Adam's adaptive learning rates naturally find sparse block structure, concentrating perturbations on the peaks that matter most.

## References

- Jaech & Joseph (arXiv:2508.02803) — Adam optimizer approach for autoconvolution
- Boyer & Li (arXiv:2506.16750) — Analytical construction
- Martin & O'Bryant (arXiv:0807.5121) — Sidon set connection
- Rechnitzer (arXiv:2602.07292) — High-precision dual minimizer

## Infrastructure

- `src/einstein/autocorrelation/evaluator.py` — arena-matching evaluator (70 tests)
- `src/einstein/autocorrelation/fast.py` — FFT evaluator (100x+ speedup)
- `scripts/autocorrelation/dinkelbach_mps.py` — Dinkelbach optimizer (Apple MPS GPU)
- `scripts/autocorrelation/dinkelbach_cpu_v2.py` — Dinkelbach optimizer (CPU)
- Verification: 3 independent scoring methods agree to 1e-12

*Last updated: 2026-04-13*
