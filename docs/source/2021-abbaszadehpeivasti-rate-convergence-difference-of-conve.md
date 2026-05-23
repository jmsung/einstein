---
type: source
kind: paper
title: On the Rate of Convergence of the Difference-of-Convex Algorithm (DCA)
authors: Hadi Abbaszadehpeivasti, Etienne de Klerk, M. Zamani
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2109.13566
source_local: ../raw/2021-abbaszadehpeivasti-rate-convergence-difference-of-conve.pdf
topic: general-knowledge
cites:
---

# On the Rate of Convergence of the Difference-of-Convex Algorithm (DCA)

**Authors:** Hadi Abbaszadehpeivasti, Etienne de Klerk, M. Zamani  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2109.13566

## One-line
Derives tight non-asymptotic worst-case convergence rates for the Difference-of-Convex Algorithm (DCA) using semidefinite programming performance estimation.

## Key claim
For DC problems $\min f_1(x) - f_2(x)$ with $f_1 \in \mathcal{F}_{\mu_1,L_1}$, $f_2 \in \mathcal{F}_{\mu_2,L_2}$, the DCA achieves $\min_{1\le k\le N+1}\|g_1^k - g_2^k\| \le \sqrt{A\Delta/(BN+C)} = O(1/\sqrt{N})$ without strong convexity assumptions, with the bound shown exact via an explicit construction; under the Polyak-Łojasiewicz inequality, $f(x_2)-f_\star \le \tfrac{1-\eta/L_1}{1+\eta/L_2}(f(x_1)-f_\star)$ (linear convergence).

## Method
Performance Estimation Problem (PEP) framework of Drori-Teboulle: cast the worst-case rate as an infinite-dimensional optimization over function classes, use Taylor-Hendrickx-Glineur interpolation conditions to reformulate as a finite SDP, then bound the SDP optimum via a hand-constructed dual feasible solution (multipliers guessed numerically, verified analytically by constraint aggregation). Applied to two termination criteria: subgradient-gap $\|g_1^k-g_2^k\|$ (smooth case) and $T(x_{k+1}) = f_1(x_k)-f_1(x_{k+1})-\langle g_2^k, x_k-x_{k+1}\rangle$ (nonsmooth case).

## Result
Three rates: (1) $O(1/\sqrt{N})$ gradient-norm bound in Corollary 3.1, with constants tighter than Le Thi et al. [26]'s $\sqrt{2\Delta/((\mu_1+\mu_2)N)}$, plus a matching tight example (Example 3.1). (2) New $O(1/N)$ rate $\min_k T(x_{k+1}) \le \min(L_2/(N(L_2+\mu_1)-\mu_1), L_1/(N(L_1+\mu_2)))\cdot (f(x_1)-f_\star)$ for the alternate criterion, valid even when both $L_1=L_2=\infty$ (fully nonsmooth). (3) Explicit linear-rate constants under PL, removing strong-convexity and bounded-iterate assumptions of Le Thi et al. [27].

## Why it matters here
General background; no direct arena tie. DC decompositions appear in sparse-signal / penalty formulations and could inform nonconvex surrogates for arena problems, but the paper is theory of convergence rates, not a technique for any specific Einstein Arena problem.

## Open questions / connections
- Extension to convex-polynomial DC decompositions (Ahmadi-Hall [3]) — could yield problem-specific rates for polynomial objectives.
- Quadratic-polynomial DC for constrained / trust-region problems (open per Section 6).
- Performance-estimation methodology itself is the reusable artifact — could be applied to other first-order schemes (basin hopping, parallel tempering) used in this repo if recast as fixed-step methods.

## Key terms
difference-of-convex programming, DCA, convex-concave procedure, performance estimation problem, semidefinite programming, Polyak-Łojasiewicz inequality, Łojasiewicz exponent, Toland duality, subgradient, worst-case convergence rate, nonsmooth optimization, Drori-Teboulle, Taylor-Hendrickx-Glineur interpolation
