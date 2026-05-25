---
type: source
kind: paper
title: Khovanskii's theorem and effective results on sumset structure.
authors: M. Curran, Leo Goldmakher
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2009.02140
source_local: ../raw/2020-curran-khovanskii-theorem-effective-results.pdf
topic: general-knowledge
cites:
---

# Khovanskii's theorem and effective results on sumset structure.

**Authors:** M. Curran, Leo Goldmakher  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2009.02140

## One-line
Effective version of Khovanskii's theorem: for finite $A \subset \mathbb{Z}^d$ with simplicial convex hull, gives explicit bounds on when $|hA|$ becomes polynomial in $h$ and a Brion-type structural formula for $hA$.

## Key claim
For $A \subset \mathbb{Z}^d$ with $A-A$ generating $\mathbb{Z}^d$ and $\Delta_A$ a $d$-simplex, $|hA| = p(h)$ for all $h \geq \mathrm{vol}(\Delta_A) \cdot (d+1)! - 1 - 3d$ (Thm 1.4), and $hA = \bigcup_{i=1}^{d+1}(h\mathbf{v}_i + T_i(A))$ for $h \geq \mathrm{vol}(\Delta_A) \cdot (d+1)! - 2 - 2d$ (Thm 1.3). For $|A|=d+2$, an exact closed-form $|hA| = \binom{h+d+1}{d+1} - \binom{h-\mathrm{vol}(\Delta_A)\cdot d!+d+1}{d+1}$ holds for all $h$ (Thm 1.2).

## Method
Lift each $a \in A$ to $\bar a = (a,1) \in \mathbb{Z}^{d+1}$ and study the cone $C_A = \mathrm{span}_\mathbb{N}\{\bar a_i\}$; the height-$h$ slice of $C_A$ is a copy of $hA$, so the generating function $C_A(t) = \sum_h |hA| t^h$ encodes everything at once. Partition $C_A$ by residue classes modulo the sublattice $\Lambda$ spanned by lifts of vertices of $\Delta_A$; each class $S_\pi$ is a finite union of translated cones whose generating series is a rational function $P(t)/(1-t)^{d+1}$. The effective bounds come from explicitly controlling the heights of minimal/virtual generators (Lemmas 3.1, 3.2) — the height of any minimal element of $S_\pi$ is $\leq \mathrm{vol}(\Delta_A)\cdot d! - 1$.

## Result
Three effective theorems for simplicial $\Delta_A$: (i) Khovanskii phase transition at $h \geq \mathrm{vol}(\Delta_A)(d+1)! - 1 - 3d$, (ii) local-global structure $hA = \bigcup_i (h\mathbf{v}_i + T_{\mathbf{v}_i}(A))$ for large $h$, (iii) Brion-type identity $\sigma_{hA}(x) = \sigma_0(x) + x^{hb}\sigma_b(x)$ for $A \subset \mathbb{Z}$ with $h \geq 2b-4$. The $|A|=d+2$ case yields an exact formula valid for all $h \in \mathbb{N}$, with a counterintuitive phase: small-$h$ cardinality $\binom{h+d+1}{d+1}$ is independent of the specific points in $A$.

## Why it matters here
General background; no direct arena tie — geometry-of-numbers / Ehrhart-theoretic technique for counting lattice points in iterated sumsets, potentially relevant if a future problem reframes a discrete-combinatorics or sphere-packing count as a sumset cardinality. The lifting-to-a-cone trick is a general-purpose move for turning a sequence-indexed combinatorial quantity into a rational generating function.

## Open questions / connections
- Conjectured tighter phase transition $h \geq \mathrm{vol}(\Delta_A) \cdot d! - |A| + d + 1$ (no simplex hypothesis), specializing to Granville–Walker's $h \geq b - |A| + 2$ in dim 1.
- Extending the Brion-type formula (Thm 5.1) from $\mathbb{Z}$ to $\mathbb{Z}^d$ — blocked by extraneous sets becoming finite unions of hypersurfaces instead of points.
- The numerator $x^4 y^8 t^{11}$ in the $A=\{(0,0),(-1,1),(1,2),(4,0)\}$ example points to non-lattice "phantom" interior weights whose interpretation is unknown; understanding this may unify the simplicial / non-simplicial proofs.

## Key terms
Khovanskii's theorem, sumset, iterated sumset $hA$, Ehrhart theory, lattice points in polytopes, Brion's formula, tangent cone, simplicial cone, generating function, Hilbert polynomial, Frobenius coin problem, convex hull simplex, virtual generator
