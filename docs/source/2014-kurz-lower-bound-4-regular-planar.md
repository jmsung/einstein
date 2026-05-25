---
type: source
kind: paper
title: A lower bound for 4-regular planar unit distance graphs
authors: Sascha Kurz
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1401.4377
source_local: ../raw/2014-kurz-lower-bound-4-regular-planar.pdf
topic: general-knowledge
cites:
---

# A lower bound for 4-regular planar unit distance graphs

**Authors:** Sascha Kurz  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1401.4377

## One-line
Exhaustive computer search establishes that any 4-regular planar unit distance graph (matchstick graph) must have at least 34 vertices, narrowing the gap to the known Harborth graph upper bound of 52.

## Key claim
Every 4-regular matchstick graph has $n \geq 34$ vertices (Theorem 13), improving prior lower bounds and tightening the long-standing $[?, 52]$ range for the minimum-vertex 4-regular planar unit distance graph.

## Method
Combines structural graph theory (Euler's formula, area arguments, parity of the boundary defect $\tau$) with exhaustive enumeration via the `plantri` program for 3-connected planar 4-regular graphs up to 33 vertices, plus a recursive face-addition algorithm pruned by necessary unit-distance criteria. A connectivity reduction (Lemma 5) shows non-3-connected candidates decompose into smaller "incomplete" matchstick graphs $M_\tau$ with $\tau \in \{2,4\}$, whose minimum sizes are bounded separately.

## Result
For incomplete 4-regular matchstick graphs: $n(M_0) \geq 16$, $n(M_2) \geq 17$, $n(M_4) \geq 17$ (with $n(M_4) \leq 20$ exhibited). The connectivity lemma gives $n(M) \geq \min(2 n(M_2), 2 n(M_4)+2) = 34$ when $M$ is not 3-connected; computer search excludes 3-connected cases up to 33 vertices, yielding the 34-vertex bound. Also derives $f_4(k) \leq k^4/4 + 2k^2/3 - 2$ for max inner vertices given outer-face size $k$.

## Why it matters here
General background on extremal discrete geometry / unit-distance graph problems; not directly tied to current Einstein Arena problems but illustrates the area-argument + Euler-formula technique used across packing/extremal problems, and demonstrates how exhaustive enumeration of planar graph families with necessary geometric pruning can close lower-bound gaps.

## Open questions / connections
- Exact values of $n(M_2)$ and $n(M_4)$ remain open (bounds $17 \leq n(M_4) \leq 20$).
- Is $f_4(k)$ (max inner vertices for given outer face $k$) bounded, and does it match the $O(k^4)$ upper bound — contrast with 3-regular case where $f_3(k)$ is unbounded for $k \geq 6$.
- Gap between lower bound 34 and Harborth's 52-vertex construction remains wide; can either bound be improved?

## Key terms
matchstick graph, unit distance graph, 4-regular planar graph, Harborth graph, Euler's formula, area argument, planar embedding, exhaustive enumeration, plantri, extremal combinatorics, discrete geometry, connectivity decomposition
