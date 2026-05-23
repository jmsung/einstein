---
type: source
kind: paper
title: Bounding the number of edges of matchstick graphs
authors: J'er'emy Lavoll'ee, K. Swanepoel
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2108.07522
source_local: ../raw/2021-lavollee-bounding-number-edges-matchstick.pdf
topic: general-knowledge
cites:
---

# Bounding the number of edges of matchstick graphs

**Authors:** J'er'emy Lavoll'ee, K. Swanepoel  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2108.07522

## One-line
Improves the upper bound on the number of edges of an $n$-vertex matchstick graph (planar unit-distance graphs drawn without crossings), making partial progress toward Harborth's conjecture.

## Key claim
Any matchstick graph with $n$ vertices has $e \le 3n - c\sqrt{n - 1/4}$ edges, where $c = \tfrac{1}{2}\sqrt{12 + 2\pi\sqrt{3}} \approx 3.3815$ — strong enough to settle Harborth's conjectured maximum $3n - \lceil\sqrt{12n-3}\rceil$ for all $n \le 14$ and a long list of larger sporadic $n$ (16, 18–21, 23, …, 120, 127).

## Method
Combines (i) Euler's formula for plane graphs with the double-counting identity $e = 3n - 3 - b - \sum_{i\ge 4}(i-3)f_i$ (Lemma 4), (ii) an induction-on-$n$ argument refining Harborth's penny-graph proof to obtain $e \le 3n - \lceil\sqrt{12n-3}\rceil + g$ in terms of the number $g$ of bounded non-triangular faces (Theorem 2), and (iii) the isoperimetric inequality applied to the outer boundary polygon, yielding $b^2 > \pi\sqrt{3} f_3$ (Lemma 5). Case analysis on cut vertices, chords, and shared boundary vertices closes the induction.

## Result
Theorem 1: $e \le 3n - c\sqrt{n - 1/4}$ with $c \approx 3.3815$, improving on the easy bound $3n - \sqrt{2\pi\sqrt{3}}\sqrt{n} + O(1) \approx 3n - 3.30\sqrt{n}$. Corollary 3: the number of bounded triangular faces is at most $2n + 1 - \lceil\sqrt{12n-3}\rceil$, and this is sharp — attained by triangular-lattice patches (Figure 2).

## Why it matters here
Direct relevance to discrete-geometry / extremal-graph arena problems involving unit-distance constraints and crossing-free planar drawings; tightens the constant in the leading $\sqrt{n}$ correction to $3n$, a quantity that appears whenever isoperimetric + Euler arguments bound edge counts of triangulated planar configurations. Complements existing wiki content on penny graphs, the triangular lattice, and isoperimetric arguments used in packing bounds.

## Open questions / connections
- Closing the gap to Harborth's exact conjecture $3n - \lceil\sqrt{12n-3}\rceil$ for all $n$ (currently only $n \le 14$ and sporadic cases).
- Extending Eppstein's $2n - c\sqrt{n}$ bound for triangle-free *penny* graphs to triangle-free *matchstick* graphs — blocked because non-triangular faces have no obvious lower area bound.
- Remark 8 notes a slightly stronger bound $e \le 3n - \sqrt{12(n+2g) - 3} + g$ is provable with more boundary casework; tightening $c$ further likely needs new ideas beyond Euler + isoperimetric.

## Key terms
matchstick graph, penny graph, unit-distance graph, Harborth conjecture, Euler formula, isoperimetric inequality, triangular lattice, planar graph edge bound, double counting, 2-connected planar graph, triangle-free penny graph, Eppstein, Swanepoel, extremal planar graph
