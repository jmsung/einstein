# Problem 2: First Autocorrelation Inequality (Upper Bound)

**Status**: **Rank #1** — C = 1.502861628 (Δ = 1.23e-6 below previous SOTA)

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

### What Worked (Breakthrough)

- **Square parameterization** (f = v²) instead of log-space (f = exp(v)) — accesses a fundamentally different optimization landscape. The v² parameterization allows exact zeros and has different gradient structure, escaping local minima that trap the exp parameterization.
- **n=90000 sweet spot** — block-repeat SOTA 3× to n=90000, then optimize with v². This specific resolution maximizes improvement from the square parameterization.
- **Ultra-aggressive L-BFGS** — very long optimization at LOW beta (1e6-1e7) with large history_size=300 and max_iter=3000. The ~6 minute exploration at low beta finds deeper basins before tightening.

### What Didn't Work

- **LP scaling at large n** — cutting-plane LP scales linearly at n ≈ 200 but diverges at n ≈ 30,000. The constraint count grows faster than the solver can handle.
- **FOSS LP solver cross-over** — open-source solvers (HiGHS) stall in the n ≈ 2,000-5,000 regime where commercial solvers (MOSEK, Gurobi) would be needed.
- **ULP-scale random polish** — at the precision floor, random perturbations have negligible probability of finding improvement.
- **Exp parameterization at any n** — L-BFGS with f=exp(v) converges to Δ≈5.25e-8 at all tested resolutions (30k-300k), well below the 1e-7 minImprovement gate.
- **Adam/SGD optimizers** — much worse than L-BFGS for this problem.
- **Multi-peak polish** — subgradient descent on the exact objective couldn't escape the L-BFGS local minimum due to peak-locking (Jaech & Joseph, 2025).
- **Random starts / CMA-ES** — couldn't find competitive basins at any resolution.

## Key Insights

- **Parameterization matters more than resolution**: The square parameterization (f=v²) escapes local minima that trap the exp parameterization (f=exp(v)) at every resolution tested. This is the single most important finding.
- **Peak-locking**: Gradient methods on the first autocorrelation inequality suffer from "peak-locking" (Jaech & Joseph, 2025) — the current argmax of the autoconvolution is reinforced during optimization. The v² parameterization mitigates this.
- **Resolution sweet spots**: n=90000 (3× block-repeat of 30000) is the optimal resolution for square-param optimization. Larger n gives diminishing returns due to optimization difficulty.
- **Low-beta exploration is critical**: Extended L-BFGS at low beta (1e6-1e7) with large history explores the landscape broadly before tightening. This ~6 minute exploration phase at β=1e6 found a basin 12× deeper than the threshold.

## References

- AlphaEvolve (2025) — discovered constructions for autocorrelation problems ([arXiv:2511.02864](https://arxiv.org/abs/2511.02864))
- TTT-Discover (2026) — test-time training for mathematical discovery ([arXiv:2601.16175](https://arxiv.org/abs/2601.16175))
- Matolcsi & Vinuesa (2009) — improved bounds on the first autocorrelation inequality ([arXiv:0907.1379](https://arxiv.org/abs/0907.1379))
- Cloninger & Steinerberger (2017) — rigorous lower bound C ≥ 1.28 ([arXiv:1403.7988](https://arxiv.org/abs/1403.7988))
- Jaech & Joseph (2025) — peak-locking in autoconvolution optimization ([arXiv:2508.02803](https://arxiv.org/abs/2508.02803))
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
- `scripts/first_autocorrelation/mega_optimize.py` — multi-phase optimizer (square param + resolution sweep)
- `tests/first_autocorrelation/test_evaluator.py` — evaluator parity tests

*Last updated: 2026-04-15*
