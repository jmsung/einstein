<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-reasoning]
title: "AFlow: Automating Agentic Workflow Generation"
authors: [Jiayi Zhang, Jinyu Xiang, Zhaoyang Yu, Fengwei Teng, Xiong-hui Chen, Jiaqi Chen, Mingchen Zhuge, Xin Cheng, Sirui Hong, Jinlin Wang, Bingnan Zheng, Bangbang Liu, Yuyu Luo, Chenglin Wu]
year: 2024
source_url: https://arxiv.org/abs/2410.10762
drive_file_id: 1Bdpll01AyjerlcpYQWrJYe5vt4f5ziZA
text_source: paperclip
ingested_by: agent
---

# AFlow: Automating Agentic Workflow Generation

**Authors:** Jiayi Zhang, Jinyu Xiang, Zhaoyang Yu, Fengwei Teng, Xiong-hui Chen, Jiaqi Chen, Mingchen Zhuge, Xin Cheng, Sirui Hong, Jinlin Wang, Bingnan Zheng, Bangbang Liu, Yuyu Luo, Chenglin Wu  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2410.10762

## One-line
AFlow uses Monte Carlo Tree Search to automatically discover and optimize code-represented LLM agent workflows, replacing manual prompt-chain design.

## Key claim
Treating workflow design as a search problem over code graphs of LLM-invoking nodes connected by edges (with reusable "operators" like Ensemble, Review & Revise), AFlow + MCTS discovers workflows that beat the strongest manual baseline by 5.7% on average across six benchmarks and beat prior automated workflow methods (e.g., ADAS) by 19.5%. With AFlow-discovered workflows, GPT-4o-mini matches GPT-4o IO at 4.55% of its dollar cost on HumanEval.

## Method
Workflows are formalized as graphs of nodes $N_i = (M, P, \tau, F)$ — model, prompt, temperature, output format — connected by code-expressed edges encoding loops, branches, and conditionals. AFlow searches this space with MCTS using four operations: soft mixed-probability selection biased by node score and visit count, LLM-driven expansion that proposes a code modification, execution-based evaluation on a validation set, and backpropagation of success/failure traces into a tree-structured experience that the LLM expander conditions on. Predefined operators (Self-Consistency Ensemble, Review&Revise, Programmer, MultiAgent Debate, etc.) serve as macro-nodes to compress the search.

## Result
On six benchmarks — HumanEval, MBPP, MATH, GSM8K, HotpotQA, DROP — AFlow is the top method in all six, e.g. HumanEval 94.7% (vs 89.3% best manual), MATH 50.0% pass-rate where the next-best manual is 46.1%. Pareto cost-performance tables show GPT-4o-mini + AFlow > GPT-4o IO on HumanEval at $0.05 vs $0.64. Ablations isolate three contributing mechanisms: operators (raise per-iteration improvement probability), tree experience (avoid revisiting failed branches), and execution feedback (guide modifications via run-time logs).

## Key terms
agentic workflow, Monte Carlo Tree Search, MCTS, automated workflow optimization, code-represented graph, LLM-invoking node, operator, Self-Consistency Ensemble, Review and Revise, execution feedback, tree-structured experience, ADAS, GPTSwarm, Pareto cost-performance
