---
type: source
kind: paper
title: Training-Free Group Relative Policy Optimization
authors: Yuzheng Cai, Siqi Cai, Yuchen Shi, Zihan Xu, Lichao Chen, Yulei Qin, Xiaoyu Tan, Gang Li, Zongyi Li, Haojia Lin, Yong Mao, Ke Li, Xing Sun
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2510.08191
source_local: ../raw/2025-cai-training-free-group-relative-policy.pdf
topic: general-knowledge
cites:
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

## Why it matters here
Directly relevant to the self-improvement-loop and council-dispatch rules — the paper formalizes "learned experiential knowledge as token prior" with an explicit ops grammar (Add/Delete/Modify/Keep), which is essentially what `docs/wiki/findings/` + experience selection does manually here. Suggests a concrete mechanism to operationalize the autonomous-loop branch: each cycle's failure/success findings become an indexed experience library that conditions the next council dispatch, with semantic advantage replacing the missing scalar reward signal on hard problems.

## Open questions / connections
- Does semantic-advantage distillation work when there is *no* ground truth (their no-GT variant kept gains) — directly applicable to Einstein Arena problems where verifier drift makes scalar reward unreliable; aligns with triple-verify rule.
- Library curation: at 48 experiences after 100 samples, how does retrieval/ranking scale to wiki-sized $|E|$? Paper doesn't address; the wiki's qmd-based retrieval would be the analog.
- Capability prerequisite: QwQ-32B actually *regressed* on web tasks with the same recipe (27.5→25.5%) — suggests the method only compounds for sufficiently strong base models, with implications for which Einstein cycles benefit.
- Connects to Self-Refine (Madaan 2023), Reflexion (Shinn 2023), Agent KB (Tang 2025); extends them by tying experience updates to *group-relative* semantic comparison rather than single-trajectory reflection.

## Key terms
GRPO, training-free RL, semantic advantage, in-context reinforcement learning, experience library, ReAct, tool-integrated reasoning, AIME, DeepSeek-V3.1, self-refine, Reflexion, agentic RL, token prior, group rollouts, frozen policy
