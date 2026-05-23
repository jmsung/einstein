---
type: source
kind: paper
title: The sparsity of character tables of high rank groups of Lie type
authors: M. Larsen, A. Miller
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2006.00847
source_local: ../raw/2020-larsen-sparsity-character-tables-high.pdf
topic: general-knowledge
cites:
---

# The sparsity of character tables of high rank groups of Lie type

**Authors:** M. Larsen, A. Miller  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2006.00847

## One-line
Proves that for finite simple groups of Lie type, the fraction of non-zero entries in the character table tends to zero as the rank grows.

## Key claim
**Theorem 1:** For any sequence $G_i$ of finite simple groups of Lie type with rank $\to \infty$, the sparsity $\Sigma(G_i) := |\{(g^G,\chi) : \chi(g) \neq 0\}| / (k(G)|\mathrm{Irr}(G)|) \to 0$. Bounded-rank series have nonzero rational limits (e.g. $\Sigma(L_2(q)) \to 1/2$); the unbounded-rank case is the new result.

## Method
Burnside-style divisibility trick combined with Lusztig's classification of irreducible characters. For most pairs $(g^G,\chi)$, find a large Zsigmondy prime $\ell$ with $\mathrm{ord}_\ell |g^G| < \mathrm{ord}_\ell \chi(1)$, forcing $d_{g^G,\chi} := \chi(1)/(\chi(1),|g^G|)$ to be large; then since $\chi(g)$ is divisible by $d_{g^G,\chi}$ in cyclotomic integers, the average of $|\chi(g)|^2$ over such non-zero values exceeds $d^2$, but the orthonormality average is 1, forcing those pairs to be rare. Reduces conjugacy-class counting to characteristic polynomials in $L_n(q), U_n(q), O_n(q)$ via Proposition 2's bipartite framework.

## Result
$\Sigma(G_i) \to 0$ for all unbounded-rank Lie-type sequences (types $A_r$, ${}^2A_r$, $B_r$, $C_r$, $D_r$, ${}^2D_r$, Suzuki, Ree). Also **Theorem 20**: small normal subsets ($|S| < \delta|G|$) consist of few conjugacy classes ($< \epsilon k(G)$). Uses subexponential bounds: unipotent class counts grow subexponentially (Lemma 12), $|L_n(q)| = |U_n(q)| = |O_{2r}(q)| = q^r$ (Lemma 5), and the fraction of polynomials with $\rho(P) \geq m$ is $< 4 \cdot 2^{-m/4}$.

## Why it matters here
General background; no direct arena tie. Closest relevance is methodological: the "Zsigmondy prime + cyclotomic-integer averaging" trick is a clean example of using number-theoretic divisibility to force statistical separation — a stance that may inform extremal-combinatorics problems where divisibility constraints rule out near-tight configurations.

## Open questions / connections
- Is $\Sigma(A_n) \to 0$ or $\to$ a constant in $(0,1)$? Numerical evidence [Miller 2019] suggests strict positivity — open.
- Miller [2014]: probability $\chi(g) = 0$ for random $(\chi,g)$ in symmetric groups tends to 1 (opposite phenomenon from bounded-rank Lie type).
- Extends [Gallagher-Larsen-Miller 2019] "Many zeros of many characters of $GL(n,q)$" to all classical types and uses [Fulman-Guralnick 2012, 2013] conjugacy-class bounds.

## Key terms
character table sparsity, finite simple groups of Lie type, Lusztig classification, Deligne-Lusztig characters, Zsigmondy primes, Burnside divisibility, cyclotomic integers, unipotent characters, classical groups, regular semisimple, conjugacy classes, subexponential growth
