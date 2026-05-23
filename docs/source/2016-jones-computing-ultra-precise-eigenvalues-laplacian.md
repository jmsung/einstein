---
type: source
kind: paper
title: Computing ultra-precise eigenvalues of the Laplacian within polygons
authors: R. Jones
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1602.08636
source_local: ../raw/2016-jones-computing-ultra-precise-eigenvalues-laplacian.pdf
topic: general-knowledge
cites:
---

# Computing ultra-precise eigenvalues of the Laplacian within polygons

**Authors:** R. Jones  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1602.08636

## One-line
Extends the Fox–Henrici–Moler point-matching method of particular solutions (MPS) to compute Dirichlet/Neumann Laplacian eigenvalues in polygons (L-shape, cut-square, 5-point star, regular pentagon/hexagon) to hundreds — sometimes >1000 — digits of precision.

## Key claim
With (a) Chebyshev-distributed matching points and (b) sufficient intermediate precision (≈1.4–1.7× the target eigenvalue precision), the point-matching determinant's roots — as the expansion order $N$ increases — *alternate* above and below the true eigenvalue, yielding rigorous-by-inspection bounds $\lambda_\alpha^{[N\downarrow]} < \lambda_\alpha < \lambda_\alpha^{[N\uparrow]}$ with exponential convergence rate $\rho \sim 1/2$ to $1/6$.

## Method
Fourier–Bessel expansion $\Psi^{[N]}(k,r) = \sum_\nu c_\nu J_{m_\nu}(kr)\,\{\sin,\cos\}(m_\nu \tilde\theta)$ centered at the *non-analytic vertex*, with $m_\nu$ chosen as fractional multiples of $\pi/\Delta\phi$ to handle the corner singularity exactly. Boundary conditions are enforced at $N$ Chebyshev-distributed points on non-adjacent edges, producing an $N\times N$ matrix $M^{[N]}(\lambda)$ whose determinant roots are tracked as $N$ increments. Symmetry reduction (reducing to a polygon with at most one non-analytic vertex from which all edges are visible) is essential for convergence and degeneracy disentanglement; computation uses GP/PARI with GMP at thousands-of-digits arbitrary precision.

## Result
Headline: lowest Dirichlet eigenvalue of the unit-edged regular pentagon to 1502 digits ($\lambda_1 \approx 10.99642708\ldots$, OEIS A262823); regular hexagon to 1001 digits ($\lambda_1 \approx 7.15533913\ldots$, A263202); L-shape to 1001 digits (A262701). Table of 100-digit results for cut-square, 5-point star, regular $\sigma$-gons ($\sigma=5,\ldots,10$). Empirical convergence rate $\rho \approx 5/\sigma$ for regular $\sigma$-gons; the 8139th pentagon Dirichlet eigenvalue $\lambda_{8139} \approx 100001.28\ldots$ is bounded to 300 digits.

## Why it matters here
General background; no direct arena tie. The closest connection is *methodological* — the alternation-bound trick (watching a parameter sweep where successive iterates straddle the limit) is a transferable diagnostic pattern, and the "exponential convergence requires precision $\sim 1.5N$ digits" lesson echoes the project's mpmath-polish discipline for P5/P6/P11/P14/P17.

## Open questions / connections
- Can the alternation-bounding heuristic (matching contour "flipping" causing $\lambda^{[N]} A_N \approx \lambda A$ oscillation) be made into a rigorous a posteriori bound rather than empirical?
- Symmetry reduction of the cut-square via the $m \in \{4/7, 8/7, 12/7, \ldots\}$ A/B/C class decomposition — what is the underlying group-theoretic explanation?
- Extends Fox–Henrici–Moler (1967) and Betcke–Trefethen (2004) GSVD; complements Amore et al. (2015) Richardson-extrapolated finite differences.

## Key terms
Helmholtz equation, Laplacian eigenvalues, method of particular solutions, point-matching, collocation, Fox–Henrici–Moler, Betcke–Trefethen, GSVD, Fourier–Bessel expansion, Chebyshev nodes, exponential convergence, eigenvalue bounds, alternation, non-analytic vertex, symmetry reduction, L-shape, regular pentagon, GMP, PARI, arbitrary precision
