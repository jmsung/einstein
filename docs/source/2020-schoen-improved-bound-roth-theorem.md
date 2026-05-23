---
type: source
kind: paper
title: Improved bound in Roth's theorem on arithmetic progressions
authors: Tomasz Schoen
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2005.01145v1
source_local: ../raw/2020-schoen-improved-bound-roth-theorem.pdf
topic: general-knowledge
cites: 
---

# Improved bound in Roth's theorem on arithmetic progressions

**Authors:** Tomasz Schoen  ·  **Year:** 2020  ·  **Source:** http://arxiv.org/abs/2005.01145v1

## One-line
Sharpens the upper bound on the size of three-term progression-free subsets of $\{1,\dots,N\}$ to $|A| \ll N (\log\log N)^{3+o(1)}/\log N$, the best known result near the logarithmic barrier.

## Key claim
If $A \subseteq \{1,\dots,N\}$ contains no non-trivial three-term arithmetic progression, then $|A| \ll N (\log\log N)^{3}(\log\log\log N)^{5}/\log N$, improving Bloom's $(\log\log N)^4$ exponent and Sanders's $(\log\log N)^6$.

## Method
Fourier-analytic density-increment argument on Bohr sets (Bourgain machinery), combined with structural analysis of the large spectrum due to Bateman–Katz. Three cases by Fourier-coefficient magnitude: (i) middle-size coefficients via dimension bounds, (ii) additively smoothing spectrum via Shkredov-style $E_{2m}$ bounds and Bateman–Katz Lemma 5.3, (iii) additively nonsmoothing spectrum via the Bateman–Katz structure theorem $\Delta \approx X + H$ with highly structured $H$ — the hard case handled in Lemma 13. A first-step large density increment of $(\log(1/\delta))^{1-o(1)}$ on a low-rank Bohr set is then iterated with Bloom's procedure.

## Result
Theorem 1: $|A| \ll N(\log\log N)^3(\log\log\log N)^5/\log N$. Intermediate Theorem 15 yields rank-$\delta^{-1+c}$ Bohr set with density increment $\Omega(\mu \log(1/\delta)/\log\log^5(1/\delta))\cdot\delta$. Behrend lower bound remains $\exp(-c\sqrt{\log N})\cdot N$ — a large gap persists.

## Why it matters here
General background for additive-combinatorics methodology — Fourier large-spectrum analysis, Bohr-set density increment, and $E_{2m}$ energy bounds are reusable across extremal-combinatorics problems (sieve theory, Sidon sets, autocorrelation). No direct Einstein Arena problem on Roth/3-AP, but the Bateman–Katz structural theorem and spectrum-dimension toolkit transfer to any problem where "large Fourier coefficients localize on structured sets."

## Open questions / connections
- Lemma 14 (large-Fourier-coefficient case) is the bottleneck: any improvement to its $(\log(1/\delta))^{1-o(1)}$ increment would directly improve the main bound — author flags this explicitly.
- Gap to Behrend $\exp(-c\sqrt{\log N})$ lower bound — conjecturally the truth is much closer to the lower side; logarithmic barrier $N/\log N$ remains uncrossed in the integer case.
- High-dim analogue (Croot–Lev–Pach, Ellenberg–Gijswijt polynomial method) gives $(3-c)^n$ in $\mathbb{F}_3^n$ — integer-case transfer of polynomial method still open.

## Key terms
Roth theorem, three-term arithmetic progression, density increment, Bohr set, large spectrum, Bateman–Katz, additively smoothing, additive energy $E_{2m}$, Shkredov, Bourgain, Chang spectral lemma, Fourier analysis on $\mathbb{Z}/N\mathbb{Z}$, additive dimension, Behrend construction
