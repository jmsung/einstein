---
type: source
kind: paper
title: Crossings Between Non-homotopic Edges
authors: J. Pach, G. Tardos, G'eza T'oth
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2006.14908
source_local: ../raw/2020-pach-crossings-between-non-homotopic-edges.pdf
topic: general-knowledge
cites:
---

# Crossings Between Non-homotopic Edges

**Authors:** J. Pach, G. Tardos, G'eza T'oth  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2006.14908

## One-line
Establishes a crossing-lemma-style bound for non-homotopic topological multigraphs: edges connecting the same vertex pair (or loops at the same vertex) must be drawn so none is homotopic to another, and one bounds the crossing number from below in terms of $n$ and $m$.

## Key claim
For a non-homotopic topological multigraph with $n>1$ vertices and $m>4n$ edges, $\operatorname{cr}(G) \ge \tfrac{1}{24}\,m^2/n$, and this is tight up to a polylogarithmic factor: there exist constructions achieving $\operatorname{cr}(G) \le 30\,(m^2/n)\log_2^2(m/n)$. For fixed $n\ge 2$ and $m\to\infty$, $\operatorname{cr}(n,m)/m^2 \to \infty$, so the quadratic lower bound is not asymptotically sharp.

## Method
Lower bound (Theorem 1) via a Turán-type argument: the non-crossing graph $D$ of edges has no clique of size $3n-2$ (by a planarity lemma bounding loose non-homotopic multigraphs at $3n-3$ edges in the plane / $3n-6$ on the sphere), so Turán bounds $|E(D)|$, and non-edges of $D$ lower-bound crossings. Upper bound (Theorem 2) constructs $x$-loops as concatenations of elementary polygonal loops representing distinct words in the free group $F_n = \pi_1(\mathbb{R}^2\setminus\{a_1,\dots,a_n\})$, perturbed so crossings track sign changes. Super-quadratic gap (Theorem 3) uses a finiteness theorem $f(n,k) < 2^{(2k)^{2n}}$ for non-homotopic $x$-loops with $<k$ self- and pairwise intersections, proved by an inductive face-splitting / signature-counting argument plus winding-number and Erdős–Szekeres lemmas.

## Result
Tight up to polylog: $\tfrac{1}{24}\,m^2/n \le \operatorname{cr}(n,m) \le 30\,(m^2/n)\log_2^2(m/n)$ for $n\ge 2$, $m>4n$. Auxiliary: loose non-homotopic multigraphs satisfy $m\le 3n-6$ (sphere) / $3n-3$ (plane). For the homotopy-counting function: $2^{\sqrt{nk/3}} \le f(n,k) \le 2^{(2k)^{2n}}$ when $2\le n\le 2k$; $f(n,k)\ge (n/k)^{k-1}$ for $n\ge 2k$; $\operatorname{cr}(n,m) = \Omega(\log m^{1/(6n)}/n^7)$ relative to $m^2$.

## Why it matters here
General background; no direct arena tie — none of the 23 Einstein Arena problems is a crossing-number / topological-multigraph problem. Closest tangential relevance is the Turán-type extremal argument (used in extremal graph problems on the inventory) and the Erdős–Szekeres lemma as a combinatorial sub-tool; the free-group-of-the-punctured-plane construction is unlikely to transfer.

## Open questions / connections
- Close the polylog gap between $m^2/n$ and $(m^2/n)\log_2^2(m/n)$ for $\operatorname{cr}(n,m)$.
- Tighten $f(n,k)$: conjecture that $\log f(n,k)$ is polynomial in $k$ with degree independent of $n$; current bounds $2^{\sqrt{k/3}} \le f(2,k) \le 2^{16k^4}$ leave huge room.
- Extends the Ajtai–Chvátal–Newborn–Szemerédi / Leighton crossing lemma and Székely's multigraph variant $\operatorname{cr}(G)\ge c'\,m^3/(kn^2)$ to the weakest possible non-degeneracy assumption (homotopy-distinctness only, no edge-multiplicity cap).

## Key terms
crossing number, crossing lemma, non-homotopic multigraph, topological graph, free group, fundamental group of punctured plane, winding number, Turán's theorem, Erdős–Szekeres lemma, Székely multigraph bound, loose multigraph, x-loop homotopy classes
