---
type: source
kind: paper
title: Turán's Theorem for random graphs
authors: B. DeMarco, J. Kahn
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1501.01340
source_local: ../raw/2015-demarco-tur-theorem-random-graphs.pdf
topic: general-knowledge
cites:
---

# Turán's Theorem for random graphs

**Authors:** B. DeMarco, J. Kahn  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1501.01340

## One-line
Determines the sharp threshold above which the largest $K_r$-free subgraph of $G_{n,p}$ is exactly $(r-1)$-partite, settling a 25-year-old question of Babai–Simonovits–Spencer.

## Key claim
For each fixed $r\ge 3$, there is a constant $C$ such that if $p > C n^{-2/(r+1)} \log^{2/[(r+1)(r-2)]} n$, then w.h.p. every largest $K_r$-free subgraph of $G_{n,p}$ is $(r-1)$-partite — i.e., $t_r(G_{n,p}) = b_r(G_{n,p})$. The exponent of $n$ and log are best possible up to $C$.

## Method
Reduces $t_r(G) = b_r(G)$ to two structural lemmas about balanced $(r-1)$-cuts $\Pi=(A_1,\dots,A_{r-1})$: (1) any large $K_r$-free $F \subseteq G$ satisfying a minimum-degree-into-$A_1$ condition obeys $\varphi(F,\Pi) < |\Pi_G|$, and (2) the defect of $\Pi$ dominates the count of "bad" pairs in $A_1$ for which the $K_r^-$-extension count $\kappa_G(xy, A_2,\dots,A_{r-1}) < \gamma \Lambda_r(n,p)$ is small. Tools: Janson's inequality (lower tails), Kim–Vu polynomial concentration, Harris/FKG correlation, a Riordan–Warnke extension of Janson, the Conlon–Gowers / Schacht sparse-stability theorem as a black box, and a delicate edge-switching encoding ("type A/B/C steps") that bounds the count of bad configurations by a sequence-counting argument.

## Result
Sharp threshold $p_c \asymp n^{-2/(r+1)} \log^{2/[(r+1)(r-2)]} n$ for the event $\{t_r(G_{n,p}) = b_r(G_{n,p})\}$. Strictly stronger than the Conlon–Gowers/Schacht sparse Turán theorem in the regime where it applies (which gives only $t_r(G) < (1 - 1/(r-1) + \vartheta)|G|$ for $p > Kn^{-2/(r+1)}$). The conjectured exact constant is $C > [2r/(r+1)]^{2/[(r+1)(r-2)]}$, matching the threshold for "every edge lies in a $K_r$."

## Why it matters here
General background; no direct arena tie. Relevant only as a methodological reference for extremal-graph problems with sparse-random structure (Conlon–Gowers / Schacht / hypergraph containers, Janson lower tails, Kim–Vu polynomial concentration) if such tools are ever recruited for combinatorics-flavored arena problems.

## Open questions / connections
- Exact constant $C$: conjectured $[2r/(r+1)]^{2/[(r+1)(r-2)]}$; "stopping time" version is false (counterexample sketched in Section 13.A).
- Conjecture 13.1: $p_c(F_H) = O(p_c(G_H))$ for any $H$ with a color-critical edge (extending from cliques to general critical $H$).
- Conjecture 13.2: for $p \gg n^{-1}\log n$, no max cut of $G_{n,p}$ contains $\ge 51\%$ of edges at any vertex — still open even for $r=3$ at $p>Cn^{-1/2}$.
- Question whether a simpler "max-$K_r$-free $\Rightarrow$ nearly $(r-1)$-partite" suffices in place of the full Conlon–Gowers Theorem 1.4 (Theorem 1.4 used here only as a black box).

## Key terms
Turán's theorem, random graph $G_{n,p}$, $K_r$-free subgraph, $(r-1)$-partite, sparse random extremal, threshold, Babai–Simonovits–Spencer, Brightwell–Panagiotou–Steger, Conlon–Gowers, Schacht, Kohayakawa–Łuczak–Rödl, Janson inequality, Kim–Vu polynomial concentration, Harris/FKG inequality, color-critical edge, hypergraph containers, max cut, balanced cut, defect, Mantel's theorem
