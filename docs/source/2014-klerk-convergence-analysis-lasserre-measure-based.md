---
type: source
kind: paper
title: Convergence analysis for Lasserre’s measure-based hierarchy of upper bounds for polynomial optimization
authors: E. Klerk, M. Laurent, Zhao Sun
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1411.6867
source_local: ../raw/2014-klerk-convergence-analysis-lasserre-measure-based.pdf
topic: general-knowledge
cites:
---

# Convergence analysis for Lasserre's measure-based hierarchy of upper bounds for polynomial optimization

**Authors:** E. Klerk, M. Laurent, Zhao Sun  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1411.6867

## One-line
Proves an $O(1/\sqrt{r})$ convergence rate for Lasserre's measure-based hierarchy of SDP upper bounds for minimizing a continuous function over a compact set $K$.

## Key claim
For $K$ compact satisfying a mild interior-ball density assumption and $f$ Lipschitz with constant $M_f$, the degree-$2r$ SOS-density upper bound $f^{(r)}_K$ satisfies $f^{(r)}_K - f_{\min,K} \le \zeta(K) M_f / \sqrt{r}$ for all $r \ge r_K + 1$, where $\zeta(K)$ depends only on $K$.

## Method
Lasserre's reformulation expresses $f_{\min,K} = \inf_h \int_K f h\,dx$ over SOS densities $h \in \Sigma[x]_r$ with $\int_K h\,dx = 1$, computable as a generalized eigenvalue problem in the moments $m_\alpha(K)$. The convergence proof picks an explicit feasible density: the degree-$2r$ Taylor truncation $H_{r,a}$ of a Gaussian centered at the minimizer $a \in K$ (which is SOS by Hilbert's univariate theorem applied to $\phi_{2r}(t) = \sum_{k=0}^{2r}(-t)^k/k!$), then bounds $\int_K \|x-a\| H_{r,a}\,dx$ via Stirling and the geometric Assumption 1: $\mathrm{vol}(B_\epsilon(a) \cap K) \ge \eta_K \epsilon^n \gamma_n$.

## Result
Main bound (Theorem 3): $f^{(r)}_K - f_{\min,K} \le \zeta(K) M_f / \sqrt{r}$; for polynomials of degree $d$ on a convex body, $f^{(r)}_K - f_{\min,K} \le 2d^2 \zeta(K) \sup_K |f| / (w_{\min}(K) \sqrt{r})$ via Markov's inequality. Closed-form $\eta_K, \epsilon_K, r_K$ are given for the hypercube ($\eta_K \sim 1/(2\sqrt{n})$), simplex ($\eta_K \sim 1/\sqrt{2n}$), and unit ball. Numerical experiments on Booth, Matyas, Three-Hump Camel, Motzkin, Styblinski–Tang, and Rosenbrock confirm fast practical convergence; conditional-distribution sampling from the optimal SOS density yields feasible points beating uniform sampling (Markov: $\Pr[f(X) \ge (1+\epsilon)f^{(r)}_K - \epsilon f_{\min,K}] \le 1/(1+\epsilon)$). Whether $1/\sqrt{r}$ is tight remains open.

## Why it matters here
Directly relevant to any Einstein Arena problem expressible as polynomial minimization over a simplex / hypercube / ball — provides a principled SDP-based upper-bound hierarchy with provable rate, complementing Lasserre's better-known lower-bound hierarchy. The Gaussian-Taylor SOS density construction is a reusable technique for proving rates of SOS approximation schemes.

## Open questions / connections
- Is $1/\sqrt{r}$ the true rate, or can it be sharpened to $1/r$ (matching the multinomial bound on the simplex) or $1/r^2$ (matching hypergeometric)?
- Can more general nonnegativity certificates than SOS (e.g., Schmüdgen, Putinar with weights for $K$) improve the constant or rate?
- Extends [Lasserre 2011, SIAM J. Optim. 21] qualitative convergence to quantitative; complements lower-bound rates of Schweighofer (Schmüdgen, $O(1/\sqrt[c]{2r})$) and Nie–Schweighofer (Putinar).
- Sampling from the optimal SOS density as a multi-start seed for global optimization heuristics.

## Key terms
Lasserre hierarchy, SOS density, polynomial optimization, semidefinite programming, upper bound, measure-based hierarchy, Gaussian Taylor truncation, Lipschitz, convex body, interior cone condition, moments, generalized eigenvalue, simplex, hypercube, Euclidean ball, Markov inequality
