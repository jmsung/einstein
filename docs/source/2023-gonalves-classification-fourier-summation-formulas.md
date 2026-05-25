---
type: source
kind: paper
title: A classification of Fourier summation formulas and crystalline measures
authors: Felipe Gonçalves
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2312.11185v3
source_local: ../raw/2023-gonalves-classification-fourier-summation-formulas.pdf
topic: general-knowledge
cites: 
---

# A classification of Fourier summation formulas and crystalline measures

**Authors:** Felipe Gonçalves  ·  **Year:** 2023  ·  **Source:** http://arxiv.org/abs/2312.11185v3

## One-line
Classifies all Fourier summation formulas (and crystalline measures with quadratic decay) on $\mathbb{R}$ via a bijection with Hermite-Biehler entire functions whose ratio $A/B$ is almost periodic on the upper half-plane.

## Key claim
Every real-antipodal Fourier summation pair $(\mu, a)$ with $\deg(\mu) \le 2$ and $a$ of exponential growth corresponds to a holomorphic $f: \mathbb{C}_+ \to \mathbb{C}$ such that $f(\cdot + ic) \in AP(\mathbb{C}_+)$, $\exp(f)$ is of bounded type, and $f$ admits a Poisson-type representation $\frac{f(z)+f(w)}{z-w} = \frac{1}{2\pi i}\int \frac{d\mu(t)}{(z-t)(w-t)}$; conversely any such $f$ generates an FS-pair (Theorems 1-2). For locally-finite-support $\mu$, the pair is built from four Hermite-Biehler functions $E_j = A_j - iB_j$ with $\mu = \sum p_j / \phi'_j(\gamma) \cdot \delta_\gamma$ over zeros of $B_j$ (Theorems 3-4).

## Method
Combines almost-periodic-function theory (Besicovitch / Bohr spectrum $E_f(\lambda)$), de Branges space techniques, Hermite-Biehler factorization $|E^*(z)| < |E(z)|$ on $\mathbb{C}_+$, and Poisson representation of functions with nonnegative real part. Krein's theorem on bounded-type functions of exponential type and Phragmén-Lindelöf principles control growth; a new construction via eta-quotients $\eta(r,z) = \prod_{d|N} \eta(dz)^{r_d}$ (weight-$1/2$ modular forms on $\Gamma_0(N)$) produces self-dual crystalline measures interpolating between Poisson summation and Guinand's example.

## Result
A one-parameter family $\mu_c$ ($c \in [0, 1/8]$) of self-dual crystalline measures supported on $\{\pm\sqrt{n+c}\}_{n \ge 0}$, with $\mu_0$ = Poisson summation and $\mu_1$ = Guinand's example; for irrational $c$, support intersects any arithmetic progression at most twice. Theorem 5 classifies nonnegative crystalline measures with uniformly discrete support bounded away from $0$ (dropping the $\mathbb{N}$-valuedness assumption of Olevskii-Ulanovskii). Generalizes Kurasov-Sarnak (trig-polynomial-root construction) and Lev-Olevskii (Poisson-only for uniformly discrete support+spectrum).

## Why it matters here
General background; no direct arena tie. Touches functional-inequality / Fourier-interpolation territory (Radchenko-Viazovska, Cohn-Elkies framework) that underlies sphere-packing magic functions, but the connection to specific Einstein Arena problems is indirect.

## Open questions / connections
- Whether the conjectural Kulikov-Nazarov-Sodin pairs at the critical exponent $\alpha + \beta = 1$ with $ab = 1$ are realizable as crystalline measures.
- Extension to dense-spectrum quasicrystals (real-world quasicrystal diffraction) vs the locally-finite case classified here.
- Connection to Bondarenko-Radchenko-Seip Fourier interpolation with zeros of $\zeta$ and $L$-functions — Guinand/Riemann-Weil explicit formula appears as the prototypical almost-crystalline-measure (ACM) pair.

## Key terms
crystalline measures, Fourier quasicrystals, Hermite-Biehler functions, de Branges spaces, almost periodic functions, Poisson summation, eta-quotients, Guinand summation, Kurasov-Sarnak, Lev-Olevskii, Riemann-Weil explicit formula, Lee-Yang polynomials
