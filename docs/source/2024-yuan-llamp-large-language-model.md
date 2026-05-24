---
type: source
kind: paper
title: "LLaMP: Large Language Model Made Powerful for High-fidelity Materials Knowledge Retrieval and Distillation"
authors: Chiang Yuan, Chia-Hong Chou, Janosh Riebesell
year: 2024
author: agent
drafted: 2026-05-24
ingested_at: 2026-05-24
source_type: arxiv
source_url: https://arxiv.org/abs/2401.17244
source_local: ../raw/2024-yuan-llamp-large-language-model.pdf
topic: general-knowledge
cites:
---

# LLaMP: Large Language Model Made Powerful for High-fidelity Materials Knowledge Retrieval and Distillation

**Authors:** Chiang Yuan, Chia-Hong Chou, Janosh Riebesell  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2401.17244

## One-line
A hierarchical multi-agent ReAct framework that grounds LLMs in the Materials Project database to retrieve high-fidelity materials data and run atomistic simulations without fine-tuning.

## Key claim
A supervisor ReAct agent dispatching specialized assistant ReAct agents (each owning one API schema) dramatically reduces hallucination on materials property queries vs. vanilla LLMs — e.g., bulk-modulus MAE drops from ~41 GPa (GPT-4) to 14.57 GPa, magnetic-ordering classification accuracy rises from 0.48 to 0.98, and magnetization $R^2$ improves from $-0.20$ to $0.992$.

## Method
**Hierarchical ReAct orchestration**: a top-level supervisor agent decomposes queries and routes subtasks to specialized assistant agents, each scoped to a single tool/API endpoint (MP elasticity, thermodynamics, magnetism, synthesis, arXiv, Python REPL, MLFF MD). Each assistant uses ReAct's iterative thought–action–observation loop with self-correcting tool calls. The expanded action space is $\hat{A} = A \cup L$ (language + tool actions). A self-consistency metric $\text{SCoR} = \text{CoP} \times \text{Confidence}$, with $\text{CoP} = \exp(-\hat{\sigma}/\sqrt{n})$, quantifies reproducibility across $N$ trials.

## Result
LLaMP outperforms StructChem, Darwin, GPT-4+Serp, GPT-4, Gemini-Pro, and Llama-3 across bulk moduli, formation energies, common and multi-element bandgaps, with the highest SCoR and lowest MAE in every category (e.g., formation-energy MAE 0.009 eV vs. 1.6–8 eV baseline). Ablation shows grounding quality correlates with backbone function-calling ability (Claude-3.5-Sonnet > Gemini-1.5-Flash > Llama-3-8B). Demonstrated capabilities: crystal-structure editing (Li insertion in diamond-cubic Si), DOI-grounded inorganic synthesis recipes, and an end-to-end MACE-MP-0 NVT annealing MD workflow on a 270-atom LiTaO₃ supercell.

## Why it matters here
General background; no direct arena tie. The relevance is methodological: hierarchical ReAct orchestration with one-tool-per-assistant agents, and the SCoR metric for measuring response self-consistency, are directly transferable patterns for the einstein autonomous-loop council-dispatch and verifier infrastructure.

## Open questions / connections
- Can SCoR-style precision/confidence metrics be used to score local optimizer agreement (a soft version of triple-verify)?
- Does the one-API-per-agent pattern outperform a single agent with full schema for the council-dispatch persona system?
- The bandgap gap between GGA-DFT (MP) and experiment (40–50% underestimate) remains open — analogous to local-vs-arena verifier drift on Einstein problems.

## Key terms
retrieval-augmented generation, ReAct agent, hierarchical agent orchestration, function calling, tool use, self-consistency metric, SCoR, Materials Project, DFT, hallucination mitigation, multimodal RAG, MACE-MP-0
