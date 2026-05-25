---
type: source
kind: paper
title: Well-Separated Spherical Designs
authors: A. Bondarenko, D. Radchenko, M. Viazovska
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1303.5991
source_local: ../raw/2013-bondarenko-well-separated-spherical-designs.pdf
topic: general-knowledge
cites:
---

# Well-Separated Spherical Designs

**Authors:** A. Bondarenko, D. Radchenko, M. Viazovska  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1303.5991

## One-line
Proves that for every $N \geq C_d t^d$ there exists a spherical $t$-design on $S^d$ of $N$ points whose pairwise distances are simultaneously $\Omega(N^{-1/d})$ — asymptotically optimal cardinality AND optimal separation.

## Key claim
**Theorem 1:** For each $d \geq 2$ there exist constants $C_d, \lambda_d > 0$ such that for every $t \in \mathbb{N}$ and every $N > C_d t^d$, there exists a spherical $t$-design $\{x_i\}_{i=1}^N \subset S^d$ with $|x_i - x_j| \geq \lambda_d N^{-1/d}$ for $i \neq j$. This is the optimal cardinality (matches the lower bound $N(d,t) \geq c_d t^d$ from Delsarte–Goethals–Seidel) together with the optimal separation (matches the isodiametric upper bound).

## Method
Nonconstructive topological-degree argument extending the authors' earlier Brouwer-fixed-point approach (Bondarenko–Radchenko–Viazovska, Annals 2013). Build a convex area-regular partition $\{R_1, \dots, R_N\}$ of $S^d$ with diameter $\leq K_d N^{-1/d}$ (each cell contains a spherical cap of radius $\sim b_d N^{-1/d}$), then define continuous maps $x_i: \mathcal{P}_t \to R_i$ that move $x_i$ toward the maximizer of $\langle \cdot, \nabla P(x_i)\rangle$ in $R_i$ but stop short by a factor $(1-\delta)$, keeping points away from cell boundaries. Spherical Marcinkiewicz–Zygmund inequalities (Mhaskar–Narcowich–Ward) plus a topological-degree existence theorem then force a zero $P^* \in \Omega$ of the centroid map $f(P) = \sum G_{x_i(P)}$, yielding both the design property and the separation.

## Result
For every $d \geq 2$ and $t \in \mathbb{N}$, well-separated spherical $t$-designs of size $N = O(t^d)$ exist on $S^d$. This settles a prediction of An–Chen–Sloan–Womersley and Hesse–Leopardi: such designs are asymptotically optimal not only for equal-weight quadrature but also for Riesz $s$-energy minimization, packing, and Korevaar–Meyers' spherical Faraday-cage potential. New auxiliary results: (i) Proposition 1 — convex area-regular partitions of $S^d$ of diameter $\leq K_d N^{-1/d}$ for every $N$ (extending Alexander's $S^2, N=6n^2$ construction via Lemma 1 on equal-mass rectangle partitions of $M$-uniform measures); (ii) Lemma 2 — a gradient-norm MZ inequality $(1-8d\eta) \int |\nabla P| \leq \frac{1}{N}\sum |\nabla P(x_i)| \leq (1+8d\eta)\int |\nabla P|$.

## Why it matters here
Directly relevant to Einstein Arena problems involving spherical configurations — kissing-number / sphere-packing problems on $S^d$, autocorrelation-style quadrature problems, and any "distribute $N$ points on a sphere" minimal-energy setup. The construction is nonconstructive (topological degree), so it gives **existence + cardinality + separation guarantees** that bound the search space but does not hand over coordinates; arena work would still need explicit constructions (Hardin–Sloane) or numerical optimization for concrete $N$.

## Open questions / connections
- Explicit construction of $O(t^d)$-point well-separated $t$-designs — the proof is nonconstructive; matching constants in $C_d, \lambda_d$ to known explicit families (Hardin–Sloane snub-cube-type) remains open.
- Extends Bondarenko–Radchenko–Viazovska 2013 (Annals, optimal asymptotic bounds without separation) and Bondarenko–Viazovska 2010 (Brouwer fixed point, weaker bound).
- Hesse–Leopardi conditional: well-separated optimal designs ⇒ asymptotically minimal Riesz $s$-energy — now unconditional for $s$ in the relevant range.
- Sharp constants $C_d$ and $\lambda_d$, and the dimension dependence (the proof gives $C_d, \lambda_d$ but they are not optimized).

## Key terms
spherical t-design, well-separated configuration, topological degree theory, Marcinkiewicz-Zygmund inequality, area-regular partition, geodesic convexity, Riesz s-energy, Korevaar-Meyers conjecture, Faraday cage, sphere packing, kissing number, Brouwer fixed point, Delsarte-Goethals-Seidel bound, Bondarenko-Radchenko-Viazovska, Viazovska
