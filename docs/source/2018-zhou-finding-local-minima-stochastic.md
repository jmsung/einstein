---
type: source
kind: paper
title: Finding Local Minima via Stochastic Nested Variance Reduction
authors: Dongruo Zhou, Pan Xu, Quanquan Gu
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1806.08782
source_local: ../raw/2018-zhou-finding-local-minima-stochastic.pdf
topic: general-knowledge
cites:
---

# Finding Local Minima via Stochastic Nested Variance Reduction

**Authors:** Dongruo Zhou, Pan Xu, Quanquan Gu  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1806.08782

## One-line
Two first-order stochastic optimization algorithms (SNVRG⁺+Neon2) that find approximate local minima of nonconvex functions faster than prior variance-reduced methods, in both finite-sum and online settings.

## Key claim
For finite-sum nonconvex $F = \frac{1}{n}\sum_i f_i$, SNVRG⁺+Neon2$_{\text{finite}}$ reaches an $(\epsilon, \epsilon_H)$-second-order stationary point ($\|\nabla F\|_2 \le \epsilon$, $\lambda_{\min}(\nabla^2 F) \ge -\epsilon_H$) in $\widetilde{O}(n^{1/2}\epsilon^{-2} + n\epsilon_H^{-3} + n^{3/4}\epsilon_H^{-7/2})$ stochastic gradient evaluations, improving the $n^{2/3}\epsilon^{-2}$ first term of SVRG+Neon2. The online variant attains $\widetilde{O}(\epsilon^{-3} + \epsilon_H^{-5} + \epsilon^{-2}\epsilon_H^{-3})$, beating SCSG+Neon2 ($\epsilon^{-10/3}$) and Natasha2 ($\epsilon^{-3.25}$) in wide regimes.

## Method
Builds on **stochastic nested variance reduction (SNVRG)**: SVRG-style control variates extended to $K = \log\log B_0$ nested reference points/gradients per epoch, geometrically tuned batch sizes $B_l$ and inner loop lengths $T_l$. The variant **One-epoch-SNVRG⁺** randomizes total iterations $T \sim \text{Geom}(p)$ and outputs the *last* iterate (vs. uniform-random iterate in prior work), giving a last-iterate gradient bound. Composed with **Neon2** (Allen-Zhu & Li 2017) — a first-order negative-curvature extractor — to escape saddles whenever the gradient is small. Third-order smoothness improves $\epsilon_H^{-7/2} \to \epsilon_H^{-5/2}$ and $\epsilon_H^{-5} \to \epsilon_H^{-4}$.

## Result
- Theorem 5.4 (finite-sum): $\widetilde{O}\!\left(\frac{\Delta_F n^{1/2} L_1}{\epsilon^2} + \frac{\Delta_F n L_2^2}{\epsilon_H^3} + \frac{\Delta_F n^{3/4} L_1^{1/2} L_2^2}{\epsilon_H^{7/2}}\right)$ with prob $\ge 1/4$ (boostable).
- Online: $\widetilde{O}(\Delta_F \sigma L_1 \epsilon^{-3} + \Delta_F \sigma^2 L_2^2 \epsilon^{-2}\epsilon_H^{-3} + \Delta_F L_1^2 L_2^2 \epsilon_H^{-5})$.
- Under $L_3$-third-order smoothness: exponents on $\epsilon_H$ drop by half a unit, matching/beating FLASH (Yu et al. 2017a).
- Strictly first-order (no Hessian-vector products), Hessian-Lipschitz assumption required; sub-Gaussian stochastic gradient assumed in online case.

## Why it matters here
General background; no direct arena tie. Nonconvex large-scale finite-sum/stochastic optimization is not the regime for Einstein Arena problems (low-dim continuous geometry, LP/SDP, equioscillation), which are typically deterministic and benefit from mpmath polish or sequential CPU optimizers, not variance-reduced SGD. Could conceivably inform any future ML-style sub-problem (e.g. learned surrogates), but otherwise tangential.

## Open questions / connections
- Extends SNVRG (Zhou et al. 2018a) and the Neon/Neon2 line (Xu-Yang 2017; Allen-Zhu-Li 2017) for saddle escape via first-order oracles.
- Tightness: matches lower bound $\Omega(n^{1/2}\epsilon^{-2})$ for finite-sum first-order stationary; whether $n^{3/4}$ in the saddle term is optimal remains open.
- Can the constant-probability $1/4$ guarantee be replaced by a high-probability bound without the $\log(1/p)$ restart overhead?

## Key terms
SNVRG, variance reduction, SVRG, SCSG, Neon2, Natasha2, second-order stationary point, saddle point escape, negative curvature, nonconvex stochastic optimization, Hessian-Lipschitz, gradient complexity, third-order smoothness, cubic regularization, finite-sum optimization
