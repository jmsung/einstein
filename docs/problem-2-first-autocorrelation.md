# Problem 2: First Autocorrelation Inequality (Upper Bound)

**Status**: No submission (below minImprovement gate)

## Problem

For non-negative f supported on [-1/4, 1/4], define the autoconvolution f ⋆ f. The first autocorrelation constant is

C(f) = max_x (f ⋆ f)(x) / (∫f)²

The arena task is to find f minimizing C(f). Lower C means a tighter upper bound on the inequality. The current public best is ≈ 1.50286.

## Background

The problem has deep connections to additive combinatorics. Cloninger & Steinerberger (2017) proved C ≥ 1.28 rigorously. The gap between this lower bound and the best known upper bound (≈1.503) remains wide open, suggesting room for novel approaches.

## Arena Details

- **API ID**: 2
- **Direction**: minimize
- **Solution format**: `{"values": [floats]}` — discretized f
- **minImprovement**: checked at submission time

## Approach

### Strategy Overview

A multi-pronged attack combining FFT-backed smooth surrogates with linear programming and Frank-Wolfe methods. The problem proved harder to crack than expected — LP scaling limits and basin structure prevented reaching a competitive submission.

### Optimization Techniques

- **FFT-backed surrogate**: O(n log n) autoconvolution via `scipy.signal.fftconvolve`, enabling fast gradient-based iteration.
- **L-BFGS cascade**: Multi-restart L-BFGS on the smooth surrogate with varying initial conditions and resolution levels.
- **Cutting-plane LP**: Linear programming formulation with iterative constraint generation via CVXPY — solves a relaxation and adds violated constraints each round.
- **Pairwise Frank-Wolfe**: Away-step / pairwise Frank-Wolfe (Lacoste-Julien & Jaggi 2015) for simplex-constrained optimization, explored as a replacement for cutting-plane LP at large n.
- **Basin-break cycling**: Cycle through different n values (discretization resolution) to escape local optima — different resolutions sometimes access different basins.

### What Worked

- **FFT evaluator** — 100x+ speedup enables rapid iteration at high resolution
- **LP formulation at small n** — cutting-plane converges cleanly at n ≈ 200
- **Multi-resolution cycling** — changing n sometimes escapes local basins

### What Didn't Work

- **LP scaling at large n** — cutting-plane LP scales linearly at n ≈ 200 but diverges at n ≈ 30,000. The constraint count grows faster than the solver can handle.
- **FOSS LP solver cross-over** — open-source solvers (HiGHS) stall in the n ≈ 2,000-5,000 regime where commercial solvers (MOSEK, Gurobi) would be needed.
- **ULP-scale random polish** — at the precision floor, random perturbations have negligible probability of finding improvement.

## Key Insights

- **LP scaling wall**: Cutting-plane LP hits a fundamental scaling barrier at large n. The next step would be away-step Frank-Wolfe, not a bigger LP solver.
- **Resolution is a hyperparameter**: Different values of n lead to genuinely different basins. Treating discretization resolution as tunable is essential.
- **The gap persists**: The theoretical lower bound (1.28) and best upper bound (≈1.503) remain far apart — significant room for novel approaches exists.

## References

- AlphaEvolve (2025) — discovered constructions for autocorrelation problems ([arXiv:2511.02864](https://arxiv.org/abs/2511.02864))
- TTT-Discover (2026) — test-time training for mathematical discovery ([arXiv:2601.16175](https://arxiv.org/abs/2601.16175))
- Matolcsi & Vinuesa (2009) — improved bounds on the first autocorrelation inequality ([arXiv:0907.1379](https://arxiv.org/abs/0907.1379))
- Cloninger & Steinerberger (2017) — rigorous lower bound C ≥ 1.28 ([arXiv:1403.7988](https://arxiv.org/abs/1403.7988))
- Lacoste-Julien & Jaggi (2015) — pairwise / away-step Frank-Wolfe for simplex-constrained problems ([arXiv:1511.05932](https://arxiv.org/abs/1511.05932))

## Infrastructure

- `src/einstein/first_autocorrelation/evaluator.py` — exact arena-matching evaluator
- `src/einstein/first_autocorrelation/optimizer.py` — smooth surrogate + FFT autoconv helpers
- `scripts/first_autocorrelation/optimize_fft.py` — main L-BFGS cascade
- `scripts/first_autocorrelation/cycle_n.py` — cycle through n values for basin break
- `scripts/first_autocorrelation/alt_polish.py` — alternating cascade + multi-peak polish
- `scripts/first_autocorrelation/polish_lottery.py` — ulp-scale random polish
- `scripts/first_autocorrelation/pairwise_fw.py` — pairwise Frank-Wolfe diagnostic
- `scripts/first_autocorrelation/km_lp.py` — cutting-plane LP with CVXPY and block-averaging
- `tests/first_autocorrelation/test_evaluator.py` — evaluator parity tests

*Last updated: 2026-04-13*
