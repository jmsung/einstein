---
type: source
kind: paper
title: AFlow: Automating Agentic Workflow Generation
authors: Jiayi Zhang, Jinyu Xiang, Zhaoyang Yu, Fengwei Teng, Xiong-hui Chen, Jiaqi Chen, Mingchen Zhuge, Xin Cheng, Sirui Hong, Jinlin Wang, Bingnan Zheng, Bangbang Liu, Yuyu Luo, Chenglin Wu
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2410.10762
source_local: ../raw/2024-zhang-aflow-automating-agentic-workflow.pdf
topic: general-knowledge
cites:
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

## Why it matters here
General background; no direct arena tie. Relevant only as meta-methodology: the math-solving protocol in this repo is itself a hand-built agentic workflow, and AFlow's "operators + MCTS over code-graphs + tree-structured failure memory" maps directly onto the self-improvement loop (council dispatch, gap-detect, failure-finding). It suggests that the council/operator choice and ordering could in principle be search-optimized rather than hand-fixed.

## Open questions / connections
- Could AFlow-style MCTS be applied over the council-dispatch + technique-library to auto-tune which personas + operators to invoke per problem category?
- AFlow requires a numerical evaluator; on math problems we have triple-verified scores, so the loop closes — but operator search would need a budget model since each rollout is expensive.
- Extends ADAS (Hu et al. 2024) (linear heuristic code-search) and GPTSwarm (Zhuge et al. 2024) (RL over graph workflows) by combining code-expressivity with MCTS; leaves open whether discovered workflows transfer across task families.

## Key terms
agentic workflow, Monte Carlo Tree Search, MCTS, automated workflow optimization, code-represented graph, LLM-invoking node, operator, Self-Consistency Ensemble, Review and Revise, execution feedback, tree-structured experience, ADAS, GPTSwarm, Pareto cost-performance
