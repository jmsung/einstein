---
type: source
kind: paper
title: Semidefinite programming bounds for distance distribution of spherical codes
authors: Oleg R. Musin
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2309.13854v2
source_local: ../raw/2023-musin-semidefinite-programming-bounds-distance.pdf
topic: general-knowledge
cites: 
---

# Semidefinite programming bounds for distance distribution of spherical codes

**Authors:** Oleg R. Musin  ·  **Year:** 2023  ·  **Source:** http://arxiv.org/abs/2309.13854v2

## One-line
Extends the Bachoc–Vallentin 3-point SDP framework from bounding spherical-code cardinality to bounding the *distance distribution* $\{A_t\}$, yielding a shorter proof of $k(4)=24$.

## Key claim
For $(N,n,T)$ spherical codes, a symmetric 3-point function $F$ plus auxiliary functions $h,g$ with $F(t,u,v)\le g(t)+g(u)+g(v)$ on $D_3(T)$ give an SDP-checkable lower bound $R_g(C)\ge (N-M)/(3N)$ with $M=F(1,1,1)+3h(1)$ (Theorem 3.1, Corollary 3.1); applied with a degree-22 Gegenbauer polynomial $g_1$ on $T=[-1,1/2]$ this gives $B_1(25)=0.0324$, contradicting the kissing-number assumption $N\ge 25$ in $\mathbb{R}^4$.

## Method
3-point SDP with Bachoc–Vallentin matrices $S^n_k$ and PSD Gegenbauer combinations, but with the inequality flipped to bound $E_g(C)=\sum g(x\cdot y)$ from below rather than $|C|$ from above. Trick: allow $g$ to have *negative* Gegenbauer coefficients (so LP/Delsarte fails) provided $F$ is PSD and $S_h(C)\ge 0$ holds via a separately chosen $h$. Polynomials $g_1,g_2$ were computed by Maria Dostert's SDP solver for the $\pi/3$-cap interval $T=[-1,0.5]$.

## Result
Reproves $k(4)=24$ without the hardest sub-case ($m=5$ points in a spherical cap) of Musin 2008. With $g_1$ ($g_1(t)\le 0$ on $[-\sqrt{2}/2,1/2]$, $M_1=22.5689$): for an alleged $(25,4,\pi/3)$ code, the cap-method maximum of $R_{g_1}(C)$ over $\mu\le 4$ is $0.0266$ but the SDP lower bound is $0.0324$ — contradiction. Also gives sharp interval distance-distribution bounds for the conjectured 24-cell kissing code, e.g. $A([-1,-0.45])\le 9$, $A([0.35,0.5])\ge 8$.

## Why it matters here
Directly informs **kissing number** (P-family) and any arena problem where the LP/Delsarte bound is loose because the natural test function has mixed-sign Gegenbauer coefficients — the SDP route here recovers and tightens it. Also a template for *distance-distribution* constraints (vs cardinality alone), relevant to uniqueness/rigidity arguments and to sphere-packing problems where one needs to pin down $A_t$ on sub-intervals.

## Open questions / connections
- Uniqueness of the 24-cell as the maximal $k(4)=24$ arrangement — paper claims the distance-distribution SDP framework can plausibly close it (joint work with Dostert/Kolpakov/Moustrou in preparation [13]).
- Generalize Theorems 2.2/3.1 to sphere packings in $\mathbb{R}^n$ via Musin's $H_k$ polynomials to attack the **24-cell conjecture** ($\delta_4=1/8$, $D_4$ optimality).
- Extend to $k$-point ($k=4,5,6$) SDP bounds à la de Laat–Machado–Oliveira Filho–Vallentin for equiangular lines and $s$-distance sets; apply to Tammes ($N=15,\ldots$) to prune the planar-graph list $L_N$; apply as a Yudin-type bound for Thomson / Riesz / universally optimal configurations.

## Key terms
semidefinite programming, SDP 3-point bound, Bachoc–Vallentin, distance distribution, spherical codes, kissing number, k(4)=24, 24-cell, Gegenbauer polynomials, Delsarte LP bound, Musin, Dostert
