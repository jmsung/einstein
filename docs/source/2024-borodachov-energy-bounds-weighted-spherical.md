---
type: source
kind: paper
title: Energy bounds for weighted spherical codes and designs via linear programming
authors: Sergiy Borodachov, Peter Boyvalenkov, Peter Dragnev, Douglas Hardin, Edward Saff, Maya Stoyanova
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2403.07457v2
source_local: ../raw/2024-borodachov-energy-bounds-weighted-spherical.pdf
topic: general-knowledge
cites: 
---

# Energy bounds for weighted spherical codes and designs via linear programming

**Authors:** Sergiy Borodachov, Peter Boyvalenkov, Peter Dragnev, Douglas Hardin, Edward Saff, Maya Stoyanova  ·  **Year:** 2024  ·  **Source:** http://arxiv.org/abs/2403.07457v2

## One-line
Extends the Delsarte–Yudin/Levenshtein LP energy-bound framework to *weighted* spherical codes, producing universal lower and upper bounds on weighted $h$-energy via a single effective cardinality $N_W = 1/\sum w_i^2$.

## Key claim
For a weighted code $(C,W)$ on $S^{n-1}$ with $N_W \in (D(n,m), D(n,m+1)]$ and absolutely monotone potential $h$, $E_h(W) \ge \sum_{i=0}^{k-1+\varepsilon} \rho_i\, h(\alpha_i)$, where $(\alpha_i, \rho_i)$ are the Levenshtein-quadrature nodes/weights at $L_m(n,s) = N_W$ (ULB, Theorem 2.3); a parallel upper bound (UUB, Theorem 4.2) holds for fixed maximal inner product $s$, with a refined extension when $(C,W)$ is also a weighted $\tau$-design.

## Method
Delsarte–Yudin LP relaxation in the Gegenbauer basis: feasible polynomials $f(t) \le h(t)$ on $[-1,1)$ with nonnegative Gegenbauer coefficients $f_i \ge 0$, $i \ge 1$, giving $E_h(C,W) \ge f_0 - f(1)\sum w_i^2$. The replacement $N \to N_W := 1/\sum w_i^2$ (always $\le N$, equal iff equi-weighted) plugs directly into the Levenshtein quadrature machinery; the optimal $f$ in degree $\le m$ is the Hermite interpolant to $h$ at the Levenshtein nodes, with positive-definiteness from Krein / strengthened-Krein conditions on Jacobi-polynomial products.

## Result
ULB and UUB are derived in closed form for degrees 1 and 2 and computed numerically through degree 9. Worked examples: weighted pentakis dodecahedron $(C_{32},W) \subset S^2$ (icosahedron weight $5/168$, dodecahedron weight $9/280$, a weighted spherical 9-design) — for the Coulomb potential, ULB $\approx 0.804786$, actual $\approx 0.8050318$, UUB $\approx 0.8234054$, and design-strengthened UUB $\approx 0.805816$. A weighted cube∪crosspolytope family yields weighted 5-designs in $S^{n-1}$ with comparably tight strips for $n=3,\dots,7$. The bounds are universal in three senses: Cohn–Kumar (one attainer optimal for all absolutely monotone $h$), Levenshtein (one bound per $W$), and parameter-universal (nodes/weights depend on $W,n$ only, not $h$).

## Why it matters here
General background for LP-based universal bounds on the sphere; informs concepts/techniques pages on Delsarte–Yudin LP, Levenshtein quadrature, Cohn–Kumar universal optimality, and spherical designs. Most directly tied to kissing-number and sphere-packing-style arena problems where weighted configurations or Gauss-quadrature node placement appear; the $N_W$ substitution is a clean generalization worth knowing when arena weights are non-uniform.

## Open questions / connections
- Necessary + sufficient optimality of ULB beyond strictly absolutely monotone potentials with $h'(-1) > 0$ — what happens at the boundary case?
- Authors flag a forthcoming companion paper applying Theorem 5.3 to polarization (max–min energy) of weighted spherical designs.
- Extends [Boyvalenkov–Dragnev–Hardin–Saff–Stoyanova 2016, 2020] equi-weighted ULB/UUB; complements Cohn–Kumar (2007) and Levenshtein (1992, 1998) — natural next step is three-point / SDP refinement à la Cohn–Woo (2012).

## Key terms
Delsarte–Yudin LP, Levenshtein bound, Cohn–Kumar universal optimality, Gegenbauer polynomials, Jacobi polynomials, weighted spherical design, Hermite interpolation, Gauss quadrature, Krein condition, absolutely monotone potential, pentakis dodecahedron, Fejes Tóth potential
