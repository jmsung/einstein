---
type: source
kind: paper
title: Universal minima of discrete potentials for sharp spherical codes
authors: Peter Boyvalenkov, Peter Dragnev, Douglas Hardin, Edward Saff, Maya Stoyanova
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2211.00092v2
source_local: ../raw/2022-boyvalenkov-universal-minima-discrete-potentials.pdf
topic: general-knowledge
cites: 
---

# Universal minima of discrete potentials for sharp spherical codes

**Authors:** Peter Boyvalenkov, Peter Dragnev, Douglas Hardin, Edward Saff, Maya Stoyanova  ·  **Year:** 2022  ·  **Source:** http://arxiv.org/abs/2211.00092v2

## One-line
Shows that essentially all known sharp spherical codes (and the icosahedron, dodecahedron, 600-cell) attain universal lower bounds for the *minimum* of discrete potentials, with minima locations independent of the potential.

## Key claim
For sharp codes $C = (n,N,\tau)$ on $S^{n-1}$, the max-min polarization $Q_h(C) := \inf_{x \in S^{n-1}} \sum_{y \in C} h(x \cdot y)$ attains the LP-derived universal lower bound (PULB) $N \sum_{i \in I} \rho_i h(\alpha_i)$ for *every* potential $h$ with $h^{(\tau+1)}$ of constant sign — with explicit $\alpha_i, \rho_i$ from Gegenbauer-zero Gauss-Jacobi quadrature. Exceptions (icosahedron, $E_8$ kissing, Leech kissing) attain a **second-level PULB** built from a "Skip 1–Add 2" $T$-design quadrature on $T = \{1,\dots,2k+2\}\setminus\{2k\}$.

## Method
Linear programming on Gegenbauer expansions: any polynomial $f \leq h$ of degree $\leq \tau$ gives $Q_h(C) \geq Nf_0$; the optimal LP $f$ is the Hermite interpolant of $h$ at quadrature nodes (zeros of $P_k^{(0,\epsilon)}$ or adjacent Jacobi polynomials). For $T$-designs missing one moment, they introduce **PULB-subspaces** spanned by $\{P_j^{(n)}\}_{j=0}^{2k+2} \setminus \{P_{2k}^{(n)}\}$ admitting a quadrature with one extra node, yielding a strictly sharper bound. Existence of a witness point $\bar x \in S^{n-1}$ with $I(\bar x, C)$ matching the quadrature nodes is verified case-by-case using strongly-regular-graph structure (Higman-Sims, Hoffman-Singleton, Gewirtz, Brouwer-Haemers, McLaughlin, Gosset $4_{21}$).

## Result
- **First-level PULB attained** (Theorem 3.1): regular $N$-gon, simplex, cross-polytope, $(5,16,3)$, $(6,27,4)$, $(7,56,5)$, $(21,112,3)$, $(21,162,3)$, $(22,100,3)$, $(22,275,4)$, $(22,891,5)$, $(23,552,5)$, $(23,4600,7)$ — Table 2 gives exact quadrature.
- **Second-level PULB attained** (Theorem 5.1): icosahedron, dodecahedron, $E_8$ kissing $(8,240,7)$ at nodes $\{\pm\sqrt 2/2, \pm\sqrt 2/4, 0\}$ with weights $(14,64,84,64,14)$, Leech kissing $(24,196560,11)$ at nodes $\{\pm\sqrt 6/4, \pm\sqrt 6/6, \pm\sqrt 6/12, 0\}$ with weights $(552, 11178, 48600, 75900, \dots)$.
- **Case $h^{(\tau+1)} \leq 0$** (Theorem 7.1): all strongly sharp and antipodal sharp codes have minimum *at a code point*; 600-cell minimum attained at code points when $h^{(i)} \geq 0$ for $i=1,\dots,15$ and $h^{(16)} \leq 0$ (Theorem 7.2).
- **By-product:** improved Fazekas-Levenshtein covering-radius bound — covering radius $\geq$ largest quadrature node, attained by icosahedron.

## Why it matters here
Directly informs **kissing number / sphere packing** problems where the optimizer minimizes a potential over a known configuration — gives a *closed-form* certified minimum without further optimization, plus the exact witness point (closest-facet construction). The second-level technique generalizes LP duality past the basic Delsarte ceiling and is relevant whenever a configuration is a $T$-design but not a full $\tau$-design — likely useful for arena problems on $E_8$, Leech, and 600-cell-adjacent configurations.

## Open questions / connections
- Infinite family $((q^3+1)(q+1), q(q^3+1)/(q+1), 3)$ for $q = 2^m, m \geq 2$ and the 600-cell under case (i) ($h^{(\tau+1)} \geq 0$) — deferred to future work.
- Generalizes Cohn-Kumar universal optimality (energy) [20] to polarization (min-of-potential) — same configurations are optimal in both senses.
- 600-cell under absolutely monotone $h$ (or $h^{(16)} \geq 0$) is open and "much more complex".
- Extends PULB framework of [15] (Boyvalenkov-Dragnev-Hardin-Saff-Stoyanova 2023) and the energy ULB of [13] (Constr. Approx. 2016).

## Key terms
sharp spherical codes, polarization universal lower bound, PULB, Gegenbauer polynomials, Gauss-Jacobi quadrature, spherical $\tau$-designs, $T$-designs, Delsarte-Goethals-Seidel, Levenshtein quadrature, Cohn-Kumar universal optimality, $E_8$ kissing configuration, Leech lattice, 600-cell, icosahedron, Higman-Sims graph, strongly regular graphs, Fazekas-Levenshtein covering radius, Hermite interpolation LP bound
