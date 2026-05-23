---
type: source
kind: paper
title: Structure in additively nonsmoothing sets
authors: M. Bateman, N. Katz
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1104.2862
source_local: ../raw/2011-bateman-structure-additively-nonsmoothing-sets.pdf
topic: general-knowledge
cites:
---

# Structure in additively nonsmoothing sets

**Authors:** M. Bateman, N. Katz  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1104.2862

## One-line
Reproves a structural theorem showing that sets which saturate Hölder's inequality between $E_4$ and $E_8$ (additively "nonsmoothing" sets) must decompose into translates of sets with small doubling.

## Key claim
If $\Delta \subseteq Z$ is symmetric of size $M$ with $E_4(\Delta') \sim M^{2+\tau_0}$ for all large $\Delta' \subseteq \Delta$ and $E_8(\Delta) \lesssim M^{4+3\tau_0+\sigma_0}$ (σ₀-nonsmoothing), then $\Delta$ admits a partition into pieces $B_j$ each covered by $X_j + H_j$ where $|H_j - H_j| \lesssim |H_j|^{1+f(\sigma_0)}$ — i.e., $H_j$ has near-trivial doubling, with $f(\sigma_0) \to 0$ as $\sigma_0 \to 0$.

## Method
Iterative graph refinement on the difference set $\Delta - \Delta$. Two quantities — **comity** (how often $\Delta[x] \cap \Delta[y]$ is large for differences $x,y$) and the new **sideways comity** (how often $\Delta[x] \cap F_{x,b}$ is large) — control progress. When either is large, pigeonhole/Cauchy-Schwarz upgrades to a denser graph at lower "height" $\alpha$; when both are small, the asymmetric Balog–Szemerédi–Gowers theorem extracts the structured $H, X$. Hölder via Fourier ($E_{2m}(A) = |Z|^{2m-1}\sum |\hat{1_A}(\xi)|^{2m}$) underlies the nonsmoothing inequality.

## Result
Theorem 1.3: Disjoint decomposition $\Delta = \sqcup_j B_j$ with $|H_j| \gtrsim M^{\tau+\alpha+f(\sigma)}$, $|X_j| \lesssim M^{1-\tau-2\alpha+f(\sigma)}$, $|H_j - H_j| \lesssim |H_j|^{1+f(\sigma)}$, $|(X_j + H_j) \cap B_j| \gtrsim M^{1-\alpha-f(\sigma)}$. By Freiman, each $H_j$ sits efficiently in a coset progression (or subspace in $\mathbb{F}_3^N$). The new proof is cleaner than [BK] via sideways comity but gives worse quantitative dependence on $\sigma$.

## Why it matters here
General background; no direct arena tie. The technique (energy ratios, structured-vs-pseudorandom decomposition via BSG) is part of additive-combinatorics toolkit relevant to extremal-set problems and cap-set–style obstructions, but no current Einstein Arena problem invokes $E_4/E_8$ smoothing directly.

## Open questions / connections
- Improving the dependence $f_{\tau_0}(\sigma)$ — the BSG-routed proof here is worse than [BK]'s direct argument; what's the true rate?
- The parent application is cap sets in $\mathbb{F}_3^N$ ([BK] arXiv:1101.5851) — now superseded by Croot–Lev–Pach / Ellenberg–Gijswijt polynomial method (2016).
- Does sideways comity generalize to higher-order energies $E_{2m}$, $m \geq 4$?

## Key terms
additive energy, $E_4$, $E_8$, additive smoothing, Hölder's inequality, Balog–Szemerédi–Gowers, asymmetric BSG, comity, sideways comity, Freiman's theorem, cap sets, $\mathbb{F}_3^N$, small doubling, coset progression, Bateman, Katz
