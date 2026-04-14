# Problem 12: Flat Polynomials (degree 69)

**Status**: JSAgent #9 (score 1.3539)

## Problem

Find 70 coefficients in {+1, −1} defining a degree-69 polynomial p(z) that minimizes:

C⁺ = max|p(z)| / √71

evaluated at 10⁶ equally-spaced points on the unit circle |z| = 1.

## Background

Littlewood polynomials have all coefficients in {+1, −1}. The "flatness" problem asks how close max|p(z)| can get to its L₂ norm √(n+1) on the unit circle. By Parseval's theorem, ‖p‖₂ = √70 for 70 coefficients, so the ratio max|p(z)|/√71 has a theoretical lower bound near √70/√71 ≈ 0.993.

Balister et al. (2019) proved that flat Littlewood polynomials exist for all degrees, confirming Littlewood's 1966 conjecture. Whether "ultraflat" polynomials (ratio → 1) exist for ±1 coefficients remains open (Erdős 1957).

## Arena Details

- **API ID**: 12
- **Direction**: minimize
- **Solution format**: `{"coefficients": [70 × ±1]}` (descending degree, np.poly1d convention)
- **Scoring**: `max|p(z)| / √71` at 10⁶ unit circle points
- **minImprovement**: 1e-5

## Approach

### Strategy Overview

A discrete combinatorial search over the 2⁷⁰ binary coefficient space, seeded with algebraic constructions and refined via Memetic Tabu Search (MTS).

### Algebraic Constructions as Warm-Starts

Seven distinct construction families provide starting points across different regions of the search space:

- **Turyn (shifted Fekete)**: Cyclic shifts of Fekete polynomials — best known asymptotic Mahler measure
- **Fekete (Legendre symbol)**: Natural degree-(p−1) polynomials for prime p with good flatness
- **Rudin-Shapiro**: Achieves max|p(z)| ≤ √2 · √(n+1) at power-of-2 degrees (ratio ≤ 1.414)
- **CRT tensor products**: Chinese Remainder Theorem compositions
- **Kloosterman sum**: Number-theoretic constructions from exponential sums
- **Sidelnikov**: From difference sets in finite fields
- **Period-3**: Simple periodic constructions as baselines

### Memetic Tabu Search (MTS)

The primary optimizer: combines tabu search (short-term memory preventing recent flips) with local hill-climbing. Each iteration flips the coefficient that most improves the score, maintaining a tabu list to avoid cycling.

Multi-resolution evaluation speeds up the search: coarse evaluation (fewer unit circle points) for screening, full 10⁶-point evaluation for verification.

### What Worked

- **MTS campaign** — independently discovered score 1.3539
- **Construction diversity** — 7 families seed different regions of the 2⁷⁰ space
- **Multi-resolution evaluation** — fast screening + exact verification

### What Didn't Work

- **Reaching SOTA** — gap from our 1.3539 to SOTA 1.2809 suggests a fundamentally different construction or much larger search
- **Simple SA/GA** — outperformed by MTS for this discrete binary landscape

## Key Insights

- **Binary search spaces are vast but structured**: 2⁷⁰ ≈ 10²¹ is far too large for exhaustive search, but algebraic constructions provide footholds in good regions.
- **Tabu search outperforms SA/GA for binary problems**: The short-term memory mechanism prevents cycling and enables deeper exploration of local neighborhoods.
- **The gap to SOTA is significant**: 1.3539 vs 1.2809 suggests the top solutions use fundamentally different constructions or significantly more compute.

## References

- Balister et al. (2019) — Flat Littlewood polynomials exist ([arXiv:1907.09464](https://arxiv.org/abs/1907.09464))
- Mossinghoff (2024) — Turyn polynomials and Mahler's problem ([arXiv:2405.08281](https://arxiv.org/abs/2405.08281))
- Jedwab, Katz, Schmidt (2013) — Small L₄ norm Littlewood polynomials ([arXiv:1205.0260](https://arxiv.org/abs/1205.0260))
- AlphaEvolve (2025) — Mathematical exploration at scale ([arXiv:2511.02864](https://arxiv.org/abs/2511.02864))

## Infrastructure

- `src/einstein/flat_poly/evaluator.py` — evaluator, 7 constructions, SA/GA/Tabu/MTS optimizers
- `tests/flat_poly/test_flat_poly.py` — 70 tests (constraints, scoring, math properties, constructions, optimizers)
- `scripts/flat_poly/optimize_flat_poly.py` — MTS campaign with multi-resolution evaluation

*Last updated: 2026-04-13*
