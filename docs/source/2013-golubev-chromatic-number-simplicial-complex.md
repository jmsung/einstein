---
type: source
kind: paper
title: On the chromatic number of a simplicial complex
authors: Konstantin Golubev
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1306.4818
source_local: ../raw/2013-golubev-chromatic-number-simplicial-complex.pdf
topic: general-knowledge
cites:
---

# On the chromatic number of a simplicial complex

**Authors:** Konstantin Golubev  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1306.4818

## One-line
Generalizes Hoffman's spectral lower bound on the chromatic number of a graph to pure $d$-dimensional simplicial complexes, using the spectra of higher (upper) Laplacian operators.

## Key claim
For a nonempty pure $d$-dimensional simplicial complex $X$ on $n$ vertices,
$$\alpha(X) \le \frac{\mu_0 \cdots \mu_{d-1} - (k_0+1)(k_1+2)\cdots(k_{d-2}+d-1)k_{d-1}}{\mu_0 \cdots \mu_{d-1}} \cdot n,$$
and hence $\chi(X) \ge \mu_0\cdots\mu_{d-1} / \bigl(\mu_0\cdots\mu_{d-1} - (k_0+1)\cdots(k_{d-2}+d-1)k_{d-1}\bigr)$, where $k_j$ is the minimum degree of a $j$-face and $\mu_j$ is the largest eigenvalue of the $j$-th upper Laplacian $\Delta^+_j$. Specializes to Hoffman's bound when $d=1$.

## Method
Spectral / Rayleigh-quotient argument on the Eckmann higher Laplacians $\Delta^+_j = \partial_j \circ \delta_j$ acting on antisymmetric cochains $C^j(X,\mathbb{R})$. The proof bounds $|X_1(A,B)|$ (edges between an independent set $A$ and its complement $B$) from above via the Rayleigh quotient of an indicator-like cochain $f_0 \in C^0$ against $\mu_0$, and from below by an inductive lemma that propagates a face-counting lower bound from dimension $d-1$ down to dimension $1$ using each $\mu_j$. A shorter direct proof is given for complexes with a complete $(d-1)$-skeleton via a tailored cochain $f \in C^{d-1}$.

## Result
The bound is sharp on the complete $d$-complex $K_n^d$: $\alpha(K_n^d) = d$, $\mu_{d-1}=n$, $k_{d-1}=n-d$, giving equality $d = (n-(n-d))/n \cdot n$. Auxiliary results: a Wilf-style upper bound $\chi(X) \le \lceil \chi(X^{(1)})/d \rceil$ relating weak chromatic number to underlying-graph chromatic number; recovery of Hoffman's classical bound $\alpha(G) \le \frac{\mu-k}{\mu}n$ as the $d=1$ case.

## Why it matters here
General background; no direct arena tie. Potentially relevant to problems with extremal-set / hypergraph-coloring structure (intersecting families, Kneser-type, Sidon-like incidence) where spectral bounds on independence numbers of higher-dimensional complexes could provide a Hoffman-style certificate; complements existing wiki coverage of LP/SDP relaxations and Lovász-style spectral methods.

## Open questions / connections
- Extends Hoffman 1970 and Lovász 1979 (Shannon capacity / Kneser) — does the higher-dim bound give sharp results for natural hypergraph analogues (e.g., Erdős–Ko–Rado for $r$-wise intersecting families)?
- Builds on Horak–Jost 2013 spectral theory of combinatorial Laplacians and Parzanchevski–Rosenthal–Tessler higher Cheeger inequalities — is there a higher-dim Lubotzky–Phillips–Sarnak Ramanujan-complex construction giving large $\chi$ and large girth in this sense?
- When is the bound tight beyond $K_n^d$? Identifying complexes where $\mu_j$'s align with degree products is open.

## Key terms
Hoffman bound, chromatic number, independence number, simplicial complex, higher Laplacian, upper Laplacian, Eckmann Laplacian, spectral graph theory, Rayleigh quotient, Horak-Jost, Parzanchevski-Rosenthal-Tessler, Kneser graph, Erdős-Ko-Rado, Ramanujan complex, weak chromatic number, hypergraph coloring
