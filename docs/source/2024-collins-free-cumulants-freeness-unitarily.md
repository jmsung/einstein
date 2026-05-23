---
type: source
kind: paper
title: Free cumulants and freeness for unitarily invariant random tensors
authors: Benoît Collins, R. Gurau, L. Lionni
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2410.00908
source_local: ../raw/2024-collins-free-cumulants-freeness-unitarily.pdf
topic: general-knowledge
cites:
---

# Free cumulants and freeness for unitarily invariant random tensors

**Authors:** Benoît Collins, R. Gurau, L. Lionni  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2410.00908

## One-line
Extends free probability — free cumulants, moment-cumulant inversion, and free independence — from unitarily invariant random matrices to local-unitary (LU) invariant random tensors with $D$ inputs/outputs, in both pure ($A = T \otimes \bar T$) and mixed (Wishart-like) regimes.

## Key claim
For LU-invariant random tensors scaling like the pure complex Gaussian or like a Wishart tensor at large $N$, one can define **tensorial free cumulants** via moment-cumulant formulas summing over $D$-tuples of non-crossing permutations $\tau \preceq \sigma$, such that (i) the cumulants of independent tensors are additive, (ii) vanishing of mixed first-order free cumulants defines **asymptotic tensor freeness**, and (iii) random tensors converge in distribution to elements of newly-constructed **tensorial probability spaces** generalizing non-commutative probability spaces.

## Method
Trace-invariants are encoded by $D$-tuples of permutations $\sigma \in S_n^D$ (with $\Pi(\sigma) = \Pi(\sigma_1) \vee \cdots \vee \Pi(\sigma_D)$); finite-$N$ moments are expectations of these invariants. Weingarten calculus on $U(N)^{\otimes D}$ is used to invert the classical cumulant generating function (related to the tensor HCIZ integral) on trace-invariants, defining finite-$N$ free cumulants. The large-$N$ limit isolates **melonic** invariants as the first-order surviving class (pure case) and a Wishart-melonic class (mixed), with the same non-crossing combinatorics governing both moment-cumulant inversions.

## Result
- Tensorial moment-cumulant formula: $\kappa_\sigma^m(\vec m) = \sum_{\tau \preceq \sigma} \varphi_{\Pi(\tau),\tau}^m(\vec m)\, M(\sigma\tau^{-1})$ (and its inverse), with $M$ the Möbius function on non-crossing partitions.
- Three equivalent characterizations of asymptotic tensor freeness: (1) vanishing of mixed first-order tensorial free cumulants; (2) vanishing on connected $\sigma$ with $\omega(\sigma, \mathrm{id}) = 0$ when colors mix; (3) factorization-after-centering of moments on almost-alternating melonic graphs of paired tensors (Thm. 7.5 mixed, Thm. 7.6 pure).
- Construction of tensorial probability spaces $(\mathcal A, \varphi)$ in which random LU-invariant tensors have well-defined limits, with tensor freeness lifting to subspaces they generate.
- Additivity: for independent LU-invariant tensors, first-order free cumulants are additive — the tensorial analogue of free convolution for sums of independent unitarily invariant matrices.

## Why it matters here
General background; no direct arena tie. The melonic non-crossing combinatorics and Möbius-inversion machinery here could inform any future arena problem touching tensor invariants, multipartite quantum-state distributions, or large-$N$ tensor model spectra — none of the current 23 problems are tensorial, but the moment-cumulant inversion pattern parallels techniques used in autocorrelation/uncertainty problems (Möbius inversion on lattices).

## Open questions / connections
- Higher-order tensor free cumulants (beyond first order) — only a "preliminary discussion" given; full theory analogous to second-order freeness [Mingo–Speicher, ref 59; Collins–Mingo–Śniady–Speicher, ref 3] is open.
- Real-symmetric-tensor analogue: Kunisky–Moore–Wein [29] and Bonnin–Bordenave [30] develop a parallel theory; reconciling complex LU-invariant and real-symmetric free cumulants is open.
- Applications to quantum information: tensor freeness as a tool for entanglement measures on LU-equivalence classes of multipartite states, extending Collins–Nechita / Aubrun lines of work.
- Spectrum of sums of independent LU-invariant tensors (tensorial Horn problem) — additivity established; explicit distributions not yet computed.

## Key terms
free cumulants, free probability, unitarily invariant random tensors, local-unitary invariance, Weingarten calculus, melonic invariants, non-crossing partitions, Möbius inversion, Wishart tensor, tensor HCIZ integral, asymptotic freeness, multipartite entanglement, Collins, Gurau, Speicher, Voiculescu, large-N expansion, tensorial probability space, paired tensors
