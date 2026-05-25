---
type: source
kind: paper
title: Bounds for the sum of distances of spherical sets of small size
authors: Alexander Barg, Peter Boyvalenkov, Maya Stoyanova
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2105.03511v2
source_local: ../raw/2021-barg-bounds-sum-distances-spherical.pdf
topic: general-knowledge
cites: 
---

# Bounds for the sum of distances of spherical sets of small size

**Authors:** Alexander Barg, Peter Boyvalenkov, Maya Stoyanova  ·  **Year:** 2021  ·  **Source:** http://arxiv.org/abs/2105.03511v2

## One-line
Explicit lower and upper bounds for the sum of pairwise distances $\tau_n(C_N) = \sum_{i,j} \|z_i - z_j\|$ of a spherical code of size $N = \Theta(n^\alpha)$, $0 < \alpha \le 2$, derived by specializing Levenshtein-type universal energy bounds.

## Key claim
For codes on $S^{n-1}$, the sum of distances satisfies $\tau(n,N) \le \sqrt{2}\,N^2 - \Theta(\text{lower-order})$, with three explicit closed-form upper bounds $\tau_1, \tau_2, \tau_3$ valid on the cardinality segments $[2, n+1]$, $[n+1, 2n]$, $[2n, n(n+3)/2]$ — attained by the simplex code, biorthogonal code, and codes meeting the 3rd Levenshtein bound, respectively. Matching lower bounds $\tau^{(i)}(n,N,s)$ hold when the maximum inner product $s$ is bounded.

## Method
Specialize the Universal Lower Bounds (ULB) of Boyvalenkov–Dragnev–Hardin–Saff–Stoyanova [14] and Universal Upper Bounds (UUB) [16] for absolutely monotone potentials to $L(t) = -\sqrt{2(1-t)}$ (since $2 + L(t)$ is absolutely monotone). The bounds use Delsarte LP with Gegenbauer polynomial expansion, with parameters $(\rho_i, \alpha_i)$ from the Levenshtein hierarchy on segments $[D^*(n,m), D^*(n,m+1))$ where $D^*$ is the Delsarte–Goethals–Seidel design bound. Stolarsky's invariance principle $\tau_n(C_N)/N^2 + c_n D_{L^2}(C_N) = W(S^{n-1})$ links sum-of-distances to quadratic spherical-cap discrepancy.

## Result
Three explicit bounds, e.g. $\tau_1(n,N) = N\sqrt{2N(N-1)}$ (simplex, $N \le n+1$); $\tau_2(n,N)$ a closed form attained by the biorthogonal code ($n+1 \le N \le 2n$); $\tau_3(n,N)$ a degree-3 LP bound for $2n \le N \le n(n+3)/2$. Asymptotically, $\tau_3(n,N) = \sqrt{2}N^2 - \frac{\sqrt{2\delta}}{8\sqrt[4]{2}}N^{3/2} + O(N)$ for $N = \delta n^2$, improving the trivial $\sqrt{2}N^2 - N/(4\sqrt[4]{2n}) + O(n^{-2})$ from the average-distance bound. De Caen's equiangular-line families ($M = \frac{4}{9}(n+1)^2$, $s = 1/(2r+1)$) and Kerdock/dual-BCH spherical embeddings closely match the upper bound numerically across $r = 3,\ldots,7$.

## Why it matters here
Direct background for Cohn–Elkies-style LP bounds and Levenshtein universal bounds applied at small $N/n$ regime — relevant to sphere packing (P1), kissing number, and any problem where Delsarte LP at finite cardinality is the tool. Provides closed-form benchmarks for evaluating spherical configurations against universal optimality, complementing existing wiki content on equioscillation and SDP relaxation.

## Open questions / connections
- Higher-degree ($m \ge 4$) closed-form Levenshtein bounds — paper stops at $m=3$ because expressions become unwieldy; could a CAS-assisted derivation extend the hierarchy?
- Tightness at the regime boundary $N = n(n+3)/2$: do strongly-regular-graph embeddings always saturate $\tau_3$?
- Binary-code analogue via Stolarsky's invariance for finite metric spaces [4] — direct port of these bounds to Hamming space.
- Connection to equiangular line maximum-size problem (Jiang–Tidor–Yao–Zhang–Zhao 2021): sum-of-distances upper bound implicitly constrains line-set cardinality.

## Key terms
sum of distances, spherical code, Stolarsky invariance principle, quadratic discrepancy, Levenshtein bound, universal lower bound, universal upper bound, Delsarte linear programming, Gegenbauer polynomials, equiangular lines, strongly regular graphs, simplex code, biorthogonal code, Kerdock code, absolutely monotone potential, Cohn-Kumar universal optimality
