---
type: source
kind: paper
title: Computation of Laplacian eigenvalues of two-dimensional shapes with dihedral symmetry
authors: David Berghaus, Robert Stephen Jones, Hartmut Monien, Danylo Radchenko
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2210.13229v1
source_local: ../raw/2022-berghaus-computation-laplacian-eigenvalues-two-dimensio.pdf
topic: general-knowledge
cites: 
---

# Computation of Laplacian eigenvalues of two-dimensional shapes with dihedral symmetry

**Authors:** David Berghaus, Robert Stephen Jones, Hartmut Monien, Danylo Radchenko  ·  **Year:** 2022  ·  **Source:** http://arxiv.org/abs/2210.13229v1

## One-line
Numerically computes Laplacian eigenvalues of dihedrally-symmetric 2D shapes to ~1000-digit precision and extracts closed-form $1/n$ asymptotic expansions whose coefficients involve Riemann zeta values and single-valued multiple zeta values.

## Key claim
For regular $n$-gons (area $\pi$), the lowest Dirichlet eigenvalue admits an expansion $\lambda_1(n) \sim j_{0,1}^2 \sum_{k\geq 0} C_k(x)/n^k$ with $x=j_{0,1}^2$, where coefficients $C_k(x)$ are polynomials in $x$ of degree $\lfloor (k-3)/2\rfloor$ whose coefficients lie in the algebra of multiple zeta values; the authors compute $C_k$ up to $k=16$ (extending prior $k\leq 8$), with single-valued MZVs like $\zeta_{sv}(3,5,3)$, $\zeta_{sv}(5,3,5)$ first appearing at $k=11$. Analogous expansions are conjectured for Neumann polygons, regular star polygons $\{n,q\}$ (involving alternating MZVs), and smooth star / hypocycloid shapes.

## Method
Method of Particular Solutions (MPS) with Fourier–Bessel expansions on dihedral fundamental triangle, combined with **domain decomposition**: split the fundamental region into two sub-regions, expand from different vertices, and point-match eigenfunctions + normal derivatives along the interior boundary. Computed via Arb arbitrary-precision arithmetic in Julia/Nemo at $\sim 1.2N$ working digits to handle ill-conditioned point-matching matrices (largest $3039\times 3039$ at 3647 digits). Coefficients extracted by Richardson extrapolation on $\sim 650$ polygons computed to $\geq 980$ digits, then LLL (via Pari) identifies closed-form rational combinations of (single-valued) zeta values.

## Result
Computed 8 new Dirichlet expansion coefficients $C_9,\ldots,C_{16}$ for regular polygons; 17 coefficients for Neumann polygons; 9 coefficients for star polygons (with explicit $q$-polynomial dependence, recovering $q=1$ as the convex case); $\sim 23$ coefficients for smooth star shapes $r(\theta)=R+d\cos(n\theta)$ with $d=n^{-m}$ (these are rational polynomials in $x$); hypocycloid coefficients $C_0=1$, $C_1\approx 0.37229$, $C_2\approx 1.16088$, $C_3\approx 1.87230$ to ~65 digits but no closed form found. Total compute: 2.7 million thread-hours.

## Why it matters here
General background; no direct arena tie. The MPS + domain-decomposition + Arb + Richardson + LLL **pipeline** is a transferable template for any wiki problem requiring high-precision numerical discovery of closed-form constants (e.g., extremal-configuration energies, autocorrelation extrema, packing densities) — compute to many digits, then PSLQ/LLL against candidate basis (zeta values, MZVs, $\pi$, Bessel zeros).

## Open questions / connections
- Rigorous proof that Neumann, star, and smooth-shape coefficients lie in MZV / alternating-MZV algebras (Dirichlet proved through $C_{14}$ in companion arXiv:2103.01057; $C_{15}, C_{16}$ still conjectural).
- Closed-form expressions for hypocycloid limit constants $C_1, C_2, C_3$ — currently only numerical to 65 digits; what basis do they live in?
- Whether the $1/n$ expandability extends to all smoothly-deforming families of shapes converging to a circle, and what governs the appearance of single-valued vs. ordinary MZVs.

## Key terms
Laplacian eigenvalues, method of particular solutions, domain decomposition, Fourier-Bessel expansion, regular polygons, hypocycloid, star polygons, Dirichlet boundary, Neumann boundary, multiple zeta values, single-valued MZV, Riemann zeta, LLL algorithm, Richardson extrapolation, Arb arbitrary precision, point matching, Bessel function zeros, asymptotic expansion, PSLQ closed-form discovery
