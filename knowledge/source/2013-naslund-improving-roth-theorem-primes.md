---
type: source
kind: paper
title: On Improving Roth's Theorem in the Primes
authors: Eric Naslund
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1302.2299
source_local: ../raw/2013-naslund-improving-roth-theorem-primes.pdf
topic: general-knowledge
cites:
---

# On Improving Roth's Theorem in the Primes

**Authors:** Eric Naslund  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1302.2299

## One-line
Sharpens the quantitative bound on the density of progression-free subsets of the primes by replacing an $L^2$ estimate with an $L^{2k}$ estimate in the Helfgott–De Roton framework.

## Key claim
If $A \subset \mathbb{P} \cap [1,N]$ contains no nontrivial 3-term arithmetic progression and has relative density $\alpha = |A|/\pi(N)$, then $\alpha \ll \frac{(\log\log\log N)^6}{\log\log N}$.

## Method
W-trick to remove small primes and lift $A$ to a dense subset $A_0 \subset \mathbb{Z}/P\mathbb{Z}$; convolve $a = \mathbf{1}_{A_0}$ (normalized) with the indicator $\sigma$ of a Bohr set $B(R,\epsilon)$ built from the large spectrum. The novelty is bounding $\|a*\sigma\|_{2k}$ (not just $\|a*\sigma\|_2$) via a Selberg-sieve estimate of Klimov for $k$-tuples of primes in arithmetic progression, giving sharper control over outliers; combine with Sanders' bound on Roth in the integers and take $2k \sim \log\log\log N$.

## Result
Theorem 1: $\alpha \ll (\log\log\log N)^6 / \log\log N$, improving Helfgott–De Roton's $(\log\log\log N)/(\log\log N)^{1/3}$ (and the $(\log\log\log N)^{5/2}/(\log\log N)^{1/2}$ one gets by plugging Sanders into their argument) by roughly a factor of $(\log\log N)^{1/2}$ up to log-log-log corrections. The exponent on $\log\log N$ in the denominator goes from $1/2$ to $1$ via the $L^{2k}$ trick.

## Why it matters here
General background; no direct arena tie. Relevant only as a methodological exemplar: replacing $L^2$ with $L^{2k}$ for sharper tail control in convolution-based extremal arguments — a pattern transferable to autocorrelation / extremal-graph problems where Plancherel-only bounds leave slack.

## Open questions / connections
- Can the exponent 6 on $(\log\log\log N)$ be reduced, or is the true bound closer to the integer case $(\log\log N)^5/\log N$?
- Extends Green (2005), Helfgott–De Roton (2011), Sanders (2011) — same Bohr-set / restriction-theory machinery, sharper norm.
- The $L^{2k}$ Selberg-sieve moment bound (Klimov) is reusable wherever one needs $k$-th moments of prime-indicator convolutions.

## Key terms
Roth's theorem in the primes, 3-term arithmetic progression, relative density, W-trick, Selberg sieve, Klimov theorem, Bohr set, large spectrum, restriction theory, $L^{2k}$ moment bound, Brun–Titchmarsh, Helfgott, De Roton, Sanders, Green–Tao
