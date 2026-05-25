---
type: source
kind: paper
title: Diversity of uniform intersecting families
authors: A. Kupavskii
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1709.02829
source_local: ../raw/2017-kupavskii-diversity-uniform-intersecting-families.pdf
topic: general-knowledge
cites: 
---

# Diversity of uniform intersecting families

**Authors:** A. Kupavskii  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1709.02829

## One-line
Proves Frankl's conjecture that for $n \geq Ck$ the maximum diversity of an intersecting $k$-uniform family on $[n]$ is $\binom{n-3}{k-2}$, attained uniquely (up to isomorphism) by the "two out of three" family $A_2 = \{F : |F \cap [3]| \geq 2\}$.

## Key claim
For some absolute constant $C$ and all $n > Ck > 0$, every intersecting family $\mathcal{F} \subset \binom{[n]}{k}$ satisfies $\gamma(\mathcal{F}) \leq \binom{n-3}{k-2}$, with equality only when $\mathcal{F}$ is a subfamily of an isomorphic copy of $A_2$. Improves Frankl's earlier $n \geq 6k^2$ bound toward the conjectured threshold $n > 3k$. A counterexample (due to Lifshitz) is also given for $2k < n < 3k$, showing the extremal family is *not* shifted there.

## Method
Two-stage approach: (i) apply the Dinur–Friedgut junta theorem to reduce an intersecting family to a small-center $j$-junta $\mathcal{J}$ plus a small remainder; (ii) classify intersecting juntas — either $\mathcal{J} \subset A_2$ or all $\leq 2$-element sets in its defining family share a common element — and finish via a cross-intersecting Kruskal–Katona-style inequality (Lemma 5) on the residual families. Counterexample section uses $p$-biased measure, Margulis–Russo, and KKL-style influence bounds on a clever "runs-of-1s lex" junta $T_r$ to beat the natural "$r+1$ out of $2r+1$" family $D_r$.

## Result
Establishes $\gamma(\mathcal{F}) \leq \binom{n-3}{k-2}$ for $n > Ck$ with characterization of equality (Theorem 2). Lemma 5: cross-intersecting $\mathcal{A} \subset \binom{[m]}{a}$, $\mathcal{B} \subset \binom{[m]}{b}$ with $m > (C'+1)\max\{a,b\}$ and $|\mathcal{B}| \leq \binom{m-(b-a+1)}{a-1}$ satisfy $|\mathcal{A}| + C'|\mathcal{B}| \leq \binom{m}{a}$. Disproves the naive Ahlswede–Khachatrian-shaped conjecture $\gamma(\mathcal{F}) \leq \gamma(D_r)$ in the range $2k < n < 3k$: the junta $T_r$ with KKL-sharp influences $O(\log r / r)$ achieves $\gamma_p(T_r^{\uparrow}) = (1-p)(1/2 - O(\log r/r))$ vs $\gamma_p(D_r^{\uparrow}) = (1-p)(1/2 - \Omega(1/\sqrt{r}))$.

## Why it matters here
General background; no direct arena tie. Informs extremal-combinatorics / intersecting-family concepts (EKR-type problems, junta method, cross-intersecting inequalities) which sit adjacent to but outside the current 23 Einstein Arena problems.

## Open questions / connections
- Close the gap to the full conjectured range $n > 3k$ (Frankl) — current proof only handles $n \geq Ck$ for large $C$.
- Sharp behavior of $\Pr[\rho \geq k]$ in Lemma 8 (the runs-lex tail bound) is conjectured essentially tight modulo constants.
- Extends Frankl [7], Kupavskii–Zakharov [18], Lemons–Palmer [19] (whose $n > 6k^3$ bound this strengthens); relates to Keller–Lifshitz junta method [15] and Hao Huang's parallel counterexample [11] in $3k \leq n \leq (2+\sqrt{3})k$.

## Key terms
intersecting family, diversity, Erdős–Ko–Rado, Hilton–Milner, Frankl conjecture, junta method, Dinur–Friedgut, Kruskal–Katona, cross-intersecting, Ahlswede–Khachatrian, shifting, Kahn–Kalai–Linial, $p$-biased measure, influence
