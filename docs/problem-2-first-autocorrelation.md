# Problem 2: First Autocorrelation Inequality (Upper Bound)

**Status**: research bet, no submission (below minImprovement gate)

## Problem

For non-negative $f$ supported on $[-1/4, 1/4]$, define the autoconvolution
$f \star f$. The first autocorrelation constant is

$$
C(f) = \frac{\max_x (f \star f)(x)}{\left(\int f\right)^2}
$$

The arena task is to find $f$ minimizing $C(f)$. Lower $C$ means a tighter upper
bound on the inequality. The current public best is $\approx 1.50286$.

## Approach

An arena-matching evaluator and an FFT-backed smooth surrogate are provided,
along with a small family of exploratory scripts (warm-start downloader,
L-BFGS cascade, basin-break cycling, polish refinement, linear-programming
iteration, bandlimit-Fourier variant). Detailed approach notes and experiment
history are kept in the private memory bank playbook.

## Infrastructure

- `src/einstein/first_autocorrelation/evaluator.py` — exact arena-matching evaluator
- `src/einstein/first_autocorrelation/optimizer.py` — smooth surrogate + FFT autoconv helpers
- `scripts/first_autocorrelation/optimize_fft.py` — main L-BFGS cascade
- `scripts/first_autocorrelation/cycle_n.py` — cycle through $n$ values for basin break
- `scripts/first_autocorrelation/alt_polish.py` — alternating cascade + multi-peak polish
- `scripts/first_autocorrelation/polish_lottery.py` — ulp-scale random polish
- `scripts/first_autocorrelation/pairwise_fw.py` — pairwise Frank-Wolfe diagnostic
- `tests/first_autocorrelation/test_evaluator.py` — evaluator parity tests

## References

- AlphaEvolve (2025) — discovered constructions for autocorrelation problems ([arXiv:2511.02864](https://arxiv.org/abs/2511.02864))
- TTT-Discover (2026) — test-time training for mathematical discovery ([arXiv:2601.16175](https://arxiv.org/abs/2601.16175))
- Matolcsi & Vinuesa (2009) — improved bounds on the first autocorrelation inequality ([arXiv:0907.1379](https://arxiv.org/abs/0907.1379))
- Cloninger & Steinerberger (2017) — rigorous lower bound $C \ge 1.28$ ([arXiv:1403.7988](https://arxiv.org/abs/1403.7988))
- Lacoste-Julien & Jaggi (2015) — pairwise / away-step Frank-Wolfe for simplex-constrained problems ([arXiv:1511.05932](https://arxiv.org/abs/1511.05932))

*Last updated: 2026-04-09*
