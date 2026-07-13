<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-reasoning]
title: Training-Free Group Relative Policy Optimization
authors: [Yuzheng Cai, Siqi Cai, Yuchen Shi, Zihan Xu, Lichao Chen, Yulei Qin, Xiaoyu Tan, Gang Li, Zongyi Li, Haojia Lin, Yong Mao, Ke Li, Xing Sun]
year: 2025
source_url: https://arxiv.org/abs/2510.08191
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Training-Free Group Relative Policy Optimization

**Authors:** Yuzheng Cai, Siqi Cai, Yuchen Shi, Zihan Xu, Lichao Chen, Yulei Qin, Xiaoyu Tan, Gang Li, Zongyi Li, Haojia Lin, Yong Mao, Ke Li, Xing Sun  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2510.08191

## One-line
Replaces gradient-based GRPO fine-tuning with an inference-only loop that distills a natural-language "experience library" from group rollouts, steering a frozen LLM via context instead of parameters.

## Key claim
On AIME24/AIME25, applying Training-Free GRPO to frozen DeepSeek-V3.1-Terminus with only 100 out-of-domain training samples and ≈\$18 of API cost lifts Mean@32 from 80.0→82.7% (AIME24) and 67.9→73.3% (AIME25) with ReAct+code-interpreter, surpassing RL-fine-tuned 32B models (ReTool, AFM) that cost ≈\$10k.

## Method
Mirrors vanilla GRPO's rollout/reward loop but replaces the numerical group advantage $\hat A_i=(r_i-\text{mean}(r))/\text{std}(r)$ with a *semantic* group advantage: for each group of $G$ rollouts the LLM summarizes each trajectory, contrasts winners vs losers vs ground truth, and emits a natural-language "experience" $A_\text{text}$. A second prompt then proposes Add/Delete/Modify/Keep operations against a persistent experience library $E$, and subsequent rollouts condition on $\pi_\theta(o\mid q, E)$ — the frozen prior plays the role of the KL-anchor to $\pi_\text{ref}$.

## Result
Three epochs × one batch on 100 DAPO problems (group size 5, temp 0.7) yields +2.7% / +5.4% on AIME24/25 and reduces average tool calls (agent learns to skip redundant CI calls). Ablations show: directly LLM-generated experiences without group comparison do not help (79.8/67.3%); removing ground truth still gains (80.7/68.9%); group size 1 (no comparison) significantly degrades. On WebWalkerQA: 63.2→67.8% pass@1 with the same recipe. Cross-domain transfer (Table 6) shows parameter-tuned specialists collapse off-domain (ReTool 67% AIME → 18.3% Web), while Training-Free GRPO matches both by swapping $E$.

## Key terms
GRPO, training-free RL, semantic advantage, in-context reinforcement learning, experience library, ReAct, tool-integrated reasoning, AIME, DeepSeek-V3.1, self-refine, Reflexion, agentic RL, token prior, group rollouts, frozen policy
