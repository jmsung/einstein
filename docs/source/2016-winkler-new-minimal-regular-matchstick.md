---
type: source
kind: paper
title: New minimal (4; n)-regular matchstick graphs
authors: Mike Winkler, Ph.D., P. Dinkelacker, Stefan Vogel
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1604.07134
source_local: ../raw/2016-winkler-new-minimal-regular-matchstick.pdf
topic: general-knowledge
cites:
---

# New minimal (4; n)-regular matchstick graphs

**Authors:** Mike Winkler, Ph.D., P. Dinkelacker, Stefan Vogel  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1604.07134

## One-line
Catalogs the smallest known (4;n)-regular matchstick graphs (planar unit-distance graphs with non-crossing edges) for $4 \le n \le 11$, presenting new constructions discovered 2016–2018.

## Key claim
New minimal (4;n)-regular matchstick graphs are exhibited with vertex/edge counts: $n=4$: 52v/104e (Harborth, baseline) and a new 54v/108e and 57v/114e; $n=5$: 57v/115e; $n=6$: 57v/117e; $n=7$: 78v/159e (flexible); $n=8$: 62v/126e; $n=9$: 134v/273e; $n=10$: 114v/231e; $n=11$: 382v/771e. For $n>11$ only infinite examples exist.

## Method
Constructive combinatorial geometry: assemble graphs from rigid subgraph "modules" — the *kite* (12v/21e, (2;4)-regular), *double kite* and *reverse double kite* (22v/42e), and *triplet kite* (22v/41e). The $n=11$ case requires CAS-aided angle solving (eleven angles around a degree-11 vertex tuned to ~32.36°, 40.49°, 25.38°, ..., summing to $360°$ with all incident edges unit length). Rigidity/flexibility verified with Vogel's *Matchstick Graphs Calculator* (browser-based CAS).

## Result
Provides explicit constructions (with figures and online MGC proofs) for the current record holders at each $n \in \{4,\dots,11\}$. Most graphs are rigid; $n=7$ graphs are flexible and lack kite-substructure. The $n=11$ graph contains a rigid subgraph that becomes flexible upon removing one edge — exploited to tune eleven angles to satisfy unit-length constraints simultaneously. No matching lower-bound proofs; minimality is "smallest known", not proven optimal.

## Why it matters here
General background; no direct arena tie. Touches discrete geometry / planar unit-distance graphs and constraint satisfaction via rigidity tuning, which conceptually overlaps with Einstein Arena discrete-geometry / packing problems (e.g., contact-graph constructions, rigidity-based angle solving as in P11-style configurations).

## Open questions / connections
- It is open which $n$ admit smaller (4;n)-regular matchstick graphs than those listed — no matching lower bounds.
- For $n=7$: does a *rigid* or *kite-based* (4;7)-regular matchstick graph with $\le 159$ edges exist?
- For $n=10$: does a *symmetric* (4;10)-regular matchstick graph with $\le 231$ edges exist?
- Extends Harborth (1986) 52v/104e baseline; relates to Kurz–Mazzuoccolo work on 3-regular matchstick graphs with given girth.

## Key terms
matchstick graph, unit-distance graph, planar graph, Harborth graph, 4-regular graph, (4;n)-regular, rigidity, flexibility, kite subgraph, triplet kite, discrete geometry, Winkler
