---
type: source
kind: paper
title: Consequences of the Moosbauer-Poole Algorithms
authors: Manuel Kauers, Isaac Wood
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2505.05896
source_local: ../raw/2025-kauers-consequences-moosbauer-poole-algorithms.pdf
topic: general-knowledge
cites:
---

# Consequences of the Moosbauer-Poole Algorithms

**Authors:** Manuel Kauers, Isaac Wood  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2505.05896

## One-line
Leveraging the recent Moosbauer-Poole $5\times5$ (rank 93) and $6\times6$ (rank 153) matrix multiplication schemes, the authors run flip-graph searches on neighboring rectangular formats and obtain new record ranks for 12 of 14 formats considered.

## Key claim
Improved upper bounds on the bilinear rank of $n\times m$ by $m\times p$ matrix multiplication for nearly all formats with $4 \le n \le m \le p \le 7$ near $(5,5,5)$ and $(6,6,6)$, e.g. $(5,6,7) \le 150$, $(4,5,6) \le 90$, $(6,6,7) \le 176$, with all but two formats beaten vs. Sedoglavic's April-2025 catalogue.

## Method
Flip-graph search [Kauers-Moosbauer 2023; Moosbauer-Poole 2025]: take a known correct multiplication scheme as starting point and apply local "flip" moves seeking variants from which one multiplication can be eliminated. Starting points are constructed by *blockwise patching* (extending a smaller-format scheme to a larger one by appending standard sub-blocks) or by *variable zeroing* (restricting a larger scheme to a smaller format). Schemes are first found over $\mathbb{Z}_2$, then Hensel-lifted to integer coefficients where possible.

## Result
New ranks (over $\mathbb{Z}$ except where noted): $(4,5,5)\le 76$ over $\mathbb{Z}_2$, $(4,5,6)\le 90$, $(4,5,7)\le 104$, $(5,5,6)\le 106$, $(4,6,7)\le 110$, $(5,5,7)\le 123$, $(5,6,6)\le 127$, $(4,7,7)\le 130$, $(5,6,7)\le 150$, $(5,7,7)\le 176$, $(6,6,7)\le 183$. No improvement on $(4,6,6)\!=\!109$ or $(6,7,7)\!=\!215$. Roughly one day on a 100-core machine per "arrow" (one starting-point-to-format search).

## Why it matters here
General background; no direct Einstein Arena tie. This is bilinear complexity / tensor decomposition territory — distinct from the arena's sphere-packing / autocorrelation / discrete-geometry problems. It could weakly inform meta-strategy: the *incremental-search* pattern (bootstrap a hard format from a smaller solved one + blockwise extension) is structurally similar to warm-starting optimizers from related-problem solutions.

## Open questions / connections
- Are the $\mathbb{Z}_2$ schemes that fail to Hensel-lift (e.g. $(4,5,5)$ rank 74, $(6,7,7)$ rank 221) liftable over a different ring, or genuinely characteristic-dependent?
- Why are some "arrows" in the search lattice computationally much cheaper than others? — unexplained.
- Extends Arai et al. [ISSAC'24] incremental flip-graph approach; leaves open whether AlphaTensor-style RL + flip-graph hybrids could close further gaps.
- Asymptotic exponent $\omega$ is untouched — these are concrete small-format records.

## Key terms
matrix multiplication, bilinear rank, flip graph search, Strassen algorithm, Moosbauer-Poole, AlphaTensor, tensor decomposition, Hensel lifting, blockwise patching, rectangular formats, Z2 schemes, incremental search
