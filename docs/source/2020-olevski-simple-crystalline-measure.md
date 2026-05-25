---
type: source
kind: paper
title: A Simple Crystalline Measure
authors: A. Olevskiǐ, A. Ulanovskii
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2006.12037
source_local: ../raw/2020-olevski-simple-crystalline-measure.pdf
topic: general-knowledge
cites:
---

# A Simple Crystalline Measure

**Authors:** A. Olevskiǐ, A. Ulanovskii  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2006.12037

## One-line
Every pair of exponential polynomials $\psi,\varphi$ with $\Lambda_\varphi \subset \Lambda_\psi$ generates a Poisson-type summation formula, yielding simple crystalline measures whose support contains no arithmetic progression.

## Key claim
Theorem 1: for $\psi \in \mathrm{Exp}$, $\varphi \in \mathrm{Exp}_s$ with $\Lambda_\varphi \subset \Lambda_\psi$, the identity $\sum_{\lambda \in \Lambda_\varphi} c_\lambda f(\lambda) = \sum_{s \in S} a_s \hat f(s)$ holds with $c_\lambda = \psi(\lambda)/\varphi'(\lambda)$, $S \subset \mathbb{R}$ locally finite with polynomial growth $\#S \cap (-r,r) \le Cr^m$, and bounded $c_\lambda$ (and bounded $a_s$ when $\Lambda_\varphi \subset \mathbb{R}$). Corollary 2: for $\varphi \in \mathrm{Exp}_r$, $\mu = \sum_{\lambda \in \Lambda_\varphi} \delta_\lambda$ is a crystalline measure; the explicit $\varphi(z) = \sin\pi z + \delta \sin z$ ($0 < \delta \le 1/2$) gives $\Lambda_\varphi = \{k + \delta_k\}_{k\in\mathbb{Z}}$ with $\delta_k \in [-1/6,1/6]$, containing no arithmetic progression.

## Method
Contour integration of $f(z)\psi(z)/\varphi(z)$ along two horizontal lines: the residue theorem produces the left-hand side $\sum c_\lambda f(\lambda)$, while Laurent-type expansions of $1/\varphi(z)$ in the upper and lower half-planes (geometric series in $e^{2\pi i (\alpha_j-\alpha_1)z}$) yield the Fourier-side sum $\sum a_s \hat f(s)$. Boundedness of $c_\lambda$ uses an Argument-Principle compactness argument on translates $\varphi_\lambda(z) = \varphi(z+\lambda)$; boundedness of $a_s$ (real case) uses Bessel's inequality applied to test functions $\psi_{\beta,s}(z) = e^{2\pi i s z}\beta(\sin\pi\beta z/\pi\beta z)^2$. The non-AP claim for $\sin\pi z + \delta\sin z$ uses Rouché's theorem plus an irrationality/projection argument.

## Result
A clean, elementary construction of crystalline measures with uniformly discrete support containing no arithmetic progression — strictly simpler than Kurasov–Sarnak [KS20] and Meyer [M20]. The example $\Lambda = \{k + \delta_k : k \in \mathbb{Z}\}$ with $|\delta_k| \le 1/6$ (and $\delta_k \to 0$ as $\delta \to 0$) approaches $\mathbb{Z}$ but avoids any AP, and generalizes to $\sin\pi z + \sum d_j \sin\alpha_j z$ whenever some $\pi/\alpha_j$ is irrational and $\sum |d_j| \le 1/2$. Combined with Favorov [F20], this is sharp: if $\delta_k \to 0$ at infinity and $\mu = \sum\delta_\lambda$ is crystalline, then $\Lambda = \mathbb{Z}$.

## Why it matters here
General background; no direct arena tie. The crystalline-measure / Poisson-summation machinery is adjacent to Fourier-analytic LP bounds (Cohn–Elkies sphere packing, autocorrelation inequalities) — it shares the "atomic measure with atomic Fourier transform" structure but the arena problems are extremal/optimization, not existence/structure of quasicrystals.

## Open questions / connections
- Extends Lev–Olevskii [LO15–17] and Meyer [M16, M20] crystalline-measure constructions; gives the Kurasov–Sarnak [KS20] example as a special case.
- Non-simple-root / non-u.d. case: formula still holds but with derivatives of $f$ and possibly unbounded coefficients — left unworked.
- Sharpness boundary with Favorov [F20]: how large can the perturbation $\delta_k$ be (not $\to 0$) while keeping the measure crystalline?

## Key terms
crystalline measure, Poisson summation formula, exponential polynomial, quasicrystal, Dirac comb, uniformly discrete set, Fourier quasicrystal, Argument Principle, Rouché's theorem, Bessel inequality, Meyer, Lev–Olevskii, Kurasov–Sarnak, arithmetic progression
