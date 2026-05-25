---
type: source
kind: paper
title: Geometric vs Algebraic Nullity for Hyperpaths
authors: Joshua Cooper, Grant Fickes
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2107.01500v4
source_local: ../raw/2021-cooper-geometric-algebraic-nullity-hyperpaths.pdf
topic: general-knowledge
cites: 
---

# Geometric vs Algebraic Nullity for Hyperpaths

**Authors:** Joshua Cooper, Grant Fickes  ·  **Year:** 2021  ·  **Source:** http://arxiv.org/abs/2107.01500v4

## One-line
Verifies the Hu–Ye conjecture (geometric ≤ algebraic multiplicity for tensor eigenvalues) for the zero eigenvalue of 3-uniform loose hyperpaths $P_n^3$ by explicitly decomposing the nullvariety and computing the nullity.

## Key claim
For the loose 3-hyperpath $P_n^3$, the geometric multiplicity $gm(0) := \sum_j \dim(V_0^j)(k-1)^{\dim(V_0^j)-1}$ is bounded above by the algebraic multiplicity $am(0) = D_{n,3}$, where $D_{n,k} = \big(u^n([nk-n+1]u^2+[nk-2n+2]uv-[k+n-1]v^2)+k(-v)^{n+2}\big)/(u+v)^2$ with $u=(k-1)^{k-1}$, $v=k^{k-2}$.

## Method
(1) Decompose the nullvariety $V_0 \subset \mathbb{C}^{2n+1}$ via the Lagrangian polynomials of vertex links; degree-1 vertex equations are monomials $x_i x_j$, so $V_0$ splits into a union indexed by "Fibonacci subsets" of odd indices $A'_n=\{3,5,\dots,2n-1\}$. (2) Prove each component is an irreducible affine variety (prime ideal via UFD/composition argument, Prop 2.3 of Milne), classify inclusion-maximal ones by a parity condition on maximal runs of consecutive odd indices. (3) Encode component-dimensions as a bivariate rational generating function $h(y,z)$; extract $gm(0)$ via $\partial_y h|_{y=2}$. (4) Use Bao–Fan–Wang–Zhu's recurrence for $\phi_{P_n^k}(\lambda)$ via the rational iteration $f_i(x)=f_{i-1}(f(x))$, $f(x)=\lambda^k/(\lambda^k-x)$, to derive the closed form for $D_{n,k}$. (5) Compare asymptotics: $\eta_n \le \frac{F_n}{(2\lfloor n/2\rfloor+1)} \cdot \dots$ vs $D_{n,3} \ge \tfrac{4^n}{7}(5n+3)$ for $n\ge 12$; brute-force table for $n<12$.

## Result
- Nullvariety irreducible components for $P_n^3$ are in bijection with admissible sets built from "Fibonacci subsets" of $A'_n$; max component dimension is $2\lfloor n/2\rfloor + 1$.
- Closed form $D_{n,3}$: matches $3, 35, 151, 891, 3983, 19795, \dots$ for $n=1,\dots$
- $gm(0)$ sequence: $3, 13, 72, 140, 812, 1648, 7280, 18064, 60928, 176576, 509376, \dots$
- Asymptotically, $D_{n,k}/n(k-1)^{n(k-1)+1} \to 1$, so the fraction of zero eigenvalues approaches $1/(k-1)$.
- Hu–Ye conjecture $gm(0) \le am(0)$ holds for all $n \ge 1$ on $P_n^3$.

## Why it matters here
General background; no direct arena tie. Spectral hypergraph theory / tensor eigenvalues sit adjacent to extremal-hypergraph and discrete-geometry problem families on the arena, but no current Einstein problem invokes nullvariety decomposition or tensor eigenvalue multiplicity directly. Useful as a reference for the *multilinear* generalization of "geometric ≤ algebraic multiplicity" should a kissing/packing problem ever require tensor-spectral methods.

## Open questions / connections
- Extends Bao–Fan–Wang–Zhu's starlike-hypergraph characteristic polynomial recurrence [1] and the Cooper–Dutle hypergraph spectra framework [3].
- Does the same decomposition + counting strategy verify Hu–Ye for general linear hypertrees (not just paths)?
- Vertices where nullvectors vanish form *transversals* of the edge set on hypertrees — combinatorial characterization in general remains open.
- Non-zero eigenvarieties of $P_n^k$: structure and algebraic multiplicities entirely unstudied.
- Is the Hu–Ye lower-bound functional $\sum \dim(V_\lambda^j)(k-1)^{\dim-1}$ tight, or does a larger valid functional exist?

## Key terms
hypergraph spectra, tensor eigenvalue, adjacency hypermatrix, nullvariety, eigenvariety, algebraic multiplicity, geometric multiplicity, Hu–Ye conjecture, loose hyperpath, linear hyperpath, characteristic polynomial, Lagrangian polynomial, irreducible component, Fibonacci subset, Cooper, Fickes, Bao–Fan–Wang–Zhu, symmetric hyperdeterminant
