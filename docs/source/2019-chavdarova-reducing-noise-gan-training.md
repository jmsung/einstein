---
type: source
kind: paper
title: Reducing Noise in GAN Training with Variance Reduced Extragradient
authors: Tatjana Chavdarova, G. Gidel, F. Fleuret, Simon Lacoste-Julien
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1904.08598
source_local: ../raw/2019-chavdarova-reducing-noise-gan-training.pdf
topic: general-knowledge
cites:
---

# Reducing Noise in GAN Training with Variance Reduced Extragradient

**Authors:** Tatjana Chavdarova, G. Gidel, F. Fleuret, Simon Lacoste-Julien  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1904.08598

## One-line
A variance-reduced extragradient method (SVRE) that stabilizes stochastic min-max (GAN) training where vanilla stochastic extragradient provably diverges.

## Key claim
Stochastic extragradient (SEG) diverges geometrically on a simple strongly-monotone bilinear stochastic game (Thm. 1), while SVRE — combining SVRG-style control variates with Korpelevich's extrapolation step — converges linearly at rate $\ln(1/\epsilon)\times(n+\bar{\ell}/\mu)$ for $\bar\ell$-cocoercive, $\mu$-strongly-monotone operators, and is adaptive to local strong monotonicity when $\bar\ell = O(\bar L)$ (Thm. 2).

## Method
Use the finite-sum structure $L_G = \tfrac1n\sum L_G^i$, $L_D = \tfrac1n\sum L_D^i$, periodically snapshot $(\theta^S,\varphi^S)$ with full-batch gradient $\mu^S$, and form SVRG-style unbiased estimators $d^i(\omega) = (\nabla L^i(\omega) - \nabla L^i(\omega^S))/(n\pi_i) + \mu^S$. Plug these into Korpelevich's two-step extragradient: an extrapolation step to $\tilde\omega$, then an update using a *fresh independent sample* of $d$ evaluated at $\tilde\omega$. Epoch length is sampled $N\sim\text{Geom}(1/n)$ (Hofmann et al. $q$-memorization framework) so hyperparameters do not depend on $\mu$.

## Result
For $(\mu_\theta,\mu_\varphi)$-strongly-monotone, $(\bar\ell_\theta,\bar\ell_\varphi)$-cocoercive games, SVRE with $\eta \le 1/(40\bar\ell)$ achieves $E\|\omega_t-\omega^*\|^2 \le (1 - \min(\tfrac{\eta_\theta\mu_\theta}{4}+\tfrac{11\eta_\theta^2\bar\gamma_\theta^2}{25}, \tfrac{\eta_\varphi\mu_\varphi}{4}+\tfrac{11\eta_\varphi^2\bar\gamma_\varphi^2}{25}, \tfrac{2}{5n}))^t \|\omega_0-\omega^*\|^2$. Since $\ell\in[L, L^2/\mu]$, this strictly improves on Palaniappan-Bach's accelerated SVRG rate $\ln(1/\epsilon)(n+\sqrt{n}\bar L/\mu)$ when $\ell\approx L$. Empirically SVRE matches batch-extragradient on MNIST, beats SE-Adam on SVHN (FID 24.0 vs 40.0), and warm-start SVRE improves CIFAR-10 FID from 18.65 to 16.77.

## Why it matters here
General background; no direct arena tie — the Einstein Arena pipeline is currently CMA-ES / parallel tempering / mpmath-polish on deterministic non-convex objectives, not minimax/stochastic games. Could become relevant only if a future problem framing introduces an adversarial inner verifier (e.g., GAN-style approximation of an extremal configuration) or if `gpu_tempering` is reformulated with control variates.

## Open questions / connections
- Does the cocoercivity-vs-Lipschitz constant gap $\ell\in[L,L^2/\mu]$ have a discrete-optimization analogue worth checking against our basin-hopping / equioscillation pipelines?
- Variance-reduced *extrapolation* might apply to Remez exchange or LP column-generation, where each "gradient" is a costly evaluation — but the finite-sum structure is missing.
- The "noise breaks extragradient on a bilinear game" result is a sharper warning than the usual SGD-on-saddle-points lore; relevant only if/when a stochastic verifier is introduced.

## Key terms
SVRE, stochastic variance reduced extragradient, SVRG, extragradient method, Korpelevich, GAN training, saddle-point optimization, cocoercivity, strong monotonicity, variational inequality, Palaniappan-Bach, minimax game
