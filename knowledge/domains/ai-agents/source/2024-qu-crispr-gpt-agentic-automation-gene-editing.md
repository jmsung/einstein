<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, bio-drug-discovery]
title: CRISPR-GPT for agentic automation of gene-editing experiments
authors: [Yuanhao Qu, Kaixuan Huang, Ming Yin, Kanghong Zhan, Dyllan Liu, Di Yin, H. Cousins, William A. Johnson, Xiaotong Wang, Mihir M. Shah, R. Altman, Denny Zhou, Mengdi Wang, Le Cong]
year: 2024
source_url: https://arxiv.org/abs/2404.18021
drive_file_id: 1EgIb73-5UnNfd8XCC57ujlRfs4L8RK50
text_source: paperclip
ingested_by: agent
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

## Key terms
LLM agent, ReAct, chain-of-thought, task decomposition, state machine, tool-augmented LLM, CRISPR-Cas9, guide RNA design, gene knockout, prime editing, base editing, agentic automation, ChemCrow, Coscientist
