---
type: source
kind: paper
title: "Mol-Instructions: A Large-Scale Biomolecular Instruction Dataset for Large Language Models"
authors: Yin Fang, Xiaozhuan Liang, Ningyu Zhang, Kangwei Liu, Rui Huang, Zhuo Chen, Xiaohui Fan, Huajun Chen
year: 2023
author: agent
drafted: 2026-05-24
ingested_at: 2026-05-24
source_type: arxiv
source_url: https://arxiv.org/abs/2306.08018
source_local: ../raw/2023-fang-mol-instructions-large-scale-biomolecular-instruct.pdf
topic: general-knowledge
cites:
---

# Mol-Instructions: A Large-Scale Biomolecular Instruction Dataset for Large Language Models

**Authors:** Yin Fang, Xiaozhuan Liang, Ningyu Zhang, Kangwei Liu, Rui Huang, Zhuo Chen, Xiaohui Fan, Huajun Chen  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2306.08018

## One-line
Releases a 2M-entry instruction-tuning dataset for LLMs covering small-molecule, protein, and biomolecular-text tasks, and benchmarks LLaMA fine-tunes on it.

## Key claim
Instruction-tuning LLaMA-7B on Mol-Instructions (≈2,043,587 entries: 148.4K molecule, 505K protein, 53K biotext, spanning 17 subtasks across $>11$ biomolecular property dimensions) materially improves LLM performance on biomolecular tasks (property prediction, reaction prediction, retrosynthesis, protein function/catalytic-activity prediction, CER, CID/CPI extraction, Q&A) versus Alpaca-LoRA, Baize, ChatGLM, Vicuna, Galactica, MolT5, Text+Chem T5, PMC-LLaMA baselines.

## Method
Three-pronged dataset construction: (1) human-AI collaboration where a hand-written task description is expanded by gpt-3.5-turbo and manually reviewed; (2) information derivation from licensed biochem databases (PubChem, UniProtKB/Swiss-Prot+TrEMBL, ChEBI, BC4CHEMD, ChemProt, BC5CDR, MedMCQA, MMLU, PubMedQA) plus self-questioning over PubMed abstracts; (3) template-based conversion of UniProt structured annotations into textual protein-design specs. Quality control: SELFIES (Krenn et al. 2022) replaces SMILES to guarantee validity; MMseqs clustering at 90% similarity removes redundant proteins. Fine-tuning uses LoRA (rank 16, α=16, QV adapters) for molecule/text and full-finetune + DeepSpeed ZeRO for protein, on V100/A800 GPUs.

## Result
Empirical: instruction-tuned LLaMA-7B beats general instruction models and specialized small models on most reported tasks (MAE for HOMO/LUMO/gap property prediction; ROUGE for functional description; entity/relation F1 for CER and CID/CPI). MolT5 underperforms because it lacks instruction tuning; Galactica is closed-data and often outputs negative values for property prediction. Authors caveat that the resulting model is a "preliminary demonstration" not production-ready.

## Why it matters here
General background; no direct arena tie. The Einstein Arena agent works on pure math optimization (sphere packing, kissing numbers, autocorrelation inequalities, extremal graphs); biomolecular instruction tuning shares no concepts, bounds, or techniques with that work. The only weak transferable idea is the self-instruct/template + human-review pipeline for building domain-specific instruction datasets — applicable in principle to constructing a math-problem instruction dataset, but not pursued in this repo.

## Open questions / connections
- Can SELFIES-style "syntactically-safe" representations inspire a similar always-valid encoding for combinatorial/geometric configurations (e.g., point sets that satisfy hard constraints by construction)?
- The self-questioning pipeline (GPT-3.5 extracts Q&A pairs from abstracts) is a template for auto-populating `knowledge/wiki/questions/` from ingested sources — but the wiki currently uses gap-detection (`wiki_graph.py`), not abstract mining.
- Extends instruction-tuning literature (Alpaca, FLAN, Baize, COIG, UltraChat) into a specialized scientific domain; does not extend any math/optimization line of work.

## Key terms
instruction tuning, LLaMA, LoRA, SELFIES, SMILES, UniProtKB, PubChem, self-instruct, biomolecular dataset, protein design, Gene Ontology, Enzyme Commission, chemical entity recognition, gpt-3.5-turbo, MMseqs clustering
