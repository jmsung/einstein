---
type: source
kind: paper
title: Limits of local-global convergent graph sequences
authors: Hamed Hatami, László Lovász, Balázs Szegedy
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1205.4356v2
source_local: ../raw/2012-hatami-limits-local-global-convergent-graph.pdf
topic: general-knowledge
cites: 
---

# Limits of local-global convergent graph sequences

**Authors:** Hamed Hatami, László Lovász, Balázs Szegedy  ·  **Year:** 2012  ·  **Source:** http://arxiv.org/abs/1205.4356v2

## One-line
Introduces a refined "local-global" convergence notion for bounded-degree graph sequences (sensitive to both local neighborhood statistics and global colorings) and proves the limit object is representable by a graphing.

## Method
Define convergence via Hausdorff distance of "quotient sets" $Q_{G,r,k} \subseteq M(U_{r,k})$ — the set of distributions of $r$-radius colored neighborhoods over all $k$-colorings. A "regularization lemma" produces a bounded-size coloring that approximates any $k$-coloring's local statistics; this lets one assemble a universal Polish space $X = \mathcal{G}(C)$ on which the limit graphing lives, recovered via weak limits of measures.

## Key claim
For every local-global convergent sequence $(G_i)$ of bounded-degree graphs, there exists a graphing $G$ (Borel graph on a probability space satisfying the mass-transport identity $\int_A e(x,B)\,d\nu = \int_B e(x,A)\,d\nu$) such that $Q_{G_n,r,k} \to Q_{G,r,k}$ in Hausdorff distance for every $r,k$.

## Result
Main theorem: graphings represent local-global limits, refining the Benjamini–Schramm framework. Auxiliary results: (i) a partial order $\prec$ on graphings inside each local-equivalence class has a smallest element (the Bernoulli graphing) and a largest element (join construction); (ii) every atom-free hyperfinite graphing is locally-globally equivalent to its Bernoulli graphing, so locally convergent hyperfinite sequences are automatically local-global convergent (also proved independently by Elek); (iii) spectral gap and expansion are local-global invariants, while ergodicity/bipartiteness are not even local-global invariants (cycle examples $C_a, C_a', C_a''$).

## Why it matters here
General background; no direct arena tie. Closest relevance is to extremal-graph and sparse-graph regularity questions (P-class problems involving bounded-degree structure, expansion, or hyperfiniteness) and to the broader graph-limits machinery [[graphons]] / [[benjamini-schramm-convergence]] that frames extremal problems as limit-object optimizations.

## Open questions / connections
- Aldous–Lyons conjecture: does every involution-invariant measure arise as a graph limit? Strengthening: is every graphing a local-global limit of finite graphs?
- Can a $d$-regular graphing be a strictly better expander than any finite $d$-regular graph? Would refute the strengthened conjecture.
- Is every graphing $(d+1)$-edge-colorable in a Borel way (Vizing for graphings)?
- Finer convergence notions needed to distinguish ergodic vs bipartite vs disconnected limits (the $C_a, C_a', C_a''$ examples) — open theory.
- Connection to factor-of-i.i.d. processes / local algorithms: Bernoulli graphings = least-global-information limits, formalizing "what local algorithms can compute."

## Key terms
graphing, local-global convergence, Benjamini–Schramm convergence, bounded-degree graph limits, involution-invariant measure, Bernoulli graphing, hyperfinite, factor of i.i.d., local algorithm, expander, spectral gap, Aldous–Lyons conjecture, colored neighborhood metric, unimodular random graph
