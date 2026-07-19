---
type: source
kind: paper
title: Upper bounds for packings of spheres of several radii
authors: David de Laat, Fernando Mário de Oliveira Filho, F. Vallentin
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1206.2608
source_local: ../raw/2012-laat-upper-bounds-packings-spheres.pdf
topic: general-knowledge
cites:
---

# Upper bounds for packings of spheres of several radii

**Authors:** David de Laat, Fernando Mário de Oliveira Filho, F. Vallentin  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1206.2608

## One-line
Extends the Cohn–Elkies and Delsarte–Goethals–Seidel LP bounds to packings of multiple-radius spheres and spherical caps via semidefinite programming, and uses a tangency-graph refinement to slightly improve the Cohn–Elkies bounds for monodisperse sphere packing in dimensions 4–7 and 9.

## Key claim
A matrix-valued analogue of the Cohn–Elkies magic-function inequality (Theorem 1.3) upper-bounds the density of any translational packing of $N$ convex bodies $K_1,\dots,K_N$ in $\mathbb{R}^n$; together with Theorem 1.2 (spherical caps) and Theorem 1.4 (tangency-graph average-degree refinement), this yields new SDP upper bounds for binary sphere packings in dimensions 2–5 and improved center-density bounds in dimensions 3,4,5,6,7,9 (e.g., $n{=}4$: $0.130587$ vs. Cohn–Elkies $0.13126$; $n{=}3$: $0.184559$ vs. $0.18616$).

## Method
Model packings as weighted independent sets in an infinite conflict graph and bound the weighted independence number by a Lovász-$\vartheta'$-type SDP. Conditions become: matrix of Fourier coefficients (or Jacobi-polynomial coefficients $P_k^n$) PSD for $k\ge 1$, a PSD "constant-term" condition tying to $(\mathrm{vol}\,K_i)^{1/2}(\mathrm{vol}\,K_j)^{1/2}$, and $f_{ij}(x)\le 0$ on the non-overlap region. Numerically: parametrize $\hat f_{ij}(u)=\varphi_{ij}(\|u\|)e^{-\pi\|u\|^2}$ with Laguerre $L_k^{n/2-1}$ basis, encode SOS via SDP, solve with SDPA-GMP at 256-bit precision, then rationalize and project for rigorous bounds.

## Result
Binary sphere-packing upper bounds plotted for $n=2,\dots,5$ across radius ratio $r\in[0.2,1]$: e.g., $n{=}3$, $r=\sqrt{2}-1$ gives $\le 0.813$ (vs. NaCl-alloy lower bound $0.793$, gap $<3\%$); $r=0.2247$ gives $\le 0.8617$ (vs. $0.8245$). Theorem 1.2 gives sharp bounds for the 5-prism and truncated-octahedron spherical-cap packings, proving maximality. Theorem 1.4 (combining tangency-graph LP with Bachoc–Vallentin kissing-number SDP bounds) gives the strictly-better center-density bounds in Table 1.

## Why it matters here
Provides the SDP generalization of the Cohn–Elkies LP bound to multi-body/multi-radius packings — directly relevant to any arena problem combining sphere/cap packing with heterogeneous objects (binary packing, polydisperse jammed configurations, unequal-radius spherical codes). Also: the rigorous-bound-from-floating-point recipe (strictly-feasible analytic-center solve → Cholesky-rationalize → distribute residual into PSD slack) is a reusable template for any of our SDP bounds where SDPA-GMP outputs need to be certified.

## Open questions / connections
- Does Theorem 1.3 reproduce / beat Florian's planar binary-circle bound for $r<1$? Authors show it is worse at $r=1/2$ ($0.91744$ vs Florian $0.91581$) — open whether this is intrinsic or due to restricted SOS parametrization.
- Periodicity of the LP/SDP bound for spherical caps in $n=3$ (and apparently higher $n$) — observed numerically, no proof.
- Limit as $r\to 0$ of the binary-sphere bound — numerically inaccessible due to SDP conditioning; analytic behavior unknown.
- Conjectured optimality of the $\mathrm{NaCl}$-alloy at $r=\sqrt{2}-1$ in $n=3$ — authors believe provable given <3% gap.

## Key terms
Cohn-Elkies bound, Delsarte-Goethals-Seidel LP, semidefinite programming, Lovász theta number, weighted theta prime, binary sphere packing, polydisperse spheres, spherical cap packing, Jacobi polynomials, Laguerre polynomials, Schoenberg theorem, Bachoc-Vallentin, kissing number, Poisson summation, sum-of-squares, rigorous SDP rounding, SDPA-GMP, magic function
