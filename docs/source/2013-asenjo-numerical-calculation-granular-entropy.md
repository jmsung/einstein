---
type: source
kind: paper
title: Numerical calculation of granular entropy.
authors: Daniel Asenjo, F. Paillusson, D. Frenkel
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1312.0907
source_local: ../raw/2013-asenjo-numerical-calculation-granular-entropy.pdf
topic: general-knowledge
cites:
---

# Numerical calculation of granular entropy.

**Authors:** Daniel Asenjo, F. Paillusson, D. Frenkel  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1312.0907

## One-line
Numerically estimates the number $\Omega(N,\phi)$ of distinct jammed packings of up to $N=128$ polydisperse soft disks by measuring basin-of-attraction volumes on the potential energy landscape.

## Key claim
The granular entropy, properly defined as $S^* = -\sum_i p_i \ln p_i - \ln N!$ (i.e. with a Gibbs $-\ln N!$ correction since basins are sampled with unequal probabilities $p_i$ proportional to their volumes), is **extensive** in $N$; for $N=128$ at $\phi=0.88$, $\Omega \sim 10^{250}$, outperforming direct enumeration by $>200$ orders of magnitude.

## Method
Generate $N_f \sim 1000$ equilibrated hard-disk fluid configurations, then Stillinger-quench (via a modified FIRE algorithm that avoids L-BFGS basin-disconnection pathologies) to soft-WCA energy minima. Compute each basin volume $v_i$ by thermodynamic integration from a harmonic reference state, $F_i = F_\text{harm} - \tfrac{1}{2}\int_0^{k_\text{max}} \langle u^2(k)\rangle\,dk$, sampled via parallel-tempered MCMC. Unbias the basin-volume-weighted distribution $B(F|N,\phi)$ by fitting a 3-parameter generalized normal $p(F|\bar F,\alpha,\beta)$ and using $\langle v\rangle = [\int B(F) e^F dF]^{-1}$, then combine with the hard-disk EOS to get $V_\text{acc}$ and hence $\Omega = V_\text{acc}/\langle v\rangle$.

## Result
For $\phi=0.88$, $\ln\Omega(N)$ grows non-linearly in $N$ but $\ln\Omega - \ln N!$ is linear through the origin (extensive), and likewise for $S^*$. Fitted $\alpha^2$ scales linearly with $N$ and $\beta \to 2$ as $N\to\infty$ (i.e. $B$ becomes Gaussian for large $N$). Two protocols with very different soft-shell ranges ($d^S/d^{HD}=1.12$ vs $1.4$) give virtually identical $\ln\Omega$, suggesting protocol independence at this density.

## Why it matters here
General background; no direct arena tie. Distant relevance: basin-of-attraction volume estimation via harmonic-reference thermodynamic integration is a technique analogue for any Einstein Arena problem where one wants to count distinct local minima of a non-convex objective (e.g. sphere/disk packing landscapes), and the unequal-basin-volume insight cautions against treating multistart-quench frequencies as uniform samples of distinct minima.

## Open questions / connections
- Does the extensivity of $S^* - \ln N!$ hold for other jamming protocols (hard particles, different parent densities, 3D)?
- Extends Xu–Frenkel–Liu 2011 (PRL 106, 245502) basin-volume method from $N\sim 16$ to $N\sim 128$; resolves the long-debated Edwards hypothesis [3,4] by redefining it without the equal-probability assumption.
- Why are jammed-minima distributions from low-density and high-density parent fluids so similar — does this reflect a deeper rigidity of the energy landscape?

## Key terms
granular entropy, Edwards hypothesis, jamming, basin of attraction, Stillinger quench, FIRE algorithm, thermodynamic integration, parallel tempering, polydisperse hard disks, WCA potential, generalized normal distribution, Gibbs $\ln N!$ correction, configurational entropy, packing enumeration
