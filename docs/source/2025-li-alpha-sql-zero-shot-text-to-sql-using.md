---
type: source
kind: paper
title: Alpha-SQL: Zero-Shot Text-to-SQL using Monte Carlo Tree Search
authors: Boyan Li, Jiayi Zhang, Ju Fan, Yanwei Xu, Chong Chen, Nan Tang, Yuyu Luo
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2502.17248
source_local: ../raw/2025-li-alpha-sql-zero-shot-text-to-sql-using.pdf
topic: general-knowledge
cites:
---

# Alpha-SQL: Zero-Shot Text-to-SQL using Monte Carlo Tree Search

**Authors:** Boyan Li, Jiayi Zhang, Ju Fan, Yanwei Xu, Chong Chen, Nan Tang, Yuyu Luo  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2502.17248

## One-line
A zero-shot Text-to-SQL framework that uses Monte Carlo Tree Search with an LLM-as-Action-Model and a self-consistency reward to progressively construct SQL queries without fine-tuning.

## Key claim
Alpha-SQL reaches **69.7%** execution accuracy on the BIRD development set with a 32B open-source LLM (Qwen2.5), beating the previous best zero-shot method (RSL-SQL with GPT-4o) by **2.5 points**, and lifting Qwen2.5 by **15–20%** across 7B/14B/32B sizes vs. direct prompting.

## Method
Frame SQL synthesis as a search problem over a tree $\Psi=(V,E)$ where nodes are partial reasoning states and edges are one of 7 actions (Question Rephrasing, Schema Selection, Column Value Identification, Column Function Identification, SQL Generation, SQL Revision, Termination), with a fixed ordering table. MCTS rollouts (Selection via UCT $Q(v,a)/N(v,a) + c\sqrt{\ln N(v)/N(v,a)}$, Expansion sampling $N_\text{expansion}$ children per valid action, Simulation, Backpropagation) explore the space, with an LLM invoked at each edge to produce the next CoT-augmented state. The reward is **self-supervised self-consistency**: $R(y,q,D) = \frac{1}{N}\sum_i \mathbb{I}[\text{Exec}(y,D)=\text{Exec}(y_i,D)]$ over $N$ high-temperature resamples — no labels required.

## Result
On BIRD-dev: 69.7% with Qwen2.5-Coder-32B (zero-shot, no fine-tuning), surpassing RSL-SQL/GPT-4o (67.2%) and prior decomposition pipelines (CHASE-SQL etc.). Ablations confirm each of the 7 actions contributes, and accuracy scales monotonically with $N_\text{rollout}$. De-duplication of CoT-distinct-but-output-identical children materially cuts the branching factor.

## Why it matters here
General background; no direct arena tie — Text-to-SQL is out of scope for sphere packing / autocorrelation / extremal problems. **Relevant only as a methodology reference**: MCTS + LLM-as-action-model + self-consistency reward is a candidate template for the autonomous-loop agent itself (e.g., council dispatch + action-space exploration on math problems), complementing rStar and AFlow already in the wiki.

## Open questions / connections
- Can the self-consistency reward generalize to math optimization where "execution equivalence" is harder to define (numerical equality with tolerance? triple-verify agreement?).
- Action-space design for math problems: what is the Text-to-SQL action set's analog for sphere packing / kissing configurations (e.g., "select parameterization", "polish basin", "verify")?
- Extends rStar (Qi et al. 2024) MCTS-with-self-consistency and CHASE-SQL multi-path decomposition; relates to AFlow (Zhang et al. 2025) for automated workflow generation already in agent literature.

## Key terms
Monte Carlo Tree Search, MCTS, UCT, LLM-as-Action-Model, self-consistency reward, Text-to-SQL, zero-shot reasoning, Chain-of-Thought, test-time compute, action space, self-supervised reward, Qwen2.5, BIRD benchmark, tree search, rStar
