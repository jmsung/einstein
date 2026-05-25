---
type: source
kind: paper
title: Optimality and uniqueness of the $D_4$ root system
authors: David de Laat, Nando Leijenhorst, W. D. Keizer
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2404.18794
source_local: ../raw/2024-laat-optimality-uniqueness-root-system.pdf
topic: general-knowledge
cites:
---

# Optimality and uniqueness of the $D_4$ root system

**Authors:** David de Laat, Nando Leijenhorst, W. D. Keizer  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2404.18794

## One-line
Proves the $D_4$ root system (24-cell vertices) is the *unique* optimal kissing configuration in $\mathbb{R}^4$ and an optimal spherical code, by computing an exact rational solution to the second level of the Lasserre hierarchy via SDP.

## Key claim
$k(4) = 24$ is uniquely achieved by $D_4$ up to isometry; $D_4$ is an optimal (not universally optimal) spherical 24-code in $S^3$, settling the Cohn–Conway–Elkies–Kumar conjecture that no universally optimal 24-point code exists in $S^3$. Bonus: $k(6) \le 77$ (improves prior 78 from Bachoc–Vallentin).

## Method
Second level of the De Laat–Vallentin Lasserre hierarchy for infinite graphs ($t=2$, a 4-point bound), reduced to a finite SDP via $O(n)$-equivariant zonal matrices $Z_\lambda$ built from Gross–Kunze representations of $O(n)$ induced from $GL(2)$; sums-of-squares + Putinar to enforce polynomial inequality constraints on $\Delta_i$. New efficiency: extra $O(2)$/$O(n-2)$ symmetries cut zonal-matrix cost so $|\lambda| \le 14$ becomes tractable. Numerical solve at 256-bit precision (≈2 weeks, 8 cores, 128GB), then rounded to an *exact rational* optimum using the Cohn–de Laat–Leijenhorst (2024) heuristic; verified in ball arithmetic.

## Result
Exact feasible $K$ with $K(\emptyset,\emptyset)=24$ and the two-point polynomial $p_2(u)=A_2K|_{I=2}$ has zeros exactly at $u \in \{-1, -1/2, 0, 1/2\}$ on $[-1,1/2]$. Complementary slackness then forces any 24-point code on $S^3$ with minimal angle $\ge \pi/3$ to use *only* inner products in $\{-1,-1/2,0,1/2\}$ (Lemma 5.1) ⇒ optimality (Thm 5.2) and uniqueness via root-system classification or via a Calderbank–Cameron–Kantor–Seidel argument (Thm 5.3). For $n=6$: a strictly feasible solution at objective 77.85 certifies $k(6)\le 77$.

## Why it matters here
Direct method for **kissing_number** problems and a template for any Einstein Arena problem where the 3-point (Bachoc–Vallentin) bound is not sharp — shows the 4-point Lasserre level can close it, with concrete rounding + verification pipeline. The authors explicitly suggest a noncompact adaptation could attack the $\mathbb{R}^4$ sphere packing problem (the $D_4$ lattice conjecture), making this a candidate technique for sphere-packing-class arena problems too.

## Open questions / connections
- Does a noncompact 4-point Lasserre bound (à la Cohn–Elkies) prove the $D_4$ lattice optimal for sphere packing in $\mathbb{R}^4$?
- Why is the 3-point bound provably non-sharp for $3\le n\le 24$ except $n=8,24$, but the 4-point level becomes sharp at $n=4$? Predict which other $n$ flip at level 3.
- Can $p_2 \equiv 0$ occur at sharpness in higher Lasserre levels? (Open per §5.1 — affects whether sharp-bound ⇒ finite inner-product set automatically.)
- Extends De Laat–Machado–de Muinck Keizer (arXiv:2211.16471) on equiangular lines from finite-orbit to infinite-orbit quotients $I_t/O(n)$.
- Pushing $|\lambda|>16$ may yield improvements at $n=5,7,10,12,16$ (computed but no improvement at current truncation).

## Key terms
kissing number, $D_4$ root system, 24-cell, spherical code, Lasserre hierarchy, semidefinite programming, sums of squares, Bachoc-Vallentin three-point bound, Delsarte LP bound, Cohn-Elkies, zonal matrices, Gross-Kunze induced representations, $O(n)$ invariants, exact SDP rounding, Putinar Positivstellensatz, universal optimality, sphere packing $\mathbb{R}^4$, complementary slackness
