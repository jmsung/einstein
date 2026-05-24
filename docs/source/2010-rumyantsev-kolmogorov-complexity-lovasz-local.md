---
type: source
kind: paper
title: Kolmogorov complexity, Lovasz local lemma and critical exponents
authors: Andrey Rumyantsev
year: 2010
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1009.4995v1
source_local: ../raw/2010-rumyantsev-kolmogorov-complexity-lovasz-local.pdf
topic: general-knowledge
cites:
---

# Kolmogorov complexity, Lovasz local lemma and critical exponents

**Authors:** Andrey Rumyantsev  ·  **Year:** 2010  ·  **Source:** http://arxiv.org/abs/1009.4995v1

## One-line
Reproves Krieger–Shallit (every real $\alpha > 1$ is a critical exponent of some sequence) via a Kolmogorov-complexity / Lovász-local-lemma framework that controls subsequence complexity even under prescribed repetition patterns.

## Key claim
For any $\alpha > 1$ there exists an infinite sequence with critical exponent exactly $\alpha$ (Theorem 5). Stronger: for $1 < \alpha < \beta$ one can build a sequence containing $r$-powers for all rational $r < \alpha$ while every length-$n$ substring is $\varepsilon n$-far (Hamming) from any fractional power of exponent $\ge \beta$ (Theorem 4).

## Method
Lovász local lemma is applied to events "$\omega(A) = Z$" indexed by finite supports $A$ and strings $Z$ of low conditional Kolmogorov complexity $K(A,Z\mid t) < \gamma\#A$. Verifying the LLL inequality reduces to convergence of $\sum_m 2^m \cdot 2^{-\gamma' m}$, yielding a sequence whose every long substring has complexity $\ge \gamma n$ ("Levin's lemma"). The construction is then extended to sequences obeying a computable equivalence/repetition pattern (Theorem 3, counting *free bits* $\#_f A$), and composed with active intervals + bracket/Cartesian-product layers to kill unwanted periods.

## Result
- Theorem 1: $\exists \omega$ s.t. $K(A,\omega(A)\mid t) \ge \gamma\#A$ for some $t\in A$, all large $A$, any $\gamma<1$.
- Theorem 3: same with free-bit count $\#_f A$ under a repetition pattern, minus $\log m(t)$ multiplicity penalty.
- Theorems 4–5: sequences with prescribed approximate/exact critical exponent $\alpha$, parameter $\gamma$ chosen close to $1$ so that density of free bits $\ge 1/\alpha$ forces complexity contradictions for any exponent $>\alpha$.

## Why it matters here
General background; no direct arena tie. The LLL-via-Kolmogorov-complexity construction template is relevant to combinatorial existence proofs (extremal graph theory, forbidden-substring problems) and to any arena problem where one needs to assert *existence of a configuration avoiding many bad events with overlapping dependencies* — a pattern that recurs whenever standard probabilistic arguments fail due to dependency.

## Open questions / connections
- Can the complexity-of-subsequence framework give *constructive* (algorithmic LLL, Moser–Tardos style) versions of these sequences?
- Quantitative dependence of the constants $N$, $\varepsilon$ on $\alpha - \beta$ — what is the tradeoff between approximation slack and minimum-substring length?
- Extends [2] (Rumyantsev–Ushakov on forbidden substrings + almost-periodic sequences) and the original Krieger–Shallit critical-exponent result [1].

## Key terms
Lovász local lemma, Kolmogorov complexity, prefix complexity, critical exponent, fractional power, repetition pattern, free bits, Levin's lemma, almost periodic sequences, forbidden substrings, Hamming distance, combinatorics on words
