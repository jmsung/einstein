---
type: source
kind: paper
title: The Kelley–Meka bounds for sets free of
three-term arithmetic progressions
authors: T. Bloom, Olof Sisask
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2302.07211
source_local: ../raw/2023-bloom-kelley-meka-bounds-sets.pdf
topic: general-knowledge
cites:
---

# The Kelley–Meka bounds for sets free of
three-term arithmetic progressions

**Authors:** T. Bloom, Olof Sisask  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2302.07211

## One-line
A self-contained exposition of Kelley–Meka's near-Behrend upper bound for cap sets in $\{1,\dots,N\}$, recast in classical Bohr-set language and extended to integer analogues of related sumset results.

## Key claim
If $A \subseteq \{1,\dots,N\}$ has no non-trivial 3-term AP, then $|A| \leq N / \exp(c (\log N)^{1/12})$ — a quasi-polynomial bound matching the Behrend-style shape $\exp(-c(\log N)^\beta)N$ for the first time, with $\beta = 1/12$ vs. Behrend's lower-bound $\beta = 1/2$.

## Method
Five-step physical-side argument bypassing the polynomial method (unavailable over $\mathbb{Z}$): (1) **Hölder lifting** — convert deficit $\langle \mu_A * \mu_A, \mu_C\rangle \le 1/2$ to large $\|\mu_A \circ \mu_A - 1\|_p$ for $p \ll L(\gamma)$; (2) **unbalancing** — exploit non-negativity of $\widehat{\mu_A \circ \mu_A}$ to upgrade to $\|\mu_A \circ \mu_A\|_{p'} \ge 1 + \Omega(1)$; (3) **dependent random choice / sifting** — find dense $A_1, A_2 \subseteq A$ with $\langle \mu_{A_1} \circ \mu_{A_2}, 1_S\rangle$ large where $S = \{x : \mu_A \circ \mu_A(x) > 1+\epsilon\}$; (4) **$L^p$ almost-periodicity** (Croot–Sisask) to find a low-rank Bohr set $V$ on which the convolution is regularized; (5) **density increment** of $(1+\Omega(\epsilon))\alpha$ on $V$, iterated. The Bloom–Sisask refinement replaces Kelley–Meka's ad hoc multi-dim progression machinery with classical regular Bohr sets.

## Result
Theorem 1: $|A| \le N \exp(-c(\log N)^{1/12})$ for 3-AP-free $A \subseteq [N]$. Theorem 2 (finite-field model): $|A| \le q^{n - cn^{1/9}}$ for $A \subseteq \mathbb{F}_q^n$ (weaker than Ellenberg–Gijswijt's $q^{n-cn}$ but proof-of-method). Theorem 3: $A+A+A$ contains an AP of length $\ge \exp(-CL(\alpha)^3) N^{c/L(\alpha)^9}$, improving Sanders' $N^{\alpha^{1+o(1)}}$. Authors note exponent improvable to $1/9$ (clean) or $5/41$ (tedious); claim $1/7$ is the natural method limit.

## Why it matters here
Direct relevance to autocorrelation-style problems and discrete-combinatorics arena problems involving 3-term progressions, Sidon-like sets, and sumset structure. The five-step recipe — Hölder lift → unbalance via spectral non-negativity → sifting → almost-periodicity → density increment — is a transferable physical-side template; the unbalancing step (Fourier non-negativity of $f \circ f$) is the key new idea worth distilling as a stand-alone wiki concept.

## Open questions / connections
- Can the $1/12$ exponent be pushed past the speculated $1/7$ method-ceiling toward Behrend's $1/2$? Authors suggest $1/3$–$1/4$ is the density-increment-with-Bohr-sets limit.
- Does the Hölder-lift + unbalancing + sifting + almost-periodicity stack generalize to other translation-invariant equations (4+ variables already known via Schoen–Sisask)?
- Extends Bloom–Sisask 2020 ($C = 1+c$ in $N/(\log N)^C$); subsumes Sanders 2008 for AP-in-$A+A+A$.
- Open: integer analogue of the full Kelley–Meka regularity structure theorem (Theorem 5 here is the proposed answer to their Footnote 9).

## Key terms
three-term arithmetic progressions, Roth's theorem, cap set, Behrend construction, Bohr sets, almost-periodicity, dependent random choice, Hölder lifting, unbalancing, density increment, Kelley-Meka, Bloom-Sisask, Sanders, Croot-Sisask, additive combinatorics, convolution non-negativity, sumset structure, $\mathbb{F}_q^n$ model
