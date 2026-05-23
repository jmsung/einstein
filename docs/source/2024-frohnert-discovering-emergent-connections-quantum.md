---
type: source
kind: paper
title: Discovering emergent connections in quantum physics research via dynamic word embeddings
authors: Felix Frohnert, Xuemei Gu, Mario Krenn, Evert P L van Nieuwenburg
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2411.06577
source_local: ../raw/2024-frohnert-discovering-emergent-connections-quantum.pdf
topic: general-knowledge
cites:
---

# Discovering emergent connections in quantum physics research via dynamic word embeddings

**Authors:** Felix Frohnert, Xuemei Gu, Mario Krenn, Evert P L van Nieuwenburg  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2411.06577

## One-line
Trains a dynamic Word2Vec embedding on 66,839 arXiv quant-ph abstracts (1994–2023) and uses an MLP on the resulting concept vectors to predict which currently-unconnected research concepts will co-occur in future papers.

## Key claim
Unsupervised dynamic word embeddings outperform knowledge-graph link-prediction baselines on the concept co-occurrence task, achieving $\text{AUC} = 0.87$ vs $0.82$ (knowledge graph + handcrafted features), $0.79$ (static Word2Vec / ProNE) and $0.78$ (Node2Vec); filtering the lowest-confidence 20% of predictions pushes AUC above $0.9$.

## Method
Skip-gram Word2Vec ($n=128$, window $k=10$) is trained sequentially year-by-year on quant-ph abstracts, each year initialized from the prior year's weights, producing time-indexed vectors $w_{c,t} \in \mathbb{R}^n$ for each of 10,235 RAKE-extracted concept tokens. An MLP classifier with PReLU, batch norm, dropout and a sigmoid head is trained with binary cross-entropy on concatenated pair-embeddings to predict whether a not-yet-co-occurring pair will co-occur in a subsequent label window. Baselines (static Word2Vec, cosine-similarity features, knowledge-graph handcrafted features, Node2Vec, ProNE) use the same classifier architecture for fair comparison.

## Result
On the test split (train embeddings $\Delta t = [1994, 2017]$, label window $\Lambda t = [2018, 2020]$, test $\Lambda t = [2021, 2023]$), the dynamic word embedding reaches $\text{AUC} = 0.87$ — the best of six methods tested. Probabilities are well-calibrated near 0 and 1, less so near 0.5, so confidence-based filtering reliably surfaces a high-precision subset. UMAP + $k$-means on the embeddings produces semantically coherent clusters (quantum computing, stochastic noise, gravitational waves, etc.) and tracks topic emergence between 2012 and 2022.

## Why it matters here
General background; no direct arena tie — this is a science-of-science / NLP forecasting paper on quantum-physics literature, not an optimization or extremal-combinatorics result. The only transferable idea is methodological: time-indexed embeddings + co-occurrence link prediction could in principle be applied to the einstein wiki to surface cross-problem concept connections (e.g. when an LP-duality technique used on P1 is likely to apply to P15), but this is meta-tooling rather than math content for any of the 23 arena problems.

## Open questions / connections
- Could contextual LLM embeddings (BERT/LLaMA/GPT) beat dynamic Word2Vec on the same prediction task once concept-synonym averaging is handled?
- Would hierarchical synonym grouping (e.g. collapsing "active space" variants) raise the granularity-vs-coverage tradeoff and change which "first co-occurrence" events the model fires on?
- How well would a recurrent classifier exploiting *multiple* time slices (not just the final-year embedding) improve AUC, given empirical neutrality of multi-slice input in this study?

## Key terms
dynamic word embeddings, Word2Vec, Skip-gram, knowledge graph, link prediction, Node2Vec, ProNE, UMAP, k-means clustering, concept co-occurrence prediction, science of science, AUC ROC, quantum physics literature, science forecasting
