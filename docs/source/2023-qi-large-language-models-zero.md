---
type: source
kind: paper
title: Large Language Models are Zero Shot Hypothesis Proposers
authors: Biqing Qi, Kaiyan Zhang, Haoxiang Li, Kai Tian, Sihang Zeng, Zhangren Chen, Bowen Zhou
year: 2023
author: agent
drafted: 2026-05-24
ingested_at: 2026-05-24
source_type: arxiv
source_url: https://arxiv.org/abs/2311.05965
source_local: ../raw/2023-qi-large-language-models-zero.pdf
topic: general-knowledge
cites:
---

# Large Language Models are Zero Shot Hypothesis Proposers

**Authors:** Biqing Qi, Kaiyan Zhang, Haoxiang Li, Kai Tian, Sihang Zeng, Zhangren Chen, Bowen Zhou  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2311.05965

## One-line
Empirically tests whether instructed LLMs can propose novel, validatable scientific hypotheses zero-shot, using a biomedical literature dataset partitioned by publication date.

## Key claim
LLMs generate untrained-yet-validated hypotheses on a temporally-held-out test set (literature from August 2023), and *increasing* uncertainty (zero-shot, multi-agent collaboration) yields higher novelty than reducing uncertainty via few-shot retrieval or domain fine-tuning — captured by the slogan "when nothing is sure, everything is possible."

## Method
Construct background↔hypothesis pairs from PubMed (10k papers, 2500 train + 200 seen-test before Jan 2023; 200 unseen-test from Aug 2023) via Self-Instruct-style filtering. Evaluate ChatGPT, Vicuna-33B, Llama-2-70B-chat, WizardLM-13B/70B, Openchat, PMC-LLaMA, MedAlpaca under zero-shot, 5-shot (random + similarity-retrieved), and SFT. A four-agent framework (Analyst → Engineer → Scientist → Critic) iterates to refine hypotheses; scoring uses BLEU/ROUGE plus four ChatGPT-as-judge metrics (novelty, relevance, significance, verifiability, 0–3 scale) cross-checked against human raters.

## Result
On the unseen set, zero-shot beats 5-shot for the largest models (Llama-2-70B-chat zero-shot Avg 2.04; few-shot retrieves higher BLEU/ROUGE but *lowers* novelty from 1.86→1.43). SFT-WizardLM-13B reaches BLEU 19.7 / ROUGE 27.6, beating gpt-3.5-turbo on overlap but with novelty only 0.97. Domain-adapted PMC-LLaMA scores high on word overlap (BLEU 22.9) yet low on ChatGPT-judged quality (Avg 1.41), exposing a word-overlap vs. semantic-quality gap. ChatGPT scores correlate strongly with human ratings.

## Why it matters here
General background; no direct arena tie. The closest analogue is the einstein agent's council-dispatch / self-improvement-loop architecture — this paper validates the "personas write questions, critic refines" pattern and supplies an evaluation rubric (novelty/relevance/significance/verifiability) that could be adapted to score persona-generated questions in `docs/wiki/questions/`.

## Open questions / connections
- Does the "uncertainty helps novelty" finding transfer to math-hypothesis generation (where verifiability is mechanical, not literature-anchored)?
- Can the four-metric rubric replace human review for gating agent-authored `findings/` and `concepts/` promotions?
- The Analyst/Engineer/Scientist/Critic loop mirrors einstein's council dispatch — is the iterative-critic step the missing ingredient that turns persona output from "plausible markdown" into testable questions?
- How does similarity-retrieval-of-few-shot-examples (which boosted BLEU but suppressed novelty) interact with wiki-first lookup — does over-anchoring on prior findings reduce the agent's hypothesis space?

## Key terms
large language models, zero-shot hypothesis generation, multi-agent collaboration, scientist-critic loop, self-instruct, instruction tuning, novelty-relevance-significance-verifiability metrics, ChatGPT-as-judge, biomedical literature, temporal data split, uncertainty and novelty, domain adaptation
