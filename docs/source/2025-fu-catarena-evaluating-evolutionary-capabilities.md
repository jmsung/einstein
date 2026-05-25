---
type: source
kind: paper
title: "CATArena: Evaluating Evolutionary Capabilities of Code Agents via Iterative Tournaments"
authors: Lingyue Fu, Xin Ding, Li Pan, Yaoming Zhu, Shaolei Zhang, Lin Qiu, Weiwen Liu, Weinan Zhang, Xuezhi Cao, Xunliang Cai, Jiaxin Ding, Yong Yu
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2510.26852
source_local: ../raw/2025-fu-catarena-evaluating-evolutionary-capabilities.pdf
topic: general-knowledge
cites:
---

# CATArena: Evaluating Evolutionary Capabilities of Code Agents via Iterative Tournaments

**Authors:** Lingyue Fu, Xin Ding, Li Pan, Yaoming Zhu, Shaolei Zhang, Lin Qiu, Weiwen Liu, Weinan Zhang, Xuezhi Cao, Xunliang Cai, Jiaxin Ding, Yong Yu  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2510.26852

## One-line
A benchmark framework that measures whether LLM code agents actually *improve over iterations* by pitting them against each other in multi-round tournaments with execution-feedback and peer-solution sharing.

## Key claim
Evolutionary capability ($S_{evo}$, the OLS slope of round-wise global performance) is weakly correlated with static single-turn proficiency ($S_{base}$): high-$S_{base}$ agents (e.g. Claude-4 on Chess, $S_{base}=0.90$) often regress ($S_{evo}=-0.061$), while low-start agents (Gemini-2.5-Pro on Gomoku, $0.25 \to S_{evo}=+0.156$) can surpass them through feedback absorption. Commercial CLI agents beat minimal-ADK agents on $S_{base}$ but show no decisive $S_{evo}$ advantage.

## Method
Two-phase loop: (1) initial zero-shot code submission $C^{(1)}$; (2) iterative evolution where each agent receives execution logs, a global leaderboard, and peer solutions, then produces $C^{(n)}$. A performance matrix $W^{n,m}_{i,j}$ aggregates round-robin win-rates (competitive: Gomoku/Chess/Bridge/Hold'em) or deterministic efficiency scores (objective: OIBench Time-AUC, SWE-Perf speedup); $S_{evo}$ is the OLS slope of per-round global scores $G^n_i$ over $N \le 4$ rounds, chosen over $G^N - G^1$ for outlier robustness.

## Result
Across six tasks and ~11 agents, $S_{evo}$ varies independently of $S_{base}$. Ablations: (i) peer-learning + self-reflection used jointly yields gains for only a minority of agents — most agents can leverage one channel but not both; (ii) hard environments (Chess, SWE-Perf, Pommerman ~4500-LoC) collapse to negligible/negative $S_{evo}$ — a "complexity barrier" beyond which agents can't extract actionable signal; (iii) the metric is stable under task-rule perturbations and across Python/JS/Go but reveals strong language bias (C++ wins OIBench, Python wins games).

## Why it matters here
General background; no direct arena tie. Relevant as methodology mirror for einstein's own cycle-log / skill-library / self-improvement-loop — this paper independently formalizes what the einstein repo calls "compounding": $S_{evo}$ is structurally the same idea as the cycle-log's cross-cycle improvement metric, and its OLS-slope-over-rounds construction is a candidate template for measuring whether the JSAgent loop actually self-improves on the 23 arena problems vs. just hammering harder each cycle.

## Open questions / connections
- Could $S_{evo}$-style OLS-slope-over-cycles replace ad-hoc "did the wiki grow" honesty checks in `docs/agent/metrics.md`?
- The "complexity barrier" phenomenon (agents stop improving once gap to optimum is large) predicts that hard arena problems (P1 sphere packing, P15/P16 equioscillation) will show flat or negative $S_{evo}$ unless peer-solution analogues (top-3 SOTA downloads) are explicitly seeded — matches the council-dispatch rule's top-3 SOTA seeding.
- Their finding that agents can't combine peer-learning + self-reflection is a direct caution against the einstein protocol's combined wiki-first + council-dispatch step — worth tracking whether cycles that do both actually outperform cycles that do one.

## Key terms
code agents, evolutionary capability, iterative tournament, self-reflection, peer-learning, $S_{evo}$ OLS slope, $S_{base}$, execution feedback, Round-Robin, OIBench, SWE-Perf, complexity barrier
