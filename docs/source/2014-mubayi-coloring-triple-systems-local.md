---
type: source
kind: paper
title: Coloring Triple Systems with Local Conditions
authors: D. Mubayi
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1410.3010
source_local: ../raw/2014-mubayi-coloring-triple-systems-local.pdf
topic: general-knowledge
cites:
---

# Coloring Triple Systems with Local Conditions

**Authors:** D. Mubayi  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1410.3010

## One-line
Constructs an edge-coloring of the complete 3-uniform hypergraph $K_n^3$ in which every 5-vertex subhypergraph sees at least 3 distinct colors, using only $e^{O(\sqrt{\log\log n})}$ colors.

## Key claim
$f_3(n,5,3) = e^{O(\sqrt{\log\log n})}$, where $f_k(n,p,q)$ is the minimum number of colors in an edge-coloring of $K_n^k$ such that every copy of $K_p^k$ receives at least $q$ colors. This resolves the first open case of a Conlon–Fox–Lee–Sudakov question, with a bound far below the asked-for $(\log n)^{o(1)}$.

## Method
Explicit construction via the Erdős–Hajnal **stepping-up** technique applied to a base coloring $\sigma$ on $K_n$ (vertices = 0/1 vectors of length $m$ with exactly $t$ ones, ordered by binary value). The base color $\sigma(vw)$ is a 4-tuple combining the first differing position, a second structural index, and two bijection-image coordinates on intersection sets; the lifted 3-graph coloring $\chi(uvw)$ pairs $\sigma$ applied to differing-position indices with a sign bit $\delta_{uvw}$ recording monotonicity of those indices. Three structural properties of $\sigma$ (forcing color disagreements under various ordering patterns) drive the case analysis ruling out any 2-colored $K_5^3$.

## Result
Theorem 1: $f_3(n,5,3) = e^{O(\sqrt{\log\log n})}$. The construction inherits $e^{O(\sqrt{\log n})}$ colors from $\sigma$ on $K_n$ and lifts to $K_N^3$ with $N = 2^n$, giving the $\sqrt{\log\log N}$ exponent. The coloring $\sigma$ is simultaneously a $(3,2)$- and $(4,3)$-coloring of $K_n$, and the lifted $\chi$ is verified to be a $(5,3)$-coloring of $K_N^3$ via a two-case analysis on the position $p$ of the minimum index $\gamma_p = \min_j \gamma_{x_j x_{j+1}}$.

## Why it matters here
General background; no direct arena tie. Belongs to extremal/Ramsey hypergraph coloring (the $f_k(n,p,q)$ generalized-Ramsey family), adjacent to extremal graph theory and combinatorics problems but with no immediate optimization-style evaluator structure in the current 23 arena problems.

## Open questions / connections
- Extends Mubayi's earlier $(4,3)$-coloring construction of $K_n$ [Combinatorica 1998, 2004] via stepping-up to one higher uniformity.
- Connects to Shelah's primitive-recursive Hales–Jewett bounds, the Conlon–Fox–Lee–Sudakov grid-Ramsey program, and the Erdős–Gyárfás generalized Ramsey numbers $f_2(n,p,p-1)=n^{o(1)}$.
- Leaves open $f_3(n,p,p-2)$ for $p \ge 6$ and the general $f_k(n,p,q)$ landscape; author conjectures the stepping-up + bijection-coordinate idea generalizes further.

## Key terms
generalized Ramsey number, $f_k(n,p,q)$, $(p,q)$-coloring, 3-uniform hypergraph, triple system, Erdős–Hajnal stepping-up, edge-coloring, Conlon–Fox–Lee–Sudakov, Erdős–Gyárfás problem, Shelah Hales–Jewett, Mubayi construction, extremal combinatorics
