---
type: source
kind: paper
title: Worst-Case Examples for Lasserre's Measure-Based Hierarchy for Polynomial Optimization on the Hypercube
authors: E. Klerk, M. Laurent
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1804.05524
source_local: ../raw/2018-klerk-worst-case-examples-lasserre-measure-based.pdf
topic: general-knowledge
cites:
---

# Worst-Case Examples for Lasserre's Measure-Based Hierarchy for Polynomial Optimization on the Hypercube

**Authors:** E. Klerk, M. Laurent  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1804.05524

## One-line
Establishes the exact $\Theta(1/d^2)$ convergence rate for Lasserre's measure-based upper-bound hierarchy on the hypercube $[-1,1]^n$, via a reduction to extremal roots of Jacobi orthogonal polynomials.

## Key claim
For polynomial minimization over $K=[-1,1]^n$ with Chebyshev-type product measure, both the Lasserre hierarchy $f_K^{(d)}$ and the stronger De Klerk–Hess–Laurent hierarchy $f^{(d)}$ satisfy $f^{(d)}_{\cdot}-f_{\min,K}=\Theta(1/d^2)$; the lower bound is achieved already by linear objectives $\sum c_i x_i$, and the matching $O(1/d^2)$ upper bound on $f_K^{(d)}$ is new (previously only $O(1/d)$ from [2]).

## Method
Reformulate $f_K^{(d)}$ via Lemma 1.2 as the smallest generalized eigenvalue of a moment matrix $A$ in an orthonormal-polynomial basis. For linear $f$, $A$ is the tridiagonal Jacobi matrix of the three-term recurrence, so $f_K^{(d)}$ equals the smallest root $\xi_{d+1}^{\alpha,\beta}$ of a Jacobi polynomial, with known $\xi_k^{\alpha,\beta}=-1+\Theta(1/k^2)$. For the upper bound, reduce to univariate quadratic $f(x)=x^2+\alpha x$ via a Taylor quadratic majorant $g(x)=f(a)+\nabla f(a)^T(x-a)+C_f\|x-a\|^2$; embed the resulting 5-diagonal Toeplitz block into a circulant matrix whose eigenvalues have a closed-form $a+2b\cos(2\pi j/(d+1))+2c\cos(4\pi j/(d+1))$ and apply Cauchy interlacing.

## Result
Theorem 4.1: $f_K^{(d)}-f_{\min,K}=O(1/d^2)$ for any polynomial $f$ on $[-1,1]^n$ under Chebyshev measure $\prod_i(1-x_i^2)^{-1/2}\,dx_i$. Corollary 3.3 / 3.5: for $f(x)=\sum c_l x_l$, $f_K^{(d)}-f_{\min,K}\ge \sum_l |c_l|(\xi_{d+1}^{\alpha_l,\beta_l}+1)=\Omega(1/d^2)$, and similarly for $f^{(d)}$ using $\min\{\xi_{d+1}^{-1/2,-1/2},\xi_d^{1/2,1/2}\}$. In the Chebyshev case $f_K^{(d)}=-\cos(\pi/(2d+2))$ exactly.

## Why it matters here
General background; no direct arena tie. Relevant if the agent ever uses Lasserre/SOS upper-bound hierarchies for box-constrained polynomial subproblems (e.g., LP/SDP relaxations in autocorrelation or sphere-packing duals) — the $\Theta(1/d^2)$ rate is the asymptotic ceiling for moment-based methods, so for hard arena problems brute-force polynomial-degree increase will not beat polynomial-time grid or specialized SDP.

## Open questions / connections
- Does the $O(1/d^2)$ rate extend from the hypercube to general convex bodies $K$? (Best known: $O(1/d)$ from [2].)
- How does the choice of reference measure $\mu$ quantitatively affect the rate beyond Chebyshev/Jacobi families?
- Is there a saturation theorem: $f_K^{(d)}-f_{\min,K}=o(1/d^2) \iff f$ is constant?

## Key terms
Lasserre hierarchy, sum-of-squares, polynomial optimization, hypercube, Jacobi polynomials, Chebyshev polynomials, extremal zeros, orthogonal polynomials, semidefinite programming, circulant matrix, Toeplitz matrix, Cauchy interlacing, De Klerk, Laurent
