---
type: source
kind: paper
title: Energy bounds for codes in polynomial metric spaces
authors: P. Boyvalenkov, P. Dragnev, D. Hardin, E. Saff, Maya M. Stoyanova
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1804.07462
source_local: ../raw/2018-boyvalenkov-energy-bounds-codes-polynomial.pdf
topic: general-knowledge
cites:
---

# Energy bounds for codes in polynomial metric spaces

**Authors:** P. Boyvalenkov, P. Dragnev, D. Hardin, E. Saff, Maya M. Stoyanova  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1804.07462

## One-line
Unified linear-programming framework that produces universal lower bounds (ULBs) on the potential energy of codes in any polynomial metric space — spheres, projective spaces, Hamming, Johnson — paralleling Levenshtein's universal upper bounds on code cardinality.

## Key claim
For any PM-space $M$ whose $Q$-system satisfies the strengthened Krein condition, an absolutely monotone potential $h$, and a code cardinality $M \in (D(M,2k-1+\varepsilon), D(M,2k+\varepsilon)]$:
$$E_h(M, M) \;\ge\; M^2 \sum_{i=0}^{k-1+\varepsilon} \rho_i\, h(\alpha_i),$$
where $\alpha_i$ are the zeros of Levenshtein's polynomial $f^{(s)}_{2k-1+\varepsilon}$ and $\rho_i$ the positive weights of the associated $1/M$-quadrature rule. The bound is LP-optimal at degree $\le 2k-1+\varepsilon$ and cannot be improved without higher-degree polynomials.

## Method
Linear programming on the $Q$-polynomial expansion: choose the test polynomial $f$ as the Hermite interpolant of $h$ at the Levenshtein nodes $\{\alpha_i\}$, so $f \le h$ on $[-1,1)$ and $f \in F_\ge$. Positive-definiteness ($f_i \ge 0$) follows from a Newton-form expansion of $f$ as a nonnegative combination of partial products, combined with results of Cohn–Kumar (2006) on $Q^{1,\varepsilon}_i$-expansions and the (strengthened) Krein condition. The $1/M$-quadrature rule (10) then turns $M f_0 - f(1)$ into the closed-form weighted sum $M\sum \rho_i h(\alpha_i)$.

## Result
Theorem 4.4 establishes the ULB above and its LP-optimality at degree $\le \tau = 2k-1+\varepsilon$. Theorem 5.2 gives a necessary/sufficient test: defining $P_j(M,s) := 1/L_{2k-1+\varepsilon}(M,s) + \sum_i \rho_i Q_j(\alpha_i)$, the ULB is globally LP-optimal iff $P_j(M,s) \ge 0$ for all $j \ge \tau+1$; if any $P_j < 0$ and $h$ is strictly absolutely monotone, a degree-$j$ polynomial improves the bound. Asymptotic Corollary 6.4: for $S^{n-1}$ and $H(n,2)$ with $M_n \sim n^{k-1+\varepsilon}$, $\liminf E_h(M_n)/M_n^2 \ge h(0)$ and the next-order term is $\ge h''(0)/2$ per dimension. Section 8 adds analogous bounds for $\tau$-designs and for codes with prescribed separation $s$.

## Why it matters here
Direct background for the Cohn–Elkies / LP-bound family used on the sphere-packing and kissing-number problems (P1, kissing dimensions): the ULB framework is the energy-side dual of the Levenshtein cardinality bound and shows exactly when LP cannot be sharpened — useful for diagnosing whether to escalate to SDP / three-point bounds or accept the LP optimum.

## Open questions / connections
- "Lifting" the Levenshtein framework to higher-degree polynomials when $P_j < 0$ — explicit construction of improving polynomials and the next-level test functions (flagged by the authors as future work).
- Extends Cohn–Kumar universal optimality (2006) and Cohn–Woo three-point bounds (2012) to the unified PM-space setting; companion paper (arXiv:1801.07334) handles inner products restricted to $[\ell, s]$.
- Sharp-configuration finiteness: in any fixed dimension $n \ge 3$ only finitely many parameter sets admit sharp configurations attaining the ULB — narrows the search space for universally optimal codes.

## Key terms
polynomial metric space, universal lower bound, linear programming bound, Levenshtein bound, Delsarte-Goethals-Seidel, Krein condition, Q-system, Gegenbauer polynomials, Krawtchouk polynomials, Hahn polynomials, 1/M-quadrature, absolutely monotone potential, spherical code energy, Hamming space, kissing number, sphere packing, Cohn-Kumar, Hermite interpolation
