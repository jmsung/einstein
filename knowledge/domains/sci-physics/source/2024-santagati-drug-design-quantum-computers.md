<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: sci-physics
domains: [sci-physics]
title: "Drug design on quantum computers"
authors: [Raffaele Santagati, Alan Aspuru-Guzik, Ryan Babbush, Matthias Degroote, Leticia González, Elica Kyoseva, Nikolaj Moll, Markus Oppel, Robert M. Parrish, Nicholas C. Rubin, Michael Streif, Christofer S. Tautermann, Horst Weiss, Nathan Wiebe, Clemens Utschig-Utschig]
year: 2024
doi: 10.1038/s41567-024-02411-5
source_url: https://arxiv.org/abs/2301.04114
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Drug design on quantum computers

**Authors:** Santagati, Aspuru-Guzik, Babbush, Degroote, González, Kyoseva, Moll,
Oppel, Parrish, Rubin, Streif, Tautermann, Weiss, Wiebe, Utschig-Utschig
(Boehringer Ingelheim Quantum Lab, Google Quantum AI, Univ. Toronto, QC Ware, BASF, academia)
**Year:** 2024 (Nat. Phys.; arXiv 2023) · **Venue:** Nature Physics 20:549–557

## TL;DR
An industry-authored *perspective* (Boehringer Ingelheim + Google Quantum AI) on
where quantum computers could realistically help drug design. The honest thesis:
the value is concentrated in **accurate quantum-chemical calculations** for the
small, strongly-correlated subproblems that classical methods (DFT, force fields,
FEP) handle poorly — *not* a wholesale replacement of the computational-chemistry
stack — and useful impact requires **fault-tolerant** hardware that does not yet
exist.

## Key contributions
- Maps drug-discovery tasks to where QM accuracy is the bottleneck: binding free
  energies, covalent/transition-state chemistry, metalloenzymes, excited states
  and photochemistry, and parameterizing classical force fields/FEP from better
  reference energies.
- Frames quantum computing as a **reference-energy accelerator** feeding the
  existing multiscale pipeline (QM/MM, FEP), not a standalone affinity engine.
- Gives realistic resource estimates: chemically-relevant electronic-structure
  targets need error-corrected qubits and deep circuits → a fault-tolerant, not
  NISQ, regime.

## Methods (as reviewed)
Surveys the two algorithm families: **variational quantum eigensolver (VQE)** —
near-term, shallow circuits, but with measurement-cost and barren-plateau
problems — and **quantum phase estimation (QPE)** — asymptotically powerful,
exact eigenenergies, but requires fault tolerance. Discusses Hamiltonian
representation, active-space selection (only the strongly-correlated orbitals go
on the quantum device), and embedding the quantum solver inside classical QM/MM
and free-energy workflows.

## Key results / claims
- Quantum advantage in drug design is **task-specific**, concentrated in
  strongly-correlated electronic structure; most of a campaign stays classical.
- No quantum advantage on real targets today; the limiting resource is
  fault-tolerant hardware (logical qubits, gate depth), years out.
- The credible near-to-mid-term role is improving the **reference energies** that
  calibrate classical FEP/force fields, tightening the accuracy of the affinity
  predictions that classical methods already make at scale.

## Limitations / open questions
- Perspective, not benchmark — no head-to-head accuracy numbers on drug targets.
- Hardware timeline uncertain; resource estimates assume error correction.
- Large protein pockets remain classical; only small fragments/active spaces are
  quantum-tractable for the foreseeable future.
