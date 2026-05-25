---
type: source
kind: paper
title: An extension the semidefinite programming bound for spherical codes
authors: O. Musin
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1903.05767
source_local: ../raw/2019-musin-extension-semidefinite-programming-bound.pdf
topic: general-knowledge
cites:
---

# An extension the semidefinite programming bound for spherical codes

**Authors:** O. Musin  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1903.05767

## One-line
Extends the Bachoc–Vallentin three-point SDP bound for spherical codes by adding a "spherical cap correction" term $\hat{h}$, then applies it to bound and pin down distance distributions of optimal codes.

## Key claim
For any $F$ in a refined class $\mathcal{F}(n,f_0,T,g,B,\theta)$ of symmetric polynomials (positive-semidefinite in Bachoc–Vallentin sense, with cap-correction $g_T$ in the slack conditions), every $(N,n,\theta)$ spherical code satisfies $N^2 f_0 \le F(1,1,1) + 3(N-1)B + 3N\hat{h}(n,\theta,T,g)$ (Theorem 1, eq. 4), strictly generalizing both Delsarte's LP bound with cap-correction [Musin 2008] and the 3-point SDP bound [Bachoc–Vallentin 2008].

## Method
Three-point SDP on triples $(c,c',c'') \in C^3$: sum $F(c\cdot c', c\cdot c'', c'\cdot c'')$ over all triples; lower-bound via PSD assumption ($\ge N^3 f_0$), upper-bound by splitting diagonal / two-distinct / three-distinct contributions. The novelty is allowing the diagonal slack $F(x,x,1)$ and triangle slack $F(x,y,z)$ to be raised by a cap-correction $g_T(x)$ on a designated subset $T \subset [-1,1)$, with $\hat{h}$ a sup over auxiliary codes in $T$. A graph-refined version (Theorem 2) replaces $N\hat{h}$ with $2\tau(G,\dots)$ where $\tau$ controls the distance graph $DG(C,T)$ — tighter when the contact graph is sparse.

## Result
Theorem 1 yields the unified bound (4); Theorem 2 strengthens it for distance graphs (eq. 8). Corollaries 1–2 give upper/lower bounds on the distance distribution $A(T) = \sum_{t\in T} A_t$ via $A(T) \le \tfrac{2}{N}\lfloor Q\rfloor$ resp. $\ge \tfrac{2}{N}\lceil R\rceil$ (eqs. 5, 6). Example 1 reproves Bannai–Sloane's uniqueness of the $E_8$ kissing distance distribution: $A_{-1}=1$, $A_{\pm 1/2}=56$, $A_0=126$ for the $(240,8,\pi/3)$ code, via explicit polynomials $g_i(t) = (2t-1)t^2(2t+1)^2(t+1)$ plus perturbations $a_i$.

## Why it matters here
Directly informs **kissing-number / sphere-packing problems** in the arena (P1, P6, and any spherical-code subproblem): provides a strictly sharper SDP framework than vanilla Bachoc–Vallentin, with a concrete recipe (Corollaries 1 & 2 + the $g_i$ construction) for forcing distance-distribution uniqueness. The roadmap section explicitly targets $k(4)=24$ uniqueness (24-cell), one-sided kissing $B(5), B(24)$, and Tammes' problem edge-counts via (12) — all candidate arena adjacencies. Adds to wiki: a *cap-correction-via-auxiliary-code* trick missing from the existing Cohn–Elkies / LP-bound pages.

## Open questions / connections
- Can Proposition 1's $2k_2 h_1 + (N-k_1-2k_2-k_3)h_2$ refinement prove $A_{-1}=1$ for the conjectured $(24,4,\pi/3)$ code, closing the 24-cell uniqueness conjecture?
- Generalize Theorems 1–2 to *sphere packings in $\mathbb{R}^n$* using the Musin $H_k$ extensions of Bachoc–Vallentin polynomials — would attack the 24-cell density conjecture ($\delta_4 = 1/8$) past Cohn–Elkies' $\delta_4 < 0.13126$.
- Extend to codes in spherical caps: target $B(5)=32$, $B(24)=144855$ one-sided kissing bounds.
- Cross-pollinate with $k$-point SDP ($k=4,5,6$) for equiangular lines [de Laat–Machado–Oliveira Filho–Vallentin 2018].

## Key terms
semidefinite programming, SDP bound, spherical codes, three-point bound, Bachoc-Vallentin, Gegenbauer polynomials, Delsarte LP bound, kissing number, distance distribution, contact graph, Tammes problem, 24-cell conjecture, $E_8$ uniqueness, cap correction, distance graph
