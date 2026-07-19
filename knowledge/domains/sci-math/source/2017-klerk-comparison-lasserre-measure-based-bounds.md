---
type: source
kind: paper
title: Comparison of Lasserre's Measure-Based Bounds for Polynomial Optimization to Bounds Obtained by Simulated Annealing
authors: E. Klerk, M. Laurent
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1703.00744
source_local: ../raw/2017-klerk-comparison-lasserre-measure-based-bounds.pdf
topic: general-knowledge
cites:
---

# Comparison of Lasserre's Measure-Based Bounds for Polynomial Optimization to Bounds Obtained by Simulated Annealing

**Authors:** E. Klerk, M. Laurent  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1703.00744

## One-line
Links Lasserre's SOS-density upper bounds for polynomial minimization on a convex body to simulated-annealing/Boltzmann bounds, upgrading the known $O(1/\sqrt{r})$ convergence to $O(1/r)$.

## Key claim
For $f$ a polynomial of degree $d$ and $K$ a compact set, $f^{(rd)}_K \le \mathbb{E}_{X\sim P_{f/t}}[f(X)] + \|f\|_{\max}/(2r)$ whenever $r \ge e\|f\|_{\max}/t$ (Theorem 4.1). Combined with Kalai–Vempala's annealing rate, this yields $f^{(rd)}_K - f_{\min,K} \le (ne+1)\|f\|_{\max}/r$ for convex $f$ on a convex body (Cor. 4.2), and the same $O(1/r)$ rate extends to non-convex polynomials via a quadratic upper-envelope argument (Cor. 4.3).

## Method
Replace the Boltzmann density $P_{f/t}(x) \propto e^{-f(x)/t}$ by its degree-$2r$ truncated-Taylor approximation $\varphi_{2r,t}(x) \propto \phi_{2r}(f(x)/t)$, which is automatically SOS and hence feasible for Lasserre's program (1). Bound the truncation error via $0 \le \phi_{2r}(\lambda) - e^{-\lambda} \le \lambda^{2r+1}/(2r+1)!$ and Stirling, then plug in the Kalai–Vempala linear-in-$t$ annealing bound $\mathbb{E}[f(X)] - f_{\min,K} \le nt$ (extended here from linear to general convex $f$ by lifting to $\widetilde K = \{(x,x_{n+1}): f(x) \le x_{n+1} \le E_K\}$).

## Result
Lasserre's measure-based upper bound hierarchy converges at rate $O(1/r)$ on convex bodies for arbitrary polynomial $f$, where $2r$ is the SOS-density degree — improving the prior $O(1/\sqrt{r})$ rate of de Klerk–Laurent–Sun. The constant is explicit: $c = (ne+1)(f_{\min,K} + C_{f,1}\,\mathrm{diam}(K) + C_{f,2}\,\mathrm{diam}(K)^2)$ with $C_{f,1} = \max\|\nabla f\|_2$, $C_{f,2} = \max\|\nabla^2 f\|_2$. Numerical tables on Booth, Matyas, Motzkin, and three-hump-camel functions show $f^{(r)}_K$ actually decays much faster than $SA(r)$ in practice — the authors conjecture the true rate may be $O(1/r^2)$.

## Why it matters here
General background for any arena problem reducible to polynomial optimization over a convex body (Lasserre/SOS hierarchies appear in LP-bound style attacks). The $O(1/r)$ rate matters when budgeting SDP degree for upper-bound certificates; the Taylor-SOS density trick is a concrete recipe the optimizer could borrow.

## Open questions / connections
- Is $f^{(r)}_K - f_{\min,K} = O(1/r^2)$ for all polynomials on convex bodies (conjectured from numerics, proven only for hypercube via Jackson kernels in [2])?
- Extends de Klerk–Laurent–Sun [4] convergence analysis; uses Kalai–Vempala [6] annealing bound and Abernethy–Hazan [1] annealing↔interior-point equivalence.
- Complexity comparison between Lasserre SDP (generalized eigenvalue, $O(\binom{n+r}{r}^3)$) and hit-and-run annealing sampling left as incomparable due to different oracle assumptions.

## Key terms
Lasserre hierarchy, sum-of-squares, SOS density, polynomial optimization, Boltzmann distribution, simulated annealing, Kalai-Vempala, measure-based upper bounds, convex body, semidefinite programming, generalized eigenvalue, Taylor truncation, hit-and-run sampling, convergence rate, Motzkin polynomial
