<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-retrieval]
title: Opportunities for retrieval and tool augmented large language models in scientific facilities
authors: [Michael H. Prince, Henry Chan, Aikaterini Vriza, Tao Zhou, V. Sastry, Yanqi Luo, M. Dearing, Ross J. Harder, Rama K. Vasudevan, M. Cherukara]
year: 2023
source_url: https://arxiv.org/abs/2312.01291
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Opportunities for retrieval and tool augmented large language models in scientific facilities

**Authors:** Michael H. Prince, Henry Chan, Aikaterini Vriza, Tao Zhou, V. Sastry, Yanqi Luo, M. Dearing, Ross J. Harder, Rama K. Vasudevan, M. Cherukara  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2312.01291

## One-line
Describes CALMS, a retrieval- and tool-augmented LLM agent that helps scientists at DOE user facilities (Advanced Photon Source, nanoscience centers) design experiments and drive instruments via natural language.

## Key claim
With retrieval-augmented context from facility documentation and ReAct-style tool calls, GPT-3.5 Turbo can answer facility-specific Q&A relevantly and without hallucination, and can autonomously drive a real diffractometer to a requested Bragg peak; the open-source Vicuna-13b-v1.5 matches Q&A relevance with context but fails to reliably emit structured JSON tool calls.

## Method
Four components: (i) an LLM (GPT-3.5 Turbo or Vicuna 1.5-16k), (ii) a moving-window conversational memory of the last K=6 turns, (iii) semantic retrieval from a ChromaDB vector store returning top N=4 chunks via embedding similarity, and (iv) tool calls (Materials Project API, SPEC diffractometer control) orchestrated through LangChain's Structured-input ReAct with Chain-of-Thought prompting. Evaluation uses human grading of relevance (yes/no), hallucination (yes/no), and completeness (0–5) across user-facility queries.

## Result
On experimental-design and operations questions, both models hallucinate without context (e.g., inventing a fake tool "ImageSim" instead of the real `ingrained`); with retrieved context, both produce relevant, truthful answers and GPT-3.5 Turbo scores multiple 5/5 on completeness while Vicuna trails. End-to-end automated execution succeeded only with GPT-3.5: a single prompt "set diffractometer to WSe$_2$ 012 Bragg peak" triggered `GetLatticeConstants` → Materials Project API → `SetDiffractometer` → SPEC motor move on APS beamline 34.

## Key terms
retrieval-augmented generation, RAG, tool-augmented LLM, ReAct, Chain-of-Thought, ChromaDB vector store, semantic search, GPT-3.5 Turbo, Vicuna, Materials Project API, scientific instrument control, agent architecture
