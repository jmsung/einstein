---
type: source
kind: paper
title: Logarithmic bounds for Roth's theorem via almost-periodicity
authors: T. Bloom, Olof Sisask
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1810.12791
source_local: ../raw/2018-bloom-logarithmic-bounds-roth-theorem.pdf
topic: general-knowledge
cites:
---

# Logarithmic bounds for Roth's theorem via almost-periodicity

**Authors:** T. Bloom, Olof Sisask  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1810.12791

## One-line
A streamlined proof that 3-AP-free subsets of $\{1,\dots,N\}$ have size $\ll N/(\log N)^{1-o(1)}$, using almost-periodicity of convolutions almost entirely in physical space.

## Key claim
$r_3(N) \ll N/(\log N)^{1-o(1)}$; more precisely, for $A \subseteq G$ (finite abelian, odd order) of density $\alpha$, $T(A) \geq \exp(-C\alpha^{-1}(\log(2/\alpha))^C)|A|^2$, so $\alpha \gtrsim (\log\log|G|)^C/\log|G|$ forces a non-trivial 3-AP.

## Method
Density-increment à la Roth/Bourgain, but the structured "piece" is found via $L^p$-almost-periodicity of $1_A * 1_A$ relative to a Bohr set (after Croot–Sisask), bypassing most Fourier analysis. Two cases drive the increment: if $\|\mu_A * 1_A\|_{L^{2m}(B')}$ is large, almost-periodicity directly yields a density jump on a sub-Bohr set $T$; if it is small, $L^{4m}$-almost-periodicity plus a 3-AP deficit gives the increment. Bourgain's two-scales lemma + regular Bohr sets close the iteration.

## Result
Recovers Sanders's logarithmic barrier $c = 1 - o(1)$ in $r_3(N) \ll N/(\log N)^c$ with $C = 7$ on the $\log\log N$ exponent (vs. Bloom's earlier $C=4$). The proof is markedly simpler than [Sanders 2011] and [Bloom 2016]; physical-space arguments replace spectrum-structure machinery.

## Why it matters here
General background; no direct arena tie. Provides exposure to $L^p$-almost-periodicity, Bohr-set regularity, and density-increment iteration — tools potentially relevant to autocorrelation / additive-combinatorics problems and to extremal-graph problems where 3-AP-free density bounds inform constructions.

## Open questions / connections
- Super-logarithmic bounds for $r_3(N)$ over $\mathbb{Z}$: the paper hints at ongoing work bridging this approach with Bateman–Katz higher-additive-energy techniques used over $\mathbb{F}_3^n$.
- Can the $\log\log$ exponent be pushed below 4 by avoiding the regularity-lemma loss in restricting $L^p$ norms to Bohr sets?
- Extends Croot–Sisask almost-periodicity [6]; connects to Schoen–Sisask (4-variable Roth) and Croot–Łaba–Sisask (APs in sumsets).

## Key terms
Roth's theorem, three-term arithmetic progressions, almost-periodicity, Croot-Sisask, Bohr sets, density increment, $L^p$ norms of convolutions, Chang-Sanders lemma, regular Bohr set, Bourgain two-scales, Fourier analysis additive combinatorics, Bateman-Katz
