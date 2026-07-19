---
type: source
kind: paper
title: Stochastic Bias-Reduced Gradient Methods
authors: Hilal Asi, Y. Carmon, Arun Jambulapati, Yujia Jin, Aaron Sidford
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2106.09481
source_local: ../raw/2021-asi-stochastic-bias-reduced-gradient-methods.pdf
topic: general-knowledge
cites:
---

# Stochastic Bias-Reduced Gradient Methods

**Authors:** Hilal Asi, Y. Carmon, Arun Jambulapati, Yujia Jin, Aaron Sidford  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2106.09481

## One-line
A multilevel Monte-Carlo wrapper turns any optimal SGD-style solver into a near-unbiased estimator of $\arg\min F$ at $O(\log(1/\delta))$ expected gradient cost, enabling cheap, dimension-free randomized smoothing via Moreau-envelope gradient estimates.

## Key claim
For $\mu$-strongly-convex $F$ with $G$-bounded stochastic subgradients, one can construct an estimator $\hat x$ with $\|\mathbb{E}\hat x - x^*\| \le \delta$, variance $O((G^2/\mu^2)\log(G/(\mu\delta)))$, and $O(\log(G/(\mu\delta)))$ expected subgradient calls — yielding an $O(N\epsilon^{-2/3} + \epsilon^{-2})$ bound for minimizing $\max_{i\le N} f^{(i)}$, matching the lower bound of Carmon et al. [13] up to log factors.

## Method
Apply Blanchet–Glynn MLMC de-biasing on top of any "optimal-distance-convergence" (ODC) SGD variant (e.g., epoch-SGD): draw $J \sim \mathrm{Geom}(1/2)$, return $x_0 + 2^J(x_J - x_{J-1})\,\mathbb{1}\{2^J \le T_{\max}\}$ where $x_j = \mathrm{ODC}(\hat\nabla f, \psi, 2^j)$, the geometric/telescoping structure giving low bias with $O(\log T_{\max})$ expected cost. Plug the resulting $\nabla f_\lambda(y) = \lambda(y - P_{f,\lambda}(y))$ estimator into accelerated proximal-point (Monteiro–Svaiter) or AGD on the Moreau envelope; for max-of-$N$ losses, combine with softmax smoothing + rejection sampling for gradient estimates within a small ball.

## Result
Four applications: (1) $\min\max_i f^{(i)}$ in $\tilde O(N\epsilon^{-2/3} + \epsilon^{-2})$ function/subgradient evals — surprising "max is no harder than average" when $N \gtrsim (GR/\epsilon)^{-4/3}$; (2) projection-efficient optimization in $O(GD/\epsilon)$ projections with near-optimal $\tilde O(\epsilon^{-2})$ $\hat\nabla f$ calls, recovering Thekumparampil et al. [51]; (3) gradient-sliding-style composite optimization recovering Lan [34] up to logs; (4) conditional on a *bounded* variant of the estimator, an $O(n)$-subgradient optimal-utility DP non-smooth SCO algorithm (open: build a high-probability bounded estimator).

## Why it matters here
General background; no direct arena tie. Relevant as a primitive for any future agent technique that needs a cheap, near-unbiased proximal-point or Moreau-envelope gradient inside an accelerated outer loop — especially for $\min\max$ formulations (worst-case / robust objectives over many constraints) that occasionally appear when reformulating arena problems (e.g., Chebyshev-style equioscillation, autocorrelation extremals) as max-of-$N$ Lipschitz pieces.

## Open questions / connections
- Does a bounded-with-high-probability optimum estimator exist? Would close the non-smooth DP-SCO gap and possibly broaden MLMC applicability.
- Can the technique extend to weakly-convex / non-convex proximal points (relevant for non-convex landscapes in arena problems)?
- Practical viability of accelerated proximal-point methods underlying the $\min\max$ result remains open [50]; theoretical-only at present.
- Relation to randomized smoothing [Duchi et al. 20] — MLMC gives dimension-free smoothing, contrasting the $d^{1/4}$ factor in classical RS.

## Key terms
multilevel Monte Carlo, Blanchet-Glynn estimator, Moreau-Yoshida envelope, proximal point, randomized smoothing, Monteiro-Svaiter acceleration, epoch SGD, strongly convex optimization, min-max optimization, softmax smoothing, rejection sampling, differentially private SCO, gradient sliding, bias-variance tradeoff
