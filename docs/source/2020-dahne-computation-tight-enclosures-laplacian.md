---
type: source
kind: paper
title: Computation of Tight Enclosures for Laplacian Eigenvalues
authors: J. Dahne, B. Salvy
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2003.08095
source_local: ../raw/2020-dahne-computation-tight-enclosures-laplacian.pdf
topic: general-knowledge
cites:
---

# Computation of Tight Enclosures for Laplacian Eigenvalues

**Authors:** J. Dahne, B. Salvy  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2003.08095

## One-line
Certified high-precision enclosures (up to 100+ digits) of fundamental Dirichlet–Laplacian eigenvalues on spherical triangles, via the method of particular solutions combined with interval arithmetic and Taylor models.

## Key claim
The method of particular solutions (MPS), previously dismissed for certified computation because it cannot guarantee the eigenvalue index, *can* be made fully rigorous: the authors certify 100 digits of $\lambda_1 \approx 5.15914564246654171122\ldots$ for the spherical triangle with angles $(2\pi/3, 2\pi/3, 2\pi/3)$ (the 3D Kreweras cone), plus 20–168 certified digits for the other 9 unresolved spherical triangles from Bogosel et al.

## Method
MPS expands a candidate eigenfunction as $u = \sum_k c_k u_k$ in basis solutions of $\Delta u + \lambda u = 0$ (sines × Bessel functions in the plane; sines × Ferrers / associated Legendre functions $P_\nu^{-k\alpha}(\cos\theta)$ on the sphere), choosing $\lambda$ to minimize the smallest singular value $\sigma(\lambda)$ of the boundary-evaluation matrix penalized by interior unit-norm constraint. Certification uses the Moler–Payne a posteriori bound $|\lambda - \lambda^*|/\lambda^* \le \sqrt{\mathrm{Vol}(\Omega)}\, \max_{\partial\Omega}|u|\,/\,\|u\|_2$ where the numerator is bounded via Taylor models (cancellation-robust) computed from the linear ODE recurrences for Bessel/Ferrers coefficients, and the denominator via either a verified 1D integrator (orthogonal case) or a superharmonicity argument $\inf_{\Omega'} u \ge \inf_{\partial\Omega'} u$ combined with the spherical Faber–Krahn inequality (multi-singular case). For triangles with $\ge 2$ singular corners, corner-only expansions fail to converge; the fix is to add an interior-point expansion. Index certification uses domain monotonicity: embed $\Omega$ in a spherical cap-sector whose second eigenvalue (a Ferrers-function zero) exceeds the computed $\lambda$.

## Result
- 10 spherical triangles tabulated, all certified rigorously: 6 "regular" (≤1 singular corner) reach 20–168 digits; 4 "singular" (≥2 singular corners) reach 20–110 digits.
- 3D Kreweras: $\lambda_1 = 5.1591456424665417112216748625993501893151700566462081663\ldots$ (100+ digits), giving asymptotic exponent $\alpha = -1 - \sqrt{\lambda_1 + 1/4} \approx -3.32575700417\ldots$
- Continued-fraction filter shows that if $\alpha$ were rational, its denominator would exceed $9.5 \times 10^{51}$ — strong numerical evidence against a D-finite generating function for 3D Kreweras walks.
- L-shaped planar region used as a calibration example: 27 certified digits with 180 expansion terms.

## Why it matters here
General background; no direct arena tie. The methodology — high-precision certified enclosures via a posteriori bounds + interval arithmetic + Taylor models on ODE-defined basis functions — is a transferable template for any Einstein Arena problem where a small approximate residual must be converted into a rigorous bound (relevant to triple-verify discipline for problems involving spectra, eigenvalue bounds, or Cohn–Elkies-style positivity certificates).

## Open questions / connections
- Does the 3D Kreweras generating function satisfy *any* linear ODE? The $>10^{51}$ denominator bound is strong evidence against D-finiteness but not a proof.
- Can the interior-point-plus-corners trick be replaced by a principled basis-completion rule, or is it inherently heuristic?
- Extends Betcke–Trefethen (2005) MPS revival and Jones (2017) high-precision MPS by adding rigorous certification; complements Liu–Oishi FEM-based certified bounds (which scale poorly in precision).
- Gómez-Serrano–Orriols (2019) "three eigenvalues do not determine a triangle" uses the same superharmonicity-based norm lower bound — extended here from planar to spherical singular triangles.

## Key terms
method of particular solutions, Laplace-Beltrami eigenvalue, Dirichlet eigenvalue, spherical triangle, Moler-Payne bound, Taylor models, interval arithmetic, Arb ball arithmetic, Faber-Krahn inequality, Ferrers function, Bessel function, 3D Kreweras walks, D-finite generating function, certified enclosure, Betcke-Trefethen, domain monotonicity
