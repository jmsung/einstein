---
type: source
kind: paper
title: The Complexity of Making the Gradient Small in Stochastic Convex Optimization
authors: Dylan J. Foster, Ayush Sekhari, Ohad Shamir, N. Srebro, Karthik Sridharan, Blake E. Woodworth
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1902.04686
source_local: ../raw/2019-foster-complexity-making-gradient-small.pdf
topic: general-knowledge
cites:
---

# The Complexity of Making the Gradient Small in Stochastic Convex Optimization

**Authors:** Dylan J. Foster, Ayush Sekhari, Ohad Shamir, N. Srebro, Karthik Sridharan, Blake E. Woodworth  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1902.04686

## One-line
Nearly matching upper and lower bounds on the oracle complexity of finding $\epsilon$-stationary points ($\|\nabla F(x)\|\le\epsilon$) in stochastic convex optimization, separately for local stochastic first-order and global (statistical-learning) oracles.

## Key claim
The local stochastic complexity decomposes as (deterministic optimization term) $+$ (sample term): $\tilde\Theta(\sqrt{HR}/\sqrt\epsilon + \sigma^2/\epsilon^2)$ for domain-bounded and $\tilde\Theta(\sqrt{H\Delta}/\epsilon + \sigma^2/\epsilon^2)$ for range-bounded $H$-smooth convex $F$, while the global/sample complexity depends only **logarithmically** on $H$ — an exponential separation between the two models in the smoothness dependence.

## Method
Extends Allen-Zhu's "recursive regularization" (SGD3): solve a sequence of subproblems $F^{(t)}(x)=F(x)+\lambda\sum_{k\le t}2^{k-1}\|x-\hat x_k\|^2$, "zooming in" with increasingly strong regularizers. Inner solver is swapped from SGD to AC-SA2 (a restarted Ghadimi–Lan accelerated stochastic approximation) for the local model, and to regularized ERM (finite-sum, solved by standard ERM methods) for the global model. Matching lower bounds come from (i) a Gaussian-orthogonal-direction construction for the $\sigma^2/\epsilon^2$ term and (ii) reduction from noisy binary search (Feige et al.; Karp–Kleinberg) to force the $\log(HR/\epsilon)$ factor.

## Result
For $F\in\mathcal F_{DB}[H,0;R]$ with stochastic first-order oracle: upper $\tilde O(\sqrt{HR}/\sqrt\epsilon + (\sigma^2/\epsilon^2)\log^3(HR/\epsilon))$, lower $\Omega(\sqrt{HR}/\sqrt\epsilon + (\sigma^2/\epsilon^2)\log(HR/\epsilon))$. For the global oracle (samples), upper $\tilde O((\sigma^2/\epsilon^2)\log^3(HR/\epsilon))$ with no polynomial $H$ term, matched by a $\Omega(\sigma^2/\epsilon^2)$ lower bound; in 1D, smoothness can be removed entirely (Theorem 5: $O((\sigma^2/\epsilon^2)\log(L/\epsilon))$ via ERM + held-out gradient selection).

## Why it matters here
General background; no direct arena tie. Loosely relevant to compute-router intuition (when statistical $\sigma^2/\epsilon^2$ samples dominate vs deterministic accelerated-gradient $\sqrt{HR/\epsilon}$ iterations), and to mpmath/AC-SA-style polish where the "stationarity vs suboptimality" gap matters for verification — but no concept page or arena problem currently leans on stochastic-convex stationarity rates.

## Open questions / connections
- Extending the local/global decomposition and the recursive-regularization technique to **non-convex** stochastic optimization (the original motivation; here only convex is closed).
- Computational–statistical tradeoff hinted at: ERM-based global algorithm beats SGD in sample count when $H\gg\sigma^2$, but needs finite-sum solver — is the compute overhead tight?
- Connection to Carmon et al. (2017a,b) deterministic stationary-point lower bounds, and to Davis–Drusvyatskiy (2018) recursive regularization for Moreau envelopes of Lipschitz (non-smooth) functions.

## Key terms
stochastic convex optimization, stationary point, oracle complexity, recursive regularization, SGD3, AC-SA, accelerated stochastic approximation, Ghadimi–Lan, empirical risk minimization, sample complexity, noisy binary search lower bound, smoothness dependence, Allen-Zhu, Foster–Sekhari–Shamir–Srebro–Sridharan–Woodworth
