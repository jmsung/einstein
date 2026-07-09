---
type: source
kind: paper
title: Tensor networks for complex quantum systems
authors: R. Orús
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1812.04011
source_local: ../raw/2018-ors-tensor-networks-complex-quantum.pdf
topic: general-knowledge
cites:
---

# Tensor networks for complex quantum systems

**Authors:** R. Orús  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1812.04011

## One-line
A review of tensor network (TN) states and algorithms — compact representations of quantum many-body wavefunctions whose bond dimension $\chi$ encodes entanglement — and their reach across condensed matter, quantum gravity (AdS/CFT), and machine learning.

## Key claim
Anywhere correlations have structure, a tensor network with $O(\text{poly}(N))$ parameters can represent it efficiently: MPS for gapped 1d, PEPS for 2d area-law states, MERA for 1d critical systems with $S(L) = O(\log L)$, and bMERA for area-law violators — with the Schmidt rank $\chi$ bounding entanglement entropy via $S \le \log \chi$.

## Method
Tensor network decomposition of the $O(2^N)$-coefficient wavefunction into a graph of small tensors connected by bond indices of dimension $\chi$. Core numerical tool is the SVD $\Psi = U\Lambda V^\dagger$ (equivalent to the Schmidt decomposition), used both for canonical-form construction and for truncation in $\chi$. Variants — MPS, PEPS, TTN, MERA, bMERA, MPO/PEPO, MPDO — are chosen to match the entanglement / area-law structure of the target Hamiltonian.

## Result
Catalogues the structural properties (block entropy scaling, correlation length, contraction cost, canonical form) of the main TN families: MPS satisfies a strict 1d area law and is exactly contractible; PEPS captures 2d area-law and critical correlations but is #P-hard to contract exactly; MERA reproduces $S(L) \sim \log L$ for 1d CFTs and is conjectured dual to AdS slices (Swingle); bMERA permits arbitrary $S(L)$ scaling, accommodating spin-charge separation. Reviews applications across the 2d Hubbard model, kagome antiferromagnets, lattice gauge theory, quantum chemistry (DMRG), and MBL phases.

## Why it matters here
General background; no direct arena tie. TN/MERA's role as a *structured low-rank ansatz for high-dimensional objects* is the closest analogy to compute-router decisions (parameter count vs precision) on einstein problems, but the specific bounds and tools (SVD truncation, area-law arguments) don't transfer to sphere-packing / autocorrelation / Sidon-set problems on the arena.

## Open questions / connections
- Can PEPS represent chiral topological order with gapped bulk excitations? (Open as of 2018.)
- Holographic dictionary: precise sense in which MERA/cMERA realizes AdS/CFT — bulk geometry from entanglement renormalization (Swingle, Ryu-Takayanagi).
- Neural networks ↔ TN equivalence (Levine–Sharir–Cohen–Shashua 2018): which network classes correspond to which TN topologies, and what does the bond dimension mean for expressivity?

## Key terms
tensor network, matrix product state, MPS, PEPS, MERA, branching MERA, DMRG, Schmidt decomposition, singular value decomposition, area law, entanglement entropy, bond dimension, AdS/CFT, Swingle, Vidal, Cirac, Verstraete, topological order, conformal field theory, many-body localization
