<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-reasoning, bio-clinical]
title: "MedAgents: Large Language Models as Collaborators for Zero-shot Medical Reasoning"
authors: [Xiangru Tang, Anni Zou, Zhuosheng Zhang, Yilun Zhao, Xingyao Zhang, Arman Cohan, Mark B. Gerstein]
year: 2023
source_url: https://arxiv.org/abs/2311.10537
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# MedAgents: Large Language Models as Collaborators for Zero-shot Medical Reasoning

**Authors:** Xiangru Tang, Anni Zou, Zhuosheng Zhang, Yilun Zhao, Xingyao Zhang, Arman Cohan, Mark B. Gerstein  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2311.10537

## One-line
A training-free multi-agent LLM framework that simulates a multi-disciplinary medical consultation — gather domain-expert personas, propose analyses, summarize, iterate to consensus, decide — to improve zero-shot medical QA.

## Key claim
On nine medical QA benchmarks (MedQA, MedMCQA, PubMedQA, six MMLU medical subtasks), zero-shot MedAgents with GPT-3.5 averages 72.1% (vs Zero-shot CoT 58.3%, Zero-shot CoT+SC 70.9%, Few-shot CoT+SC 71.6%); GPT-3.5 errors are 77% domain-knowledge gaps vs only 8% CoT-reasoning gaps, motivating role-play over plain CoT.

## Method
Five-stage pipeline: (1) Expert Gathering — LLM classifies the question and options into $m=5$ question-domain experts and $n=2$ option-domain experts; (2) Analysis Proposition — each expert persona produces question/option analyses; (3) Report Summarization — a "medical assistant" LLM extracts key knowledge + total analysis; (4) Collaborative Consultation — iterative yes/no vote with modification opinions, revising the report up to $t=5$ rounds until unanimous; (5) Decision Making — final answer derived from the consensus report. All zero-shot, temperature 1.0, GPT-3.5/GPT-4, no retrieval augmentation.

## Result
MedAgents beats zero-shot baselines by large margins and matches/exceeds 5-shot CoT+SC under zero-shot. GPT-3.5 average across nine datasets: 72.1 (MedAgents) vs 70.9 (Zero-shot CoT+SC) vs 71.6 (Few-shot CoT+SC). Ablation shows each stage (analysis, summarization, consultation) contributes non-trivially. Cost ≈ \$0.014/question, ~40s inference; 5-repetition variance is small (e.g. MedQA GPT-4: 83.7 vs 83.5 mean). Human eval identifies four error classes: missing domain knowledge (77%), mis-retrieval, consistency, CoT errors (8%).

## Key terms
multi-agent LLM, role-playing, council dispatch, medical question answering, MedQA, MedMCQA, PubMedQA, MMLU, chain-of-thought, self-consistency, zero-shot reasoning, collaborative consultation, expert gathering, consensus voting, hallucination
