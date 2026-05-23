---
type: source
kind: paper
title: Spectra of combinatorial Laplace operators on simplicial complexes
authors: Danijela Horak, J. Jost
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1105.2712
source_local: ../raw/2011-horak-spectra-combinatorial-laplace-operators.pdf
topic: general-knowledge
cites:
---

# Spectra of combinatorial Laplace operators on simplicial complexes

**Authors:** Danijela Horak, J. Jost  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1105.2712

## One-line
Builds a unified weighted framework for combinatorial Laplace operators on simplicial complexes and defines a normalized higher-order Laplacian $\Delta^{up}_i$ whose spectrum lies in $[0, i+2]$.

## Key claim
With weights chosen so $w(F) = \deg F$ for all non-facet faces (and facet weights $=1$), the resulting normalized combinatorial Laplacian $\Delta^{up}_i$ has spectrum bounded above by $i+2$, generalizing the classical bound $[0,2]$ for the normalized graph Laplacian and giving the boundary eigenvalue $i+2$ a concrete combinatorial meaning (orientability/chromatic obstructions).

## Method
Frames all Laplacians ($L^{up}_i = \delta_i^* \delta_i$, $L^{down}_i = \delta_{i-1}\delta_{i-1}^*$, $L_i = L^{up}_i + L^{down}_i$) as adjoint constructions whose form depends entirely on the choice of weight function $w$ on faces, equivalently the scalar product on cochain groups. Bounds are derived via Cauchy–Schwarz on $(\delta_i f, \delta_i f) \le (i+2)\sum_F f([F])^2 \deg F$, plus min-max / Courant–Fischer. Spectral effects of wedge, join, and motif-duplication operations are obtained from tensor-product cochain decompositions and Cauchy interlacing.

## Result
(1) Zero-eigenvalue multiplicity of $L_i$ equals $\dim \tilde H_i$ (discrete Hodge / Eckmann). (2) $\text{spec}(\Delta^{up}_i) \subseteq [0, i+2]$; the upper-bound is attained iff $K$ contains no $(i+1)$-orientable odd circuit and no $(i+1)$-non-orientable even circuit. (3) Chromatic number $i+2$ of the 1-skeleton $\Rightarrow$ $i+2 \in \text{spec}(\Delta^{up}_i)$. (4) Join formula: $\text{spec}(\Delta^{down}_{d_1+d_2+1}(K_1 * K_2)) = \{\lambda_i + \mu_j\}$. (5) Duplicating a $k$-motif $\Sigma$ ($m$ times) introduces $(m-1)$ copies of each eigenvalue of $\Delta^{up}_i(\text{Cl St }\Sigma)|_{\text{St }\Sigma}$; vertex duplication specifically produces eigenvalue $i+1$.

## Why it matters here
General background; no direct arena tie — none of the 23 problems are framed as simplicial-complex spectral problems. Closest tangential value: extremal-graph / hypergraph problems could in principle exploit higher-order Laplacian spectra (chromatic-number bounds, motif counts), but the wiki currently has no such usage.

## Open questions / connections
- Can the $\Delta^{up}_i$ spectrum give Cheeger-type expansion or isoperimetric bounds useful for kissing/packing contact-graph analysis?
- Extends Banerjee–Jost normalized graph Laplacian work (motif duplication) to all dimensions — does duplication detection help diagnose symmetry in optimizer basins?
- Relation to Cohn–Elkies / LP-bound style spectral methods on simplicial / hypergraph relaxations remains unexplored.
- Author flags weighted-Čech-Laplacian as a tool for intersection-pattern data analysis (forward reference, undeveloped here).

## Key terms
combinatorial Laplacian, normalized graph Laplacian, simplicial complex, Hodge theorem, Eckmann, cochain complex, coboundary operator, chromatic number, motif duplication, join of complexes, Cauchy interlacing, hypergraph Laplacian, Horak, Jost
