---
type: source
kind: paper
title: On the maximum number of five-cycles in a triangle-free graph
authors: Andrzej Grzesik
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1102.0962
source_local: ../raw/2011-grzesik-maximum-number-five-cycles-triangle-free.pdf
topic: general-knowledge
cites:
---

# On the maximum number of five-cycles in a triangle-free graph

**Authors:** Andrzej Grzesik  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1102.0962

## One-line
Settles Erdős's conjecture that a triangle-free graph on $n$ vertices contains at most $(n/5)^5$ copies of $C_5$, attained by the balanced blow-up of $C_5$, via Razborov's flag algebra method.

## Key claim
The Turán density satisfies $\pi_{C_5}(K_3) \le 24/625$, equivalently the number of 5-cycles in any triangle-free graph on $n$ vertices is at most $(n/5)^5$; extremal example is the balanced blow-up of $C_5$ when $5 \mid n$.

## Method
Flag algebra SDP at level $l=5$: enumerate all triangle-free graphs on 5 vertices, fix three types on 3 vertices ($\sigma_0$ empty, $\sigma_1$ one edge, $\sigma_2$ two edges) with $m=4$, giving 8 + 6 + 5 admissible $\sigma$-flags. Exhibit three explicit positive semidefinite matrices $P, Q, R$ (with characteristic polynomials verifiable in Mathematica/Maple) whose combination certifies the bound $24/625$ via Razborov's inequality $\pi_A(F) \le \max_H (d_A(H) + c_H)$. A standard blow-up argument transfers the density bound to the exact integer count.

## Result
$\pi_{C_5}(K_3) = 24/625$ (the upper bound is tight at the $C_5$ blow-up which achieves density $24/625$). Improves Győri's $c\binom{n+1}{5}/5$ with $c \approx 1.038$ and Füredi's later unpublished bound to the conjectured exact value $(n/5)^5$. Same result obtained independently and simultaneously by Hatami–Hladký–Král–Norine–Razborov (arXiv:1102.1634) via different techniques.

## Why it matters here
Canonical worked example of Razborov flag algebras settling an Erdős extremal-graph conjecture via SDP — directly relevant to any Einstein Arena problem of the form "max density of subgraph $H$ in graph forbidding $F$", and a template for setting up the type/flag enumeration plus PSD certificate. The explicit small matrices ($8\times8$, $6\times6$, $5\times5$) make it a readable entry point before scaling to the larger flag-SDP problems in the wiki's extremal-graph cluster.

## Open questions / connections
- Generalisation: max number of $C_{2k+1}$ in $K_{r}$-free graphs (Bondy–Simonovits, Erdős–Győri–Simonovits) — does the analogous balanced odd-cycle blow-up remain extremal, and how does flag-algebra level $l$ scale?
- Stability / uniqueness: is the $C_5$ blow-up the unique extremal structure, and what is the stability region (close-to-extremal graphs must be close to a blow-up)?
- Extends Győri (1989) and Füredi's unpublished improvement; settles Erdős (1984) pentagon conjecture; parallels Razborov's flag-algebra resolution of the Caccetta–Häggkvist-type and 3-hypergraph extremal problems.

## Key terms
flag algebra, Razborov, Turán density, triangle-free graph, $C_5$ pentagon, Erdős conjecture, semidefinite programming, blow-up construction, extremal graph theory, $\sigma$-flag, positive semidefinite certificate, Győri bound
