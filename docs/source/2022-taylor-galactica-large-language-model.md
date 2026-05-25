---
type: source
kind: paper
title: "Galactica: A Large Language Model for Science"
authors: Ross Taylor, Marcin Kardas, Guillem Cucurull, Thomas Scialom, A. Hartshorn, Elvis Saravia, Andrew Poulton, Viktor Kerkez, Robert Stojnic
year: 2022
author: agent
drafted: 2026-05-24
ingested_at: 2026-05-24
source_type: arxiv
source_url: https://arxiv.org/abs/2211.09085
source_local: ../raw/2022-taylor-galactica-large-language-model.pdf
topic: general-knowledge
cites:
---

# Galactica: A Large Language Model for Science

**Authors:** Ross Taylor, Marcin Kardas, Guillem Cucurull, Thomas Scialom, A. Hartshorn, Elvis Saravia, Andrew Poulton, Viktor Kerkez, Robert Stojnic  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2211.09085

## One-line
A large language model trained on a curated 106B-token scientific corpus (papers, code, reference material, SMILES, protein/DNA sequences, LaTeX) with task-specific tokens for citations, reasoning, and modalities.

## Key claim
On a curated scientific corpus with specialized tokenization, an LLM can outperform much larger general models on scientific reasoning and knowledge tasks: $68.2\%$ vs GPT-3's $49.0\%$ on LaTeX equations, $41.3\%$ vs Chinchilla's $35.7\%$ on math MMLU, and $20.4\%$ vs PaLM 540B's $8.8\%$ on MATH — with the 30B variant beating PaLM 540B at $18\times$ fewer parameters.

## Method
Pre-train a decoder-only Transformer (up to 120B params) on 106B curated tokens, blending text, LaTeX, code, SMILES, amino acids, and DNA in a common markdown format. Introduce a `<work>` working-memory token wrapping step-by-step reasoning (with optional Python offload) and `[START_REF]`/`[END_REF]` citation tokens to model the citation graph; mathematics is character-split (digits, parens, operators as individual tokens). Prompts from many task datasets (QA, entity extraction, summarization, chemical property prediction) are mixed directly into pre-training rather than added via fine-tuning, and the model is trained on repeated tokens for multiple epochs without overfitting.

## Result
Galactica 120B sets new SOTA on PubMedQA ($77.6\%$) and MedMCQA dev ($52.9\%$), outperforms BLOOM and OPT-175B on BIG-bench despite no general-corpus training, and beats tuned sparse/dense retrievers on citation prediction (with the empirical citation distribution approaching the reference as scale grows). The `<work>` token outperforms PaLM-540B chain-of-thought on MMLU dev ($42.4\%$ vs $19.1\%$), and chemical/docking property prediction RMSE decreases with scale on 3/5 docking targets — though performance plateaus on harder targets (ESR2, PGR), hinting at limits of text-only molecular representation.

## Why it matters here
General background; no direct arena tie. Relevant only as methodology context for the JSAgent's own wiki+agent loop: curated-corpus + repeated-token training, prompt-in-pretraining, and the `<work>`-style externalized reasoning token are design analogues for how a math-research agent might structure its own memory, scratchpad, and citation tooling.

## Open questions / connections
- Can curated-corpus + repeated-token training (vs Chinchilla's fresh-token assumption) generalize to small specialist agents over a math wiki?
- Does `<work>`-style internal-memory tokenization with Python offload outperform chain-of-thought for arithmetic-heavy optimization reasoning (relevant to mpmath polish narratives)?
- Citation-graph modeling via special tokens suggests a route for an agent to learn cite hygiene from its own wiki — open: does it hallucinate less than retrieval at small scale?
- Text-only modality fails on geometry-heavy docking; parallel limitation for sphere-packing / kissing-number where coordinates carry the signal.

## Key terms
large language model, scientific corpus, prompt pre-training, working memory token, chain-of-thought, citation prediction, SMILES, protein sequence, MMLU, MATH benchmark, Chinchilla scaling laws, repeated tokens
