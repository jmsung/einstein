---
type: source
kind: paper
title: Loss landscapes and optimization in over-parameterized non-linear systems and neural networks
authors: Chaoyue Liu, Libin Zhu, Mikhail Belkin
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2003.00307
source_local: ../raw/2020-liu-loss-landscapes-optimization-over-parameterized.pdf
topic: general-knowledge
cites:
---

# Loss landscapes and optimization in over-parameterized non-linear systems and neural networks

**Authors:** Chaoyue Liu, Libin Zhu, Mikhail Belkin  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2003.00307

## One-line
Proposes the PL$^*$ (Polyak–Łojasiewicz variant) condition as the right replacement for local convexity when analyzing optimization of over-parameterized non-linear systems, and proves wide neural networks satisfy it.

## Key claim
For over-parameterized maps $F:\mathbb{R}^m\to\mathbb{R}^n$ ($m>n$) with square loss, $\mu$-PL$^*$ ($\|\nabla L(w)\|^2 \geq \mu L(w)$) holds wherever $\lambda_{\min}(K(w))\geq\mu$ for the tangent kernel $K(w)=DF(w)DF(w)^T$; if this holds in a ball of radius $R=O(1/\mu)$ around $w_0$, then (i) a global minimizer (interpolating solution) exists in the ball and (ii) GD/SGD converge exponentially with rate $(1-\eta\mu)^t$.

## Method
Tangent-kernel spectral analysis: reduce PL$^*$ verification to lower-bounding $\lambda_{\min}(K(w))$. Control change of $K$ across a ball via Hessian-tensor norm $\|H_F\|$ (mean-value-style bound), then apply to wide neural networks where $\|H_F\|=O(1/\sqrt{m})$ for linear-output-layer architectures (NTK regime). Extend to general nets, CNNs, ResNets via composition arguments — PL$^*$ is preserved under well-behaved input/output transformations.

## Result
Under-parameterized systems have $\lambda_{\min}(K(w))\equiv 0$ and cannot be PL$^*$; over-parameterized ones generically have a singular set $S_{\text{sing}}$ of codimension $m-n+1$, so PL$^*$ holds across most of $\mathbb{R}^m$. For Gaussian random Jacobians, $\mathbb{E}[\log\kappa(K)]<2\log(m/(m-n+1))+5$ — conditioning improves with over-parameterization. Explicit width requirements (Thm. 13): $m=\tilde\Omega(nR^{6L+2}/(\lambda_0-\mu\rho^{-2})^2)$ gives $\mu$-PL$^*$ in $B(w_0,R)$ for CNNs/ResNets. Local non-convexity (Prop. 2): if $\text{rank}(H_{F_i}(w^*))>2n$ for some $i$, no neighborhood of $w^*$ is convex.

## Why it matters here
General background; no direct arena tie. Tangentially relevant to compute routing intuition (well-conditioned ⇒ fast GD/SGD) and to understanding why some optimization landscapes in the project look "essentially non-convex" yet still admit gradient methods; the codimension-of-singular-set parameter-counting argument is a useful framing tool for landscape questions on parameterized math problems (e.g., parameter-rich sphere-packing / autocorrelation parameterizations).

## Open questions / connections
- Manifold extension: how does PL$^*$ behave when $F:M\to N$ between Riemannian manifolds (relevant whenever the parameterization has structural constraints)?
- Almost-over-parameterized regime: paper conjectures large models on big data traverse a PL$^*$ stretch before settling — formal characterization of the transition is open.
- Connections to accelerated methods (Nesterov, SGD+momentum) in the PL$^*$ regime — does the same condition number govern convergence rates?
- Relates to Polyak (1963), Łojasiewicz (1963), NTK [Jacot et al. 2018], Bassily–Belkin–Ma (SGD exponential convergence), Oymak–Soltanolkotabi (overparameterized nonlinear learning).

## Key terms
Polyak-Łojasiewicz condition, PL$^*$, tangent kernel, neural tangent kernel, NTK, over-parameterization, condition number, Hessian spectral norm, gradient descent convergence, uniform conditioning, singular set, wide neural networks, essential non-convexity, square loss, $\lambda_{\min}$, Belkin, Liu, Lojasiewicz
