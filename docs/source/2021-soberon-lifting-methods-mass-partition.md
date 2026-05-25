---
type: source
kind: paper
title: Lifting Methods in Mass Partition Problems
authors: P. Sober'on, Yuki Takahashi
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2109.03749
source_local: ../raw/2021-soberon-lifting-methods-mass-partition.pdf
topic: general-knowledge
cites:
---

# Lifting Methods in Mass Partition Problems

**Authors:** P. Sober'on, Yuki Takahashi  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2109.03749

## One-line
Extends ham-sandwich-style mass partition theorems by lifting $\mathbb{R}^d$ to polyhedral surfaces in $\mathbb{R}^{d+1}$ instead of smooth Veronese maps, yielding equipartitions by parallel hyperplanes, concentric spheres, and bounded-complexity polyhedra.

## Key claim
Any $d+1$ absolutely continuous measures in $\mathbb{R}^d$ can be simultaneously halved by the region between two parallel hyperplanes (Theorem 1.2); equivalently, any $d+2$ measures can be halved by the region between two concentric spheres ("bagel ham sandwich", Corollary 1.3).

## Method
Lift $\mathbb{R}^d$ to a piecewise-linear surface $S(H) \subset \mathbb{R}^{d+1}$ (graph of $x \mapsto \mathrm{dist}(x,H)$) rather than to a paraboloid/Veronese image, then apply the ham sandwich theorem for general measures. The parallel-hyperplane result requires a new Borsuk–Ulam-type theorem (Theorem 3.4) for $(\mathbb{Z}_2)^{k+1}$-equivariant maps $S^d \times V_k(\mathbb{R}^d) \to \mathbb{R}^d \times \mathbb{R}^{d-1} \times \cdots \times \mathbb{R}^{d-k}$, proved via Fadell–Husseini cohomological index. A smoothing $S(H)_\varepsilon$ thickens the lift so the induced measures vanish on hyperplanes.

## Result
(i) $d+1$ measures halved by parallel hyperplanes; (ii) $d+2$ measures halved by concentric spheres; (iii) for well-separated supports, parallel hyperplanes can cut arbitrary fractions $\alpha_i \in (0,1)$ of each of $d+1$ measures (Theorem 1.5); (iv) for $n$ nicely-separated measures in $\mathbb{R}^d$, a convex polyhedron with $\le n$ facets (or $n$ vertices) achieves arbitrary fractions (Theorems 5.2, 5.3); (v) Akopyan–Karasev's $1/n$-fraction convex set can be written as the intersection of $\sum_j k_j(p_j-1)p_j$ half-spaces where $n=\prod p_j^{k_j}$ (Theorem 1.6).

## Why it matters here
General background; no direct arena tie — none of the 23 arena problems are mass-partition problems. The polyhedral-lift trick (replacing smooth Veronese maps with PL surfaces + ham sandwich for general measures) is a transferable technique that could inform parameterization choices in extremal discrete-geometry settings, but the connection is indirect.

## Open questions / connections
- Q6.2: Can the $1/n$-equipartition convex set use only $O(\log n)$ half-spaces (vs $\sum k_j(p_j-1)p_j$)?
- Q6.3: Does a regular torus in $\mathbb{R}^3$ halve any 5 measures (3D bagel)?
- Q6.4: Existence of a square in $\mathbb{R}^2$ halving any 3 measures (mixes with Kano's staircase-path conjecture).
- Extends Bárány–Hubard–Jerónimo (well-separated wedge cuts), Akopyan–Karasev (fractional-equipartition convex sets), Stone–Tukey (polynomial ham sandwich).

## Key terms
ham sandwich theorem, mass partition, equipartition, parallel hyperplanes, concentric spheres, polynomial ham sandwich, Borsuk-Ulam, Stiefel manifold, Fadell-Husseini index, well-separated measures, polyhedral lifting, Veronese map, wedge partition, Akopyan-Karasev, Soberón, Stone-Tukey, Bárány
