---
type: source
kind: paper
title: Between Stochastic and Adversarial Online Convex Optimization: Improved Regret Bounds via Smoothness
authors: Sarah Sachs, Hédi Hadiji, Tim van Erven, Cristóbal Guzmán
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2202.07554v2
source_local: ../raw/2022-sachs-between-stochastic-adversarial-online.pdf
topic: general-knowledge
cites: 
---

# Between Stochastic and Adversarial Online Convex Optimization: Improved Regret Bounds via Smoothness

**Authors:** Sarah Sachs, Hédi Hadiji, Tim van Erven, Cristóbal Guzmán  ·  **Year:** 2022  ·  **Source:** http://arxiv.org/abs/2202.07554v2

## One-line
Interpolates between i.i.d. stochastic and fully adversarial online convex optimization, giving regret bounds in terms of cumulative gradient variance $\sigma_T$ and adversarial variation $\Sigma_T$ that smoothly degrade between the two regimes.

## Key claim
For Optimistic FTRL with smooth expected losses (smoothness constant $L$), $E[R_T(u)] = O(D(\bar\sigma_T + \bar\Sigma_T)\sqrt{T} + LD^2)$; under additional $\mu$-strong convexity, $E[R_T(u)] = O(\tfrac{1}{\mu}(\sigma_{\max}^2 + \Sigma_{\max}^2)\log T + LD^2\kappa\log\kappa)$. Matching lower bounds (Thms 6, 8) show both are tight.

## Method
Optimistic Follow-the-Regularized-Leader (OFTRL) with adaptive AdaHedge/AdaFTRL-style stepsize $\eta_t = D^2/(\nu + \sum_{s<t}\eta_s\|g_s-M_s\|^2)$ and optimistic prediction $M_t = g_{t-1}$. For strongly convex losses, OFTL is run on a surrogate $\ell_t(x) = \langle g_t, x-x_t\rangle + \tfrac{\mu}{2}\|x-x_t\|^2$. The key trick: retain a *negative* Bregman/quadratic term $-\tfrac{\mu t}{4}\|x_t-x_{t+1}\|^2$ in the analysis and cancel $E\|\nabla F_t(x_t)-\nabla F_t(x_{t-1})\|^2 \le L^2 E\|x_t-x_{t-1}\|^2$ via smoothness — same idea Nemirovski (2005) used for extra-gradient $O(1/T)$ rates.

## Result
Recovers the standard $O(DG\sqrt{T})$ adversarial bound when $\bar\sigma_T = 0$, and matches stochastic accelerated gradient descent rates $O(\sigma\sqrt{T} + L)$ in the i.i.d. case — the first such direct regret-analysis derivation for general convex smooth losses (previously only known for linear losses via Rakhlin–Sridharan). Applications: adversarially corrupted i.i.d. gives $E[R_T] \le R_T^s + O(D\sqrt{GC})$ for corruption budget $C$; single-pass random-order model gives $O(D\sigma_1\sqrt{T\log(e\tilde\sigma_1^2/\sigma_1^2)})$, improving the leading $G$ to $\sigma_1$ over Sherman et al. (2021).

## Why it matters here
General background; no direct arena tie. Relevant only as methodology — the "keep the negative quadratic term" trick is a generic acceleration device that could inform adaptive-stepsize design in iterative optimizers (basin-hopping, CMA-ES) where stochastic gradients meet adversarial restarts, but no Einstein Arena problem is online/regret-shaped.

## Open questions / connections
- Can the smoothness constant $L$ be learned online without paying the additive $(L_0 + L^2/L_0)D^2$ price the paper flags?
- Extends Hazan & Kale (2010) gradual-variation bounds and Rakhlin–Sridharan (2013) optimistic OCO; complements Joulani et al. (2020) stochastic acceleration via anytime online-to-batch.
- Random-order model results (Sherman et al. 2021, Garber et al. 2020) — can the $\sqrt{\log T}$ gap vs i.i.d. sampling-with-replacement be closed?

## Key terms
online convex optimization, OCO, stochastic convex optimization, regret bounds, optimistic FTRL, OFTRL, smoothness, gradient variance, adversarial variation, random order model, adversarial corruption, Nemirovski extra-gradient, stochastic accelerated gradient descent, AdaHedge
