---
type: source
kind: paper
title: Embedding graphs into larger graphs: results, methods, and problems
authors: Miklós Simonovits, Endre Szemerédi
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1912.02068v1
source_local: ../raw/2019-simonovits-embedding-graphs-larger-graphs.pdf
topic: general-knowledge
cites: 
---

# Embedding graphs into larger graphs: results, methods, and problems

**Authors:** Miklós Simonovits, Endre Szemerédi  ·  **Year:** 2019  ·  **Source:** http://arxiv.org/abs/1912.02068v1

## One-line
A wide-ranging survey of extremal graph theory — Turán-type problems, embedding, and the methods (Regularity, Stability, Blow-up, Semi-random, Absorbing) that drive them — dedicated to Lovász's 70th birthday.

## Key claim
Extremal graph theory is organized around a clean dichotomy: $\operatorname{ex}(n, \mathcal{L}) = o(n^2)$ iff $\mathcal{L}$ contains a bipartite graph; otherwise $\operatorname{ex}(n, \mathcal{L}) \geq \lfloor n^2/4 \rfloor$. The survey threads Mantel ($\lfloor n^2/4 \rfloor$ for $K_3$-free), Turán's theorem ($e(T_{n,p})$ for $K_{p+1}$-free), Erdős–Stone ($(1 - 1/p)\binom{n}{2} + o(n^2)$ for $K_{p+1}(t,\dots,t)$), and Kővári–Sós–Turán ($\operatorname{ex}(n, K(a,b)) \leq \tfrac12 (b-1)^{1/a} n^{2-1/a} + O(n)$) through a half-century of refinements.

## Method
Survey of methods rather than a single technique: Szemerédi's Regularity Lemma + Blow-up Lemma for dense embedding; Stability theory (Erdős–Simonovits, Lovász–Simonovits) showing near-extremal graphs are near-Turán; Semi-random / Rödl nibble for independent sets in uncrowded (hyper)graphs; Absorbing method for spanning structures; Dependent Random Choice, Hypergraph Containers, Flag Algebras (named, not detailed). Finite-geometric constructions (Erdős–Rényi–Sós, Brown, Kollár–Rónyai–Szabó) supply matching lower bounds for the Zarankiewicz / $K(a,b)$ regime.

## Result
Catalogues sharp / asymptotic Turán numbers across regimes: $\operatorname{ex}(n,C_4) = \Theta(n^{3/2})$; Kollár–Rónyai–Szabó give $\operatorname{ex}(n, K(a,b)) = \Theta(n^{2-1/a})$ for $b > (a-1)!$ (Alon–Rónyai–Szabó); Erdős's $C_4$-free bipartite bound $e(G) \leq 3n\sqrt{n}$ used to show $|A| \leq \pi(n) + O(n^{3/4})$ for multiplicative-Sidon sets in $[1,n]$. Surveys Ramsey–Turán theory, Pósa–Seymour, Bollobás–Eldridge, Ruzsa–Szemerédi triangle-removal, Erdős–Faber–Lovász, and hypergraph Dirac-type results (Rödl–Ruciński–Szemerédi).

## Why it matters here
General background on extremal/Turán methodology — Regularity, Stability, Semi-random, and the bipartite/non-bipartite dichotomy — relevant to arena problems with extremal-graph or hypergraph flavor (e.g. P12 large-feedback-arc, P13/P19 extremal-graph variants, Sidon-type autocorrelation problems). Anchors the wiki's pointers to Razborov flag algebras, Sidorenko's conjecture, and the Erdős–Sós / Loebl–Komlós–Sós tree-embedding line, which already appear in `docs/source/`.

## Open questions / connections
- Kővári–Sós–Turán sharpness conjecture: does $\operatorname{ex}(n, K(a,b)) \geq c_{a,b} n^{2-1/a}$ hold for **all** $a \leq b$ (currently open for $a \in \{2,3\}$ beyond known cases)?
- Erdős–Sós conjecture on tree-embedding (paper says proof is being written up [8]) and the Loebl–Komlós–Sós conjecture.
- Hypergraph Hamiltonicity / tight-cycle Dirac thresholds and hypergraph Turán densities (Razborov flag-algebra frontier).
- Pósa–Seymour, Bollobás–Eldridge packing, and Ramsey–Turán matching as open embedding frontiers.

## Key terms
extremal graph theory, Turán's theorem, Erdős–Stone theorem, Kővári–Sós–Turán, Zarankiewicz problem, Szemerédi regularity lemma, blow-up lemma, stability method, absorbing method, semi-random nibble, Sidon set, Ramsey–Turán, hypergraph Turán, Sidorenko conjecture, flag algebras
