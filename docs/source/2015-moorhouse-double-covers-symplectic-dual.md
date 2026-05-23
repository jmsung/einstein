---
type: source
kind: paper
title: Double covers of symplectic dual polar graphs
authors: G. Eric Moorhouse, Jason S. Williford
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1504.01067
source_local: ../raw/2015-moorhouse-double-covers-symplectic-dual.pdf
topic: general-knowledge
cites:
---

# Double covers of symplectic dual polar graphs

**Authors:** G. Eric Moorhouse, Jason S. Williford  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1504.01067

## One-line
Constructs a new infinite family of imprimitive $Q$-polynomial association schemes as double covers of symplectic dual polar graphs $\Gamma(2n,q)$ when $q \equiv 1 \pmod 4$.

## Key claim
For odd prime power $q \equiv 1 \pmod 4$ and $n \geq 1$, the Maslov-index sign function $\sigma$ on the set $\mathcal{V}$ of maximal totally isotropic subspaces of a $2n$-dimensional symplectic space defines a $PSp(2n,q)$-invariant nontrivial two-graph $\Delta(2n,q)$, whose associated double cover $\widetilde{\Gamma} \to \Gamma$ carries a $Q$-polynomial $(2n+1)$-class association scheme $S_{n,q}$ on $2|\mathcal{V}|$ vertices with two $Q$-polynomial orderings.

## Method
Defines the Maslov index $\sigma(X,Y) = \chi(\delta_X(\mathbf{x})\delta_Y(\mathbf{y})\det[B(x_i,y_j)])$ using the quadratic character $\chi$ and determinant functions, proves it determines a two-graph via the 4-set coherence relation, and lifts to a double cover. The $Q$-polynomial property is proven by exhibiting explicit polynomials $s_\ell(x)$ realizing a $Q$-sequence and computing the $P$-matrix via generating-function identities involving $E_m(t) = \prod_{i=0}^{m-1}(1+q^i t)$. Computations verified using MAGMA.

## Result
The scheme $S_{n,q}$ has $2n+1$ classes, is $Q$-bipartite with two $Q$-polynomial orderings (related by the Galois action $r \mapsto -r$ where $r=\sqrt{q}$), and for non-square $q$ has irrational splitting field $\mathbb{Q}(\sqrt{q})$ — the only known unbounded-class $Q$-polynomial family with irrational splitting field. Explicit $P$- and $Q$-matrices given for the $n=2$ case; existence of a hypothetical primitive subscheme verified feasible up to $n=20$.

## Why it matters here
General background; no direct arena tie. The Delsarte LP framework (cited via association schemes) underlies the Cohn–Elkies sphere-packing bound used in arena problems, but this specific construction is highly specialized algebraic combinatorics with no obvious lever on the 23 Einstein Arena problems.

## Open questions / connections
- Is $S_{n,q}$ the extended $Q$-bipartite double of a primitive $Q$-polynomial scheme? Parameters satisfy Krein conditions and integrality up to $n=20$.
- Existence of the smallest hypothetical primitive subscheme ($n=2$ case shown explicitly) is unknown.
- Extends Penttila–Williford (2011) and Martin–Muzychuk–Williford (2007) families of imprimitive cometric schemes; complements the bipartite-double Hermitian construction (the only other known unbounded non-$P$-polynomial $Q$-polynomial family).

## Key terms
association scheme, Q-polynomial, two-graph, double cover, symplectic group, dual polar graph, Maslov index, Delsarte LP bound, Gaussian coefficient, Krein parameter, splitting field, imprimitive scheme
