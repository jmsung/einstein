---
type: source
kind: paper
title: Complete resolution of the circulant nut graph order-degree existence problem
authors: Ivan Damnjanovi'c
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2212.03026
source_local: ../raw/2022-damnjanovic-complete-resolution-circulant-nut.pdf
topic: general-knowledge
cites:
---

# Complete resolution of the circulant nut graph order-degree existence problem

**Authors:** Ivan Damnjanovi'c  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2212.03026

## One-line
Fully characterizes which $(n,d)$ pairs admit a $d$-regular circulant nut graph (a circulant graph whose adjacency matrix has nullity 1 with a nowhere-zero kernel vector).

## Key claim
$N_d = \emptyset$ unless $4 \mid d$ and $2 \mid n$; for $d \equiv_8 4$, $N_d = \{n : 2\mid n, n \ge d+4\}$; for $d=8$, $N_8 = \{14\} \cup \{n : 2\mid n, n \ge 18\}$ (note the "irregularity" — no order 16); for $8 \mid d \wedge d \ge 16$, $N_d = \{n : 2\mid n, n \ge d+6\}$.

## Method
Reduces nut-graph existence to a polynomial non-vanishing condition: for $G=\mathrm{Circ}(n,S)$, $G$ is a nut graph iff $n$ is even, $|S|$ splits evenly between odd/even, and the symbol polynomial $P(x)=\sum_{s\in S}(x^s+x^{-s})$ has no $n$-th roots of unity as zeros except possibly $\pm 1$. Constructions are given explicitly for each remaining case ($n=4t+8$; $8\mid n$, $n\ge 4t+16$; $n\equiv_8 4$, $n\ge 4t+12$), and non-divisibility by cyclotomic polynomials $\Phi_b(x)$ is verified using the Filaseta-Schinzel lacunary-polynomial theorem combined with finite computer-algebra checks (Mathematica) over the bounded residue set of $b$'s.

## Result
Theorem 5 closes the existence problem completely, settling Bašić et al.'s conjecture (refuted in its strong form) and extending Damnjanović-Stevanović and Damnjanović's earlier partial results that only covered odd $t$ or $n\equiv_4 2$. The construction uses generator sets of the form $\{1,\ldots,t-3\}\cup\{t-1,t\}\cup\{n/4, n/4+2\}\cup\{n/2-t,\ldots,n/2-1\}$ with case-specific perturbations, and the proof relies on bounding the number of nonzero terms in residue-reduced symbol polynomials.

## Why it matters here
General background; no direct arena tie. Circulant nut graphs are an extremal spectral-graph object not currently among the 23 Einstein Arena problems, but the cyclotomic-divisibility / lacunary-polynomial machinery (Filaseta-Schinzel) and the technique of converting an extremal combinatorial existence problem into roots-of-unity non-vanishing could inform any future arena problem with circulant / spectral / roots-of-unity structure.

## Open questions / connections
- What is the analogous order-degree characterization for *Cayley nut graphs* over non-cyclic abelian groups?
- Can the cyclotomic-divisibility framework be replaced by a purely combinatorial argument that avoids computer verification of the 40 / 26 sporadic $b$-values?
- Extends Sciriha's original nut-graph theory and Bašić et al.'s circulant-nut conjecture; leaves open the *minimum-order* function for higher symmetry classes.

## Key terms
circulant graph, nut graph, graph spectrum, adjacency nullity, cyclotomic polynomial, Filaseta-Schinzel lacunary polynomial theorem, roots of unity, symbol polynomial, extremal spectral graph theory, Sciriha, Damnjanović, generator set, regular graph existence
