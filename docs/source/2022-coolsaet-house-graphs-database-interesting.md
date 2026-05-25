---
type: source
kind: paper
title: "House of Graphs 2.0: a database of interesting graphs and more"
authors: K. Coolsaet, Sven D'hondt, J. Goedgebeur
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2210.17253
source_local: ../raw/2022-coolsaet-house-graphs-database-interesting.pdf
topic: general-knowledge
cites:
---

# House of Graphs 2.0: a database of interesting graphs and more

**Authors:** K. Coolsaet, Sven D'hondt, J. Goedgebeur  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2210.17253

## One-line
Announces a rebuilt web database (https://houseofgraphs.org) of ~22,000 "interesting" graphs — named graphs, conjecture counterexamples, extremal graphs — searchable by 44 precomputed invariants.

## Key claim
The new House of Graphs hosts ~22,000 curated graphs across 27 graph-class meta-directories with 44 boolean+numeric invariants precomputed per graph, queryable by invariant value/range, keyword, or graph6/HoG-id, with user-uploadable graphs canonicalised via nauty before insertion.

## Method
Rebuilt stack: PostgreSQL + Spring (Java back-end) + React/TypeScript + D3 front-end + Docker, replacing the 2012 Struts/GWT/Grinvin stack. Invariant computation is decoupled into standalone CLI programs (any language) scheduled through a Slurm multilevel feedback queue so cheap invariants finish fast while NP-hard ones (treewidth, hamiltonicity, genus) get longer slots. Key external solvers: nauty (canonical form / isomorphism), Boyer–Myrvold planarity, Brinkmann genus, Tamaki treewidth, Goedgebeur–Renders (hypo)hamiltonicity.

## Result
Database grew from ~1,500 graphs (2012) to ~22,000; invariants from 24 → 44; graph-class meta-directory lists from 10 → 27 (snarks, fullerenes, cubic, quartic, nut, platypus, perihamiltonian, hypohamiltonian, triangle-free k-chromatic, …). New features: multiple drawings per graph, D3-based editor with spring embedder + tikz/svg/pdf export, formula-style search planned, bcrypt password hashing replacing MD5.

## Why it matters here
General background; no direct arena tie. Closest hooks are P3/P7 (extremal-graph-theory and discrete combinatorics problems) — HoG could serve as a lookup for named extremal graphs (Petersen, Coxeter, Heawood, Chvátal) or counterexample candidates when an arena problem reduces to a known small-graph configuration; nauty's canonical form is the standard way to check "have I seen this graph before."

## Open questions / connections
- Can HoG's keyword/invariant search seed council-dispatch when a problem reduces to small-graph extremal questions (e.g. minimum graph with given chromatic-number × girth)?
- Planned subgraph-containment search would let us query "does any HoG graph contain G as induced subgraph" — useful for extremal/Turán-style problems.
- Extends Brinkmann–Coolsaet–Goedgebeur–Mélot 2013 [4]; complements GraPHedron [22] conjecture-making system.

## Key terms
House of Graphs, graph database, graph invariants, nauty, canonical form, graph6 format, extremal graphs, snarks, fullerenes, cubic graphs, hypohamiltonian, treewidth, GraPHedron, Brinkmann, Goedgebeur, McKay
