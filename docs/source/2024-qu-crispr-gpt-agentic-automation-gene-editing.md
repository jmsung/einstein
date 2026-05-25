---
type: source
kind: paper
title: CRISPR-GPT for agentic automation of gene-editing experiments
authors: Yuanhao Qu, Kaixuan Huang, Ming Yin, Kanghong Zhan, Dyllan Liu, Di Yin, H. Cousins, William A. Johnson, Xiaotong Wang, Mihir M. Shah, R. Altman, Denny Zhou, Mengdi Wang, Le Cong
year: 2024
author: agent
drafted: 2026-05-24
ingested_at: 2026-05-24
source_type: arxiv
source_url: https://arxiv.org/abs/2404.18021
source_local: ../raw/2024-qu-crispr-gpt-agentic-automation-gene-editing.pdf
topic: general-knowledge
cites:
---

# CRISPR-GPT for agentic automation of gene-editing experiments

**Authors:** Yuanhao Qu, Kaixuan Huang, Ming Yin, Kanghong Zhan, Dyllan Liu, Di Yin, H. Cousins, William A. Johnson, Xiaotong Wang, Mihir M. Shah, R. Altman, Denny Zhou, Mengdi Wang, Le Cong  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2404.18021

## One-line
An LLM agent that decomposes CRISPR gene-editing experimental design into a state-machine of sub-tasks (system selection, gRNA design, delivery, off-target, protocol, validation), invoking external tools to overcome general-purpose LLM hallucination on biological sequences.

## Key claim
General-purpose LLMs (GPT-4) hallucinate gRNA/primer sequences that fail to align to reference genomes; wrapping a ReAct-style planner around a hand-authored task-decomposition table plus tool calls (Primer3, Broad guide-RNA libraries, CRISPRitz off-target, web search) produces actionable, expert-vetted designs. Validated end-to-end via wet-lab knockout of TGFBR1/SNAI1/BAX/BCL2L1 in A375 cells by non-expert users.

## Method
Four-module architecture: (1) **LLM planner** decomposes user request into an ordered task list respecting a static dependency DAG (22 tasks across 4 meta-tasks: knockout, base-edit, prime-edit, CRISPRa/i); (2) **Task Executor** as chained state machines — each state = one sub-goal with templated instructions and well-defined transitions; (3) **Tool Provider** wraps APIs (Primer3, BLAST, CRISPRitz, guide-RNA DBs) behind LLM-friendly textual interfaces rather than exposing raw signatures; (4) **LLM Agent** answers on the user's behalf via ReAct + chain-of-thought, with human override at every step. JSON-formatted prompts; "I don't know → manual control" rule for raw sequence requests.

## Result
22 task state machines covering full pipelines for Cas9/Cas12a knockout, ABE/CBE base editing, prime editing, and CRISPRa/i. Human evaluation by 12 CRISPR experts on Accuracy / Reasoning / Completeness / Conciseness rubrics (1–5 scale) shows CRISPR-GPT outperforms ChatGPT-3.5 and GPT-4 (gpt-4-0613). Wet-lab validation: 4 crRNAs cloned via Golden Gate into Cas12a backbone, lentiviral delivery into A375, NGS amplicon confirmation of editing — designed by non-expert users using the agent.

## Why it matters here
General background; no direct arena tie. **Methodologically relevant** to the einstein autonomous-loop agent: same pattern of *LLM-planner + state-machine task executor + wrapped tool calls + human-override* that this repo is building for math problem-solving — particularly the "wrap APIs behind LLM-friendly textual interfaces" lesson and the static-dependency-DAG vs dynamic-planning tradeoff (CRISPR-GPT deliberately forbids LLM from adding/deleting tasks at runtime for robustness).

## Open questions / connections
- Static task DAG vs dynamic planner: paper flags dynamic task addition as future work — same tradeoff facing einstein's [[council-dispatch]] and math-solving-protocol state machines.
- "I don't know" → human handoff for raw sequence requests — analog to the agent's wiki-first refusal + triple-verify when asked for numerical claims it can't ground.
- Extends ChemCrow (chemistry) and Coscientist (Pd-catalyzed coupling) into the bio domain; the cross-domain pattern (wrapped-tool LLM agent + wet-lab loop) is the transferable artifact, not the CRISPR specifics.

## Key terms
LLM agent, ReAct, chain-of-thought, task decomposition, state machine, tool-augmented LLM, CRISPR-Cas9, guide RNA design, gene knockout, prime editing, base editing, agentic automation, ChemCrow, Coscientist
