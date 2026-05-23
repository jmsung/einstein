---
type: source
kind: paper
title: The edge of random tensor eigenvalues with deviation
authors: Nicolas Delporte, Naoki Sasakura
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2405.07731
source_local: ../raw/2024-delporte-edge-random-tensor-eigenvalues.pdf
topic: general-knowledge
cites:
---

# The edge of random tensor eigenvalues with deviation

**Authors:** Nicolas Delporte, Naoki Sasakura  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2405.07731

## One-line
Computes signed and genuine Z-eigenvalue distributions of order-3 symmetric Gaussian random tensors perturbed by a Gaussian vector noise, locating two critical noise variances at which the spectral edge bifurcates.

## Key claim
For symmetric Gaussian random tensors of order 3 and size $N$ with Gaussian noise of rescaled variance $\bar\beta = \beta N^2$, two critical thresholds appear: at $\bar\beta_1 = 3\alpha/64$ a second-largest eigenvalue emerges as an outlier from the bulk (matching the semicircle edge $y_c=\sqrt 2$), and at $\bar\beta_2 = (3 + 2\sqrt 3)\alpha/96$ this outlier merges with the trivial largest eigenvalue and both become complex.

## Method
Field-theoretic at large $N$: rewrites the eigenvector counting density via a quartic fermionic action (signed distribution, exact at finite $N$) and a combined boson–fermion action with Hubbard–Stratonovich decomposition (genuine $|\det M|$). Factorizes parallel/transverse sectors under $O(1)\times O(N-1)$, solves Schwinger–Dyson saddle equations with a graded boson–fermion symmetry, and extracts the edge via Lefschetz-thimble steepest descent on the Hermite-polynomial integral representation involving $U(1-N/2, 3/2, 3\alpha k^2/(2|v|^2))$.

## Result
The signed and genuine spectral edges obey the **same** large-$N$ equation $h(y)=0$ with $y=3\alpha/(2N|v|^2)$. Near $\bar\beta_1$ the edge displacement scales as $|y-y_c| \propto (\bar\beta - \bar\beta_1)^2$ on the $y>y_c$ side (with coefficient changing from $128\sqrt 2/9$ to $512\sqrt 2/9$) and as $(\bar\beta - \bar\beta_1)$ on $y<y_c$. A BRST invariance shows the integrated signed density is $\beta$-independent, so the eigenvector count remains exponential in $N$ even as $\beta\to\infty$, with lower bound $\sim 2^{(N+1)/2}/\sqrt{3\pi N}$.

## Why it matters here
General background; no direct arena tie. Closest relevance is methodological — the field-theoretic + Schwinger–Dyson treatment of high-dimensional random landscapes and the BBP-like outlier/edge transitions could inform stability analysis or pseudospectrum thinking for any extremal/spectral problem, but none of the 23 arena problems currently use Z-eigenvalues of random tensors.

## Open questions / connections
- Extension to higher-order tensors ($p>3$) and to complex tensors (entanglement entropy of random quantum states).
- Definition of a tensor pseudospectrum based on Z-eigenvalues (cf. matrix pseudospectrum of Trefethen–Embree, H-eigenvalue version of Che–Li–Qi–Wei).
- Connection to spiked-tensor recovery thresholds (Richard–Montanari, Arous–Mei–Montanari–Nica) and to May–Wigner instability on random hypergraphs.
- Behavior of eigenvector overlap $\langle v(\beta), v(0)\rangle$ near $\bar\beta_1$ — numerics suggest it crosses zero there but is unproven.

## Key terms
Z-eigenvalues, random tensors, spherical p-spin glass, Kostlan polynomials, BBP transition, pseudospectrum, signed eigenvalue distribution, Schwinger–Dyson equations, Lefschetz thimble, Hubbard–Stratonovich, BRST invariance, large-N field theory, Auffinger–Ben Arous–Černý, spiked tensor model
