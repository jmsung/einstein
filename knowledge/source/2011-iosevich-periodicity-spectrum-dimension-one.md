---
type: source
kind: paper
title: Periodicity of the spectrum in dimension one
authors: A. Iosevich, Mihail N. Kolountzakis
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1108.5689
source_local: ../raw/2011-iosevich-periodicity-spectrum-dimension-one.pdf
topic: general-knowledge
cites:
---

# Periodicity of the spectrum in dimension one

**Authors:** A. Iosevich, Mihail N. Kolountzakis  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1108.5689

## One-line
Proves that every spectrum $\Lambda$ of a bounded measurable set $\Omega \subseteq \mathbb{R}$ of measure 1 must be periodic, with integer period.

## Key claim
**Theorem 1:** If $\Lambda \subseteq \mathbb{R}$ is a spectrum of a bounded measurable set $\Omega \subseteq \mathbb{R}$ of measure 1, then $\Lambda$ is periodic and any period is a positive integer. This generalizes Bose–Madan (2011) / Kolountzakis (2011), which required $\Omega$ to be a finite union of intervals.

## Method
Symbolic dynamics over a finite alphabet $\Sigma = Z_{\hat\chi_\Omega} \cap (0,\Delta]$ of admissible successive-gap values (finite because $\hat\chi_\Omega$ is entire with discrete zeros, and tiling forces a uniform upper gap bound $\Delta$). The spectrum is encoded as a bi-infinite sequence in $\Sigma^\mathbb{Z}$; the F. and M. Riesz theorem (analyticity of Fourier transforms of measures supported on a half-line) shows the resulting closed shift-invariant set $X \subseteq \Sigma^\mathbb{Z}$ is determined by left and right half-lines. A compactness/diagonal argument then yields a finite window-size $w$ that determines every element, and a pigeonhole over $|\Sigma|^w$ window-contents forces periodicity with period $\le |\Sigma|^w$.

## Result
Any spectrum $\Lambda$ takes the form $\Lambda = T\mathbb{Z} + \{\ell_1,\dots,\ell_T\}$ with $T \in \mathbb{Z}_{>0}$ (Corollary 2). Consequently, if $\Omega$ is spectral, then $\Omega$ tiles $\mathbb{R}$ at integer level $T$ when translated by $T^{-1}\mathbb{Z}$. Period bound: $\le |\Sigma|^w$, finite but not explicit. The result is sharp in dimension: it **fails** in $d \ge 2$ — even the unit cube admits non-periodic spectra (Lagarias–Reeds–Wang, Iosevich–Pedersen).

## Why it matters here
General background; no direct arena tie — none of the 23 Einstein Arena problems are spectral-set / Fuglede-conjecture problems. Tangentially relevant as a worked example of how the F. and M. Riesz theorem + symbolic-dynamics compactness can convert "structure of zero set of an entire Fourier transform" into a periodicity theorem, a pattern that could inform autocorrelation / uncertainty-style problems where $\hat\chi$ zeros control admissible point configurations.

## Open questions / connections
- Fuglede's conjecture (spectral $\iff$ translational tile) remains open in $d=1,2$; false for $d \ge 3$ (Tao 2004, Matolcsi, Kolountzakis–Matolcsi, Farkas–Révész).
- Is the conjecture true if $\Omega$ is restricted to convex domains? The tiling $\Rightarrow$ spectrality direction is known for convex sets.
- Periodic Tiling Conjecture (Grünbaum–Shephard, Lagarias–Wang): every translational tile admits a periodic tiling — open in $d \ge 2$, true for $d=1$ and for convex polytopes in any $d$ (Venkov, McMullen).
- The period upper bound $|\Sigma|^w$ is ineffective; an explicit bound in terms of $\Omega$ would sharpen decidability arguments.

## Key terms
Fuglede conjecture, spectral set, translational tiling, periodicity, F. and M. Riesz theorem, symbolic dynamics, shift-invariant subshift, half-line determination, entire function zeros, packing condition, uncertainty principle, Iosevich, Kolountzakis, Bose-Madan
