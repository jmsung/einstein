---
type: source
kind: paper
title: A note on tempered measures
authors: M. Baake, Nicolae Strungaru
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2202.09175
source_local: ../raw/2022-baake-note-tempered-measures.pdf
topic: general-knowledge
cites:
---

# A note on tempered measures

**Authors:** M. Baake, Nicolae Strungaru  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2202.09175

## One-line
Clarifies the precise relationship between tempered distributions and Radon measures, showing that "tempered" and "slowly increasing" coincide for positive measures but diverge for signed/complex ones.

## Key claim
For positive Radon measures on $\mathbb{R}^d$, the five properties — slowly increasing, strongly tempered, $|\psi|\in L^1(\mu)$ for all $\psi\in\mathcal{S}$, $\psi\in L^1(\mu)$ for all $\psi\geq 0$, and tempered — are all equivalent (Thm 2.6). For signed/complex measures, a tempered measure need NOT be slowly increasing; equivalence is recovered if the support is uniformly discrete (Thm 4.4), but fails for merely locally finite support (Example 4.7).

## Method
Constructive functional analysis. Builds a Schwartz bump $\psi$ adapted to dyadic annuli $A_j=\{2^{j-1}\leq |x|_2\leq 2^j\}$ (Lemma 2.4) to force $\mu(A_j)\leq c\cdot 2^{aj}$ from $L^1$-integrability of all Schwartz functions. For counterexamples, uses sequences $g_n\in C_c(\mathbb{R})$ with $\|g_n\|_1$ large but $\|\hat g_n\|_\infty\leq 2^{-n}$ (via dilations of $f\ast f_n$, $f=1_{[-1,1]}$, $f_n=\frac{n}{2}1_{[-1/n,1/n]}$), then assembles $\mu=\sum_n\delta_{nv}\ast\nu_n$ whose Fourier transform converges uniformly while $\mu$ itself grows faster than any polynomial.

## Result
Three structural theorems (2.6, 2.7, 4.4) plus Corollary 4.5 establishing the equivalence diagram. Explicit counterexample (Prop 3.6) realising Argabright–Gil de Lamadrid's claim concretely: a signed Radon measure on $\mathbb{R}$ that is tempered but not slowly increasing. Example 4.7 (via Kahane–Salem) produces a tempered pure-point measure $\mu=\sum_m\delta_{8m}\ast\omega_m$ with locally finite support that fails to be slowly increasing — sharpening the uniformly-discrete hypothesis in Thm 4.4. Lemma 2.9: slowly increasing $\Leftrightarrow$ linear combination of positive tempered measures.

## Why it matters here
General background; no direct arena tie. The 23 Einstein problems are finite-dimensional optimization (sphere packing, kissing, autocorrelation, Sidon, etc.); this paper sits in the harmonic-analysis / aperiodic-order foundations literature. Potentially relevant only as scaffolding for Cohn–Elkies-style LP-bound arguments where one manipulates tempered measures / distributions on $\mathbb{R}^d$, but the questions here (signed-measure pathology) do not touch the LP-bound machinery, which uses positive measures throughout.

## Open questions / connections
- Extends [Argabright–Gil de Lamadrid 1974] by making the signed-measure pathology constructive and explicit.
- Connects to [Spindeler–Strungaru arXiv:2105.03382] on translation-bounded measures as Fourier transforms — relevant to spectral theory of quasicrystals / Meyer sets.
- Open: characterise the exact gap between "locally finite support + tempered" and "slowly increasing" — Example 4.7 shows the gap is non-empty but does not classify it.

## Key terms
tempered measure, tempered distribution, Radon measure, slowly increasing, strongly tempered, Schwartz space, Fourier transform of measures, aperiodic order, Meyer set, uniformly discrete support, Hahn–Jordan decomposition, Argabright–Gil de Lamadrid
