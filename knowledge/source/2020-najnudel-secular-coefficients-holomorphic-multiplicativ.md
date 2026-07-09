---
type: source
kind: paper
title: Secular coefficients and the holomorphic multiplicative chaos
authors: J. Najnudel, Elliot Paquette, N. Simm
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2011.01823
source_local: ../raw/2020-najnudel-secular-coefficients-holomorphic-multiplicativ.pdf
topic: general-knowledge
cites:
---

# Secular coefficients and the holomorphic multiplicative chaos

**Authors:** J. Najnudel, Elliot Paquette, N. Simm  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2011.01823

## One-line
Studies the coefficients $c_n^{(N)}$ of the characteristic polynomial $\det(1-zU_N^*)$ for the Circular $\beta$-Ensemble, identifying their limit law as a new "Holomorphic Multiplicative Chaos" (HMC) closely tied to Gaussian multiplicative chaos.

## Key claim
For $\beta > 4$ (i.e. $\theta = 2/\beta < 1/2$) with $n,N\to\infty$ and $n/N\to 0$, $c_n^{(N)}/\sqrt{\mathbb{E}|c_n^{(N)}|^2} \xrightarrow{d} Z\cdot E(1)^{-1/\beta}/\Gamma(1-2/\beta)$ where $Z$ is standard complex normal and $E(1)$ is independent exponential; equivalently $c_n \xrightarrow{d} \sqrt{M_\theta}\,Z$ with $M_\theta$ the Fyodorov-Bouchaud GMC total mass. Also resolves Diaconis-Gamburd's open question: for $\beta=2$ the middle coefficient $c^{(N)}_{\lfloor N/2\rfloor} \xrightarrow{d} 0$ at rate $w_N=(\log(1+N))^{-1/4}$.

## Method
Combinatorial: generalize Diaconis-Gamburd's magic-square moment formula to all $\beta>0$ via Jack symmetric functions, giving $\mathbb{E}|c_n|^{2k}$ as a $\theta$-weighted sum over $k\times k$ magic squares. Probabilistic: second-moment / martingale methods on the Fourier expansion $c_n = [z^n]\exp(\sqrt{\theta}\sum_k z^k N_k/\sqrt{k})$, combined with Karamata-Hardy-Littlewood Tauberian theorems (extended to in-probability convergence) to link partial sums $\sum |c_q|^2$ to the GMC total mass $M_\theta$. Sobolev regularity of HMC analyzed via Gaussian computations on Fourier modes.

## Result
- Magic-square moment formula extended to all $\beta>0$: $\mathbb{E}\big[\prod c_{\mu_j}\overline{c_{\nu_j}}\big] = \sum_{A\in\mathrm{Mag}_{\mu,\nu}}\prod \binom{A_{ij}+\theta-1}{A_{ij}}$.
- Moment asymptotics: $\mathbb{E}|c_n|^{2k}/\mathbb{E}|c_n|^{2k} \to k!\,\Gamma(1-k\theta)/\Gamma(1-\theta)^k$ (Morris/Fyodorov-Bouchaud form) for $\theta k < 1$.
- HMC regularity threshold: $s_\theta = -\theta^2$ for $\theta\le 1$, $s_\theta = -(\sqrt\theta+1)^2/2$ for $\theta>1$ — sharp Sobolev exponent.
- Tight order of magnitude $|c_n|\asymp w_n$ where $w_n = n^{\theta-1}$ for $\theta\in(0,1)$, $w_n=(\log(1+n))^{-1/4}$ at $\theta=1$.

## Why it matters here
General background; no direct arena tie. The magic-square / Birkhoff-polytope combinatorics and the Tauberian + second-moment machinery could touch problems with extremal-combinatorics or autocorrelation flavor, but none of the 23 arena problems map directly onto secular coefficients of random matrices.

## Open questions / connections
- Extending Theorem 1.1's distributional limit from $\beta>4$ to all $\beta>2$ and (with renormalization) $\beta=2$ — the conjectured full-subcritical regime.
- Sharpening the supercritical ($\theta\in(1,2)$) exponent $(3-2\sqrt\theta)/(2-\theta)$ governing $\mathbb{E}|c_n-c_n^{(N)}|^2$ — $L^2$ comparison is known suboptimal.
- Volumes of Birkhoff polytopes (known only for $k\le 10$) directly control multiplicative constants in moments — connects to active enumerative combinatorics.

## Key terms
Circular beta ensemble, CUE, secular coefficients, characteristic polynomial, Gaussian multiplicative chaos, holomorphic multiplicative chaos, magic squares, Birkhoff polytope, Fyodorov-Bouchaud formula, Morris integral, Jack symmetric functions, Tauberian theorem, Sobolev regularity, Diaconis-Gamburd, log-correlated fields, Ewens sampling formula
