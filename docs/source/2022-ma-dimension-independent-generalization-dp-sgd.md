---
type: source
kind: paper
title: Dimension Independent Generalization of DP-SGD for Overparameterized Smooth Convex Optimization
authors: Yi-An Ma, T. Marinov, Tong Zhang
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2206.01836
source_local: ../raw/2022-ma-dimension-independent-generalization-dp-sgd.pdf
topic: general-knowledge
cites:
---

# Dimension Independent Generalization of DP-SGD for Overparameterized Smooth Convex Optimization

**Authors:** Yi-An Ma, T. Marinov, Tong Zhang  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2206.01836

## One-line
Proves DP-SGD attains the optimal $\tilde{O}(n^{-1/2})$ excess generalization error with $(\epsilon,\delta)$-differential privacy at $\epsilon = \tilde{O}(n^{-1/4})$ for smooth convex losses, with a bound that depends on $\mathrm{trace}(\tilde{H}_D)$ rather than the ambient dimension $d$.

## Key claim
For overparameterized smooth convex problems (e.g. logistic regression with $\|x\|_2 \le 1$), DP-SGD achieves excess risk $\ell(w,D) + O(G\|w\|_2/\sqrt{n} + \eta_0^2 \mathrm{trace}(\tilde{H}_D)/(\epsilon^2 n))$ — replacing the pessimistic $\sqrt{d\log(1/\delta)}/(\epsilon n)$ term of Bassily et al. [2019] with a trace-of-Hessian term that stays bounded as $d \to \infty$.

## Method
Identifies DP-SGD with Stochastic Gradient Langevin Dynamics (SGLD) and imports the dimension-independent SGLD convergence analysis of Freund-Ma-Zhang [2021] (composite-optimization viewpoint, $W_2$-Wasserstein + regularized-entropy regret). Combines this with: (i) stability analysis à la Hardt-Recht-Singer for generalization, (ii) Rényi-DP / strong-composition / privacy-amplification-by-subsampling (Balle-Barthe-Gaboardi, Mironov) for the privacy accounting, in both single-pass (mini-batched, last-iterate via Shamir-Zhang) and multi-pass (online) regimes.

## Result
Theorem 1 (single-pass, $T=n$): last iterate $w_T$ is $(2\epsilon,\delta)$-DP with excess generalization $\le \ln(n)(G\|w\|_2^2 + 1.5\eta_0^2 G)/(\eta_0\sqrt{n}) + \eta_0^2 \log(1/\delta)\,\mathrm{trace}(\tilde{H}_D)/(\epsilon^2 n)$. Theorem 2 (multi-pass, $T=n^\alpha\epsilon^2$, $1\le\alpha\le 2$): $(3\epsilon\ln(2/\delta)+3\epsilon^2,\delta)$-DP on all iterates with averaged excess risk $O(G\|w\|^2_2\ln(T/\delta)/(\eta_0\sqrt{n}) + \eta_0^2\,\mathrm{trace}(\tilde{H}_D) + \eta_0 G\sqrt{n\ln(1/\delta)}/(\epsilon^2 n^{\alpha-1}))$; choosing $\epsilon=n^{-1/4}, \alpha=2$ gives $\tilde{O}(n^{-1/2})$ at $T=n^{1.5}$ work.

## Why it matters here
General background; no direct arena tie. The DP-utility tradeoff is unrelated to sphere packing / autocorrelation / kissing / extremal-graph problems in the arena, though the underlying machinery (SGLD as smoothed-objective optimizer, Wasserstein regret bounds, last-iterate convergence) is methodologically adjacent to noisy-gradient samplers we use for optimization.

## Open questions / connections
- Extending the trace-of-Hessian bound from unconstrained to constrained convex optimization (left as explicit open problem in §3.1).
- Sharpening log factors via Rényi-DP strong composition (Abadi et al., Mironov) instead of $(\epsilon,\delta)$-DP composition.
- Comparison with Song et al. [2021], which uses rank rather than trace of the Hessian — trace is typically much smaller in practice but the rank-based bounds apply in constrained settings.

## Key terms
DP-SGD, differential privacy, stochastic gradient Langevin dynamics, SGLD, dimension-independent bounds, overparameterized convex optimization, trace of Hessian, Rényi differential privacy, privacy amplification by subsampling, Wasserstein regret, last-iterate convergence, logistic regression, Gaussian mechanism, strong composition theorem
