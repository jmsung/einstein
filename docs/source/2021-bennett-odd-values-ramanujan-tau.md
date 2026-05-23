---
type: source
kind: paper
title: Odd values of the Ramanujan tau function
authors: M. Bennett, Adela Gherga, Vandita Patel, S. Siksek
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2101.02933
source_local: ../raw/2021-bennett-odd-values-ramanujan-tau.pdf
topic: general-knowledge
cites:
---

# Odd values of the Ramanujan tau function

**Authors:** M. Bennett, Adela Gherga, Vandita Patel, S. Siksek  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2101.02933

## One-line
Proves effective lower bounds on the largest prime factor $P(\tau(n))$ when $\tau(n)$ is odd, and solves $\tau(n) = \pm q^b$ for primes $3 \le q < 100$ and $\tau(n) = \pm 3^{b_1} 5^{b_2} 7^{b_3} 11^{b_4}$.

## Key claim
If $\tau(n)$ is odd and $n \ge 25$, then either $P(\tau(n)) > \kappa \cdot \log\log\log n / \log\log\log\log n$ for an effective $\kappa > 0$, or some prime $p \mid n$ has $\tau(p) = 0$. As a corollary, $\tau(n)$ odd implies $P(\tau(n)) \ge 13$, ruling out $\tau(n) = \pm 3^\alpha 5^\beta 7^\gamma 11^\delta$.

## Method
Reduces $m \mapsto \tau(p^{m-1})$ to a Lucas sequence via the recurrence $\tau(p^m) = \tau(p)\tau(p^{m-1}) - p^{11}\tau(p^{m-2})$, then applies the Bilu–Hanrot–Voutier Primitive Divisor Theorem and cyclotomic polynomials $\Psi_m(X,Y)$ (related to $\mathbb{Q}(\zeta_m)^+$). For small exponents, associates Frey–Hellegouarch elliptic curves to hypothetical solutions, applies Ribet level-lowering + modularity to compare mod-11 Galois representations against weight-2 newforms of small level. Closes residual cases via Bugeaud's bound on $P(ax^u + by^v)$, Bugeaud–Győry Thue–Mahler bounds, and explicit Thue–Mahler solving.

## Result
Theorem 1: $P(\tau(n)) \gg \log\log\log n / \log\log\log\log n$ for odd $\tau(n)$ absent zero-prime divisors. Theorem 4: $P(\tau(p^m)) \gg_m \log\log p$. Theorem 5: powerful $n$ with $P(\tau(n)) \le 11$ forces $n = 8$ (where $\tau(8) = 2^9 \cdot 3 \cdot 5 \cdot 11$). Theorem 6: $\tau(n) = \pm q^\alpha$ has no solutions for prime $3 \le q < 100$, $n \ge 2$. Threshold "13" in Corollary 1.1 is sharp for the method; 17 is plausible; 19 likely needs new ideas.

## Why it matters here
General background; no direct arena tie. Number-theoretic methodology (Lucas sequences, primitive divisor theorems, Frey curve + level-lowering, Thue–Mahler solving) is a reference template for any arena problem whose structure reduces to exponential Diophantine equations, but no current Einstein Arena problem in the wiki is sphere-packing-adjacent or sieve-adjacent to $\tau(n)$.

## Open questions / connections
- Lehmer's conjecture ($\tau(n) \ne 0$) remains open; best known is $p > 8.16 \times 10^{23}$ (Derickx–van Hoeij–Zeng).
- Extension to $P(\tau(n)) \le 17$ tractable; $\le 19$ would require new techniques.
- Generalizes to weight-$k \ge 4$ newform coefficients $\lambda_f(n)$ with $\lambda_f(p)$ even for large $p$; current paper restricts to $\Delta(z)$.
- Bounds neither imply nor are implied by Luca–Shparlinski's $P(\tau(p)\tau(p^2)\tau(p^3))$ bound.

## Key terms
Ramanujan tau function, Lehmer's conjecture, Lucas sequence, primitive divisor theorem, Bilu-Hanrot-Voutier, Frey-Hellegouarch curve, Galois representation, level-lowering, modularity, Thue-Mahler equation, Bugeaud-Győry bounds, cyclotomic field, Deligne bound
