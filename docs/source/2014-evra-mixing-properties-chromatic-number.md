---
type: source
kind: paper
title: Mixing Properties and the Chromatic Number of Ramanujan Complexes
authors: Shai Evra, Konstantin Golubev, A. Lubotzky
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1407.7700
source_local: ../raw/2014-evra-mixing-properties-chromatic-number.pdf
topic: general-knowledge
cites:
---

# Mixing Properties and the Chromatic Number of Ramanujan Complexes

**Authors:** Shai Evra, Konstantin Golubev, A. Lubotzky  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1407.7700

## One-line
Extends the Erdős/Lubotzky–Phillips–Sarnak "high-girth + high-chromatic-number" construction from Ramanujan graphs to high-dimensional Ramanujan complexes, via a "colorful mixing lemma" for $d$-partite quotients of Bruhat–Tits buildings.

## Key claim
For every $d\ge 3$ and odd prime power $q$, there exist $(d-1)$-dimensional simplicial complexes $X_n$ covered by $B_d(\mathbb{F}_q((t)))$ with injectivity radius $r(X_n) \ge \frac{\log_q |X_n|}{2(d-1)(d^2-1)} - \frac12$ and chromatic number $\chi(X_n) \ge \frac12 \cdot q^{1/(2d)}$, so $\chi \to \infty$ as $q\to\infty$ while locally the complex remains 2-colorable.

## Method
Reduce hypergraph discrepancy to spectral gaps of "vertex-vs-wall" bipartite graphs $B_i$ associated to each type $i\in \mathbb{Z}/d\mathbb{Z}$ in the building quotient, via an expander-mixing-lemma argument for biregular bipartite graphs. Bound the second eigenvalue of each $B_i$ using Hee Oh's quantitative property (T) / matrix-coefficient estimates for $\mathrm{PGL}_d$ over local fields, applied through Hecke operators $H_{(-1,0,\dots,0,1)}$. Apply the resulting Colorful Mixing Lemma to the $d$-partite cover of non-partite Ramanujan complexes built from Cartwright–Steger lattice congruence subgroups $\Lambda(f)$.

## Result
**Colorful Mixing Lemma:** for a type-preserving cocompact lattice $\Gamma \le \mathrm{PGL}_d(F)$ with injectivity radius $\ge 2$, and any $W_i \subseteq V_i$, $\left| \frac{|E(W_1,\dots,W_d)|}{|X(d-1)|} - \prod_{i=1}^d \frac{|W_i|}{|V_i|} \right| \le \frac{2d}{q^{1/2}}$. Pairing this with the choice $|W_i|/|V_i| \ge 1/\chi(X)$ at a monochromatic color class forces $\chi(X) \ge (2d)^{-1/d} q^{1/(2d)}$. The diameter satisfies $\mathrm{diam}(X_n) \le 8d \cdot r(X_n)$, so up to $\sim 1/(8d)$ of the diameter every ball is 2-colorable.

## Why it matters here
General background; no direct arena tie. Closest contact is to extremal-graph / hypergraph chromatic-number techniques and to high-dimensional expander constructions — useful framing if any arena problem reduces to coloring a structured hypergraph or to discrepancy of simplicial covers. Adds an explicit constructive lower bound machinery (building quotients + Oh's bounds) absent from current wiki coverage on Ramanujan graphs.

## Open questions / connections
- Can the $q^{1/(2d)}$ exponent be improved using full Ramanujan bounds (LSV) rather than only Oh's property-(T) estimate?
- Extends Erdős 1959 (probabilistic), Lovász 1968 (constructive), LPS 1988 (Ramanujan-graph explicit) to dimension $\ge 2$ — what is the right notion of "girth" for clique complexes (compare Lubotzky–Meshulam vs Goff)?
- Does the colorful mixing lemma yield bounds on other extremal invariants (independence number, cover number, fractional chromatic) of building quotients?

## Key terms
Ramanujan complexes, Bruhat–Tits building, chromatic number, hypergraph discrepancy, expander mixing lemma, Cartwright–Steger lattice, property (T), Hee Oh matrix coefficients, $\mathrm{PGL}_d$ local field, Hecke operators, Lubotzky–Phillips–Sarnak, high-dimensional expanders, congruence subgroups, non-partite simplicial complex, injectivity radius
