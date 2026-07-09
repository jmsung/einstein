---
type: source
kind: paper
title: Log--optimal (d+2)-configurations in d-dimensions
authors: P. Dragnev, O. Musin
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1909.09909
source_local: ../raw/2019-dragnev-log-optimal-configurations-d-dimensions.pdf
topic: general-knowledge
cites:
---

# Log--optimal (d+2)-configurations in d-dimensions

**Authors:** P. Dragnev, O. Musin  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1909.09909

## One-line
Classifies all local minima of the logarithmic energy for $d+2$ points on $S^{d-1}$ as pairs of orthogonal regular simplexes, and identifies the global minimum.

## Key claim
Up to orthogonal transform, every local minimum of $E_{\log}(X)$ for $N=d+2$ points on $S^{d-1}$ ($d\geq 2$) consists of two mutually orthogonal regular simplexes of sizes $m\geq n>1$ with $m+n=d+2$; the global minimum is $m=n$ when $d$ is even and $m=n+1$ when $d$ is odd.

## Method
Lagrange-multiplier "force equations" yield $\sum_{j\neq i}(x_i-x_j)/r_{ij}=(N-1)x_i$ and centroid at origin. Setting $a_{ij}:=c-1/r_{ij}$ with $c=(N-1)/N$, the matrix $A$ has rank $\leq 1$ when $N=d+2$, so $a_{ij}=a_ia_j$; convexity of $F(t)=\sum_j (c-a_j^2)/(c-ta_j)$ on $(-\sqrt c,\sqrt c)$ forces at most two distinct $a_i$ values, splitting $X$ into two orthogonal regular simplexes. Local-minimum proof uses two quadratic-form lemmas (5.1, 5.2) on perturbation matrices with zero row/column sums.

## Result
Stationary non-degenerate configurations of $d+2$ points partition into exactly two orthogonal regular simplexes (Theorem 2.1); degenerate configurations cannot be local minima for strictly convex $h$ (Theorem 2.3); $\{1,k,l\}$-type stationary configs (one vertex equidistant to others) are saddle points (Theorem 2.4). The optimal pair gives inner products $-1/(k-1)$ within the $k$-simplex, $-1/(N-k-1)$ within the other, and $0$ across — a two-distance set / 2-design when $d$ is even. Morse indices on $\mathrm{Conf}(3,5)$: $C_0$ (regular pentagon, degenerate) has index 2, $C_1$ (FP-type $\{1,2,2\}$) has index 1, $C_2$ ($\{2,3\}$ TBP) has index 0.

## Why it matters here
Directly relevant to small-$N$ spherical energy / packing problems on $S^{d-1}$: gives a closed-form log-optimum at $N=d+2$ and identifies the orthogonal-simplex-split structure that recurs in Kuperberg's best-packing classification for $d+k$ points ($2\leq k\leq d$). Useful prior for Thomson-type / Riesz-energy problems on the arena where $N$ is just past the simplex.

## Open questions / connections
- Extend Theorem 1.1 from $k=2$ to $2<k\leq d$ (conjecture: orthogonal-simplex split matches Kuperberg-type theorem 6.2 for all $k$).
- Riesz potential $h(t)=(1-t)^{-s/2}$ on $\mathrm{Conf}(3,5)$: TBP vs FP transition at $s^*\approx 15.048$ (Schwartz); analogous transition $s^*(d)$ for $d+2$ on $S^{d-1}$ is open, esp. Newton case $s=d-2$.
- Compute Morse indices of all stationary configs on $\mathrm{Conf}(d,d+2)$ for general $d$; extend bi-quadratic-energy optimality (Tumanov) and SDP bounds (Musin) to this class; connections to Smale's 7th problem on near-log-optimal configs on $S^2$.

## Key terms
logarithmic energy, Thomson problem, Riesz potential, spherical configurations, orthogonal regular simplexes, cross-polytope, regular simplex, universally optimal, stationary configurations, Morse index, Kuperberg theorem, two-distance set, Dragnev, Musin, Cohn-Kumar, Whyte problem, triangular bi-pyramid, force equations, balanced configurations, 1-design
