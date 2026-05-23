---
type: source
kind: paper
title: A simple proof of Stolarsky’s invariance principle
authors: J. Brauchart, J. Dick
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1101.4448
source_local: ../raw/2011-brauchart-simple-proof-stolarsky-invariance.pdf
topic: general-knowledge
cites:
---

# A simple proof of Stolarsky's invariance principle

**Authors:** J. Brauchart, J. Dick  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1101.4448

## One-line
Gives a short reproducing-kernel-Hilbert-space (RKHS) proof of Stolarsky's invariance principle, which equates (up to a constant) the sum of pairwise Euclidean distances of $N$ points on $S^d$ with their spherical-cap $L_2$-discrepancy.

## Key claim
For any $N$-point set $\{x_0,\dots,x_{N-1}\} \subset S^d$,
$$\frac{1}{N^2}\sum_{k,\ell} \|x_k-x_\ell\| + \frac{1}{C_d}\int_{-1}^{1}\!\!\int_{S^d}\!\Big(\sigma_d(C(z;t)) - \tfrac{1}{N}\sum_k \mathbf{1}_{C(z;t)}(x_k)\Big)^2 d\sigma_d(z)\,dt = \iint_{S^d\times S^d}\|x-y\|\,d\sigma_d(x)d\sigma_d(y),$$
with $C_d = \omega_{d-1}/(\omega_d)\cdot\Gamma((d+1)/2)/(\sqrt{\pi}\Gamma(d/2)) \sim 1/\sqrt{2\pi d}$. A weighted generalization (Theorem 1) holds for any positive weight $v(t)$ on $[-1,1]$.

## Method
Construct an RKHS $H_C$ on $S^d$ via the reproducing kernel $K_C(x,y) = \int_{-1}^1\!\int_{S^d} \mathbf{1}_{C(z;t)}(x)\mathbf{1}_{C(z;t)}(y)\,d\sigma_d(z)\,dt$, derived from the indicator functions of spherical caps. Direct computation yields the closed form $K_C(x,y) = 1 - C_d\|x-y\|$. The squared worst-case quadrature error then expands in two ways — via the kernel's closed form (giving the distance sum) and via its integral definition (giving the $L_2$-cap discrepancy) — and equating them is the invariance principle.

## Result
Stolarsky's 1973 identity is recovered (Prop. 1) in a few lines without Haar integrals over $SO(d+1)$. The eigenfunctions of $K_C$ are ultraspherical (Gegenbauer) harmonics. A weighted version (Thm. 1) replaces $\|x-y\|$ with $K_{C,v}(x,y) = \int_{S^d} V(\min\{\langle x,z\rangle,\langle y,z\rangle\})\,d\sigma_d(z) - V(-1)$ for antiderivative $V$ of $v$, yielding a family of invariance principles linking weighted energies to weighted cap discrepancies.

## Why it matters here
Direct background for sphere-based discrepancy/energy problems: the identity converts a cap-discrepancy bound into a sum-of-distances bound and vice versa, which is the mechanism Stolarsky + Schmidt used to get the $N^{-1-1/d}$ rate for $(-1)$-energy deviation. Relevant to any Einstein Arena problem involving spherical-cap discrepancy, sum-of-distances maximization on $S^d$, or RKHS worst-case integration error on spheres.

## Open questions / connections
- Extends Stolarsky 1973, 1975 (general metric spaces) and connects to Beck 1984 (Fourier lower bound $N^{-1-1/d}$) and Schmidt 1969 (cap-discrepancy upper bound).
- Weighted generalization (Thm. 1) opens a family of invariance principles — which weight $v$ gives the tightest cap-discrepancy bound for a given energy functional?
- Karhunen–Loève expansion in ultraspherical harmonics (deferred to Brauchart–Womersley) gives explicit eigenvalues — useful for designing point sets minimizing the worst-case error.

## Key terms
Stolarsky invariance principle, spherical cap discrepancy, sum of distances, reproducing kernel Hilbert space, RKHS, worst-case integration error, ultraspherical harmonics, Gegenbauer, Riesz energy, equilibrium measure, Björck, Schmidt, sphere $S^d$, quadrature on sphere, $L_2$-discrepancy
