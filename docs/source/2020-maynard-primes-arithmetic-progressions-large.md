---
type: source
kind: paper
title: "Primes in Arithmetic Progressions to Large Moduli II: Well-Factorable Estimates"
authors: J. Maynard
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2006.07088
source_local: ../raw/2020-maynard-primes-arithmetic-progressions-large.pdf
topic: general-knowledge
cites:
---

# Primes in Arithmetic Progressions to Large Moduli II: Well-Factorable Estimates

**Authors:** J. Maynard  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2006.07088

## One-line
Extends Bombieri–Friedlander–Iwaniec by establishing Bombieri–Vinogradov-type equidistribution of primes in arithmetic progressions to moduli up to $x^{3/5-\epsilon}$ when summed against *triply* well-factorable weights.

## Key claim
For triply well-factorable weights $\lambda_q$ of level $Q \le x^{3/5-\epsilon}$ and fixed residue $a$, $\sum_{q\le Q,(q,a)=1} \lambda_q\bigl(\pi(x;q,a) - \pi(x)/\phi(q)\bigr) \ll_{a,A,\epsilon} x/(\log x)^A$. As a consequence, the linear-sieve upper-bound weights $\lambda_d^+$ inherit equidistribution to level $x^{7/12-\epsilon}$, improving the prior $x^{4/7-\epsilon}$ barrier.

## Method
Heath-Brown identity (with $k=3$) decomposes $\Lambda(n)$ into Type-I/II bilinear sums; Cauchy–Schwarz + Fourier (Poisson) + Bezout reduces these to multidimensional incomplete Kloosterman-type exponential sums bounded by Deshouillers–Iwaniec (Kuznetsov trace formula on $\Gamma_0(\cdot)$). The novelty: when the modulus factorizes into *three* pieces $q_1q_2q_3$, an extra Cauchy–Schwarz over the middle factor drops the relevant congruence-subgroup level from $R^2$ to $T^2$, trading a small diagonal-term loss for a much better off-diagonal bound — perfectly balancing the two contributions across the full range up to $x^{3/5-\epsilon}$. Combinatorial Proposition 9.1 then shows linear-sieve weights of level $x^{7/12}$ admit the requisite three-factor decomposition by a greedy split based on the size of the largest few prime factors.

## Result
Theorem 1.1: equidistribution to $Q \le x^{3/5-\epsilon}$ for triply well-factorable weights (up from $x^{4/7-\epsilon}\approx x^{0.571}$ to $x^{0.6-\epsilon}$). Theorem 1.2: linear-sieve weights $\lambda_d^+$ to $D \le x^{7/12-\epsilon} \approx x^{0.583-\epsilon}$. Proposition 9.1: every $d \in \mathcal{D}^+(x^{7/12-50\delta})$ factors as $d_1 d_2 d_3$ with the four size constraints $d_1 < N/x^\delta$, $N^2 d_2 d_3^2 \le x^{1-\delta}$, $N^2 d_1 d_2^4 d_3^3 \le x^{2-\delta}$, $N d_1 d_2^5 d_3^2 \le x^{2-\delta}$. Author notes $x^{3/5}$ appears to be the method's ceiling — quadruple-well-factorability offers no further gain.

## Why it matters here
General background; no direct arena tie. The Einstein Arena problem set spans sphere packing, autocorrelation, kissing numbers, discrete geometry — not primes in AP. However, the *methodological* core (multi-factor Cauchy–Schwarz to balance diagonal vs off-diagonal contributions; greedy three-piece factorization of weighted sums) is a structural template that could conceivably inform variance-reduction or balancing arguments in sieve-theory adjacent arena problems (e.g. Sidon sets, multiplicative-structure problems if they arise).

## Open questions / connections
- Does the $x^{3/5}$ barrier reflect a fundamental obstruction in the Kuznetsov / Deshouillers–Iwaniec input, or just the current bilinear-decomposition strategy?
- Can technical variants of Theorem 1.2 be paired with Chen's switching principle or Harman's sieve to improve concrete bounds on twin primes / Goldbach (Chen 1973; Fouvry–Grupp; Wu 2004)?
- Extends Bombieri–Friedlander–Iwaniec (1986/87) [2,3] and parallels Drappeau (2015) [6] for smooth numbers — both hit the same $x^{3/5}$ wall, suggesting a shared obstruction in the spectral input.
- Are there *other* sieve weights "closer to triply well factorable" than the linear sieve that would yield further gains?

## Key terms
Bombieri–Vinogradov, Elliott–Halberstam conjecture, well-factorable weights, triply well-factorable, linear sieve, $\beta$-sieve, Heath-Brown identity, Deshouillers–Iwaniec, Kuznetsov trace formula, Kloosterman sums, primes in arithmetic progressions, level of distribution, Maynard, Bombieri–Friedlander–Iwaniec, Chen's switching principle, Harman's sieve
