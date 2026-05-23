---
type: source
kind: paper
title: Extremizers for Fourier restriction on hyperboloids
authors: E. Carneiro, D. O. E. Silva, Mateus Sousa
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1708.03826
source_local: ../raw/2017-carneiro-extremizers-fourier-restriction-hyperboloids.pdf
topic: general-knowledge
cites:
---

# Extremizers for Fourier restriction on hyperboloids

**Authors:** E. Carneiro, D. O. E. Silva, Mateus Sousa  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1708.03826

## One-line
Completes the qualitative picture of sharp $L^2 \to L^p$ adjoint Fourier restriction on the hyperboloid $H^d$ in dimensions $d \in \{1,2\}$: pins down the last even-integer endpoint constant and proves extremizers exist in all non-endpoint cases.

## Key claim
At the endpoint $(d,p)=(1,6)$, the sharp constant is $H_{1,6} = 3^{-1/12}(2\pi)^{1/2}$ and no extremizer exists; in the non-endpoint ranges $d=1,\ 6<p<\infty$ and $d=2,\ 4<p<6$, extremizers do exist.

## Method
Reduce $\|Tf\|_{L^6}^3$ to $\|f\sigma * f\sigma * f\sigma\|_{L^2}$ via Plancherel, then bound by $\sup_x \sigma^{*3}(x)$ using the explicit integral formula derived from Lorentz invariance and recursion in $n$ for $\sigma^{*n}$; the supremum is attained on the boundary $\tau=3$ with value $2\pi/\sqrt{3}$, matched by the extremizing sequence $f_a(y)=e^{-a\langle y\rangle}$ via modified Bessel asymptotics $K_0(2a)\sim \sqrt{\pi/(4a)}\,e^{-2a}$. For existence, a Carleson–Sjölin-type bilinear cap-interaction lemma plus tessellation of $H^d$ into Lorentz-equivalent caps yields a "special cap" containing a universal mass fraction of any extremizing sequence, then Fanelli–Vega–Visciglia concentration-compactness on the Klein–Gordon side (via $H^{1/2}$ and Rellich) closes the dichotomy.

## Result
Endpoint constants on $H^d$ now known in all low-dim even-$p$ cases: $H_{1,6}=3^{-1/12}(2\pi)^{1/2}$ (new), plus Quilodrán's $H_{2,4}=2^{-3/4}\pi$, $H_{2,6}=(2\pi)^{5/6}$, $H_{3,4}=(2\pi)^{5/4}$. All four endpoints fail to admit extremizers (rigidity from strict interior maximum of $\sigma^{*n}$). Every non-endpoint $p$ in $d\in\{1,2\}$ admits an extremizer; argument relies on $p_{\text{low}}$ being an even integer so the convolution structure is available.

## Why it matters here
General background for functional/analytic inequalities; no direct Einstein Arena problem tie, but the methodology — explicit $n$-fold convolution of singular measures, Lorentz-invariant cap tessellation, Bessel-function extremizing sequences, and concentration-compactness with a "special cap" lemma — is a template for sharp-constant problems on non-compact symmetric surfaces, relevant if any arena problem reduces to an extension/restriction sharp inequality.

## Open questions / connections
- Do extremizers exist in dimensions $d \geq 3$ at non-endpoints? Authors' cap argument breaks; bilinear restriction tools (Tao, Candy) likely needed.
- At endpoints $(d,p)$ with $p$ not an even integer, is there always lack of extremizers (analogous rigidity)?
- Extends Quilodrán 2015 (computed three even-$p$ endpoint constants) and Foschi 2007 (paraboloid/cone analogues); part of a broader sharp-restriction program over spheres, paraboloids, cones, hyperboloids.

## Key terms
Fourier restriction, hyperboloid, sharp constants, extremizers, Strichartz inequality, Klein–Gordon propagator, Lorentz invariance, convolution of singular measures, concentration-compactness, Carleson–Sjölin, modified Bessel function $K_0$, cap decomposition, Carneiro, Oliveira e Silva, Quilodrán, Foschi, Fanelli–Vega–Visciglia
