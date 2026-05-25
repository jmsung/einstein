---
type: source
kind: paper
title: High Order Finite Difference Schemes for the Heat Equation Whose Convergence Rates are Higher Than Their Truncation Errors
authors: A. Ditkowski
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1711.07926
source_local: ../raw/2017-ditkowski-high-order-finite-difference.pdf
topic: general-knowledge
cites:
---

# High Order Finite Difference Schemes for the Heat Equation Whose Convergence Rates are Higher Than Their Truncation Errors

**Authors:** A. Ditkowski  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1711.07926

## One-line
Constructs finite-difference schemes for the heat equation whose actual convergence rates exceed their formal truncation-error order by engineering the truncation error to be highly oscillatory so the parabolic dissipation kills it.

## Key claim
"Error Inhibiting Schemes" (EIS): block FD schemes with truncation error $\tau = O(h)$ can achieve global error $O(h^2)$ or $O(h^3)$, and schemes with $\tau = O(h^3)$ can achieve $O(h^5)$, because high-frequency components of $T_e$ decay at rate $e^{-(N/2)^2 t}$ under the semi-discrete heat operator, contributing only $O(h^{\alpha+2})$ to the error rather than $O(h^\alpha)$.

## Method
Two-point and three-point block finite-difference stencils on staggered sub-grids ($x_j, x_{j+1/2}$ or $x_j, x_{j+1/3}, x_{j+2/3}$) with a free parameter $c$ controlling an oscillatory $(-1)^j$-type term in the truncation error. Eigenanalysis of the discrete operator $Q$ (symbols $\hat{Q}_{1,2}(\omega)$) shows the high-frequency mode is damped by the parabolic $-\omega^2$ spectrum, so tuning $c$ (e.g. $c=-1/4$ for the 2-point block, $c=-0.385$ for the 5th-order 3-point block) cancels the leading smooth error and leaves only dissipated oscillatory residue. Optional post-processing convolution filter (à la Cockburn–Luskin–Shu–Süli) further boosts accuracy.

## Result
Three concrete schemes: (i) 2-point block with $\tau=O(h)$ achieving 3rd-order convergence at $c=-1/4$; (ii) 3-point block with $\tau=O(h)$ achieving 3rd order at $c=1.340$; (iii) 3-point block with $\tau=O(h^3)$ achieving 5th order at $c=-0.385$. Numerical experiments on $u_t = u_{xx} + F$ with $u(x,t)=\exp(\cos(x-t))$ confirm slopes $-2.00$ to $-5.04$ on log-log convergence plots. Post-processing with a spectral filter recovers 4th order from the $c=-1/4$ scheme. Operation counts sit between standard 2nd/4th-order and 4th/6th-order schemes.

## Why it matters here
General background; no direct arena tie — this is numerical PDE / finite-difference methodology, not extremal combinatorics, packing, or autocorrelation. The "engineer error spectrum into the dissipative null space" idea has a faint analogy to designing magic functions whose Fourier mass lies where it does no harm (Cohn–Elkies), but the connection is metaphorical rather than technical.

## Open questions / connections
- Whether analogous error-inhibiting schemes exist for hyperbolic problems (no dissipation to absorb oscillatory error — author flags as open).
- Optimal choice of post-processing kernel (spectral $O(N\log N)$ vs local $O(N)$) for these specific schemes.
- Relation to Supra-Convergence phenomenon (Kreiss–Manteuffel–Swartz–Wendroff–White 1986) on irregular grids.

## Key terms
finite difference, heat equation, error inhibiting scheme, truncation error, semi-discrete, Lax-Richtmyer equivalence, block scheme, eigenvalue analysis, dissipation, supra-convergence, post-processing filter, Cockburn-Shu, Ditkowski, parabolic PDE, oscillatory error
