---
type: source
kind: paper
title: Maximality of subfields as cliques in Cayley graphs over finite fields
authors: Chi Hoi Yip
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2209.00864
source_local: ../raw/2022-yip-maximality-subfields-cliques-cayley.pdf
topic: general-knowledge
cites:
---

# Maximality of subfields as cliques in Cayley graphs over finite fields

**Authors:** Chi Hoi Yip  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2209.00864

## One-line
Proves that subfield cliques in generalized Paley graphs (and generalized Peisert graphs) cannot be extended — the natural algebraic clique construction is already maximal.

## Key claim
For $d > 1$, prime power $q$ with $q^n \equiv 1 \pmod{2d}$ and $q > (n-1)^2$: if $\mathbb{F}_q$ is a maximal subfield clique in the generalized Paley graph $GP(q^n, d)$, then $\mathbb{F}_q$ is a maximal clique (Theorem 1.2). This confirms Yip's Conjecture 1.4 from [12].

## Method
Character-sum estimates on Cayley graphs. The key tool is Katz's bound $|\sum_{a \in \mathbb{F}_q} \chi(\theta + a)| \le (n-1)\sqrt{q}$ for $\theta$ generating $\mathbb{F}_{q^n}/\mathbb{F}_q$. Combined with an $\varepsilon$-lower-bounded set $M = \{\chi(x) : x \in S\}$ (image of connection set under a nontrivial character of order $d$), this gives a contradiction $\varepsilon q \le (n-1)\sqrt{q}$ if an extending vertex existed.

## Result
Proposition 3.1 (general): for any Cayley graph $X = \text{Cay}(\mathbb{F}_{q^n}^+, S)$ containing $GP(q^n, d)$ as subgraph with $\{\chi(x) : x \in S\}$ being $\varepsilon$-lower bounded, $q > (n-1)^2/\varepsilon^2$ forces subfield-maximal $\Rightarrow$ clique-maximal. For $GP^*(q^n, d)$ (generalized Peisert, $d \ge 4$ even): $\varepsilon = \pi/d - \pi/d^2$, giving the bound $q > (n-1)^2 d^4 / \pi^2(d-1)^2$ (Theorem 1.4).

## Why it matters here
General background; no direct arena tie. Tangential to extremal graph theory / Cayley-graph clique problems — could inform problems involving algebraic clique constructions in arithmetic-combinatorics settings, but no current Einstein Arena problem is a direct Cayley-graph clique question.

## Open questions / connections
- Can the condition $q > (n-1)^2$ in Theorem 1.2 be dropped? Verified by SageMath for $n \le 5$ and small $n=6$ cases, but no proof.
- Counterexamples exist when $q$ is small vs $n,d$ (e.g. $q=3, n=4, d=4$ in $GP^*(81,4)$ has a size-9 clique extending $\mathbb{F}_3$) — sharpness of the lower bound remains open.
- Extends Blokhuis (1984) / Van Lint–MacWilliams for Paley graphs of square order; related to Asgarli–Yip [1] on Peisert-type graphs.

## Key terms
Cayley graph, generalized Paley graph, generalized Peisert graph, maximal clique, subfield clique, character sum, Katz bound, multiplicative character, finite field, Van Lint–MacWilliams conjecture, Erdős–Ko–Rado, clique number
