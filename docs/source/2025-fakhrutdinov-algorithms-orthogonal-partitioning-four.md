---
type: source
kind: paper
title: Algorithms for orthogonal partitioning into four parts
authors: A. Fakhrutdinov, O. Musin
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2511.20866
source_local: ../raw/2025-fakhrutdinov-algorithms-orthogonal-partitioning-four.pdf
topic: general-knowledge
cites:
---

# Algorithms for orthogonal partitioning into four parts

**Authors:** A. Fakhrutdinov, O. Musin  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2511.20866

## One-line
An optimal $\Theta(n)$ algorithm for the discrete pancake theorem (cutting $n$ planar points into four equal parts via two perpendicular lines), plus polynomial-time algorithms for the higher-dimensional orthogonal mass-partition theorems.

## Key claim
Theorem 1: Given $n$ points in $\mathbb{R}^2$, an orthogonal cut partitioning them into four equal parts can be computed in $\Theta(n)$ time, matching a proven $\Omega(n)$ lower bound. Theorem 2: For $d$ mutually orthogonal hyperplanes in $\mathbb{R}^d$ (Theorem A) or two orthogonal hyperplanes bisecting $m$ sets in $\mathbb{R}^{\delta(m)}$ (Theorem B), valid partitions are found in time $O(n^{d(d+1)/2})$ and $O(n^{2d})$ respectively.

## Method
Dual transformation $D(a,b) = \{y = ax - b\}$ turns the partition problem into finding two points on the median level $\mu_H$ of a line arrangement, with the orthogonality constraint $c = -1/a$. A prune-and-search algorithm (after Lo–Matoušek–Steiger) repeatedly divides the parameter interval into sub-intervals containing $\leq \alpha n^2 / 2$ intersections, localizes the median levels $L_p$ and $L_q$ inside trapezoids of width $\varepsilon |G|$, and discards $\geq |G|/2$ lines per phase using $\varepsilon = 1/16$, $\alpha = 1/128$. The lower bound is proved by reducing median-finding to orthogonal partitioning via the curve $(t, e^t)$, which any orthogonal cut must intersect at the median.

## Result
Optimal $\Theta(n)$ algorithm for the 2D pancake cut, improving the previous $O(n \log n)$ of Roy–Steiger [18]. Higher-dimensional Theorems A and B (from Musin's forthcoming work [11]) admit polynomial-time greedy algorithms by enumerating point-defined hyperplanes: $O(n^{d(d+1)/2})$ for $d$ mutually orthogonal hyperplanes equipartitioning a single set, and $O(n^{2d})$ for orthogonal pairs bisecting $m$ sets in dimension $\delta(m) = m + 2\lfloor \log_2 m \rfloor$. The paper conjectures an improvement to $O(n^{d(d+1)/2 - 2})$ by analogy with the ham-sandwich speedup.

## Why it matters here
General background; no direct arena tie. Mass-partition / equipartition theorems are adjacent to discrete-geometry problems on the arena (packing, kissing, autocorrelation symmetry arguments) but the algorithmic content here is computational geometry rather than optimization — relevant only if a problem reduces to finding a balanced orthogonal cut of a finite configuration.

## Open questions / connections
- Grünbaum's hyperplane equipartition problem in $\mathbb{R}^4$ remains open (Avis ruled out $d \geq 5$; Hadwiger settled $d = 3$).
- Can the $O(n^{d(d+1)/2})$ bound for Theorem A be improved to $O(n^{d(d+1)/2 - 2})$, matching the $O(n^{d-1})$ vs $O(n^{d+1})$ gap for ham-sandwich cuts?
- Extends Lo–Matoušek–Steiger [7] prune-and-search machinery to the orthogonality-constrained setting via the dual involution $a \mapsto -1/a$.

## Key terms
pancake theorem, ham-sandwich theorem, mass partition, orthogonal hyperplanes, equipartition, Borsuk-Ulam, line arrangement, median level, dual transformation, prune-and-search, Lo-Matousek-Steiger, Grünbaum problem, Musin, Stiefel manifold, computational geometry
