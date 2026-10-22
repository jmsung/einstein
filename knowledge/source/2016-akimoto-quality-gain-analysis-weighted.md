---
type: source
kind: paper
title: Quality Gain Analysis of the Weighted Recombination Evolution Strategy on General Convex Quadratic Functions
authors: Youhei Akimoto, A. Auger, N. Hansen
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1608.04813
source_local: ../raw/2016-akimoto-quality-gain-analysis-weighted.pdf
topic: general-knowledge
cites:
---

# Quality Gain Analysis of the Weighted Recombination Evolution Strategy on General Convex Quadratic Functions

**Authors:** Youhei Akimoto, A. Auger, N. Hansen  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1608.04813

## One-line
Derives a finite-dimensional error bound for the per-step quality gain of weighted-recombination evolution strategies (the (μ/μ_w,λ)-ES family underlying CMA-ES) on arbitrary convex quadratic functions, yielding closed-form optimal recombination weights and step-size.

## Key claim
For $f(x)=\tfrac12(x-x^*)^TA(x-x^*)$, the normalized quality gain $\bar\varphi$ converges to the asymptotic form $\varphi$ with an explicit error bound that vanishes whenever $\mathrm{Tr}(A^2)/\mathrm{Tr}(A)^2\to 0$ (true e.g. for bounded eigenvalues, even up to eigenvalues in $[1,\sqrt N]$) OR $\sigma/\|m\|\to 0$ (i.e. $c_m\to\infty$). The optimal recombination weights are $w_k^*\propto -E[N_{k:\lambda}]$ — **independent of the Hessian $A$** — while the optimal step-size scales with $\|\nabla f(m)\|/\mathrm{Tr}(A)$.

## Method
Rigorous quality-gain decomposition $\varphi = g(m)\cdot\bar\varphi(m,\bar\sigma)$ where $g(m)=\|\nabla f(m)\|^2/f(m)$. The candidate ranking is replaced by an explicit weight function $W(i;(X_k))$ defined via binomial / trinomial tail probabilities, keeping the $X_i$ mutually independent (avoiding the order-statistic correlation that breaks earlier heuristic derivations). Concentration inequalities of Laurent–Massart on $Z^TAZ-1$ plus Lipschitz bounds on the weight functions $u_1,u_2,u_3$ deliver the finite-$N$ error bound.

## Result
- Asymptotic normalized quality gain on the sphere: $\bar\varphi_\infty(\bar\sigma^*,(w_k^*)) = \tfrac12\sum_{i=1}^\lambda E[N_{i:\lambda}]^2$, optimal $\bar\sigma^*=\sum|E[N_{i:\lambda}]|$.
- With optimal weights $\bar\varphi_\infty/\lambda \to 0.5$ as $\lambda\to\infty$; nonnegative weights cap at $0.25$; truncation weights give only $\Theta(\mu\log(\lambda/\mu))$.
- Error bound is controlled by $\mathrm{Tr}(A^2)/\mathrm{Tr}(A)^2$: tight for Cigar ($\sim 1/(N-1)$), loose for Discus ($\sim 1$ when $N\le\alpha$).
- Numerics: theoretical $\bar\sigma^*$ approximates the empirically optimal step-size well already at $c_m=1$, $N=10$–$1000$.

## Why it matters here
General background for evolution-strategy / CMA-ES tuning; informs the **compute-router** layer when choosing population sizes and step-sizes for CMA-ES large-pop runs (compute-router.md lists CMA-ES large-population as a routed workload). No direct tie to a specific Einstein Arena problem, but relevant whenever an optimizer uses weighted recombination ES on a locally-quadratic landscape (basin polish near optima for P1, P11, P15, P16).

## Open questions / connections
- Extends Arnold 2005 (sphere) and Beyer–Melkozerov / Beyer–Hellwig (ellipsoid dynamics) to general convex quadratic with rigorous finite-$N$ bound.
- Leaves open: optimal *update rule* (not just optimal parameter value), including covariance matrix update — neither quality-gain nor dynamical-system approaches answer this.
- Distribution of the gradient direction $e=\nabla f(m)/\|\nabla f(m)\|$ along trajectories is not characterized; empirically $e$ aligns with the smallest-eigenvalue eigenspace of $A$.
- The step-size adaptation problem (since optimal $\sigma$ depends on the unknown $\|\nabla f(m)\|$) remains the practical gap.

## Key terms
evolution strategy, weighted recombination, CMA-ES, quality gain, progress rate, normalized step-size, convex quadratic function, normal order statistics, recombination weights, effective variance selection mass, mutation strength, Hessian-independence
