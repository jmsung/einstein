<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-reasoning]
title: "Graph-of-Agents: A Graph-based Framework for Multi-Agent LLM Collaboration"
authors: [Sukwon Yun, Jie Peng, Pingzhi Li, Wendong Fan, Jie Chen, James Zou, Guohao Li, Tianlong Chen]
year: 2026
source_url: https://arxiv.org/abs/2604.17148
drive_file_id: 1wkuuVvxuINmUuLvs3oecMgUArj-3HFhU
text_source: paperclip
ingested_by: agent
---

# Graph-of-Agents: A Graph-based Framework for Multi-Agent LLM Collaboration

**Authors:** Sukwon Yun, Jie Peng, Pingzhi Li, Wendong Fan, Jie Chen, James Zou, Guohao Li, Tianlong Chen  ·  **Year:** 2026  ·  **Source:** https://arxiv.org/abs/2604.17148

## One-line
A test-time multi-LLM orchestration framework that selects a small subgraph of relevant specialist agents from a pool, routes directional messages between them by relevance, and pools the refined responses into one answer.

## Key claim
Using only $k=3$ selected agents (from a pool of 6 spanning General/Code/Math/Biomedical/Finance/Legal 7–8B LLMs), GoA outperforms Mixture-of-Agents and other multi-agent baselines that use all 6 agents on MMLU, MMLU-Pro, GPQA, MATH, HumanEval, MedMCQA — e.g. GoA$_{\text{Mean}}$ hits 73.12 on MATH and 40.54 on GPQA vs MoA 65.80/32.83, with $\sim$42% fewer LLM calls and $\sim$2.4× less latency on MMLU-Pro.

## Method
Four-stage graph pipeline operating purely via prompts (no fine-tuning): (1) **Node sampling** — a meta-LLM picks top-$k$ agents from model-card metadata (domain, task, size); (2) **Edge sampling** — each agent scores the others' initial responses (scores sum to 1), producing a relevance vector $S_j=\sum_{i\ne j}\text{Score}_{i\to j}$; agents below threshold $\tau=0.05$ are pruned, and a weighted directed adjacency $A_{ji}=S_i/\sum_{k\in N_j}S_k$ is built; (3) **Two-pass message passing** — Source→Target lets less-relevant agents refine using high-relevance responses, then Target→Source lets the strong agents incorporate the refined feedback; (4) **Graph pooling** — max (most-incoming-edges node) or mean (meta-LLM weighted aggregation).

## Result
GoA$_{\text{Max}}$ best on MMLU 79.18, MMLU-Pro 54.78, MedMCQA 60.04; GoA$_{\text{Mean}}$ best on GPQA 40.54, MATH 73.12, HumanEval 84.98. With GPT-4o, GoA (3 agents) beats DyLAN (8 agents) on HumanEval (93.29 vs 92.07) and matches on MedMCQA. Ablations: reversing message-passing direction is worst ($-2.60$ MMLU-Pro, $-5.05$ GPQA); removing Source→Target ($-2.57$) hurts more than removing Target→Source ($-1.12$); $\tau=0.05$ and $k=3$ are sweet spots. Proposition 1: GoA reduces to MoA when $k=N$, $A=\mathbf{1}$, with self-loops and mean pooling.

## Key terms
Graph-of-Agents, Mixture-of-Agents, multi-agent LLM, message passing, graph pooling, node sampling, edge sampling, directed adjacency, model cards, meta-LLM, test-time inference
