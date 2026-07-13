<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: sci-math
domains: [sci-math, sci-stats]
title: "Information-Theoretic Lower Bounds on the Oracle Complexity of Stochastic Convex Optimization"
authors: [Alekh Agarwal, Peter L. Bartlett, Pradeep Ravikumar, Martin J. Wainwright]
year: 2010
source_url: https://arxiv.org/abs/1009.0571
drive_file_id: 1yNSlI82eTi24c6n_dpI5MfOGK2IaK3fQ
text_source: pdf
ingested_by: agent
---

# Information-Theoretic Lower Bounds on the Oracle Complexity of Stochastic Convex Optimization

**Authors:** Alekh Agarwal, Peter L. Bartlett, Pradeep Ravikumar, Martin J. Wainwright  ·  **Year:** 2010  ·  **Source:** https://arxiv.org/abs/1009.0571

## One-line
Proves tight minimax lower bounds on how many noisy gradient queries any stochastic algorithm needs to minimize a convex function, with sharp dependence on dimension, geometry, strong convexity, and sparsity.

## Key claim
For convex $L$-Lipschitz $f$ on $S \supseteq B_\infty(r)$ with a stochastic first-order oracle of variance $\sigma^2 \leq L^2$: $\epsilon^*_T = \Omega(Lr\sqrt{d/T})$ for $p \in [1,2]$ and $\Omega(Lr\, d^{1-1/p}/\sqrt{T})$ for $p > 2$. For $\gamma$-strongly convex functions on $B_\infty(r)$, the rate sharpens to $\Omega(L^2/(\gamma^2 T))$ in the well-conditioned regime. For $k$-sparse optima, $T = \Omega(L^2 r^2 k^2 \log(d/k)/\epsilon^2)$ — only logarithmic in ambient $d$.

## Method
Reduction from stochastic optimization to a multi-way hypothesis testing problem over a packing set of "hard" functions indexed by $\alpha \in \{-1,+1\}^d$ (or sparse variants). A novel optimization-tailored discrepancy $\rho(f_\alpha, f_\beta) := \inf_x \{f_\alpha(x)+f_\beta(x)\} - \inf_x f_\alpha(x) - \inf_x f_\beta(x)$ lower-bounds optimization error by Hamming distance. Fano's inequality plus KL-divergence bounds on the Bernoulli oracle responses then yield the query-count lower bounds.

## Result
Three matching lower bounds (convex Lipschitz, strongly convex, sparse-minimizer convex), each sharp because stochastic gradient descent or mirror descent with $\Phi_a(x) = \|x\|_a^2/(a-1)$ achieves them up to constants (Appendix C). Reveals a phase transition for strongly convex case between $1/T$ (well-conditioned) and $1/\sqrt{T}$ (poorly conditioned) regimes. Higher-order derivative oracles do not improve worst-case rates.

## Key terms
oracle complexity, stochastic convex optimization, minimax lower bound, Fano's inequality, packing set, strong convexity, sparse optimization, mirror descent, stochastic gradient descent, KL divergence, Lipschitz, Nemirovski-Yudin
