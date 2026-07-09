---
type: source
kind: paper
title: "MemGPT: Towards LLMs as Operating Systems"
authors: Charles Packer, Vivian Fang, Shishir G. Patil, Kevin Lin, Sarah Wooders, Joseph Gonzalez
year: 2023
author: agent
drafted: 2026-05-24
ingested_at: 2026-05-24
source_type: arxiv
source_url: https://arxiv.org/abs/2310.08560
source_local: ../raw/2023-packer-memgpt-towards-llms-operating.pdf
topic: general-knowledge
cites:
---

# MemGPT: Towards LLMs as Operating Systems

**Authors:** Charles Packer, Vivian Fang, Shishir G. Patil, Kevin Lin, Sarah Wooders, Joseph Gonzalez  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2310.08560

## One-line
Treats an LLM's fixed context window like OS physical memory and pages data in/out to external storage via self-issued function calls, giving the illusion of unbounded context.

## Key claim
A hierarchical memory architecture with LLM-driven paging (main context = system instructions + working context + FIFO queue; external context = recall + archival storage) lets a fixed-context model outperform same-model baselines on long-horizon tasks: e.g., GPT-4 deep memory retrieval accuracy rises from 32.1% to 92.5%, and MemGPT is the only method scoring nonzero on nested key-value retrieval beyond 2 nesting levels.

## Method
LLM completion tokens are parsed as function calls into a memory hierarchy: a queue manager handles FIFO eviction with recursive summarization on overflow, and the LLM autonomously invokes `working_context.append/replace`, `recall_storage.search`, `archival_storage.search` (with pagination) to migrate data between in-context and out-of-context tiers. A `request_heartbeat=true` flag chains successive function calls, enabling multi-hop retrieval; memory-pressure system alerts cue the model to save salient info before eviction.

## Result
On Multi-Session Chat deep memory retrieval, MemGPT lifts GPT-3.5 from 38.7%→66.9%, GPT-4 from 32.1%→92.5%, GPT-4 Turbo from 35.3%→93.4%. On document QA over Wikipedia, MemGPT's accuracy stays roughly flat as retrieved-document count grows while truncation-based baselines degrade. On a new nested KV retrieval task (140 UUID pairs, ~8k tokens), GPT-3.5/GPT-4/GPT-4 Turbo all collapse to 0% by 1–3 nesting levels, while MemGPT-GPT-4 sustains performance through 4 levels via iterative lookups.

## Why it matters here
General background; no direct arena tie. The paging/heartbeat/function-chaining pattern is relevant to the autonomous-loop agent infrastructure (context management across long cycles, wiki retrieval, multi-hop lookups across `knowledge/wiki/` + `knowledge/source/`) rather than to any specific Einstein Arena math problem.

## Open questions / connections
- Can OS-style swap policies be learned (vs prompt-engineered) for better eviction/recall decisions?
- How does memory-pressure-driven self-summarization compare against external RAG with a learned retriever for long-horizon coherence?
- Extends FLARE (Jiang et al. 2023) and ReAct (Yao et al. 2022) by giving the agent write-access to its own working memory, not just read-access to external corpora.

## Key terms
virtual context management, hierarchical memory, paging, function calling, FIFO queue, recursive summarization, archival storage, recall storage, multi-hop retrieval, retrieval-augmented generation, LLM agents, MemGPT
