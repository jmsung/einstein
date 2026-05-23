---
type: source
kind: paper
title: Fourier uniqueness pairs of powers of integers
authors: João P. G. Ramos, Mateus Sousa
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1910.04276
source_local: ../raw/2019-ramos-fourier-uniqueness-pairs-powers.pdf
topic: general-knowledge
cites:
---

# Fourier uniqueness pairs of powers of integers

**Authors:** João P. G. Ramos, Mateus Sousa  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1910.04276

## One-line
Proves that, for many exponent pairs $(\alpha,\beta)$ with $\alpha+\beta<1$, a Schwartz function vanishing on $\{\pm n^\alpha\}$ together with its Fourier transform vanishing on $\{\pm n^\beta\}$ must be identically zero.

## Key claim
Let $0<\alpha,\beta<1$. (A) If $f\in\mathcal{S}(\mathbb{R})$ and $f(\pm\log(n+1))=\hat f(\pm n^\alpha)=0$ for all $n\in\mathbb{N}$, then $f\equiv 0$. (B) If $(\alpha,\beta)\in A:=\{\alpha+\beta<1,\ \alpha<1-\sqrt{\beta(1-\alpha-\beta)}\ \text{or}\ \beta<1-\sqrt{\alpha(1-\alpha-\beta)}\}$ and $f(\pm n^\alpha)=\hat f(\pm n^\beta)=0\,\forall n$, then $f\equiv 0$. Diagonal corollary: $\alpha<1-\tfrac{\sqrt2}{2}$ suffices.

## Method
Density-of-zeros → decay bootstrap. Between consecutive zeros of $f^{(k)}$, mean-value theorem gives gaps $|a_{n+1}^{(k)}-a_n^{(k)}|\lesssim (k+1)|a_n^{(k)}|^{-(1-\alpha)/\alpha}$, which via Fourier inversion yields $|f(x)|\le C_k|x|^{k(\alpha-1)/\alpha}$. Iterating between $f$ and $\hat f$ (each forces decay on the other) drives both into a Gelfand–Shilov space $S^\nu_\mu$ with $\nu=\alpha/(1-\alpha-\beta)$, $\mu=\beta/(1-\alpha-\beta)$. Then Lemma 3 lifts $\hat f$ to an entire function of order $1/(1-L_1(\alpha,\beta))$, and the converse of Hadamard's factorization theorem forces $\sum n^{-(1+\varepsilon)\beta/(1-L_1)}<\infty$, contradicting the prescribed zero set $\{n^\beta\}$.

## Result
The admissible region $A$ strictly contains a neighborhood of $(\alpha,\beta)$ with $\alpha+\beta$ small; the diagonal threshold is $\alpha<1-\sqrt 2/2 \approx 0.293$. The proof is constructive enough to give explicit Gelfand–Shilov membership $f\in\tilde S^\nu_\mu$ and is robust under perturbations of the zero set: $|a_{k+n}-a_n|\le C_k|a_{k+n}|^{-\eta}$, $|b_{k+n}-b_n|\le C_k|b_{k+n}|^{-\omega}$ with $\eta\omega>1$ suffices. Extends to radial Schwartz functions on $\mathbb{R}^d$ via the Hankel transform.

## Why it matters here
Adjacent to the Radchenko–Viazovska $\sqrt{\mathbb{Z}}$ interpolation formula (the $\alpha=\beta=1/2$ critical case driving the Cohn–Kumar–Miller–Radchenko–Viazovska sphere-packing proofs in $d=8,24$); this paper shows that *below* the critical density, mere uniqueness — without an interpolation formula — still holds across a large region. For arena problems involving Cohn–Elkies-style magic functions, Fourier uncertainty inequalities, or autocorrelation extremal problems, this gives a flexibility lemma: zero-set rigidity is not necessary for uniqueness, only density.

## Open questions / connections
- Conjecture (Ramos–Sousa): the full region $\alpha+\beta<1$ is a Fourier uniqueness pair; current methods fall short of this.
- Critical case $\alpha+\beta=1$ (including $\alpha=\beta=1/2$): under which scalings $f(\pm a n^\alpha)=\hat f(\pm b n^\beta)=0$ force $f\equiv 0$? Likely needs Radchenko–Viazovska modular-form machinery hybridized with this complex-analytic approach.
- Connection to Meyer's crystalline measures supported on $\{\pm\sqrt{n+a}\}$ ($a\in\{9,24,72\}$) and Lev–Olevskii's quasicrystal/Poisson-summation results.
- Sharpness of the gap estimate (34) is established; improvements would have to be on-average, not pointwise.

## Key terms
Fourier uniqueness pair, Radchenko–Viazovska interpolation, Schwartz class, Hadamard factorization theorem, Gelfand–Shilov space, crystalline measure, Poisson summation, Heisenberg uniqueness pair, Cohn–Elkies linear programming bound, sphere packing $E_8$ Leech, Hankel transform, Beurling–Kahane sampling density, modular forms, Meyer quasicrystal
