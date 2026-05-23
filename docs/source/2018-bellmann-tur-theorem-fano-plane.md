---
type: source
kind: paper
title: Turán’s Theorem for the Fano Plane
authors: L. Bellmann, Christian Reiher
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1804.07673
source_local: ../raw/2018-bellmann-tur-theorem-fano-plane.pdf
topic: general-knowledge
cites:
---

# Turán's Theorem for the Fano Plane

**Authors:** L. Bellmann, Christian Reiher  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1804.07673

## One-line
Complete resolution of Sós's conjecture: the exact maximum number of edges in a 3-uniform hypergraph on $n \geq 7$ vertices with no Fano-plane subhypergraph, plus uniqueness of the extremal configuration.

## Key claim
For every $n \geq 7$, $\mathrm{ex}(n, F) = b(n) = \lfloor n^2/4 \rfloor \cdot \lfloor (n-2)/2 \rfloor$, where $F$ is the Fano plane and $b(n)$ counts edges of the balanced complete bipartite 3-graph $B_n$. For $n \geq 8$ the extremal hypergraph is uniquely $B_n$; for $n = 7$ there are exactly two extremal examples ($B_7$ and $J_7 = K_7^{(3)}$ minus the 5 edges through a fixed pair).

## Method
Induction on $n$ via the **link multigraph method** of de Caen–Füredi, combined with new extremal results on $p$-multigraphs avoiding "three crossing pairs." The proof splits by parity of $n$, exploits Füredi–Simonovits's exact value $f_4(n) = 2\binom{n}{2} + 2\lfloor n^2/4 \rfloor$, and proves a new upper bound $f_5(n) \leq \tfrac{1}{4}(7n^2 - n)$. Auxiliary lemmas characterize $B_n$ inductively from local structure (tetrahedron deletions yielding $B_{n-4}$) and forbid 5-cliques $K_5^{(3)}$ in any extremal $H$.

## Result
Resolves $\mathrm{ex}(n, F) = b(n)$ for *all* $n \geq 7$ — not just large $n$ as in Füredi–Simonovits (2005) and Keevash–Sudakov (2005), whose stability-method proofs required $n \gtrsim 10^{100}$ to $10^{900}$. The Turán density $\pi(F) = 3/4$ was known since de Caen–Füredi (2000); this paper closes the exact-Turán problem and proves uniqueness. Key technical bound: $f_5(n) \leq (7n^2-n)/4$.

## Why it matters here
General background for extremal-hypergraph / Turán-type problems; no direct Einstein Arena problem currently maps to forbidden-Fano-plane density. Closest tie is to extremal_graph / combinatorics-flavored problems where link-graph and multigraph counting techniques transfer. Adds a worked example of "induction + link multigraph + multigraph Turán sub-problem" composition pattern, distinct from flag-algebra and Cohn–Elkies LP techniques already in the wiki.

## Open questions / connections
- Exact value of $f_5(n)$: the paper conjectures equality in $f_5(n) = \max(5\lfloor n^2/3 \rfloor / \ldots, 2\binom{n}{2} + 3\lfloor n^2/4 \rfloor)$ but only proves the weaker bound needed here.
- Tetrahedron Turán density $\pi(K_4^{(3)}) \in [5/9, 0.5616]$ remains open — Razborov flag-algebra upper bound vs Turán's construction conjectured optimal; non-uniqueness of extremal configurations is the suspected obstruction.
- Stability versions (Füredi–Simonovits, Keevash–Sudakov) remain stronger in the "almost extremal" regime — this paper does not supersede them.

## Key terms
Turán hypergraph problem, Fano plane, 3-uniform hypergraph, extremal hypergraph, balanced complete bipartite hypergraph, link multigraph method, three crossing pairs, Pasch hypergraph, Sós conjecture, de Caen–Füredi, Füredi–Simonovits, Keevash–Sudakov, tetrahedron $K_4^{(3)}$, flag algebras, Turán density
