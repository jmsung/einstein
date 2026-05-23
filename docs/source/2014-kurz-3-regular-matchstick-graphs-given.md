---
type: source
kind: paper
title: 3-regular matchstick graphs with given girth
authors: Sascha Kurz, G. Mazzuoccolo
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1401.4360
source_local: ../raw/2014-kurz-3-regular-matchstick-graphs-given.pdf
topic: general-knowledge
cites:
---

# 3-regular matchstick graphs with given girth

**Authors:** Sascha Kurz, G. Mazzuoccolo  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1401.4360

## One-line
Determines the minimum vertex count for complete 3-regular planar matchstick graphs (unit-length straight-edge planar embeddings) with prescribed girth $g \in \{4,5\}$.

## Key claim
For girth $g=4$: a complete 3-regular matchstick graph on $n$ vertices exists iff $n$ is even and $n \geq 20$. For $g=5$: an explicit example exists on $n=180$ vertices, with lower bound $n \geq 30$. For $g \geq 6$: no finite example exists (Euler formula).

## Method
Combines the Euler polyhedron formula (yielding $3A_3 + 2A_4 + A_5 - A_7 - 2A_8 - \cdots = 12 - 2\tau$ for $r=3$) with area/perimeter inequalities on equilateral $k$-gons: $A_{\max}(k) = \frac{k}{4}\cot(\pi/k)$ for the regular case, plus Böröczky–Kertész–Makai bounds $A_{\min}(r) = \sqrt{3}/4$ for odd $r$ and $0$ for even $r \geq 4$. Combined with a neighbor-angle lemma ($\alpha+\beta > \pi/2$ in equilateral $k$-gons) and exhaustive enumeration via `plantri` of 3-connected planar graphs with $n \leq 18$, eliminates all smaller candidate graphs.

## Result
Theorem 3.10 establishes $n \geq 20$ for $g=4$, matched by an explicit 20-vertex construction (Fig. 5) built by joining two 10-vertex non-convex hexagonal subconfigurations. Arbitrarily large families are constructed via quadrangle chains, giving all even $n \geq 20$. The 180-vertex girth-5 example demonstrates existence; the lower bound $n \geq 30$ follows from $A_5 \geq 16$ and $k \geq 10$ via repeated area argument.

## Why it matters here
General background on rigid planar unit-distance embeddings — connects to discrete geometry problems where edge-length constraints meet planarity (relevant framing for kissing-number/contact-graph problems where contact = unit distance). The "$A_{\max}(k) = \frac{k}{4}\cot(\pi/k)$" area bound and the parity-based $A_{\min}$ result are reusable lemmas for any equilateral-polygon area argument.

## Open questions / connections
- No known general algorithm to decide whether a given planar graph is a matchstick graph (NP-hard per Cabello–Demaine–Rote, Eades–Wormald).
- Determining the minimum $n$ for girth-5 complete 3-regular matchstick graphs remains open (180 upper bound, 30 lower).
- Extends to the broader Harborth-style program: the 4-regular case (Harborth graph, $n=52$) is still the minimal-known and unproven; the 5-regular case was ruled out by Kurz–Pinchasi 2011.

## Key terms
matchstick graph, unit-distance graph, 3-regular planar graph, girth, Euler polyhedron formula, equilateral polygon area, Harborth graph, Böröczky-Kertész-Makai, plantri enumeration, rigid graph realization, edge-length-constrained embedding, discrete geometry
