---
type: source
kind: paper
title: Topological modes bound to dislocations in mechanical metamaterials
authors: J. Paulose, B. Chen, V. Vitelli
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1406.3323
source_local: ../raw/2014-paulose-topological-modes-bound-dislocations.pdf
topic: general-knowledge
cites:
---

# Topological modes bound to dislocations in mechanical metamaterials

**Authors:** J. Paulose, B. Chen, V. Vitelli  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1406.3323

## One-line
Shows that lattice dislocations in isostatic mechanical metamaterials bind topologically protected zero modes (or states of self-stress), with their count determined by the dot product of the lattice's topological polarization and the dislocation's Burgers vector.

## Key claim
For an isostatic lattice with topological polarization $P_T$ containing a dislocation of Burgers vector $b$ (dipole moment $d = R_{\pi/2} b$), the net mode index in a region enclosing the dislocation is $\nu = (1/V_{\text{cell}})\, P_T \cdot d$, where $\nu > 0$ counts zero modes and $\nu < 0$ counts states of self-stress. Verified numerically and physically in deformed kagome ($\nu = \pm 1$) and deformed square ($\nu = \pm 2$) lattices.

## Method
Generalized Maxwell counting $\nu = n_m - n_{ss} = N_{df} - N_c$ applied to isostatic lattices ($N_{df} = N_c$ everywhere). The topological polarization $P_T = \sum_i n_i a_i$ is computed from winding numbers $n_i$ of the phase of $\det R(k)$ (Fourier-transformed rigidity matrix) along Brillouin zone cycles. Equation (2) is derived by applying the divergence theorem to the flux of $P_T$ around a dislocation, using the continuum-elasticity relation $b_k = -\int_S dA\, \epsilon_{ij} \partial_i w_{jk}$ between Burgers vector and distortion tensor.

## Result
Numerical diagonalization of the dynamical matrix $D = R^\dagger R$ on lattices with $\sim 10^4$–$10^5$ nodes confirms one localized soft mode at the dislocation aligned with $P_T$ (deformed kagome, $\nu = +1$) and two soft modes at the analogous defect in the deformed square lattice ($\nu = +2$); the opposite dislocation hosts the corresponding states of self-stress. Mode amplitude decays exponentially in most directions but has two anomalously-slow-decay directions $y = \alpha_i x$ tracking the $k$-space directions $k_x = \alpha_i k_y$ along which $\det R(k)$ vanishes to quadratic order. Physical PMMA-triangle prototypes reproduce the predicted asymmetry: the polarization-aligned dislocation moves freely, the anti-aligned one stays rigid.

## Why it matters here
General background; no direct arena tie — this is condensed-matter / topological-mechanics work, not an extremal-combinatorics or sphere-packing result. The closest conceptual relevance is the use of winding numbers of $\det R(k)$ as topological invariants and the Maxwell constraint-counting framework, which could conceivably inform rigidity-based reasoning for discrete-geometry problems (P11 kissing, packing problems) but the connection is weak.

## Open questions / connections
- Theoretical derivation of why real-space weak-localization directions coincide with $k$-space directions of anomalous quadratic dispersion (authors flag this as open).
- Extension to 3D isostatic lattices and to disordered/aperiodic isostatic networks where $P_T$ may not be globally defined.
- Connections to Ran–Zhang–Vishwanath and Teo–Kane dislocation modes in electronic topological insulators (electronic analogue of the same Berry-phase interplay).

## Key terms
isostatic lattice, topological polarization, Maxwell counting, rigidity matrix, Burgers vector, dislocation, zero mode, state of self-stress, kagome lattice, Kane-Lubensky, Berry phase, winding number
