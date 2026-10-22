---
type: source
kind: paper
title: "LitSearch: A Retrieval Benchmark for Scientific Literature Search"
authors: Anirudh Ajith, Mengzhou Xia, Alexis Chevalier, Tanya Goyal, Danqi Chen, Tianyu Gao
year: 2024
author: agent
drafted: 2026-05-24
ingested_at: 2026-05-24
source_type: arxiv
source_url: https://arxiv.org/abs/2407.18940
source_local: ../raw/2024-ajith-litsearch-retrieval-benchmark-scientific.pdf
topic: general-knowledge
cites:
---

# LitSearch: A Retrieval Benchmark for Scientific Literature Search

**Authors:** Anirudh Ajith, Mengzhou Xia, Alexis Chevalier, Tanya Goyal, Danqi Chen, Tianyu Gao  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2407.18940

## One-line
Introduces a 597-question benchmark of realistic scientific-literature search queries for evaluating retrieval and reranking systems on ML/NLP papers.

## Key claim
On LitSearch, the best dense retriever (GritLM-7B) achieves recall@5 of 74.8%, beating BM25 by 24.8 absolute points; GPT-4o reranking adds another 4.4%, while commercial engines (Google Search, Scholar, Elicit) trail the best dense retriever by up to 32 recall points.

## Method
Two-pronged dataset construction: (1) GPT-4 rewrites sampled S2ORC inline citation mentions into literature-search questions, filtered by word-overlap with target titles ($>0.3$ for ACL-sourced, $>0.1$ for non-ACL dropped); (2) authors of ACL 2023 / ICLR 2024 papers write queries about their own work. All 597 questions are manually inspected for specificity (≤5 vs ≤20 matching papers) and quality. Evaluation: BM25, GTR, Instructor-XL, E5, GritLM, plus GPT-4o vanilla and one-hop reranking over a 64,183-paper corpus.

## Result
GritLM-7B dominates (70.8 R@20 broad, 74.8 R@5 specific); instruction-finetuned dense models (Instructor, E5, GritLM) all beat BM25 and GTR. GPT-4o reranking lifts BM25 R@5 by 21.5% and GritLM by 5.5% on specific inline questions. Including full paper text (vs titles+abstracts) does **not** consistently improve retrieval — embedding models trained on short docs (avg 56–79 words) degrade on 6,041-word inputs. LitSearch better separates models than MSMARCO/SCIDOCS/NQ (e.g. 15-point nDCG@10 gap GritLM vs E5 on LitSearch-specific, near-zero on MSMARCO).

## Why it matters here
General background; no direct arena tie. Relevant only as methodology context for the wiki's own vector-search retrieval (qmd over `einstein-wiki`) — confirms that instruction-finetuned dense retrievers materially outperform BM25 on scientific-literature queries, and that title+abstract embedding can beat full-text for current models.

## Open questions / connections
- Does full-text retrieval beat title+abstract once embedding models support longer contexts natively (beyond GritLM's 2048-token cap)?
- Can one-hop reranking ("retrieve citing paper, then its citations") be gamed when source-paper-in-corpus assumption holds — and what's the right defense?
- Author-written queries skew toward abstract terminology (overlap 0.43 vs 0.33 inline) — does this annotator artifact recur in math/optimization wiki query collection?

## Key terms
LitSearch, dense retrieval, BM25, GritLM, E5, Instructor, GPT-4o reranking, citation recommendation, S2ORC, recall@k, instruction-finetuned embeddings, one-hop reranking
