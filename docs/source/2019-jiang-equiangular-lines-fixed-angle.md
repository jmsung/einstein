---
type: source
kind: paper
title: Equiangular lines with a fixed angle
authors: Zilin Jiang, Jonathan Tidor, Yuan Yao, Shengtong Zhang, Yufei Zhao
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1907.12466
source_local: ../raw/2019-jiang-equiangular-lines-fixed-angle.pdf
topic: general-knowledge
cites:
---

# Equiangular lines with a fixed angle

**Authors:** Zilin Jiang, Jonathan Tidor, Yuan Yao, Shengtong Zhang, Yufei Zhao  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1907.12466

## One-line
Determines the maximum number $N_\alpha(d)$ of equiangular lines in $\mathbb{R}^d$ with fixed common angle $\arccos\alpha$ for all sufficiently large $d$, settling a problem open since Lemmens–Seidel (1973).

## Key claim
Let $\lambda = (1-\alpha)/(2\alpha)$ and let $k = k(\lambda)$ be the minimum number of vertices in a graph whose adjacency-matrix spectral radius equals $\lambda$ exactly (the *spectral radius order*). Then for $d > d_0(\alpha)$: (a) if $k < \infty$, $N_\alpha(d) = \lfloor k(d-1)/(k-1)\rfloor$; (b) if $k = \infty$, $N_\alpha(d) = d + o(d)$. In particular $N_{1/(2k-1)}(d) = \lfloor k(d-1)/(k-1)\rfloor$ for every integer $k \geq 2$, confirming Bukh's conjecture.

## Method
Recast equiangular lines as a spectral graph problem: the Gram matrix becomes $\lambda I - A_G + \tfrac12 J$, which must be PSD with rank $\leq d$. Two key ingredients: (i) a switching+Ramsey argument (extending Balla–Dräxler–Keevash–Sudakov) shows one can choose vector signs so the associated graph $G$ has bounded degree $\Delta(\alpha)$; (ii) a new spectral graph theorem: every connected $n$-vertex graph with max degree $\leq \Delta$ has $j$-th eigenvalue multiplicity at most $C(\Delta,j)\, n/\log\log n$, proved by Cauchy interlacing combined with comparing local vs global closed-walk counts after deleting an $r$-net.

## Result
Exact formula $N_\alpha(d) = \lfloor k(d-1)/(k-1)\rfloor$ for $d > 2^{2C\lambda k}$ when $k(\lambda)<\infty$, achieved by disjoint copies of the extremal $k$-vertex graph $H$ with $\lambda_1(H)=\lambda$ plus isolated vertices. When $k=\infty$ the bound $N_\alpha(d) \leq d + O_\Delta(d/\log\log n)$ follows from the eigenvalue multiplicity theorem applied to the unique component of spectral radius $>\lambda$ (forced by $\lambda_2(G)\leq \lambda$). The second-eigenvalue multiplicity bound $O(n/\log\log n)$ cannot be improved below $O(n^{1/3})$ (PSL(2,p) Cayley graphs witness this).

## Why it matters here
Directly relevant to equiangular-lines and spherical-code problems on Einstein Arena (kissing-number adjacent, sphere-packing adjacent): supplies the exact asymptotic dependence of line counts on the angle via a clean spectral-graph quantity $k(\lambda)$. The bounded-degree-via-switching + second-eigenvalue-multiplicity toolkit generalizes to two-distance sets and signed graphs (follow-up arXiv:2006.06633), which informs any agent work involving Gram matrices with two distinct off-diagonal values.

## Open questions / connections
- Conjecture 6.1: when $k(\lambda)=\infty$, is $N_\alpha(d) = d + O_\alpha(1)$? Verified except when $\lambda$ is a totally real algebraic integer largest among its conjugates.
- Question 6.3/6.4: what is the true maximum second-eigenvalue multiplicity for connected $n$-vertex $\Delta$-bounded graphs? Gap between $O(n/\log\log n)$ upper and $\Omega(n^{1/3})$ lower bound; $O(1)$ for fixed $\lambda$ would imply Conjecture 6.1.
- Question 6.5: maximum size of a spherical $\{\alpha,\beta\}$-code in $\mathbb{R}^d$ — generalization beyond pure $\pm\alpha$ inner products.
- Connections: Colding–Minicozzi harmonic-function methods, Kleiner's proof of Gromov polynomial-growth, Lee–Makarychev volume-growth eigenvalue bounds for bounded-doubling Cayley graphs.

## Key terms
equiangular lines, spectral radius order, second eigenvalue multiplicity, Cauchy interlacing, switching, Ramsey, Gram matrix, Perron–Frobenius, bounded-degree graph, spherical two-distance set, SIC-POVM, Lemmens–Seidel, Neumaier, Bukh, Jiang–Polyanskii
