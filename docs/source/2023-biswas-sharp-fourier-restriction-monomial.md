---
type: source
kind: paper
title: Sharp Fourier restriction to monomial curves
authors: Chandan Biswas, Betsy Stovall
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2302.05317
source_local: ../raw/2023-biswas-sharp-fourier-restriction-monomial.pdf
topic: general-knowledge
cites:
---

# Sharp Fourier restriction to monomial curves

**Authors:** Chandan Biswas, Betsy Stovall  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2302.05317

## One-line
Establishes sharp lower bounds for $L^p \to L^q$ Fourier extension operator norms on monomial curves in $\mathbb{R}^d$ with affine arclength measure, and gives a precompactness-modulo-symmetries dichotomy for extremizing sequences.

## Key claim
For a monomial curve $\gamma(t) = (t^{l_1}/l_1!, \ldots, t^{l_d}/l_d!)$ with $|l_\gamma| > \binom{d+2}{2}$ and $q = \tfrac{d^2+d}{2}p' > p$, the extension operator norm satisfies $B_{\gamma,p} \ge B_{\gamma,p}^{\mathrm{conc}} := B_{\gamma_0,p} \cdot c(l_\gamma,p,q)$, where $c$ is $\Psi_{p,q}^{1/q}$ (all $l_i$ odd), $2^{1/p'}$ (all $l_i$ even), or $1$ (otherwise). Extremizing sequences are precompact modulo the symmetry group iff this lower bound is strict.

## Method
Rescales an extremizer for extension off the moment curve $\gamma_0$ via approximate dilation symmetries $D_\delta^l$ at $t_0 = 1$ to concentrate at one point (generic), or symmetrically at antipodal points $\{\pm 1\}$ (parity cases). A new "two-antipodal-point" profile decomposition framework (Prop. 8.2) handles concentration in higher codimension, and a sharp Hölder/Minkowski argument (Lemma 3.2 using $\psi_{p,q}(t) = \tfrac{1}{2\pi}\int |1+e^{i\theta}t|^q d\theta \cdot (1+t^p)^{-q/p}$) captures the antipodal interaction term.

## Result
The lower bound $B_{\gamma,p} \ge B_{\gamma,p}^{\mathrm{conc}}$ holds for all monomial curves; explicit extremizing families $f_\delta$ are constructed (eq. 1.7) using truncated rescalings of moment-curve extremizers. Theorem 1.3 establishes the dichotomy: every normalized extremizing sequence has a subsequence that either converges to a true extremizer (mod symmetries) or matches $f_{\delta_n}$ with $\delta_n \searrow 0$; the latter is impossible exactly when $B_{\gamma,p} > B_{\gamma,p}^{\mathrm{conc}}$. By duality (Cor 1.4), the same dichotomy holds for the restriction operator $R_\gamma : L^r \to L^s(\lambda_\gamma)$.

## Why it matters here
General background; no direct arena tie. The profile-decomposition / concentration-compactness machinery for anisotropic-decay manifolds is methodologically adjacent to extremizer arguments that appear in Fourier-analytic approaches to packing (Cohn–Elkies) and autocorrelation problems, but the specific results target monomial-curve restriction estimates not currently in scope for the 23 arena problems.

## Open questions / connections
- Sequel announced: extending the sharp dichotomy to arbitrary polynomial curves, where the symmetry group is even more deficient (modulations only) and more than two "antipodal" concentration points may arise.
- Existence (not just bounds) of extremizers when $B_{\gamma,p} > B_{\gamma,p}^{\mathrm{conc}}$ — current results are conditional precompactness.
- Extends Biswas–Stovall (2023, moment curve, [6]) and parallels Frank–Lieb–Sabin sphere results [18] and Flock–Stovall [14] to higher-codimension monomials.

## Key terms
Fourier restriction, Fourier extension, monomial curve, affine arclength measure, moment curve, profile decomposition, concentration compactness, extremizer, Stein–Tomas inequality, antipodal concentration, torsion matrix, Brezis–Lieb lemma
