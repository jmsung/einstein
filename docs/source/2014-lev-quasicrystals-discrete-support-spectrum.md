---
type: source
kind: paper
title: Quasicrystals with discrete support and spectrum
authors: Nir Lev, A. Olevskiǐ
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1501.00085
source_local: ../raw/2014-lev-quasicrystals-discrete-support-spectrum.pdf
topic: general-knowledge
cites:
---

# Quasicrystals with discrete support and spectrum

**Authors:** Nir Lev, A. Olevskiǐ  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1501.00085

## One-line
Constructs a non-trivial real signed measure on $\mathbb{R}$ whose support and Fourier spectrum are both discrete closed sets but strongly non-periodic, showing that the uniform-discreteness hypothesis in Lev–Olevskii's earlier periodicity theorem cannot be relaxed.

## Key claim
There exists a non-zero real signed measure $\mu = \sum_{\lambda \in \Lambda} \mu(\lambda)\delta_\lambda$ on $\mathbb{R}$ such that (i) both $\Lambda$ and the spectrum $S$ are discrete closed sets, and (ii) $\Lambda$ contains only finitely many elements of any arithmetic progression — in particular $\mu$ is not a finite combination of Poisson-type measures. Both $\mu$ and $\hat\mu$ are translation-bounded.

## Method
A generalized cut-and-project construction on a lattice $\Gamma \subset \mathbb{R}^2$: instead of using a Schwartz $\varphi$ with bounded support, $\varphi$ is built by induction so that $\varphi$ vanishes on a discrete set $Z$ (controlling $\hat\mu$'s support via $\Gamma^*$) and $\hat\varphi$ vanishes on $Q$ (controlling $\mu$'s support via $\Gamma$). The inductive step uses the Matei–Meyer theorem (model sets are interpolation sets for $PW_\Omega$ when $\mathrm{mes}(\Omega) > |I|/\det\Gamma$) plus a Schwartz-class interpolation lemma to subtract off boundary values at each scale.

## Result
The constructed $\mu$ satisfies the Poisson-style summation identity $\sum_\Lambda \mu(\lambda) f(\lambda) = \sum_S \hat\mu(s)\hat f(s)$ for Schwartz $f$, with both $\Lambda$ and $S$ uncoverable by any finite union of arithmetic progressions (Prop. 6.2). One can further decompose $\mu = \mu_1 + \mu_2$ with $\mu_1$ supported on a model set and $\|\mu_2\|$ arbitrarily small. The $n$-fold product gives the analogous result in $\mathbb{R}^n$. Positivity of $\mu$ is left open.

## Why it matters here
General background; no direct arena tie — but informs the autocorrelation / uncertainty-principle problem family by sharpening intuition about how Fourier pairs of discrete measures can fail to be periodic, complementing the Cohn–Elkies / Viazovska magic-function picture where bounded-support pairs are central.

## Open questions / connections
- Can the same construction be done with a positive measure $\mu$? (Lagarias Problem 4.1(b), positive case.)
- Kolountzakis [arXiv:1502.06283] gives an alternative construction via infinite sums of Poisson measures — what's the structural relationship?
- Extends Meyer's cut-and-project model sets [Mey70, Mey95] and Matei–Meyer universal sampling [MM08, MM10] beyond bounded interpolation windows.

## Key terms
Fourier quasicrystal, cut-and-project, model set, Poisson summation formula, Paley-Wiener space, interpolation set, Matei-Meyer theorem, translation-bounded measure, pure point spectrum, dual lattice, Schwartz function, Lagarias problem, Meyer
