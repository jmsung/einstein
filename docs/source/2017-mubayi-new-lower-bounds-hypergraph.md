---
type: source
kind: paper
title: New lower bounds for hypergraph Ramsey numbers
authors: Dhruv Mubayi, Andrew Suk
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1702.05509v2
source_local: ../raw/2017-mubayi-new-lower-bounds-hypergraph.pdf
topic: general-knowledge
cites: 
---

# New lower bounds for hypergraph Ramsey numbers

**Authors:** Dhruv Mubayi, Andrew Suk  ·  **Year:** 2017  ·  **Source:** http://arxiv.org/abs/1702.05509v2

## One-line
Establishes new lower bounds for the off-diagonal 4-uniform hypergraph Ramsey numbers $r_4(5,n)$ and $r_4(6,n)$ via a refined Erdős–Hajnal stepping-up construction seeded from a graph (2-uniform) coloring.

## Key claim
For an absolute constant $c>0$: $r_4(5,n) > 2^{n^{c\log n}}$ and $r_4(6,n) > 2^{2^{cn^{1/5}}}$, improving the previous bests $2^{n^{c\log\log n}}$ and $2^{n^{c\log n}}$. The $r_4(6,n)$ bound is double-exponential in a power of $n$, matching the known tower growth rate of $r_k(k+2,n)$ for all $k\ge 5$ via stepping-up.

## Method
Variant of the Erdős–Hajnal stepping-up lemma: starting from a carefully constructed random 2-coloring $\varphi$ on the pairs of $\{0,\dots,N-1\}$ (with no monochromatic $K_{n,n}$ and no $n$-set avoiding the "bad" red-blue-blue triple pattern, via probabilistic method + partial Steiner $(n,3,2)$-systems), lift $\varphi$ to a 4-uniform coloring $\chi$ on $\{0,\dots,2^N-1\}$ using the binary-difference index $\delta(u,v)$. The red 4-tuple rules are chosen so monotone/zigzag $\delta$-sequences force structures in $\varphi$ that violate its random-construction properties.

## Result
$r_4(5,n) > 2^{n^{c\log n}}$ and $r_4(6,n) > 2^{2^{cn^{1/5}}}$ (Theorem 1.2). Stepping-up yields $r_k(k+1,n) > \mathrm{twr}_{k-2}(n^{c\log n})$ and $r_k(k+2,n) > \mathrm{twr}_{k-1}(cn^{1/5})$ for $k\ge 5$ (Corollary 1.3). Combined with the upper bound $r_k(k+2,n) < \mathrm{twr}_{k-1}(c'n^3\log n)$, the tower growth rate of $r_k(k+2,n)$ is now pinned down, almost settling the 1972 Erdős–Hajnal off-diagonal tower-growth question; only $r_4(5,n)$ being double-exponential in $n^c$ remains open (Conjecture 1.4).

## Why it matters here
General background; no direct arena tie — Einstein Arena problems concern continuous geometric/analytic optimization (sphere packings, autocorrelation, kissing) rather than off-diagonal hypergraph Ramsey numbers. The probabilistic random-coloring + partial Steiner system counting is a generic extremal-combinatorics tool, and the lower-bound construction philosophy ("lift a low-uniformity coloring via binary indices to enforce structure") is a transferable template if any arena problem reduces to a Ramsey-type pigeonhole.

## Open questions / connections
- Conjecture 1.4: prove $r_4(5,n) > 2^{2^{n^c}}$ — the last missing piece to determine tower growth of all off-diagonal $r_k(s,n)$.
- Conjecture 1.1 (Erdős): $r_3(n,n) > 2^{2^{cn}}$ — would propagate via stepping-up to diagonal $r_k(n,n)$ for all $k\ge 4$.
- Extends the Conlon–Fox–Sudakov line ($s\ge \lceil 5k/2\rceil-3$, then $s\ge k+3$) on the Erdős–Hajnal off-diagonal conjecture (2) down to $s=k+2$.

## Key terms
hypergraph Ramsey numbers, off-diagonal Ramsey, Erdős-Hajnal stepping-up lemma, $r_4(5,n)$, $r_4(6,n)$, tower function, probabilistic method, partial Steiner system, monochromatic $K_{n,n}$, Mubayi, Suk, Conlon-Fox-Sudakov
