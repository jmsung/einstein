---
type: source
kind: paper
title: Some notes on the equivalence of first-order rigidity in various geometries
authors: Franco V. Saliola, Walter Whiteley
year: 2007
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/0709.3354v1
source_local: ../raw/2007-saliola-some-notes-equivalence-first-order.pdf
ingested_for_concept: basin-rigidity.md
cites: 
---

# Some notes on the equivalence of first-order rigidity in various geometries

**Authors:** Franco V. Saliola, Walter Whiteley  ·  **Year:** 2007  ·  **Source:** http://arxiv.org/abs/0709.3354v1

## One-line
Shows that first-order rigidity of bar-and-joint frameworks is the same theory across Euclidean, spherical, hyperbolic, and exterior-hyperbolic geometries via an explicit matrix transformation between rigidity matrices.

## Key claim
For a framework $G(p)$ with $p \in \mathbb{R}^n$, there is a block-diagonal vertex-wise matrix $T_K(G,p)$ (with blocks $T_{p_i} = I + K(p_i^{(\ell)} p_i^{(m)})$) such that $R_{\mathbb{PH}}(G,p)\,T_{-1}(G,p) = R_E(G,p)$ and $R_{\mathbb{PS}^+}(G,p)\,T_{1}(G,p) = R_E(G,p)$. Consequently $G(p)$ is first-order rigid in $\mathbb{PS}^n_+$ iff in $\mathbb{PE}^n$, and (when no vertex is on the absolute, $p_i \cdot p_i \neq 1$) iff in $\mathbb{PH}^n \cup \mathbb{PD}^n$.

## Method
Derive first-order motion equations in each metric from the bilinear form $\langle x,y\rangle_k = \sum a_i x_i y_i$ (signature controls geometry). Embed all geometries projectively into $\mathbb{R}^n$ via central/gnomic projection, then express the rigidity matrix in each metric and exhibit an explicit per-vertex linear change of variables relating them. Row dependencies (self-stresses) are preserved exactly — only column space (kinematics) gets re-twisted at each vertex.

## Result
First-order rigidity, static rigidity, and self-stresses are metric-invariant across $E^n$, $S^n_+$, $H^n$, $D^n$ (and any signature $\langle\cdot,\cdot\rangle_k$ with $a_i \neq 0$). Consequences: (i) Cauchy-Dehn theorem (convex triangulated polytope in $E^n$, $n\geq 3$, is first-order rigid) transfers to all $X^n$; (ii) a first-order Andreev theorem follows via $D^n \leftrightarrow H^n$ point-plane polarity — simple convex polytopes in $H^n$ are stiff under dihedral-angle constraints, removing the usual $\leq \pi/2$ restriction; (iii) circle-angle CAD constraints in the plane $\equiv$ point-distance frameworks in $E^3$ via hyperbolic 3-space.

## Why it matters here
General background; no direct arena tie. Potentially relevant as auxiliary structure for discrete-geometry problems where rigidity/projective invariance argues that a configuration in one metric (e.g., spherical packing) is structurally equivalent to a Euclidean one — useful if any arena problem reduces to rigidity-matrix rank or self-stress arguments.

## Open questions / connections
- Does the equivalence extend to differentiable surfaces (infinite rigidity matrices) where static and first-order rigidity diverge?
- The graph-characterization problem (which $G$ are generically first-order rigid in $d$-space, $d\geq 3$) is identical in all metrics — so no metric-switching trick yields leverage.
- Polarity in Euclidean dimensions $d=2,3$ has distinctive interpretations (Whiteley [22,23]); spherical-polarity version of first-order Cauchy → Andreev-style theorem in elliptic geometry is sketched but not fully presented.

## Key terms
first-order rigidity, bar-and-joint framework, rigidity matrix, self-stress, projective invariance, Cauchy-Dehn theorem, Andreev theorem, hyperbolic geometry, spherical geometry, gnomic projection, polarity, tensegrity, convex polytope, dihedral angle, CAD geometric constraints
