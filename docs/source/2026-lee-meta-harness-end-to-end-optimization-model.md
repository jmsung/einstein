---
type: source
kind: paper
title: Meta-Harness: End-to-End Optimization of Model Harnesses
authors: Yoonho Lee, Roshen Nair, Qizheng Zhang, Kangwook Lee, Omar Khattab, Chelsea Finn
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2603.28052
source_local: ../raw/2026-lee-meta-harness-end-to-end-optimization-model.pdf
topic: general-knowledge
cites: 
---

# Meta-Harness: End-to-End Optimization of Model Harnesses

**Authors:** Yoonho Lee, Roshen Nair, Qizheng Zhang, Kangwook Lee, Omar Khattab, Chelsea Finn  ·  **Year:** 2026  ·  **Source:** https://arxiv.org/abs/2603.28052

## One-line
Automates the design of LLM "harnesses" (the code around a frozen model that decides what to store, retrieve, and show) by running a coding-agent proposer in an outer-loop search over harness source code, with full filesystem access to all prior candidates' code, scores, and execution traces.

## Key claim
Giving an agentic proposer raw access to the entire history of prior candidate code + traces (≈10 MTok/iter, ~3 orders of magnitude beyond prior text optimizers) yields substantially better harnesses than compressed-feedback methods: +7.7 pts over ACE on online text classification with 4× fewer context tokens; +4.7 pts average on 200 IMO-level problems across 5 held-out models; #1 among Claude Haiku 4.5 agents on TerminalBench-2, beating Terminus-KIRA.

## Method
Outer loop maintains a population and Pareto frontier of harnesses on a filesystem $D$; at each iteration a Claude-Code/Opus-4.6 proposer queries $D$ via `grep`/`cat` (median 82 files/iter, 20+ prior candidates referenced), proposes one or more new single-file Python harnesses, which are validated then evaluated on a held-out search set, with code+scores+traces logged back to $D$. The design is deliberately minimal — no hand-designed mutation operators, parent selection, or summary compression — so search quality scales with proposer capability. Ablations show raw execution traces (not scalar scores or LLM summaries) are the critical input: median accuracy jumps from 34.9 (scores+summary) to 50.0 (full traces).

## Result
On online text classification (GPT-OSS-120B over USPTO-50k, Symptom2Disease, LawBench): 48.6% avg vs ACE 40.9% / MCE 40.0%, using 11.4K vs 50.8K context tokens; matches OpenEvolve/TTT-Discover final accuracy in ~10× fewer evaluations and exceeds them by >10 pts at convergence. On 9 OOD classification datasets: 73.1% vs 70.2% ACE. On retrieval-augmented IMO-level math (200 problems): discovered 4-route BM25 harness (combinatorics / geometry / number theory / default) gives +4.7 pts pass@1 avg over no-retriever across 5 models. On TerminalBench-2: an "environment bootstrap" harness (single shell-snapshot injected before agent loop) added to Terminus-KIRA gains on 7/89 tasks.

## Why it matters here
Direct tie to the autonomous-loop agent being built in this repo: Meta-Harness is essentially an outer search over the same surface (proposer harness + filesystem-of-prior-attempts) that this project's self-improvement loop is constructing manually via `docs/wiki/` + `cycle-log.md`. The ablation result — raw execution traces beat LLM summaries by ~15 pts — directly validates the wiki's policy of keeping `docs/source/` distillations + `mb/active/` traces rather than only summary findings, and the filesystem-as-feedback-channel design is a concrete model for what the einstein agent's persistent layer should look like.

## Open questions / connections
- Could the council-dispatch + question-filing protocol be reframed as an outer-loop proposer search over optimizer scripts, with `mb/<problem>/experiment-log.md` as the queryable filesystem?
- Meta-Harness search budget (~60 evals / 20 iters) is small; what does the curve look like at 600 iters, and does diminishing return set in before structural rewrites are exhausted?
- The "environment bootstrap" winning candidate on TerminalBench-2 is purely additive after 6 regressions from control-flow edits — suggests a "safe-edit" prior worth encoding into the einstein cycle protocol (e.g., prefer additive context injection over evaluator/optimizer rewrites).
- Relation to GEPA, OpenEvolve, AlphaEvolve, ACE, MCE, TTT-Discover — all are compressed-feedback baselines that Meta-Harness beats; the einstein wiki should track which compression boundary it sits on.

## Key terms
harness optimization, agentic proposer, filesystem-as-feedback, coding agent, execution traces, Pareto frontier search, context engineering, ACE Agentic Context Engineering, GEPA, OpenEvolve, AlphaEvolve, TTT-Discover, retrieval-augmented reasoning, BM25 routing, TerminalBench-2, Claude Code, outer-loop search, self-improvement loop
