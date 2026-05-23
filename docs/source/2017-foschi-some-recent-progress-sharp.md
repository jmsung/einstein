---
type: source
kind: paper
title: Some recent progress on sharp Fourier restriction theory
authors: Damiano Foschi, D. Silva
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1701.06895
source_local: ../raw/2017-foschi-some-recent-progress-sharp.pdf
topic: general-knowledge
cites:
---

# Some recent progress on sharp Fourier restriction theory

**Authors:** Damiano Foschi, D. Silva  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1701.06895

## One-line
A survey of the last decade's results on sharp adjoint Fourier restriction / Strichartz inequalities — optimal constants and extremizers — focused on highly symmetric manifolds (paraboloid, cone, hyperboloid, sphere) where simple geometric arguments suffice.

## Key claim
On manifolds with sufficient symmetry, the sharp $L^2 \to L^q$ extension inequality reduces to a bilinear convolution estimate $\|f\mu * f\mu\|_{L^2}^2 \le \|\mu*\mu\|_{L^\infty} \|f\|_{L^2}^4$ via Cauchy-Schwarz + Hölder; extremizers exist iff $\mu*\mu$ is constant on its support, giving: Gaussians (paraboloid), exponentials (cone), constants (sphere $S^2$), and **non-existence** (hyperboloid, quartic-perturbed paraboloid).

## Method
The unifying technique is "delta calculus" for convolution measures: representing $(g\mu * h\mu)(\xi) = \int \delta(\xi-\eta-\zeta)\,g(\eta)h(\zeta)\,d\mu_\eta d\mu_\zeta$ and computing in adapted coordinates (bipolar, Lorentz-invariant). Two pointwise inequalities — $|f\mu*f\mu|^2 \le (\mu*\mu)(|f|^2\mu*|f|^2\mu)$ from Cauchy-Schwarz, plus $|g\mu*h\mu| \le |g|\mu*|h|\mu$ — reduce oscillatory problems to geometric integration. Spectral analysis via Funk-Hecke / spherical-harmonic expansion handles the sphere case; sign-pattern of eigenvalues $\Lambda_k(S^{d-1})$ determines whether constants are extremal.

## Result
Sharp $L^2 \to L^4$ extension on $S^{d-1}$ with constants as extremizers proven for $d \in \{3,4,5,6,7\}$; method fails for $d \ge 8$ because $\Lambda_2(S^{d-1}) > 0$. Convolution formula $(\sigma_{d-1}*\sigma_{d-1})(\xi) = V_{d-2}|\xi|^{-1}(1-|\xi|^2/4)_+^{(d-3)/2}$. New sharp mixed-norm inequality $\|\widehat{f\sigma}\|_{L^6_{\rm rad}L^2_{\rm ang}(\mathbb{R}^2)} \le I(0,0,0)^{1/6}\|f\|_{L^2(S^1)}$ via Bessel-function monotonicity $I(k,\ell,m) \le I(0,0,0)$. Hyperboloid: $(\lambda_2*\lambda_2)(\xi,\tau) = 2\pi(\tau^2-|\xi|^2)^{-1/2}\chi_{\tau\ge\sqrt{4+|\xi|^2}}$ is bounded but non-constant on support → no extremizers.

## Why it matters here
General background for functional / Fourier inequalities; the **delta-calculus toolkit** (Appendix A) is directly reusable for computing sharp constants in any extremal problem involving convolutions of surface measures on spheres, cones, paraboloids — relevant to Einstein Arena problems touching sphere packing, autocorrelation inequalities, and uncertainty-principle-style bounds. The "constant convolution measure ⇒ explicit extremizer" pattern is a transferable diagnostic.

## Open questions / connections
- Conjecture: Gaussians are extremizers for the paraboloid Strichartz inequality in **all** dimensions (proven only $d=1,2$; see Hundertmark-Zharnitsky [30]).
- Conjecture: constants are extremizers for sharp Tomas-Stein on $S^{d-1}$ in all dimensions; open for $d \ge 8$ where the $\Lambda_2 > 0$ obstruction blocks the spectral method.
- Step 1 conjecture for the $S^1$ sixfold integral (reducing 6-linear to trilinear on squares) — open in [14].
- Unifying picture (§4): paraboloid/sphere/hyperboloid as conic sections of $\Gamma_3$; restrictions of $\exp(-|\xi|)$ to each hyperplane recover the corresponding extremizer.

## Key terms
Fourier restriction, Strichartz estimate, Tomas-Stein inequality, adjoint extension operator, sharp constants, extremizers, Gaussian extremizer, paraboloid, cone, hyperboloid, sphere, Funk-Hecke formula, spherical harmonics, Bessel functions, delta calculus, convolution measure, bilinear estimate, Knapp example, Lorentz invariance, concentration compactness, mixed-norm spaces
