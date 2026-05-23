---
type: source
kind: paper
title: On the number of edges of separated multigraphs
authors: Jacob Fox, Janos Pach, Andrew Suk
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2108.11290v2
source_local: ../raw/2021-fox-number-edges-separated-multigraphs.pdf
topic: general-knowledge
cites: 
---

# On the number of edges of separated multigraphs

**Authors:** Jacob Fox, Janos Pach, Andrew Suk  ·  **Year:** 2021  ·  **Source:** http://arxiv.org/abs/2108.11290v2

## One-line
Proves an $O(n^2 \log n)$ edge bound for separated single-crossing topological multigraphs, yielding a strengthened crossing lemma whose bound is independent of edge multiplicity.

## Key claim
**Theorem 1.2:** Any separated single-crossing topological multigraph $G$ on $n$ vertices satisfies $|E(G)| \leq 64 n^2 \log n$. **Corollary 1.3:** If such a $G$ has $e \geq 4n$ edges, then $\operatorname{cr}(G) \geq 10^{-25} \, e^3 / (n^2 \log(e/n))$, settling a question of Kaufmann et al. up to the logarithmic factor (the naive separated bound was $O(n^3)$).

## Method
Probabilistic crossing-lemma argument adapted to lenses: bucket lenses by interior-vertex count into $\log n$ dyadic classes, pigeonhole to a heavy class $L_k$, pin a vertex $v$ contained in $\geq |L_k| 2^{k-1}/n$ lenses, then random-sample vertices with probability $p = 2^{-k}$ so the surviving "empty lenses through $v$" yield a simple topological graph $G'$. A Hanani–Tutte / bipartite-planarity lemma (Lemma 2.1) forces $|E(G')| \leq 4n$ because every two independent edges of $G'$ must cross (Lemma 2.2 uses the single-crossing hypothesis and the shared origin), closing the inequality. Corollary 1.3 then plugs Theorem 1.2 into the Pach–Tóth bisection-width recursion ([11], [5]).

## Result
Edge count tight up to $\log n$: a construction with semicircle pairs on collinear vertices achieves $\Omega(n^3)$ edges when edges may cross twice, showing single-crossing is essential. The crossing-number corollary $\operatorname{cr}(G) = \Omega(e^3 / (n^2 \log(e/n)))$ matches the classical Ajtai–Chvátal–Newborn–Szemerédi–Leighton bound up to a $\log(e/n)$ slack and is independent of the maximum multiplicity $m$ (unlike Székely's $e^3/(mn^2)$).

## Why it matters here
General background; no direct arena tie — separated multigraph theory is a discrete-geometry/extremal-topological-graph result that lives adjacent to incidence-bound and crossing-lemma machinery used in P12-style discrete-geometry problems but does not directly inform the current arena problem set.

## Open questions / connections
- Close the $\log n$ gap: is the true bound $O(n^2)$, as conjectured in Kaufmann–Pach–Tóth–Ueckerdt [5]?
- Extends Pach–Tóth [11] (multigraph crossing lemma) and Kaufmann et al. [5] (no-empty-lens multigraphs); related to Pach–Tardos–Tóth [12] on non-homotopic edges.
- Does an analogous bound hold for $k$-crossing topological multigraphs under a generalized "lens contains $\geq k{-}1$ vertices" condition, or only at $k=1$?

## Key terms
crossing lemma, separated multigraph, single-crossing topological graph, lens, Hanani-Tutte theorem, bisection width, Lipton-Tarjan separator, Pach-Tóth, Székely, Ajtai-Chvátal-Newborn-Szemerédi, multiplicity-independent crossing bound, extremal topological graph theory
