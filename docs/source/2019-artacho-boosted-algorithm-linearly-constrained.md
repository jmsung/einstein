---
type: source
kind: paper
title: The Boosted DC Algorithm for Linearly Constrained DC Programming
authors: F. J. A. Artacho, Rubén Campoy, P. Vuong
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1908.01138
source_local: ../raw/2019-artacho-boosted-algorithm-linearly-constrained.pdf
topic: general-knowledge
cites:
---

# The Boosted DC Algorithm for Linearly Constrained DC Programming

**Authors:** F. J. A. Artacho, Rubén Campoy, P. Vuong  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1908.01138

## One-line
Extends the Boosted DC Algorithm (BDCA) to DC programs with linear constraints by inserting a feasibility-aware line search after each DCA step, accelerating convergence on nonconvex quadratic problems.

## Key claim
For linearly constrained DC programs with a Slater point, every cluster point of the BDCA sequence is a KKT point; when the objective is quadratic, the full sequence is R-linearly (geometrically) convergent to a KKT point without requiring a cluster-point assumption. Empirically, BDCA is ~15× faster than DCA on Horn-matrix copositivity and ~3.65–3.8× faster on $\ell_1$/$\ell_\infty$ trust-region subproblems.

## Method
DC decomposition $\phi = g - h$ with $g$ smooth + indicator of polyhedron $F = \{x : \langle a_i, x\rangle \le b_i\}$, both $g,h$ strongly convex with parameter $\rho$. Each iteration solves the standard DCA convex subproblem to get $y_k$, then — only if $I(y_k) \subseteq I(x_k)$ (equivalently $d_k = y_k - x_k$ is a feasible direction at $y_k$, by Lemma 3.1) — performs a backtracking Armijo line search $\phi(y_k + \lambda d_k) \le \phi(y_k) - \alpha \lambda^2 \|d_k\|^2$ along $d_k$, with self-adaptive trial step (scale by $\gamma>1$ after consecutive acceptances). R-linear rate proof uses Luo–Tseng-style local error bound for affine VI plus Kurdyka–Łojasiewicz exponent $1/2$ for quadratic + indicator.

## Result
Theorem 3.1: $\phi(x_k)$ monotonically decreases, $\sum \|d_k\|^2 < \infty$, every limit point is a KKT point of (P) under Assumptions 1–3 (strong convexity, smoothness of $g$, Slater). Theorem 4.1: for quadratic $\phi(x) = \tfrac12\langle Qx,x\rangle + \langle q,x\rangle$ over a polyhedron, $\|x_k - x^*\| \le C\eta^k$ with $\eta = \beta/(\rho+\beta) \in (0,1)$, where $\beta$ depends on $\|Q\|$, $\sigma$, and the error-bound constant $\tau$. Boosting step activated in ~45% of iterations (copositivity), ~80% ($\ell_1$ TRS), ~40% ($\ell_\infty$ TRS).

## Why it matters here
Directly applicable to Einstein Arena problems with quadratic/DC structure under polyhedral constraints — e.g., box-constrained quadratic polish, $\ell_\infty$ trust-region inner loops, and any NP-hard nonconvex QP that admits DC decomposition $Q = \sigma I - (\sigma I - Q)$. Provides a drop-in 3–15× speedup over plain DCA/projected-gradient with a proven R-linear rate, sharpening the "sequential CPU optimizer" branch of the compute router.

## Open questions / connections
- Can BDCA's line-search trick be extended to *nonlinear* convex constraints? Authors prove a negative-ish result (Remark 3.2): for smooth convex $c_i$, $\langle \nabla c_i(y_k), d_k\rangle \ge 0$ at active constraints, so the boosting step is never triggered — open whether a different direction recovers it.
- Combination with inertial DCA [de Oliveira–Tcheou 2019] left as future work.
- The R-linear rate bound $\beta/(\rho+\beta)$ is loose in practice (observed $\eta \approx 0.9996$ in TRS tests); tighter rate under restricted strong convexity / $\lambda_{\max}(Q)$ control is open.
- Connects to copositivity testing for clique number / stability number via de Klerk–Pasechnik — relevant if any Arena problem reduces to max-clique-style extremal combinatorics.

## Key terms
DC programming, BDCA, DCA, difference of convex functions, KKT point, Slater condition, R-linear convergence, Kurdyka–Łojasiewicz, trust-region subproblem, copositivity, Horn matrix, projected gradient, error bound, Luo–Tseng, quadratic programming, polyhedral constraints, line search, Armijo
