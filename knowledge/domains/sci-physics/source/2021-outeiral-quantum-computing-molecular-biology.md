<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: sci-physics
domains: [sci-physics]
title: "The prospects of quantum computing in computational molecular biology"
authors: [Carlos Outeiral, Martin Strahm, Jiye Shi, Garrett M. Morris, Simon C. Benjamin, Charlotte M. Deane]
year: 2021
doi: 10.1002/wcms.1481
source_url: https://arxiv.org/abs/2005.12792
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# The prospects of quantum computing in computational molecular biology

**Authors:** Carlos Outeiral, Martin Strahm, Jiye Shi, Garrett M. Morris,
Simon C. Benjamin, Charlotte M. Deane (Oxford; Roche pRED; UCB Pharma)
**Year:** 2021 · **Venue:** WIREs Comput. Mol. Sci. 11:e1481 (arXiv 2005.12792)

## TL;DR
A balanced advanced review of where quantum computing could (and could not) help
computational molecular biology — protein structure prediction, molecular
simulation, and ML on biological data. It introduces the algorithms for a
biologist audience and is explicit that the field is **pre-advantage**: the
theoretical speedups are real, but useful, fault-tolerant hardware has not
arrived, and many near-term claims rest on shallow NISQ demonstrations.

## Key contributions
- Surveys three application areas: (1) **simulation** of molecular systems
  (electronic structure via VQE/QPE); (2) **optimization** problems — protein
  folding, structure prediction, alignment — mapped to quantum annealing / QAOA;
  (3) **quantum machine learning** for biological data (quantum kernels, QNNs).
- Pairs each promised speedup with the caveat that breaks it in practice (qubit
  counts, noise, data-loading/IO bottlenecks, the cost of getting classical data
  into a quantum state).
- Written for biologists — explains the algorithms without assuming a physics
  background, making it a good entry point.

## Methods (as reviewed)
Explains quantum primitives (superposition, entanglement, amplitude amplification,
phase estimation) and their algorithmic descendants: Grover-style search for
combinatorial biology problems, variational methods (VQE/QAOA) for the NISQ era,
and quantum ML kernels. Discusses how folding and alignment are encoded as
optimization (Ising/QUBO) problems suitable for annealers.

## Key results / claims
- Genuine asymptotic advantages exist for simulation and some optimization, but
  realizing them needs error-corrected machines well beyond current scale.
- **Data loading is a structural bottleneck** for quantum ML on biological data —
  the cost of encoding large classical datasets can erase the speedup.
- Near-term NISQ results are proofs of concept on toy systems; no demonstrated
  advantage on real molecular-biology problems.

## Limitations / open questions
- Review (2020/2021) — predates current hardware; treat specific qubit/timeline
  figures as dated, the conceptual map as durable.
- Optimistic on quantum ML where the data-loading problem may dominate.
- Little on protein–ligand binding free energy specifically (covered better by
  Santagati 2024 and Cao 2019).
