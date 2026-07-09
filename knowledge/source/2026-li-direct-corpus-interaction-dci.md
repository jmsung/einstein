---
type: source
kind: paper
title: Beyond Semantic Similarity: Rethinking Retrieval for Agentic Search via Direct Corpus Interaction
authors: Zhuofeng Li, Haoxiang Zhang, et al.
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2605.05242
source_local: ../raw/2026-li-direct-corpus-interaction-dci.pdf
topic: agentic-harness
cites: 
---

# Beyond Semantic Similarity: Rethinking Retrieval for Agentic Search via Direct Corpus Interaction

**Authors:** Zhuofeng Li, Haoxiang Zhang, et al.  ·  **Year:** 2026  ·  **Source:** https://arxiv.org/abs/2605.05242

## One-line
Replaces the conventional top-$k$ retriever interface with **direct corpus interaction (DCI)** — the agent searches the raw corpus via terminal tools (`grep`, `find`, file reads, shell pipelines) — and shows this beats sparse/dense/reranking retrievers across agentic search benchmarks.

## Key claim
On BrowseComp-Plus with Claude Sonnet 4.6, swapping the Qwen3-Embedding-8B retriever for DCI raises accuracy from $69.0\%$ to $80.0\%$ ($+11.0$ pts) while cutting API cost from $\$1{,}440$ to $\$1{,}016$ ($-29.4\%$); on multi-hop QA, DCI-Agent-CC reaches $83.0$ avg vs $52.3$ for the strongest retrieval-agent baseline ($+30.7$ pts); on IR ranking (BRIGHT+BEIR), $68.5$ avg NDCG@10 vs $47.0$ for ReasonRank-32B ($+21.5$ pts).

## Method
Two scaffolds: **DCI-Agent-Lite** (Pi-based, GPT-5.4 nano, only `bash`+`read` exposed) and **DCI-Agent-CC** (Claude Code, Sonnet 4.6) — both bypass any embedding model, vector index, or retrieval API and compose primitives like `grep -n`, `find | grep | grep`, `head`, `sed`, file reads. A runtime context-management layer (levels L0–L4) combines tool-result truncation (20K–50K char caps), zero-LLM compaction of older tool-result turns (trigger at 240K chars, keep last 12 turns), and model-generated summarization under further pressure. Two trajectory-level metrics evaluate process quality: **coverage** (gold-doc reach: any/mean/all) and **localization** $s(d^*,\tau) = \max_{d_{t,i}\in H(d^*,\tau)} \psi(\nu(\ell_{t,i}); \nu(|d^*|))$ where $\psi(a;b)=\max(1-\log a/\log b,\, 0)$ measures within-document evidence narrowing.

## Result
DCI dominates retrieval baselines on most benchmarks with no offline indexing, no embeddings, no reranker. Critically, ablation shows DCI's gains do **not** come from surfacing more gold documents — even when retrieval agents already surface all gold evidence, DCI prevails by converting surfaced evidence into finer-grained local search/verification (higher localization score). Authors frame this as **retrieval interface resolution**: the ability to operate on units smaller than documents/passages. The benefit persists under restricted tool profiles (Lite scaffold matches/beats baselines on QA+IR).

## Why it matters here
General background; no direct arena tie. However, the *interface-design* framing directly informs how the einstein agent should access its own corpora — `docs/wiki/`, `docs/source/`, `mb/` — suggesting `grep`/`find`/`Read` composition may outperform `qmd query` (vector retrieval) for tasks needing exact lexical match (problem IDs, persona names, dead-end slugs, citation paths), while qmd retains its role for fuzzy semantic recall. The trajectory-coverage/localization metrics offer a template for evaluating the agent's own wiki-first lookup discipline.

## Open questions / connections
- Does DCI scale to 10×–100× larger corpora than tested (BrowseComp-Plus + Wikipedia dump)? The paper's scaling study delineates an operating envelope but stops short of web-scale.
- Hybrid interfaces: when is dense retrieval still strictly better (broad fuzzy recall over heterogeneous semantics) vs DCI (exact patterns, weak-clue conjunctions, span-level verification)?
- Connects to Sutawika et al. (2026) on CLI primitives for code localization and Subramanian et al. (2025) on keyword-search agents over raw PDFs approaching vector-DB RAG.
- Failure modes documented (Case 5b): overly broad `rg` patterns + bad query formulation lead to hallucinated answers — the interface only helps if the agent can compose precise queries.

## Key terms
direct corpus interaction, DCI, agentic search, retrieval-augmented generation, RAG, retrieval interface resolution, BrowseComp-Plus, BRIGHT, BEIR, multi-hop QA, NDCG@10, coverage, localization, grep, Claude Code, BM25, dense retrieval, reranking, context management, trajectory metrics
