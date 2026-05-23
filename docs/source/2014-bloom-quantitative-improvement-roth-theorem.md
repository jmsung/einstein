---
type: source
kind: paper
title: A quantitative improvement for Roth's theorem on arithmetic progressions
authors: T. Bloom
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1405.5800
source_local: ../raw/2014-bloom-quantitative-improvement-roth-theorem.pdf
topic: general-knowledge
cites:
---

# A quantitative improvement for Roth's theorem on arithmetic progressions

**Authors:** T. Bloom  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1405.5800

## One-line
Bloom sharpens the upper bound for the largest 3-AP-free subset of $\{1,\dots,N\}$ to $|A| \ll N(\log\log N)^4/\log N$, breaking past Sanders' $(\log\log N)^6$ factor via a new Fourier-spectrum structural lemma.

## Key claim
If $A \subset \{1,\dots,N\}$ contains no non-trivial 3-term arithmetic progression, then $|A| \ll N(\log\log N)^4/\log N$ (Theorem 1.1). Same bound generalizes to any equation $c_1x_1+c_2x_2+c_3x_3=0$ with $\sum c_i=0$ (Theorem 1.3); the $\mathbb{F}_q[t]$ analogue gets $(\log n)^2 q^n/n$ (Theorem 1.4); sumset AP-length improves to $\exp(c\,\alpha^{1/2}/\log(1/\alpha) \cdot \sqrt{\log N})$ (Theorem 1.2).

## Method
Replaces Chang's lemma in the density-increment argument with a new structural result (Theorem 1.6/4.1): the large spectrum $\Delta_\eta(A)$ contains a subset of size $\gg \eta|\Delta_\eta(A)|$ that is $d$-covered with $d \ll \eta^{-1}\log(1/\alpha)$ — saving a factor of $\eta$ in dimension at the cost of $\eta$ in size. Proof works entirely in frequency space (no Croot–Sisask / Bogolyubov-style combinatorial tools), bounding $2m$-fold additive energy via random sampling of the spectrum, inspired by Bateman–Katz's cap-set breakthrough. Iterates a standard Bourgain-style Bohr-set density increment using the sharper spectral lemma.

## Result
Quantitative improvement from Sanders' $(\log\log N)^6 N/\log N$ (2011) to $(\log\log N)^4 N/\log N$. Still far from Behrend's lower bound $R(N) \gg N\exp(-c\sqrt{\log N})$. The intermediate spectral lemma is the reusable contribution; the AP-count lower bound is $\Upsilon_c(A) \geq \exp(-O_c(L(\alpha)^4\alpha^{-1}))N^2$ where $L(\alpha)=2+\lceil\log(1/\alpha)\rceil$.

## Why it matters here
General background; no direct arena tie. Relevant to additive-combinatorics / extremal-set problems should they appear (Sidon-set framing, sumset structure, frequency-space density-increment as a meta-technique transferable to discrete optimization). The spectral-energy-via-random-sampling idea is the transferable nugget.

## Open questions / connections
- Can combinatorial (Croot–Sisask) tools be combined with this frequency-only method for further gains? (Bloom explicitly conjectures yes.)
- Bateman–Katz cap-set methods may push $\mathbb{F}_q[t]$ bound to $q^n/n^{1+\epsilon}$ when $c_i \in \mathbb{F}_q$.
- Gap between $(\log\log N)^4/\log N$ upper and $\exp(-c\sqrt{\log N})$ lower remains huge — fertile territory.

## Key terms
Roth's theorem, 3-term arithmetic progression, Chang's lemma, large spectrum, additive energy, Bohr set, density increment, Fourier analysis on $\mathbb{Z}_N$, Behrend lower bound, Bateman–Katz, dissociated set, sumset arithmetic progressions, $\mathbb{F}_q[t]$ analogue, Sanders
