<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: AI Agents That Matter
authors: [Sayash Kapoor, Benedikt Stroebl, Zachary S. Siegel, Nitya Nadgir, Arvind Narayanan]
year: 2024
source_url: https://arxiv.org/abs/2407.01502
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# AI Agents That Matter

**Authors:** Sayash Kapoor, Benedikt Stroebl, Zachary S. Siegel, Nitya Nadgir, Arvind Narayanan  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2407.01502

## One-line
A critique of AI agent benchmarking practice arguing that evaluations must be cost-controlled, use proper held-out sets matched to generality level, and be reproducible — otherwise agents overfit and "SOTA" claims are meaningless.

## Key claim
On HumanEval, simple baselines (retry, warming, escalation) match or beat complex "SOTA" agents (LDB, LATS, Reflexion) at 1.5×–50× lower cost; on HotPotQA, joint cost-accuracy optimization via DSPy+Optuna cuts variable cost 41–53% while maintaining accuracy.

## Method
Empirical re-evaluation of leaderboard agents on HumanEval/WebArena with cost tracking; introduces three baselines (retry at temp=0, warming with increasing temperature 0→0.5, escalation from cheap to expensive models on failure). For joint optimization, modifies DSPy's BootstrapFewShot to use Optuna multi-objective search over temperature, few-shot example count/selection, and formatting flags to find Pareto-optimal (accuracy, token-cost) configurations. Surveys 17 agent benchmarks against a 4-level generality taxonomy (distribution-specific / task-specific / domain-general / general-purpose) to assess holdout adequacy.

## Result
LATS costs ~50× more than the warming baseline for similar HumanEval accuracy; escalation strictly Pareto-dominates LDB. Reproduction reveals systematic errors: LDB used GPT-4 (not GPT-3.5) for Reflexion baseline; LATS evaluated on subset of test cases inflating accuracy by ~3%; STeP's WebArena logs mark rate-limited failures as successes. 7/17 surveyed benchmarks have no holdout set; only 5/10 holdouts match generality level. On NovelQA, batched evaluation makes RAG appear 2× cheaper than long-context when sequential use is actually ~22× cheaper.

## Key terms
AI agent evaluation, Pareto frontier, cost-accuracy tradeoff, joint optimization, DSPy, Optuna, HumanEval, HotPotQA, WebArena, NovelQA, holdout set, benchmark overfitting, retry baseline, System 2, reproducibility
