---
type: source
kind: paper
title: On the grid Ramsey problem and related questions
authors: D. Conlon, J. Fox, Choongbum Lee, B. Sudakov
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1405.6587
source_local: ../raw/2014-conlon-grid-ramsey-problem-related.pdf
topic: general-knowledge
cites:
---

# On the grid Ramsey problem and related questions

**Authors:** D. Conlon, J. Fox, Choongbum Lee, B. Sudakov  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1405.6587

## One-line
Proves a superpolynomial lower bound on the Shelah cube lemma constant $G(r)$, refuting a conjecture of Graham–Rothschild–Spencer that polynomial bounds suffice.

## Key claim
$G(r) > 2^{c(\log r)^{5/2}/\sqrt{\log\log r}}$ for some constant $c>0$, where $G(r)$ is the minimum $n$ such that every $r$-edge-coloring of $K_n \times K_n$ contains an alternating rectangle (opposite sides same color). This is the first superpolynomial lower bound; previous bound was $\Omega(r^3)$ (Faudree–Gyárfás–Szőnyi), upper bound is Shelah's $r^{\binom{r+1}{2}}+1$.

## Method
Probabilistic construction of alternating-free colorings of the grid $\Gamma_{m,n}$ via a row-coloring lemma (Lemma 3.1): such colorings correspond to $m$ edge-colorings $c_1,\dots,c_m$ of $K_n$ such that $\chi(G(c_i,c_j)) \le r$ for all $i,j$, where $G(c_i,c_j)$ is the agreement graph. Edge partitions of $K_n$ with slowly-growing chromatic number on unions are constructed using a variant of Mubayi's $(4,3)$-coloring $c_M$, proven to be a *chromatic-$(4,3)$-coloring* (Theorem 1.7: union of any $|X|$ color classes has $\chi \le 2^{3\sqrt{|X|\log|X|}}$). Random subset sampling + union bound (Lemma 3.2) converts this into the grid lower bound.

## Result
- $G(r) > 2^{c(\log r)^{5/2}/\sqrt{\log\log r}}$ (Theorem 1.2; superpolynomial).
- Off-diagonal: $g(r^{\log C/2}, r^{r/2C}) \le r$, $g(2^{\varepsilon\log^2 r}, 2^{r^{1-\varepsilon}}) \le r$, $g(cr^2, r^{r^2/2}/e^{r^2}) \le r$ (Theorem 1.3).
- $F_3(r,5,6) \ge 2^{c\log^2 r}$ (Theorem 1.5, new case of Erdős–Gyárfás for 3-uniform hypergraphs).
- $2^{\log^2 r/36} \le F_\chi(r,4,3) \le C \cdot 2^{130\sqrt{r\log r}}$ (Theorem 1.6, chromatic variant).
- Asymmetric: $G(r,2) \ge r^2/4$ via Bose–Chowla-style $B_2$ sequences over $\mathbb{Z}_p$.

## Why it matters here
General background; no direct arena tie. Pure Ramsey-theoretic / extremal-combinatorics result — relevant only insofar as the council might invoke chromatic-partition or random-subset-of-color-classes constructions as a discrete-combinatorics technique template for problems in that family.

## Open questions / connections
- Question 6.3: Is $F_3(r,p,p-2) \ge 2^{r^c}$ for any fixed $c$? (next hypergraph case)
- Problem 6.4: Show $F_{2d-1}(r,2d,d+1)$ grows as an arbitrarily tall tower in $d$ — would refute tower-type Hales–Jewett bounds.
- Question 6.5: Is $F_\chi(r,p,p-1)$ superpolynomial for all $p \ge 4$? (confirmed for $p=4,5$ via $c_M$.)
- Question 6.7: How slowly can $\chi$ of a union of $s$ color classes grow in an edge partition of $K_n$? Improving Theorem 1.7 would tighten the $G(r)$ bound.
- Extends Shelah (1989), Gyárfás (1994), Faudree–Gyárfás–Szőnyi (1992), Mubayi (1998), Conlon–Fox–Lee–Sudakov (Erdős–Gyárfás resolution).

## Key terms
Hales–Jewett theorem, Shelah cube lemma, grid Ramsey problem, alternating rectangle, Erdős–Gyárfás problem, generalized Ramsey number, chromatic Ramsey, Mubayi coloring, $(p,q)$-coloring, edge-partition chromatic number, primitive recursive bounds, Cartesian product $K_n \times K_n$, Bose–Chowla sequences, van der Waerden
