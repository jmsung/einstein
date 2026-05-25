---
type: source
kind: paper
title: On the $j$-th smallest modulus of a covering system with distinct moduli
authors: Jonah Klein, Dimitris Koukoulopoulos, Simon Lemieux
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2212.01299v2
source_local: ../raw/2022-klein-th-smallest-modulus-covering.pdf
topic: general-knowledge
cites: 
---

# On the $j$-th smallest modulus of a covering system with distinct moduli

**Authors:** Jonah Klein, Dimitris Koukoulopoulos, Simon Lemieux  ·  **Year:** 2022  ·  **Source:** http://arxiv.org/abs/2212.01299v2

## One-line
Generalizes Hough's minimum-modulus bound for covering systems with distinct moduli to give a super-exponential lower bound on the $j$-th smallest modulus.

## Key claim
There exists an absolute constant $c > 0$ such that the $j$-th smallest modulus in a minimal covering system with distinct moduli is at least $\exp(c j^2 / \log(j+1))$.

## Method
Adapts the **distortion method** of Balister–Bollobás–Morris–Sahasrabudhe–Tiba (BBMST 2022) to covering systems of multiplicity $s > 1$ rather than $s = 1$. Key reduction: if $\mathcal C$ is a minimal covering system, then truncating the first $\ell-1$ progressions and shifting by $h \in [0, 2^{\ell-1})$ yields a covering system $\mathcal C_\ell$ of multiplicity $2^{\ell-1}$ (using Crittenden–Vanden Eynden's theorem that $n$ progressions failing to cover $\mathbb Z$ also fail to cover $\{1,\dots,2^n\}$). Then bound first/second moments $M_j^{(1)}, M_j^{(2)}$ of distortion-weighted indicator measures, using Mertens' estimate and Chebyshev's prime-counting bound, choosing the free parameters $\delta_j \in [0,1/2]$ to push the master inequality below $1$.

## Result
**Theorem 1:** $j$-th smallest modulus $\ge \exp(c j^2 / \log(j+1))$ for some absolute $c > 0$. **Theorem 3** (the engine): a covering system of multiplicity $s$ has smallest modulus $\ge \exp(c \log^2(s+1) / \log\log(s+2))$. Complementary **Theorem 2** constructs, for each $j \ge 5$, a minimal covering system with explicit moduli $2 < 2^2 < \dots < 2^{j-4} < 3\cdot 2^{j-5} < 2^{j-3} < 3\cdot 2^{j-4} < 3\cdot 2^{j-3}$ — so the growth rate cannot be improved beyond doubly-exponential without further input. Independent weaker version (only $C_j$ existence, no rate) by Cummings–Filaseta–Trifonov.

## Why it matters here
General background; no direct arena tie. Distortion method (probabilistic measure surgery on $\mathbb Z/Q\mathbb Z$ to certify non-covering) is a transferable analytic-combinatorial technique relevant to any arena problem requiring lower bounds on extremal arithmetic structures or sieve-style obstructions.

## Open questions / connections
- Gap between lower bound $\exp(c j^2/\log j)$ and Theorem 2's doubly-exponential construction — what is the true growth rate?
- Squarefree-moduli sharpening (Cummings–Filaseta–Trifonov got minimum modulus $\le 118$ under squarefree assumption) — does the $j$-th-modulus generalization tighten under squarefreeness?
- Distortion method has further applications (Erdős–Selfridge problem, density of uncovered set); what other sieve-flavored extremal problems admit it?

## Key terms
covering systems, Erdős minimum modulus problem, distortion method, distinct moduli, Crittenden–Vanden Eynden theorem, Hough theorem, Balister–Bollobás–Morris–Sahasrabudhe–Tiba, multiplicity of congruence system, Mertens estimate, sieve theory, arithmetic progressions, probabilistic method
