---
type: source
kind: paper
title: The Why and How of Nonnegative Matrix Factorization
authors: Nicolas Gillis
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1401.5226
source_local: ../raw/2014-gillis-why-how-nonnegative-matrix.pdf
topic: general-knowledge
cites:
---

# The Why and How of Nonnegative Matrix Factorization

**Authors:** Nicolas Gillis  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1401.5226

## One-line
Tutorial-survey on nonnegative matrix factorization (NMF): why it produces sparse, interpretable parts-based features, and how to compute it via standard local algorithms and the polynomial-time near-separable subclass.

## Key claim
General NMF ($\min_{W,H\geq 0}\|X-WH\|_F^2$) is NP-hard, but the near-separable subclass — where $X = W[I_r, H']\Pi + N$ with $W$ full rank and $\|H'(:,j)\|_1 \leq 1$ — is solvable in polynomial time and provably robust to noise: the Successive Projection Algorithm (SPA) recovers the columns of $W$ up to $\ell_2$ error $O(\epsilon\kappa^2(W))$ provided $\epsilon \leq O(\sigma_{\min}(W)/(\sqrt{r}\kappa^2(W)))$.

## Method
Two-block coordinate descent framework alternating NNLS subproblems in $W$ and $H$, instantiated as: multiplicative updates (MU, majorization-minimization), alternating least squares (ALS, projected unconstrained LS), alternating NNLS (ANLS, exact active-set), and hierarchical ALS (HALS, exact column-wise coordinate descent in closed form). For separable NMF, SPA greedily picks the column of maximum $\ell_2$ norm, projects onto the orthogonal complement, and iterates $r$ times — equivalent to modified Gram-Schmidt with column pivoting.

## Result
Establishes (i) first-order optimality conditions $W \circ \nabla_W F = 0$, $H \circ \nabla_H F = 0$ that structurally explain NMF's sparsity, (ii) convergence guarantees for ANLS and modified MU, (iii) SPA's noise-robustness bound above (improvable to $O(\epsilon\kappa(W))$ via post-processing or SDP preconditioning), and (iv) connections of $\mathrm{rank}_+(X)$ to biclique cover (rectangle covering bound $\mathrm{bc}(G(X)) \leq \mathrm{rank}_+(X)$), extended formulations (Yannakakis: slack-matrix nonnegative rank = min facets of any extension), nondeterministic communication complexity, and nested-polytopes problems.

## Why it matters here
General background; no direct arena tie. Possibly relevant as a methodology reference for any arena problem that reduces to nonnegative low-rank decomposition or to greedy column-selection / maximum-volume submatrix subroutines; the rectangle-covering and extended-formulation bounds touch combinatorial-geometry territory adjacent to several arena problems.

## Open questions / connections
- No known near-separable NMF algorithm provably robust for all $W$ with $\alpha(W) > 0$ running in $O(n)$ operations.
- Tighter bounds on nonnegative rank via $\mathrm{rank}_+(X)$ vs slack-matrix structure (Yannakakis 1991; Fiorini et al.) — directly relevant to LP extended-formulation lower bounds.
- Choice of factorization rank $r$ (order model selection) remains heuristic — SVD decay, expert priors, or trial-and-error.

## Key terms
nonnegative matrix factorization, NMF, near-separable, Successive Projection Algorithm, SPA, nonnegative rank, multiplicative updates, alternating least squares, HALS, ANLS, NNLS, rectangle covering bound, extended formulations, Yannakakis, slack matrix, biclique cover, hyperspectral unmixing, endmember extraction, NP-hard factorization, maximum volume submatrix
