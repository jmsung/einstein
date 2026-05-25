---
type: source
kind: paper
title: A Modern Introduction to Online Learning
authors: Francesco Orabona
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1912.13213
source_local: ../raw/2019-orabona-modern-introduction-online-learning.pdf
topic: general-knowledge
cites:
---

# A Modern Introduction to Online Learning

**Authors:** Francesco Orabona  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1912.13213

## One-line
A graduate-level textbook on online convex optimization (OCO) that develops regret-minimization algorithms in a unified framework via Online Mirror Descent (OMD) and Follow-The-Regularized-Leader (FTRL).

## Key claim
Essentially every modern online-learning algorithm — OGD, OSD, AdaGrad, Exponentiated Gradient, Hedge/AdaHedge, Online Newton Step, Vovk–Azoury–Warmuth, Perceptron, Exp3, UCB, Tsallis-INF, Universal Portfolio — is an instantiation of OMD or FTRL with a chosen regularizer/mirror map, and their regret bounds follow from a small set of master lemmas (Be-the-Leader, one-step OMD, strong convexity / smoothness duality, local-norm bounds). Canonical rates: $O(\sqrt{T})$ for Lipschitz convex losses, $O(\log T)$ for strongly convex losses, $O(L^\star)$ adaptive bounds, and parameter-free $O(\|u\|\sqrt{T \log(\|u\|T)})$ unconstrained.

## Method
Convex-analysis machinery (Fenchel conjugates, Bregman divergences, strong convexity ↔ smoothness duality) is used to derive two master algorithms — OMD (lazy/eager mirror step) and FTRL (regularized minimization of cumulative loss) — and reduce all other algorithms to choice of regularizer + linearization. Lower bounds are obtained via the probabilistic/Khintchine method and coin-betting dualities; parameter-free algorithms are built from the coin-betting game via the Krichevsky–Trofimov bettor.

## Result
Full proofs of: (i) $O(\sqrt{T})$ regret for OSD with $\eta_t = D/(G\sqrt{t})$; (ii) $O(\log T)$ regret for strongly convex losses; (iii) AdaGrad's $\sum_t \|g_t\|^2$-adaptive bound; (iv) matching $\Omega(\sqrt{T})$ and $\Omega(\sqrt{T \log T})$ lower bounds for bounded/unconstrained OLO; (v) Online Newton Step's $O(d \log T)$ for exp-concave losses; (vi) Universal Portfolio's $O(d \log T)$ regret giving the Krichevsky–Trofimov $\tfrac{1}{2}\log T$ redundancy bound; (vii) Tsallis-INF's best-of-both-worlds $O(\sqrt{KT})$ adversarial / $O(\log T)$ stochastic bandit regret; (viii) online→batch, online→Rademacher, online→PAC-Bayes, and online→time-uniform concentration (Ville's inequality, confidence sequences) conversions.

## Why it matters here
General methodology / no direct arena tie — none of the 23 Einstein problems are online-learning problems. The relevant transferable pieces are: (a) **Bregman divergence and Fenchel conjugate machinery** as a unified language for "right geometry → right algorithm" decisions (relevant to picking parameterizations in optimization-heavy problems like P1, P11, P15, P16); (b) **strong convexity ↔ smoothness duality** as a diagnostic for why certain optimizer convergence rates degrade; (c) the **adversarial-vs-stochastic stance** as a robustness frame for verifier-drift scenarios.

## Open questions / connections
- Whether OMD/FTRL geometry tools (mirror maps, local norms) can inform parameterization choice for non-convex packing/sphere-packing landscapes, where the "right geometry" question is wide open.
- Connections between Universal Portfolio / coin-betting confidence sequences and the project's triple-verify rule: time-uniform concentration could in principle give anytime-valid bounds on optimizer convergence.
- Parameter-free algorithms (no learning-rate tuning) raise the question of analogous parameter-free local optimizers — relevant to the "no validation set" pain in this project.

## Key terms
online convex optimization, regret minimization, Online Mirror Descent, Follow-the-Regularized-Leader, AdaGrad, Bregman divergence, Fenchel conjugate, strong convexity, exp-concave, Online Newton Step, Exponentiated Gradient, coin betting, parameter-free, Universal Portfolio, Krichevsky–Trofimov, multi-armed bandit, Tsallis-INF, PAC-Bayes, Rademacher complexity, Orabona
