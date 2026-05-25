---
type: source
kind: paper
title: "Bounds for spherical codes: The Levenshtein framework lifted"
authors: P. Boyvalenkov, P. Dragnev, D. Hardin, E. Saff, Maya M. Stoyanova
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1906.03062
source_local: ../raw/2019-boyvalenkov-bounds-spherical-codes-levenshtein.pdf
topic: general-knowledge
cites:
---

# Bounds for spherical codes: The Levenshtein framework lifted

**Authors:** P. Boyvalenkov, P. Dragnev, D. Hardin, E. Saff, Maya M. Stoyanova  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1906.03062

## One-line
Lifts the classical Levenshtein LP framework for spherical codes to a "next level" by enlarging the admissible polynomial subspace via skip-two/add-two augmentation, yielding strictly improved universal lower bounds on energy $E_h(n,N)$ and upper bounds on $A(n,s)$.

## Key claim
For $(n,N)$ where the first-level test functions $Q^{(n,N)}_{\tau+3}$ or $Q^{(n,N)}_{\tau+4}$ are negative, a 1/N-quadrature on the skip-two/add-two subspace $\Lambda_{n,k} := P_{\tau(n,N)} \oplus \mathrm{span}\{P^{(n)}_{\tau+3}, P^{(n)}_{\tau+4}\}$ exists under explicit conditions and is a ULB-space; applied at third level it yields a new proof that the 600-cell $W_{120}$ on $S^3$ is universally optimal, with two new LP-optimal polynomials of degree 17 that together with Cohn–Kumar's form the vertices of the convex hull of all LP-optimal solutions.

## Method
Delsarte–Yudin linear programming with Hermite interpolation: extend the admissible subspace $\Lambda$ beyond $P_{\tau(n,N)}$ by adjoining two higher Gegenbauer modes (skip $\tau+1, \tau+2$; add $\tau+3, \tau+4$); establish necessary/sufficient conditions for a 1/N-quadrature rule on $\Lambda$ via expansions in adjacent Jacobi polynomials $P^{1,0}_i$; show the Hermite interpolant of an absolutely monotone $h$ at the new quadrature nodes is positive definite and stays below $h$, certifying LP-optimality. Interlacing of new nodes $\{\beta_i\}$ with Levenshtein nodes $\{\alpha_i\}$ is proved via the Levenshtein polynomial as a test function.

## Result
For $(n,N)=(4,24)$ (24-cell): $\Lambda_{4,3}=P_5 \oplus \mathrm{span}\{P^{(4)}_8,P^{(4)}_9\}$ is a ULB-space; Newton energy bound improves from 333 (level 1) to ≈ 333.16 (level 2), with actual 24-cell energy 334; also yields $A(4,s)\le 23$ for $s$ slightly below $\beta_4$ instead of 24. For $(n,N)=(4,120)$ (600-cell): level-3 lift on subspaces $\Lambda_1 = P_{10} \oplus \mathrm{span}\{P^{(4)}_{13..17}\}$ and $\Lambda_2 = P_{11} \oplus \mathrm{span}\{P^{(4)}_{14..17}\}$ gives a simpler proof of universal optimality than Cohn–Kumar's $\Lambda_3$, with full characterization: every degree-17 LP-optimal polynomial is a convex combination of $f_{h,\Lambda_1}, f_{h,\Lambda_2}, f_{h,\Lambda_3}$.

## Why it matters here
Directly relevant to sphere-packing/kissing problems and to LP-bound technique: when the wiki's first-level Levenshtein/ULB bound (already in `concepts/`) has negative test functions $Q_{\tau+3}, Q_{\tau+4}$, this paper provides the concrete recipe to lift; the 600-cell's optimality proof structure (convex hull of LP-optimal vertices) is a template for "when is the LP bound tight?" diagnostics on other configurations.

## Open questions / connections
- Conjecture 6.1: for each dimension $n$, the set of $N \in [D(n,\tau), D(n,\tau+1)]$ admitting a second-level bound forms an interval — unproven.
- Extends Levenshtein [28], Cohn–Kumar [14], and Cohn–Woo [15]; complements Andreev's [1,2] degree-18 cubic-replacement trick for $\Lambda_3$ at $j=14$.
- When does the level-$\ell$ lift terminate (LP-optimal) vs. require further skip/add iterations? Tied to the $j_0(n)$ index where $Q^{(n,N)}_{2k+3}$ goes negative.
- The 24-cell is *not* universally optimal (Cohn–Conway–Elkies–Kumar [13]); the level-2 LP-optimal polynomial here certifies why LP alone cannot prove it for any absolutely monotone $h$.

## Key terms
Levenshtein bound, Delsarte–Yudin linear programming, universal lower bound, ULB-space, 1/N-quadrature, Gegenbauer polynomials, Jacobi adjacent polynomials, Hermite interpolation, 600-cell, 24-cell, spherical codes, universal optimality, Cohn–Kumar, absolutely monotone potential, test functions, skip-two/add-two subspace, Boyvalenkov
