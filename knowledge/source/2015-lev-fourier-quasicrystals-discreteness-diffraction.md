---
type: source
kind: paper
title: Fourier quasicrystals and discreteness of the diffraction spectrum
authors: Nir Lev, A. Olevskiǐ
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1512.08735
source_local: ../raw/2015-lev-fourier-quasicrystals-discreteness-diffraction.pdf
topic: general-knowledge
cites:
---

# Fourier quasicrystals and discreteness of the diffraction spectrum

**Authors:** Nir Lev, A. Olevskiǐ  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1512.08735

## One-line
Proves that a positive-definite measure on $\mathbb{R}^n$ with uniformly discrete support and discrete-closed spectrum is forced to be a finite sum of translated/modulated Dirac combs — a rigidity theorem for Fourier quasicrystals.

## Key claim
**Theorem 2.1:** If $\mu$ is positive-definite on $\mathbb{R}^n$, supported on a uniformly discrete set $\Lambda$, and its spectrum $S$ is a discrete closed set, then $S$ is automatically *uniformly* discrete and $\mu = \sum_{j=1}^N \sum_{\lambda \in L+\tau_j} P_j(\lambda)\delta_\lambda$ for some lattice $L$ and trigonometric polynomials $P_j$. A dichotomy (Thm 5.1): either $S$ is uniformly discrete, or its accumulation points are relatively dense — there is no middle ground.

## Method
Auxiliary "correlation" measures $\nu_h = \sum_{s \in S_h} \overline{\hat\mu(s)}\hat\mu(s+h)\,\delta_s$ for $h \in S-S$; their Fourier transforms are translation-bounded and supported in $\overline{\Lambda - \Lambda}$ (Lemma 4.1). Combined with Ingham–Kahane interpolation in Bernstein spaces $B(\Omega)$ (Theorem 3.3) and a Schwartz bump $\varphi$ with $\int\varphi=0$, $\mathrm{spec}(\varphi)\subset B_1$, $\varphi>0$ outside a ball (Lemma 5.2), one forces a contradiction unless $S_h$ meets every ball of radius $C/d(\Lambda)$. For the $n=1$ finite-density case (Thm 2.2) uses Beurling–Malliavin density and a super-additivity argument on $D^\#(S_h)$.

## Result
Three rigidity theorems (2.1, 2.2, 2.3) reducing weak discreteness assumptions to the periodic crystal form (1.3); a sharp dichotomy theorem (5.1, 7.1) with explicit constant $C/d(\Lambda)$ controlling accumulation; an existence theorem (2.4, via Beurling–Malliavin) constructing a positive-definite quasicrystal on a Meyer set whose spectrum is *nowhere dense countable*. Applied to Hof's diffraction (Thm 2.5/9.1): any Delone set of finite local complexity with uniformly discrete diffraction spectrum has periodic diffraction.

## Why it matters here
General background; no direct arena tie. Closest relevance is to autocorrelation/diffraction problems and to LP-style duality between a discrete set and its spectrum — the Cohn–Elkies "magic function" idiom uses the same support/spectrum interplay on $\mathbb{R}^n$. The Bernstein-space interpolation lemma (Cor 3.4) is a reusable tool: "a measure on a uniformly discrete set whose FT vanishes on a ball of radius $C/d(\Lambda)$ must be zero."

## Open questions / connections
- §11.2 Q1: drop positive-definiteness in $n>1$ — is $\Lambda$ still in finitely many lattice translates (Favorov shows: not a single lattice, but possibly several incommensurate ones)?
- §11.2 Q2: even in $\mathbb{R}^1$, without positive-definiteness, does discrete-closed $S$ force uniformly discrete $S$?
- §11.3: Freiman's theorem ($|A+A| \le K|A| \Rightarrow$ generalized AP) as an alternative route to the arithmetic-structure step; connects to additive combinatorics tools relevant to Sidon-set / extremal problems.

## Key terms
Fourier quasicrystal, Meyer set, model set, cut-and-project, uniformly discrete support, discrete spectrum, positive-definite measure, Poisson summation, Dirac comb, Bernstein space interpolation, Beurling–Malliavin density, Ingham–Kahane, Hof diffraction, autocorrelation measure, finite local complexity, Delone set, Lagarias problem 4.1, translation-bounded measure
