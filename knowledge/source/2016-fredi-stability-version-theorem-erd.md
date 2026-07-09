---
type: source
kind: paper
title: A stability version for a theorem of Erdős on nonhamiltonian graphs
authors: Z. Füredi, A. Kostochka, Ruth Luo
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1608.05741
source_local: ../raw/2016-fredi-stability-version-theorem-erd.pdf
topic: general-knowledge
cites:
---

# A stability version for a theorem of Erdős on nonhamiltonian graphs

**Authors:** Z. Füredi, A. Kostochka, Ruth Luo  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1608.05741

## One-line
Proves a stability refinement of Erdős's edge-maximum theorem for nonhamiltonian graphs: any 2-connected nonhamiltonian $n$-vertex graph with $\delta(G)\ge d$ and more than $e(n,d+1)$ edges must be a subgraph of one of two explicit extremal graphs.

## Key claim
For $n\ge 3$, $d\le \frac{n-1}{2}$, if $G$ is nonhamiltonian with $\delta(G)\ge d$ and $e(G) > e(n,d+1) = \max\{h(n,d+1), h(n,\frac{n-1}{2})\}$ where $h(n,d) = \binom{n-d}{2}+d^2$, then $G\subseteq H_{n,d}$ or $G\subseteq H'_{n,d}$. The gap $e(n,d)-e(n,d+1) = n-3d-2 \ge n/2$ for $d < d_0(n)-1$, giving a wide stability window.

## Method
Classical extremal-graph saturation argument plus two lemmas built on Pósa's theorems. Lemma 6 uses Ore-type degree-sum constraints on saturated nonhamiltonian graphs to force a structural decomposition: a set $D$ of $k\le \frac{n-1}{2}$ low-degree vertices with $G-D$ complete. Lemma 7 then applies Pósa's hamilton-cycle-with-prescribed-edges theorem to pin $G$ down to $H_{n,d}$ or $H'_{n,d}$.

## Result
Establishes the stability theorem (Theorem 3): in the regime $d < d_0(n) \approx n/6$, the only near-extremal 2-connected nonhamiltonian graphs are subgraphs of Erdős's sharpness example $H_{n,d}$ (a $K_{n-d}$ with $d$ extra vertices each adjacent to the same $d$-set in $A$) or $H'_{n,d}$ (edge-disjoint union of $K_{n-d}$ and $K_{d+1}$ sharing one vertex). The bound $e(H'_{n,d}) > e(n,d+1)$ only holds when $d = O(\sqrt{n})$.

## Why it matters here
General background; no direct arena tie. Extremal/Turán-type stability results on hamiltonicity are tangential to the current Einstein Arena problem set (sphere packing, autocorrelation, kissing, discrete geometry), though Pósa-type degree-sum techniques and saturation arguments are reusable templates for extremal-graph problems if one appears.

## Open questions / connections
- Extends Erdős (1962) and Ore (1959); independently proved by Li–Ning (2016) via spectral methods — comparing the proof techniques may yield a unified stability framework.
- Whether the 2-connectivity hypothesis can be relaxed in the stability conclusion.
- Analogous stability versions for related hamiltonicity bounds (Moon–Moser, Chvátal–Erdős).

## Key terms
nonhamiltonian graphs, stability theorem, Erdős, Pósa, Ore, Dirac, hamiltonian cycle, minimum degree, extremal graph theory, Turán-type bound, saturated graph, edge maximization
