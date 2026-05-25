---
type: source
kind: paper
title: "Simplicial complexes: Spectrum, homology and random walks"
authors: Ori Parzanchevski, Ron Rosenthal
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1211.6775
source_local: ../raw/2012-parzanchevski-simplicial-complexes-spectrum-homology.pdf
topic: general-knowledge
cites:
---

# Simplicial complexes: Spectrum, homology and random walks

**Authors:** Ori Parzanchevski, Ron Rosenthal  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1211.6775

## One-line
Defines a higher-dimensional random walk on oriented $(d-1)$-cells of a simplicial complex whose asymptotic behavior detects $(d-1)$-homology and whose mixing rate is controlled by the Eckmann–Garland spectral gap.

## Key claim
For a finite $d$-complex, the normalized "expectation process" $\tilde{E}_n^{\sigma_0}(\sigma) = \left(\tfrac{d}{p(d-1)+1}\right)^n [p_n^{\sigma_0}(\sigma) - p_n^{\sigma_0}(\bar\sigma)]$ converges to an exact form iff $H_{d-1}(X)=0$, with rate $O\!\left(\left(1-\tfrac{1-p}{p(d-1)+1}\lambda(X)\right)^n\right)$; the Alon–Boppana theorem fails in higher dimension (counterexample: balls in the 2-regular triangle tree $T_2^2$ have $\lim_r \lambda(B_r) = 3/2 - \sqrt{2}$ while $\lambda(T_2^2)=0$), but holds under three sufficient conditions (nonzero gap of $X$, non-isolated $0$ in spectrum, or $(d-1)$-skeleton expansion).

## Method
Combinatorial Hodge theory on the simplicial cochain complex with weighted inner products ($w(\sigma)=1/\deg\sigma$ for $\sigma\in X_{d-1}$), giving upper/lower Laplacians $\Delta^+=\partial_d\delta_d$, $\Delta^-=\delta_{d-1}\partial_{d-1}$. The Markov operator on $(d-1)$-forms is the transpose of the transition operator $A$; spectral measures $\mu_\sigma$ on $\mathrm{Spec}\,A$ are tracked via moment convergence under local convergence of pointed complexes. Explicit spectral analysis of balls in arboreal complexes via symmetry-group isotypic decomposition (representations of the Klein four-group acting on $B_r(T_2^2)$).

## Result
Spectrum of $\Delta^+$ lies in $[0,d+1]$; the eigenvalue $d+1$ appears iff $X$ is *disorientable* (a higher-dim bipartiteness). For inifinite $X$ with all $(d-2)$-cells of infinite degree, $\sup_\sigma \limsup_n \sqrt[n]{|\tilde E_n^\sigma(\sigma)|} = 1 - \tfrac{1-p}{p(d-1)+1}\lambda(X)$ (Kesten-type identity). Arboreal $k$-regular $d$-complex $T_k^d$ spectrum is computed in closed form; for low regularity ($k \le d+1$) an *isolated eigenvalue* appears — a phenomenon absent from regular trees. Higher-dim notions of amenability ($\lambda=0$), transience ($\sum_n \tilde E_n^\sigma(\sigma)<\infty$), and disorientability are introduced with partial implications mapped.

## Why it matters here
General background; no direct arena tie. Relevant tangentially to any extremal-graph or combinatorial-expansion problem where spectral-gap / expander framing applies (e.g., Cheeger-type bounds, higher-order Laplacians on hypergraph-like structures); supplies vocabulary if council dispatch ever invokes high-dimensional expansion or coboundary/cohomology techniques.

## Open questions / connections
- Is $\limsup_n \sqrt[n]{|E_n^\sigma(\sigma)|}$ independent of starting cell $\sigma$ for $(d-1)$-connected complexes (graph case: yes)?
- Does $\lambda$ monotonicity under covering maps $X\to Y$ extend from graphs to $d$-complexes?
- Are properties (T) and (T') (sum-finiteness vs. $\partial_d f = \tilde\sigma$ solvability in $L^2$) equivalent — the higher-dim analogue of Lyons' transience criterion?
- Extends Eckmann (1944), Garland (1973), Kesten (1959); related to Ramanujan complexes (Lubotzky–Samuels–Vishne) and coboundary expansion (Linial–Meshulam, Gromov).

## Key terms
simplicial complex, higher-dimensional Laplacian, Eckmann-Garland, spectral gap, Alon-Boppana, Kesten, random walk on cells, $(d-1)$-homology, coboundary, disorientability, arboreal complex, expander, Cheeger inequality, Hodge decomposition, amenability, transience
