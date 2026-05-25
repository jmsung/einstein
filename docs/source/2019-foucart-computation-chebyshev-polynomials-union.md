---
type: source
kind: paper
title: Computation of Chebyshev Polynomials for Union of Intervals
authors: S. Foucart, J. Lasserre
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1903.04335
source_local: ../raw/2019-foucart-computation-chebyshev-polynomials-union.pdf
topic: general-knowledge
cites:
---

# Computation of Chebyshev Polynomials for Union of Intervals

**Authors:** S. Foucart, J. Lasserre  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1903.04335

## One-line
Numerical SDP-based procedures to compute weighted Chebyshev polynomials of the first kind ($L^\infty$-minimal monic) and second kind ($L^1$-minimal monic) on $K = \bigcup_{\ell=1}^L [a_\ell, b_\ell] \subseteq [-1,1]$.

## Key claim
For any finite union of compact intervals $K$ and rational weight $w = \Sigma/\Omega$, the monic Chebyshev polynomial $T_N^{K,w}$ minimizing $\|P w\|_K$ is computed exactly by a single SDP (Theorem 2); for the second-kind problem $U_N^{K,w}$ minimizing $\|P/w\|_{L^1(K)}$, a hierarchy of SDPs indexed by $d \geq N$ produces ersatz polynomials $V_{N,d}^K$ with $\|V_{N,d}^K\|_d \nearrow \|U_N^K/w\|_{L^1(K)}$ and a computable a-posteriori relative error $\delta_{N,d}^K$ (Theorem 5, Proposition 6).

## Method
First kind: encode the constraint $-c\Sigma \leq \Omega P \leq c\Sigma$ on each $[a_\ell, b_\ell]$ via an exact SDP characterization of polynomial nonnegativity on a sub-interval (Proposition 1, in the Chebyshev basis with parameters $\alpha_\ell, \beta_\ell$ depending on $\arccos a_\ell, \arccos b_\ell$). Second kind: rewrite $\|P/w\|_{L^1(K)}$ as an infimum over Jordan decompositions of signed measures, then apply the discrete trigonometric moment problem — a sequence $y$ is a moment sequence on $[0,\pi]$ iff its infinite Toeplitz matrix $\mathrm{Toep}_\infty(y) \succeq 0$ — and truncate at order $d$. Extra constraints (e.g. all roots inside $K$) are added via $2^{L-1}$ sign-pattern SDPs enforcing nonnegativity on each gap $[b_\ell, a_{\ell+1}]$.

## Result
Theorem 2 gives an exact SDP for $T_N^{K,w}$ with rational weight. Proposition 4 defines a norm $\|P\|_d$ via truncated Toeplitz/moment SDP and proves monotone convergence $\|P\|_d \nearrow \|P/w\|_{L^1(K)}$. Theorem 5 proves $V_{N,d}^K \to U_N^K$ along subsequences (full sequence under uniqueness). Proposition 6 gives two-sided bounds $\|V_{N,d}^K\|_d \leq \|U_N^K/w\|_{L^1(K)} \leq \|V_{N,d}^K/w\|_{L^1(K)}$; numerics show $\delta_{N,d}^K \approx 6\text{–}8 \cdot 10^{-4}$ for $N=5$, $L=3$. Proposition 7: $U_N^K$ is unique iff it has $N$ simple roots all inside $K$.

## Why it matters here
Direct toolkit for any arena problem reducible to a minimax-polynomial / extremal-polynomial problem on a disconnected real set — informs the [[equioscillation]], [[remez-exchange]], and [[sdp-relaxation]] concepts, complementing [[parallel-tempering]] and [[mpmath-polish]] with an exact-by-construction alternative for low/medium $N$. Particularly relevant if any arena problem (autocorrelation P15/P16, uncertainty-style, or interval-supported LP dual) admits a Chebyshev / minimum-$L^1$ reformulation over a union of intervals.

## Open questions / connections
- Extends Peherstorfer's orthogonal-polynomial construction (which requires the strict-Chebyshev / $N+L$ equioscillation condition) to the general case where strictness fails.
- A-priori $d(\varepsilon)$ for prescribed accuracy in the second-kind hierarchy is left open — only a-posteriori bound $\delta_{N,d}^K$ is given.
- How does this scale vs the Filip Remez-type implementation [5] in wall-clock and accuracy for large $L$, $N$?
- Can the restricted-roots construction (sign-pattern enumeration over $2^{L-1}$ SDPs) be replaced by a single SDP using SOS on the gaps?

## Key terms
Chebyshev polynomials first kind, Chebyshev polynomials second kind, semidefinite programming, union of intervals, polynomial nonnegativity, method of moments, Toeplitz matrix, discrete trigonometric moment problem, equioscillation, capacity logarithmic potential, Remez exchange, restricted Chebyshev polynomial, Foucart Lasserre, weighted L1 minimization, monic polynomial extremal
