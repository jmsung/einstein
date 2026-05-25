---
type: source
kind: paper
title: On the rate of convergence in Wasserstein distance of the empirical measure
authors: N. Fournier, A. Guillin
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1312.2128
source_local: ../raw/2013-fournier-rate-convergence-wasserstein-distance.pdf
topic: general-knowledge
cites:
---

# On the rate of convergence in Wasserstein distance of the empirical measure

**Authors:** N. Fournier, A. Guillin  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1312.2128

## One-line
Sharp non-asymptotic $L^p$ bounds and concentration inequalities for the Wasserstein-$p$ distance between an empirical measure $\mu_N$ and its underlying law $\mu$ on $\mathbb{R}^d$, valid for all $p>0$, $d\ge 1$.

## Key claim
If $M_q(\mu)<\infty$ for some $q>p$, then $\mathbb{E}[T_p(\mu_N,\mu)] \le C M_q^{p/q}(\mu)\cdot r(N,p,d,q)$ where the rate $r$ is $N^{-1/2}+N^{-(q-p)/q}$ if $p>d/2$, $N^{-1/2}\log(1+N)+N^{-(q-p)/q}$ if $p=d/2$, and $N^{-p/d}+N^{-(q-p)/q}$ if $p\in(0,d/2)$ — matching known lower bounds up to a possible $\sqrt{\log N}$ at $p=d/2$.

## Method
Builds on Dereich–Scheutzow–Schottstedt's dyadic-cube distance $D_p(\mu,\nu)$ — sum over scales $\ell\ge 1$ of $2^{-p\ell}\sum_{F\in\mathcal{P}_\ell}|\mu(F)-\nu(F)|$ on $(-1,1]^d$, extended to $\mathbb{R}^d$ via dyadic shells $B_n$. Shows $T_p\le \kappa_{p,d} D_p$, then controls $D_p(\mu_N,\mu)$ cell-by-cell via Binomial concentration (Bennett/Bernstein) and a Poissonization trick to gain independence across cells. Truncation at radius $R\sim(\log N)^{1/\alpha}$ handles non-compact support under exponential moments.

## Result
**Theorem 1** (moments): the three-regime bound above, sharp by explicit lower-bound examples (Dirac mixtures, uniform on $[-1,1]^d$, power-law tails). **Theorem 2** (concentration): $\Pr(T_p(\mu_N,\mu)\ge x) \le a(N,x)\mathbf{1}_{x\le 1}+b(N,x)$ with $a$-tail $\exp(-cNx^2)$, $\exp(-cN(x/\log(2+1/x))^2)$, or $\exp(-cNx^{d/p})$ in the three dimensional regimes, plus a $b$-tail matching Fuk–Nagaev / Borovkov shapes under polynomial / stretched-exponential moments. Extends to $\rho$-mixing stationary sequences, Markov chains with $L^2$ spectral gap, and McKean–Vlasov particle systems.

## Why it matters here
General background; no direct arena tie. The dyadic-scale decomposition is a generic recipe for empirical-measure convergence that could inform any sampling / quantization step in the agent's optimization (e.g., when measuring how well an $N$-point configuration approximates a continuous target measure for sphere packing or autocorrelation problems).

## Open questions / connections
- Can the $\log(1+N)$ at $p=d/2$ be sharpened to $\sqrt{\log N}$ as Ajtai–Komlós–Tusnády suggests for $d=2$?
- Can concentration inequalities be obtained for $\rho$-mixing / Markov / particle-system cases (only moment bounds given)?
- For smooth / structured $\mu$ in $d\ge 3$, Talagrand's $N^{-p/d}$ rate beats $N^{-1/2}$ for large $p$ — when does the agent's empirical measure fall in this regime?

## Key terms
Wasserstein distance, empirical measure, transportation cost, dyadic partition, concentration inequality, Fuk-Nagaev, Bennett inequality, Poissonization, $\rho$-mixing, McKean-Vlasov, quantization, Dereich-Scheutzow-Schottstedt, Talagrand, Ajtai-Komlós-Tusnády
