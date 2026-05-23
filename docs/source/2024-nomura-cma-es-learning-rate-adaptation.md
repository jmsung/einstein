---
type: source
kind: paper
title: CMA-ES with Learning Rate Adaptation
authors: Masahiro Nomura, Youhei Akimoto, Isao Ono
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2401.15876v2
source_local: ../raw/2024-nomura-cma-es-learning-rate-adaptation.pdf
ingested_for_concept: cma-es-with-warmstart.md
cites: 
---

# CMA-ES with Learning Rate Adaptation

**Authors:** Masahiro Nomura, Youhei Akimoto, Isao Ono  ·  **Year:** 2024  ·  **Source:** http://arxiv.org/abs/2401.15876v2

## One-line
Introduces LRA-CMA-ES, a CMA-ES variant that online-adapts the mean/covariance learning rates $\eta_m, \eta_\Sigma$ to maintain a constant signal-to-noise ratio, removing the need for manual learning-rate tuning on multimodal and noisy problems.

## Key claim
The optimal learning rate for CMA-ES is approximately $\eta^* \approx 1/(1 + \mathrm{SNR}^{-1})$ under the assumption $H \approx cF$ (Hessian proportional to Fisher information); maintaining $\mathrm{SNR} = \alpha\eta$ via the proposed LRA mechanism solves well-structured multimodal problems (Rastrigin, Schaffer, Bohachevsky, Griewank) and strong-noise variants ($\sigma_n^2 = 10^6$) at default population size $\lambda = 4 + \lfloor 3\ln d\rfloor$, where fixed-$\eta$ CMA-ES fails.

## Method
Views CMA-ES through the IGO framework as Euler–Maruyama discretization of an SDE $d\theta = g(\theta)dt + \sqrt{\eta/\lambda}\,R(\theta)dW$, showing that decreasing $\eta$ and increasing $\lambda$ play equivalent roles (the ratio $\eta/\lambda$ controls noise). Derives optimal $\eta$ from a second-order Taylor expansion of expected improvement. Estimates SNR online from exponential moving averages $E$ and $V$ of update direction and squared norm, using the Fisher-norm-invariant ratio $\|E[\Delta]\|_F^2 / (E[\|\Delta\|_F^2] - \|E[\Delta]\|_F^2)$, then adapts $\eta_m, \eta_\Sigma$ independently to track target SNR $\alpha$.

## Result
LRA-CMA-ES matches or beats fixed-$\eta$ CMA-ES across noiseless multimodal benchmarks (Sphere, Ellipsoid, Rosenbrock, Ackley, Schaffer, Rastrigin, Bohachevsky, Griewank) up to $d=40$ without any $\eta$ tuning. On noisy problems with $\sigma_n^2 \in \{1, 10^6\}$ it strictly outperforms PSA-CMA-ES (state-of-the-art population-size adaptation) — e.g., on noisy Rastrigin with $\sigma_n^2=10^6$, PSA stalls while LRA continues to improve. Theoretical SNR analysis on the Sphere gives $\mathrm{SNR} \approx \lambda/(d-1) \cdot (\boldsymbol{w}^T\boldsymbol{n}_{(\lambda)})^2/(\|\boldsymbol{w}\|^2\|\boldsymbol{n}_{(\lambda)}\|^2) \lesssim 1$ for $\lambda \lesssim 4(d-1)$, justifying the small-SNR approximation $1/(1+\mathrm{SNR}^{-1}) \approx \mathrm{SNR}$.

## Why it matters here
Directly relevant to compute-router decisions for problems where CMA-ES is in the toolkit (sphere packing parameterizations, kissing-number configurations, discrete-geometry optimization). Replaces the population-size-vs-learning-rate tuning burden with a single SNR target, and is more parallel-friendly than $\lambda$-adaptation since $\lambda$ stays fixed — relevant for Modal A100/H100 large-pop float64 runs flagged in `compute-router.md`.

## Open questions / connections
- Fails on 40-D Schaffer despite fixed-small-$\eta$ CMA-ES succeeding; mechanism unclear and needs SNR-trace analysis.
- Hyperparameters $\beta_m, \beta_\Sigma, \alpha, \gamma$ chosen empirically; principled scaling like $\beta_m = O(1/d), \beta_\Sigma = O(1/d^2), \alpha = O(\lambda/d)$ proposed but unverified for multimodal/noisy regimes.
- Does not solve weakly-structured multimodals — needs BIPOP/IPOP-style restart integration, left as future work.

## Key terms
CMA-ES, covariance matrix adaptation, learning rate adaptation, signal-to-noise ratio, IGO framework, information-geometric optimization, natural gradient, Fisher information, evolution strategy, multimodal optimization, noisy optimization, Rastrigin, PSA-CMA-ES, population size adaptation, Nomura, Akimoto
