---
type: source
kind: paper
title: AOrchestra: Automating Sub-Agent Creation for Agentic Orchestration
authors: Jianhao Ruan, Zhihao Xu, Yiran Peng, Fashen Ren, Zhaoyang Yu, Xinbing Liang, Jinyu Xiang, Bang Liu, Chenglin Wu, Yuyu Luo, Jiayi Zhang
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2602.03786
source_local: ../raw/2026-ruan-aorchestra-automating-sub-agent-creation.pdf
topic: general-knowledge
cites: 
---

# AOrchestra: Automating Sub-Agent Creation for Agentic Orchestration

**Authors:** Jianhao Ruan, Zhihao Xu, Yiran Peng, Fashen Ren, Zhaoyang Yu, Xinbing Liang, Jinyu Xiang, Bang Liu, Chenglin Wu, Yuyu Luo, Jiayi Zhang  ·  **Year:** 2026  ·  **Source:** https://arxiv.org/abs/2602.03786

## One-line
An orchestrator-centric agentic framework that spawns specialized sub-agents on the fly by instantiating a unified 4-tuple $\langle \text{Instruction}, \text{Context}, \text{Tools}, \text{Model}\rangle$ for each subtask.

## Key claim
Treating sub-agents as dynamically composed 4-tuples (rather than context-isolated threads or static predefined roles) yields a 16.28% relative improvement over the strongest baseline (Claude Code, OpenHands, Mini-SWE, ReAct) on GAIA / Terminal-Bench 2.0 / SWE-Bench-Verified when paired with Gemini-3-Flash, and the orchestration policy is learnable (SFT: +11.51% pass@1 on GAIA; in-context cost-aware routing: +3.03% pass@1 with −18.5% cost).

## Method
A central orchestrator restricted to two actions, $\mathcal{A} = \{\text{Delegate}(\Phi), \text{Finish}(y)\}$, with $\Phi = (I, C, T, M)$ separating working memory $(I,C)$ from capabilities $(T,M)$; it never touches the environment directly. Learning has two prongs: (1) SFT (behavior cloning on 2K Gemini-3-Flash orchestration trajectories from TaskCraft, full-finetune Qwen3-8B) for subtask decomposition and 4-tuple synthesis; (2) iterative in-context optimization of the orchestrator's prompt $I_{\text{main}}$ using a Claude-Sonnet-4.5 optimizer over trajectories scored on $\mathbb{E}[\mathbb{1}\{\text{Success}\} - \lambda \cdot \text{Cost}(\tau)]$.

## Result
With Gemini-3-Flash: GAIA pass@1 = 80.0% (vs Claude Code 49.09%), Terminal-Bench 2.0 = 52.86% (vs 28.57%), SWE-Bench-Verified = 82.0% (vs 64.0%); average pass@1 across the three benchmarks = 71.62% vs the best baseline OpenHands at 49.49%. GAIA stratifies by difficulty: L1 88.7%, L2 80.2%, L3 61.5%; 34 tasks solved after >5 orchestrator attempts (strong error recovery / replanning).

## Why it matters here
General background on agentic system design; no direct arena (sphere-packing / autocorrelation / extremal-combinatorics) tie. The 4-tuple $(I,C,T,M)$ abstraction and the Delegate/Finish action space are directly relevant to designing the einstein autonomous-loop agent's council dispatch and self-improvement loop — specifically, the separation of "working memory" from "capabilities" maps cleanly onto how council personas should be instantiated with task-specific context + tool subsets, and the cost-aware in-context optimization is a candidate pattern for trading off model tier vs. compute spend on per-problem subtasks.

## Open questions / connections
- Can the 4-tuple $\Phi$ abstraction subsume the einstein council-dispatch pattern (persona = preset $(I, T)$, problem = $C$, tier = $M$)?
- Iterative prompt optimization over $(\text{Perf}, \text{Cost})$ suggests a Pareto-frontier analog for compute-router decisions (local CPU / MPS / Modal) — is the trajectory→optimizer→strategy loop reusable for routing math workloads?
- Paper does not test on math-reasoning benchmarks (AIME / MATH / Putnam); transfer of orchestration gains to formal-math / optimization problems is open.

## Key terms
agentic orchestration, sub-agent-as-tools, 4-tuple abstraction, dynamic sub-agent creation, context isolation, model routing, cost-aware orchestration, supervised fine-tuning, in-context learning, Pareto frontier, GAIA, SWE-Bench, Terminal-Bench, ReAct, Claude Code, behavior cloning
