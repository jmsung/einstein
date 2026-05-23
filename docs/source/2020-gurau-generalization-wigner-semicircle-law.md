---
type: source
kind: paper
title: On the generalization of the Wigner semicircle law to real symmetric tensors
authors: R. Gurau
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2004.02660
source_local: ../raw/2020-gurau-generalization-wigner-semicircle-law.pdf
topic: general-knowledge
cites:
---

# On the generalization of the Wigner semicircle law to real symmetric tensors

**Authors:** R. Gurau  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2004.02660

## One-line
Defines a resolvent for real symmetric order-$p$ tensors via a Gaussian $p$-spin partition function, proves its large-$N$ spectral density obeys a universal Wigner-like law on a finite cut, and locates the BBP-style detection threshold for a spiked tensor.

## Key claim
For a Gaussian random symmetric tensor $T \in \otimes^p \mathbb{R}^N$ of order $p \geq 3$, the expected resolvent has a finite cut on $[-p^p/(p-1)^{p-1},\, p^p/(p-1)^{p-1}]$ in the large-$N$ limit, with a universal "spectral density" (a Meijer $G$-function generalization of the Wigner semicircle). For a spiked tensor $A = b\, N^{(p-2)/2} v^{\otimes p} + T$, the detection threshold is $b_t^2 = (p-1)^p / (p-2)^{p-2}$, above which the largest non-removable singularity of the resolvent jumps from $p^p/(p-1)^{p-1}$ to $p^p/2$.

## Method
Defines a balanced resolvent $\omega(w;T)$ as the normalized two-point function of a zero-dimensional $p$-spin model $S(\phi) = \phi^2/2 - w^{-1} T\phi^p/p$, generalizing $N^{-1} \mathrm{Tr}(w-T)^{-1}$ from matrices. Borel-Leroy summability of the perturbative expansion in trace invariants (combinatorial maps) is used to organize the series; at large $N$, melonic graph dominance collapses the two infinite cuts (along $\mathbb{R}_\pm$) into a single finite cut. Discontinuities are computed by saddle-point / instanton analysis, with real instantons in bijection with real Z-eigenpairs (Cartwright–Sturmfels normalization $x^2 = 1$).

## Result
The generating function $\omega(w) = \sum_n I_n(T) / (N w^{n+1})$ over balanced trace invariants $I_n$ (sums over connected rooted $p$-valent maps) admits a contour-integral representation for an invariant class. In the large-$N$ Gaussian average, the support and spectral density are explicit (Meijer $G$); universality follows from prior tensor-universality results [Gurau 2014]. For the spike model the threshold $b_t^2 = (p-1)^p/(p-2)^{p-2}$ is derived analytically and compared favorably to Proposition 2 of Arous–Mei–Montanari–Nica [2019].

## Why it matters here
General background; no direct arena tie. Closest hooks are landscape/saddle structure of random tensors (relevant whenever a problem reduces to extremizing a multilinear form on a sphere, e.g. spherical $p$-spin–style energies) and the BBP-style signal-to-noise threshold, which is the canonical phase transition any spike-detection or low-rank-recovery sub-routine inherits.

## Open questions / connections
- Can the largest non-removable singularity of the averaged resolvent for $p \geq 3$ be linked to the largest real Z-eigenvalue of $T$ at finite $N$ (analogue of $p=2$)? Author flags as future work.
- Signal *reconstruction* (recovering $v$ from the spiked tensor once detected) is left open — resolvent formalism gives detection only.
- Connects melonic dominance (Bonzom–Gurau–Rivasseau, Evnin 2020) ↔ spiked tensor PCA (Arous et al. 2019, Lesieur et al. 2017) ↔ landscape complexity (Ros 2020); a unified eigenvalue-statistics framework for tensors.

## Key terms
Wigner semicircle law, real symmetric tensor, tensor resolvent, Z-eigenvalue, Cartwright–Sturmfels, spiked tensor model, signal-to-noise threshold, BBP transition, $p$-spin model, melonic graphs, Meijer G-function, Borel summability, trace invariants, Gaussian orthogonal ensemble, instanton saddle point
