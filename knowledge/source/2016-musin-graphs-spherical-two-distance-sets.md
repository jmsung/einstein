---
type: source
kind: paper
title: Graphs and spherical two-distance sets
authors: O. Musin
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1608.03392
source_local: ../raw/2016-musin-graphs-spherical-two-distance-sets.pdf
topic: general-knowledge
cites:
---

# Graphs and spherical two-distance sets

**Authors:** O. Musin  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1608.03392

## One-line
Gives exact formulas for the minimum dimension in which a graph $G$ can be embedded as a Euclidean / spherical / unit-circumradius ($1/\sqrt{2}$) two-distance set, expressed via multiplicities of a Cayley–Menger polynomial.

## Key claim
For a graph $G$ on $n$ vertices, $\dim_{E_2}(G) = n - \mu(G) - 1$ where $\mu(G)$ is the multiplicity of the smallest root $\tau_1 > 1$ of the Cayley–Menger polynomial $C_G(t)$; the spherical number $\dim_{S_2}(G)$ equals $\dim_{E_2}(G)$ when the circumradius $R(G) < \infty$ and equals $n-1$ otherwise; a $J$-spherical (radius $1/\sqrt{2}$, min distance $1$) representation exists uniquely for every $G \neq K_n$.

## Method
Reduce embedding existence to vanishing of the Cayley–Menger determinant $C_G(t)$ in $t = b^2$ (second distance squared); the embedding dimension is read off from root multiplicity (Einhorn–Schoenberg). Sphericity is detected via the ratio $F_G(t) = -\tfrac12 M_G(t)/C_G(t)$ giving squared circumradius. Existence/uniqueness of the $J$-spherical case ($R = 1/\sqrt{2}$) uses Rankin's spherical-cap bound plus Kirszbraun's Lipschitz-extension theorem to show $\Phi_G(x)$ (min enclosing ball radius) is monotone increasing on $[\sqrt{2}, 2\tau_1]$.

## Result
Bounds: $\dim_{E_2}(G) \geq (\sqrt{8n+1}-3)/2$ from $n \leq (d+1)(d+2)/2$; for spherical sets $n \leq d(d+3)/2$. $R(G) \geq 1/\sqrt{2}$ (Rankin). For the join $G = G_1 + \cdots + G_m$ with sorted $\beta^*(G_i)$, explicit closed-form formulas for $\dim_{J_2}, \dim_{S_2}, \dim_{E_2}$ in terms of summed $\dim_{J_2}(G_i)$ and remaining vertex counts. Corollary: complete multipartite $K_{n_1,\ldots,n_m}$ with $n_1 = \cdots = n_k > n_{k+1} \geq \cdots$ has $\dim_{S_2} = n-k$, $\dim_{E_2} = \min(n-k, n-2)$. Cross-polytope $K_{2,\ldots,2}$ achieves $\dim_{J_2}(G) = n/2$.

## Why it matters here
General background; no direct arena tie. Tangentially relevant to problems involving few-distance point configurations on spheres (kissing-number style, equiangular lines) since the Cayley–Menger / circumradius machinery and Rankin's $\sqrt{2}$ bound are reusable tools; the $d(d+3)/2$ two-distance bound (Delsarte–Goethals–Seidel) is the canonical spherical-design ceiling.

## Open questions / connections
- Range and maximum of $R(G)$ — can $R(G) > 1$? Countable subset of $[1/\sqrt{2}, \infty)$.
- Monotonicity/convexity conjecture: $F_G(t)$ increasing and convex on $(1, \tau_1(G))$.
- Generalization of Einhorn–Schoenberg to $s$-distance edge-colored $K_n$ via multivariate Cayley–Menger polynomials $C_L(t_2,\ldots,t_s)$, $F_L = -\tfrac12 M_L/C_L$.
- Connections: Kuperberg's theorem on $\geq d+2$ points at distance $\geq \sqrt{2}$ in $S^{d-1}$ (join-decomposability); Lisoněk's tight $d=8$ two-distance set; Barg–Yu / Glazyrin–Yu bounds extending $n \leq d(d+1)/2$.

## Key terms
two-distance set, spherical two-distance set, Cayley–Menger determinant, Einhorn–Schoenberg, circumradius, Rankin theorem, Kirszbraun theorem, Kuperberg join theorem, complete multipartite graph, graph join, equiangular lines, Delsarte–Goethals–Seidel bound, kissing number
