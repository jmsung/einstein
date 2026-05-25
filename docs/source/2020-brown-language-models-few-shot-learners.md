---
type: source
kind: paper
title: Language Models are Few-Shot Learners
authors: Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, J. Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, G. Sastry, Amanda Askell, S. Agarwal, Ariel Herbert-Voss, Gretchen Krueger, T. Henighan, R. Child, A. Ramesh, Daniel M. Ziegler, Jeff Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Ma-teusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, I. Sutskever, Dario Amodei
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2005.14165
source_local: ../raw/2020-brown-language-models-few-shot-learners.pdf
topic: general-knowledge
cites:
---

# Language Models are Few-Shot Learners

**Authors:** Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, J. Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, G. Sastry, Amanda Askell, S. Agarwal, Ariel Herbert-Voss, Gretchen Krueger, T. Henighan, R. Child, A. Ramesh, Daniel M. Ziegler, Jeff Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Ma-teusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, I. Sutskever, Dario Amodei  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2005.14165

## One-line
Introduces GPT-3, a 175B-parameter autoregressive transformer, and shows that scaling alone enables strong few-shot, one-shot, and zero-shot task performance via in-context learning without any gradient updates.

## Key claim
At sufficient scale (175B params), a single autoregressive LM performs many NLP tasks competitively with fine-tuned SOTA purely via in-context conditioning on a natural-language description plus $K \approx 10$–$100$ demonstrations — e.g. 71.2% on TriviaQA (few-shot, SOTA among closed-book) and 85.0 F1 on CoQA.

## Method
Train 8 dense transformer LMs ($n_{\text{params}}$ from 125M to 175B, $n_{\text{ctx}} = 2048$, alternating dense/locally-banded sparse attention) on ~300B tokens of filtered Common Crawl + WebText2 + Books1/2 + Wikipedia, with quality-weighted sampling and document-level fuzzy deduplication. Evaluate each model in zero-/one-/few-shot regimes by prepending a task description and $K$ input→output exemplars to the prompt; the model completes the final input — no weight updates.

## Result
Few-shot performance scales smoothly with $\log(\text{params})$ and the gap between zero-/one-/few-shot widens with scale, suggesting larger models are better in-context meta-learners. GPT-3 reaches near-SOTA on translation, QA, cloze, and Winograd-style tasks, but underperforms on ANLI, RACE, QuAC and on synthetic tasks like multi-digit arithmetic past 3 digits. Authors also report a systematic train/test contamination audit and degraded fairness/bias metrics.

## Why it matters here
General background; no direct arena tie. Relevant only as backdrop for using LLM agents (this repo's JSAgent) to solve math optimization — the in-context-learning paradigm motivates why a council-of-personas dispatch with carefully chosen demonstrations could shape agent behavior without fine-tuning.

## Open questions / connections
- Does in-context learning genuinely acquire new skills or only retrieve pre-trained patterns? (Authors flag this as unresolved.)
- Power-law scaling of validation loss [KMH+20] — at what scale do specific reasoning tasks (arithmetic, NLI) saturate or break?
- Bidirectional / denoising objectives (BERT, T5) vs autoregressive — which is better for the few-shot regime at scale?

## Key terms
GPT-3, few-shot learning, in-context learning, meta-learning, autoregressive language model, transformer, scaling laws, zero-shot, sparse attention, Common Crawl, prompt conditioning, Kaplan scaling
