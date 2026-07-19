---
type: source
kind: paper
title: The maximum size of a non-trivial intersecting uniform family that is not a subfamily of the Hilton--Milner family
authors: Jie Han, Y. Kohayakawa
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1509.05464
source_local: ../raw/2015-han-maximum-size-non-trivial-intersecting.pdf
topic: general-knowledge
cites:
---

# The maximum size of a non-trivial intersecting uniform family that is not a subfamily of the Hilton--Milner family

**Authors:** Jie Han, Y. Kohayakawa  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1509.05464

## One-line
Determines the maximum size of a $k$-uniform intersecting family that is neither contained in the Erdős–Ko–Rado star $\mathcal{F}_0$ nor in the Hilton–Milner family $\mathcal{F}_1$, and classifies all extremal families for $k \geq 3$.

## Key claim
For $k \geq 3$, $n > 2k$, any intersecting $k$-uniform family $\mathcal{H}$ that is neither EKR nor HM (and not contained in $\mathcal{G}_2$ when $k=3$) satisfies $|\mathcal{H}| \leq \binom{n-1}{k-1} - \binom{n-k-1}{k-1} - \binom{n-k-2}{k-2} + 2$, with equality iff $\mathcal{H} \cong \mathcal{J}_2$ (or also $\mathcal{G}_2, \mathcal{G}_3$ when $k=4$).

## Method
Shifting technique à la Erdős–Ko–Rado / Frankl–Füredi, with a careful handling of the cases where standard shifts $S_{xy}$ would collapse the family into $\mathcal{F}_0$, $\mathcal{F}_1$, or $\mathcal{G}_2$. The authors freeze a small set $X_i$ of "obstruction" vertices and shift only outside it, then count traces $\mathcal{A}_i = \{E \cap Y : |E \cap Y| = i\}$ on a $\sim 2k$-vertex window. A "non-separability" lemma (via cross-intersecting partitions) proves stability of the shifts and hence uniqueness of extremal families.

## Result
Establishes the bound $\binom{n-1}{k-1} - \binom{n-k-1}{k-1} - \binom{n-k-2}{k-2} + 2$ (matches Hilton–Milner 1967 Theorem 3 at $s=2$, but sharper for $k=3$ and with full extremal characterization). Yields Corollary 1.7: for $k \geq 4$, if $d(\mathcal{H}) \leq d(\mathcal{J}_2)$ then $|\mathcal{H}| \leq |\mathcal{J}_2|$, with uniqueness for $k \geq 5$ — an EKR-type theorem with a maximum-degree condition extending Frankl 1987.

## Why it matters here
General background for extremal set theory / intersecting families; informs combinatorial-bound techniques (shifting, trace-counting, cross-intersecting non-separability) that may surface in extremal-graph / discrete-geometry arena problems but no direct arena tie to the current 23 problems.

## Open questions / connections
- Generalize to $t$-intersecting families ($t > 1$), starting from Ahlswede–Khachatrian.
- Next layer: max size of intersecting $\mathcal{H}$ that is also not contained in $\mathcal{J}_2$ (Kostochka–Mubayi 2016 answered for large $n$ — full $n,k$ open).
- Connects to Frankl's hierarchy by transversal number, and to the Jackowska–Polcyn–Ruciński Turán-number hierarchy.

## Key terms
Erdős–Ko–Rado theorem, Hilton–Milner theorem, intersecting family, shifting technique, $k$-uniform hypergraph, extremal set theory, cross-intersecting, non-separable family, stability, maximum degree, trace, Frankl, Füredi
