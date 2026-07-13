<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-verification
domains: [ai-verification, ai-agents]
title: "Evaluating LLM-based Agents for Multi-Turn Conversations: A Survey"
authors: [Shengyue Guan, Haoyi Xiong, Jindong Wang, Jiang Bian, Bin Zhu, Jian-guang Lou]
year: 2025
source_url: https://arxiv.org/abs/2503.22458
drive_file_id: 1CBIorriaOKbZN4iuwl8oBEgYvPqvE5Ul
text_source: pdf
ingested_by: agent
---

# Evaluating LLM-based Agents for Multi-Turn Conversations: A Survey

**Authors:** Shengyue Guan, Haoyi Xiong, Jindong Wang, Jiang Bian, Bin Zhu, Jian-guang Lou (Microsoft)  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2503.22458

## One-line
A PRISMA-guided survey of ~250 scholarly sources on evaluating LLM-based multi-turn conversational agents, organized into two taxonomies — what to evaluate and how to evaluate it.

## Key claim
Multi-turn conversational agent evaluation requires jointly assessing four components (end-to-end experience, tool/action use, memory, planning) using a mix of annotation-based, automated-metric, and LLM-as-judge methodologies; traditional single-turn metrics (BLEU, ROUGE) are insufficient to capture dynamic, interactive multi-turn behavior.

## Method
Follows a PRISMA-inspired selection pipeline: identified 1,123 unique records (479 from Google Scholar keyword search + 1,081 from top venues ICLR/NeurIPS/AAAI/NAACL/EMNLP/ACL, 2022-2024) spanning 2017-2025; screened to 790, assessed 523 for eligibility, included 351 in qualitative synthesis (272 with targeted evaluation insights). Builds two interrelated taxonomies: (1) **What to evaluate** — end-to-end experience (task completion, multitask capability, interaction patterns, temporal dimensions, user experience/safety), action/tool-use components, memory (conversation memory vs. turn memory; memory spans and forms), and planning (task modeling, task decomposition, adaptation/control, reflection); (2) **How to evaluate** — evaluation data (conversation data generation vs. annotation) and evaluation metrics (annotation-based vs. annotation-free/automated, including LLM-as-judge hybrid strategies).

## Result
Corpus breakdown: 40% conference articles, 25% journal articles, 20% preprints, 15% industry reports. Notable examples surveyed include MT-Bench (8 categories: writing, roleplay, extraction, reasoning, math, coding, STEM, humanities) extended to a million-conversation dataset across 25 LLMs; a four-category interaction-pattern taxonomy (recollection, expansion, refinement, follow-up); a three-tier taxonomy (Perceptivity, Adaptability, Interactivity) analyzing 4,208 turns across 1,388 dialogues; Hendrycks et al.'s 57-task multitask benchmark; and the CoSafe dataset for coreference-based attack safety evaluation. Identifies open challenges: lack of scalable real-time evaluation pipelines, weak privacy-preserving mechanisms, and absence of robust metrics capturing dynamic multi-turn interaction quality.

## Key terms
LLM-based agents, multi-turn conversation, conversational AI evaluation, PRISMA survey, task completion, tool use, agent memory, agent planning, annotation-based evaluation, LLM-as-judge, MT-Bench, interaction patterns, evaluation metrics
