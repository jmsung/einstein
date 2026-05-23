---
type: source
kind: paper
title: Variance Reduction for Matrix Games
authors: Y. Carmon, Yujia Jin, Aaron Sidford, Kevin Tian
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1907.02056
source_local: ../raw/2019-carmon-variance-reduction-matrix-games.pdf
topic: general-knowledge
cites:
---

# Variance Reduction for Matrix Games

**Authors:** Y. Carmon, Yujia Jin, Aaron Sidford, Kevin Tian  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1907.02056

## One-line
A randomized primal-dual algorithm solves bilinear saddle-point problems $\min_x \max_y y^\top A x$ to additive error $\epsilon$ in time $\tilde{O}(\mathrm{nnz}(A) + \sqrt{\mathrm{nnz}(A) \cdot (m+n)} \cdot L/\epsilon)$, beating both exact and fully stochastic gradient methods in the moderate-accuracy / dense regime.

## Key claim
For $A \in \mathbb{R}^{m\times n}$ with $L = \|A\|_{\max}$ ($\ell_1$-$\ell_1$) or $L = \max_i \|A_{i:}\|_2$ ($\ell_2$-$\ell_1$), the method finds an $\epsilon$-saddle point in time $\tilde{O}(\mathrm{nnz}(A) + \sqrt{\mathrm{nnz}(A)(m+n)} \cdot L/\epsilon)$ — a $\sqrt{n}$ improvement over Nemirovski's mirror-prox $\tilde{O}(\mathrm{nnz}(A) \cdot L/\epsilon)$ in the square-dense case, matching the speedup Katyusha/accelerated SVRG achieve over fast gradient methods for finite-sum minimization.

## Method
Combines Nemirovski's **conceptual prox-method** (outer extragradient loop solving $O(\alpha/\epsilon)$ relaxed proximal subproblems) with a novel **"centered" stochastic gradient estimator** whose variance is bounded by squared distance to a reference point: $\mathbb{E}\|\tilde{g}_{z_0}(z) - g(z_0)\|_*^2 \le L^2 \|z - z_0\|^2$. The key innovation is **"sampling from the difference"** — drawing coordinate $i$ with probability $p_i(y) = |[y]_i - [y_0]_i| / \|y - y_0\|_1$ (or squared-difference for $\ell_2$), making the sampling distribution iterate-dependent rather than fixed. For $\ell_2$-$\ell_1$ a local-norms analysis with gradient clipping recovers the correct Lipschitz dependence.

## Result
Three concrete settings: (1) $\ell_1$-$\ell_1$ matrix games (LP-equivalent) with $L = \|A\|_{\max}$; (2) $\ell_2$-$\ell_1$ games (hard-margin SVM, minimum enclosing ball) with $L = \max_i \|A_{i:}\|_2$; (3) $\ell_2$-$\ell_2$ games with $L = \|A\|_F$. Strictly improves on mirror-prox/dual-extrapolation $\tilde{O}(\mathrm{nnz}(A) \cdot L/\epsilon)$ whenever $\mathrm{nnz}(A) = \omega(m+n)$, and on Grigoriadis–Khachiyan/Clarkson–Hazan–Woodruff sublinear $\tilde{O}((m+n) L^2/\epsilon^2)$ whenever the latter isn't truly sublinear. Extensions: composite objectives, relative strong convexity (linear convergence), SVRG-style estimator for finite-sum saddles, restarted variant for exact proximal points.

## Why it matters here
General background for the optimization toolkit — matrix-game / LP solvers underlie any **flag-algebra SDP / Cohn–Elkies LP** workflow (P1 sphere packing, P15/P16 autocorrelation, kissing-number LP bounds). The "centered gradient estimator" + "sampling from the difference" idea is a plausible accelerator for the project's **HiGHS LP / IPM** stage when matrices grow dense; useful as a reference for future RAM-bound LP routing (compute-router) and any future SDP solver work. No direct tie to current per-problem solutions; library-level technique.

## Open questions / connections
- Does "sampling from the difference" extend usefully to $\ell_\infty$-$\ell_1$ games (Sherman 2017, Sidford–Tian 2018) where domain-size $\Theta$ doesn't scale logarithmically?
- Can the centered-estimator framework be adapted to **LP duality / Cohn–Elkies-style infinite LPs** by discretization, beating mirror-prox on the discretized matrix?
- Extends Balamurugan–Bach 2016 (factored-splits SVRG for $\ell_2$-$\ell_2$ saddles) to non-Euclidean geometries and gives accelerated rates; leaves open the $\|A\|_{\mathrm{op}}$ vs $\|A\|_F$ gap in $\ell_2$-$\ell_2$.
- Open: matching lower bounds in the linear-but-not-sublinear regime $\mathrm{nnz}(A) \in [m+n, (m+n)^2]$.

## Key terms
matrix games, bilinear saddle point, variance reduction, mirror-prox, Nemirovski prox-method, extragradient, centered gradient estimator, sampling from the difference, primal-dual, linear programming, SVM, Bregman divergence, KL divergence, local norms, Grigoriadis-Khachiyan, Clarkson-Hazan-Woodruff, SVRG, Katyusha, dual extrapolation, Carmon, Sidford
