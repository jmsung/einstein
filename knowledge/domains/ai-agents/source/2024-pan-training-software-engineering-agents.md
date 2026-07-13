<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-reasoning]
title: Training Software Engineering Agents and Verifiers with SWE-Gym
authors: [Jiayi Pan, Xingyao Wang, Graham Neubig, N. Jaitly, Heng Ji, Alane Suhr, Yizhe Zhang]
year: 2024
source_url: https://arxiv.org/abs/2412.21139
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Training Software Engineering Agents and Verifiers with SWE-Gym

**Authors:** Jiayi Pan, Xingyao Wang, Graham Neubig, N. Jaitly, Heng Ji, Alane Suhr, Yizhe Zhang  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2412.21139

## One-line
Builds the first executable training environment for SWE agents (2,438 real GitHub-issue tasks with runtime + unit tests) and uses it to train both a policy and an outcome-supervised verifier, achieving SOTA among open-weight SWE agents.

## Key claim
Rejection-sampling fine-tuning a 32B Qwen-2.5-Coder on just 491 SWE-Gym trajectories lifts SWE-Bench Verified resolution from 7.0% to 20.6% (+13.6) and Lite from 3.0% to 15.3% (+12.3); adding a learned verifier for Best@k selection over 8 rollouts pushes Verified to 32.0% and Lite to 26.0%.

## Method
SWE-Gym packages 2,438 Python issues from 11 repos with pre-installed dependencies and gold-patch-validated unit tests (≈200 human-hours + 10k CPU-hours to construct). Training uses filtered behavior cloning on successful agent–environment trajectories from two scaffolds (OpenHands ReAct-style; Moatless specialized workflow). Inference-time scaling trains an outcome-supervised reward model (ORM) on success/failure trajectory pairs and reranks $k$ candidate rollouts by predicted $P(\text{success})$, giving roughly log-linear gains in $k$.

## Result
- Policy: +12–14% absolute resolution on both SWE-Bench splits across 7B/14B/32B; reduces stuck-in-loop rate by 4.6–18.6%.
- Verifier + Best@8: 32.0% Verified, 26.0% Lite — new open-weight SOTA, competitive with the closed 72B Nebius system (40.6%) at much lower compute.
- Training data scales without saturation up to 491 trajectories; per-instance trajectory cap of 2 best balances coverage vs easy-task bias; naive on-policy self-improvement (32B) regressed Lite from 15.3% to 8.7%.

## Key terms
SWE-Gym, SWE-Bench, software engineering agents, rejection sampling fine-tuning, outcome-supervised reward model, ORM, verifier reranking, Best@k, inference-time scaling, OpenHands, Moatless, Qwen-2.5-Coder, agent trajectories, per-instance capping
