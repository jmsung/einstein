---
type: source
kind: paper
title: Maximizers for the Stein–Tomas Inequality
authors: R. Frank, E. Lieb, Julien Sabin
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1603.07658
source_local: ../raw/2016-frank-maximizers-stein-tomas-inequality.pdf
topic: general-knowledge
cites:
---

# Maximizers for the Stein–Tomas Inequality

**Authors:** R. Frank, E. Lieb, Julien Sabin  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1603.07658

## One-line
Gives a sharp dichotomy criterion (a strict energy inequality relating the Stein–Tomas constant $R_N$ to the Strichartz constant $S_{N-1}$) under which all maximizing sequences for the adjoint Fourier restriction inequality on $S^{N-1}$ are precompact modulo modulations, hence a maximizer exists in every dimension.

## Key claim
For $N \geq 2$ and $q = 2(N+1)/(N-1)$, if $R_N > \frac{\Gamma((q+1)/2)}{2^{q/2}\sqrt{\pi}\,\Gamma((q+2)/2)} \cdot S_{N-1}$, then every $L^2$-normalized maximizing sequence for $R_N$ is precompact in $L^2(S^{N-1})$ up to modulations, and a maximizer exists. The non-strict inequality $\geq$ always holds; strict inequality is also necessary.

## Method
Method of the missing mass (MMM), applied twice: once for the exact modulation symmetry, once for the almost dilation symmetry. Key ingredients: (i) a refined Stein–Tomas inequality built on Tao's sharp bilinear restriction theorem for paraboloids (replacing $X^p$-space arguments); (ii) a generalized Brézis–Lieb lemma decoupling main piece from a remainder that converges a.e. while a non-convergent piece is handled separately; (iii) a local-smoothing-type a.e. convergence result.

## Result
Concentration analysis shows the maximum "energy" achievable by a sequence concentrating at a pair of antipodal points equals $\frac{\Gamma((q+1)/2)}{2^{q/2}\sqrt{\pi}\,\Gamma((q+2)/2)} S_{N-1}$, strictly greater than $S_{N-1}$ (single-point concentration). Assuming Foschi's conjecture (Gaussians maximize Strichartz for $d \geq 3$), the strict inequality (1.2) holds, giving existence of a maximizer for $R_{d+1}$ in all $N \geq 4$. Recovers Christ–Shao ($N=2,3$) without needing $q$ to be an even integer.

## Why it matters here
General background; no direct arena tie. Relevant tangentially to functional inequalities / uncertainty principles (problems P14, P17) as an example of how strict-energy-inequality criteria force precompactness in non-local concentration-compactness — a methodological cousin to Cohn–Elkies-style sharp constant problems.

## Open questions / connections
- Foschi's Conjecture 1.2: do Gaussians maximize Strichartz $S_d$ for all $d \geq 3$? Open; resolution would close the Stein–Tomas existence question.
- Extension to general compact manifolds with positive Gauss curvature, where "antipodal points" generalize to pairs with opposite normal vectors.
- Connection to Brézis–Nirenberg / Yamabe problems: this is the first instance of *non-local* multi-point concentration (vs single-point) requiring strict energy gap.

## Key terms
Stein–Tomas inequality, Strichartz inequality, Fourier restriction, adjoint restriction, maximizing sequence, precompactness, concentration-compactness, missing mass method, Brézis–Lieb lemma, bilinear restriction, antipodal concentration, Foschi conjecture, Gaussian maximizer, paraboloid, sphere
