---
type: source
kind: paper
title: Hedgehogs are not colour blind
authors: D. Conlon, J. Fox, V. Rodl
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1511.00563
source_local: ../raw/2015-conlon-hedgehogs-not-colour-blind.pdf
topic: general-knowledge
cites:
---

# Hedgehogs are not colour blind

**Authors:** D. Conlon, J. Fox, V. Rodl  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1511.00563

## One-line
Exhibits a 3-uniform hypergraph family (hedgehogs) whose 2-colour Ramsey number is polynomial but whose 4-colour Ramsey number is exponential — the first class showing strong colour-count dependence.

## Key claim
For the 3-uniform hedgehog $H_t$ (body $\{1,\dots,t\}$ plus a unique spine vertex per pair): $r_3(H_t) \le 4t^3$ while $r_3(H_t;4) \ge 2^{ct}$. For 3 colours, $r_3(H_t;3)$ is sandwiched polynomially between $F(t)$ and $F(t^3)$, where $F(t)$ is the Erdős–Hajnal-type function for 4-coloured $K_n$ avoiding red/blue/green rainbow triangles.

## Method
Upper bound: define a partial graph colouring based on whether a pair $(u,v)$ has few monochromatic triples; use a counting contradiction to bound degrees, then apply Brooks' theorem to extract an independent set serving as the hedgehog body, embedding spines greedily. Lower bound: lift a graph colouring (where every $t$-clique uses all $q$ colours) to a hypergraph colouring by assigning each triple $uvw$ a colour missing from $\{\chi(u,v),\chi(v,w),\chi(w,u)\}$. The 3-colour analysis reduces to the rainbow-triangle case of the multicolour Erdős–Hajnal conjecture, using Spencer's independent-set lemma and a Fox–Grinshpun–Pach result.

## Result
$r_3(H_t) \le 4t^3$ (polynomial); $r_3(H_t;4) \ge 2^{ct}$ (exponential); $r_3(H_t;3) = O(t^4 F(t^3)^2)$ and $\ge F(t)$, giving $r_3(H_t;3) \le t^{c\log t}$. For $k\ge 4$, $r_k(H_t^{(k)}) \le t_{k-2}(c_k t)$ (tower of height $k-2$); for $k=4$ this is tight: $r_4(H_t^{(4)}) \ge 2^{ct}$. Also shows the Burr–Erdős conjecture fails for 3-uniform hypergraphs with $\ge 3$ colours (hedgehogs are 1-degenerate).

## Why it matters here
General background; no direct arena tie. Relevant only as a methodological reference for extremal hypergraph / Ramsey-style arguments (Brooks' theorem extraction, lift-from-graph-colouring constructions, Spencer independent-set lemma) that could surface if an arena problem maps onto extremal graph/hypergraph territory.

## Open questions / connections
- Problem 3: prove $r_3(H_t) = t^{2+o(1)}$ (approximate 2-colour linearity).
- Problem 4: special case of multicolour Erdős–Hajnal — is $F(t)$ polynomial? (Would tighten $r_3(H_t;3)$ to polynomial.)
- Problem 2: does there exist a $k$-uniform hypergraph family with 2-colour Ramsey polynomial but $q$-colour Ramsey tower of arbitrary height $h$?
- Problem 1: is there a $q$-colouring of $K_n^{(3)}$ on $2^{2^{ct}}$ vertices where every $t$-subset uses $\ge 3$ colours? Affirmative (with $\ge 5$ colours) would give $r_4(H_t^{(4)};q) \ge 2^{2^{ct}}$.
- Curious mirror: upper bound $t^{c\log t}$ for $r_3(H_t;3)$ matches Conlon–Fox–Sudakov lower bound for $r_3(K_t;3)$.

## Key terms
Ramsey number, hypergraph Ramsey, hedgehog hypergraph, multicolour Ramsey, Erdős–Hajnal conjecture, rainbow triangle, Burr–Erdős conjecture, degeneracy, Brooks' theorem, Spencer independent set, tower function, Kostochka–Rödl construction
