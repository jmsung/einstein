---
type: source
kind: paper
title: Recursive Language Models
authors: Alex L. Zhang, T. Kraska, Omar Khattab
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2512.24601
source_local: ../raw/2025-zhang-recursive-language-models.pdf
topic: general-knowledge
cites: 
---

# Recursive Language Models

**Authors:** Alex L. Zhang, T. Kraska, Omar Khattab  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2512.24601

## One-line
Introduces a general inference paradigm where an LLM treats its long prompt as a variable in a Python REPL and writes code that recursively invokes itself on programmatically extracted slices, bypassing context-window limits.

## Key claim
RLMs scale to 10M+ token inputs and beat vanilla GPT-5 by a median 26% vs compaction, 130% vs CodeAct-with-sub-calls, and 13% vs Claude Code across four long-context benchmarks at comparable cost; on OOLONG-Pairs (a quadratic-complexity aggregation task), base GPT-5 scores $\le 0.1\%$ F1 while RLM(GPT-5, depth=3) reaches 76.0%.

## Method
A Read-Eval-Print Loop (REPL) is initialized with the user prompt $P$ bound to a variable; the root LLM receives only constant-size metadata (length, prefix) and emits Python code that may slice $P$ and call `sub_LM(prompt)` or `sub_RLM(prompt)` over arbitrarily many slices, with intermediate state persisted symbolically as REPL variables. Termination is signaled by writing to a `Final` variable, and stdout is truncated each iteration so root context never grows with $|P|$. A small Qwen3-8B model is additionally post-trained on 1,000 RLM trajectories from an unrelated domain (LongBenchPro) using SFT, yielding +28.3% median gain.

## Result
Across four benchmarks (S-NIAH, BrowseComp-Plus 1K $\approx$ 6–11M tokens, OOLONG, OOLONG-Pairs, CodeQA 23K–4.2M tokens): RLM(GPT-5, depth$\ge$1) achieves 62–92% where base GPT-5 hits 0–44%; on the compositional reasoning benchmark LONGCOT-MINI, RLM(GPT-5.2)+decomposition hints reaches 65.6% overall vs 38.7% for base GPT-5.2 (+69.5% relative). Median per-task API cost stays comparable to or below baselines (e.g., $\$0.99$ vs extrapolated $\$1.50$–$2.75$ for BrowseComp+), though tail-cost variance is high. RL fine-tuning on Qwen3-4B-Instruct over MRCRv2 demonstrates length generalization from short to long splits.

## Why it matters here
General background; no direct arena tie. Potentially relevant as inference-scaffold design for the autonomous-loop agent itself — the REPL-with-recursive-sub-call pattern parallels how the math-solving protocol decomposes a hard problem into wiki queries, council sub-calls, and per-slice analysis, and could inform how the loop manages 10M+ token wiki context across many problems.

## Open questions / connections
- Could RLM-style symbolic recursion replace ad-hoc compaction when the council surveys the full wiki for a new problem (depth-1 sub-call per persona over per-problem slices)?
- Tail-latency / cost outliers come from RLMs that "discard" stored answers (Example E.2) — what fine-tuning signal eliminates this failure mode for an open small model?
- Length-generalization via RLVR on a synthetic short→long task is promising; does it transfer to non-synthetic math-reasoning corpora?

## Key terms
recursive language model, RLM, REPL, inference-time scaling, long context, context compaction, context rot, sub-agent delegation, CodeAct, ReAct, symbolic recursion, needle-in-a-haystack, OOLONG, BrowseComp-Plus, LongBench, Qwen3, GPT-5, Khattab, length generalization
