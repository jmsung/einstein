---
type: source
kind: paper
title: A version of Szemerédi's regularity lemma for multicolored graphs and directed graphs that is suitable for induced graphs
authors: M. Axenovich, Ryan R. Martin
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1106.2871
source_local: ../raw/2011-axenovich-version-szemer-regularity-lemma.pdf
topic: general-knowledge
cites:
---

# A version of Szemerédi's regularity lemma for multicolored graphs and directed graphs that is suitable for induced graphs

**Authors:** M. Axenovich, Ryan R. Martin  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1106.2871

## One-line
Extends the Alon–Fischer–Krivelevich–Szegedy strong regularity lemma — which produces a partition plus a refined sub-partition suitable for *induced* embedding — from graphs to $r$-edge-colored complete graphs and to directed graphs.

## Key claim
For every $r\geq 2$, every $m$, and every function $E:\mathbb{N}\to(0,1)$, there exist $S,\delta$ such that any sufficiently large $r$-graph or digraph $G$ admits equipartitions $\mathcal{A}=\{V_i\}_{i=1}^k$ and $\mathcal{A}'=\{V_i'\subset V_i\}_{i=1}^k$ with $k\geq m$, $|V_i'|\geq \delta n$, where every pair in $\mathcal{A}'$ is $E(k)$-regular and all but $E(0)\binom{k}{2}$ pairs satisfy $\|d(V_i,V_{i'}) - d(V_i',V_{i'}')\|_\infty < E(0)$ in the vector of per-color densities (Theorem 1.12).

## Method
Iterate the standard multicolor / digraph regularity lemma (Komlós–Simonovits; Alon–Shapira) along a tower $T(1)<T(2)<\dots$ until the **mean-square density index** $\mathrm{ind}(\mathcal{A}) = k^{-2}\sum_{i<i'}\sum_\rho d_\rho(V_i,V_{i'})^2$ stops gaining $\Omega(r\epsilon^4)$ between consecutive refinements; the defect Cauchy–Schwarz lemma (Lemma 2.2) forces this to occur within $O(r\epsilon^{-4})$ steps. Per-color slicing and embedding lemmas (Lemmas 1.7, 1.8, 1.10, 1.11) carry the graph induction over to colored / oriented edges by treating the density as an $L^\infty$ vector across colors $\rho \in \{1,\dots,r\}$ or $\rho \in \{\square,-,\leftarrow,\to\}$. A random selection of one sub-cluster per part yields the final partition pair with positive probability.

## Result
Establishes the multicolor and digraph analogues of Alon–Fischer–Krivelevich–Szegedy. Embedding-lemma constants are explicit: $\gamma_{1.8}(\eta,k)=\min\{(\eta/2)^{k-1},(1/6)^{k-1}\}$ and $\delta_{1.8}(\eta,k)=\delta_{1.8}(\eta-\gamma,k-1)(\eta-\gamma)^{k-1}(1-(k-1)\gamma)$. As an application (Theorem 3.8/3.9), for any hereditary $r$-graph or digraph property $\mathcal{H}=\bigcap_{H\in\mathcal{F}(\mathcal{H})}\mathrm{Forb}(H)$ and random model $G_{n,\mathbf{p}}$, the edit distance satisfies $\mathrm{dist}(G_{n,\mathbf{p}},\mathcal{H}) \geq f_K(\mathbf{p})\binom{n}{2} - o(n^2)$ w.h.p. for some colored-type $K\in K(\mathcal{H})$, where $f_K(\mathbf{p}) = k^{-2}\mathbf{1}^T(J-\sum_\rho p_\rho A_\rho)\mathbf{1}$.

## Why it matters here
General background; no direct arena tie. Closest adjacency is the **extremal_graph / combinatorics** family — the strong-regularity machinery underpins Razborov flag algebras and induced-subgraph density bounds that occasionally appear in extremal-graph arena problems, but no current Einstein problem is known to live on a colored-regularity lemma.

## Open questions / connections
- Does the $f_K$ lower bound for digraph hereditary properties match the upper bound exactly (analogous to the Alon–Stav characterization for graphs)?
- The $\delta_{1.12}$ produced is tower-type in $1/\epsilon$ — is a primitive-recursive bound possible for the *colored* induced case, paralleling Conlon–Fox for graphs?
- Connection to flag-algebra / SDP relaxations: $f_K$ is a quadratic form $\mathbf{1}^T(J-\sum p_\rho A_\rho)\mathbf{1}$, which is exactly the shape optimized in Razborov-style density problems.

## Key terms
Szemerédi regularity lemma, strong regularity lemma, multicolored graphs, directed graphs, induced subgraph embedding, slicing lemma, embedding lemma, edit distance, hereditary properties, colored regularity graphs, Alon Fischer Krivelevich Szegedy, Komlós Simonovits, density index, flag algebra, defect Cauchy-Schwarz
