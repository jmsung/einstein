---
type: source
kind: paper
title: Opportunities for retrieval and tool augmented large language models in scientific facilities
authors: Michael H. Prince, Henry Chan, Aikaterini Vriza, Tao Zhou, V. Sastry, Yanqi Luo, M. Dearing, Ross J. Harder, Rama K. Vasudevan, M. Cherukara
year: 2023
author: agent
drafted: 2026-05-24
ingested_at: 2026-05-24
source_type: arxiv
source_url: https://arxiv.org/abs/2312.01291
source_local: ../raw/2023-prince-opportunities-retrieval-tool-augmented.pdf
topic: general-knowledge
cites:
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

## Why it matters here
General background; no direct arena tie. The retrieval-augmented + tool-calling architecture (vector store of chunked docs, top-N=4 retrieval, ReAct tool dispatch) is structurally the same pattern as this repo's wiki-first lookup + council dispatch + skill-library loop — useful as an external reference for the autonomous-loop branch's design.

## Open questions / connections
- Can fine-tuned open-source models (Vicuna successors) be made reliable enough to emit valid JSON for structured tool calls, closing the gap with GPT-3.5?
- How does retrieval quality scale when the document store contains decades of e-logs rather than curated docs — does top-N=4 chunking still suffice?
- What evaluation protocol distinguishes "relevant + hallucinated" from "irrelevant + truthful" responses systematically (current scoring is human-graded)?

## Key terms
retrieval-augmented generation, RAG, tool-augmented LLM, ReAct, Chain-of-Thought, ChromaDB vector store, semantic search, GPT-3.5 Turbo, Vicuna, Materials Project API, scientific instrument control, agent architecture
