---
type: source
kind: paper
title: Majorization and minimal energy on spheres
authors: Oleg R. Musin
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2001.04067v4
source_local: ../raw/2020-musin-majorization-minimal-energy-spheres.pdf
topic: general-knowledge
cites: 
---

# Majorization and minimal energy on spheres

**Authors:** Oleg R. Musin  ·  **Year:** 2020  ·  **Source:** http://arxiv.org/abs/2001.04067v4

## One-line
Uses Karamata's majorization inequality to characterize point configurations on spheres that minimize $f$-potential energy for *all* convex decreasing $f$ simultaneously (called M-sets).

## Key claim
If $X \subset S^{n-1}$ is an M-set with respect to a distance functional $\rho$, then $X$ minimizes $E_f(X) = \sum_{i<j} f(\rho(x_i,x_j))$ for every convex decreasing $f$. Regular simplices are the unique M-sets of cardinality $n+1$ on $S^{n-1}$ under $\rho = r^s$ with $s \le 2$ (Thm 4.1); regular $n$-gons are the unique M-sets on $S^1$ under angular distance (Thm 3.2); and for $n+k$ points ($2 \le k \le n$) at minimum distance $\ge \sqrt{2}$, the M-sets are orthogonal products of regular simplices (Thm 4.2).

## Method
Generalizes the Karamata majorization theorem $A \triangleright B \Rightarrow \sum f(a_i) \le \sum f(b_i)$ to multisets of pairwise distances $R_\rho(X)$ on a metric space. M-sets are defined as maximal elements of the majorization partial order on $\{R_\rho(X) : |X|=m\}$. Optimality proofs use $\sum_{i,j} p_i \cdot p_j = \|\sum p_i\|^2 \ge 0$ (a Gegenbauer/PSD constraint at $k=1$), Lagrange multipliers for small cases, and Kuperberg's theorem for the constrained-distance case. Section 6 ties M-sets to spherical $f$-designs via Delsarte's LP bound on Gegenbauer expansions.

## Result
- $M(S^{n-1}, r^s, n+1)$ = regular $n$-simplices for $s \le 2$.
- $M(S^1, \varphi, n)$ = vertices of regular $n$-gons.
- $M(S^1, r^s, 3)$: regular triangles for $s \le \log_{4/3}(9/4) \approx 2.8188$; bifurcates to a family of isoceles triangles for $s$ beyond this threshold (Thm 5.1).
- $M(B^n, r^s, \sqrt{2}, n+k)$ = orthogonal product of $k$ regular simplices summing to dimension $n$.
- Every $f$-design with non-negative Gegenbauer coefficients is an M-set with $\rho = -f(x\cdot y)$ (Thm 6.2).

## Why it matters here
Directly relevant to **kissing-number / sphere-packing / spherical-code** problems on the arena: the M-set framework is a *universal optimality* principle — one configuration minimizes *all* convex decreasing potentials at once, so finding M-sets sidesteps the choice of potential. Connects Cohn–Kumar universal optimality, Delsarte LP bounds, and spherical designs into a single majorization picture. Provides exact theorems for $n+1$ and $2n$ point configurations on $S^{n-1}$ that are immediate baselines/upper-bound certificates for any arena problem in those regimes.

## Open questions / connections
- Describe $M(S^{n-1}, \varphi, n+1)$ for $n \ge 3$ — Musin conjectures a 2-parameter family of tetrahedra $\Delta_{a,\theta}$ for $n=3$.
- Find $M(S^2, r^s, 5)$ — would resolve TBP-vs-pyramid Riesz energy minimization across all $t$ (currently known TBP-optimal for $t < 15.048$, non-optimal for $t > 15.04081$).
- Conjecture: logarithmic energy of $n+k$ points on $S^{n-1}$ is minimized by $k$ orthogonal regular simplices ($k=3,\ldots,n-1$ open).
- Classification of maximal $f$-designs of degree $\ge 2$ with $a+b > 0$; which graphs embed as $f$-designs?

## Key terms
majorization inequality, Karamata, M-sets, universal optimality, spherical f-design, Delsarte LP bound, Gegenbauer polynomials, Cohn-Kumar, regular simplex, cross-polytope, Riesz energy, Thomson problem, Tammes problem, triangular bipyramid, two-distance sets, equiangular lines, Kuperberg, Rankin, Musin
