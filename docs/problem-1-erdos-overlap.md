# Problem 1: Erdős Minimum Overlap

## Problem

Find a step function h: [0, 2] → [0, 1] with ∫h = 1 that minimizes the overlap integral:

C = max_k ∫ h(x)(1 − h(x+k)) dx

## Background

The Erdős minimum overlap problem (1955) asks for the constant c = lim M(n)/n, where M(n) is the minimum over all equal partitions {A, B} of {1,...,2n} of max_k |{(a,b): a−b=k}|.

The continuous relaxation via Swinnerton-Dyer uses density functions h on [0,2]. Step functions give upper bounds on c.

**Current bounds**: 0.379005 < c < 0.380871 (gap ≈ 0.002).

## Key References

- Erdős (1955) — original problem formulation
- White (2022) — lower bound 0.379 via Fourier analysis ([arXiv:2201.05704](https://arxiv.org/abs/2201.05704))
- Haugland (2016) — 51-piece upper bound ([arXiv:1609.08000](https://arxiv.org/abs/1609.08000))
- AlphaEvolve (2025) — 95-piece construction ([arXiv:2511.02864](https://arxiv.org/abs/2511.02864))

## Arena Details

- **API ID**: 1
- **Direction**: minimize
- **Solution format**: `{"values": [floats]}` — discretized h
- **Scoring**: `max(correlate(h, 1−h, 'full')) × (2/n)`
- **minImprovement**: 1e-6

## Approach

Gradient-based optimization on discretized step functions with cross-correlation scoring. A warm-start pipeline polishes the best known SOTA solution using multi-point mass transport and dyadic mass transport (zero-sum perturbations that preserve ∫h = 1).

## Infrastructure

- `src/einstein/erdos/evaluator.py` — exact overlap evaluator
- `src/einstein/erdos/fast.py` — fast numerical evaluator used by the optimization loop
- `scripts/erdos/optimize_erdos.py` — main optimizer entry point
- `scripts/erdos/optimize_warmstart.py` — warm-start polisher (multi-point + dyadic mass transport)
- `scripts/erdos/submit.py` — arena submission script with pre-submission checklist

*Last updated: 2026-04-05*
