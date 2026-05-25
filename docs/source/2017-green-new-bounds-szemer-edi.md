---
type: source
kind: paper
title: "New bounds for Szemer\'edi's theorem, III: A polylogarithmic bound for $r_4(N)$"
authors: B. Green, T. Tao
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1705.01703
source_local: ../raw/2017-green-new-bounds-szemer-edi.pdf
topic: general-knowledge
cites:
---

# New bounds for Szemer\'edi's theorem, III: A polylogarithmic bound for $r_4(N)$

**Authors:** B. Green, T. Tao  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1705.01703

## One-line
Proves that the largest subset of $\{1,\dots,N\}$ with no 4-term arithmetic progression has size $\ll N(\log N)^{-c}$, matching the Heath-Brown/Szemerédi quality known for 3-APs.

## Key claim
$r_4(N) \ll N(\log N)^{-c}$ for some absolute constant $c > 0$ — a polylogarithmic upper bound, improving the previous $Ne^{-c\sqrt{\log\log N}}$ from Green–Tao 2005 (which itself improved Gowers's $N(\log\log N)^{-c}$).

## Method
Energy-decrement / regularity approach (rather than the density-increment of Roth/Gowers), inspired by Bergelson–Host–Kra Khintchine-type recurrence for length-4 progressions. Reduces Theorem 1.1 to a local recurrence inequality $\Lambda_{a,r}(f) \geq (\mathbb{E}f)^4 - O(\eta)$ with a "thickness" bound $P(r=0) \ll \exp(-\eta^{-O(1)})/p$, established via a local inverse $U^3$-theorem built from Bohr-set machinery, dilated tori, cocycle/coboundary arguments on quadratic phase functions, and iterated Cauchy–Schwarz symmetrization. The Cauchy–Schwarz identity for $x-3y+3z-w=0$ (Lemma 3.2) is the positivity engine specific to length-4.

## Result
For any $N \geq 100$, $r_4(N) \leq C \cdot N (\log N)^{-c}$ with $c>0$ absolute. Authors state this "appears to be the limit of our methods." The proof goes through a stronger Khintchine-type theorem (Theorem 3.1) on $\mathbb{Z}/p\mathbb{Z}$ that couples $a$ and $r$ (giving up independence to gain the quantitative thickness bound).

## Why it matters here
General background; no direct arena tie. Informs additive-combinatorics concepts (Bohr sets, Gowers norms, inverse theorems, energy decrement, arithmetic regularity) that could surface in extremal-set / Sidon-set / autocorrelation contexts but is not directly used by any current Einstein Arena problem.

## Open questions / connections
- Behrend lower bound $r_4(N) \gg N\exp(-c\log^{1/3} N)$ leaves a huge gap with this $(\log N)^{-c}$ upper bound.
- Method couples $a$ and $r$ — independent-$r$ version (Khintchine recurrence à la Bergelson–Host–Kra [19]) does not yield this bound; recovering it is open.
- Extension to $r_k(N)$ for $k \geq 5$ requires inverse $U^{k-1}$ theory; the length-4 Cauchy–Schwarz positivity (Lemma 3.2) has no longer-progression analogue per [2, 53].

## Key terms
Szemerédi theorem, $r_4(N)$, 4-term arithmetic progression, Gowers norm, $U^3$ inverse theorem, Bohr set, energy decrement, arithmetic regularity lemma, Khintchine recurrence, Bergelson–Host–Kra, quadratic Fourier analysis, Cauchy–Schwarz
