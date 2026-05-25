---
type: source
kind: paper
title: Upper Tail Large Deviations of Regular Subgraph Counts in Erdős‐Rényi Graphs in the Full Localized Regime
authors: Anirban Basak, Riddhipratim Basu
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1912.11410
source_local: ../raw/2019-basak-upper-tail-large-deviations.pdf
topic: general-knowledge
cites:
---

# Upper Tail Large Deviations of Regular Subgraph Counts in Erdős‐Rényi Graphs in the Full Localized Regime

**Authors:** Anirban Basak, Riddhipratim Basu  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1912.11410

## One-line
Proves the conjectured upper-tail large-deviation rate for the count of any connected $\Delta$-regular subgraph $H$ in the sparse Erdős–Rényi graph $G(n,p)$ across the entire "localized" regime $(\log n)^{1/(v_H-2)} \ll np^{\Delta/2} \ll n$.

## Key claim
For any connected $\Delta$-regular graph $H$ ($\Delta\ge 2$) and $\delta>0$, $\lim_{n\to\infty} -\log \mathbb{P}(\mathrm{UT}(H,\delta))/(n^2 p^\Delta \log(1/p)) = \min\{\theta_H,\,\tfrac{1}{2}\delta^{2/v_H}\}$ when $n^{-1/2}\ll p^{\Delta/2}$, and $=\tfrac{1}{2}\delta^{2/v_H}$ when $(\log n)^{1/(v_H-2)}\ll np^{\Delta/2}\ll n^{1/2}$, where $\theta_H$ solves $P_H(\theta)=1+\delta$ for the independence polynomial $P_H$.

## Method
Extends the Harel–Mousset–Samotij "seed → core graph + union bound" entropic-stability framework: when the standard core-graph net is too big (the bipartite obstruction, e.g. $K_{2,Cn^2p^2}$ for $C_4$), they build refined nets via a *strong-core* graph whose bipartite subgraph $G_b$ has a long blow-up-of-a-path block structure, decoupling the count into $G_b$ and $G\setminus G_b$ for separate entropic-stability bounds. A dyadic chaining argument over $e(G)$ scales, plus a low-degree/high-degree edge split controlled by $N_{1,1}(H,G)$, covers the sparser sub-regime where the bipartite reduction fails; a Kőnig edge-coloring decomposition of the bipartite double cover of $H$ provides the matching/cycle covers needed for the counting lemmas.

## Result
The rate function matches the mean-field variational problem $\Phi_{n,H}(\delta)$ from Bhattacharya–Ganguly–Lubetzky–Zhao, whose minimizer for $p\ll n^{-1/\Delta}$ is planting a clique on $\delta^{1/v_H} np^{\Delta/2}$ vertices. Combined with HMS for the denser side, this closes the conjecture across the full localized regime for all connected regular $H$, matching the optimal Poisson-regime threshold exponent $1/(v_H-2)$.

## Why it matters here
General background; no direct arena tie — this is sparse random-graph large-deviation theory (clique-planting as the optimal upper-tail structure), tangentially relevant to extremal-graph and combinatorial problems but not the Einstein Arena problem set directly.

## Open questions / connections
- Boundary behavior at $np^{\Delta/2}\sim (\log n)^{1/(v_H-2)}$: localized and Poisson regimes are conjectured to coexist; authors believe their chaining ideas extend.
- Irregular graphs ($H$ with non-uniform degree) remain open below $p\ll n^{-1/\Delta}$; the DeMarco–Kahn conjecture has known counterexamples (Šileikis–Warnke).
- Extension to homomorphism counts $\mathrm{Hom}(C_{2t},G)$ would yield upper-tail LDP for the top adjacency eigenvalue of $G(n,p)$ in the sparse regime; also open for random regular graphs and random hypergraphs in sparser ranges.

## Key terms
Erdős–Rényi graph, upper tail large deviations, subgraph counts, regular graph, localized regime, mean-field variational problem, independence polynomial, entropic stability, core graph, seed graph, clique planting, Kőnig edge coloring, bipartite double cover, Harel–Mousset–Samotij, Bhattacharya–Ganguly–Lubetzky–Zhao, Szemerédi regularity, sparse random graphs, chaining argument
