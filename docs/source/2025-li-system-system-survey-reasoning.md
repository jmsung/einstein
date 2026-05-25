---
type: source
kind: paper
title: From System 1 to System 2: A Survey of Reasoning Large Language Models
authors: Zhong-Zhi Li, Duzhen Zhang, Ming-Liang Zhang, Jiaxin Zhang, Zengyan Liu, Yuxuan Yao, Haotian Xu, Junhao Zheng, Pei-Jie Wang, Xiuyi Chen, Yingying Zhang, Fei Yin, Jiahua Dong, Zhijiang Guo, Le Song, Cheng-Lin Liu
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2502.17419
source_local: ../raw/2025-li-system-system-survey-reasoning.pdf
topic: general-knowledge
cites:
---

# From System 1 to System 2: A Survey of Reasoning Large Language Models

**Authors:** Zhong-Zhi Li, Duzhen Zhang, Ming-Liang Zhang, Jiaxin Zhang, Zengyan Liu, Yuxuan Yao, Haotian Xu, Junhao Zheng, Pei-Jie Wang, Xiuyi Chen, Yingying Zhang, Fei Yin, Jiahua Dong, Zhijiang Guo, Le Song, Cheng-Lin Liu  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2502.17419

## One-line
A comprehensive survey of "reasoning LLMs" (o1/o3, DeepSeek-R1, etc.) framed as the System 1 → System 2 cognitive transition, cataloging the methods, benchmarks, and infrastructure for slow, deliberate, multi-step LLM reasoning.

## Key claim
Reasoning LLMs are best understood as foundational LLMs augmented along five orthogonal axes — Structure Search, Reward Modeling, Self Improvement, Macro Action, and Reinforcement Fine-Tuning — and these methods, not scale alone, are what produce System-2-like deliberation (long CoT, verification micro-actions like "Wait/Alternatively", self-correction, exploratory branching) on math and coding benchmarks.

## Method
Taxonomic literature review. The authors trace three pre-LLM enablers (symbolic logic, MCTS with UCB1 selection $\text{UCB1} = w_i/n_i + c\sqrt{\ln N / n_i}$, and RL from Q-learning through AlphaGo/AlphaZero/AlphaStar) and map each onto a modern reasoning-LLM component (Macro Action, Structure Search, Reward Modeling / Reinforcement Fine-Tuning respectively). Output behavior (exploration, verification, longer inference, overthinking) is separated from training dynamics (RLHF variants — PPO/DPO/GRPO — long-CoT distillation, self-play).

## Result
No new bound or theorem; an organizational synthesis. Establishes a 5-axis blueprint for constructing reasoning LLMs, surveys representative systems (o1/o3, R1, Marco-o1, Huatuo-o1, QwQ, Quiet-STaR, Search-o1, LIMO, s1, Seed-Thinking-v1.5), reasoning benchmarks (text + multimodal), and extension areas: large-scale RL infrastructure (verl, OpenRLHF, Megatron, vLLM, SGLang), safety (overthink/jailbreak/H-CoT attacks; GuardReasoner, ThinkGuard), agentic use (Search-R1, ReSearch, Agent-R1, OpenManus), and efficient reasoning (Chain-of-Draft, token-budget control, latent/continuous CoT, diffusion-based reasoning).

## Why it matters here
General background; no direct arena tie. Useful as a map of the *agent-architecture* literature underlying the autonomous-loop branch (council dispatch, self-improvement loop, macro actions, RL fine-tuning) — not for math content on sphere packing, kissing numbers, or LP/SDP bounds.

## Open questions / connections
- Overthinking trap on simple problems — relevant to council-dispatch budgeting and the "ask the question first" rule.
- Process reward modeling (step-level supervision) as the closest analog to triple-verify discipline at the reasoning-trajectory level.
- Search-augmented reasoning (Search-o1, Search-R1, R1-Searcher) as a template for wiki-first-lookup-style retrieval integration into the agent loop.

## Key terms
reasoning LLMs, System 1 / System 2, chain-of-thought, MCTS, UCB1, reinforcement learning, PPO, DPO, GRPO, process reward model, self-improvement, macro action, long-CoT, o1, DeepSeek-R1, agentic reasoning
