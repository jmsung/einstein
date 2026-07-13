<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-retrieval, sci-chem]
title: "HoneyComb: A Flexible LLM-Based Agent System for Materials Science"
authors: [Huan Zhang, Yu Song, Ziyu Hou, Santiago Miret, Bang Liu]
year: 2024
source_url: https://arxiv.org/abs/2409.00135
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# HoneyComb: A Flexible LLM-Based Agent System for Materials Science

**Authors:** Huan Zhang, Yu Song, Ziyu Hou, Santiago Miret, Bang Liu  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2409.00135

## One-line
An LLM-based agent system for materials science that augments base LLMs with a curated knowledge base (MatSciKB) and an inductively-constructed tool hub (ToolHub) plus a hybrid BM25+Contriever retriever.

## Key claim
Combining a domain knowledge base with a domain tool hub and a hybrid retriever substantially raises QA accuracy of generic LLMs on materials-science benchmarks — e.g. GPT-4 on MaScQA: $58.46 \to 79.07$ (+20.61), HoneyBee on SciQA: $33.96 \to 79.69$ (+45.73).

## Method
Three components: (1) **MatSciKB** — 38,469 entries from arXiv abstracts, Wikipedia, textbooks, datasets, formulas, and GPT-generated examples, organized into 16 topical categories via BERTopic clustering; (2) **ToolHub** — 6 general tools (Google/Scholar/arXiv/Wikipedia/YouTube search + Python REPL) plus domain-specific APIs built by **Inductive Tool Construction** (LLM drafts a function per training question, human verifies, then decomposes into reusable atomic functions); (3) **Two-phase Assessor→Executor protocol** that filters relevant tools, decomposes complex queries into subquestions, calls tools, and reflects on observations. Retrieval is a two-step BM25 (fast top-N) + Contriever embedding similarity (top-3) hybrid.

## Result
On MaScQA (650 GATE engineering questions, 14 domains) HoneyComb improved every backbone (HoneyBee +16.76, GPT-3.5 +4.92, GPT-4 +20.61, Llama2 +14.16, Llama3 +22.61). On SciQA (11,679 multi-choice) gains range from +0.14 (GPT-3.5, already near-ceiling) to +45.73 (HoneyBee). Ablation on GPT-4: MatSciKB-only 78.31, ToolHub-only 73.23, both+retriever 79.07 on MaScQA; ToolHub-only drops SciQA to 85.57 while MatSciKB-only reaches 96.34, indicating dataset-dependent component value.

## Key terms
LLM agent, retrieval-augmented generation, materials science, knowledge base, tool hub, inductive tool construction, BM25, Contriever, hybrid retrieval, BERTopic, MaScQA, SciQA, ReAct-style executor, Python REPL
