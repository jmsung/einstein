---
type: source
kind: paper
title: "MatSci-NLP: Evaluating Scientific Language Models on Materials Science Language Tasks Using Text-to-Schema Modeling"
authors: Yurun Song, Santiago Miret, Bang Liu
year: 2023
author: agent
drafted: 2026-05-24
ingested_at: 2026-05-24
source_type: arxiv
source_url: https://arxiv.org/abs/2305.08264
source_local: ../raw/2023-song-matsci-nlp-evaluating-scientific-language.pdf
topic: general-knowledge
cites:
---

# MatSci-NLP: Evaluating Scientific Language Models on Materials Science Language Tasks Using Text-to-Schema Modeling

**Authors:** Yurun Song, Santiago Miret, Bang Liu  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2305.08264

## One-line
Introduces a 7-task NLP benchmark for materials science text and a unified text-to-schema fine-tuning method that outperforms single-task and standard multitask baselines on BERT-family encoders.

## Key claim
Domain-specific pretraining (MatBERT on materials science journals) plus a question-answering-style "Task-Schema" input format consistently beats single-task fine-tuning, multitask MMOE, and seq2seq baselines in the low-resource (1% train / 99% test) regime; MatBERT + Task-Schema achieves the best aggregate micro-F1 across the 7 tasks.

## Method
Curates 7 NLP tasks (NER, relation classification, event argument extraction, paragraph classification, synthesis action retrieval, sentence classification, slot filling) from publicly available materials science corpora into a unified JSON schema. Proposes an encoder-decoder architecture pairing a swappable domain-specific BERT encoder with a generic transformer decoder; the "Task-Schema" prompt format wraps each example as (text, description, instruction options, predefined answer schema) and applies constrained decoding that filters outputs to the valid label set, recasting generation as classification with cross-entropy loss. Fine-tunes 7 BERT variants (BERT, BioBERT, ScholarBERT, SciBERT, BatteryBERT, MatSciBERT, MatBERT) on a 1%-train split and evaluates with micro/macro-F1.

## Result
With Task-Schema, MatBERT reaches micro-F1 ≈ 0.875 on NER, 0.804 on relation classification, 0.756 on event argument extraction, 0.717 on paragraph classification, 0.909 on synthesis action retrieval, 0.548 on sentence classification, 0.722 on slot filling. SciBERT is second-best overall; MatSciBERT and BatteryBERT trail despite materials-specific pretraining; ScholarBERT (largest, general-science) and vanilla BERT consistently rank worst — showing pretraining-corpus *quality* dominates *size*. Task-Schema and other QA-inspired schemas (Potential Choices, Examples) beat Single-Task and MMOE baselines across nearly every (model × task) cell.

## Why it matters here
General background; no direct arena tie. The benchmark and methodology are NLP-for-materials, not optimization for sphere packing / autocorrelation / kissing numbers — there is no mathematical bound, theorem, or technique here relevant to the Einstein Arena problem set. Of marginal interest only as evidence that domain-curated pretraining + structured-output prompting helps in low-resource regimes, a meta-observation that could inform how an agent uses LLMs for scientific text extraction but not for solving math problems.

## Open questions / connections
- Whether constrained-decoding / schema-structured outputs help LLMs on math-reasoning tasks (the paper only tests classification-style NLP tasks).
- Extension to autoregressive / instruction-tuned LLMs (paper studies BERT-only encoders).
- Whether the "corpus quality > corpus size" finding (SciBERT > ScholarBERT) generalizes to math/optimization corpora.

## Key terms
MatSci-NLP, MatBERT, SciBERT, BERT, text-to-schema, multitask learning, named entity recognition, relation classification, synthesis action retrieval, low-resource fine-tuning, domain-specific pretraining, materials science NLP
