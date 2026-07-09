---
type: source
kind: paper
title: How to determine if a random graph with a fixed degree sequence has a giant component
authors: Felix Joos, Guillem Perarnau, Dieter Rautenbach, Bruce Reed
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1601.03714v3
source_local: ../raw/2016-joos-how-determine-random-graph.pdf
topic: general-knowledge
cites: 
---

# How to determine if a random graph with a fixed degree sequence has a giant component

**Authors:** Felix Joos, Guillem Perarnau, Dieter Rautenbach, Bruce Reed  ·  **Year:** 2016  ·  **Source:** http://arxiv.org/abs/1601.03714v3

## One-line
Gives a sharp criterion — valid for essentially every feasible degree sequence — determining whether the random simple graph $G(D)$ with prescribed degrees has a linear-order component.

## Key claim
A well-behaved feasible degree sequence $D$ (meaning $M_D := \sum_{d_i \ne 2} d_i \to \infty$) yields a giant component in $G(D)$ w.h.p. iff $R_D \ge \epsilon M_D$, where $R_D$ is the sum of the top-degree tail beyond the index $j_D$ at which the partial sum $\sum_{i \le j}d_{\pi_i}(d_{\pi_i}-2)$ first becomes positive (degrees sorted ascending). The classical Molloy–Reed ratio $\sum d_i(d_i-2)/\sum d_i$ is shown to give the *wrong* answer in general (e.g. star + matching example with ratio $\approx 3$ but no giant component).

## Method
Breadth-first exploration of $G(D)$ analyzed on the *suppressed* multigraph $H(D)$ obtained by deleting cyclic components and suppressing degree-2 vertices, combined with a combinatorial switching argument to estimate the probability that a specific vertex $w$ is next explored (approximately proportional to $\deg w$). A preprocessing step quarantines high-degree "hub" vertices so concentration bounds on the open-edge count hold throughout the exploration; expected increase stays positive precisely while edges in the $R_D$ tail remain unexplored.

## Result
Theorems 1–2: for well-behaved $D$, $R_D \le \delta(n) M_D$ ($\delta \to 0$) implies no component of order $\gamma n$ w.h.p.; $R_D \ge \epsilon M_D$ implies a $\gamma(\epsilon)n$-component w.h.p. Theorem 6: when $M_D \le b$ constant, both giant/no-giant probabilities are bounded away from 0 and 1 (sequence genuinely indeterminate). The criterion subsumes Molloy–Reed (1995), Janson–Łuczak (2009), Bollobás–Riordan (2015), and Aiello–Chung–Lu power-law results as special cases (Theorems 37–38).

## Why it matters here
General background; no direct arena tie — this is extremal/probabilistic combinatorics on random graphs with prescribed degree sequence, not a configuration-optimization problem in the arena's current set. Could marginally inform any future problem touching extremal graph thresholds or degree-sequence constraints, but no current problem invokes giant-component phase transitions.

## Open questions / connections
- Quantitative dependence $\gamma(\epsilon)$ and $\gamma(\delta)$ for arbitrary degree sequences — precise constants known only under MR/JL/BR conditions.
- Order of the second-largest component and subcritical-regime size distribution for arbitrary $D$.
- Extending site/bond percolation, diameter, and $k$-core threshold results from restricted degree-sequence classes to arbitrary $D$ using the $R_D/M_D$ framework.

## Key terms
random graphs, configuration model, giant component, degree sequence, Molloy-Reed criterion, phase transition, scale-free networks, power-law degree distribution, switching argument, breadth-first exploration, suppression of degree-2 vertices, Aiello-Chung-Lu
