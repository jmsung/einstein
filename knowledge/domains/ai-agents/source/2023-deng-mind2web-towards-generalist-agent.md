<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "Mind2Web: Towards a Generalist Agent for the Web"
authors: [Xiang Deng, Yu Gu, Boyuan Zheng, Shijie Chen, Samuel Stevens, Boshi Wang, Huan Sun, Yu Su]
year: 2023
source_url: https://arxiv.org/abs/2306.06070
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Mind2Web: Towards a Generalist Agent for the Web

**Authors:** Xiang Deng, Yu Gu, Boyuan Zheng, Shijie Chen, Samuel Stevens, Boshi Wang, Huan Sun, Yu Su  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2306.06070

## One-line
Introduces a benchmark dataset and two-stage LLM pipeline for building generalist web-browsing agents that follow natural-language instructions on arbitrary real-world websites.

## Key claim
A two-stage MindAct pipeline — a fine-tuned small LM (DeBERTa-v3-base) for HTML element candidate ranking followed by an LLM (Flan-T5 / GPT-3.5 / GPT-4) for multi-choice action prediction — substantially outperforms direct classification or generation baselines, reaching ~52% element accuracy and ~52% step success rate on cross-task evaluation with Flan-T5XL (vs. ~20% and ~17% for the generation baseline), while still achieving only ~5% full-task success, leaving large room for improvement.

## Method
Two-stage architecture: (1) a small cross-encoder LM scores each DOM element against the (task, prior-actions) query via binary cross-entropy on positive target / random-negative pairs, retrieving top-$k$ candidates; (2) candidates are batched into 5-way multi-choice questions with a "None of the above" option and fed to a Seq2Seq LLM that selects the element and emits the operation (Click / Type / Select), iteratively re-grouping survivors until one element remains. Dataset built by crowdsourcing 2,350 high-level tasks across 137 real websites in 31 domains via a Playwright annotation tool with element-then-operation two-step capture, then author-verified.

## Result
On three out-of-distribution splits (Cross-Task / Cross-Website / Cross-Domain), MindAct + Flan-T5XL achieves element accuracy 55.1 / 42.0 / 42.1, operation F1 ~66–76, step success ~52 / 39 / 40, and full-task success 5.2 / 5.1 / 2.9 percent. GPT-4 (3-shot, 50-task subset, top-10 candidates) underperforms fine-tuned Flan-T5XL (step SR 36.2 / 30.1 / 26.4). Candidate generation with DeBERTa-v3-base achieves ~88% recall@50 while shrinking ~580-element pages to a tractable LLM input. The discrimination-as-multichoice formulation beats direct generation by ~2–3× on element accuracy.

## Key terms
web agent, generalist agent, large language model, LLM, HTML grounding, DOM element ranking, cross-encoder, multi-choice question answering, Flan-T5, GPT-4, in-context learning, Mind2Web benchmark
