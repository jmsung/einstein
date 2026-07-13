<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "CATArena: Evaluating Evolutionary Capabilities of Code Agents via Iterative Tournaments"
authors: [Lingyue Fu, Xin Ding, Li Pan, Yaoming Zhu, Shaolei Zhang, Lin Qiu, Weiwen Liu, Weinan Zhang, Xuezhi Cao, Xunliang Cai, Jiaxin Ding, Yong Yu]
year: 2025
source_url: https://arxiv.org/abs/2510.26852
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
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

## Key terms
code agents, evolutionary capability, iterative tournament, self-reflection, peer-learning, $S_{evo}$ OLS slope, $S_{base}$, execution feedback, Round-Robin, OIBench, SWE-Perf, complexity barrier
