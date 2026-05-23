---
type: source
kind: paper
title: Globally Solving Nonconvex Quadratic Programs via Linear Integer Programming Techniques
authors: Wei Xia, Juan C. Vera, L. Zuluaga
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1511.02423
source_local: ../raw/2015-xia-globally-solving-nonconvex-quadratic.pdf
topic: general-knowledge
cites: 
---

# Globally Solving Nonconvex Quadratic Programs via Linear Integer Programming Techniques

**Authors:** Wei Xia, Juan C. Vera, L. Zuluaga  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1511.02423

## One-line
Reformulates non-convex quadratic programs as mixed-integer linear programs (MILPs) by linearizing the KKT conditions and using big-$M$ constraints with explicitly computable dual-variable bounds.

## Key claim
Any QP $\min \tfrac{1}{2}x^\top H x + f^\top x$ s.t. $Ax=b, x\ge 0$ with bounded non-empty feasible set admits an equivalent MILP reformulation (IQP), where the big-$M$ on dual variables can be set to $M > (\kappa + \|f\|_\alpha^*) H_{A,b} \|e\|_\beta$ with $\kappa = \max\{\|Hx\|_\alpha^* : Ax=b, x\ge 0\}$ and $H_{A,b}$ a Hoffman constant — and at least one globally optimal KKT point satisfies $e^\top \lambda^* \le M$.

## Method
Use the QP's KKT conditions as redundant constraints, then apply the Giannessi–Tomasin identity $\tfrac{1}{2}x^\top Hx + f^\top x = \tfrac{1}{2}(f^\top x - b^\top \mu)$ to linearize the objective. Model the complementarity $x^\top \lambda = 0$ via binary $z_j$ with big-$M$ constraints $x_j \le z_j U_j$, $\lambda_j \le (1-z_j) V_j$. Dual bounds $V$ come from a perturbation argument: relax $x\ge 0$ to $x\ge -te$, penalize $t$ in the objective, and use the Hoffman bound on the non-negativity constraints (Güler–Hoffman–Rothblum 1995) to force $t^*=0$ at optimum.

## Result
Closed-form Hoffman constants: $H_{A,b}=2$ for standard QP on the simplex ($\ell_1/\ell_1$ norms), giving $M = 2n(\|H\|_{\infty,\infty} + \|f\|_\infty)$; $H_{A,b}=1$ for box-constrained QP ($\ell_\infty/\ell_\infty$), giving an explicit $M$ in terms of $\|u-l\|$. For general QP, $H_A$ is computed via extreme points of a dual polytope (Proposition 3). Empirically `quadprogIP` outperforms `quadprogBB`, BARON, and CPLEX by orders of magnitude on standard QP (SQP, StableQP, Scozzari/Tardella) instances; CPLEX wins on BoxQP. Unlike `quadprogBB`, the method handles QPs with unbounded dual feasible sets.

## Why it matters here
General background; no direct arena tie. Could be a tool for **autocorrelation/extremal-graph** problems if reformulated as small QPs (Motzkin–Straus → clique number is cited), but most arena problems are too large or non-quadratic for direct MILP attack. Mostly a pointer to MILP-via-KKT-linearization as a verification path for small QP subproblems.

## Open questions / connections
- Efficient computation of the Hoffman constant $H_A$ in (20) for general $A$ is open (Zheng–Ng 2004, Peña–Vera–Zuluaga 2017).
- Tightening big-$M$ constants — current bounds are loose for BoxQP large-scale instances.
- Extension to copositive programming via Burer (2009) completely positive reformulation, suggested as future work.
- Hansen et al. (1993) valid cuts $z_i^x + z_i^s = 1$ when $H_{ii} < 0$ strengthen BoxQP IQP — generalizable?

## Key terms
quadratic programming, KKT conditions, mixed-integer linear programming, big-M reformulation, Hoffman bound, linear complementarity problem, standard quadratic program, box-constrained QP, Motzkin-Straus, complementarity constraints, dual variable bounds, completely positive programming, quadprogIP, Giannessi-Tomasin
