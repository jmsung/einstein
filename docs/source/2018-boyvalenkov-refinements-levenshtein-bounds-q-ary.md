---
type: source
kind: paper
title: Refinements of Levenshtein Bounds in q-ary Hamming Spaces
authors: P. Boyvalenkov, D. Danev, Maya M. Stoyanova
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1801.01982
source_local: ../raw/2018-boyvalenkov-refinements-levenshtein-bounds-q-ary.pdf
topic: general-knowledge
cites:
---

# Refinements of Levenshtein Bounds in q-ary Hamming Spaces

**Authors:** P. Boyvalenkov, D. Danev, Maya M. Stoyanova  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1801.01982

## One-line
Sharpens the Levenshtein universal upper bound on $A_q(n,s)$ (max code size in $q$-ary Hamming space with prescribed max inner product) by replacing each double root of Levenshtein's polynomial with two simple roots at adjacent admissible inner products $t_j \in T_n$.

## Key claim
For every $n \geq q \geq 2$, an LP-feasible degree-3 polynomial yields a strict improvement of the third Levenshtein bound $L_3(n,s;q)$ whenever Levenshtein's interior root $\alpha_0 \notin T_n$, giving the closed-form bound $A_q(n,s) \leq a(a+q)dq / [a^2(2-q-j) + Da + E]$ (Theorem 4.4) — a $q$-ary generalization of McEliece's binary bound. Concrete improvements: $A_3(14,-1/7) \leq 237$ (vs Levenshtein 256.5), $A_4(11,-3/11) \leq 320$ (vs 364), $A_5(11,-5/11) \leq 250$ (vs 265).

## Method
Discretization refinement of Delsarte/Levenshtein linear programming: take Levenshtein's polynomial $f_m(t) = (t-s)(t+1)^\varepsilon A^2(t)$ whose double roots $\alpha_i$ are continuous in $s$, locate the interval $(t_{j-1}, t_j) \ni \alpha_i$ in the discrete inner-product set $T_n$, and replace the double root with two simple roots $t_{j-1}, t_j$. The resulting polynomial still satisfies Delsarte's conditions (A1) non-positivity on $T_n \cap [-1,s]$ and (A2) non-negative Krawtchouk coefficients (proven via $f_2, f_1 > 0$ from concavity in $j$); KKT optimality conditions verify global LP-optimality.

## Result
For the third Levenshtein bound, asymptotics with $j = c n^\alpha$: bound equals $[(q-1)n - (j+q-2)](j+q) + j(j+q-1)^2 + o(1)$ for $\alpha \in [0, 1/5)$; with extra term $c^5 n^{5\alpha-1}/(q-1)$ for $\alpha \in [1/5, 1/2)$; and $\sim c(q-1)^2 n^{3/2}/(q-1-c^2)$ at $\alpha = 1/2$ (Corollary 4.6). For the fourth bound: $A_q(n,s) \lesssim q(q-1)^2 n^2 / [2(q-c)]$ (Theorem 5.2). Computational reach extends to $n = 10000, q = 3$ via $L_5$, matching Barg-Jaffe simplex bounds for binary $n=1000$ across $d/n \in [0.25, 0.45]$.

## Why it matters here
Direct relevance to coding-theoretic / extremal-set arena problems via Delsarte LP framework — informs autocorrelation inequalities, kissing-number-style sphere packings (where Cohn-Elkies LP is the parallel tool), and any problem where vanishing-at-discrete-points sharpens a continuous LP bound. The "replace double zero with adjacent simple zeros" trick is a transferable technique for tightening LP bounds when the constraint set is discrete.

## Open questions / connections
- Conjecture 3.1: for fixed $q \geq 3$ there exists $s_q$ such that the refinement matches the full LP optimum for all $s \in [-1, s_q) \cap T_n$ — proven only for $m=3$ with rare exceptions ($q=3$, $n \in \{5,7,8,9\}$).
- Disagreement with Samorodnitsky's conjecture on exponential strength of Delsarte LP — computational evidence does not support it.
- Putative codes attaining the bound (Table 2) must be 3-designs with integral distance distributions; ~30-50% of cases pass integrality, leaving open existence questions for individual $(n, M, d)$ triples.
- Extension to $L_5$ and beyond: positivity proofs for $f_i$ coefficients become technically harder; verified only numerically.

## Key terms
Levenshtein bound, Delsarte linear programming, Krawtchouk polynomials, Hamming space, q-ary codes, McEliece bound, adjacent polynomials, KKT optimality, polynomial metric space, code distance distribution, 3-design, Sidelnikov codes
