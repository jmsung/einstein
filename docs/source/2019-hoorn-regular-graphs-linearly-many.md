---
type: source
kind: paper
title: Regular graphs with linearly many triangles
authors: P. Hoorn, Gábor Lippner, Elchanan Mossel
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1904.02212
source_local: ../raw/2019-hoorn-regular-graphs-linearly-many.pdf
topic: general-knowledge
cites:
---

# Regular graphs with linearly many triangles

**Authors:** P. Hoorn, Gábor Lippner, Elchanan Mossel  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1904.02212

## One-line
Determines the exact log-asymptotic count of $d$-regular graphs on $n$ nodes with at least a constant fraction $c$ of the maximum possible triangles, and proves that almost all such graphs are structured: a union of (pseudo-)cliques plus an almost triangle-free part.

## Key claim
For fixed $0 < c < 1$ and $d = o(n)$ with $\log d = o(\log n)$:
$$\lim_{n\to\infty} \frac{\log |G_{d,c}(n)|}{\log |G_d(n)|} = 1 - c \cdot \frac{d-1}{d+1},$$
confirming the 2002 Collet–Eckmann conjecture. Structurally, with high probability a uniform random graph in $G_{d,c}(n)$ has $o(n)$ "bad" nodes — for fixed $d$, $<\log n / \log\log\log n$ bad nodes — so almost all triangles sit inside disjoint $(d{+}1)$-cliques (fixed $d$) or disjoint pseudo-cliques of size $d + o(d)$ (growing $d$).

## Method
Configuration-model edge-revealing argument: order edges of a labeled $d$-regular graph in a configuration order and record a binary profile $\phi(G) \in \{0,1\}^{nd/2}$ marking which edges create a new triangle when added. An upper bound counts graphs with a given profile via $|\phi^{-1}(x)| \le (dn)^{dn/2}(d^2/n)^{|x|}$; a random-relabeling Markov argument shows a constant fraction of orbit elements lie in the high-profile set. The matching lower bound is constructive: take $b = cn/(d{+}1)$ disjoint $K_{d+1}$'s plus a uniform $d$-regular graph on the remaining $(1{-}c)n$ vertices.

## Result
Sharp bound (up to $O(1/\log(n/d))$): $\log|G_{d,c}(n)| = (1 - c\tfrac{d-1}{d+1}) \cdot \tfrac{dn}{2}\log\tfrac{n}{d+1} + O(dn)$. Structural theorem (growing $d$): almost all triangles concentrate in $(1+O(\delta))cn/d$ pairwise-disjoint pseudo-cliques, where $\delta = (3c)^{1/3}(\log d / \log(n/d^2))^{1/4}$. Extends verbatim to $k$-cliques: same rate function with $K_k$-counts replacing triangles.

## Why it matters here
General background; no direct arena tie. Relevant tangentially to extremal-graph problems if any arise (e.g., density-constrained regular graphs) — the technique of "configuration ordering + reveal profile + random relabeling" is a clean combinatorial alternative to entropy/variational large-deviation machinery and could inform counting arguments for clique-rich configurations.

## Open questions / connections
- Sharp logarithmic rate for $d$ polynomial in $n$ (the $\log d / \log(n/d)$ error term is not $o(1)$ here).
- Extends Collet–Eckmann (2002) and complements Chatterjee–Varadhan / Chatterjee–Dembo / Lubetzky–Zhao variational approaches for $G(n,p)$ upper-tail triangle counts.
- Connection to Krioukov's "clustering implies geometry" — does the clique-cluster structure persist under additional global constraints (degree distribution, diameter)?

## Key terms
regular graphs, triangle count, upper tail large deviations, configuration model, Collet–Eckmann conjecture, pseudo-clique, extremal graph theory, Erdős–Rényi, entropy maximization, clique density, random regular graph, Lubetzky–Zhao
