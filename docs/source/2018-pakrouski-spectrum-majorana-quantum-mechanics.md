---
type: source
kind: paper
title: Spectrum of Majorana Quantum Mechanics with O(4)^{3} Symmetry.
authors: K. Pakrouski, I. Klebanov, F. Popov, G. Tarnopolsky
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1808.07455
source_local: ../raw/2018-pakrouski-spectrum-majorana-quantum-mechanics.pdf
topic: general-knowledge
cites:
---

# Spectrum of Majorana Quantum Mechanics with O(4)^{3} Symmetry.

**Authors:** K. Pakrouski, I. Klebanov, F. Popov, G. Tarnopolsky  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1808.07455

## One-line
Numerical Lanczos diagonalization of a 3-index Majorana tensor quantum mechanics with $O(4)^3$ symmetry, exploiting $U(1)\times U(1)$ Cartan charge sectors and discrete symmetries to extract all gauge-singlet energies and propose closed-form expressions.

## Key claim
The $2^{32}$-dimensional Hilbert space of the $O(4)^3$ quartic Majorana Hamiltonian decomposes via $U(1)\times U(1)$ charges into manageable sectors; all 36 $SO(4)^3$ gauge-singlet energies are determined exactly, with ground state $E_0 \approx -160.140170 = -\tfrac{3}{2}\sqrt{447+\sqrt{125601}}$, and residual discrete symmetry group is identified as $A_4 \times \mathbb{Z}_2$ (enhanced to $S_4 \times \mathbb{Z}_2$, the full cube group, at $E=0$).

## Method
Lanczos algorithm on sparse 16+16 qubit matrices, using the $O(N)^2 \times U(N/2)$ basis (raising/lowering operators $\bar c_{abk}, c_{abk}$) to split the $2^{32}$ space into 289 charge sectors. Symmetry resolution adds penalty term $H + 100\sum_i C_{2i} + \sum_i a_i P_i$ to push non-singlet states up and split parity-degenerate states. Closed-form singlet energies inferred from the small dimension of fixed-parity subspaces, e.g. an order-2 polynomial in $E^2$ when only two singlets share parities $(P_1,P_2,P_3)=(-,-,-)$.

## Result
Largest sector $(Q_0,Q_1)=(0,0)$ has $\binom{16}{8}^2 \approx 1.66\times 10^8$ states. Singlet spectrum is symmetric under $E\to -E$, with degeneracies $\{1,2,3\}$ tracing to real irreps of $A_4$. Notable exact values: $\pm 8\sqrt{23}\approx \pm 38.367$, $\pm 8\sqrt{24}\approx \pm 39.192$, $\pm 8\sqrt{123}\approx \pm 88.724$, plus quartic-polynomial roots $\pm\tfrac{3}{2}\sqrt{187\pm\sqrt{11481}}$ and $\pm\tfrac{3}{2}\sqrt{447\pm\sqrt{125601}}$. Ratio $E_0/E_{\rm bound}\approx 0.96$ shows large-$N$ approximations fail at $N=4$.

## Why it matters here
General background; no direct arena tie. The methodology — exploiting Cartan-subgroup charge conservation and discrete symmetry penalty terms to make $\sim 10^8$-dim sparse eigenproblems tractable via Lanczos — is methodologically transferable to any large discrete optimization with block-diagonal symmetry structure, but the Einstein Arena problems (sphere packing, autocorrelation, kissing numbers, etc.) do not involve fermionic tensor Hamiltonians.

## Open questions / connections
- Exact analytic derivation of the polynomial coefficients $A_i$ governing singlet energies (left for future work).
- Extension of the symmetry-resolved Lanczos method to larger $N$ in the $O(N)^3$ Klebanov–Tarnopolsky model where $2^{N^3/2}$ explodes.
- Why does large-$N$ propagator approximation give $E_0/E_{\rm bound}\approx 0.41$ vs. actual $0.96$ at $N=4$ — what is the convergence rate?

## Key terms
SYK model, tensor model, Majorana fermions, melonic diagrams, $O(N)^3$ symmetry, Lanczos algorithm, gauge singlets, $A_4 \times Z_2$, discrete parity symmetry, quadratic Casimir, charge sector decomposition, sparse exact diagonalization
