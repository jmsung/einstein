---
type: source
kind: paper
title: Every real-rooted exponential polynomial is the restriction of a Lee-Yang polynomial
authors: Lior Alon, A. Cohen, C. Vinzant
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2303.03201
source_local: ../raw/2023-alon-every-real-rooted-exponential-polynomial.pdf
topic: general-knowledge
cites:
---

# Every real-rooted exponential polynomial is the restriction of a Lee-Yang polynomial

**Authors:** Lior Alon, A. Cohen, C. Vinzant  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2303.03201

## One-line
Proves that every real-rooted univariate exponential polynomial $f(x)=\sum_j c_j e^{\lambda_j x}$ arises as the restriction of a multivariate Lee-Yang polynomial to a positive line in the torus, completing the Kurasov-Sarnak characterization of $\mathbb{N}$-valued Fourier quasicrystals.

## Key claim
**Theorem 1.1:** If $f(x)=\sum_{j=0}^{s} c_j e^{\lambda_j x}$ is real-rooted (with $\mathrm{Im}(\lambda_0)$ minimal), let $n=\dim_{\mathbb{Q}}\{\mathrm{Im}(\lambda_j-\lambda_0)\}_{j\geq1}$. Then there exists a Lee-Yang polynomial $p\in\mathbb{C}[z_1,\dots,z_n]$ and $\ell\in\mathbb{R}_+^n$ with $\mathbb{Q}$-linearly independent entries such that $f(x)=e^{\lambda_0 x}\,p(\exp(ix\ell))$. The dimension $n$ is optimal.

## Method
Three-step reduction via amoeba geometry. (1) **Lemma 2.1** (Pólya 1920): real-rootedness forces $\mathrm{conv}(\{\lambda_j\})$ to be a line segment with real normal, so all $\lambda_j-\lambda_0$ are purely imaginary. (2) **Lemma 2.2**: Carathéodory's theorem on the rational polyhedral cone $L_{\mathbb{R}}\cap\mathbb{R}_{\geq0}^s$ picks $n$ integer extreme rays giving a polynomial lift. (3) **Lemma 2.6 + Corollary 3.3**: Levin's almost-periodic-function lower bound (uniform $|f(x+iy)|\geq m(h,\delta)>0$ off zeros) plus equidistribution on the torus shows the line $\mathbb{R}\ell$ is disjoint from the amoeba $\mathcal{A}(p)$; Proposition 2.5 then fills in full-dimensional cones in $\mathcal{A}(p)^c$ around $\pm\ell$, which a monomial change-of-variables converts into Lee-Yang structure ($\mathbb{R}_+^n\cup\mathbb{R}_-^n\subset\mathcal{A}(q)^c$).

## Result
**Corollary 1.4:** A measure $\mu$ on $\mathbb{R}$ is an $\mathbb{N}$-valued Fourier quasicrystal iff $\mu=\mu_{p,\ell}$ for some Lee-Yang polynomial $p$ and positive frequencies $\ell\in\mathbb{R}_+^n$. This closes the loop: Kurasov-Sarnak [5] showed Lee-Yang $\Rightarrow$ FQ; Olevskii-Ulanovskii [10] reduced FQs to real-rooted exponential polynomials; this paper shows every such polynomial lifts. Worked example: $\sin(\pi x)+\varepsilon\sin(x)$ for $|\varepsilon|\leq 1/2$ lifts to the Lee-Yang $p(z_1,z_2)=\tfrac{1}{2i}(z_1 z_2-1+\varepsilon z_2-\varepsilon z_1)$ on $\ell=(\pi-1,\pi+1)$.

## Why it matters here
General background; no direct arena tie. Closest tangential relevance is the **stable-polynomial / Lee-Yang machinery** as a real-rootedness certification tool — potentially relevant to autocorrelation-inequality problems where roots-on-a-line structure constrains extremal configurations, but the FQ application is distant from the 23-problem set.

## Open questions / connections
- Future work (announced): connect *properties* of $\mathbb{N}$-valued FQs to invariants of the associated Lee-Yang polynomial (Newton polytope, amoeba topology, multiplicity structure).
- The construction is non-unique even though $n$ is optimal — what is the natural moduli space of lifts?
- Extends Pólya 1920 + Levin's almost-periodic-zero theory + Gelfand-Kapranov-Zelevinsky amoeba theory into the Fourier-quasicrystal setting; suggests amoeba complement / Newton polytope tools may certify other "all-real-zeros" phenomena.

## Key terms
Lee-Yang polynomial, Schur stable polynomial, real-rooted exponential polynomial, Fourier quasicrystal, crystalline measure, amoeba, Newton polytope, Kurasov-Sarnak construction, Olevskii-Ulanovskii, almost periodic function, Pólya zero strips, Gelfand-Kapranov-Zelevinsky
