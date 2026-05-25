---
type: source
kind: paper
title: "Private Empirical Risk Minimization Beyond the Worst Case: The Effect of the Constraint Set Geometry"
authors: Kunal Talwar, Abhradeep Thakurta, Li Zhang
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1411.5417
source_local: ../raw/2014-talwar-private-empirical-risk-minimization.pdf
topic: general-knowledge
cites:
---

# Private Empirical Risk Minimization Beyond the Worst Case: The Effect of the Constraint Set Geometry

**Authors:** Kunal Talwar, Abhradeep Thakurta, Li Zhang  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1411.5417

## One-line
Replaces the dimension factor $\sqrt{p}$ in differentially-private ERM error bounds with the Gaussian width $G_C$ of the constraint set, via noisy Mirror Descent and noisy Frank-Wolfe.

## Key claim
For $(\varepsilon,\delta)$-DP convex ERM with $L$-Lipschitz losses, noisy Mirror Descent achieves excess risk $\tilde O(L G_C / (\varepsilon n))$, and on the $\ell_1$-ball with $\ell_\infty$-bounded data (LASSO) noisy Frank-Wolfe achieves $\tilde O((n\varepsilon)^{-2/3})$ — matched by an $\Omega(1/(n\log n)^{2/3})$ lower bound.

## Method
Two algorithms with constraint-set-aware geometry: (1) **Noisy Mirror Descent** — at each step add Gaussian noise to the gradient and take a Bregman-projection step under a potential $\Psi$ that is 1-strongly convex w.r.t. a norm $\|\cdot\|_Q$ tailored to $C$ (e.g. $\Psi(\theta)=\tfrac{1}{4(q-1)}\|\theta\|_{Q,q}^2$ with $q=\log k/(\log k-1)$ for polytopes with $k$ vertices). (2) **Noisy Frank-Wolfe** — at each iteration pick a vertex of the polytope via the exponential / report-noisy-max mechanism on linear scores $\langle s, \nabla L(\theta_t)\rangle$, then convex-combine. Lower bound uses fingerprinting codes (Bun-Ullman-Vadhan / Tardos codes padded as in DTTZ14).

## Result
- Mirror Descent: $R(A) = O(L_2 G_C \log(n/\delta)/(\varepsilon n))$; for polytopes $G_C \asymp \|C\|_2\sqrt{\log k}$, giving $O(L_2 \|C\|_2 \sqrt{\log k}\log(n/\delta)/(\varepsilon n))$.
- Strongly convex: $\tilde O\big(L^2(G_C^2+\|C\|_2^2)/(\Delta(n\varepsilon)^2)\big)$ — quadratic-in-$n$ improvement.
- Frank-Wolfe (polytope, $\ell_1$-Lipschitz): $R(A)=O\big(\Gamma_L^{1/3}(L_1\|C\|_1)^{2/3}\log(nk)\log(1/\delta)/(n\varepsilon)^{2/3}\big)$.
- LASSO corollary: $R(A)=O(\log(np/\delta)/(n\varepsilon)^{2/3})$.
- Matching lower bound for $\ell_1$-LASSO: $\Omega(1/(n\log n)^{2/3})$.

## Why it matters here
General background; no direct arena tie — this is about differential privacy in ML, not optimization-landscape geometry for arena problems. The only mildly relevant idea is the **Gaussian width** $G_C = \mathbb{E}_g[\sup_{\theta\in C}\langle\theta,g\rangle]$ as a constraint-set complexity measure (e.g. $G_{\ell_1\text{-ball}}=\Theta(\sqrt{\log p})$ vs $G_{\ell_2\text{-ball}}=\Theta(\sqrt{p})$), which conceptually overlaps with the LP / Cohn-Elkies framing of constrained optimization but does not give a tool the agent can deploy on the 23 arena problems.

## Open questions / connections
- Connects to Chandrasekaran-Recht-Parrilo-Willsky on Gaussian-width-driven sample complexity for convex inverse problems.
- Whether the strongly-convex bound is tight beyond the $\ell_2/\ell_2$ case studied in BST14.
- Extension to non-convex losses, and to losses Lipschitz w.r.t. norms other than $\ell_2$ or $\ell_1$ (e.g. matrix Schatten norms beyond the nuclear ball mention).

## Key terms
differential privacy, empirical risk minimization, Gaussian width, mirror descent, Frank-Wolfe, LASSO, sparse linear regression, fingerprinting codes, Bregman divergence, exponential mechanism, curvature constant, constraint set geometry
