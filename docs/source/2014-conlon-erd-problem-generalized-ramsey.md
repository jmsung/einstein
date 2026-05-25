---
type: source
kind: paper
title: The Erdős–Gyárfás problem on generalized Ramsey numbers
authors: D. Conlon, J. Fox, Choongbum Lee, B. Sudakov
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1403.0250
source_local: ../raw/2014-conlon-erd-problem-generalized-ramsey.pdf
topic: general-knowledge
cites:
---

# The Erdős–Gyárfás problem on generalized Ramsey numbers

**Authors:** D. Conlon, J. Fox, Choongbum Lee, B. Sudakov  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1403.0250

## One-line
Resolves the Erdős–Gyárfás question by showing $q = p-1$ is the largest $q$ for which the generalized Ramsey function $f(n,p,q)$ — the minimum number of colors needed so every $K_p \subseteq K_n$ sees at least $q$ colors — is subpolynomial in $n$.

## Key claim
**Theorem 1.1:** For all $p \geq 4$ and $n \geq 1$, $f(n, p, p-1) \leq 2^{16p (\log n)^{1 - 1/(p-2)} \log \log n}$, which is subpolynomial in $n$. Combined with the prior observation $f(n,p,p) = n^{\Omega(1)}$, this pins the polynomial/subpolynomial threshold exactly at $q = p-1$.

## Method
Explicit recursive edge-coloring construction generalizing Mubayi's $(4,3)$-coloring. Vertices are identified with $\{0,1\}^\alpha$; colors record, at multiple "resolutions" $r_0 < r_1 < \cdots < r_{p+1}$, the index and content of the first differing block via auxiliary functions $\eta_d, \xi_d$, composed as $c_p = \xi_p \times \cdots \times \xi_0$. Correctness uses induction on $\alpha$ with a partition into "inherited" colors $C_I$ (from a projection $\pi_{\alpha'}$) and "emerging" colors $C_E$, plus a pigeonhole argument across resolutions ensuring $\eta_{d-1}$ is injective on $C_E(d)$ for some $d$, yielding the inequality $|C_I| \geq |C_B| + \sum_{c \in C_E}(\mu_c - 1)$.

## Result
Quantitative upper bound $f(n,p,p-1) \leq 2^{16p (\log n)^{1 - 1/(p-2)} \log \log n}$; refined variant (Section 6.2) shaves the $\log \log n$ factor at the cost of a more technical proof. Section 6.1 strengthens this to a $(p + \lfloor r \rfloor + 1, p + \lfloor r \rfloor)$-coloring with $r = (p+4)/2$. Lower-bound side (Section 6.5): $f(n,4,3) \geq c \log n$ (Fox–Sudakov), and propagation formula $f(n \cdot f(n,p-1,q-1), p, q) \geq f(n,p-1,q-1)$ gives $f(n,p,p-1) \geq (c+o(1)) \log n$ for $p \geq 5$. Substantial gap remains.

## Why it matters here
General background; no direct arena tie. Relevant as a methodological exemplar of *recursive multi-resolution constructions* with inductive correctness proofs via refinement lattices — a pattern that could inspire constructions for extremal-graph or autocorrelation problems where one needs explicit colorings/configurations beating naive bounds.

## Open questions / connections
- Closing the gap between $f(n,p,p-1) \leq 2^{O(p)(\log n)^{1 - 1/(p-2)} \log \log n}$ and the $\Omega(\log n)$ lower bound, especially for $p \geq 5$ (Question 6.2).
- Question 6.1: does there exist an $n^{o(1)}$-color edge-coloring of $K_n$ such that the union of every $p-1$ color classes has chromatic number at most $p$? (Stronger chromatic-number variant of the clique-number property.)
- Extends Mubayi (1998) and Eichhorn–Mubayi (2000) constructions; complements Sárközy–Selkow sharpenings of Erdős–Gyárfás.

## Key terms
generalized Ramsey number, Erdős–Gyárfás problem, $(p,q)$-coloring, $f(n,p,q)$, subpolynomial coloring, Mubayi construction, recursive edge-coloring, multi-resolution blocks, refinement of functions, inherited vs emerging colors, Ramsey theory, Conlon Fox Lee Sudakov, Schur
