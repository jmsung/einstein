---
type: source
kind: paper
title: "AutoMLGen: Navigating Fine-Grained Optimization for Coding Agents"
authors: Shangheng Du, Xiangchao Yan, Dengyang Jiang, Jiakang Yuan, Yusong Hu, Xin Li, Liang He, Bo Zhang, Lei Bai
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2510.08511
source_local: ../raw/2025-du-automlgen-navigating-fine-grained-optimization.pdf
topic: general-knowledge
cites:
---

# AutoMLGen: Navigating Fine-Grained Optimization for Coding Agents

**Authors:** Shangheng Du, Xiangchao Yan, Dengyang Jiang, Jiakang Yuan, Yusong Hu, Xin Li, Liang He, Bo Zhang, Lei Bai  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2510.08511

## One-line
An LLM coding agent for end-to-end machine-learning-engineering tasks that replaces tree-structured search with Monte Carlo Graph Search (MCGS) plus a curated ML domain knowledge base, achieving SOTA on MLE-Bench.

## Key claim
On MLE-Bench (75 Kaggle competitions) with a 12-hour budget (half the standard 24h), AutoMLGen attains $36.4\%$ average medal rate, $18.7\%$ gold-medal rate, $96.4\%$ valid-submission rate, and $48.4\%$ above-median rate — beating ML-Master ($29.3\%$), Neo ($34.2\%$ at 36h), and R&D-Agent ($22.4\%$). On MLE-Bench-Lite it reaches $62.1\%$ medal rate.

## Method
Search is reframed as a directed graph $G=(V, E_T \cup E_{\text{ref}})$: primary edges $E_T$ form an MCTS tree (UCT selection with $c=1.414$, backprop only along $E_T$), while reference edges $E_{\text{ref}}$ enable three new expansion modes — **intra-branch evolution** (reuse last $k$ trajectory nodes), **cross-branch reference** (top-$N$ nodes from other branches when stalled), and **multi-branch aggregation** (spawn fresh branch root from fused top trajectories). Fine-grained operators (Draft / Debug / Improve-Normal / Improve-FE / Improve-CS / Fusion / Ensemble / Code-Review) act on nodes, seeded by a model-data-strategy knowledge base curated from HuggingFace/GitHub/Kaggle, injected at initialization with probability $0.8$.

## Result
Ablation on MLE-Bench-Lite: baseline MCTS $40.91\%$ → +KB $50.00\%$ → +intra-branch $59.09\%$ → full MCGS $68.12\%$ medal rate. Cross-LLM robustness shown with DeepSeek-R1, o4-mini, Gemini-2.5-pro: text tasks converge tightly across models, image/tabular tasks show larger model-dependent variance. Asynchronous branch-parallel exploration (3 workers, max 500 search steps, branch top-$k=5$, global top-$k=10$) drives the 12h budget.

## Why it matters here
General background; no direct arena tie. The MCGS graph-with-reference-edges idea is potentially relevant to the autonomous-loop agent's own cycle architecture (intra-branch self-reflection, cross-problem reuse of dead-end findings, multi-cycle aggregation map cleanly onto the wiki's findings/concepts/promotion loop), but the paper itself studies Kaggle ML pipelines, not math-optimization problems.

## Open questions / connections
- Does the $E_T$-only backprop with $E_{\text{ref}}$-aided expansion generalize to math-search loops where "branches" are problem-attempt cycles and "reference edges" are wiki findings cited across problems?
- Can the Improve-CS / Fusion operators be re-cast as council-dispatch operators that fuse persona-question outputs across branches?
- The $0.8$ KB-injection-at-init probability is a tunable cold-start prior — analog for wiki-first-lookup discipline at cycle start?
- Extends AIDE [arXiv:2502.13138] (greedy tree), ML-Master [arXiv:2506.16499] (MCTS + scoped memory), R&D-Agent [arXiv:2505.14738] (parallel traces) by adding cross-branch graph edges.

## Key terms
Monte Carlo Graph Search, MCGS, MCTS, UCT, coding agent, MLE-Bench, AutoML, knowledge base prior, intra-branch evolution, cross-branch reference, multi-branch aggregation, trajectory reuse, fine-grained operators, LLM agent, self-evolving search
