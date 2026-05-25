---
type: source
kind: paper
title: On the Caccetta-Haggkvist conjecture with forbidden subgraphs
authors: Alexander Razborov
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1107.2247v2
source_local: ../raw/2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra.pdf
topic: general-knowledge
cites: 
---

# On the Caccetta-Haggkvist conjecture with forbidden subgraphs

**Authors:** Alexander Razborov  ·  **Year:** 2011  ·  **Source:** http://arxiv.org/abs/1107.2247v2

## One-line
Proves the $\ell=3$ Caccetta–Häggkvist conjecture for $C_3$-free oriented graphs that additionally avoid (as induced subgraphs) any of three specific 4-vertex orgraphs — In-Pendant, Out-Pendant, or Twisted Circle — which are missing from every known extremal configuration.

## Key claim
**Theorem 3.1:** Every $C_3$-free orgraph $\Gamma$ on $n$ vertices that contains no induced copy of the In-Pendant, Out-Pendant, or Twisted Circle has a vertex of out-degree $\le \lfloor (n-1)/3 \rfloor$. The induced restriction can be lifted at the cost of enlarging the forbidden family to six 5-vertex orgraphs (Theorem 3.2).

## Method
Flag-algebra-flavored argument restricted to finite objects: critical edges (minimum-outdegree out-neighbor) are introduced, and structural claims (Claims 5.1–5.5) force critical 2-paths $u \to v \to w$ to have specific local profiles. The crux (Claim 5.6) is a single density inequality $\alpha(u)+\alpha(v)+\alpha(w)+\Delta \le 1$ proved by case analysis over a random vertex $x$; summing along a cycle of critical edges cancels the cross terms and forces some $\alpha(v_i) \le 1/3$. Notably no Cauchy–Schwarz / SDP multiplicative structure is used — a "compromise" flag-algebra style.

## Result
For all $C_3$-free orgraphs avoiding the three induced 4-vertex obstructions, $\min_v d^+_\Gamma(v) \le (n-1)/3$, matching the conjectured CH bound exactly (not just asymptotically). The three forbidden orgraphs are absent in the full lexicographic-product family $\Gamma_{CH}$ (Claim 2.2), so the result covers all currently conjectured extremal configurations. Best general asymptotic bound at the time was $c \le 0.3465$ (Hladký–Král'–Norine 2009).

## Why it matters here
General background for extremal-graph / discrete-geometry style flag-algebra arguments; demonstrates the "forbidden-induced-subgraph + induction on $n$ + critical-edge averaging" template that the wiki's Razborov persona embodies. No direct Einstein Arena problem tie, but informs methodology for any extremal-density problem solvable via flag algebras without the full SDP machinery.

## Open questions / connections
- Can any one of the three forbidden 4-vertex orgraphs be removed from the hypothesis? Razborov reports trying and failing for all three.
- Lichiardopol (2012, added in proof) settled the independence-number-2 case unconditionally — a strictly stronger statement on that subclass.
- Extends Bondy [Bon97] (counting subgraphs approach) and parallels Razborov's own program on Turán $(3,4)$ [Raz10, Raz11]; companion to Lovász's local Sidorenko work [Lov10].
- Chudnovsky–Seymour (2006, unpublished) had the out-regular case for missing $C_3, I_3$; Seymour the $C_3, K_{2,1}$ case — leaves open the non-out-regular $C_3, I_3$ case.

## Key terms
Caccetta-Häggkvist conjecture, oriented graph, girth, minimum out-degree, $C_3$-free digraph, flag algebra, Razborov, induced subgraph, extremal configuration, lexicographic product, critical edge, In-Pendant Out-Pendant Twisted Circle, directed triangle, Bondy, Lichiardopol, extremal combinatorics
