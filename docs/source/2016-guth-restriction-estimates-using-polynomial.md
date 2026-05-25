---
type: source
kind: paper
title: Restriction estimates using polynomial partitioning II
authors: L. Guth
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1603.04250
source_local: ../raw/2016-guth-restriction-estimates-using-polynomial.pdf
topic: general-knowledge
cites:
---

# Restriction estimates using polynomial partitioning II

**Authors:** L. Guth  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1603.04250

## One-line
Improves Stein's restriction-conjecture exponents for the paraboloid in dimensions $n \geq 4$ by introducing a "$k$-broad" weak surrogate for $k$-linear restriction, proved via polynomial partitioning.

## Key claim
For the paraboloid extension operator $E$ in $\mathbb{R}^n$, $\|Ef\|_{L^p} \lesssim \|f\|_{L^p}$ holds for $p > 2 \cdot \frac{3n+1}{3n-3}$ ($n$ odd) and $p > 2 \cdot \frac{3n+2}{3n-2}$ ($n$ even); e.g. $p > 2.8$ in $n=4$ (previous best $p > 3$). The asymptotic lower bound on $p$ improves from $2 + 3n^{-1}$ to $2 + \tfrac{8}{3}n^{-1}$.

## Method
Polynomial partitioning (Guth–Katz) applied to wave-packet decomposition: at scale $R$, partition $\mathbb{R}^n$ by the zero set $Z(P)$ of a degree-$D$ polynomial into cellular vs algebraic regimes, then induct on radius (transverse subcase) and dimension (tangential subcase). The key new device is the $k$-broad norm $\|Ef\|_{BL^p_{k,A}}$, which discounts wave-packet contributions concentrated near $A$ many $(k{-}1)$-planes, sidestepping the obstruction that prevents a full $k$-linear bound. A transverse equidistribution estimate ($|Ef|$ ~ constant along directions perpendicular to $Z$ over scale $R^{1/2}$) closes the tangential induction.

## Result
Sharp $k$-broad estimate $\|Ef\|_{BL^p_{k,A}(B_R)} \lesssim_{K,\epsilon} R^\epsilon \|f\|_{L^2}$ for $p \geq \bar p(k,n) := 2 \cdot \frac{n+k}{n+k-2}$ and all $2 \leq k \leq n$; the exponent $\bar p(k,n)$ is sharp via planar-slab and algebraic-variety (e.g. quadric in $\mathbb{R}^4$) examples. Combined with a decoupling-based broad→linear reduction (Prop 9.1) and $\epsilon$-removal, this gives Theorem 1.1.

## Why it matters here
General background; no direct arena tie. Relevant to any future arena problem involving Fourier restriction, decoupling, or polynomial-method extremal bounds — the polynomial partitioning toolkit (Guth–Katz) and broad/multilinear surrogates are general-purpose techniques for combinatorial-geometric extremal problems that could surface in sphere-packing or kissing-number variants.

## Open questions / connections
- Conjecture 1.4 (honest $k$-linear restriction for $3 \leq k \leq n-1$) remains open; broad norm is a workaround, not a substitute.
- Conjecture 11.1: for an $m$-dim degree-$D$ variety $Z \subset \mathbb{R}^n$, $|\Theta(Z)| \leq C(n,D,\epsilon) R^{(m-1)/2+\epsilon}$ — a special case of Kakeya that would tighten high-dimensional restriction further.
- Extended by [GHI] (Hörmander-type operators, sharp up to endpoint) and [OW] (cone restriction, sharp for $n \leq 5$).

## Key terms
restriction conjecture, paraboloid extension operator, polynomial partitioning, k-linear restriction, k-broad norm, wave packet decomposition, Bennett-Carbery-Tao multilinear, Bourgain-Guth, decoupling, Kakeya conjecture, transverse equidistribution, Hörmander operators
