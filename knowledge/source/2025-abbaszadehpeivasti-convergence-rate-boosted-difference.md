---
type: source
kind: paper
title: On the convergence rate of the boosted Difference-of-Convex Algorithm (DCA)
authors: Hadi Abbaszadehpeivasti, Etienne de Klerk, Adrien Taylor
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2510.16569v2
source_local: ../raw/2025-abbaszadehpeivasti-convergence-rate-boosted-difference.pdf
topic: general-knowledge
cites: 
---

# On the convergence rate of the boosted Difference-of-Convex Algorithm (DCA)

**Authors:** Hadi Abbaszadehpeivasti, Etienne de Klerk, Adrien Taylor  ·  **Year:** 2025  ·  **Source:** http://arxiv.org/abs/2510.16569v2

## One-line
First theoretical proof that the boosted DCA (an extra step of length $\alpha$ along the DCA direction) provably beats classical DCA in the worst case when both DC components are strongly convex.

## Key claim
For $f_1, f_2 \in \mathcal{F}_{\mu,L}(\mathbb{R}^n)$ with $0 \leq \mu < L < \infty$ and $\kappa := \mu/L$, after $N$ iterations of boosted DCA with $\alpha \in [0, \min\{1, 2\kappa\}]$:
$$\min_{1 \le k \le N+1} \|\nabla f(x_k)\|^2 \;\leq\; \frac{L(f(x_1) - f^\star)}{(1+\kappa\alpha)N + \tfrac{1}{2(1-\kappa)}}.$$
Strictly improves over $\alpha = 0$ (classical DCA) whenever $\kappa > 0$; bound shown tight on an explicit piecewise-quadratic example.

## Method
SDP-based performance estimation (Drori–Teboulle, refined by Taylor–Hendrickx–Glineur): the worst-case input for boosted DCA is cast as a tractable SDP using interpolation conditions for $\mathcal{F}_{\mu,L}$. Multipliers for the dual SDP are discovered computer-assistedly, then verified analytically via a single-iteration descent inequality combined with induction. Extends to backtracking (parameter-free) variant and to gradient descent under PŁ as a special case ($f_1 = \tfrac{L}{2}\|x\|^2$).

## Result
Three theorems: (1) sublinear $O(1/N)$ gradient-norm bound for fixed-step boosted DCA, strictly tighter than classical DCA when $\mu > 0$; (2) same rate for a backtracking variant with degraded constants $\bar L, \bar\mu, \bar\alpha$; (3) under PŁ with modulus $\eta$, $\kappa = \eta/L$, gradient descent with step length $\tfrac{3}{(2+\kappa)L}$ achieves linear contraction $\beta = \tfrac{4 - \kappa^3 - 3\kappa}{(2+\kappa)^2}$ — beats the prior best step length $\min\{2/(3L), 1/((1+\sqrt{2}\kappa)L)\}$ for $0 < \kappa < 1/4$.

## Why it matters here
General background; no direct arena tie. Closest relevance: optimizer-design wisdom — confirms that small over-relaxation ($\alpha > 0$) is provably (not just empirically) beneficial for strongly convex DC structure, and demonstrates SDP-PEP as a tool for tightly analyzing custom optimizers, which could inform local-polish step-size choices on smooth problems (e.g. P5/P14/P17 mpmath-polish regimes).

## Open questions / connections
- Generalize to asymmetric curvature ($\mu_1 \neq \mu_2$, $L_1 \neq L_2$, possibly infinite); numerics in Fig. 3 suggest a convex-in-$\alpha$ landscape with optimal $\alpha^\star \approx 0.4$ that current theory misses.
- Conjecture: the SDP performance bound is rank-one and the appendix construction gives the *exact* tight worst-case for all $(\mu, L, \alpha, N)$, not just Example 1.
- Extend to constrained / proximal boosted DCA (Aragón Artacho–Campoy–Vuong, Zhang–Niu); combine with Rotaru–Patrinos–Glineur's generalized-DCA analysis.
- PŁ characterization via Rubbens–Hendrickx–Taylor [17, Prop. 3.4] yields numerically tighter bounds — analytical form still open.

## Key terms
boosted DCA, difference-of-convex algorithm, performance estimation, semidefinite programming, SDP-PEP, smooth interpolation, Polyak-Łojasiewicz inequality, gradient descent step size, strong convexity, L-smoothness, backtracking line search, worst-case convergence rate, Taylor-Hendrickx-Glineur, Abbaszadehpeivasti
