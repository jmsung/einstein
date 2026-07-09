---
type: source
kind: paper
title: A Boosted-DCA with Power-Sum-DC Decomposition for Linearly Constrained Polynomial Programs
authors: Hu Zhang, Yi-Shuai Niu
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2205.02571
source_local: ../raw/2022-zhang-boosted-dca-power-sum-dc-decomposition-linearly.pdf
topic: general-knowledge
cites:
---

# A Boosted-DCA with Power-Sum-DC Decomposition for Linearly Constrained Polynomial Programs

**Authors:** Hu Zhang, Yi-Shuai Niu  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2205.02571

## One-line
Introduces a power-sum-of-linear-forms DC decomposition for arbitrary multivariate polynomials and a boosted DCA with exact line search (BDCAe) that exploits it to solve linearly constrained polynomial optimization problems.

## Key claim
Any form $f \in H_d[x]$ admits a power-sum DC decomposition $f(x) = \sum_{\alpha \in I_+} \lambda_\alpha \langle \alpha, x\rangle^d - \sum_{\alpha \in I_-} (-\lambda_\alpha)\langle \alpha, x\rangle^d$ where $\lambda$ is obtained by solving the sparse linear system $V(n,d)\lambda = c$ with the (nonsingular) power-product matrix $V(n,d)$; and BDCAe converges to critical points with KL-rate guarantees while its exact line search reduces to finding roots of an explicitly-coefficiented univariate polynomial on an interval.

## Method
DC decomposition: two variants — termwise (T-PSDC) applied per homogeneous component, and homogenizing-dehomogenizing (HD-PSDC) which lifts $f$ to one extra variable $x_h$, decomposes the resulting even-degree form, then sets $x_h=1$. Algorithm: BDCAe iterates a convex subproblem $\min_{x \in P} g_i(x) - \langle \nabla h_i(x_k), x\rangle$ solved by Fast Dual Proximal Gradient (FDPG) exploiting the separable power-sum block structure, then performs an exact line search $t_k = \arg\min_{t \in [0,\bar t]} \hat f(t)$ along the DC descent direction $d_k = y_k - x_k$, where $\bar t = \min_{i \in I(d_k)}(b_i - \langle a_i, y_k\rangle)/\langle a_i, d_k\rangle$ bounds feasibility. The line search reduces to root-finding on a univariate polynomial whose coefficients come from the power-sum representation.

## Result
Subsequential convergence of $\{x_k\}$ to a DC critical point of (POPL) is proven; under the Kurdyka–Łojasiewicz property convergence rates are established for $\{f(x_k)\}$. Empirically on MVSK portfolio optimization and box-constrained polynomial problems, BDCAe beats DCA, BDCA (Armijo), UDCA, UBDCA on CPU time and is competitive with or better than FILTERSD/FMINCON especially when $d$ is even and $n \ge 30$; HD-PSDC runs ~2× faster than T-PSDC on even degrees and both are ≥3× faster than DSOS-DC across all tests. Sparsity of $V(n,d)$ exceeds 90% for $n>6$ at $d \in \{3,4,5,6\}$ and approaches 1 as $n \to \infty$.

## Why it matters here
General background; no direct arena tie — BDCAe targets dense polynomial programs on polyhedra (portfolio, box constraints), which is not the working regime for any of the 23 Einstein Arena problems whose optimizers are SLSQP / L-BFGS / NM / basin-hopping / parallel tempering / mpmath polish. The exact-line-search-via-univariate-roots idea is a small possibly-reusable trick if a future problem reduces to polynomial DC on a polyhedron.

## Open questions / connections
- How to generate power-sum DC decompositions with minimal number of square terms (impacts DCA efficiency)?
- Adaptive update rule for the strong-convexity modulus $\rho$ — tradeoff: small $\rho$ tightens the DC decomposition (fewer outer iterations) but large $\rho$ accelerates FDPG on the inner convex subproblem.
- Extends Ahmadi–Hall DSOS/SDSOS-DC (LP/SOCP/SDP-based) and Niu's earlier projective $\sigma\|x\|^2$ DC; relates to Reznick's sums-of-even-powers representation and Comon–Mourrain Waring-style decomposition of binary forms.

## Key terms
DC programming, DCA, boosted DCA, exact line search, power-sum decomposition, power-product matrix, DC-SOS decomposition, Kurdyka-Łojasiewicz property, Fast Dual Proximal Gradient, polynomial optimization, MVSK portfolio, Niu, Le Thi, Pham Dinh Tao, Ahmadi
