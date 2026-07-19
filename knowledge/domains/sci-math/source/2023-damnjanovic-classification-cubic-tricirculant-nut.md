---
type: source
kind: paper
title: Classification of Cubic Tricirculant Nut Graphs
authors: Ivan Damnjanovi'c, N. Bašić, Tomaz Pisanski, Arjana Žitnik
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2312.14884
source_local: ../raw/2023-damnjanovic-classification-cubic-tricirculant-nut.pdf
topic: general-knowledge
cites:
---

# Classification of Cubic Tricirculant Nut Graphs

**Authors:** Ivan Damnjanovi'c, N. Bašić, Tomaz Pisanski, Arjana Žitnik  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2312.14884

## One-line
Proves no cubic bicirculant graph is a nut graph and gives a complete arithmetic classification of which cubic tricirculant graphs are nut graphs.

## Key claim
A cubic tricirculant graph is a nut graph iff it is a $T_1(n,a,b)$ or $T_4(n,a,b)$ (with $n$ even) satisfying explicit gcd/parity/2-adic-valuation conditions; no cubic circulant or bicirculant nut graph exists. A nut graph has adjacency-matrix nullity exactly 1 with a nowhere-zero kernel vector.

## Method
Reduce the local kernel-vector conditions (Lemma 3) on each tricirculant family to a circulant system whose eigenvalues are evaluated at $n$-th roots of unity via $c_0 + c_1\zeta + \cdots + c_{n-1}\zeta^{n-1}$. Nullity-one is then equivalent to a lacunary integer polynomial $R_{a,b}(x)$ having only $\zeta=1$ as an $n$-th-root-of-unity zero; cyclotomic-divisibility analysis using $\Phi_f(x)=\Phi_{f/p^{k-1}}(x^{p^{k-1}})$ and the Filaseta–Schinzel theorem on lacunary polynomials (bounded nonzero terms $\le N$) reduces the infinite condition to finitely many residue checks mod $f \in \{2,3,4,5,6,7,10,12,14,15,20,21,28,30,42,60,84\}$, verified by computer algebra.

## Result
For $T_1(n,a,b)$: nut iff $\gcd(n/2,a)=\gcd(n/2,b)=1$, $a\not\equiv_2 n/2$, $b\not\equiv_2 n/2$, and $v_2(b-a)\ge v_2(n)$. For $T_4(n,a,b)$: nut iff $\gcd(n/2,a,b)=1$, plus parity conditions on $a,b$ depending on whether $4\mid n$, plus (when $10\mid n$) one of $a,b,a-b,a+b$ divisible by 5. Types 2 and 3 are excluded outright; the triangular prism is the only graph simultaneously of types 1 and 3.

## Why it matters here
General background; no direct arena tie. The cyclotomic / lacunary-polynomial technique (encode a combinatorial property as "polynomial has no roots of unity of prescribed order", then use Filaseta–Schinzel to bound the search) is a transferable tool for any Einstein Arena problem whose feasibility condition reduces to an exponential-sum vanishing, e.g. autocorrelation/Sidon-type problems.

## Open questions / connections
- Extension to quartic bicirculant nut graphs (cited as in-progress, ref [17]).
- Generalization to $k$-circulant nut graphs for $k\ge 4$ — same eigenvalue-on-roots-of-unity machinery should apply.
- Whether the Filaseta–Schinzel bound on nonzero terms is tight here, or if a smaller list of $f$ suffices.

## Key terms
nut graph, circulant graph, bicirculant, tricirculant, cubic graph, graph spectrum, adjacency matrix nullity, cyclotomic polynomial, lacunary polynomial, Filaseta–Schinzel theorem, roots of unity, 2-adic valuation
