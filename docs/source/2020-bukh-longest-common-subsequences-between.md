---
type: source
kind: paper
title: Longest common subsequences between words of very unequal length
authors: Boris Bukh, Zichao Dong
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2009.05869v2
source_local: ../raw/2020-bukh-longest-common-subsequences-between.pdf
topic: general-knowledge
cites: 
---

# Longest common subsequences between words of very unequal length

**Authors:** Boris Bukh, Zichao Dong  ·  **Year:** 2020  ·  **Source:** http://arxiv.org/abs/2009.05869v2

## One-line
Determines the asymptotic expected longest common subsequence (LCS) between two random words of very unequal lengths $n$ and $(1-\varepsilon)kn$ over a $k$-symbol alphabet.

## Key claim
Defining $\gamma_{k,\varepsilon} = \lim_{n\to\infty} \frac{1}{n}\mathbb{E}\,\mathrm{LCS}(w,w')$ for $w \sim [k]^n$, $w' \sim [k]^{(1-\varepsilon)kn}$, the paper proves $1 - 8\varepsilon^2 \le \gamma_{k,\varepsilon} \le 1 - \varepsilon^2/72$ uniformly in $k \ge 2$ for $\varepsilon < 1/60$, and proves a matching lower bound $\gamma_{k,\varepsilon} \ge 1 - \tfrac{1}{4}\varepsilon^2(1+Ck^{-2/13})$ for large $k$ — half of the conjecture $\gamma'_k \to 1/4$ as $k\to\infty$.

## Method
**Variable-length chopping + "$d$-almost contained" prefix waiting times.** Chop the long word $w'$ into fixed-length subwords of length $L$; for each, find the longest prefix of the short word $w$ that becomes a subsequence after removing at most $d$ symbols, denoted $P_d(L)$. Bound $\mathbb{E}[P_d(L) - P_0(L)]$ by reducing prefix evolution (Proposition 6 "bumping" particle process) to **longest non-decreasing subsequences (LNDS)** of words built from "expectant partitions" — most of which are trivial, putting growth near the Tracy–Widom regime. The hard analysis uses a novel **adversarial-game reformulation of Markov chains** (Theorem 11), reducing complex state spaces to worst-case smaller chains, plus KMT strong approximation to Brownian motion + Baryshnikov's GUE largest-eigenvalue identity.

## Result
For $L \ge 20k$: $\mathbb{E}[P_1(L) - P_0(L)] \ge L/(7k)$ (Theorem 3) and $\mathbb{E}[P_d(L) - P_0(L)] \le d\sqrt{2L/k} + d$ (Theorem 4), which yield Theorem 1's two-sided $\varepsilon^2$ bound. A finer asymptotic $\mathbb{E}[P_d(L)-P_0(L)] = 2\sqrt{dL/k}(1 + \text{lower-order})$ (Theorem 5) drives the $\tfrac{1}{4}\varepsilon^2$ lower bound. Also derives an explicit error-term version of the LNDS-on-random-word asymptotic (Lemma 18): $\mathbb{E}[\mathrm{LNDS}(w)]/(2\sqrt{n}) = 1 - \Theta(k^{-2/3}) + O((k^2 + k\log n)/n^{1/2})$.

## Why it matters here
General background; no direct arena tie — but the **adversarial-game Markov chain analysis** (Section 4, Theorem 11) is a transferable technique for upper-bounding worst-case behavior of complicated stochastic processes, and the **LNDS / Tracy–Widom + KMT + GUE largest-eigenvalue** machinery (Appendix C) connects extremal combinatorics on random sequences to random matrix theory — patterns that could surface in autocorrelation / random-construction lower bounds.

## Open questions / connections
- Conjecture: $\gamma'_k \to 1/4$ as $k \to \infty$; only the lower bound is proven. A sublinear-in-$d$ improvement of Lemma 15 (currently $d\sqrt{2L/k}+d$) would close it.
- Refines Chvátal–Sankoff constants $\gamma_k$ (Lueker '09, Kiwi–Loebl–Matoušek '05 with $\gamma_k = (2+o(1))/\sqrt{k}$) to the unequal-length regime.
- Fills a gap in Bréton–Houdré '10 (LNDS convergence to Tracy–Widom for growing $k$) by giving moment convergence with explicit error terms via a clean alternative proof.

## Key terms
longest common subsequence, LCS, Chvátal–Sankoff constant, longest non-decreasing subsequence, LNDS, Tracy–Widom distribution, GUE largest eigenvalue, Markov chain adversarial game, Talagrand inequality, Komlós–Major–Tusnády strong approximation, Poissonization, Brownian motion approximation, random words, Bukh, Dong
