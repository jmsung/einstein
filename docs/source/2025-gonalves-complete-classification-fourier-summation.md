---
type: source
kind: paper
title: A Complete Classification of Fourier Summation Formulas on the real line
authors: Felipe Gonçalves, Guilherme Vedana
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2504.02741v1
source_local: ../raw/2025-gonalves-complete-classification-fourier-summation.pdf
topic: general-knowledge
cites: 
---

# A Complete Classification of Fourier Summation Formulas on the real line

**Authors:** Felipe Gonçalves, Guilherme Vedana  ·  **Year:** 2025  ·  **Source:** http://arxiv.org/abs/2504.02741v1

## One-line
Completes the classification of all Poisson-style summation formulas $\int \hat\varphi \, d\mu = \sum a(\lambda_n)\varphi(\lambda_n)$ on $\mathbb{R}$ by putting them in bijection with almost-periodic holomorphic functions in a generalized Nevanlinna class.

## Key claim
Every Fourier summation pair $(\mu,a)$ — with $\mu$ strongly tempered of degree $\le 2(k+1)$ and $a$ of finite exponential growth — corresponds uniquely to a holomorphic $F:\mathbb{C}_+ \to \mathbb{C}$ that (I) lies in $N_{\le k} - N_{\le k}$, (II) is almost periodic on a shifted half-plane $\mathbb{C}_+ + ic_1$, and (III) has Fourier coefficients $E_F(\lambda)$ of finite exponential growth; the correspondence is a bijection (Theorem 1) and extends to merely locally summable $E_F$ (Theorem 2).

## Method
Associates to $(\mu,a)$ an auxiliary holomorphic kernel $G_k(w,z,x)$ built as iterated convolution of $e^{-2\pi|x|}$ with the Cauchy-style kernel, then tests the FS identity against $G_k$ to reconstruct $F$ via a Nevanlinna–Poisson factorization $F(z) = \frac{(z^2+1)^k}{2\pi i}\int \frac{1+tz}{t-z} \frac{d\mu(t)}{(1+t^2)^{k+1}} + iQ(z)$. Almost-periodicity is recovered from the absolutely convergent series $\tfrac12 a(0) + \sum_{\lambda>0} a(\lambda)e^{2\pi i\lambda z}$; the converse uses Bochner approximation by trigonometric polynomials plus a Phragmén–Lindelöf bound to force $E_F(\lambda)=0$ for $\lambda<0$.

## Result
The classification removes the prior restriction $\deg(\mu)\le 2$ from Gonçalves [arXiv:2312.11185], allowing arbitrary polynomial growth of $\mu$. New examples now captured include: (a) the Selberg trace formula on compact hyperbolic surfaces (yielding $\deg\mu = 3$ via the Laplacian spectrum and prime-geodesic length spectrum); (b) Meyer's crystalline measure built from $r_3(n)$ (three-squares function, also $\deg = 3$); (c) the Guinand-style modular family $\mu_c = \sum \alpha_{n,c}(\delta_{\sqrt{n+c}}+\delta_{-\sqrt{n+c}})$ for $c\in[0,1/8]$ with conjectural $\deg\mu_c = 3$.

## Why it matters here
General background for any Einstein Arena problem that uses Fourier-analytic duality on $\mathbb{R}$ — Cohn–Elkies-style linear-programming bounds, $+1$/$-1$ autocorrelation problems, sphere packing in low dimensions, and Fourier-uniqueness/interpolation constructions à la Radchenko–Viazovska. The Nevanlinna-class characterization tells the agent *which* test-pair $(\mu,a)$ are admissible when designing magic functions or LP dual certificates, and the examples (Selberg trace, Meyer crystalline) supply concrete higher-degree FS-pairs beyond Poisson.

## Open questions / connections
- Does $\deg\mu_c = 3$ hold for all $c\in[0,1/8]$? Hecke bound only gives $\le 3$; numerics suggest $|\alpha_{n,c}|\le 1$.
- For $c > 1/8$ the Guinand family fails FS but still produces summation on analytic test functions in a strip — what is the right classification there?
- Connection to Lee–Yang polynomials (Alon–Cohen–Vinzant) and Fourier quasicrystals (Kurasov–Sarnak, Lev–Olevskii): how does this Nevanlinna characterization specialize to the crystalline (locally finite support) subclass?
- Extends/completes Gonçalves [arXiv:2312.11185]; complements Radchenko–Viazovska interpolation [Publ. IHES 129, 2019].

## Key terms
Fourier summation pair, Poisson summation, Selberg trace formula, generalized Nevanlinna class, almost periodic function, crystalline measure, Fourier quasicrystal, Guinand-Meyer construction, Radchenko-Viazovska interpolation, Cohn-Elkies, modular forms, Phragmén-Lindelöf, Bochner approximation, three-squares function $r_3(n)$
