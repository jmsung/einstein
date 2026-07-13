<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory"
authors: [Prateek Chhikara, Dev Khant, Saket Aryan, Taranjeet Singh, Deshraj Yadav]
year: 2025
source_url: https://arxiv.org/abs/2504.19413
drive_file_id: 13Cf1RgpFdiU9pDAhisIhqrWSm0uGJOTO
text_source: pdf
ingested_by: agent
---
# Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory

**Authors:** Prateek Chhikara, Dev Khant, Saket Aryan, Taranjeet Singh, Deshraj Yadav  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2504.19413

## One-line
Mem0 is a memory-centric architecture that dynamically extracts, consolidates, and retrieves salient conversational facts, giving LLM agents coherent long-term memory without relying on ever-larger context windows.

## Key claim
Selective, structured memory management (extract → consolidate → retrieve) outperforms both full-context processing and existing memory-augmented/RAG baselines on long-term conversational QA, while cutting token cost and latency dramatically — extended context windows alone do not solve long-term coherence because real conversations are thematically discontinuous and attention degrades over distant tokens.

## Method
Two architectures, both using GPT-4o-mini as the LLM backbone:
- **Mem0**: two-phase pipeline. (1) *Extraction phase* — given a new message pair $(m_{t-1}, m_t)$, combines a periodically-refreshed conversation summary $S$ with the last $m$ messages ($m=10$) to form a prompt $P$; an LLM extraction function $\phi(P)$ outputs a set of candidate salient facts $\Omega = \{\omega_1, ..., \omega_n\}$. (2) *Update phase* — for each candidate fact, retrieves the top $s$ ($s=10$) semantically similar existing memories via vector embeddings, then an LLM tool-call interface chooses one of four operations: ADD (new fact), UPDATE (augment existing memory), DELETE (existing memory contradicted), or NOOP (no change) — replacing a separate classifier with LLM reasoning directly.
- **Mem0^g**: extends Mem0 with a graph memory layer. Memories are a directed labeled graph $G=(V,E,L)$: nodes are entities (with type, embedding, creation timestamp), edges are labeled relationships (e.g., `lives_in`), stored via Neo4j. An *entity extractor* LLM module identifies entities; a *relationship generator* LLM module derives relationship triplets $(v_s, r, v_d)$. On update, new triplets are matched against existing nodes by embedding similarity threshold $t$ (reusing or creating nodes), and a *conflict detector* + LLM *update resolver* mark relationships obsolete (not deleted) rather than removing them, preserving temporal reasoning. Retrieval is dual-path: entity-centric subgraph traversal from anchor entities, plus semantic-triplet matching of the whole query against relationship embeddings.

Evaluated on the LOCOMO benchmark (10 long multi-session conversations, ~600 dialogue turns / ~26,000 tokens each, ~200 QA pairs/conversation across single-hop, multi-hop, temporal, open-domain categories) against six baseline categories: established memory systems (LoCoMo, ReadAgent, MemoryBank, MemGPT, A-Mem), open-source LangMem, RAG (chunk sizes 128–8192, k∈{1,2}), full-context processing, OpenAI's ChatGPT memory feature, and Zep (commercial memory platform). Metrics: F1, BLEU-1, and LLM-as-a-Judge (J) for quality; token consumption and p95/search/total latency for deployment cost.

## Result
- Mem0 achieves **J=67.13** (single-hop), **51.15** (multi-hop), **72.93** (open-domain), **55.51** (temporal); Mem0^g achieves **J=65.71, 47.19, 75.71, 58.13** respectively — both set new SOTA on most categories, beating A-Mem by >25 J points on single-hop.
- Averaged across categories, **Mem0 achieves 26% relative improvement in LLM-as-a-Judge over OpenAI's memory feature**; Mem0^g scores ~2% higher overall than base Mem0.
- Zep edges out both Mem0 variants on open-domain questions (J=76.60 vs. Mem0^g's 75.71, a 0.89-point lead) — the one category where a baseline wins.
- Graph memory (Mem0^g) helps most on temporal reasoning (J=58.13, best overall) but gives **no gain on multi-hop** and a slight drop on single-hop vs. base Mem0, indicating relational structure helps only for queries needing explicit relationship/temporal grounding.
- Deployment efficiency: Mem0 achieves **91% lower p95 latency** and **>90% lower token cost** than the full-context baseline, while still matching or beating it on quality — the core practical selling point over "just use a bigger context window."

## Key terms
long-term memory, memory-augmented LLM agents, LOCOMO benchmark, memory extraction, memory consolidation, graph memory, entity extraction, relationship triplets, LLM-as-a-Judge, retrieval-augmented generation, ADD/UPDATE/DELETE/NOOP operations, temporal reasoning, multi-hop QA, token cost, p95 latency
