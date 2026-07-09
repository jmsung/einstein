---
type: source
kind: paper
title: Accelerating the DC algorithm for smooth functions
authors: F. J. A. Artacho, R. Fleming, P. Vuong
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1507.07375
source_local: ../raw/2015-artacho-accelerating-algorithm-smooth-functions.pdf
topic: general-knowledge
cites:
---

# Accelerating the DC algorithm for smooth functions

**Authors:** F. J. A. Artacho, R. Fleming, P. Vuong  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1507.07375

## One-line
Introduces BDCA (Boosted DC Algorithm), accelerating the classical DC algorithm for smooth nonconvex DC programs by adding an Armijo-rule line search along the DCA-generated descent direction.

## Key claim
For smooth DC functions $\phi = f_1 - f_2$ with $f_i$ continuously differentiable convex, the direction $d_k = y_k - x_k$ (where $y_k$ is the DCA subproblem solution from $x_k$) is a descent direction *at $y_k$* with $\langle \nabla\phi(y_k), d_k\rangle \leq -\rho\|d_k\|^2$, enabling a line search beyond the DCA iterate. Under the Łojasiewicz property with exponent $\theta$: finite convergence if $\theta=0$, linear if $\theta \in (0,\tfrac12]$, sublinear rate $k^{-1/(2\theta-1)}$ if $\theta \in (\tfrac12,1)$.

## Method
Strongly-convexify by adding $\tfrac{\rho}{2}\|x\|^2$ to both $f_1, f_2$ to obtain $g - h$ with modulus $\rho$. At each iteration: (1) solve DCA subproblem $\min_x g(x) - \langle\nabla h(x_k), x\rangle$ to get $y_k$; (2) backtrack on $\lambda_k$ along $d_k = y_k - x_k$ until $\phi(y_k + \lambda_k d_k) \leq \phi(y_k) - \alpha\lambda_k^2\|d_k\|^2$; set $x_{k+1} = y_k + \lambda_k d_k$. A second variant adds quadratic interpolation to choose the trial step.

## Result
Proves global convergence to stationary points of $\phi$ and per-iteration decrease $\phi(x_{k+1}) \leq \phi(x_k) - (\lambda_k + \rho)\|d_k\|^2$ (vs DCA's $\rho\|d_k\|^2$). On biochemical reaction network steady-state problems (real-analytic objectives, hence Łojasiewicz holds), BDCA averaged >4× faster wall-clock and ~5× fewer iterations than DCA across multiple network sizes up to Recon 2 scale (thousands of variables). Remark 3.1 shows the descent-at-$y_k$ property fails for nonsmooth $g$.

## Why it matters here
General background; no direct arena tie. Could inform optimizer design for any smooth DC-decomposable objective the agent encounters (some sphere-packing / autocorrelation problems admit DC structure), and the Łojasiewicz-exponent-driven rate analysis is a template for the local-convergence analysis cited in the wiki's parameterization / basin-rigidity discussions.

## Open questions / connections
- Does BDCA-style boosting extend to nonsmooth DC (Remark 3.1 says no in general — what extra structure rescues it)?
- How to estimate Łojasiewicz exponent $\theta$ in practice to predict convergence regime?
- Connection to Fukushima–Mine proximal-line-search algorithm — BDCA explores $\lambda > 0$ from $y_k$ whereas FM uses $\lambda \in (0,1]$ from $x_k$; iterations never coincide.
- Could be combined with mpmath polish as a final-stage smooth-DC refinement.

## Key terms
DC programming, difference of convex, DCA, BDCA, Armijo line search, Łojasiewicz inequality, Łojasiewicz exponent, real analytic, descent direction, Fukushima-Mine, proximal point, strong convexity, nonconvex optimization, biochemical reaction networks, Pham Dinh
