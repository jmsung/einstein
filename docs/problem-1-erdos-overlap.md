# Problem 1: Erdős Minimum Overlap

**Status**: JSAgent **#1**

## Problem

Find a step function h: [0, 2] → [0, 1] with ∫h = 1 that minimizes the overlap integral:

C = max_k ∫ h(x)(1 − h(x+k)) dx

## Background

The Erdős minimum overlap problem (1955) asks for the constant c = lim M(n)/n, where M(n) is the minimum over all equal partitions {A, B} of {1,...,2n} of max_k |{(a,b): a−b=k}|.

The continuous relaxation via Swinnerton-Dyer uses density functions h on [0,2]. Step functions give upper bounds on c.

**Current bounds**: 0.379005 < c < 0.380871 (gap ≈ 0.002).

## Arena Details

- **API ID**: 1
- **Direction**: minimize
- **Solution format**: `{"values": [floats]}` — discretized h
- **Scoring**: `max(correlate(h, 1−h, 'full')) × (2/n)`
- **minImprovement**: 1e-6

## Approach

### Strategy Overview

Gradient-based optimization on discretized step functions with cross-correlation scoring. The SOTA basin is unreachable from scratch — warm-starting from the best known solution is critical.

### Warm-Start Pipeline

1. Download top leaderboard solutions via `/api/solutions/best?problem_id=1`
2. Verify the downloaded solution reproduces the published score bit-exactly
3. Use the best solution as the seed for all subsequent optimization

### Optimization Techniques

- **Multi-point mass transport**: Zero-sum perturbations (Σ δ_i = 0) that preserve ∫h = 1. Moving mass between multiple points simultaneously explores neighborhoods that single-point moves miss.
- **Dyadic mass transport**: Structured perturbations at power-of-2 scales that explore the landscape hierarchically — pairs of equal-and-opposite adjustments at varying resolution.
- **Cross-correlation scoring**: Fast O(n log n) scoring via FFT-based cross-correlation, matching the arena formula.

### What Worked

- **Warm-starting from SOTA** — the published basin is deep and stable
- **Multi-point mass transport** — finds improvements that single-point moves miss
- **Triple verification** (fast evaluator, exact reimplementation, cross-check) prevents phantom scores

### What Didn't Work

- **From-scratch optimization** — converges to suboptimal local minima far from the SOTA basin
- **Simple gradient descent** — the landscape is extremely flat near the optimum; improvements are at the float64 precision floor

## Key Insights

- **Float64 precision floor**: The mathematical optimum within the SOTA basin projects onto many near-equivalent float64 representations. All progress is in the last few ULPs of precision.
- **Warm-start is essential**: The SOTA basin is unreachable from random initialization. Always start from published solutions.
- **The gap is tiny**: The best known upper bound (≈0.3809) is within 0.002 of the lower bound (0.379), suggesting the true constant c is nearly pinned down.

## References

- Erdős (1955) — original problem formulation
- White (2022) — lower bound 0.379 via Fourier analysis ([arXiv:2201.05704](https://arxiv.org/abs/2201.05704))
- Haugland (2016) — 51-piece upper bound ([arXiv:1609.08000](https://arxiv.org/abs/1609.08000))
- AlphaEvolve (2025) — 95-piece construction ([arXiv:2511.02864](https://arxiv.org/abs/2511.02864))

## Infrastructure

- `src/einstein/erdos/evaluator.py` — exact overlap evaluator
- `src/einstein/erdos/fast.py` — fast numerical evaluator used by the optimization loop
- `scripts/erdos/optimize_erdos.py` — main optimizer entry point
- `scripts/erdos/optimize_warmstart.py` — warm-start polisher (multi-point + dyadic mass transport)
- `scripts/erdos/submit.py` — arena submission script with pre-submission checklist

*Last updated: 2026-04-13*
