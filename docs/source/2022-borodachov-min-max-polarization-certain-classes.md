---
type: source
kind: paper
title: Min-Max Polarization for Certain Classes of Sharp Configurations on the Sphere
authors: S. Borodachov
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2203.13756
source_local: ../raw/2022-borodachov-min-max-polarization-certain-classes.pdf
topic: general-knowledge
cites:
---

# Min-Max Polarization for Certain Classes of Sharp Configurations on the Sphere

**Authors:** S. Borodachov  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2203.13756

## One-line
Proves that antipodal sharp and strongly sharp (even-strength design) point configurations on $S^d$ minimize the maximum total potential over the sphere for any completely monotone potential.

## Key claim
For $f:[0,4]\to\mathbb{R}$ continuous on $[0,4]$ and completely monotone on $(0,4]$ (modulo an additive constant), any strongly $m$-sharp or antipodal $m$-sharp configuration $\omega_N^*\subset S^d$ minimizes $Q_f(\omega_N;S^d):=\max_{x\in S^d}\sum_{i=1}^N f(|x-x_i|^2)$ over all $N$-point multisets, and the max is attained at points of $\omega_N^*$ itself (Theorem 2.5).

## Method
Delsarte–Yudin linear programming: build a polynomial $Q\in P_L$ that Hermite-interpolates $g(t)=f(2-2t)$ at the design's dot-product values $\{\tau_i\}$ and satisfies $Q\ge g$ on $[-1,1]$ (Lemma 3.1, using convexity of $g^{(L)}$). Since $\omega_N^*$ is an $L$-design, $\sum_i Q(z\cdot x_i)$ is constant in $z$ (Funk–Hecke), so $p_f(z)\le\sum_i Q(z\cdot x_i)=p_f(y)$ for any $y\in\omega_N^*$. Combined with Cohn–Kumar universal optimality of sharp configurations for the dual (min-energy) problem to handle the cross-configuration comparison.

## Result
- Theorem 2.3: strongly $m$-sharp $\Rightarrow$ max of $p_f$ attained at $\omega_N$ when $f^{(2m-1)}$ concave on $(0,4)$.
- Theorem 2.4: antipodal $m$-sharp $\Rightarrow$ same conclusion when $f^{(2m-2)}$ convex on $(0,4)$.
- Theorem 2.5 + Corollaries 2.6/2.7: covers Riesz $|x-y|^s$ ($-2<s<0$) and Gaussian $e^{-\sigma|x-y|^2}$ kernels.
- Optimal configs include: regular $N$-gon ($S^1$), regular simplex ($d+2$ pts on $S^d$), cross-polytope, icosahedron (12 pts on $S^2$), $E_8$ minimal vectors (240 on $S^7$), Leech minimal vectors (196560 on $S^{23}$), Schläfli (27 on $S^5$), McLaughlin (275 on $S^{21}$), kissing configs on $S^6$, $S^{22}$.

## Why it matters here
Directly bears on **P1 (sphere packing / kissing-type) and any problem whose objective is a min-max over $S^d$ of a sum of decreasing radial kernels** — gives a clean recipe (find a sharp/antipodal design at the right cardinality) for proving optimality without needing positive-definiteness of the interpolant. Complements existing wiki entries on Cohn–Elkies / Cohn–Kumar universal optimality by extending them from min-energy to min-max polarization.

## Open questions / connections
- Extends Stolarsky [27,28] and Nikolov–Rafailov [24,25] from special configs (simplex, cross-polytope, cube) to all known sharp/antipodal-sharp designs.
- Dual problem (max of min-polarization) for antipodal sharp configs handled separately in Borodachov [6,7] — more subtle, sometimes requires different polynomial.
- No strongly $m$-sharp configurations exist for $m\ge 3$, $d\ge 2$ (Bannai–Damerell), so antipodal branch carries the high-dim cases.
- Open: extension to non-sharp but highly symmetric designs; quantitative gap when $\omega_N$ is near-sharp.

## Key terms
polarization, min-max polarization, sharp configuration, strongly sharp, antipodal configuration, spherical design, tight design, Delsarte-Yudin LP, Cohn-Kumar universal optimality, completely monotone potential, Funk-Hecke formula, Hermite interpolation, Riesz kernel, Gaussian kernel, $E_8$ lattice, Leech lattice, kissing configuration, Stolarsky, Borodachov
