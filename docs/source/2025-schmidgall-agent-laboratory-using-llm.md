---
type: source
kind: paper
title: "Agent Laboratory: Using LLM Agents as Research Assistants"
authors: Samuel Schmidgall, Yusheng Su, Ze Wang, Ximeng Sun, Jialian Wu, Xiaodong Yu, Jiang Liu, Zicheng Liu, E. Barsoum
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2501.04227
source_local: ../raw/2025-schmidgall-agent-laboratory-using-llm.pdf
topic: general-knowledge
cites:
---

# Agent Laboratory: Using LLM Agents as Research Assistants

**Authors:** Samuel Schmidgall, Yusheng Su, Ze Wang, Ximeng Sun, Jialian Wu, Xiaodong Yu, Jiang Liu, Zicheng Liu, E. Barsoum  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2501.04227

## One-line
An autonomous multi-agent LLM pipeline that takes a human research idea and produces a code repository plus research report through three phases (literature review → experimentation → report writing).

## Key claim
A staffed-by-LLM "lab" with specialized agents (PhD, Postdoc, ML Engineer, SW Engineer, Professor) plus two solver modules (mle-solver, paper-solver) can autonomously execute ML research at ~$2.33/paper with gpt-4o and reach SOTA on a subset of MLE-Bench challenges, with o1-preview rated best by human reviewers and human-in-the-loop ("co-pilot mode") materially raising paper quality.

## Method
Three-phase agent workflow. (1) Literature Review: PhD agent iteratively queries arXiv API with `summary`/`full text`/`add paper` actions until $N{=}\max$ relevant papers curated. (2) Experimentation: PhD+Postdoc draft a plan, ML/SW Engineer prepare data (HuggingFace), then `mle-solver` runs a tree-search-like loop with `EDIT`/`REPLACE` code commands, compile-then-repair ($N_{\text{rep}}{=}3$), LLM-as-reward scoring on $[0,1]$, self-reflection on success/failure, and stabilization via top-program sampling + batch parallelization. (3) Report Writing: `paper-solver` builds an 8-section LaTeX scaffold, iteratively edits with LaTeX compile checks, and scores via an adapted NeurIPS auto-reviewer (Lu et al. 2024b — 65% human-level accuracy, F1 0.57).

## Result
o1-preview produces best human-rated papers (clarity, soundness); o1-mini wins experimental quality; gpt-4o trails. Auto-reviewer overestimates quality vs humans (6.1/10 vs 3.8/10). Co-pilot mode beats autonomous mode overall but trades off experimental quality/usefulness. mle-solver earns more medals (incl. gold/silver) than MLAB, OpenHands, and AIDE on the MLE-Bench subset. Cost: ~\$2.33/paper (gpt-4o), ~84% cheaper than prior autonomous-research baselines.

## Why it matters here
General background; no direct arena tie. Relevant only as architectural precedent for the autonomous-loop branch — patterns like `mle-solver`'s top-program pool + batch-parallel exploration + LLM-reward scoring map directly onto the einstein cycle_runner's apply pipeline, and `paper-solver`'s scaffold→edit→compile loop mirrors the wiki distill→lint cycle.

## Open questions / connections
- Auto-reviewer optimism gap (6.1 vs 3.8) — is the same drift biasing LLM-as-reward in `mle-solver` (and by analogy, any LLM-graded score in our wiki_lint / distill pipeline)?
- Does top-program-pool + EDIT/REPLACE outperform a single-trajectory CMA-ES-style agent loop? Direct analogue to our parallel apply step.
- Co-pilot vs autonomous trade-off: human gates raise quality but hurt experimental throughput — mirrors our wiki-ingest human-gating decision.
- No reproducibility / variance numbers reported across seeds; agent-lab outputs may be high-variance like our cycle-log entries.

## Key terms
LLM agents, autonomous research, mle-solver, paper-solver, MLE-Bench, AIDE, OpenHands, LLM-as-reward, tree search, self-reflection, batch parallelization, top-program sampling, automated peer review, co-pilot mode, NeurIPS auto-reviewer, agent pipeline
