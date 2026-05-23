---
type: source
kind: paper
title: In-the-Flow Agentic System Optimization for Effective Planning and Tool Use
authors: Zhuofeng Li, Haoxiang Zhang, Seungju Han, Sheng Liu, Jianwen Xie, Yu Zhang, Yejin Choi, James Zou, Pan Lu
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2510.05592
source_local: ../raw/2025-li-in-the-flow-agentic-system-optimization.pdf
topic: general-knowledge
cites:
---

# In-the-Flow Agentic System Optimization for Effective Planning and Tool Use

**Authors:** Zhuofeng Li, Haoxiang Zhang, Seungju Han, Sheng Liu, Jianwen Xie, Yu Zhang, Yejin Choi, James Zou, Pan Lu  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2510.05592

## One-line
AgentFlow is a trainable four-module (planner/executor/verifier/generator) agentic system whose planner is optimized on-policy inside the live multi-turn loop via Flow-GRPO, a GRPO variant that broadcasts a single trajectory-level outcome reward to every turn.

## Key claim
With a 7B Qwen2.5-Instruct backbone and only the planner trained, AgentFlow beats specialized tool-integrated RL baselines and even GPT-4o (~200B) on ten benchmarks: +14.9% search, +14.0% agentic (GAIA), +14.5% math (incl. AIME24 6.7%→40.0%, GameOf24 31.0%→53.0%), +4.1% scientific (GPQA, MedQA).

## Method
Four modules share an explicit, deterministic evolving memory $M_t$ over a multi-turn MDP; only the planner $\pi_\theta$ is trainable. Flow-GRPO assigns a verifiable LLM-as-judge final-outcome reward $r \in \{0,1\}$ to every turn of a rollout, then applies GRPO-style group-normalized advantages $A_t^i = (\bar R_i - \mu)/\sigma$ with PPO clipping and KL penalty ($\beta=0.001$) to a frozen reference. This converts the long-horizon, sparse-reward credit-assignment problem into a sequence of single-turn token-level policy updates (proof of equivalence in appendix B).

## Result
The trained planner gains adaptive tool selection, query refinement, and self-correction; ablations show Flow-GRPO substantially outperforms SFT on the same data, produces shorter responses, and scales positively with backbone size and turn budget (training capped at 3 turns/rollout, batch 32, 8 rollouts/sample, lr $1\times10^{-6}$, temp 0.5). Qualitative examples document recovery from failed searches, strategic tool switching, and correct relativistic physics formulation where the untrained agent loops.

## Why it matters here
Directly relevant to einstein's autonomous-loop branch: AgentFlow's planner/executor/verifier/generator decomposition and Flow-GRPO's broadcast-outcome credit assignment map onto the council-dispatch + self-improvement-loop architecture, and offer a concrete recipe for *training* (not just prompting) the planner that selects techniques and tools across multi-turn math-solving rollouts. General background for arena problems; no direct math-bound connection.

## Open questions / connections
- Could Flow-GRPO's single-broadcast-reward equivalence be extended to *per-problem* triple-verify scores rather than binary judge labels, enabling dense reward shaping for arena cycles?
- The evolving-memory $M_t$ as "explicit deterministic record" parallels the wiki/findings layer — does training the planner on wiki-context state generalize across problems?
- Extends GRPO (Shao et al. 2024) and tool-integrated RL (Search-R1, ReSearch, ToRL, Verl-Tool) by replacing monolithic policy with modular trainable agent; leaves open how to train *multiple* modules jointly without instability.

## Key terms
Flow-GRPO, AgentFlow, GRPO, group-relative policy optimization, tool-integrated reasoning, agentic systems, multi-turn RL, credit assignment, sparse reward, on-policy, planner-executor-verifier, LLM-as-judge, GAIA, AIME24, Qwen2.5
