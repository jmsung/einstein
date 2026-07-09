---
type: source
kind: paper
title: Fourier Quasicrystals with Unit Masses
authors: A. Olevskiǐ, A. Ulanovskii
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2009.12810
source_local: ../raw/2020-olevski-fourier-quasicrystals-unit-masses.pdf
topic: general-knowledge
cites:
---

# Fourier Quasicrystals with Unit Masses

**Authors:** A. Olevskiǐ, A. Ulanovskii  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2009.12810

## One-line
Characterizes every Fourier quasicrystal whose atoms all have mass 1 as the zero set of an exponential polynomial with purely imaginary frequencies.

## Key claim
**Theorem 1.** If $\mu = \sum_{\lambda \in \Lambda} \delta_\lambda$ is a Fourier quasicrystal (FQ) on $\mathbb{R}$, then there exists an exponential polynomial $p(x) = \sum_{k=1}^n b_k e^{i\gamma_k x}$ with $b_k \in \mathbb{C}$, $\gamma_k \in \mathbb{R}$, having only real simple zeros, such that $\Lambda$ is exactly the zero set of $p$. The converse (every such $p$ yields an FQ) is established in [OU20].

## Method
Combine tempered-distribution Fourier analysis with classical entire-function theory. Step 1: prove a counting bound $\mu(a,b) \le C(1+b-a)$ via convolution with a Schwartz bump, giving relative uniform discreteness of $\Lambda$. Step 2: build the canonical Weierstrass-type product $\psi(z) = \lim \prod (1 - z/\lambda) e^{z/\lambda}$, identify $\psi'/\psi$ with the half-plane Cauchy sum of $\hat\mu$ (formula (5)), then apply the Phragmén–Lindelöf principle in two opposing angles plus the Paley–Wiener theorem to force the series expansion to truncate to finitely many exponential terms.

## Result
The support $\Lambda$ of any unit-mass FQ on $\mathbb{R}$ is exactly the real zero set of an entire function of exponential type that is an exponential polynomial $\sum b_k e^{i\gamma_k x}$ with $\gamma_k \in \mathbb{R}$. Remark 1 extends this to FQs with integer masses $\mu = \sum c_\lambda \delta_\lambda$, $c_\lambda \in \mathbb{N}$: $\Lambda$ is still the (now possibly non-simple) real zero set of such an exponential polynomial. This closes the structural classification opened by Kurasov–Sarnak (2020).

## Why it matters here
General background; no direct arena tie. Possible peripheral relevance to autocorrelation/uncertainty problems (P14, P17) where exponential-polynomial / Paley–Wiener structure controls distribution of zeros, but none of the 23 problems directly involve crystalline measures.

## Open questions / connections
- Higher-dimensional analogue: does the characterization extend to FQs in $\mathbb{R}^d$, $d \ge 2$?
- Quantitative control: given $\Lambda$, how do the frequencies $\gamma_k$ and degree $n$ relate to gap/density statistics of $\Lambda$?
- Connection to stable polynomials (Kurasov–Sarnak [KS20]) — which stable-polynomial families yield FQs with prescribed spectral support?

## Key terms
Fourier quasicrystal, crystalline measure, exponential polynomial, imaginary frequencies, Dirac comb, tempered distribution, Paley–Wiener theorem, Phragmén–Lindelöf principle, entire function of exponential type, Weierstrass product, uniformly discrete set, Olevskii, Ulanovskii, Kurasov–Sarnak, stable polynomial
