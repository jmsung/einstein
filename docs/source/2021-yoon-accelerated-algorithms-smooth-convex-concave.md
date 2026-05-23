---
type: source
kind: paper
title: Accelerated Algorithms for Smooth Convex-Concave Minimax Problems with O(1/k^2) Rate on Squared Gradient Norm
authors: Taeho Yoon, Ernest K. Ryu
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2102.07922
source_local: ../raw/2021-yoon-accelerated-algorithms-smooth-convex-concave.pdf
topic: general-knowledge
cites:
---

# Accelerated Algorithms for Smooth Convex-Concave Minimax Problems with O(1/k^2) Rate on Squared Gradient Norm

**Authors:** Taeho Yoon, Ernest K. Ryu  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2102.07922

## One-line
Introduces the Extra Anchored Gradient (EAG) algorithm achieving optimal $O(1/k^2)$ last-iterate convergence on the squared gradient norm for smooth convex-concave minimax problems, with a matching lower bound.

## Key claim
For $R$-smooth convex-concave $L$ with saddle point $z^*$, EAG (both constant- and varying-step versions) attains $\|\nabla L(z_k)\|^2 \leq C R^2 \|z_0 - z^*\|^2 / k^2$ (e.g., $C=260$ for EAG-C with $\alpha=1/(8R)$; $C \approx 27$ for EAG-V with $\alpha_0 \approx 0.618/R$). A matching $\Omega(R^2/k^2)$ lower bound on biaffine instances proves order-optimality across the broad algorithm class $\mathcal{A}_{\text{sep}}$.

## Method
Combines two ingredients distinct from Nesterov's acceleration: (i) extragradient steps (a half-step lookahead $z_{k+1/2}$ used to evaluate $G$) and (ii) **anchoring** — each iterate pulled toward $z_0$ by coefficient $\beta_k = 1/(k+2)$, resembling Halpern iteration. Convergence is proved via a non-increasing Lyapunov function $V_k = A_k \|G(z_k)\|^2 + B_k \langle G(z_k), z_k - z_0 \rangle$ with quadratically growing $A_k$ and linearly growing $B_k$. The lower bound uses Chebyshev-polynomial minimax arguments on biaffine $L(x,y)=\langle Ax-b, y-c\rangle$ via Krylov subspaces $\mathcal{K}_{k-1}(A;b)$, extending Nemirovsky's 1991/1992 framework with a resisting-oracle construction.

## Result
EAG-V with $\alpha_0 \approx 0.618/R$ gives $\|\nabla L(z_k)\|^2 \leq 27 R^2 \|z_0-z^*\|^2 / ((k+1)(k+2))$. The lower bound is $\|\nabla L(z_k)\|^2 \geq R^2 \|z_0-z^*\|^2 / (2\lfloor k/2\rfloor + 1)^2$ on biaffine $L$, holding for all deterministic gradient-based algorithms in $\mathcal{A}_{\text{sep}}$ (including alternating updates). EAG breaks the prior $\Omega(R^2/k)$ 1-SCLI bound of Golowich et al. (2020) because its $k$-dependent anchoring coefficients make it non-stationary (2-CLI / translated 1-CLI).

## Why it matters here
General background; no direct arena tie. Relevant only as methodology — anchoring/Halpern-style pull-to-initial-point and Lyapunov design with mixed linear+quadratic growth coefficients are transferable acceleration patterns that could inspire custom optimizer schedules for monotone-operator fixed-point steps that show up in some LP/SDP dual updates (e.g., primal-dual splitting on P1 Cohn-Elkies LPs). Not core to any of the 23 problems.

## Open questions / connections
- Closing the ~100× constant gap between upper ($C \approx 27$) and lower ($\approx R^2/(2\lfloor k/2\rfloor + 1)^2$) bounds — likely needs non-biaffine worst-case constructions à la Drori (2017).
- Whether the optimal $\delta$ in $\beta_k = \delta/(k+1)$ (numerically $\approx 2.697$) admits a closed-form characterization.
- Extension to stochastic, nonconvex-concave, or composite (proximal) settings — the paper leaves these to future work.
- Resolves in the negative the open question of whether the $\Omega(1/k)$ 1-SCLI gradient-norm lower bound generalizes to 2-CLI and translated 1-CLI classes.

## Key terms
extragradient, anchoring, Halpern iteration, minimax optimization, saddle point, monotone operator, Lyapunov function, squared gradient norm, last-iterate convergence, Chebyshev polynomial, Krylov subspace, CLI lower bound, Yoon, Ryu, Nemirovsky
