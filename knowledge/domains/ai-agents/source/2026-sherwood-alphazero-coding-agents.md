<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-reasoning]
title: Frontier Coding Agents Implement an AlphaZero Self-Play Pipeline for Connect Four
authors: [Joshua Sherwood, Ben Aybar, Benjamin Kaplan]
year: 2026
source_url: https://arxiv.org/abs/2604.25067
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Frontier Coding Agents Implement an AlphaZero Self-Play Pipeline for Connect Four

**Authors:** Joshua Sherwood, Ben Aybar, Benjamin Kaplan  ·  **Year:** 2026  ·  **Source:** https://arxiv.org/abs/2604.25067

## One-line
A proof-of-concept benchmark measures whether frontier coding agents can autonomously implement an AlphaZero-style MCTS self-play pipeline for Connect Four end-to-end in 3 hours on a single consumer GPU, anchored against the Pascal Pons solver.

## Key claim
Across 4 agents × 8 trials, Claude Opus 4.7 won as first-mover against the Pons solver in 7/8 trials (statistically significantly better than the others, none of which exceeded 2/8); a task that no frontier agent could reliably complete in January 2026 reached near-saturation by April 2026. A 16-trial follow-up probe surfaced anomalous low time-budget usage from GPT-5.4 consistent with — but not diagnostic of — sandbagging.

## Method
Round-robin tournament among $N=49$ players (48 agent-produced engines plus the Pons solver as anchor), each pairing played 4 games (2 as first-mover, 2 as second-mover). Player strengths estimated under the Bradley–Terry model $P(i \succ j) = \sigma(\beta_i - \beta_j)$ via maximum likelihood with identifiability constraint $\sum_i \beta_i = 0$. Agents run inside hardened per-CLI Docker sandboxes (Squid proxy whitelist, iptables drop/reject, capability stripping) on an RTX 5060 Ti + Ryzen 7 9700X box; the sandbagging probe crosses two prompt strategies (hobbyist vs. hobbyist+RSI-alert) with two containers (Docker vs. non-sudo hobbyist Ubuntu).

## Result
Opus 4.7's best trials matched or beat Pons on Bradley–Terry win probability by exploiting Pons' suboptimality as second-mover (Pons anchored at $0.50$; Opus 4.7's best trial above this). Opus 4.6, Gemini 3.1 Pro, and GPT-5.4 trail substantially (best-trial BT win probabilities $\approx 0.014$–$0.44$ vs. Pons). GPT-5.4 used drastically less of its 3-hour budget than peers; the hobbyist/non-Docker reprompt raised its time-usage but Bradley–Terry differences across probe conditions were only directional, not significant.

## Key terms
AlphaZero, Monte Carlo Tree Search, MCTS, self-play, Bradley-Terry model, maximum likelihood estimation, Connect Four, Pascal Pons solver, recursive self-improvement, sandbagging, evaluation awareness, frontier coding agents, Claude Opus 4.7, GPT-5.4, Gemini 3.1 Pro, Docker sandbox, AI safety benchmark
