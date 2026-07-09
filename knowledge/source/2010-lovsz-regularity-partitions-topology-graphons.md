---
type: source
kind: paper
title: Regularity partitions and the topology of graphons
authors: László Lovász, Balázs Szegedy
year: 2010
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1002.4377v1
source_local: ../raw/2010-lovsz-regularity-partitions-topology-graphons.pdf
topic: general-knowledge
cites: 
---

# Regularity partitions and the topology of graphons

**Authors:** László Lovász, Balázs Szegedy  ·  **Year:** 2010  ·  **Source:** http://arxiv.org/abs/1002.4377v1

## One-line
Shows that graphons carry a canonical metric topology on their underlying point set, and that combinatorial constraints (excluded induced sub-bigraphs) force this topology to be compact and finite-dimensional — yielding polynomial-size regularity partitions.

## Key claim
If a graphon $(J,W)$ excludes some bigraph $F$ as an induced sub-bigraph (i.e., is "thin"), then $W$ is $\{0,1\}$-valued a.e., $J$ is compact, and its packing dimension is at most $10|F|$; consequently such graphons admit weak regularity partitions with $O(\varepsilon^{-10|V(F)|})$ classes and ultra-strong partitions with $O(\varepsilon^{-10|V(F)|^2})$ classes — polynomial in $1/\varepsilon$ rather than tower-type.

## Method
Two metrics are placed on $J$: the neighborhood distance $r_W(x,y) = \|W(x,\cdot) - W(y,\cdot)\|_1$ and the similarity distance $r_{W \circ W}$ via the operator square. "Pure" graphons are introduced as the canonical complete-separable-metric representatives (unique up to isometry among weakly isomorphic graphons). The thinness-implies-finite-dimension proof routes through Vapnik–Chervonenkis dimension: thinness bounds the DE-dimension of the support family $\{\mathrm{supp}\,W(x,\cdot)\}$, then Sauer–Shelah plus Komlós–Pach–Woeginger $\varepsilon$-net bounds give polynomial packing.

## Result
(i) Every graphon is weakly isomorphic to a unique pure graphon up to isometry. (ii) $(J, r_{W \circ W})$ is always compact and metrizes the weak topology; $(J, r_W)$ may be strictly finer ("compact graphons" are those where both topologies coincide). (iii) Voronoi cells of an average $\varepsilon$-net in $(J, r_{W \circ W})$ form a weak regularity partition with error $\leq 8\sqrt{\varepsilon}$, and conversely. (iv) Thin graphons have polynomial $L^1$-complexity; the polynomial bound on partition size avoids the tower-of-twos in Szemerédi/Alon–Fischer–Krivelevich–M. Szegedy. (v) Random-free hereditary graph properties yield compact finite-dim closures via a bigraph $F$ with $tb(F,W)=0$.

## Why it matters here
General background; no direct arena tie. The paper's tools — VC-dimension bounding combinatorial complexity, polynomial-size regularity for "structured" extremal classes, $L^\infty$ weak-$*$ compactness via $r_{W \circ W}$ — are the analytic substrate for Problem 8 (Borgs–Chayes–Lovász moment uniqueness) and Problem 9 (Lovász very-large-graphs), and they connect to extremal-graph problems where flag-algebra/SDP bounds and finitely-forcible graphons appear.

## Open questions / connections
- Conjecture 5.11: every nonempty subgraph-density extremal class contains a graphon of polynomial $L^1$-complexity — i.e., extremal solutions are finite-dimensional. Open across extremal combinatorics.
- The "essential discontinuity" set of a pure $W$ (Remark 3.5) — combinatorial meaning unknown.
- Whether the $10|F|$ packing-dimension bound is tight (Remark 4.2 is upper-only).
- Extends Lovász–Szegedy "Szemerédi's Lemma for the analyst" (2007) and connects to Lovász–Sós generalized quasirandom graphs and Borgs–Chayes–Lovász finitely forcible graphons.

## Key terms
graphon, regularity lemma, Szemerédi partition, weak regularity partition, similarity distance, neighborhood distance, packing dimension, VC-dimension, Sauer-Shelah, thin graphon, finitely forcible, hereditary property, Lovász, Szegedy, Vapnik-Chervonenkis
