---
type: source
kind: paper
title: Symmetric Layer-Rainbow Colorations of Cubes
authors: Amin Bahmanian
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2205.02210
source_local: ../raw/2022-bahmanian-symmetric-layer-rainbow-colorations-cubes.pdf
topic: general-knowledge
cites:
---

# Symmetric Layer-Rainbow Colorations of Cubes

**Authors:** Amin Bahmanian  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2205.02210

## One-line
Settles the existence problem for symmetric $(2,1)$-latin cubes of order $n$ via a transportation-network / integer circulation argument.

## Key claim
A symmetric latin cube of order $n$ — an $n \times n \times n$ array on $n^2$ symbols where every axis-parallel layer is rainbow and full $S_3$-symmetry holds on index triples — exists if and only if $n \equiv 0, 2 \pmod{3}$, with two exceptions $n = 1$ and $n = 3$.

## Method
Reduces existence to partitioning the non-uniform set system $\binom{X}{1} \cup 3\binom{X}{2} \cup 2\binom{X}{3}$ into parallel classes (Lemma 2.1). Existence of such a partition is reduced to integrality of a $3 \times n^2$ nonnegative system $a_i + 2b_i + 3c_i = n$ with prescribed row sums $n, 3\binom{n}{2}, 2\binom{n}{3}$ (Lemma 3.1, solved by explicit block matrices $M_n$ per residue class mod 6). The partition is then built inductively by splits $F_i$, using a Ford–Fulkerson integer circulation on an auxiliary digraph to round a fractional circulation to $\{0,1\}$ at each induction step.

## Result
Theorem 1.1: symmetric latin cubes of order $n$ exist iff $n \equiv 0,2 \pmod 3$, $n \notin \{1,3\}$. The $n \equiv 1 \pmod 3$ obstruction is a counting argument: $a_i + 2b_i \equiv 1 \pmod 3$ forces $|A \cup B| \le n + \tfrac{3}{2}\binom{n}{2}$, yielding $n \le 1$. Explicit examples are constructed for $n = 5, 6, 8$ (and parametric families for all $n \equiv 0 \pmod 6$, $2 \pmod 6$, $3 \pmod 6$ with $n \ne 3$, $5 \pmod 6$).

## Why it matters here
General background; no direct arena tie. Closest relevance is to extremal combinatorics / design-theory problems involving symmetric configurations and orthogonal arrays, but no Einstein Arena problem is currently identified that uses layer-rainbow cube structure.

## Open questions / connections
- Generalization to $(s,f)$-latin hypercubes with symmetry — existence open beyond cubes.
- Enumeration of symmetric latin cubes (Bailey–Preece–Zemroch 1978 only handled small orders for $(1,1)$-cubes).
- Connection to orthogonal arrays (Hedayat–Sloane–Stufken) and to mutually orthogonal Sudoku frequency squares (Ethier–Mullen).

## Key terms
latin cube, symmetric latin square, parallel class, transportation network, integer circulation, Ford-Fulkerson, orthogonal array, combinatorial design, factorization, set system partition, Bahmanian, layer-rainbow
