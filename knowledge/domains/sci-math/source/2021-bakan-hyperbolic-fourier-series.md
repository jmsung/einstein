---
type: source
kind: paper
title: Hyperbolic Fourier series
authors: A. Bakan, H. Hedenmalm, A. Montes-Rodríguez, D. Radchenko, M. Viazovska
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2110.00148
source_local: ../raw/2021-bakan-hyperbolic-fourier-series.pdf
topic: general-knowledge
cites:
---

# Hyperbolic Fourier series

**Authors:** A. Bakan, H. Hedenmalm, A. Montes-Rodríguez, D. Radchenko, M. Viazovska  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2110.00148

## One-line
Constructs an explicit $L^1(\mathbb{R})$ biorthogonal system to the "hyperbolic trigonometric" sequence $\{1, e^{i\pi nx}, e^{i\pi n/x}\}_{n\in\mathbb{Z}\setminus\{0\}}$, yielding a Fourier-pair interpolation formula for solutions of the Klein–Gordon equation on the characteristic lattice $\{(\pi n,0),(0,\pi n)\}_{n\in\mathbb{Z}}$.

## Key claim
For every $f\in L^1(\mathbb{R},(1+x^2)^{-1}dx)$, the hyperbolic Fourier series $h_0(f)+\sum_{n\neq 0}\big(h_n(f)e^{i\pi nx}+m_n(f)e^{-i\pi n/x}\big)$ converges to $f$ in $\mathcal{S}'(\mathbb{R})$; the explicit biorthogonal system $\{H_0,H_n,M_n\}$ is complete in $L^1(\mathbb{R})$ and satisfies decay $|H_0(x)|\le 3/(1+x^2)$, $|H_n(x)|+|M_n(x)|\le \pi^6|n|^2/(1+x^2)$.

## Method
Builds the biorthogonal kernel via integrals against the Gauss hypergeometric function $F_\triangle(z)=F(1/2,1/2;1;z)$ on the line $\mathrm{Re}\,s=1/2$, with "Schwarz triangle polynomials" $S_n^\triangle$ (degree $n$, leading $16^n$) extracted from the meromorphic part of $\exp(n\pi F_\triangle(1-z)/F_\triangle(z))$ — the Chibrikova-type kernel also used in Radchenko–Viazovska's real-line Fourier pair interpolation. Analytic continuation of the generating function is controlled by two partitions of the upper half-plane (Schwarz partition and an even-rational/even-integer-continued-fraction partition tied to the elliptic modular function $\lambda$). The framework links to the Perron–Frobenius–Ruelle operator $T_1$ of the even Gauss map $G_2(x)=\{-1/x\}_2$, with $H_n^\pm$ solving $(I\pm T_1)H_n^\pm = e^{i\pi nx}$.

## Result
Theorem 1.1 gives closed-form integral representations for $H_0,H_n$ on $\mathrm{Re}=1/2$ with $M_n(x)=H_n(-1/x)/x^2$; biorthogonality $\int e^{-i\pi nx}H_p=\delta_{n,p}$, $\int e^{i\pi m/x}H_p=0$ (and dual for $M_q$) is established. Interpolation formula (1.10) reconstructs any Klein–Gordon solution $U_\varphi(x,y)=\int\varphi(t)e^{ixt+iy/t}dt$ from its samples $\{U_\varphi(\pi n,0),U_\varphi(0,\pi n)\}_{n\in\mathbb{Z}}$ under the decay condition $\sum n^2(|U_\varphi(\pi n,0)|+|U_\varphi(0,\pi n)|)<\infty$, via interpolating functions $R_n(\pi m,0)=\delta_{n,m}$, $R_n(0,\pi m)=0$. Extends Hedenmalm–Montes-Rodríguez (2011) uniqueness Theorem A to an explicit reconstruction.

## Why it matters here
Direct relevance to Einstein Arena autocorrelation / uncertainty / Fourier-interpolation problems (P14 / Cohn–Elkies family / +1/−1 uncertainty principle on $\mathbb{R}$): this is the Radchenko–Viazovska magic-function machinery in its hyperbolic ($e^{ixt+iy/t}$) incarnation, with explicit decay estimates ($|H_n|\lesssim n^2/(1+x^2)$) that constrain what density of constraints can pin down a Schwartz function. The Schwarz-triangle-polynomial generating-function technique (modular forms + hypergeometric kernels) is the same toolkit that produced the $E_8$ / Leech sphere-packing magic functions — a concrete worked example of "modular forms → explicit Fourier interpolation kernel."

## Open questions / connections
- How densely can the $\{(\pi n,0),(0,\pi n)\}$ lattice be thinned while preserving uniqueness for $U_\varphi$ — i.e., what is the analogue of Beurling–Malliavin density for the hyperbolic system?
- The decay $\pi^6|n|^2/(1+x^2)$ is loose; tighter bounds (or $L^p$ estimates) would extend convergence to weaker function classes — connects to optimal weights in Cohn–Elkies-style LP bounds.
- The promised follow-up (general smooth Klein–Gordon solutions on bounded rectangles representable as $U_\varphi$) and series expansion of $U_\varphi$ via the hyperbolic Fourier series of $\varphi$ are deferred — both directly relevant to discretized Goursat / sampling-theorem questions.
- Connection to the Perron–Frobenius–Ruelle operator of the even Gauss map suggests a dynamical/transfer-operator route to interpolation kernels — a potentially new framework relative to existing wiki Cohn–Elkies / Viazovska entries.

## Key terms
hyperbolic Fourier series, Klein-Gordon equation, Fourier pair interpolation, Radchenko-Viazovska, Hedenmalm-Montes-Rodriguez, biorthogonal system, Gauss hypergeometric function, Schwarz triangle function, elliptic modular function, Perron-Frobenius-Ruelle operator, even Gauss map, Chibrikova kernel, modular forms, discretized Goursat problem, magic function, tempered distributions
