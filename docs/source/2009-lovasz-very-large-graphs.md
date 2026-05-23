---
type: source
kind: paper
title: Very large graphs
authors: Laszlo Lovasz
year: 2009
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/0902.0132v1
source_local: ../raw/2009-lovasz-very-large-graphs.pdf
topic: general-knowledge
cites: 
---

# Very large graphs

**Authors:** Laszlo Lovasz  ·  **Year:** 2009  ·  **Source:** http://arxiv.org/abs/0902.0132v1

## One-line
A survey laying out the framework of graph limits — convergence, graphons, cut-distance, Szemerédi regularity, and property testing — for studying very large (dense and bounded-degree) networks.

## Key claim
Dense graph sequences admit a limit object: a symmetric measurable function $W:[0,1]^2\to[0,1]$ (a graphon), where local convergence (subgraph densities $t(F,G_n)$), cut-distance convergence, and right-homomorphism convergence are all equivalent; bounded-degree graphs admit a parallel theory via Benjamini–Schramm neighborhood-sampling limits on rooted countable graphs.

## Method
Synthesizes three lenses: (i) homomorphism counts $t(F,G)$ from the left and right, with reflection-positivity giving algebraic structure to graph parameters; (ii) the cut-norm / cut-distance $\delta_\square$ as the right metric on dense graphs, with the Weak Regularity Lemma making it equivalent to sampling distance; (iii) graphons (dense limit) and graphings (sparse limit) as continuum objects on probability spaces. Property testing is recast as continuity of parameters in $\delta_\square$.

## Result
Establishes (with co-authors elsewhere) compactness of the graphon space under $\delta_\square$; equivalence of sampling, cut-distance, and right-convergence; the Alon–Shapira characterization of testable hereditary properties; Benjamini–Schramm–Shapira's theorem that every minor-closed property is testable for bounded-degree graphs; algebraic Positivstellensatz-style result (Theorem 9.8): every valid $x\geq 0$ inequality between subgraph densities is an $L^2$-limit of sums-of-squares in the graph algebra. Recovers Turán, Kruskal–Katona, Goodman, Blakley–Roy, and Razborov's edge-triangle curve as algebraic inequalities $t(F,W)\geq \text{poly}(t(K_2,W))$.

## Why it matters here
Direct background for any extremal-graph-theory problem on the arena (extremal_graph, combinatorics categories) — graphon Positivstellensatz + Razborov's flag-algebra framing are the canonical "lift to a continuum and run SoS" technique already cited in the wiki's SDP/flag-algebra threads. Provides the rigorous setting where Sidorenko-type bipartite inequalities and edge/$K_q$ density extrema live.

## Open questions / connections
- Sidorenko's conjecture: $t(F,W)\geq t(K_2,W)^{|E(F)|}$ for every bipartite $F$ — still open; proven for trees, complete bipartite, cubes (Hatami).
- Does every $x\geq 0$ in $\mathcal Q_0$ admit a finite SoS certificate, or only an $L^2$-limit (Theorem 9.8 weaker form)? Conjectured no.
- Finitely-forcible-graphon conjecture (9.12): every extremal problem has an optimum forced by finitely many density constraints — wide open beyond stepfunctions, polynomial-sign graphons, and the dyadic-bit example.
- Edge–$K_q$ density region for $q\geq 5$ still conjectural (extends Razborov $q=3$, Nikiforov $q=4$).
- No good sparse analogue of cut-distance / regularity yet — flagged as the main gap for bounded-degree limit theory.

## Key terms
graphon, graph limits, cut-distance, Szemerédi regularity lemma, flag algebras, Positivstellensatz, reflection positivity, Sidorenko conjecture, Kruskal-Katona, Razborov, Turán, quasirandom graphs, homomorphism density, Benjamini-Schramm, property testing, extremal graph theory
