---
type: source
kind: paper
title: A Crossing Lemma for Multigraphs
authors: J. Pach, G. Tóth
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1801.00721
source_local: ../raw/2018-pach-crossing-lemma-multigraphs.pdf
topic: general-knowledge
cites:
---

# A Crossing Lemma for Multigraphs

**Authors:** J. Pach, G. Tóth  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1801.00721

## One-line
Proves the classical Crossing Lemma bound $\text{cr}(G) \geq c\, e^3/n^2$ extends to multigraphs once the drawing is "branching" — every lens between parallel edges contains a vertex — eliminating Székely's dependence on edge multiplicity $m$.

## Key claim
For any branching topological multigraph $G$ with $n$ vertices and $e > 4n$ edges, $\text{cr}_{\text{br}}(G) \geq c\, e^3/n^2$ with absolute constant $c > 10^{-7}$, settling a conjecture of Kaufmann. Compare Székely's earlier $c\, e^3/(mn^2)$, which degrades with multiplicity.

## Method
Three-pronged argument: (1) Theorem 3 — a Davenport-Schinzel order-2 sequence argument bounds edges in any crossing-free branching multigraph by $n(n-2)$; (2) Theorem 2 — bisection-width-vs-crossings inequality $b_{\text{br}}(G) \leq 22\sqrt{c(G) + \sum d_i^2} + n$, proved via the Alon-Seymour-Thomas planar separator applied to a vertex-replacement gadget (each vertex $v_i$ replaced by a $d_i \times d_i$ grid), with careful local curve modifications to preserve the branching property in both halves; (3) recursive decomposition driving a contradiction against (1).

## Result
$\text{cr}_{\text{br}}(G) \geq c\, e^3/n^2$ for $c > 10^{-7}$ whenever $e > 4n$ in a branching drawing (no two adjacent edges cross; independent edges cross at most once; every parallel-edge lens contains a vertex on each side). Theorem 3's edge bound $e \leq n(n-2)$ is tight (sphere construction: $n$-gon equator + Northern/Southern half-circles). Conditions (ii)–(iii) are necessary: a tripartite construction with $e = (n/3)^3$ edges and only $\sim n^6/3^7$ crossings shows the bound fails if edges may cross multiply.

## Why it matters here
General background; no direct arena tie. Most relevant as methodology — the bisection-width recursion with branching-preservation invariants is a template for extremal arguments where the "good drawing" property is non-hereditary, which is a recurring obstacle pattern in discrete geometry problems (e.g., contact-graph reasoning in packing problems like P11).

## Open questions / connections
- Extends Ajtai–Chvátal–Newborn–Szemerédi / Leighton (1982) and Székely (1997); resolves Kaufmann's branching-multigraph conjecture.
- Constant $c > 10^{-7}$ is loose vs the simple-graph Crossing Lemma constant $1/64$ — can the branching constant be pushed close to $1/64$?
- Conditions (ii)/(iii) (adjacent edges no-cross, independent edges $\leq 1$ crossing) are necessary as stated — what bound holds for $k$-quasi-planar branching multigraphs?

## Key terms
Crossing Lemma, branching topological multigraph, branching bisection width, Davenport-Schinzel sequence order 2, Alon-Seymour-Thomas planar separator, edge multiplicity, lens, Pach, Tóth, Székely, Kaufmann conjecture, Szemerédi-Trotter, non-hereditary property, recursive decomposition
