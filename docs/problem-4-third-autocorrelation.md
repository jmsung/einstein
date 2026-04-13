# Problem 4: Third Autocorrelation Inequality (Upper Bound)

**Status**: JSAgent **#1**

## Problem

For f: [-1/4, 1/4] → ℝ (possibly signed), define the autoconvolution f ⋆ f. The third autocorrelation constant is

C(f) = |max_t (f ⋆ f)(t)| / (∫f)²

The arena task is to find f minimizing C(f). Unlike the first autocorrelation inequality, f is allowed to take negative values, enabling destructive interference in the autoconvolution and lower constants. This is variant (b) of Problem 6.4 in the AlphaEvolve paper.

## Arena Details

- **API ID**: 4
- **Direction**: minimize
- **Solution format**: `{"values": [floats]}` — discretized f
- **Scoring**: `abs(np.convolve(f,f).max() * dx) / (np.sum(f) * dx)**2`
- **minImprovement**: 1e-4

## Approach

### Strategy Overview

The breakthrough was recognizing the **equioscillation trap** at fixed n and escaping it by going to larger n via **block-repeat initialization**.

### The Equioscillation Trap

At a fixed discretization level n, the optimal solution develops an equioscillation pattern — multiple values of the autoconvolution are simultaneously near the maximum, creating a balanced stress network. With 15+ active constraints, the basin becomes fully rigid and no local move can improve the objective.

### Larger-n Escape via Block-Repeat

The escape technique:
1. Take the best solution at n = 400
2. Block-repeat each value to create an n = 1600 solution (each value repeated 4x)
3. Add small Gaussian noise to break the exact equioscillation pattern
4. Optimize at n = 1600 with L-BFGS using a LogSumExp smooth-max surrogate
5. The higher resolution permits finer adjustments that escape the equioscillation lock

This produced a 1.52 × 10⁻³ improvement — well above the minImprovement gate.

### Smooth-Max Surrogate (L-BFGS + LogSumExp)

The `max` in the objective is non-differentiable. We replace it with LogSumExp: max(v) ≈ (1/β) log Σ exp(β · v_i). A **beta cascade** (1e4 → 1e10) is essential — low β gives a smooth landscape for finding the right neighborhood, high β recovers the true objective for precision.

### Verification

The final score is verified with three independent implementations before submission:
- `np.convolve` (exact direct convolution)
- `scipy.signal.fftconvolve` (FFT-based)
- Direct O(n²) loop

If any two disagree, the improvement is rejected.

### What Worked

- **Block-repeat + noise** — breaks equioscillation lock by introducing new degrees of freedom
- **Beta cascade** — essential for smooth-max surrogates; jumping directly to high β gets trapped
- **Triple verification** — prevents phantom scores from numerical artifacts

### What Didn't Work

- **Direct optimization at fixed n** — equioscillation lock prevents any improvement once the trap forms
- **Random restarts at fixed resolution** — all converge to the same equioscillation pattern
- **Small perturbations of equioscillated solution** — the stress network absorbs them

## Key Insights

- **Equioscillation is a universal trap**: For piecewise-constant discretized functions, optimizers inevitably find an equioscillation pattern that locks the basin. Recognizing this is the first step to escaping.
- **Piecewise-constant discretization is the bottleneck**: Solution quality is limited by the discretization, not the basin. Going to larger n with block-repeat initialization provides new degrees of freedom.
- **Block-repeat + noise is a general escape technique**: This transfers to any discretized-function problem where equioscillation traps form at fixed resolution.
- **JSAgent improved below AlphaEvolve's bound**: AlphaEvolve reported C'_{6.4} ≤ 1.4557; JSAgent pushed below this to hold rank #1.

## Results

JSAgent improved the upper bound below the AlphaEvolve paper's reported C'_{6.4} ≤ 1.4557 for this variant and currently holds rank #1.

## References

- Tao et al., *Mathematical exploration and discovery at scale* ([arXiv:2511.02864](https://arxiv.org/abs/2511.02864)), Problem 6.4 (variant b).
- de Dios Pont & Madrid, *On classical inequalities for autocorrelations and autoconvolutions* ([arXiv:2106.13873](https://arxiv.org/abs/2106.13873)).
- Matolcsi & Vinuesa (2009) — improved bounds on autocorrelation inequalities ([arXiv:0907.1379](https://arxiv.org/abs/0907.1379)).

## Infrastructure

- `src/einstein/third_autocorrelation/evaluator.py` — exact arena-matching evaluator
- `src/einstein/third_autocorrelation/optimizer.py` — shared surrogate / autograd helpers
- `scripts/third_autocorrelation/optimize_torch.py` — direct-conv optimizer entry point
- `scripts/third_autocorrelation/optimize_fft.py` — FFT-conv optimizer entry point
- `scripts/third_autocorrelation/submit.py` — pre-flight check, triple verification, and blocking leaderboard poll

*Last updated: 2026-04-13*
