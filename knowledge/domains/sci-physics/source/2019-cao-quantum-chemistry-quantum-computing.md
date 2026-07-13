<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: sci-physics
domains: [sci-physics]
title: "Quantum Chemistry in the Age of Quantum Computing"
authors: [Yudong Cao, Jonathan Romero, Jonathan P. Olson, Matthias Degroote, Peter D. Johnson, Mária Kieferová, Ian D. Kivlichan, Tim Menke, Borja Peropadre, Nicolas P. D. Sawaya, Sukin Sim, Libor Veis, Alán Aspuru-Guzik]
year: 2019
doi: 10.1021/acs.chemrev.8b00803
source_url: https://arxiv.org/abs/1812.09976
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Quantum Chemistry in the Age of Quantum Computing

**Authors:** Yudong Cao, Jonathan Romero, Jonathan P. Olson, Matthias Degroote,
Peter D. Johnson, Mária Kieferová, Ian D. Kivlichan, Tim Menke, Borja Peropadre,
Nicolas P. D. Sawaya, Sukin Sim, Libor Veis, Alán Aspuru-Guzik
(Harvard, Zapata Computing, Univ. Toronto)
**Year:** 2019 · **Venue:** Chem. Rev. 119(19):10856–10915 (arXiv 1812.09976)

## TL;DR
The canonical, comprehensive review of **quantum algorithms for the
electronic-structure problem** — how to compute molecular ground- and
excited-state energies on a quantum computer. It is the methods foundation behind
"quantum computing for drug discovery": everything downstream (binding energies,
reaction energetics) reduces to solving the molecular Hamiltonian accurately,
which is exactly what these algorithms target.

## Key contributions
- End-to-end treatment of the electronic-structure pipeline on quantum hardware:
  second-quantized Hamiltonian → **fermion-to-qubit mapping** (Jordan–Wigner,
  Bravyi–Kitaev, parity) → state preparation → energy estimation → measurement.
- Detailed comparison of the two algorithm families: **quantum phase estimation
  (QPE)** (exact, fault-tolerant, deep circuits) vs **variational quantum
  eigensolver (VQE)** (NISQ-friendly, shallow, but measurement- and
  optimization-limited).
- Covers ansatz design (UCC and hardware-efficient), error mitigation, active-space
  reduction, and resource/qubit estimates for chemically meaningful systems.

## Methods (as reviewed)
Lays out how molecular orbitals and electron correlation are encoded in qubits,
the trade-offs of each fermionic encoding (locality vs qubit count), and how VQE
optimizes a parameterized circuit against the Hamiltonian expectation value while
QPE extracts eigenphases. Discusses the measurement problem (number of Pauli
terms scales steeply with system size) and strategies to tame it.

## Key results / claims
- The electronic-structure problem is the **natural killer app** for quantum
  computing — quantum systems simulating quantum systems — and strong correlation
  (where classical DFT/coupled-cluster struggle) is where advantage should appear.
- VQE is the realistic near-term route but is bounded by measurement cost and
  classical-optimizer issues (e.g. barren plateaus); QPE needs error correction.
- Chemically-relevant accuracy on non-trivial molecules requires resources beyond
  current devices — a fault-tolerant target.

## Limitations / open questions
- 2019 review — algorithmic landscape has advanced (better measurement schemes,
  qubitization); the conceptual framework and encodings remain canonical.
- Heavy on the chemistry/algorithms layer; not drug-discovery-specific (pair with
  Santagati 2024 for the drug-design framing).
- Real-system resource estimates remain daunting; no demonstrated advantage on
  drug-relevant molecules.
