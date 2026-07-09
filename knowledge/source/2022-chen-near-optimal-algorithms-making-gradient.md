---
type: source
kind: paper
title: Near-Optimal Algorithms for Making the Gradient Small in Stochastic Minimax Optimization
authors: Le-Yu Chen, Luo Luo
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2208.05925
source_local: ../raw/2022-chen-near-optimal-algorithms-making-gradient.pdf
topic: general-knowledge
cites:
---

# Near-Optimal Algorithms for Making the Gradient Small in Stochastic Minimax Optimization

**Authors:** Le-Yu Chen, Luo Luo  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2208.05925

## One-line
Designs RAIN, a stochastic first-order algorithm that achieves near-optimal SFO complexity for finding $\epsilon$-stationary points (small gradient norm) in smooth convex-concave and strongly-convex-strongly-concave minimax problems, plus an extension RAIN++ for structured nonconvex-nonconcave cases.

## Key claim
RAIN attains SFO complexity $\tilde{O}(\sigma^2 \epsilon^{-2} + \kappa)$ for SCSC and $\tilde{O}(\sigma^2 \epsilon^{-2} + LD\epsilon^{-1})$ for CC minimax, with matching lower bounds $\Omega(\tilde{} \sigma^2 \epsilon^{-2} + \kappa)$ and $\Omega(\tilde{} \sigma^2 \epsilon^{-2} + LD\epsilon^{-1})$ — establishing near-optimality. Improves over prior SEAG ($O(\sigma^2 L^2 \epsilon^{-4} + LD\epsilon^{-1})$) and stochastic Halpern ($\tilde{O}(\sigma^2 L D \epsilon^{-3} + L^3 D^3 \epsilon^{-3})$).

## Method
Recursive anchoring: solves a sequence of two-sided regularized sub-problems $f^{(s)}(x,y) = f^{(s-1)} + \frac{\lambda_s}{2}\|x-x_s\|^2 - \frac{\lambda_s}{2}\|y-y_s\|^2$ with anchors $\{(x_s,y_s)\}$ that move with iterations (unlike Yoon-Ryu/Lee-Kim's fixed anchor at $z_0$). Each sub-problem is solved by Epoch-SEG, a two-phase stochastic extragradient with fixed-stepsize phase (optimization-error reduction) followed by decreasing-stepsize phase (statistical-error reduction). RAIN++ runs RAIN on the saddle envelope $f_{2L}(x,y)$ using an MLMC-based estimator (EnvGradEst) for its gradient.

## Result
Theorem 4.1 (SCSC): $\tilde{O}(\kappa + \sigma^2 \epsilon^{-2} \log^3 \kappa)$ SFO calls. Theorem 4.2 (CC): $\tilde{O}(LD\epsilon^{-1} + \sigma^2 \epsilon^{-2} \log^3(LD/\epsilon))$. Theorem 5.3 (intersection-dominant, $\tau \geq 2L$): $\tilde{O}(\sigma^2 \epsilon^{-2} + L/\alpha)$. Theorem 5.4 (negative comonotonic, $\rho \in [-1/(2L), 0)$): $\tilde{O}(\sigma^2 \epsilon^{-2} + LD\epsilon^{-1})$. All four match the proven lower bounds up to log factors.

## Why it matters here
General background; no direct arena tie — the 23 Einstein problems are deterministic optimization (sphere packing, autocorrelation, kissing numbers), not stochastic minimax. Tangentially informs `compute-router` thinking about variance-vs-bias trade-offs in stochastic optimizers; the anchoring trick is conceptually adjacent to proximal-point regularization used in some packing relaxations.

## Open questions / connections
- Extends Allen-Zhu's (2018) recursive regularization from convex SGD to monotone operator setting.
- Builds on Yoon-Ryu (2021) EAG and Lee-Kim (2021) SEAG; introduces moving anchors as key innovation.
- Open: tightness of polylog factors; whether RAIN-style anchoring helps in nonconvex-strongly-concave (not addressed here).
- Saddle-envelope technique (Grimmer et al. 2023) for nonconvex-nonconcave may have broader use in non-monotone variational inequalities.

## Key terms
stochastic minimax optimization, extragradient method, anchored iteration, EAG, SEAG, RAIN, saddle envelope, convex-concave, strongly-convex-strongly-concave, negative comonotonicity, intersection dominant, SFO complexity, variational inequality, monotone operator, MLMC gradient estimator
