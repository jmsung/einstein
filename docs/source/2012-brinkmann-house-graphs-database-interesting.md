---
type: source
kind: paper
title: "House of Graphs: A database of interesting graphs"
authors: G. Brinkmann, K. Coolsaet, J. Goedgebeur, Hadrien Mélot
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1204.3549
source_local: ../raw/2012-brinkmann-house-graphs-database-interesting.pdf
topic: general-knowledge
cites:
---

# House of Graphs: A database of interesting graphs

**Authors:** G. Brinkmann, K. Coolsaet, J. Goedgebeur, Hadrien Mélot  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1204.3549

## One-line
Announces House of Graphs (hog.grinvin.org), a searchable online database of "interesting" graphs — counterexamples, extremal graphs, and named graphs — seeded with 1570 entries and extensible by registered users.

## Key claim
A curated small-but-rich list of interesting graphs (rather than exhaustive enumeration up to $n$ vertices, which is intractable — e.g. $\approx 2.9 \times 10^{16}$ connected graphs on 14 vertices) gives a high-yield search space for testing conjectures and hunting counterexamples; the database makes this list searchable by invariant ranges, keywords, and isomorphism-checked uploads.

## Method
Curation strategy: import extremal graphs from GraPHedron (polyhedral approach — graphs are placed in $p$-dimensional invariant space and vertices of the convex hull are flagged extremal); collapse "conglomerates" (many graphs at one extremal point, e.g. trees, $K_{m,n}$) via a greedy heuristic for the underlying NP-complete minimum set cover. Invariant values (chromatic number, clique number, diameter, matching number, …) are computed via Grinvin and stored; submissions are isomorphism-checked against existing entries.

## Result
Public database with $\approx 1570$ seed graphs, searchable by invariant, range, keyword, or graph6/multicode upload. Hosts or links to complete lists: snarks up to 34 vertices (girth 4) / 36 vertices (girth 5), IPR-fullerenes up to 160 vertices, regular graphs by (degree, $n$, girth), vertex-transitive graphs, planar classes. Worked example: girth 6 → regular → average degree 3 → 14 vertices uniquely retrieves the Heawood (3,6)-cage.

## Why it matters here
General background; no direct arena tie. Potentially useful as a lookup index if a discrete-geometry / extremal-graph arena problem (e.g. kissing-graph contact structure, extremal Sidon-set incidence graphs) reduces to checking small candidate graphs against named/extremal entries — but no arena problem currently invokes the named-graph zoo directly.

## Open questions / connections
- Extends GraPHedron (Mélot 2008) as a public-facing extremal-graph repository.
- Open: does the conglomerate-representative greedy heuristic miss extremal points whose only representatives are atypical? (NP-complete set-cover approximation).
- Connection: complements McKay's geng, Meringer's genreg, snarkhunter as the "curated counterexample" layer above exhaustive generators.

## Key terms
graph database, extremal graphs, GraPHedron, polyhedral method, graph invariants, snarks, IPR-fullerenes, Heawood graph, Petersen graph, cages, conglomerates, set cover, graph6 format
