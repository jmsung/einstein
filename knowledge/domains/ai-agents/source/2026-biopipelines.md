<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "BioPipelines: Accessible Computational Protein and Ligand Design for Chemical Biologists"
authors: [Gianluca Quargnali, Pablo Rivera-Fuentes]
year: 2026
doi: 10.64898/2026.03.11.711024
source_url: https://www.biorxiv.org/content/10.64898/2026.03.11.711024v1
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# BioPipelines: Accessible Computational Protein and Ligand Design for Chemical Biologists

## TL;DR
BioPipelines is an open-source Python framework that lets experimental chemical biologists chain >30 deep-learning protein/ligand design tools (RFdiffusion, ProteinMPNN, AlphaFold2, Boltz2, LigandMPNN, etc.) into multi-step workflows written in a few lines of experiment-like code — prototyped interactively in Jupyter, then submitted unchanged to a SLURM cluster, with new tools addable via AI coding agents.

## Key findings
- **Three design objectives**: (1) *abstraction* — pipelines read like experiment descriptions; (2) *modularity* — any tool integrates via a standardized biomolecular interface; (3) *testability* — the same code runs interactively in Jupyter/Colab and at production scale.
- **Two-phase execution**: a Python *configuration phase* predicts the resulting filesystem structure and generates self-contained bash scripts; only afterward does the *execution phase* run them. **No long-running orchestrator is required during cluster execution** — generated scripts can be inspected, modified, or resubmitted independently, doubling as execution artifacts and documentation.
- **Three core typed data streams** flow between tools: (1) *structures* (.pdb/.cif/.sdf), (2) *sequences* (1D protein/DNA/RNA), (3) *compounds* (SMILES/CCD), plus associated tabular data. Tools map input streams → output streams (e.g. ProteinMPNN: structures→sequences; AlphaFold2: sequences→structures; Boltz2: sequences+compounds→structures).
- **Five demonstrated applications**:
  1. *Inverse folding / gene synthesis* — redesign ubiquitin (PDB 4LCD) with soluble-trained ProteinMPNN, fold with AF2, encode codon-optimized DNA via a DNAEncoder using CoCoPUTs codon tables with thresholded weighted sampling.
  2. *De novo domain redesign* — replace the adenylate kinase LID domain (PDB 4AKE, residues A118–160) with RFdiffusion backbones of length 50–70; ProteinMPNN designs 2 seqs/backbone; AF2 validates. Per-structure designed positions flow automatically to ProteinMPNN without manual file parsing.
  3. *Compound-library screening* — screen tryptophan derivatives against the TrpR homodimer + DNA operator (PDB 1TRO) using Boltz2 cofolding; combinatorial `Bundle`/`Each` assistants control entity inclusion; outputs binding probability (unitless) + affinity (µM).
  4. *FRET calcium sensor modeling* — fuse EBFP–calmodulin–EYFP with variable linkers (4×4 = 16 constructs via the `Fuse` tool); predict apo and Ca²⁺-bound forms with Boltz2; MSAs recycled between states to reduce server load; measure chromophore distance/inter-domain angle.
  5. *Iterative binding-site optimization* — evolve the NocT periplasmic binding protein pocket for histopine binding with LigandMPNN over cycles, generating 10 mutants/cycle by weighted sampling on mutation frequencies; carry forward the best predicted-affinity structure each round.
- **AI-agent extensibility**: new tools for published GitHub repos are implemented by giving Claude Code (Opus 4.6) the repo URL and one instruction ("Implement a BioPipelines tool for the repository: <url> conforming to the existing tool standards"); the agent reads install/IO/CLI docs and generates the install script, parameter validation, bash generation, and output parsing. Adding a tool requires implementing only four methods; base classes handle environment activation, completion tracking, and standardized output.
- Substantial portions of the codebase itself were written/refactored by Claude Code (Opus 4.6). MIT-licensed at github.com/locbp-uzh/biopipelines.

## Methods (brief)
Software framework paper: pure-Python package with typed interfaces (enabling IDE autocompletion/type-checking), built on Python context managers for natural-language-like syntax, pandas for table ops, py3Dmol for inline 3D rendering, and SLURM for cluster submission. Validation is by worked application examples rather than wet-lab benchmarking.

## Limitations
No experimental validation — all five applications are computational demonstrations of framework ergonomics, not benchmarked design outcomes. Binding affinities rely on Boltz2 regression, which the authors flag as "arguably less reliable" than its classification output (citing Bret et al. 2026). Not peer-reviewed (bioRxiv preprint). Generalizability to arbitrary tools depends on each tool fitting the three-stream type model.

## Citations of interest
- Jumper et al. 2021 (*Nature*) — AlphaFold2, the structure-prediction backbone used throughout.
- Watson et al. 2023 (*Nature*) — RFdiffusion, backbone generation for de novo/domain redesign.
- Dauparas et al. 2022 (*Science*) — ProteinMPNN inverse folding; and Dauparas et al. 2025 (*Nat. Methods*) — LigandMPNN for ligand-aware sequence design.
- Passaro et al. 2025 (bioRxiv) — Boltz-2 cofolding + binding affinity prediction, central to the screening/sensor examples.
- Bret et al. 2026 (*JCIM*) — assessment of Boltz-2 binding-classification performance, basis for the affinity-reliability caveat.
- Mirdita et al. 2022 (*Nat. Methods*) — ColabFold, the prior art for democratizing folding tools.
