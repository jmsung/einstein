---
type: source
kind: paper
title: On the Wasserstein Distance between Classical Sequences and the Lebesgue Measure
authors: Louis Brown, S. Steinerberger
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1909.09046
source_local: ../raw/2019-brown-wasserstein-distance-between-classical.pdf
topic: general-knowledge
cites:
---

# On the Wasserstein Distance between Classical Sequences and the Lebesgue Measure

**Authors:** Louis Brown, S. Steinerberger  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1909.09046

## One-line
Shows that Kronecker sequences $x_n = (n\alpha_1, \ldots, n\alpha_d) \bmod 1$ with badly approximable $\alpha \in \mathbb{R}^d$ attain the optimal $W_2$ transport rate $N^{-1/d}$ to Lebesgue measure on $\mathbb{T}^d$, uniformly in $N$.

## Key claim
For $d \geq 2$ and badly approximable $\alpha$, $W_2\!\left(\tfrac{1}{N}\sum_{k=1}^N \delta_{x_k}, dx\right) \leq c_{\alpha,d} N^{-1/d}$ (Theorem 5), which is best possible. This yields a refined numerical-integration error $\left|\int_{\mathbb{T}^d} f - \tfrac{1}{N}\sum f(k\alpha)\right| \leq c_\alpha \|\nabla f\|_{L^\infty}^{(d-1)/d} \|\nabla f\|_{L^2}^{1/d} N^{-1/d}$ (Theorem 6), strictly stronger than Bakhvalov's classical $\|\nabla f\|_{L^\infty} N^{-1/d}$.

## Method
Uses a Fourier-side master inequality (from Steinerberger [48]) bounding $W_2$ by $\inf_{t>0}\bigl(\sqrt{t} + \bigl(\sum_k e^{-2\|k\|^2 t}\|k\|^{-2}|\hat\mu(k)|^2\bigr)^{1/2}\bigr)$, recycling exponential-sum estimates. For Kronecker sequences, geometric-series gives $|\hat\mu(k)| \leq (2/N)/\|\langle k,\alpha\rangle\|$; Khintchine's transference + dyadic-shell counting controls the small-denominator sum. The integration theorem combines heat-smoothing, Monge-Kantorovich duality, and a Sobolev $\dot H^{-1}$ duality bound; the regular-grid version (Theorem 7) uses a Morrey-type Poincaré inequality with Lorentz-space Hölder (O'Neil).

## Result
- Theorem 5 (Kronecker, $d \geq 2$, badly approximable $\alpha$): $W_2 \lesssim_{\alpha,d} N^{-1/d}$, optimal and uniform in $N$.
- Theorem 6 (Kronecker integration): error $\lesssim \|\nabla f\|_{L^\infty}^{(d-1)/d}\|\nabla f\|_{L^2}^{1/d} N^{-1/d}$.
- Theorem 7 (regular grid): same shape with $L^1$ replacing $L^2$ — strictly better, optimal in those norms.
- Theorem 4 (random walk on $\mathbb{T}$ with step $\pm\alpha$, $\alpha$ quadratic irrational): $W_2(\mu_k, dx) \lesssim_\alpha k^{-1/4}$.
- Theorem 8 (general compact manifold): integration bound via Laplacian eigenfunction expansion and heat-kernel smoothing.

## Why it matters here
Provides a uniform-in-$N$ optimal-transport scaling for irrational-rotation sequences, with a smoothed-diaphony generalization of Zinterhof's diaphony to $d \geq 2$ — relevant to autocorrelation/uniformity problems and any arena task where Kronecker / low-discrepancy sequences are used as deterministic samplers. The Theorem 6 integration bound (gradient $L^2$ replacing $L^\infty$) is a sharper sampling guarantee than Koksma-Hlawka for problems with localized derivative concentration.

## Open questions / connections
- Is the badly-approximable hypothesis necessary in Theorem 5, or does Dirichlet-generic $\alpha$ suffice (as in $d=1$)?
- Does an $L^1$ analogue of Theorem 6 (matching Theorem 7's grid bound) hold for Kronecker sequences?
- Does any sequence uniformly achieve the regular-grid Theorem 7 rate $\|\nabla f\|_{L^\infty}^{(d-1)/d}\|\nabla f\|_{L^1}^{1/d} N^{-1/d}$?
- Sharper rate than $k^{-1/4}$ for the $\pm\alpha$ random walk (Theorem 4 conjectured non-optimal).
- Extends Peyre [41] ($W_2 \lesssim \dot H^{-1}$), Steinerberger [48], Graham [26] ($\Omega(\sqrt{\log N}/N)$ lower bound in $d=1$); connects to Beck-Chen irregularities-of-distribution program.

## Key terms
Wasserstein distance, Kronecker sequence, badly approximable vector, diaphony, Zinterhof, discrepancy, Erdős-Turán inequality, Koksma-Hlawka, Khintchine transference, heat kernel smoothing, $\dot H^{-1}$ Sobolev norm, low-discrepancy sequence, numerical integration, Bakhvalov, Peyre inequality, equidistribution
