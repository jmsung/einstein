---
type: source
kind: paper
title: Towards a proof of the 24-cell conjecture
authors: O. Musin
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1712.04099
source_local: ../raw/2017-musin-towards-proof-24-cell-conjecture.pdf
topic: general-knowledge
cites:
---

# Towards a proof of the 24-cell conjecture

**Authors:** O. Musin  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1712.04099

## One-line
Survey/programme paper outlining approaches — irreducible contact graphs, LP/SDP bounds, multivariate positive-definite functions — toward proving the 24-cell conjecture and the uniqueness of the maximal 24-point kissing arrangement in $\mathbb{R}^4$.

## Key claim
The 24-cell conjecture (minimal Voronoi cell volume in any unit-sphere packing of $\mathbb{R}^4$ is $\geq$ volume of the regular 24-cell circumscribed to the unit sphere) would also prove $D_4$ is the densest 4-D packing ($\Delta_4 = \pi^2/16$, center density $\delta_4 = 1/8$); the paper proposes a reduction strategy combining Fejes Tóth-style local-density reduction, SDP-bound tightening toward $k(4)=24$, and isoperimetric inequalities on polytopes.

## Method
Three interlocking tools: (i) **irreducible contact graphs** on $S^3$ (locally rigid arrangements, enumerated as in the $N=13,14$ Tammes solutions); (ii) **SDP bounds on $k(4)$** using multivariate positive-definite functions $H_k^{(n,m)}$ (Bachoc–Vallentin / Musin), already pushing the bound to $s_{16}(4) < 24.0569$; (iii) **multivariate p.d. functions in $\mathbb{R}^n$** (not just $S^{n-1}$) — $H_k^{(4,1)}(t,x,y,u,v)$ with $x=|p_i|^2, y=|p_j|^2$ — to handle non-touching neighbors. Dimension reduction via fixed-point/combinatorial-topology methods (à la Bondarenko–Radchenko–Viazovska for $t$-designs).

## Result
Current best Cohn–Elkies/de Laat–de Oliveira Filho–Vallentin upper bound: $\delta_4 < 0.130587$ (vs conjectured $1/8 = 0.125$). SDP-on-$k(4)$ ladder: $s_7(4) < 24.5797$ → $s_{11}(4) < 24.1055$ → $s_{16}(4) < 24.0569$, monotonically approaching but not yet hitting 24. Sub-conjecture stated: spherical kissing number $k_S(4) = 22$. Programme — not a proof — for full resolution.

## Why it matters here
Background for any 4-D sphere-packing / kissing / Voronoi-cell problem on Einstein Arena: documents the canonical Fejes Tóth → Hales → Musin reduction chain (local-density + irreducible contact graphs + SDP) and the still-open gap between best LP/SDP upper bounds and the conjectured optima. Anchors the irreducible-contact-graph technique used in Tammes $N=13,14$ for transfer to $S^3$.

## Open questions / connections
- Does the SDP-bound sequence $s_d(4)$ actually converge to 24 as $d \to \infty$, and if so at what degree does equality (and hence a uniqueness proof à la dim 8/24) become attainable?
- Can the multivariate p.d. functions $H_k^{(4,1)}$ produce a bound $N \leq 24$ for non-touching neighbor configurations near the central sphere, closing the $N \geq 25$ case for the 24-cell conjecture?
- Enumeration of irreducible contact graphs on $S^3$ — analog of the $S^2$ work for Tammes — remains the combinatorial bottleneck.
- Spherical 2-distance sets in $\mathbb{R}^4$ for $n=7,8,9$ (Einhorn–Schoenberg / Lisoněk gap).

## Key terms
24-cell conjecture, $D_4$ lattice, kissing number $k(4)=24$, sphere packing $\mathbb{R}^4$, Voronoi cell, Cohn-Elkies LP bound, Bachoc-Vallentin SDP, multivariate positive-definite functions, irreducible contact graph, Tammes problem, Fejes Tóth method, Hales-Ferguson Kepler, Schoenberg-Bochner, dodecahedral conjecture
