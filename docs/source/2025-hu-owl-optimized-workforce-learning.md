---
type: source
kind: paper
title: OWL: Optimized Workforce Learning for General Multi-Agent Assistance in Real-World Task Automation
authors: Mengkang Hu, Yuhang Zhou, Wendong Fan, Yuzhou Nie, Bowei Xia, Tao Sun, Ziyu Ye, Zhaoxuan Jin, Yingru Li, Qiguang Chen, Zeyu Zhang, Yifeng Wang, Qianshuo Ye, Bernard Ghanem, Ping Luo, Guohao Li
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2505.23885
source_local: ../raw/2025-hu-owl-optimized-workforce-learning.pdf
topic: general-knowledge
cites:
---

# OWL: Optimized Workforce Learning for General Multi-Agent Assistance in Real-World Task Automation

**Authors:** Mengkang Hu, Yuhang Zhou, Wendong Fan, Yuzhou Nie, Bowei Xia, Tao Sun, Ziyu Ye, Zhaoxuan Jin, Yingru Li, Qiguang Chen, Zeyu Zhang, Yifeng Wang, Qianshuo Ye, Bernard Ghanem, Ping Luo, Guohao Li  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2505.23885

## One-line
A hierarchical multi-agent framework (WORKFORCE) decouples a domain-agnostic planner from domain-specific worker agents, and trains only the planner via SFT+DPO (OWL) to achieve open-source SOTA on the GAIA generalist-assistant benchmark.

## Key claim
WORKFORCE with Claude-3.7-Sonnet reaches $69.70\%$ on GAIA (beating OpenAI Deep Research's $67.36\%$ by $+2.34\%$), and OWL post-training lifts Qwen2.5-32B-Instruct from $36.36\%$ to $52.73\%$ ($+16.37\%$), surpassing GPT-4o-mini ($47.27\%$) and Qwen2.5-72B-Instruct ($49.09\%$) using no GAIA data in training.

## Method
Three-tier architecture: (i) a domain-agnostic **Planner** decomposes tasks; (ii) a **Coordinator** dispatches subtasks via a shared task channel (no peer-to-peer messaging); (iii) specialized **Worker Nodes** (Web, Document, Reasoning/Coding) execute with their own toolkits. Training is two-stage on the planner only: SFT on filtered GPT-4o-mini-synthesized successful trajectories, then **DPO** on preference pairs derived from real-world execution outcomes. Curriculum spans HotpotQA, WikiTableQuestions, custom math, and Infinity-MM to force capability coverage rather than domain memorization. Workers stay frozen; replanning is triggered by worker-reported subtask failure.

## Result
On GAIA validation: Level-1 $84.91\%$, Level-2 $68.60\%$, Level-3 $42.31\%$, avg $69.70\%$ — open-source SOTA. Ablation: training **planner only** ($45.45\%$) ≈ training both planner+worker ($46.68\%$) ≫ training workers only ($31.51\%$, *below* the $36.36\%$ baseline), confirming the planner is the leverage point. Wilcoxon signed-rank: WORKFORCE vs Single Agent $p<0.0001$; OWL vs base 32B $p=0.0018$. Robustness (multi-capability tasks) std $3.05$ vs $11.39$ for Role-Playing.

## Why it matters here
General background; no direct arena tie. The architectural pattern — **stable domain-agnostic planner + swappable domain-specific workers** — is structurally analogous to the einstein council-dispatch + per-problem worker design in `.claude/rules/council-dispatch.md`; the OWL ablation showing "train the planner, not the workers" gives empirical weight to focusing self-improvement effort on the coordinator/protocol layer rather than per-problem optimizer code.

## Open questions / connections
- Ablation says worker-only training *degrades* below baseline ($-4.85\%$): does that generalize to math-solving councils where worker specialization (e.g., mpmath polish, LP) is the actual bottleneck, or is this GAIA-specific?
- OWL uses DPO over real execution traces — directly applicable as a training signal for the einstein cycle-log if cycles were ever used to fine-tune a planner agent.
- Replanning is triggered only by *worker self-assessed failure*; no analog of triple-verify cross-check between independent workers. Verifier-mismatch failure modes (P9/P14/P17) would slip past this mechanism.
- Extends MetaGPT [13], CAMEL [16], MALT [20]; sits in the same family as Magnetic-One and Open Deep Research.

## Key terms
multi-agent system, hierarchical planner, domain-agnostic planning, worker decoupling, DPO, supervised fine-tuning, GAIA benchmark, task decomposition, replanning, coordinator, trajectory synthesis, OWL
