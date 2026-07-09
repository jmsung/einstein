---
type: source
kind: paper
title: Conditions for linear convergence of the gradient method for non-convex optimization
authors: Hadi Abbaszadehpeivasti, Etienne de Klerk, M. Zamani
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2204.00647
source_local: ../raw/2022-abbaszadehpeivasti-conditions-linear-convergence-gradie.pdf
topic: general-knowledge
cites:
---

# Conditions for linear convergence of the gradient method for non-convex optimization

**Authors:** Hadi Abbaszadehpeivasti, Etienne de Klerk, M. Zamani  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2204.00647

## One-line
Sharpens the linear-convergence rate of fixed-step gradient descent on smooth non-convex functions satisfying the Polyak–Łojasiewicz (PL) inequality, and proves PL is both necessary and sufficient for linear convergence in this class.

## Key claim
For $f \in F_{\mu,L}(\mathbb{R}^n)$ with $\mu \in (-\infty, 0]$, $L \in (0, \infty)$, satisfying PL with constant $\mu_p$ on the sublevel set, the gradient step with $t_1 = 1/L$ and $\mu = -L$ gives $f(x_2) - f^\star \le \tfrac{2L - 2\mu_p}{2L + \mu_p}(f(x_1) - f^\star)$, strictly tighter than the classical Polyak rate $1 - \mu_p/L$. Moreover, Algorithm 1 is linearly convergent on $\{x : f(x) \le f(x_1)\}$ **iff** $f$ satisfies PL there (Theorem 5).

## Method
Performance Estimation Programming (PEP) à la Drori–Teboulle: the worst-case ratio $(f(x_2)-f^\star)/(f(x_1)-f^\star)$ is cast as a finite SDP via the Rotaru–Glineur–Panagiotis hypoconvex interpolation theorem ($F_{\mu,L}$ class). Closed-form dual multipliers are constructed by hand to give analytic upper bounds across three step-length regimes ($t_1 \in (0, 1/L]$, an intermediate cubic-root regime, and $t_1 \in [\cdot, 2/L)$); the optimal step length is the root of an explicit cubic $r(t)$.

## Result
Three-piece closed-form rate (Theorem 3) covering $t_1 \in (0, 2/L)$; the optimal step is characterized by Proposition 1 as the root of $r(t) = L\mu(L+\mu-\mu_p)t^3 - (L^2 - \mu_p(L+\mu) + 5L\mu + \mu_2)t^2 + 4(L+\mu)t - 4$. Theorem 4: on $F_{\mu,L}$ a non-constant function satisfying the Łojasiewicz inequality with exponent $\theta$ must have $\theta \ge 1/2$ (rules out faster-than-linear regimes for smooth bounded-curvature functions). Theorem 6 maps PL ↔ quadratic functional growth ↔ quadratic gradient growth ↔ quasar-convexity, giving sharpened PEP-derived rates in each case (e.g., Theorem 7: $(\mu_q/(2L - 2\mu_q))^N$ for $\mu_q$-quadratic-functional-growth, $\mu_q \in (L/2, L)$, beating the PL-implied rate).

## Why it matters here
General background; no direct arena tie. Most arena problems use specialized optimizers (LP/SDP/Remez/parallel tempering/mpmath polish) rather than vanilla fixed-step gradient descent — see compute-router. Could inform step-size choice in any L-BFGS / gradient-polish phase where a PL-like sublevel structure is suspected (e.g., near a known basin in P5/P11/P15/P17), but the bounds here assume global PL on a sublevel set, which is rarely verified in arena workloads.

## Open questions / connections
- Tightest PEP bound for Algorithm 1 under PL is still open — Theorem 3 is sharp in known multipliers but not proven tight against the SDP optimum.
- Extension to accelerated / momentum methods (Nesterov, "Algorithm 2") under PL — flagged as future work.
- Relationship to Kurdyka–Łojasiewicz with $\theta \in (1/2, 1)$ (sublinear regime) and to biased-SGD analysis (Hu–Seiler–Lessard 2021) is not worked out here.

## Key terms
Polyak-Łojasiewicz inequality, gradient method, fixed step length, performance estimation programming, semidefinite programming, hypoconvex interpolation, quadratic functional growth, quadratic gradient growth, quasar-convex, Łojasiewicz exponent, linear convergence rate, Drori-Teboulle, non-convex smooth optimization
