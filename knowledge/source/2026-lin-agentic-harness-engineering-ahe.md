---
type: source
kind: paper
title: Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses
authors: Jiahang Lin, Shichun Liu, Chengjun Pan, et al.
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2604.25850
source_local: ../raw/2026-lin-agentic-harness-engineering-ahe.pdf
topic: agentic-harness
cites: 
---

# Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses

**Authors:** Jiahang Lin, Shichun Liu, Chengjun Pan, et al.  ·  **Year:** 2026  ·  **Source:** https://arxiv.org/abs/2604.25850

## One-line
An autonomous closed-loop system where one agent evolves another coding agent's "harness" (prompts, tools, middleware, memory) by reading structured trajectory evidence and committing falsifiable, file-level edits.

## Key claim
Ten AHE iterations lift pass@1 on Terminal-Bench 2 from 69.7% (bash-only seed) to 77.0%, surpassing the human-designed Codex harness (71.9%) and self-evolving baselines ACE (68.9%) and Training-Free GRPO (72.3%); the frozen harness transfers to SWE-bench-verified with 12% fewer tokens than the seed and yields +5.1 to +10.1 pp cross-family gains on three alternate base models without re-evolution.

## Method
Three matched "observability pillars" implemented on the NexAU framework: (1) **component observability** — seven editable component types (system prompt, tool description/implementation, middleware, skill, sub-agent, long-term memory) exposed as files at fixed mount points with git-versioned edits; (2) **experience observability** — an Agent Debugger distills ~10M raw trajectory tokens into a ~10K-token layered evidence corpus with per-task root-cause reports plus a benchmark-level overview; (3) **decision observability** — every edit ships a change-manifest entry naming the evidence, root cause, fix, predicted fixes, and predicted regressions, which the next round verifies against observed task-level deltas, automatically rolling back ineffective edits at file granularity. The outer loop (Algorithm 1) iterates rollout → clean → attribute prior manifest + rollback → distill → evolve → commit, with $k \geq 2$ rollouts per task to stabilize pass@1.

## Result
On Terminal-Bench 2 (89 tasks): AHE 77.0% vs Codex 71.9%, NexAU0 seed 69.7%; component ablation shows memory-only 75.3%, tool-only 73.0%, middleware-only 71.9%, but system-prompt-only regresses to 67.4% — so non-prompt components carry the gain and interact non-additively (single-component swaps overshoot the stacked total). On SWE-bench-verified: 75.6% aggregate (best of panel), 461k tokens/trial vs 526k seed (12% reduction), 582k TF-GRPO, 679k ACE. Cross-model: largest gains on bases farthest from saturation (deepseek-v4-flash +10.1pp, qwen-3.6-plus +6.3pp, gemini-3.1-flash-lite +5.1pp). Self-attribution is reliable for fixes (precision/recall swing high across rounds) but blind to regressions (cumulative regression precision 11.6%, recall 11.1% — 40 unforeseen regressions vs 5 foreseen).

## Why it matters here
Direct architectural relevance to the einstein autonomous-loop agent: the three observability pillars (decoupled file-level components, layered drill-down evidence corpus, falsifiable change manifests with rollback) map almost 1:1 onto einstein's `.claude/rules/`, `knowledge/wiki/` distillation, and `docs/agent/cycle-log.md` + skill-library architecture. Empirically validates this project's core bets that (a) failures-as-findings with articulated why compound, (b) prompt-only self-evolution underperforms structural edits to tools/middleware/memory, and (c) self-attribution is asymmetric — fixes are foreseeable, regressions are not, which directly motivates einstein's triple-verify rule as the regression-foresight gap-filler.

## Open questions / connections
- Regression foresight is the explicit open problem: 89% of regressions are unforeseen by the evolve agent — what structural signal would surface them before commit?
- Non-additive component interaction caps aggregate gain (single-component swaps overshoot full AHE on Hard tier) — how to optimize jointly without combinatorial explosion?
- Timeout-budget coupling during evolution leaks into the harness, creating a generalization hazard when transferring across reasoning tiers (the non-monotone GPT-5.4 medium/high/xhigh result).
- Extends prior single-surface self-evolution lines (ACE playbooks [49], TF-GRPO [4], reflection [20,32], skill libraries [41], program archives [11,24], graph workflows [48,51]) to joint multi-component optimization.
- Connects to einstein's [[self-improvement-loop]], [[cycle-discipline]], [[failure-is-a-finding]], [[triple-verify]] rules and the `docs/agent/` honesty layer.

## Key terms
agentic harness engineering, observability-driven evolution, self-evolving agent, coding agent harness, Terminal-Bench, SWE-bench, NexAU framework, Agent Debugger, change manifest, falsifiable contract, component ablation, cross-model transfer, self-attribution, regression foresight, ACE playbook, Training-Free GRPO
