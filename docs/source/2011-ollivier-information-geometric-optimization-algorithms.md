---
type: source
kind: paper
title: "Information-Geometric Optimization Algorithms: A Unifying Picture via Invariance Principles"
authors: Y. Ollivier, Ludovic Arnold, A. Auger, N. Hansen
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1106.3708
source_local: ../raw/2011-ollivier-information-geometric-optimization-algorithms.pdf
topic: general-knowledge
cites:
---

# Information-Geometric Optimization Algorithms: A Unifying Picture via Invariance Principles

**Authors:** Y. Ollivier, Ludovic Arnold, A. Auger, N. Hansen  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1106.3708

## One-line
Derives a unified continuous-time black-box optimization framework (IGO) from natural-gradient ascent on any parametric distribution family, recovering CMA-ES, xNES, PBIL, cGA, and cross-entropy as special cases via invariance principles.

## Key claim
Following the natural gradient (w.r.t. Fisher metric) of the $P_\theta$-expectation of a quantile-rewritten objective $W_\theta^f$ yields a flow on parameter space $\Theta$ that is simultaneously invariant under (i) reparametrization of $\theta$, (ii) $X$-coordinate changes preserving the family $P_\theta$, and (iii) strictly increasing transformations of $f$ — and this flow is essentially the unique choice with minimal change of $P_\theta$ per unit objective improvement (Prop. 2: $\theta_t = \arg\max\{t \cdot g(\theta) + \mathrm{Ent}(P_\theta)\} + o(t)$ near the uniform start).

## Method
Replace $f$ with an adaptive monotone rewriting $W_\theta^f(x) = w(q_\theta(x))$ based on $P_\theta$-quantiles of $f$ (invariance under increasing transforms), then perform natural-gradient ascent $\dot\theta = I(\theta)^{-1} \partial_\theta \mathbb{E}_{P_\theta}[W_\theta^f]$ where $I$ is the Fisher information matrix. The continuous IGO flow is Euler-discretized and Monte-Carlo sampled to give explicit algorithms; an equivalent formulation (Thm. 10) characterizes the update as an infinitesimal weighted maximum-likelihood step, linking IGO to cross-entropy / IGO-ML (Thm. 12).

## Result
Specializing to Gaussian $P_\theta = \mathcal{N}(m, C)$ on $\mathbb{R}^d$ recovers a version of CMA-ES and xNES; Bernoulli $P_\theta$ on $\{0,1\}^d$ recovers PBIL and cGA; restricted Boltzmann machines yield a novel multimodal discrete optimizer. Speed bound (Prop. 20): $\|\dot\theta\|_{\text{Fisher}} \le \sqrt{\mathrm{Var}_{[0,1]} w}$, so the per-step KL change is bounded by the variance of the selection scheme $w$. Quantile monotonicity (Thm. proven in D.3): the $q$-quantile of $f$ under $P_{\theta_{t+\delta t}}$ is strictly less than that under $P_{\theta_t}$ unless the gradient vanishes.

## Why it matters here
Provides the principled foundation for CMA-ES — already the workhorse continuous optimizer on Einstein Arena problems with $\mathbb{R}^d$ search spaces (sphere packing, kissing, autocorrelation, equioscillation polish) — and explains *why* its invariance properties make it robust to bad parametrizations. The diversity-preservation result (Prop. 2) is directly relevant to multi-basin problems (P1, P11, P15, P16) where greedy descent collapses prematurely; suggests IGO/xNES variants as alternatives when CMA-ES loses diversity.

## Open questions / connections
- Can the quantile rewriting $W_\theta^f$ be tuned per problem (e.g. truncation vs smooth $w$) to balance convergence speed vs basin diversity for known multimodal arena problems?
- IGO on discrete $\{0,1\}^d$ via RBMs handles bit dependencies — applicable to combinatorial arena problems (Sidon-like, extremal graph) where PBIL/cGA assume independence?
- Relationship to information-geometric methods used by Zhou & Hu (2014) for non-differentiable optimization — does second-order info improve near-SOTA polish?
- The KL-step-size interpretation suggests a principled learning-rate schedule; not yet tested against CMA-ES default $c_\sigma$, $c_c$ heuristics on float64 polish near SOTA.

## Key terms
information-geometric optimization, IGO, natural gradient, Fisher information metric, CMA-ES, xNES, PBIL, cGA, cross-entropy method, Kullback-Leibler divergence, invariance, quantile rewriting, evolution strategies, estimation of distribution algorithms, restricted Boltzmann machine, Amari, Ollivier, Hansen
