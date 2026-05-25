---
type: source
kind: paper
title: Van Lint-MacWilliams' conjecture and maximum cliques in Cayley graphs over finite fields
authors: Shamil Asgarli, Chi Hoi Yip
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2106.01522
source_local: ../raw/2021-asgarli-van-lint-macwilliams-conjecture-maximum.pdf
topic: general-knowledge
cites:
---

# Van Lint-MacWilliams' conjecture and maximum cliques in Cayley graphs over finite fields

**Authors:** Shamil Asgarli, Chi Hoi Yip  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2106.01522

## One-line
Gives a new proof of the van Lint–MacWilliams conjecture and extends it to a new family of "Peisert-type" Cayley graphs over $\mathbb{F}_{q^2}$, characterizing their maximum cliques as the subfield $\mathbb{F}_q$.

## Key claim
For any Peisert-type graph $X = \mathrm{Cay}(\mathbb{F}_{q^2}^+, S)$ where $S$ is a union of at most $(q+1)/2$ cosets of $\mathbb{F}_q^*$ containing $\mathbb{F}_q^*$: $\omega(X) = q$, and every maximum clique containing $0$ is an $\mathbb{F}_p$-subspace (Thm 1.2). Under an $\varepsilon$-lower-bounded character condition and $p > 4.1 n^2/\varepsilon^2$ (where $q = p^n$), the only maximum clique containing $0,1$ is $\mathbb{F}_q$ (Thm 1.3) — resolving Mullin's conjecture for Peisert graphs and Yip's conjecture for $\mathrm{P}^*_{q^4}$ at sufficiently large $p$.

## Method
Combines two tools: (1) Rédei–Ball–Szőnyi direction theory — a clique of size $q$ in $\mathrm{AG}(2,q)$ that determines $\le (q+1)/2$ directions must be $K$-linear over some subfield $K \subseteq \mathbb{F}_q$, forcing $\mathbb{F}_p$-subspace structure; (2) Weil-type character sum estimates on subspaces (Katz, Reis) — $|\sum_{x \in C} \chi(x)| < 2n\sqrt{p}\,|C|$ for $C$ an $\mathbb{F}_p$-subspace, contradicted by the $\varepsilon$-lower-bound $|\sum \chi(x)| \ge \varepsilon(|C|-1)$ unless $C = \mathbb{F}_q$. The "$\varepsilon$-lower bounded" notion captures non-cancellation of $\chi(S)$ on the complex plane (e.g. $\{1, i\}$ is $1/\sqrt{2}$-lower bounded).

## Result
Establishes: van Lint–MacWilliams for large $p$; Mullin's conjecture for Peisert graphs of order $q^2$ with $q = p^n$, $p > 8.2 n^2$ (Thm 1.4); generalized Peisert graphs $\mathrm{GP}^*(q^2, d)$ with $p > 4.1 n^2 d^4/\pi^2(d-1)^2$ (Thm 2.20); $\mathbb{F}_q$ is a maximal clique in the Peisert graph of order $q^4$ for $q > 3$ (Thm 1.5); and an embeddability/stability result: any clique with $|C| > q - (1 - m/(q+1))\sqrt{q}$ sits in an $\mathbb{F}_p$-subspace of dimension $n$ (Thm 2.15).

## Why it matters here
General background; no direct arena tie — none of the 23 problems are EKR-type clique problems on Paley/Peisert graphs. Possible peripheral relevance to the autocorrelation / Sidon-set family (P-class problems using finite-field character sum technology) and to any future problem invoking quadratic-residue / Cayley-graph structure.

## Open questions / connections
- Extends Blokhuis (1984) and Sziklai (1999) to non-multiplicatively-closed connection sets — the Peisert-type framework unifies (generalized) Paley + Peisert graphs under one $\mathbb{F}_p$-subspace + character-sum argument.
- Conjecture 5.2 (Yip): for $d \mid (q^n-1)/(q-1)$, does $\mathbb{F}_{p^r}$ form a maximal clique in $\mathrm{GP}(q, d)$? Partial progress here (Thm 5.3 for $n$ odd prime, $q > n^2$).
- Sharpness of the $p > 4.1 n^2/\varepsilon^2$ threshold: Example 2.21 shows $\mathrm{GP}^*(3^4, 10)$ and $\mathrm{GP}^*(5^4, 26)$ have more max cliques than the subfield orbit predicts — small-$p$ regime needs different tools.

## Key terms
Paley graph, Peisert graph, Peisert-type graph, Cayley graph, maximum clique, clique number, Erdős-Ko-Rado, van Lint-MacWilliams conjecture, Blokhuis, Sziklai, Rédei direction theorem, Ball direction theorem, character sum estimates, Weil bound, multiplicative character, finite field $\mathbb{F}_{q^2}$, generalized Paley graph, subfield clique, $\mathbb{F}_p$-subspace, affine Galois plane, ε-lower bounded
