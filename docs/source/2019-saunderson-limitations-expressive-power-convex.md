---
type: source
kind: paper
title: Limitations on the Expressive Power of Convex Cones without Long Chains of Faces
authors: J. Saunderson
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1902.06401
source_local: ../raw/2019-saunderson-limitations-expressive-power-convex.pdf
topic: general-knowledge
cites:
---

# Limitations on the Expressive Power of Convex Cones without Long Chains of Faces

**Authors:** J. Saunderson  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1902.06401

## One-line
Proves that convex cones with a $k$-neighborliness property cannot be represented as projected slices of any finite Cartesian product of cones whose face lattices have only short chains.

## Key claim
**Theorem 1.4:** If a proper convex cone $C$ is $k$-neighborly with respect to arbitrarily large finite subsets of normalized extreme rays, then $C$ has no $K_1 \times \cdots \times K_m$-lift whenever each factor satisfies $\ell(K_i) \le k+1$ (where $\ell(\cdot)$ is the max length of a chain of nonempty faces). This subsumes Averkov's earlier $(\mathcal{S}_+^k)^m$ bound and extends it to smooth cones, exponential cones, low-degree hyperbolicity cones, and cones over univariate-convex-function epigraphs.

## Method
Generalizes Averkov's argument by replacing PSD-specific algebra (rank, column space) with face-lattice primitives (minimal face $F_C(x)$, chain length $\ell(K)$). Combines (i) the Gouveia–Parrilo–Thomas factorization theorem (lifts $\Leftrightarrow$ nonnegative factorizations of the slack operator) with (ii) Ramsey's theorem for $k$-uniform hypergraphs to force a contradiction: a $k$-neighborly system with too many extreme rays must produce a monochromatic $(k+1)$-subset whose induced faces collapse impossibly. Key lemma (4.2): if $\sum x_i \in \operatorname{relint}(K)$, some subset of size $\le \ell(K)-1$ already lies in the relative interior.

## Result
Concrete corollaries: $\mathcal{S}_+^3$ has no lift via a finite product of smooth cones (e.g., second-order cones); $\mathcal{S}_+^4$ has no lift via any product of $3$-dimensional cones (including exponential cones); $\mathcal{S}_+^{k+1}$ has no $\Lambda_+(p,e)$-lift when all irreducible factors of the hyperbolic polynomial $p$ have degree $\le k$. The quantitative bound (cardinality $|V| < R_k(k+1; (k+1)^m)$) is finite but extremely weak due to Ramsey-number growth.

## Why it matters here
General background; no direct arena tie. Touches the agent's compute-router/SDP toolbox indirectly: it tells us when a "simpler" lifted reformulation is provably impossible, which is relevant if/when we consider SOCP or exponential-cone relaxations for problems currently posed as SDPs (e.g., LP-bound work on kissing/sphere packing). Worth noting alongside `findings/sdp-relaxation-uselessness`: this paper gives the structural reason some clean SDP cones resist reduction to cheaper conic forms.

## Open questions / connections
- Can the Ramsey-based lower bound on the number of factors $m$ be tightened beyond Ramsey-growth rates? The $k=1$ case reduces to LP extension complexity.
- Extends Fawzi (2018, $\mathcal{S}_+^3$ has no SOC lift) and Averkov (2019, semidefinite extension degree). Leaves open: quantitative lower bounds on hyperbolicity-cone lift size (only quantifier-elimination–style bounds exist).
- Connects to derivative relaxations / Renegar derivatives of $\mathcal{S}_+^k$ — these inherit neighborliness from PSD faces and are thus also irrepresentable via short-chain products.

## Key terms
convex cone lift, $k$-neighborliness, chain of faces, semidefinite extension degree, hyperbolicity cone, Renegar derivatives, second-order cone, exponential cone, Gouveia–Parrilo–Thomas factorization, Ramsey theorem hypergraph, Averkov, Fawzi, sums of squares, nonnegative polynomials, smooth cone
