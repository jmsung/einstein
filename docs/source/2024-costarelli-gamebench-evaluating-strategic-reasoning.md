---
type: source
kind: paper
title: GameBench: Evaluating Strategic Reasoning Abilities of LLM Agents
authors: Anthony Costarelli, Mat Allen, Roman Hauksson, Grace Sodunke, S. Hariharan, Carlson Cheng, Wenjie (Andy) Li, A. Yadav
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2406.06613
source_local: ../raw/2024-costarelli-gamebench-evaluating-strategic-reasoning.pdf
topic: general-knowledge
cites:
---

# GameBench: Evaluating Strategic Reasoning Abilities of LLM Agents

**Authors:** Anthony Costarelli, Mat Allen, Roman Hauksson, Grace Sodunke, S. Hariharan, Carlson Cheng, Wenjie (Andy) Li, A. Yadav  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2406.06613

## One-line
A 9-game cross-domain benchmark for LLM strategic reasoning, using obscure board/card/social-deduction games chosen to be out-of-distribution from pretraining corpuses.

## Key claim
Across 9 games rated via an exponential Bradley–Terry model, no GPT-3/GPT-4 configuration matches the human baseline (rating $1.76$); base GPT-4 ($-0.89$) actually performs *worse* than random ($-0.50$), driven largely by total failure on Sea Battle. CoT scaffolding gives the strongest lift (GPT-4-CoT rating $0.16$), beating RAP ($-0.10$).

## Method
Nine games (Air Land Sea, Arctic Scavengers, Are You the Traitor?, Codenames, Hive, Pit, Santorini, Two Rooms and a Boom, Sea Battle) span six reasoning axes: abstract strategy, non-determinism, hidden info, language communication, social deduction, cooperation. Agents (GPT-3, GPT-4, $\pm$ Chain-of-Thought, $\pm$ Reasoning-via-Planning MCTS at depth 2, random baseline, human) play pairwise matches; ratings fit by MLE on an exponential Bradley–Terry model $P(i > j) = e^{\beta_i}/(e^{\beta_i}+e^{\beta_j})$ with 10,000 bootstrap resamples weighted inversely by per-game match count.

## Result
Ranking: human ($1.76$) > GPT-4-CoT ($0.16$) > GPT-3-CoT ($0.06$) > GPT-4-RAP ($-0.10$) > GPT-3 ($-0.48$) > random ($-0.50$) > GPT-4 ($-0.89$). CoT helps GPT-4 more than GPT-3 (consistent with bigger-model-uses-context better). RAP underperforms CoT, hypothesized to be compounding state-prediction errors in its MCTS rollout. Aggregate ratings are fragile to single-game outliers (Sea Battle dominates GPT-4's collapse); authors propose g-factor / factor-analysis aggregation.

## Why it matters here
General background; no direct arena tie. Tangentially relevant as a *benchmark-design* reference for the einstein agent's self-improvement metrics (cycle-log, skill-library) — the paper's discussion of cherry-picking risk, out-of-distribution curation, and aggregation fragility echoes the honesty checks in `docs/agent/`.

## Open questions / connections
- How to design black-box scaffolds beyond CoT/RAP that actually beat CoT — RAP-as-implemented suffered from compounding errors in predicted states.
- Robust aggregation across heterogeneous tasks (g-factor / factor analysis vs. naive Bradley–Terry mean) — parallels the einstein cycle-log's "per-problem vs aggregate" tension.
- How to verify out-of-distribution status without strategy-guide-injection ablations, and how to keep curated benchmarks OOD as frontier models retrain.

## Key terms
LLM agent benchmark, strategic reasoning, Chain-of-Thought prompting, Reasoning-via-Planning, Monte Carlo tree search, Bradley–Terry model, exponential rating model, Elo, bootstrapping, GPT-3.5, GPT-4, social deduction games, out-of-distribution evaluation, scaffolding ablation
