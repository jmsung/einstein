---
type: source
kind: paper
title: The Landscape of the Spiked Tensor Model
authors: G. B. Arous, Song Mei, A. Montanari, M. Nica
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1711.05424
source_local: ../raw/2017-arous-landscape-spiked-tensor-model.pdf
topic: general-knowledge
cites:
---

# The Landscape of the Spiked Tensor Model

**Authors:** G. B. Arous, Song Mei, A. Montanari, M. Nica  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1711.05424

## One-line
Computes the expected number of critical points and local maxima of the maximum-likelihood objective for the rank-one spiked tensor model on the sphere, showing exponentially many "uninformative" local maxima cluster in a narrow band orthogonal to the planted signal.

## Key claim
For $Y = \lambda u^{\otimes k} + W/\sqrt{2n}$ with $k \geq 3$, the expected number of local maxima of $f(\sigma) = \langle Y, \sigma^{\otimes k}\rangle$ on $S^{n-1}$ is $\exp\{n S_0(m,x) + o(n)\}$ with explicit complexity rate $S_0(m,x)$ (Theorems 1, 2). Local maxima are confined either very near $u$ or to a band of width $\Theta(\lambda^{-1/(k-2)})$ around the equator $\{\sigma : \langle u,\sigma\rangle = 0\}$; for general critical points the band is $\Theta(\lambda^{-1/(k-1)})$.

## Method
Kac-Rice formula expresses the expected critical-point count as an integral involving $\mathbb{E}|\det \mathrm{Hess}\,f(\sigma)|$. The Hessian distribution is a rank-one deformation $aW_n + bI_n + ce_1e_1^T$ of a GOE matrix, so the eigenvalue large-deviation theory of Maïda (2007) for rank-one perturbations of Gaussian ensembles replaces Selberg's integral (the tool used in [Auffinger–Ben Arous–Černý 2013] for the $\lambda=0$ p-spin case). Spherical-integral asymptotics (Guionnet–Maïda) handle the rank-one term.

## Result
Explicit closed-form complexity functions $S(m,x)$ (Eq. 6) for all critical points and $S_0(m,x) = S(m,x) - L(\theta(m),t(x))$ (Eq. 11) for local maxima, with $\theta = \sqrt{2k(k-1)}\lambda m^{k-2}(1-m^2)$ and $t = \sqrt{2k/(k-1)}\,x$. Phase-transition threshold $\lambda_c = \sqrt{(k-1)^{k-1}/(2k(k-2)^{k-2})}$ above which a "good" critical point near $m \approx 1$ emerges. Heuristic implication: gradient-ascent from a random initialization $\langle u,\sigma_0\rangle = \Theta(n^{-1/2})$ escapes the equatorial band of uninformative maxima only when $\lambda \geq C n^{(k-2)/2}$ — matching the known power-iteration threshold of Montanari–Richard 2014.

## Why it matters here
General background; no direct arena tie. Closest relevance is methodological: Kac-Rice + GOE large-deviations as a template for counting critical points of random homogeneous polynomials on $S^{n-1}$, which is the same geometric setting as several arena problems (sphere-packing potentials, autocorrelation cost functions). The "exponentially many uninformative local maxima in a narrow band" picture explains why basin-hopping / power-iteration on such landscapes needs informed initialization, paralleling P11/P15/P16 multistart failure modes.

## Open questions / connections
- Expected vs typical count diverge for $\lambda > 0$ (unlike the $\lambda=0$ p-spin case, per Subag 2015); typical-count computation is open and forthcoming via [BBRC18].
- Rigorously connecting the equatorial-band escape threshold $\lambda \geq C n^{(k-2)/2}$ to the algorithmic power-iteration threshold of [MR14].
- Gap between $\lambda_{\text{Bayes}} = O(1)$, ML threshold $\lambda_{\text{ML}}(k)$ (one-step RSB, conjectured from [Tal06, GS00]), and polynomial-time threshold $\lambda \gtrsim n^{(k-2)/4}$ from tensor-unfolding / SoS [HSS15, HSSS16].

## Key terms
spiked tensor model, tensor PCA, Kac-Rice formula, complexity function, GOE large deviations, rank-one deformation, p-spin spherical glass, Maïda spherical integral, signal-to-noise threshold, non-convex landscape, local maxima counting, power iteration threshold, Auffinger, Ben Arous, Montanari
