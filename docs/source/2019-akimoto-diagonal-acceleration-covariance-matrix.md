---
type: source
kind: paper
title: Diagonal Acceleration for Covariance Matrix Adaptation Evolution Strategies
authors: Youhei Akimoto, N. Hansen
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1905.05885
source_local: ../raw/2019-akimoto-diagonal-acceleration-covariance-matrix.pdf
topic: general-knowledge
cites:
---

# Diagonal Acceleration for Covariance Matrix Adaptation Evolution Strategies

**Authors:** Youhei Akimoto, N. Hansen  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1905.05885

## One-line
Augments CMA-ES with an adaptively-damped diagonal scaling matrix $D$ (covariance factored as $\sigma^2 DCD$) that captures the advantages of separable CMA-ES without losing performance on non-separable problems.

## Key claim
dd-CMA-ES matches the better of plain and separable CMA on all tested function classes, and on non-separable functions with coordinate-wise mis-scaling (e.g. Ellipsoid-Cigar) achieves **overadditive speedup** — outperforming both variants; up to $\sim$10× fewer $f$-calls on 160-dim separable Ellipsoid, scaling tested to $n=5120$. Also relaxes default learning-rate scaling from $\Theta(1/n^2)$ to $\Theta(1/n^{1.75})$ (plain) and $\Theta(1/n)$ to $\Theta(1/n^{0.75})$ (separable).

## Method
Decomposes the sampling covariance as $\sigma^2 DCD$ with $D$ diagonal and $C$ a positive-definite correlation-like matrix; $C$ uses standard CMA updates while $D$ uses faster separable-CMA-style updates. A **dynamic damping factor** $1/\beta$ modulates the $D$ learning rate as a function of $\mathrm{cond}(C)$: when $C$ is near identity, $D$ adapts as fast as separable CMA; once $C$ has learned variable dependencies, $D$ updates are suppressed to avoid disturbing $C$. Two new schemes (eigenvalue-bounded rescaling factor $\alpha^{(t)}$, and rescaling unpromising samples $\tilde{y}_{i:\lambda} = \sqrt{n}\,y_{i:\lambda}/\|z_{i:\lambda}\|$) guarantee positive-definiteness under active updates with negative weights.

## Result
On rotated Cigar/Ellipsoid/Discus dd-CMA matches plain CMA; on separable counterparts it matches separable CMA up to large $n$. On Ell-Cig (non-separable with coordinate mis-scaling) dd-CMA improves scaling over both baselines — the diagonal first absorbs coordinate scaling, then $C$ learns the Cigar long axis. Population-size scaling tested up to $\lambda/\lambda_{\text{def}} = 1024$ (40-dim) with dd-CMA always tracking the better baseline. The decomposition $\Sigma = DCD$ is unique; the paper's target regime is when both $D$ and $C$ have non-negligible condition number ($\gtrsim 100$).

## Why it matters here
Direct compute-router input for any Einstein Arena problem with **coordinate-wise ill-conditioning plus correlated variables** — e.g. point-configuration problems where some coordinates (radii, angles) are intrinsically scaled differently from others, or sphere-packing parameterizations mixing position + radius. Adds to the wiki's CMA-ES technique page: dd-CMA-ES is the preferred default over both plain and separable CMA when variable sensitivities are unknown a priori (the common black-box case for Arena problems where parameterization choice is partly heuristic).

## Open questions / connections
- $\beta_{\text{thresh}}$ tuning for separable Ellipsoid at $n>320$ — performance deviates from separable-CMA scaling; possibly needs $n$-dependent threshold.
- Default $\lambda$ may need to increase for dd-CMA on multimodal separable functions (TwoAxes shows high run-variance at default $\lambda=13$).
- Extends Krause–Glasmachers (xCMA) and Arnold–Hansen (1+1)-active-CMA to the $(\mu_w,\lambda)$ case with two distinct positive-definiteness mechanisms.
- Connection to parameterization-selection wisdom: dd-CMA partly *removes* the cost of bad parameterization, but only when mis-scaling is coordinate-aligned.

## Key terms
CMA-ES, covariance matrix adaptation, evolution strategy, diagonal decoding, separable CMA, active covariance update, positive-definiteness, rank-one update, rank-mu update, cumulative step-size adaptation, evolution path, condition number, black-box optimization, Akimoto, Hansen
