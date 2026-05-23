---
type: source
kind: paper
title: Fourier Pairs of Discrete Support with Little Structure
authors: Mihail N. Kolountzakis
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1502.06283
source_local: ../raw/2015-kolountzakis-fourier-pairs-discrete-support.pdf
topic: general-knowledge
cites:
---

# Fourier Pairs of Discrete Support with Little Structure

**Authors:** Mihail N. Kolountzakis  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1502.06283

## One-line
An elementary construction of a Fourier pair of discrete measures on $\mathbb{R}$ whose supports cannot be covered by finitely many arithmetic progressions, so the pair cannot arise from finitely many applications of the Poisson Summation Formula (PSF).

## Key claim
There exists a translation-bounded measure $\nu = \sum_{\lambda \in \Lambda} c_\lambda \delta_\lambda$ with $\Lambda \subset \mathbb{R}$ discrete, whose Fourier transform $\hat\nu = \sum_{s \in S} d_s \delta_s$ also has discrete support $S$, and such that **neither $\Lambda$ nor $S$ is contained in a finite union of arithmetic progressions** — disproving that all such "crystalline" Fourier pairs come from PSF.

## Method
Finite/cyclic-group dimension counting: on $\mathbb{Z}_N$, the linear system "f vanishes on a window $I$ and $\hat f$ vanishes on $I$" has $\sim 4N/5$ unknowns vs $\sim 2N/5$ equations, so a nonzero solution exists. Lift to a periodic measure on $\mathbb{Z}$ via $\tau_n = f(n \bmod N)$, dilate by $1/\sqrt{N}$ to open a hole $(-M,M)$ around the origin in both $\mu$ and $\hat\mu$ (with $N = 100M^2$). Overlay infinitely many such pairs with increasing $M_n \to \infty$, modulated/translated by a $\mathbb{Q}$-linearly independent sequence $\epsilon_n \to 0$, weighted by $D_n = V_n n^2$ for convergence.

## Result
The construction yields a Fourier pair $(\nu, \hat\nu)$ of discrete-support, translation-bounded measures whose supports have **infinite $\mathbb{Q}$-dimension** (from the $\mathbb{Q}$-independent modulation/translation parameters), while any finite union of arithmetic progressions spans only a finite-dimensional $\mathbb{Q}$-subspace — so the supports cannot be contained in such a union. Simpler than Lev–Olevskii [3] but does not achieve their stronger "no infinite AP-intersection" property.

## Why it matters here
General background on Fourier-analytic uncertainty / crystalline measures; informs autocorrelation-inequality and uncertainty-principle problems where one analyzes pairs $(\mu, \hat\mu)$ with constrained supports (the Cohn–Elkies / sphere-packing magic-function machinery sits in the same family). Provides a concrete *anti*-rigidity example: discrete-support Fourier pairs are not all "PSF-like," so structural assumptions in arena LP/SDP bounds must be checked.

## Open questions / connections
- Can the elementary $\mathbb{Z}_N$ dimension-counting trick be sharpened to also force $S$ to meet every AP only finitely often (matching [3])?
- Relation to Meyer's Pisot/Salem quasicrystal constructions [4] and Lev–Olevskii's uniformly-discrete rigidity theorem [1,2] — what is the exact dividing line (uniform discreteness vs mere discreteness)?
- Does an analog hold in $\mathbb{R}^d$, and what are the implications for Cohn–Elkies-style LP bounds with discrete-support test functions?

## Key terms
Poisson summation formula, quasicrystal, crystalline measure, Fourier pair, discrete support, tempered distribution, uniformly discrete set, arithmetic progression, Q-linear independence, Lev-Olevskii, Meyer Pisot Salem, Cohn-Elkies, autocorrelation, uncertainty principle, translation bounded measure
