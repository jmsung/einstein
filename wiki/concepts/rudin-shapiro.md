---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P12]
related_techniques: [memetic-tabu-search.md]
related_findings: [discrete-optimization.md]
related_personas: [gauss.md, euler.md, ramanujan.md]
cites:
  - sidon-sets.md
  - parameterization-selection.md
  - ../source/papers/2020-balister-flat-littlewood.md
---

# Rudin–Shapiro polynomials

## TL;DR

The **Rudin–Shapiro polynomials** are a recursively-defined family of `±1`-coefficient polynomials with provably *small* sup-norm on the unit circle — specifically `‖P_n‖_∞ ≤ √(2(n+1))` for the n-th member. They're the canonical *constructive* family for "flat" Littlewood polynomials (P12's problem class), giving the asymptotic ratio `‖P‖_∞ / √n → √2`. The arena's P12 SOTA at 1.2809 is BELOW this asymptotic bound — it's a *computer-search-discovered* configuration past Rudin–Shapiro, found via memetic tabu search and likely matching the theoretical Erdős–Littlewood lower bound for finite n.

## What it is

The Rudin–Shapiro family `(P_n, Q_n)` is defined recursively:

- `P_0(z) = Q_0(z) = 1`
- `P_{n+1}(z) = P_n(z) + z^{2^n} Q_n(z)`
- `Q_{n+1}(z) = P_n(z) − z^{2^n} Q_n(z)`

Each `P_n` is a polynomial of degree `2^n − 1` with all coefficients `±1`. Equivalently, the coefficient sequence is the *Rudin–Shapiro sequence* (OEIS A020985, related): a_k = (−1)^(number of "11" substrings in binary of k).

Key bound (Rudin 1959 / Shapiro 1951 thesis):

> For all `z ∈ S^1` (unit circle), `|P_n(z)|² + |Q_n(z)|² = 2 · 2^n`.

This pointwise identity gives `|P_n(z)| ≤ √(2 · 2^n) = √(2(deg + 1))` for all `z`. The sup-norm bound `‖P‖_∞ / √(deg+1) ≤ √2 ≈ 1.4142` is asymptotic; finite-degree polynomials may achieve slightly less.

## When it applies

- **P12 Flat Polynomials** (degree 69, ±1 coefficients) — Rudin–Shapiro is the canonical *known constructive* family for this problem class. The problem asks `min max|p(z)|/√71` for degree-69 ±1 polynomials. Rudin–Shapiro at degree 71 (lifting from `P_n` for `2^n ≥ 72`) gives a baseline; actual SOTA at 1.2809 is *better*, found by computer search.
- **Sidon-set constructions for autocorrelation** — Rudin–Shapiro coefficient patterns produce `±1` sequences with bounded autocorrelation, related to the Barker / Schroeder family. P2/P3 autocorrelation problems can use these as warm-starts.
- **Coding theory** — Rudin–Shapiro sequences underlie certain low-correlation binary codes used in CDMA-style applications.

## Why it works (the structural argument)

The recursion `P_{n+1} = P_n + z^{2^n} Q_n` interleaves two branches at the `2^n` boundary. This:

1. **Doubles the degree** while keeping the sup-norm bounded by `√2` times the previous (constant ratio).
2. **Produces a Walsh-like orthogonality**: `P_n(z)` and `Q_n(z)` are orthogonal in the `L^2` inner product on the unit circle.
3. **Gives a "balanced" coefficient sum** — the `±1` pattern alternates such that local Fourier mass is evenly distributed.

The construction is GAUSS-style (recursive arithmetic with sign-flip rules) — not deeply algebraic, just careful interleaving. It's *the* canonical example of a "tame" constructive Littlewood polynomial.

## Asymptotics and the gap to SOTA

Erdős asked (1957): is there a constant `c < √2` such that every degree-n ±1 polynomial has sup-norm at least `c · √(n+1)`? Equivalently: can we beat Rudin–Shapiro asymptotically?

Modern bounds (per [`source/papers/2020-balister-flat-littlewood.md`](../../source/papers/2020-balister-flat-littlewood.md)):

- **Lower bound** (Erdős): `‖P‖_∞ / √(n+1) ≥ 1` for any non-constant `±1` polynomial.
- **Upper bound** (Balister–Bollobás–Morris–Sahasrabudhe–Tiba 2020): proves *flat* `±1` polynomials exist asymptotically, ratio approaching `1` (resolving Erdős #26). But the construction is non-explicit — uses probabilistic + structural arguments.
- **Constructive bound**: Rudin–Shapiro gives `√2 ≈ 1.4142`.
- **Arena P12 SOTA**: 1.2809 at degree 69. Below Rudin–Shapiro's `√2`; matches the structural floor for n=70 found by *non-recursive* search.

The gap from `√2` to 1.0 (existential lower bound) is open at finite `n`; computer-search SOTA at small n typically lands somewhere in `[1.2, √2]` depending on n's specific factorization properties.

## Classic examples

- **`P_3` at degree 7** (n=3, 2^3 = 8 coefficients): coefficients `(1, 1, 1, −1, 1, 1, −1, 1)`. Sup-norm `√(2·8) = 4`. Ratio `4/√8 = √2`.
- **`P_6` at degree 63**: 64 coefficients. Sup-norm bounded by `√128 ≈ 11.31`. Ratio `√2`.
- **For P12 at degree 69**: Rudin–Shapiro lifted to degree 71 (`P_n` for `n=7` truncated), gives ratio ~`√2 = 1.4142`. SOTA 1.2809 is below this; found via memetic tabu search (Together-AI, 1.26B evaluations).

## How the agent should use it

When the council dispatches with category `flat_polynomials`, `±1_combinatorics`, or any P12-style problem:

1. **Gauss persona** ([`personas/gauss.md`](../personas/gauss.md)) and **Euler persona** ([`personas/euler.md`](../personas/euler.md)) both reach for Rudin–Shapiro as the canonical constructive baseline.
2. **Use Rudin–Shapiro as a warm-start** — provides `±1` polynomial of any degree with sup-norm bounded by `√2 · √(n+1)`.
3. **Local search to beat √2** — empirically, memetic tabu search finds configurations with ratio in `[1.25, √2]` at small n. P12 SOTA 1.2809 is the result of 1.26B-evaluation tabu search.
4. **Don't expect to beat SOTA via structure alone** — the asymptotic gap to 1.0 is provably hard (Balister et al. 2020 used non-constructive methods).

## Limits

- **Recursive construction restricts degree**: Rudin–Shapiro `P_n` has degree `2^n − 1`. For degrees not of this form, you'd take `P_n` and truncate or use a related variant — losing the exact `√2` bound.
- **Doesn't give optimal at small n**: at degree 69 (P12), Rudin–Shapiro gives ratio ~1.4142; computer search finds 1.2809. The recursive bound is asymptotic, not optimal.
- **The asymptotic gap is real**: even Balister–Bollobás 2020's existence proof of flat `±1` polynomials (ratio → 1) doesn't give an explicit construction beating Rudin–Shapiro at any finite n; computer search remains the only path.

## See also

- [`concepts/sidon-sets.md`](sidon-sets.md) — related ±1 / autocorrelation framework
- [`concepts/parameterization-selection.md`](parameterization-selection.md) — Rudin–Shapiro is a specific parameterization for ±1 polynomial spaces
- [`techniques/memetic-tabu-search.md`](../techniques/memetic-tabu-search.md) — the technique that found P12 SOTA
- [`personas/gauss.md`](../personas/gauss.md), [`personas/euler.md`](../personas/euler.md), [`personas/ramanujan.md`](../personas/ramanujan.md) — personas that reach for ±1 constructions
- [`findings/discrete-optimization.md`](../findings/discrete-optimization.md) — broader pattern for ±1 / discrete-combinatorial extremals
- [`source/papers/2020-balister-flat-littlewood.md`](../../source/papers/2020-balister-flat-littlewood.md) — Annals 2020 proof of flat Littlewood existence (resolves Erdős #26)

*Last updated: 2026-05-02*
