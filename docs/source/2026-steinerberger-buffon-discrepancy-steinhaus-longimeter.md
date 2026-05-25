---
type: source
kind: paper
title: Buffon Discrepancy and the Steinhaus Longimeter
authors: Stefan Steinerberger
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2603.27807v1
source_local: ../raw/2026-steinerberger-buffon-discrepancy-steinhaus-longimeter.pdf
topic: general-knowledge
cites: 
---

# Buffon Discrepancy and the Steinhaus Longimeter

**Authors:** Stefan Steinerberger  ·  **Year:** 2026  ·  **Source:** http://arxiv.org/abs/2603.27807v1

## One-line
Defines and bounds *Buffon discrepancy* — how uniformly a length-$L$ 1D set inside a convex planar domain $\Omega$ intersects every line in proportion to chord length — via generalized Steinhaus longimeter constructions.

## Key claim
For any bounded convex $\Omega\subset\mathbb{R}^2$, the generalized Steinhaus set $S_{n,\varepsilon}\cap\Omega$ with $n\sim L^{1/3}$, $\varepsilon\sim L^{-2/3}$ achieves Buffon discrepancy $\lesssim L^{1/3}$; for the unit disk $\mathbb{D}$, a union of concentric circles achieves Buffon discrepancy $\leq 100$ uniformly in $L$.

## Method
Cauchy–Crofton scaling fixes the canonical proportionality constant $c = 2L/(\pi\,\mathrm{area}(\Omega))$, reducing the problem to discrepancy of a 1D density. For the disk, concentric circles of radii $r_i = \sqrt{1 - i^2\pi^4/(4L^2)}$ discretize the chord-length density $2\sqrt{1-d^2}$ to within $\pm 1$. For general $\Omega$, intersection counts with $S_{n,\varepsilon}$ reduce to the sum $\sum_{k=0}^{n-1}|\sin(\pi k/n + \theta)|$, expanded via the Fourier series of $|\sin|$ and balanced by choosing $n\sim L^{1/3}$.

## Result
Theorem 1: $\max_\ell |\#(\ell\cap S) - (2L/\pi^2)\mathcal{H}^1(\ell\cap\mathbb{D})| \leq 100$ for an explicit concentric-circle construction at any $L$. Theorem 2: for any convex $\Omega$, $\|\#(\ell\cap S) - (2L/(\pi\,\mathrm{area}(\Omega)))\mathcal{H}^1(\ell\cap\Omega)\|_{L^\infty(\mu)} \leq c_\Omega L^{1/3}$, sharp because $n$ lines meeting at the origin force this rate when $n\sim L^{1/3}$.

## Why it matters here
Direct relevance to discrete-geometry / discrepancy-style arena problems where one must equidistribute a 1D structure against a continuous chord-length functional — supplies a Crofton-scaling normalization trick and a parameter-balancing recipe ($n\sim L^{1/3}$) for related lattice/grid constructions; the paper also notes AlphaEvolve was used as an exploratory tool, paralleling the agent's own search workflow.

## Open questions / connections
- Can Buffon discrepancy of order $\sim 1$ be achieved for *every* convex domain (not just the disk), and via what construction?
- Are there non-Steinhaus, non-circular sets attaining $O(1)$ discrepancy on $\mathbb{D}$ (numerics in Figs. 1, 3 suggest yes)?
- Higher-dimensional analogues: in $\mathbb{R}^3$ both "lines" and "co-dim 1" versions are open; connects to integral geometry (Santaló) and quasi-Monte Carlo on the sphere (Liu et al.).

## Key terms
Buffon discrepancy, Cauchy-Crofton formula, Steinhaus longimeter, integral geometry, kinematic measure, geometric discrepancy, chord length distribution, convex domain, concentric circles, equidistribution of lines, Fourier series of |sin|, Steinerberger, Moran, AlphaEvolve
