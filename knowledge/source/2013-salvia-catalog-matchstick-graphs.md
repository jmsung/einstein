---
type: source
kind: paper
title: A catalog for matchstick graphs
authors: Raffaele Salvia
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1303.5965
source_local: ../raw/2013-salvia-catalog-matchstick-graphs.pdf
topic: general-knowledge
cites:
---

# A catalog for matchstick graphs

**Authors:** Raffaele Salvia  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1303.5965

## One-line
Enumerates all connected planar unit-distance graphs (matchstick graphs) with up to 9 edges, by both topological and isomorphism classes.

## Key claim
For $n=9$ edges, there are exactly $\varrho(9)=633$ nonisomorphic connected matchstick graphs falling into $\varphi(9)=19$ homeomorphism classes; the full count across $|E|\le 9$ is 964 distinct matchstick graphs. Both sequences grow faster than exponentially with $n$.

## Method
Exhaustive hand-classification: enumerate all connected planar graphs with $|E|\le 9$, filter by realizability as a unit-distance embedding in the plane (matchstick condition), group by topological homeomorphism, then by isomorphism. Graphs are organized by edge count $|E|$, face count $F$ (including outer), and max degree $\Delta$. Extends Read (1968) who had solved $n\le 8$.

## Result
Tabulates $\varrho(n)$ and $\varphi(n)$ for $n=1,\dots,9$ (matching OEIS A003055, A066951 through $n=8$, adding $n=9$). Empirical extrapolation predicts $\varrho(10)\in[500,600]$ and $\varphi(10)\approx 2000$–$2100$ (lower bounds $\varrho(10)\ge 458$, $\varphi(10)\ge 1936$ from incremental-ratio monotonicity for $n>4$). Recognizing matchstick realizability is NP-hard (Eades–Wormald 1990; Cabello–Demaine–Rote 2007), so no closed-form is known.

## Why it matters here
General background; no direct arena tie. Matchstick graphs sit in the intersection of planar graphs and unit-distance graphs — adjacent to discrete-geometry / packing themes (rigid bar frameworks, contact graphs in disk packings) but the arena problems do not currently invoke a planar unit-edge enumeration.

## Open questions / connections
- Closed-form or asymptotic for $\varrho(n)$, $\varphi(n)$? Growth rate is faster than exponential but uncharacterized.
- Exact value of $\varrho(10)$, $\varphi(10)$ — predicted but not computed.
- Relation to the unit-distance graph problem (Erdős): how do matchstick (planar UD) counts relate to general UD-graph counts on $n$ vertices?
- Connection to rigid-bar frameworks / Henneberg constructions — what fraction admit a unique embedding?

## Key terms
matchstick graph, unit-distance graph, planar graph, graph enumeration, homeomorphism class, isomorphism class, NP-hard realizability, Eades-Wormald, Cabello-Demaine-Rote, Harborth, OEIS A003055, OEIS A066951, discrete geometry
