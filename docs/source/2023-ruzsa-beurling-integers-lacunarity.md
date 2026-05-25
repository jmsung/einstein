---
type: source
kind: paper
title: Beurling integers with lacunarity
authors: Imre Z. Ruzsa
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2311.11127v1
source_local: ../raw/2023-ruzsa-beurling-integers-lacunarity.pdf
topic: general-knowledge
cites: 
---

# Beurling integers with lacunarity

**Authors:** Imre Z. Ruzsa  ·  **Year:** 2023  ·  **Source:** http://arxiv.org/abs/2311.11127v1

## One-line
Constructs and obstructs examples of Beurling generalized integers (multiplicative semigroups of reals) whose consecutive gaps are bounded below, probing how far non-integer "primes" can coexist with a lacunary integer-like sequence.

## Key claim
If $P$ is a set of primes with $\sum_{p\notin P} 1/p < \infty$ and $\alpha\in\mathbb{R}\setminus\mathbb{Z}$, then $G = P\cup\{\alpha\}$ forces $\liminf(b_{i+1}-b_i)=0$ (Thm 1); conversely, if $\sum_{p\in P} 1/\sqrt{p}<\infty$, a positive-measure set of $\alpha$ makes $G=P\cup\{\alpha\}$ lacunary with $b_{i+1}-b_i\ge 1$ (Thm 2/3).

## Method
Two complementary techniques: (i) constructive Diophantine arguments using continued-fraction convergents/medians plus sieve-style residue-class counts to find integers $x,y$ free of "missing" primes with $|\alpha^m x - y|<\delta$ (Thm 1); (ii) a metric/measure-theoretic argument taking logs $\beta=\log\alpha$ and bounding the measure of "bad" $\beta\in[t,2t]$ by $\sum_{m\in B'} 1/\sqrt{m}$, convergent under the $\sum 1/\sqrt{g}<\infty$ hypothesis (Thm 2/3). Theorems 4–6 use $\mathbb{Q}[\sqrt{q}]$ units, Khinchin badly-approximable numbers, Gelfond–Schneider transcendence, and Gaussian-prime arguments via lattice-triangle areas.

## Result
Theorem 1: lacunarity fails when omitting only an $\sum 1/p$-convergent set of primes. Theorem 3: lacunarity with $b_{i+1}-b_i\ge\delta$ is achievable on a positive-measure set of $\alpha$ whenever $\sum_{g\in G'} 1/\sqrt{g}<\infty$. Theorem 6 constructs irrational generator sets $G$ with $G(x)>cx/\log x$ and gap $\ge 1$ — densest known non-integer lacunary Beurling set. Open: can a maximal lacunary set achieve $B(x)=O(\sqrt{x})$? Theorem 5 shows $x^{1/c}$ density via $G=\{p^c\}$, $1<c<2$.

## Why it matters here
General background; no direct arena tie. Relevant to sieve-theory / multiplicative-structure problems and to Diophantine-approximation toolkit (continued fractions, Khinchin, Gelfond–Schneider) — these tools also surface in autocorrelation/Sidon-set problems and gap-distribution analysis.

## Open questions / connections
- How thin can a maximal lacunary Beurling-integer set be — is $B(x)=O(\sqrt{x})$ attainable?
- The $\sum 1/\sqrt{g}<\infty$ threshold is sharp by Thm 4 (prime squares "just" fail measure-theoretically yet positive-measure example exists by Khinchin-type exception): characterize the intermediate regime between $\sum 1/p$ and $\sum 1/\sqrt{p}$.
- Extends Lagarias [1997] "Beurling integers with the Delone property" — Lagarias settled the integer case; conjectured non-existence of non-integer Delone Beurling sets remains open.

## Key terms
Beurling generalized integers, multiplicative semigroup, lacunarity, Delone property, continued fractions, convergents, median, residue class sieve, badly approximable, Khinchin theorem, Gelfond–Schneider, Gaussian primes, $\mathbb{Q}[\sqrt{2}]$ units, prime reciprocal sum, Lagarias, Ruzsa, gap distribution, transcendence
