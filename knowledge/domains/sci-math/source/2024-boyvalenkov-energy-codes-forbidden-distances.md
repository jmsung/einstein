---
type: source
kind: paper
title: Energy of codes with forbidden distances in 48 dimensions
authors: P. Boyvalenkov, P. Dragnev
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2412.07577
source_local: ../raw/2024-boyvalenkov-energy-codes-forbidden-distances.pdf
topic: general-knowledge
cites:
---

# Energy of codes with forbidden distances in 48 dimensions

**Authors:** P. Boyvalenkov, P. Dragnev  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2412.07577

## One-line
Proves universal optimality (over all absolutely monotone potentials) of the four known even unimodular extremal 48-dimensional lattices' minimal-vector configurations as $T$-avoiding spherical codes on $S^{47}$ via Delsarte-Yudin linear programming.

## Key claim
The 52,416,000-point spherical 11-designs from the minimal vectors of $P_{48p}, P_{48q}, P_{48m}, P_{48n}$ are universally optimal for $h$-energy (any absolutely monotone $h$ with $h^{(12)}>0$) among: (i) $T_1$-avoiding antipodal codes or 3-designs with $T_1=(-1/3,-1/6)\cup(1/6,1/3)$, and (ii) all $T_2$-avoiding codes with $T_2=(-1/2,-1/3)\cup(1/3,1/2)$, both at cardinality $N=52416000$.

## Method
Delsarte-Yudin LP framework: construct a degree-11 Hermite interpolant $f$ matching $h$ at the configuration's 8 inner products $\{-1, \pm 1/2, \pm 1/3, \pm 1/6, 0\}$ (doubled at certain nodes), then show (A1) $f\le h$ off $T$ via the Hermite error formula with sign-controlled product, and (A2) all Gegenbauer coefficients $f_i\ge 0$ via Newton-form expansion plus positive-definiteness of partial products $PP_r$ in $P_i^{(48)}$. For $T_1$, $PP_{11}$ has one negative coefficient $g_{3,11}$, salvaged by restricting to antipodal/3-design codes where $M_3(C)=0$. Tight quadrature comes from the 11-design property.

## Result
For absolutely monotone $h$ with $h^{(12)}>0$ on $(-1,1)$, any $T_i$-avoiding code $C\subset S^{47}$ with $|C|=52416000$ satisfies $E_h(C)\ge 36848[h(-1/2)+h(1/2)] + 1678887[h(-1/3)+h(1/3)] + 12608784[h(-1/6)+h(1/6)] + 23766960\,h(0) + h(-1)$ (eqs. 12–13), with equality forcing $C$ to be an antipodal distance-invariant 11-design with the unique distance distribution (10). A matching upper LP bound (Thm 4.6) makes these codes optimal among $T_1$-avoiding 11-designs too.

## Why it matters here
General background for sphere-packing / kissing-number problems (Einstein Arena P1, P2, P3 family) — extends the Cohn-Kumar universal-optimality template from $E_8/\Lambda_{24}$ to dimension 48, and demonstrates the Hermite-interpolation + Gegenbauer-positivity recipe that the LP optimizer in this repo should mirror when the avoiding-distance structure is known.

## Open questions / connections
- Extends [8] (Gonçalves-Vedana lattice density in $\mathbb{R}^{48}$) and [3] (kissing number 52,416,000 in dimension 48) to the energy regime.
- Whether the same four lattices are universally optimal *without* the $T_i$-avoidance constraint (dimension 48 analog of Cohn-Kumar) remains open.
- The trick of allowing one negative Gegenbauer coefficient $g_{3,11}$ by restricting to $M_3(C)=0$ (antipodal / 3-design) is reusable elsewhere — when an LP bound is tantalizingly close, restrict the code class to kill the bad moment.

## Key terms
Delsarte-Yudin LP bound, universal optimality, spherical 11-design, even unimodular extremal lattice, dimension 48, Gegenbauer polynomials, Hermite interpolation, absolutely monotone potential, $h$-energy, $T$-avoiding code, kissing number, Cohn-Kumar, antipodal code, distance distribution, moments $M_i(C)$, positive-definite
