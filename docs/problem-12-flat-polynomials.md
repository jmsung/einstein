# Problem 12: Flat Polynomials (degree 69)

## Problem

Find 70 coefficients in {+1, −1} defining a degree-69 polynomial p(z) that minimizes:

C⁺ = max|p(z)| / √71

evaluated at 10⁶ equally-spaced points on the unit circle |z| = 1.

## Background

Littlewood polynomials have all coefficients in {+1, −1}. The "flatness" problem asks how close max|p(z)| can get to its L₂ norm √(n+1) on the unit circle. By Parseval's theorem, ||p||₂ = √70 for 70 coefficients, so the ratio max|p(z)|/√71 has a theoretical lower bound near √70/√71 ≈ 0.993.

Balister et al. (2019) proved that flat Littlewood polynomials exist for all degrees, confirming Littlewood's 1966 conjecture. Whether "ultraflat" polynomials (ratio → 1) exist for ±1 coefficients remains open (Erdős 1957).

## Key Constructions

- **Rudin-Shapiro**: Achieves max|p(z)| ≤ √2 · √(n+1) at power-of-2 degrees. Ratio ≤ √2 ≈ 1.414.
- **Fekete (Legendre symbol)**: For prime p, gives natural degree-(p−1) polynomials with good flatness properties.
- **Turyn (shifted Fekete)**: Cyclic shifts of Fekete polynomials achieve best known asymptotic Mahler measure.

## Arena Details

- **API ID**: 12
- **Direction**: minimize
- **Solution format**: `{"coefficients": [70 × ±1]}` (descending degree, np.poly1d convention)
- **Scoring**: `max|p(z)| / √71` at 10⁶ unit circle points
- **minImprovement**: 1e-5

## Key References

- Balister et al. (2019) — Flat Littlewood polynomials exist ([arXiv:1907.09464](https://arxiv.org/abs/1907.09464))
- Mossinghoff (2024) — Turyn polynomials and Mahler's problem ([arXiv:2405.08281](https://arxiv.org/abs/2405.08281))
- Jedwab, Katz, Schmidt (2013) — Small L₄ norm Littlewood polynomials ([arXiv:1205.0260](https://arxiv.org/abs/1205.0260))
- AlphaEvolve (2025) — Mathematical exploration at scale ([arXiv:2511.02864](https://arxiv.org/abs/2511.02864))

## Our Result

- **Rank**: #8 on the arena leaderboard
- **Score**: 1.3539 (independently discovered via Memetic Tabu Search)
- **SOTA**: 1.2809 — proven 4-flip local optimum, likely global optimum for n=70

## Infrastructure

- `src/einstein/flat_poly.py` — evaluator, 7 constructions (Turyn, Fekete, RS, CRT, Kloosterman, Sidelnikov, period-3), SA/GA/Tabu/MTS optimizers
- `tests/test_flat_poly.py` — 70 tests (constraints, scoring, math properties, constructions, optimizers)
- `scripts/optimize_flat_poly.py` — MTS campaign with multi-resolution evaluation
- `scripts/modal_flat_poly.py` — GPU-accelerated parallel tabu search (Modal A100)

*Last updated: 2026-04-02*
