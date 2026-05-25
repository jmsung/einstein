---
type: source
kind: paper
title: Non-convex Finite-Sum Optimization Via SCSG Methods
authors: Lihua Lei, Cheng Ju, Jianbo Chen, Michael I. Jordan
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1706.09156
source_local: ../raw/2017-lei-non-convex-finite-sum-optimization-scsg.pdf
topic: general-knowledge
cites:
---

# Non-convex Finite-Sum Optimization Via SCSG Methods

**Authors:** Lihua Lei, Cheng Ju, Jianbo Chen, Michael I. Jordan  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1706.09156

## One-line
Introduces SCSG, a variance-reduced stochastic gradient method for non-convex finite-sum minimization that beats both SGD and SVRG-style methods across the full accuracy spectrum.

## Key claim
For smooth non-convex $f = \frac{1}{n}\sum_i f_i$, SCSG reaches $\mathbb{E}\|\nabla f(x)\|^2 \le \epsilon$ in IFO complexity $O(\min\{\epsilon^{-5/3}, \epsilon^{-1} n^{2/3}\})$ — strictly better than SGD's $O(\epsilon^{-2})$ and never worse than SVRG's $O(n + n^{2/3}\epsilon^{-1})$. Under the Polyak–Łojasiewicz condition with constant $\mu$, the rate becomes $\tilde O((\mu\epsilon)^{-1}\wedge n) + \mu^{-1}((\mu\epsilon)^{-1}\wedge n)^{2/3})$.

## Method
SCSG runs $T$ epochs; epoch $j$ draws a batch $I_j$ of size $B_j$, computes a control gradient $g_j = \nabla f_{I_j}(\tilde x_{j-1})$, then runs $N_j \sim \text{Geom}(B_j/(B_j+b_j))$ SVRG-style inner updates with mini-batch size $b_j$ and stepsize $\eta_j \sim L^{-1}(B_j/b_j)^{-2/3}$. The geometric stopping time is essential: it makes the inner-loop average equal to a primal–dual gap telescope (via Lemma A.2), which lets the analysis avoid bounded-iterate assumptions. Two recommended schedules: constant $B_j = \min(\lceil 12 H^*/\epsilon\rceil, n)$ for moderate accuracy, or time-varying $B_j = \min(\lceil j^{3/2}\rceil, n)$ for high accuracy.

## Result
Theorem 3.2 telescopes a one-epoch bound $\mathbb{E}\|\nabla f(\tilde x_j)\|^2 \le \frac{5L}{\gamma}(b_j/B_j)^{1/3}\mathbb{E}[f(\tilde x_{j-1})-f(\tilde x_j)] + 6 H^* \mathbb{I}(B_j<n)/B_j$. With constant batches (Cor. 3.3): $\mathbb{E}C_{\text{comp}}(\epsilon) = O(\epsilon^{-1}\wedge n + (\epsilon^{-1}\wedge n)^{2/3}\epsilon^{-1})$. With $B_j = j^{3/2}$ (Cor. 3.4): $\tilde O(\epsilon^{-5/3} \wedge n^{2/3}\epsilon^{-1})$. Empirically beats mini-batch SGD on MNIST with FCN/LeNet in both training and validation loss.

## Why it matters here
General background; no direct arena tie. None of the 23 Einstein Arena problems are large-finite-sum ERM-style; the agent's optimizers are L-BFGS / basin-hopping / parallel tempering / mpmath polish over low-dimensional configurations, not neural-network training. The geometric-stopping trick could in principle inform a randomized inner-loop length for variance-reduced multistart, but the regime mismatch (no finite-sum structure, no stochastic gradients) makes the connection speculative.

## Open questions / connections
- Combining SCSG variance reduction with momentum and adaptive stepsizes (Adam-style) — left open by authors.
- Gap to optimal non-convex rate: SCSG achieves $\epsilon^{-5/3}$ vs the best gradient-method rate $\epsilon^{-5/6}$ from Carmon–Hinder–Duchi–Sidford; can a stochastic counterpart close this?
- Whether the geometric-stopping epoch structure transfers to constrained or manifold-valued non-convex problems (e.g., Stiefel/sphere) — unaddressed.

## Key terms
SCSG, SVRG, variance reduction, non-convex optimization, finite-sum, stochastic gradient, Polyak-Lojasiewicz, geometric stopping, IFO complexity, mini-batch, Lei, Jordan
