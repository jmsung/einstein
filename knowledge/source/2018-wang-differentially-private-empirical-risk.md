---
type: source
kind: paper
title: "Differentially Private Empirical Risk Minimization Revisited: Faster and More General"
authors: Di Wang, Minwei Ye, Jinhui Xu
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1802.05251
source_local: ../raw/2018-wang-differentially-private-empirical-risk.pdf
topic: general-knowledge
cites:
---

# Differentially Private Empirical Risk Minimization Revisited: Faster and More General

**Authors:** Di Wang, Minwei Ye, Jinhui Xu  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1802.05251

## One-line
Faster differentially-private algorithms for empirical risk minimization (ERM) that achieve near-optimal utility with substantially reduced gradient complexity across strongly-convex, non-strongly-convex, high-dimensional, and non-convex (Polyak-Łojasiewicz) settings.

## Key claim
For $(\epsilon,\delta)$-DP ERM with $1$-smooth $1$-Lipschitz convex losses: DP-SVRG attains utility $\tilde O(p\log(n)/(n^2\epsilon^2\mu))$ in gradient complexity $O((n+\kappa)\log(n\epsilon\sqrt{\mu/p}))$ (vs $O(n^2)$ for prior DP-GD); DP-SVRG++ attains the optimal $O(\sqrt{p}/(n\epsilon))$ utility in $O(n\sqrt{L/\epsilon}\sqrt{p}+n\log(n\epsilon/\sqrt{p}))$ gradients; DP-AccMD reduces high-dim gradient complexity from $O(n^3)$ to $O(n^{1.5})$ with utility scaling in Gaussian width $G_C$; under Polyak-Łojasiewicz, DP-GD gives near-optimal $O(G^2 p\log^2(n)\log(1/\delta)/(n^2\epsilon^2))$.

## Method
Gradient-perturbation paradigm: inject Gaussian noise into the gradients of variance-reduced first-order optimizers (Prox-SVRG, SVRG++, Accelerated Mirror Descent, GD), with privacy accounting via the moments accountant of Abadi et al. and Rényi-divergence bounds. High-dimensional case uses Minkowski-norm geometry over a centrally symmetric convex set $C$, replacing $\sqrt{p}$ by the Gaussian width $G_C$. Non-convex analysis exploits the Polyak-Łojasiewicz inequality $\|\nabla F(x)\|^2 \ge 2\mu(F(x)-F^*)$ to recover linear-convergence-style rates.

## Result
DP-SVRG (Thm 4.1–4.2), DP-SVRG++ (Thm 4.3–4.4), DP-AccMD (Thm 5.3–5.4), DP-GD under PL (Thm 6.2) and for gradient-norm utility (Thm 6.3). Across all four regimes the paper improves either gradient complexity or utility (or both) vs Bassily-Smith-Thakurta 2014, Talwar-Thakurta-Zhang 2014/2015, and Zhang et al. 2017. Logistic-regression experiments on Covertype ($n=200{,}000$, $p=54$) confirm dominance over DP-GD at $\epsilon\in\{0.2,0.5,1\}$, $\delta=10^{-3}$.

## Why it matters here
General background; no direct arena tie. The paper is ML/privacy theory, not extremal combinatorics or sphere packing; it does not inform any of the 23 Einstein Arena problems.

## Open questions / connections
- Can the optimal utility bound be attained with gradient perturbation for non-smooth convex losses (e.g. SVM)?
- Lower bound on utility under the gradient-norm measure $\mathbb{E}\|\nabla F(x_\text{priv})\|^2$ for non-convex objectives is unknown.
- Extension to other structured non-convex classes (gradient-dominated, quasi-convex + locally-Lipschitz of Hazan-Levy-Shalev-Shwartz 2015, Kurdyka-Łojasiewicz of Li-Pong 2016).

## Key terms
differential privacy, empirical risk minimization, gradient perturbation, SVRG, Prox-SVRG, accelerated mirror descent, moments accountant, Gaussian mechanism, Polyak-Lojasiewicz condition, Gaussian width, Minkowski norm, strong convexity
