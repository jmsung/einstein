---
type: source
kind: paper
title: "Performance of first-order methods for smooth convex minimization: a novel approach"
authors: Y. Drori, M. Teboulle
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1206.3209
source_local: ../raw/2012-drori-performance-first-order-methods-smooth.pdf
topic: general-knowledge
cites:
---

# Performance of first-order methods for smooth convex minimization: a novel approach

**Authors:** Y. Drori, M. Teboulle  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1206.3209

## One-line
Introduces the Performance Estimation Problem (PEP) framework: treat the worst-case behavior of a first-order optimizer as itself an optimization problem, solvable via SDP relaxation and duality.

## Key claim
For smooth convex $f \in C_L^{1,1}(\mathbb{R}^d)$, the gradient method with step $h \in (0,1]$ satisfies the tight analytical bound $f(x_N) - f^* \leq \frac{LR^2}{4Nh+2}$ — sharper than the classical $\frac{LR^2}{2N}$ — and a numerically-derived optimal first-order scheme achieves roughly $2\times$ better worst-case performance than Nesterov's fast gradient method.

## Method
Replace the infinite-dimensional functional constraint "$f$ convex, $L$-smooth" with finitely many inequalities (3.2) on the iterate values, gradients, and points; this turns worst-case analysis into a nonconvex Quadratic Matrix Program. Apply Lagrangian duality + a dimension-reduction lemma (Lemma 3.1) to obtain a tractable SDP dual, whose value upper-bounds the true worst case. For optimal step sizes, relax the resulting bilinear SDP via a change of variables $r_{i,k} = \lambda_i h_k^{(i)} + \tau_i \sum_t h_k^{(t)}$ into a linear SDP (LIN), then recover step sizes by back-substitution.

## Result
Gradient method: tight $\frac{LR^2}{4Nh+2}$ bound (Theorem 3.1), attained by a specific worst-case $C_L^{1,1}$ function (Theorem 3.2). For the heavy-ball method ($\alpha=1, \beta=1/2$) the SDP yields the first known $C_L^{1,1}$-convex rate (slightly better than gradient, far worse than FGM). For FGM, numerics suggest the auxiliary sequence $\{f(y_i)\}$ converges at the same rate as the main sequence (Conjecture 4.1). The PEP-optimal $N=5$ algorithm has explicit non-Nesterov step sizes (e.g., $x_1 = x_0 + \frac{1.618}{L}f'(x_0)$); bound $\approx LR^2/53.8$ vs FGM's $\approx LR^2/28.7$.

## Why it matters here
General background; no direct arena tie — but the PEP methodology (encode "worst case over a function class" as an SDP via finitely many class-defining inequalities) is structurally analogous to LP/SDP bounds in extremal combinatorics and sphere packing (Cohn-Elkies, flag algebra), and could inform meta-optimizer design for the agent's own optimization loops.

## Open questions / connections
- Conjecture 4.1: do FGM's auxiliary sequence $\{f(y_i)\}$ and main sequence $\{f(x_i)\}$ share the same convergence rate?
- Is there a clean analytical form for the PEP-optimal first-order method (the numerics suggest one exists)?
- Extends Nemirovski–Yudin oracle complexity framework; later spawned the "PEP-SDP" line (Taylor–Hendrickx–Glineur) and the OGM (Kim–Fessler) achieving the exact optimal rate.

## Key terms
performance estimation problem, PEP, first-order methods, gradient method, heavy ball method, Nesterov fast gradient, semidefinite relaxation, Lagrangian duality, smooth convex minimization, oracle complexity, optimal step sizes, Quadratic Matrix Program
