---
type: source
kind: paper
title: Lower complexity bounds of first-order methods for convex-concave bilinear saddle-point problems
authors: Yuyuan Ouyang, Yangyang Xu
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1808.02901
source_local: ../raw/2018-ouyang-lower-complexity-bounds-first-order.pdf
topic: general-knowledge
cites:
---

# Lower complexity bounds of first-order methods for convex-concave bilinear saddle-point problems

**Authors:** Yuyuan Ouyang, Yangyang Xu  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1808.02901

## One-line
Proves that for convex-concave bilinear saddle-point problems (and affinely constrained smooth convex optimization), first-order methods cannot beat $O(1/t)$ in the convex case and $O(1/t^2)$ in the strongly convex case — so several existing primal-dual methods are already optimal.

## Key claim
For any first-order method $M$ on the bilinear SPP $\min_{x\in X}\max_{y\in Y} f(x) + \langle Ax-b,y\rangle - g(y)$ with $L_f$-Lipschitz $\nabla f$ and Euclidean balls $X,Y$ of radii $R_X,R_Y$, there exists a worst-case instance such that the primal-dual gap satisfies
$$\phi(\bar x^{(t)}) - \psi(\bar y^{(t)}) \;\ge\; \tfrac{\sqrt 2+2}{4}\cdot\tfrac{L_f R_X^2}{16(4t+9)^2} + \tfrac{\|A\| R_X R_Y}{4t+9}.$$
Under $\mu$-strong convexity of $f$, the bound is $\tfrac{5\|A\|^2 R_Y^2}{512\mu(4t+9)^2}$. Matching results hold for affinely constrained problems (Theorem 1).

## Method
Construct "hard" instances as convex QPs $\min \tfrac12 x^\top H x - h^\top x$ s.t. $Ax=b$, where $A$ has a bidiagonal Toeplitz block $B$ (entries $-1,1$) plus a padding block $G$, and the right-hand side is $\tfrac{L_A}{2}\mathbf 1$. The bidiagonal structure means $k$ first-order oracle calls confine iterates to a Krylov subspace $K_{k-1} = \mathrm{span}\{e_{2k-i,n},\dots,e_{2k,n}\}$ that captures only the last $k$ coordinates of the optimal solution $x^*=(1,2,\dots,2k,0,\dots)$. To drop the linear-span assumption, a rotation-invariance argument (Nemirovski 1991/1992) lifts the bound to arbitrary first-order methods described by rule sequences $\{I_t\}$.

## Result
Tight lower bounds matching known upper bounds (up to constants / a log term):
- Affinely constrained convex: $f(\bar x^{(t)})-f^* \gtrsim \tfrac{L_f \|x^*\|^2}{t^2} + \tfrac{\|A\|\|x^*\|\|y^*\|}{t}$, plus $\|A\bar x^{(t)}-b\| \gtrsim \tfrac{\|A\|\|x^*\|}{t}$.
- Strongly convex affinely constrained: $\|\bar x^{(t)}-x^*\|^2 \gtrsim \tfrac{\|A\|^2\|y^*\|^2}{\mu^2 t^2}$.
- General SPP: as in Key claim. Confirms optimality of Nesterov's smoothing (2005), Chambolle-Pock, Chen-Lan-Ouyang accelerated primal-dual, and AL-ADMM (Ouyang et al. 2015).
- Requires $t < m/4 - 2$ (dimension-limited regime).

## Why it matters here
General background; no direct arena tie. Relevant if the agent ever frames an arena problem as a constrained convex / saddle-point program (e.g., LP-bound formulations like Cohn-Elkies for sphere packing, SDP flag algebra, or any extremal problem solved via Lagrangian duality) — this paper tells you *not to expect Nesterov-style $O(1/t^2)$ acceleration past the linear constraint*, so wall-clock estimates for ADMM / primal-dual splitting should assume $O(1/\varepsilon)$ iterations, not $O(1/\sqrt\varepsilon)$.

## Open questions / connections
- Lower bound for the *feasibility residual* that depends jointly on constraint and objective (current bounds let the objective be ignored).
- Separate-oracle setting: when $\nabla f$ is much more expensive than $Ax, A^\top y$ (Lan's gradient-sliding regime), what is the per-oracle lower bound?
- "Hard" instances assuming pre-specified $L_f, L_A, \mathrm{diam}(X), \mathrm{diam}(Y)$ — current construction lets $X,Y$ scale with the instance.
- Extends Nemirovski-Yudin 1983, Nesterov 2004 unconstrained lower bounds to the constrained / saddle setting.

## Key terms
saddle-point problems, bilinear, first-order methods, lower complexity bound, information-based complexity, Krylov subspace, Nemirovski rotation invariance, primal-dual, affinely constrained, Lipschitz gradient, strong convexity, Nesterov smoothing, ADMM, augmented Lagrangian
