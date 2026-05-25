---
type: source
kind: paper
title: Quasicrystals and Poisson’s summation formula
authors: Nir Lev, A. Olevskiǐ
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1312.6884
source_local: ../raw/2013-lev-quasicrystals-poisson-summation-formula.pdf
topic: general-knowledge
cites:
---

# Quasicrystals and Poisson's summation formula

**Authors:** Nir Lev, A. Olevskiǐ  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1312.6884

## One-line
Characterizes complex measures on $\mathbb{R}$ (and positive measures on $\mathbb{R}^n$) whose support and spectrum are both uniformly discrete, proving they must come from the classical Poisson summation formula.

## Key claim
If $\mu = \sum_{\lambda \in \Lambda} \mu(\lambda)\delta_\lambda$ is a temperate measure on $\mathbb{R}^n$ with uniformly discrete support $\Lambda$ and uniformly discrete spectrum $S$, then (in $n=1$, or for positive $\mu$ in $n>1$) $\Lambda$ is contained in a finite union of translates of a lattice $L$, and $\mu = \sum_{j=1}^N P_j \sum_{\lambda \in L+\theta_j} \delta_\lambda$ for trigonometric polynomials $P_j$ and shifts $\theta_j$.

## Method
Harmonic-analytic: for each $h \in \Lambda - \Lambda$, form the auxiliary measure $\mu_h = \sum_{\lambda \in \Lambda_h} \overline{\mu(\lambda)}\mu(\lambda+h)\delta_\lambda$ and show its spectrum is gap-bounded near the origin. Combine Beurling–Landau sampling/interpolation density theorems, an Ingham-type spectral-gap result for u.d. sets, and Meyer's model-set / cut-and-project characterization (via a Lagarias-style argument) to force $\Lambda$ to be a Meyer set with no transverse component, hence essentially a lattice. Theorem 3 then inverts a Vandermonde system on $\mathbb{Z}^n$-periodic Fourier pieces to recover the trigonometric-polynomial form.

## Result
Resolves Lagarias's conjecture (Problem 4.1(a) in his 2000 survey) affirmatively in dimension 1 for arbitrary complex measures, and in all dimensions for positive measures. Establishes that "Fourier quasicrystals" with two-sided uniform discreteness reduce exactly to crystallographic (lattice-derived) structures — no genuinely aperiodic example exists in this strict class. Leaves open the non-positive multi-dimensional case and the relaxation to merely discrete (non-u.d.) support/spectrum.

## Why it matters here
General background; no direct arena tie. Relevant tangentially to autocorrelation / uncertainty-style problems where one might hope a non-lattice u.d. support could realize an extremal Fourier configuration — this paper rules that out under the strict u.d. spectrum hypothesis, narrowing the search space for any "magic-function on a quasicrystal" construction.

## Open questions / connections
- Does Theorem 2 hold for signed (non-positive) measures in $n>1$? Guinand's $\{\pm\sqrt{n+1/9}\}$ example suggests possible counterexamples once uniform discreteness is dropped.
- Can the uniform-discreteness hypothesis on $\Lambda$ or $S$ be weakened to merely closed-discrete (Lagarias Problem 4.1(b))?
- Extension to locally compact abelian groups (authors conjecture yes, details not worked out).
- Spectral properties of measures supported on low-block-complexity sequences (Fibonacci-type) — a different aperiodicity regime.

## Key terms
Fourier quasicrystal, Poisson summation formula, uniformly discrete set, crystalline measure, Meyer set, model set, cut-and-project, Delone set, spectral gap, Beurling–Landau density, Bernstein space sampling, Lagarias conjecture, trigonometric polynomial, dual lattice, Ingham theorem
