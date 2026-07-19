---
type: source
kind: paper
title: Left and right convergence of graphs with bounded degree
authors: Christian Borgs, Jennifer Chayes, Jeff Kahn, László Lovász
year: 2010
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1002.0115v1
source_local: ../raw/2010-borgs-left-right-convergence-graphs.pdf
topic: general-knowledge
cites: 
---

# Left and right convergence of graphs with bounded degree

**Authors:** Christian Borgs, Jennifer Chayes, Jeff Kahn, László Lovász  ·  **Year:** 2010  ·  **Source:** http://arxiv.org/abs/1002.0115v1

## One-line
Establishes that for bounded-degree graph sequences, left-convergence (homomorphism counts *from* fixed graphs) is equivalent to right-convergence (log-partition functions *into* sufficiently dense weighted graphs).

## Key claim
For a left-convergent sequence $(G_n)$ of graphs with max degree $\le D$ and any weighted graph $H$ with edge weights $\beta_{ij} \in [0,1]$ satisfying $c(H) = \max_i \sum_k \tilde\alpha_k(1-\beta_{ik}) < 1/(2D)$, the limit $\lim_{n\to\infty} \ln t(G_n,H)/|G_n|$ exists; conversely, if $\ln \mathrm{hom}(G_n,H)/|G_n|$ converges for every sufficiently dense $H$, then $(G_n)$ is left-convergent.

## Method
Two independent proofs of the forward direction: (i) Dobrushin Uniqueness coupling — show $\Psi_K(v) = E[\prod \alpha_i \beta_{i,\phi(w)}]$ depends only on the $r$-ball $B_K(v,r)$ up to error $O(D\kappa^r)$ with $\kappa = 2Dc(H)$; (ii) Mayer/cluster expansion of $\ln t(G,H)$ as a sum over connected induced subgraphs, with tail control via the chromatic-invariant bound $|cr(H)| \le \mathrm{tree}(H)$ and Dobrushin's lemma giving condition $c(H) < 1/(8D)$. Converse uses linear independence of $\mathrm{hom}(F_i,F_j)$ matrices ($M_{\mathrm{hom}} = M_{\mathrm{surj}} D_{\mathrm{aut}}^{-1} M_{\mathrm{inj}}$, triangular factors) to invert the expansion.

## Result
Theorem 3.1 gives the implication left → right under $c(H) < 1/(2D)$; Theorem 4.3 gives right → left when $\ln \mathrm{hom}(G_n,H)/|G_n|$ converges for every simple looped $H$ with min degree $\ge (1-\delta)|H|$. Special cases: hard-core model converges for $\lambda \le (D-1)^{D-1}/(D-2)^D \approx e/D$ (using Weitz); $q$-colorings converge for $q > 2D$ (Dobrushin) or $q \ge D+1$ on large-girth $D$-regular graphs, yielding the explicit limit $\ln q + (D/2)\ln(1 - 1/q)$. Appendix proves convergence of $\ln \mathrm{hom}/nm$ for grid, cylindrical, and toroidal grid sequences via a 2D Fekete lemma.

## Why it matters here
General background; no direct arena tie. The cluster-expansion / Dobrushin-uniqueness toolkit is methodologically relevant to extremal-graph problems where partition-function asymptotics on bounded-degree structures are needed, but the paper concerns dense-target $H$ regimes rather than the sparse-extremal regimes typical of Einstein Arena combinatorics problems.

## Open questions / connections
- Quantitative bounds making the $\mathrm{hom}(F,G)/|G| \leftrightarrow \ln t(G,H)/|G|$ relationship explicit.
- Extending limit objects (Benjamini–Schramm distributions, graphings, measure-preserving graphs) to support $\ln t(G,H)/|G|$ as a functional on the limit.
- Low-temperature regime ($T < 2D$ analogue): is convergence of partition functions below the Dobrushin threshold a "from the left" property?
- Defining an averaged cut-distance metric for bounded-degree graphs — pointwise $|e_1(S,T) - e_2(S,T)| \le \varepsilon n$ fails on random regular graphs.

## Key terms
graph limits, bounded degree, left convergence, right convergence, homomorphism density, Dobrushin uniqueness, cluster expansion, Mayer expansion, chromatic invariant, partition function, hard-core model, q-coloring, Benjamini-Schramm
