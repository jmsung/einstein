---
type: source
kind: paper
title: Introduction to Online Convex Optimization
authors: Elad Hazan
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1909.05207
source_local: ../raw/2016-hazan-introduction-online-convex-optimization.pdf
topic: general-knowledge
cites:
---

# Introduction to Online Convex Optimization

**Authors:** Elad Hazan  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1909.05207

## One-line
A graduate textbook unifying convex optimization, online learning, and game theory through the regret-minimization framework of Online Convex Optimization (OCO).

## Key claim
Sublinear regret $\text{Regret}_T = o(T)$ is achievable against adversarial convex losses by simple first-order methods: Online Gradient Descent achieves $O(\sqrt{T})$ regret for $G$-Lipschitz convex losses over a bounded convex set $K$, improvable to $O(\log T)$ for strongly convex or exp-concave losses (via Online Newton Step).

## Method
A repeated-game formalism: at each round $t$, the player picks $x_t \in K \subseteq \mathbb{R}^n$, then adversary reveals convex $f_t$; performance is measured by regret against the best fixed $x^\star$ in hindsight. Core machinery: gradient descent + Bregman-divergence regularization (RFTL / Online Mirror Descent), second-order curvature (Online Newton Step for exp-concave losses), Frank-Wolfe / Conditional Gradient for projection-free updates, follow-the-perturbed-leader for linear losses, and bandit reductions via one-point gradient estimators on Minkowski-shrunk sets $K_\delta$.

## Result
Canonical bounds established: OGD $O(GD\sqrt{T})$; strongly-convex OGD $O((G^2/\alpha)\log T)$; ONS for exp-concave $O((n/\alpha)\log T)$; EXP3 multi-armed bandit $O(\sqrt{Tn\log n})$; bandit convex optimization $O(T^{3/4})$ via gradient-free estimators with self-concordant barriers giving near-optimal $\tilde O(\sqrt{T})$ for linear bandits. Equivalences: von Neumann minimax $\Leftrightarrow$ LP duality $\Leftrightarrow$ no-regret dynamics $\Leftrightarrow$ Blackwell approachability.

## Why it matters here
General background; no direct arena tie. Potentially relevant to autocorrelation / extremal problems where iterative gradient-based exploration over convex polytopes (simplex, $\ell_p$-balls, spectrahedron) is the natural search; projection-free Frank-Wolfe and adaptive-gradient (AdaGrad/Adam) ideas could inform parameter scheduling in the optimizer pipeline.

## Open questions / connections
- Can adaptive-regret (Chapter 10) algorithms detect basin-shifts in arena problems where the landscape changes across regimes (e.g., parameter cascades in P14/P17)?
- Frank-Wolfe / Conditional Gradient is a candidate replacement for projected SLSQP when constraints are defined by linear-optimization oracles (LP-flavored problems like Sidon-set or Cohn-Elkies LP polish).
- Multiplicative weights / Hedge already shows up in flag-algebra SDP rounding — does the OCO-game view yield faster MW-style schedules for the LP/SDP polish stage?

## Key terms
online convex optimization, regret minimization, online gradient descent, online Newton step, exp-concave, follow-the-regularized-leader, online mirror descent, Frank-Wolfe conditional gradient, bandit convex optimization, multiplicative weights Hedge, Blackwell approachability, AdaGrad, von Neumann minimax, self-concordant barrier, Bregman divergence
