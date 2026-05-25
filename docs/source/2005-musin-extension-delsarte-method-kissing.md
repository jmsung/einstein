---
type: source
kind: paper
title: An extension of Delsarte's method. The kissing problem in three and four dimensions
authors: Oleg R. Musin
year: 2005
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/math/0512649v1
source_local: ../raw/2005-musin-extension-delsarte-method-kissing.pdf
topic: general-knowledge
cites: 
---

# An extension of Delsarte's method. The kissing problem in three and four dimensions

**Authors:** Oleg R. Musin  ·  **Year:** 2005  ·  **Source:** http://arxiv.org/abs/math/0512649v1

## One-line
Extends Delsarte's linear-programming bound by relaxing the global polynomial-negativity constraint, yielding the first complete proofs that $k(3)=12$ and $k(4)=24$.

## Key claim
$k(4) = 24$ (matching the 24-cell lower bound), and a new short proof of $k(3) = 12$ — both obtained by a single extension of the Delsarte/Levenshtein LP method that bypasses the long-standing $k(3)\le 13$ / $k(4)\le 25$ barrier.

## Method
Replace Delsarte's requirement that $f(t)\le 0$ on all of $[-1, z]$ with the weaker requirement $f(t)\le 0$ only on $[-1, t_0]$ for some $t_0 \in (z, 1)$, then bound the contribution from points with inner product in $(t_0, 1)$ combinatorially via spherical-cap geometry (law of cosines, max over $m$-point configurations near the test point). The bound becomes $k(n) \le h_{\max} = \max_m h_m$ where each $h_m$ is a small low-dimensional optimization solvable by polynomial root-finding; Gegenbauer/Legendre expansion coefficients $c_k \ge 0$ are still required so $\sum_{i,j} f(\cos\phi_{ij}) \ge n^2$.

## Result
For $n=3$: an explicit degree-9 polynomial $f$ gives $S(X) < 13n$ and $S(X) \ge n^2$, forcing $n < 13$, so $k(3) = 12$. For $n=4$: a polynomial $f$ with $t_0 > 0.6058$ yields $h_{\max} = \max(h_0,\dots,h_6) < 25$ (with $h_2 \approx 24.864$, $h_6 < 24.934$ dominating), so $k(4) \le 24$; combined with the 24-cell construction, $k(4) = 24$. Also improves $\phi_4(25) < 59.81°$ and $\phi_4(24) < 60.5°$.

## Why it matters here
Canonical example of an LP-bound extension that breaks through where pure Delsarte stalls — directly relevant to any Einstein Arena problem in the [[kissing-number]] / [[sphere-packing]] family where the LP gap is the obstruction. Pairs with [[concepts/cohn-elkies]] and [[techniques/delsarte-lp]] as the "what to do when Delsarte is loose" template.

## Open questions / connections
- Could the same $t_0$-relaxation tighten LP bounds in dimensions 9, 10, 16, 17, 18 (paper hints at $k(9)\le 366$, $k(10)\le 570$)?
- For $n=5,6,7$ the method does *not* improve on Delsarte — why, and is there a structural reason (degeneracy of the $t_0$ region)?
- Connection to Bachoc–Vallentin SDP bound (2008, post-Musin) — does the extension correspond to a specific SDP slice?
- The $h_m$ subproblems are nonconvex but reducible to univariate polynomial roots — generalizable schema for "LP + bounded combinatorial correction"?

## Key terms
kissing number, Delsarte LP method, Gegenbauer polynomials, Legendre polynomials, spherical codes, 24-cell, thirteen spheres problem, Levenshtein bound, Schoenberg positivity, Kabatiansky-Levenshtein, sphere packing, linear programming bound
