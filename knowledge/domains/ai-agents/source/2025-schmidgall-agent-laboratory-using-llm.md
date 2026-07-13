<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-reasoning]
title: "Agent Laboratory: Using LLM Agents as Research Assistants"
authors: [Samuel Schmidgall, Yusheng Su, Ze Wang, Ximeng Sun, Jialian Wu, Xiaodong Yu, Jiang Liu, Zicheng Liu, E. Barsoum]
year: 2025
source_url: https://arxiv.org/abs/2501.04227
drive_file_id: 1YA2BdozBltpNMLf0MpwCErm---HjBHfi
text_source: paperclip
ingested_by: agent
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

## Key terms
LLM agents, autonomous research, mle-solver, paper-solver, MLE-Bench, AIDE, OpenHands, LLM-as-reward, tree search, self-reflection, batch parallelization, top-program sampling, automated peer review, co-pilot mode, NeurIPS auto-reviewer, agent pipeline
