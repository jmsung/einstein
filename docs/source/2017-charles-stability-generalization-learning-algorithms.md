---
type: source
kind: paper
title: Stability and Generalization of Learning Algorithms that Converge to Global Optima
authors: Zachary B. Charles, Dimitris Papailiopoulos
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1710.08402
source_local: ../raw/2017-charles-stability-generalization-learning-algorithms.pdf
topic: general-knowledge
cites:
---

# Stability and Generalization of Learning Algorithms that Converge to Global Optima

**Authors:** Zachary B. Charles, Dimitris Papailiopoulos  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1710.08402

## One-line
Derives black-box generalization bounds for learning algorithms by combining their convergence rate with the Polyak-Łojasiewicz / quadratic-growth geometry around global minima, instead of requiring (strong) convexity.

## Key claim
For $L$-Lipschitz empirical losses satisfying the PL condition with parameter $\mu$, any algorithm converging to a global optimum has uniform stability $\epsilon_{stab} \le O(L\epsilon_A/\mu) + O(L^2/(\mu n))$, where $\epsilon_A$ is the optimization error — recovering Hardt–Recht–Singer's strongly-convex SGD bound while extending it to GD, SVRG, RCD and a nonconvex class.

## Method
Decompose $|\ell(w_S;z) - \ell(w_{S'};z)|$ via the triangle inequality through the two algorithmic outputs and their projected global optima $w_S^*, w_{S'}^*$. Bound the "algorithm → optimum" terms using PL's gradient-domination inequality $\tfrac12\|\nabla f\|^2 \ge \mu(f-f^*)$ (or QG's $f-f^* \ge \tfrac{\mu}{2}\|x-x_p\|^2$); bound the "optimum-to-optimum" term by noting that for the leave-one-out loss, $\nabla f_S(w_{S'}^*) = \tfrac{1}{n}\nabla\ell$, which is $O(L/n)$. Convergence rate $\epsilon_A$ is then plugged in from existing analyses of SGD/GD/SVRG/RCD.

## Result
Three "case" bounds depending on whether convergence is in iterate distance, function value, or gradient norm — all yield $O(L^2/(\mu n))$ pointwise/uniform stability at convergence. Theorem 4.1: $g \circ \sigma(Xw)$ is PL with $\mu = \lambda\sigma_{\min}(X)^2 c^2$ for strongly-convex $g$, leaky-ReLU $\sigma$, full-rank $X$. Theorem 4.4: every full-rank critical point of a deep linear network $\tfrac12\|W_\ell\cdots W_1 X - Y\|_F^2$ is a global minimizer. Theorem 6.1/6.2: explicit 1-layer net where full-batch GD is uniformly unstable ($\ge 1/2$) while SGD achieves $O(1/n)$ stability — formalizing Hardt et al.'s Fig. 10 intuition.

## Why it matters here
General background; no direct arena tie. PL/QG geometric conditions are a generic "gradient-dominates-suboptimality" template that could conceivably be invoked when arguing local rigidity of a basin (e.g., the three-way local-optimality framing for P1), but the paper's content is ML-generalization theory, not extremal combinatorics or sphere packing.

## Open questions / connections
- Can stability be derived for convergence to *approximate local* (not global) minima in genuinely nonconvex losses?
- Among multiple local minima of a fixed loss, can sharpness/flatness be tied to generalization gap quantitatively (cf. Keskar et al. on sharp minima)?
- Why is SGD systematically more stable than GD in nonconvex settings beyond the 1-layer toy?
- Extends Karimi–Nutini–Schmidt (PL convergence) and Hardt–Recht–Singer (SGD stability); parallels Kawaguchi's linear-net landscape result with a stronger full-rank → global-min claim.

## Key terms
Polyak-Łojasiewicz condition, quadratic growth condition, uniform stability, pointwise hypothesis stability, generalization gap, gradient domination, SGD, gradient descent, SVRG, randomized coordinate descent, deep linear networks, leaky ReLU, sharp minima, Bousquet-Elisseeff, Hardt-Recht-Singer
