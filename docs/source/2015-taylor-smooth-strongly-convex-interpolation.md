---
type: source
kind: paper
title: Smooth strongly convex interpolation and exact worst-case performance of first-order methods
authors: Adrien B. Taylor, J. Hendrickx, François Glineur
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1502.05666
source_local: ../raw/2015-taylor-smooth-strongly-convex-interpolation.pdf
topic: general-knowledge
cites:
---

# Smooth strongly convex interpolation and exact worst-case performance of first-order methods

**Authors:** Adrien B. Taylor, J. Hendrickx, François Glineur  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1502.05666

## One-line
Reformulates the worst-case analysis of fixed-step first-order methods on smooth (strongly) convex functions as an exactly solvable finite-dimensional SDP, via new necessary-and-sufficient interpolation conditions.

## Key claim
For any class $\mathcal{F}_{\mu,L}(\mathbb{R}^d)$ of $L$-smooth $\mu$-strongly convex functions, the exact worst-case performance of an $N$-step fixed-step first-order black-box method can be obtained as the optimal value of a convex SDP of size $O(N^2)$, with primal solutions giving matching worst-case functions and dual solutions giving certified upper bounds.

## Method
Performance Estimation Problem (PEP) framework: replace the infinite-dimensional sup over $f \in \mathcal{F}_{\mu,L}$ with a finite sup over interpolable triples $\{(x_i, g_i, f_i)\}_{i \in I}$. The core technical step is deriving tight $\mathcal{F}_{\mu,L}$-interpolation inequalities by composing (i) minimal-curvature subtraction (Theorem 3) and (ii) Legendre–Fenchel conjugation (Theorem 2), reducing smooth strongly convex interpolation to plain convex interpolation (Theorem 1, the cyclic monotonicity / pointwise-max construction). Naive discretization of standard $\mathcal{F}_{0,L}$ characterizations (e.g. $\|g_i-g_j\|^2 \le L\|x_i-x_j\|^2$) is shown to be insufficient via explicit counterexamples.

## Result
Exact, dimension-independent SDP formulation (`sdp-PEP`) covering gradient method (GM), Nesterov's fast gradient method (FGM), and Kim–Fessler optimized gradient method (OGM), under criteria $f(x_N)-f^*$, $\|\nabla f(x_N)\|$, and $\min_i \|\nabla f(x_i)\|$. Conjectured tight worst-case bounds — e.g. for GM on $\mathcal{F}_{0,L}$ with step $h$, $f(x_N)-f^* \le \frac{LR^2}{2}\max\{(2Nh+1)^{-1}, (1-h)^{2N}\}$ — yielding an optimal step $h_{\text{opt}}(N) \in [3/2, 2)$ with $h_{\text{opt}} \to 2$, a factor-2 asymptotic improvement over the classical $h=1$ bound $LR^2/(2(N+1))$. Strongly-convex generalization (Conjecture 2) closes the $\mu \to 0$ continuity gap with the smooth case; matches IQC asymptotic rates of Lessard–Recht–Packard up to constants but is strictly tighter at finite $N$.

## Why it matters here
General background; no direct arena tie — this is convex optimization machinery, not extremal/discrete geometry. Closest relevance is methodological: the PEP→SDP reduction via interpolation conditions is structurally analogous to SDP/flag-algebra liftings used in extremal combinatorics, and the constructive primal-recovery idea (every dual bound has a matching extremal function) mirrors the equioscillation / active-constraint diagnostics already in the wiki.

## Open questions / connections
- Can PEP be extended to line-search methods, projected gradient, or restricted-feasible-region first-order methods? (Authors flag this as open.)
- Can step sizes be *optimized* inside `sdp-PEP` (jointly over method coefficients), tightening Drori–Teboulle / Kim–Fessler designs to provably optimal methods?
- Is the one-dimensional piecewise-quadratic worst-case structure (functions $f_{1,\tau}$, $f_2$) provable, not just conjectured? — closing this would convert Conjectures 1–5 into theorems.

## Key terms
performance estimation problem, PEP, semidefinite programming, smooth convex interpolation, strong convexity, Legendre-Fenchel conjugation, gradient method, fast gradient method, Nesterov acceleration, optimized gradient method, worst-case analysis, fixed-step first-order methods, Drori-Teboulle, Kim-Fessler, integral quadratic constraints
