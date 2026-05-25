---
type: source
kind: paper
title: Charting the space of chemical nut graphs
authors: P. Fowler, Tomavz Pisanski, Nino Bavsi'c
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2009.01286
source_local: ../raw/2020-fowler-charting-space-chemical-nut.pdf
topic: general-knowledge
cites:
---

# Charting the space of chemical nut graphs

**Authors:** P. Fowler, Tomavz Pisanski, Nino Bavsi'c  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2009.01286

## One-line
Characterizes exactly which degree-signature pairs $(v_3, v_2)$ admit a "chemical nut graph" — a connected simple graph of max degree 3 whose adjacency matrix has nullity 1 with a nowhere-zero kernel eigenvector.

## Key claim
A chemical nut graph with $v_3$ vertices of degree 3 (even, $>0$) and $v_2$ vertices of degree 2 exists iff one of: (a) $v_3=2, v_2=7+2k$; (b) $v_3=4, v_2=10+2k$; (c) $v_3=6, v_2 \geq 7$; (d) $v_3 \geq 8$ with 11 explicit small exceptions $\{(8,0),(8,1),(8,2),(8,4),(10,0),(10,1),(10,2),(12,1),(14,0),(14,2),(16,0)\}$. All realisable pairs except $(20,0)$ admit a planar realisation.

## Method
Combines (i) a finite computer-generated census of chemical nut graphs up to $n \leq 22$ as a seed-graph atlas, with (ii) three local "growth" constructions that preserve the nut property and surface genus: **bridge insertion** (add 2 vertices on a bridge → $v_2 \mapsto v_2+2$), **edge subdivision** (insert 4 vertices on any edge → $v_2 \mapsto v_2+4$), and the **Fowler construction** (replace a degree-$d$ vertex with a cocktail-party gadget → $v_3 \mapsto v_3 + 2d$). Each construction is proved iff-preserving via an explicit kernel-eigenvector extension rule. A pigeonhole argument (Theorem 12: if $v_2 \geq \tfrac{9}{2}v_3+1$ then some edge of the underlying cubic has $\geq 4$ subdivision vertices) propagates non-realisability infinitely upward.

## Result
The realisability "chart" Table 2 fills the entire $(v_3, v_2)$ quadrant from 22 seed graphs (11 bridged-planar, 7 2-connected-planar, 3 polyhedral, 1 toroidal at $(20,0)$). Polyhedral (3-connected planar) chemical nut graphs exist iff $v_2 = 0$ and $v_3 \in \{12, 18\} \cup \{v_3 \geq 24 : v_3 \text{ even}\}$. Toroidal 3-regular nut graphs exist for every even $n \geq 20$. Betti number range: $1 < m - n + 1 \leq \tfrac{n+1}{2}$ with a small explicit list of missing values per $n$.

## Why it matters here
General background; no direct arena tie. Possible weak relevance to extremal-graph / discrete-structure problems where nullity-1 spectral constraints or constructive enumeration of degree-constrained graphs appear — the seed-plus-local-construction pattern is a transferable proof template for "characterize all $(a,b)$ such that an object exists" combinatorial-existence problems.

## Open questions / connections
- Existence of *signed* chemical nut graphs (explicitly raised as future work; cites [Belardo et al., Ghorbani et al.]).
- Stability/realisability of nut fullerenes as actual carbon molecules — all known nut fullerenes have multiple pentagon-pentagon adjacencies, suggesting chemical instability.
- Whether the seed-and-construction framework generalises to higher max degree or other spectral-nullity constraints (extends Sciriha's earlier nut-graph series and Gauci–Pisanski–Sciriha's regular-nut-graph work).

## Key terms
nut graph, chemical graph, singular adjacency matrix, kernel eigenvector, nullity one, Fowler construction, bridge construction, subdivision construction, cubic graph, polyhedral graph, fullerene, Hückel model, omniconductor, seed graph
