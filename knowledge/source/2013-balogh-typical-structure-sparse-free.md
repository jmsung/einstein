---
type: source
kind: paper
title: The typical structure of sparse $K_{r+1}$-free graphs
authors: J. Balogh, R. Morris, Wojciech Samotij, L. Warnke
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1307.5967
source_local: ../raw/2013-balogh-typical-structure-sparse-free.pdf
topic: general-knowledge
cites:
---

# The typical structure of sparse $K_{r+1}$-free graphs

**Authors:** J. Balogh, R. Morris, Wojciech Samotij, L. Warnke  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1307.5967

## One-line
Pins down the sharp edge-count threshold $m_r$ at which a typical $K_{r+1}$-free graph on $n$ vertices flips from non-$r$-partite to $r$-partite, for every $r \geq 2$.

## Key claim
For each $r \geq 2$ there is an explicit constant $\theta_r$ and threshold $m_r = \theta_r n^{2-2/(r+2)} (\log n)^{1/(\binom{r+1}{2}-1)}$ such that, for any $\varepsilon>0$: if $m \geq (1+\varepsilon)m_r$, almost all $K_{r+1}$-free $n$-vertex graphs with $m$ edges are $r$-partite; if $(1+\varepsilon)d_r \leq m \leq (1-\varepsilon)m_r$ (with $d_r=\Theta(n)$ the $r$-colorability threshold), almost none are.

## Method
Two-sided enumeration. The 0-statement counts graphs that are $r$-colorable except for one monochromatic edge using the Hypergeometric FKG inequality, showing they outnumber properly $r$-colored graphs below $m_r$. The 1-statement splits above $m_r$ into a sparse case (using the KŁR conjecture / hypergraph containers via Balogh-Morris-Samotij and Saxton-Thomason, plus a delicate Hypergeometric Janson inequality argument on low-degree vs. high-degree monochromatic edge distributions) and an easier dense case ($m > \mathrm{ex}(n,K_{r+1}) - \xi n^2$) handled by matching/density bounds.

## Result
Theorem 1.1 establishes the double sharp threshold at $m_r$ for all $r \geq 3$ (the $r=2$ case follows as the property of being bipartite lacks a sharp threshold in $G_{n,m}$). The critical exponent $2 - 2/(r+2)$ and log power $1/(\binom{r+1}{2}-1)$ arise from balancing the count of monochromatic-edge $K_{r+1}^-$ avoidance probabilities against the $\binom{e(\Pi)}{m}$ baseline. Generalizes Kolaitis–Prömel–Rothschild (dense regime) and Osthus–Prömel–Taraz ($r=2$).

## Why it matters here
General background; no direct arena tie. Demonstrates the "hypergraph containers + Janson + FKG" enumeration toolkit for proving sharp structural thresholds in sparse extremal combinatorics, which is relevant methodology if any arena problem reduces to counting/structure of $H$-free objects.

## Open questions / connections
- Conjecture 1.3: extend the sharp threshold to all strictly 2-balanced edge-color-critical $H$, with threshold $C n^{2-1/m_2(H)}(\log n)^{1/(e(H)-1)}$.
- Generalize to color-critical-vertex graphs (Hundack–Prömel–Steger regime) where typical structure admits bounded-degree non-monochromatic parts.
- Hypergraph analogues remain mostly open beyond a few specific 3-uniform cases (Fano plane, triangle-free triple systems).

## Key terms
$K_{r+1}$-free graphs, Turán number, sharp threshold, $r$-partite, Kolaitis-Prömel-Rothschild, hypergraph containers, KŁR conjecture, Janson inequality, FKG inequality, Erdős-Simonovits stability, sparse random analogue, Balogh-Morris-Samotij
