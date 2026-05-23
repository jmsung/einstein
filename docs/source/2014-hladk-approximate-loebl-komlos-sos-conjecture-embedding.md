---
type: source
kind: paper
title: THE APPROXIMATE LOEBL-KOMLOS-SOS CONJECTURE AND EMBEDDING TREES IN SPARSE GRAPHS
authors: J. Hladký, Diana Piguet, M. Simonovits, M. Stein, E. Szemerédi
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1406.3935
source_local: ../raw/2014-hladk-approximate-loebl-komlos-sos-conjecture-embedding.pdf
topic: general-knowledge
cites:
---

# THE APPROXIMATE LOEBL-KOMLOS-SOS CONJECTURE AND EMBEDDING TREES IN SPARSE GRAPHS

**Authors:** J. Hladký, Diana Piguet, M. Simonovits, M. Stein, E. Szemerédi  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1406.3935

## One-line
Sketch of an approximate proof of the Loebl–Komlós–Sós conjecture for large $k$, via a new "sparse decomposition" that extends Szemerédi's regularity lemma to sparse host graphs for tree embedding.

## Key claim
**Theorem 3:** For every $\varepsilon > 0$ there exists $k_0$ such that for every $k > k_0$, every $n$-vertex graph $G$ with at least $(1+\varepsilon)n/2$ vertices of degree at least $(1+\varepsilon)k$ contains every tree $T$ with $k$ edges as a subgraph.

## Method
Introduces a **sparse decomposition** that splits any graph (after removing $o(kn)$ edges) into four parts: $\Psi$ (huge-degree vertices, $\deg \geq \Omega^{**}k$), $G_{\mathrm{reg}}$ (regular pairs from regularizing maximal edge-disjoint $(\gamma k,\gamma)$-dense spots simultaneously via a Vizing-coloring + multi-energy refinement of Szemerédi's argument), $G_{\mathrm{exp}}$ (a $(\gamma k,\gamma)$-nowhere-dense expander with min-degree $\geq \rho k$), and $A$ (small Venn cells with an $(\Lambda,\beta,\gamma)$-avoiding expansion property). The tree $T$ is cut into small subtrees ($< \tau k$) plus a small "skeleton" $W = W_A \cup W_B$ (Lemma 5), then placed via a global matching-like structure (Lemma 7: cluster sets $X,Y \subseteq L$ playing the role of $A,B$ in the dense case, with a regular matching $M$) and local embedding strategies tailored to each of the four parts.

## Result
The approximate LKS conjecture holds for all sufficiently large $k$, with no restriction $k = \Theta(n)$ — i.e., it covers the sparse regime $k = o(n)$ that the original regularity lemma cannot reach. The degree threshold $(1+\varepsilon)k$ on $(1+\varepsilon)n/2$ vertices is asymptotically tight (the extremal graph $G^*$ from $K_n$ minus a clique on $n/2+1$ vertices has $n/2-1$ vertices of degree exactly $k$ and contains no $k$-edge path). Implies Ramsey bound $R(T_k, T_m) \leq k+m$ asymptotically.

## Why it matters here
General background; no direct arena tie. The sparse-decomposition machinery (huge-degree set + regular pairs + nowhere-dense expander + avoiding-property set) is a structural template potentially relevant to any extremal-graph / discrete-geometry problem where the natural host is sparse, but none of the 23 Einstein Arena problems currently in scope is a tree-containment or LKS-type question.

## Open questions / connections
- Exact (not approximate) LKS conjecture for large $k$ — authors flag this as work in progress via Simonovits stability methods.
- Whether LKS can be proved without the regularity lemma / sparse decomposition (analogous to the Levitt–Sárközy–Szemerédi "deregularization" of Pósa's conjecture).
- The sparse decomposition is highly non-unique (unlike the essentially-unique dense regularity partition of Alon–Shapira–Stav) — open whether a canonical sparse decomposition exists.
- Erdős–Sós conjecture (the average-degree analogue) — same machinery, in-preparation proof by Ajtai–Komlós–Simonovits–Szemerédi.

## Key terms
Loebl-Komlos-Sos conjecture, Erdos-Sos conjecture, sparse regularity lemma, sparse decomposition, tree embedding, extremal graph theory, regular pairs, nowhere-dense graph, dense spots, avoiding property, cluster graph, Szemeredi regularity lemma, median degree, Vizing coloring, Ramsey number for trees
