---
type: source
kind: paper
title: Optimization, Learning, and Games with Predictable Sequences
authors: A. Rakhlin, Karthik Sridharan
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1311.1869
source_local: ../raw/2013-rakhlin-optimization-learning-games-predictable.pdf
topic: general-knowledge
cites:
---

# Optimization, Learning, and Games with Predictable Sequences

**Authors:** A. Rakhlin, Karthik Sridharan  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1311.1869

## One-line
Shows how Optimistic Mirror Descent — online learning with a predicted-gradient "hint" $M_t$ — unifies and accelerates offline smooth optimization, saddle-point problems, uncoupled zero-sum game dynamics, and approximate convex programming (e.g. Max Flow).

## Key claim
A single algorithmic primitive (Optimistic Mirror Descent with $M_t \approx \nabla G(g_{t-1})$) yields (i) the Mirror Prox $O(HR^2/T)$ rate for smooth convex optimization, extended to $\alpha$-Hölder gradients at rate $O(HR^{1+\alpha}/T^{(1+\alpha)/2})$; (ii) an uncoupled, adaptive Exponential-Weights-like dynamic for zero-sum games converging to minimax at rate $O(\log T \cdot (\log m + \log n)/T)$ while preserving $O(T^{-1/2})$ against adversarial play; (iii) an $\tilde O(d^{3/2}/\epsilon)$ algorithm for $\epsilon$-approximate Max Flow on graphs with $d$ edges.

## Method
Optimistic Mirror Descent runs two interleaved Bregman-projected updates per round: a "primary" play $f_t$ using a predicted gradient $M_t$, then a "secondary" $g_t$ using the realized $\nabla G_t(f_t)$. Regret is controlled by $\sum_t \|\nabla_t - M_t\|_*^2$ rather than $\sum_t \|\nabla_t\|_*^2$ — so any predictability of the gradient sequence (smoothness, two cooperating players, structured saddle point) is automatically converted into faster rates. Step sizes are chosen adaptively from past prediction errors (no doubling trick, no prior knowledge of opponent's strategy).

## Result
For smooth saddle points $\phi(f,x)$ with Hölder-smooth partials of exponent $\gamma$, two players running OMD against each other reach $\epsilon$-equilibrium in $O((H(R_1^2+R_2^2)/\epsilon)^{2/(1+\gamma)})$ rounds (Cor. 5). For zero-sum matrix games with $A\in[-1,1]^{n\times m}$, the modified Exponential-Weights-with-doubled-latest-loss-vector achieves $\tilde O(1/T)$ minimax convergence under uncoupled play, and a partial-information (4-query, real-payoff-only) variant gives $\tilde O((m+n)/T)$ (Prop. 6, Lemma 7). Max Flow follows by reduction to a smooth saddle point: $T = O(d \log d / \epsilon)$ iterations at $O(d)$ each → $\tilde O(d^{3/2}/\epsilon)$ total, matching Christiano et al. [8] with a much simpler procedure (Cor. 9).

## Why it matters here
General background; no direct arena tie. Closest relevance is to LP/SDP-based bounds (Cohn–Elkies, flag-algebra SDP, kissing-number LP) and to saddle-point reformulations of constrained optimization — if any arena problem is recast as $\min_f \max_x \phi(f,x)$ with smooth $\phi$, Mirror Prox / OMD gives a fast first-order solver that may outperform off-the-shelf IPM for large $d$.

## Open questions / connections
- Can the $1/T$ uncoupled-game rate be attained with only one bandit observation $e_i^\top A e_j$ per round (authors conjecture no)?
- Doubling-trick / $p$-norm regularizer to remove the extraneous $\log T$ factor under entropic regularization (the $R_{\max}^2 \ge \sup_g D_R(f^*,g)$ obstruction for negative entropy).
- Extends Nemirovski's Mirror Prox [9] to Hölder-smooth gradients (interpolation between $T^{-1/2}$ and $T^{-1}$) — relevant whenever a problem's gradient is only Hölder, not Lipschitz.
- Connects to Daskalakis–Deckelbaum–Kim [6] uncoupled-dynamics question in behavioral economics.

## Key terms
Optimistic Mirror Descent, Mirror Prox, predictable sequences, Bregman divergence, saddle-point optimization, Hölder smoothness, zero-sum matrix game, uncoupled dynamics, minimax equilibrium, Exponential Weights, no-regret, approximate Max Flow, convex programming, Nemirovski
