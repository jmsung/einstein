---
type: source
kind: paper
title: Counting solutions to invariant equations in dense sets
authors: Tomasz Kosciuszko
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2306.08567
source_local: ../raw/2023-kosciuszko-counting-solutions-invariant-equations.pdf
topic: general-knowledge
cites:
---

# Counting solutions to invariant equations in dense sets

**Authors:** Tomasz Kosciuszko  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2306.08567

## One-line
Improves quantitative bounds on the size of dense integer sets avoiding (or sparsely containing) solutions to translation-invariant linear equations in $k \geq 4$ variables.

## Key claim
For an invariant equation $a_1 x_1 + \cdots + a_k x_k = 0$ ($\sum a_i = 0$) with $k \geq 4$, any $A \subseteq \{1,\dots,N\}$ of density $\alpha$ has at least $\exp(-C \log^7(2/\alpha)) N^{k-1}$ solutions (Theorem 3). For solution-free sets in equations of length $k \geq 2 \cdot 3^{m+1} + 2$, density is bounded by $\exp(-c \log^{1/(6+\gamma_m)} N)\, N$ with $\gamma_m = 2^{1-m}$ (Theorem 1). A Behrend-type construction gives a matching upper bound $\exp(-c \log^2(2/\alpha)) N^{k-1}$ (Theorem 4).

## Method
Bohr-set density-increment iteration in $\mathbb{Z}/p\mathbb{Z}$, combining the Croot–Sisask almost-periods lemma with Chang–Sanders spectrum control to build low-dimensional Bohr sets of almost-periods. A Konyagin-style trick inductively constructs $A'_i, T_i$ so that $w A^+ - w A^+$ contains a large Bohr set for $w \approx 3^{m+1}$, sharpening the long-equation bound. Young's convolution inequality extends Croot–Sisask to multi-set convolutions; the "popular sums" set $P$ enables the density increment when solutions are rare.

## Result
Theorem 3 replaces Bloom's $\exp(-C \alpha^{-1/(k-2)} \log^4(2/\alpha)) N^{k-1}$ lower bound with the much stronger $\exp(-C \log^7(2/\alpha)) N^{k-1}$ — matching the shape of Kelley–Meka's 3-term bound. Theorem 1 improves Schoen–Sisask's $\exp(-c \log^{1/7} N)$ exponent down toward $1/6$ as $k \to \infty$. As an application (Theorem 11), Sidon sets avoiding an invariant equation of length $\geq 5$ satisfy $|S| \leq N^{1/2} \exp(-C (\log \log N)^{1/7})$.

## Why it matters here
General background for additive-combinatorics techniques (Bohr sets, Croot–Sisask, density-increment) that could inform extremal-set and Sidon-set arena problems; the Behrend-type construction and the $\log^c$ exponent shape are reusable templates. No direct arena tie to current packing/autocorrelation problems unless a Sidon-set or sum-free set problem appears.

## Open questions / connections
- Gap between $\log^7$ upper (Theorem 3) and $\log^2$ lower (Theorem 4) bounds — can the exponent be pushed to 2?
- Can the constant $6 + \gamma_m$ in Theorem 1 be driven below 6, or even to the Behrend exponent 2?
- Extends Schoen–Sisask 2016, Bloom 2012, Kelley–Meka 2023; applications to Prendiville's transference principle (Roth-Waring-Goldbach, Sidon equations) remain to be quantified.

## Key terms
invariant equations, Bohr sets, Croot-Sisask lemma, Chang-Sanders theorem, density increment, Behrend construction, Sidon sets, Fourier transference principle, Kelley-Meka, Schoen-Sisask, almost periods, Roth's theorem
