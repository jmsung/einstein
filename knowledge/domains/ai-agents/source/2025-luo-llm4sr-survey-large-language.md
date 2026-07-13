<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "LLM4SR: A Survey on Large Language Models for Scientific Research"
authors: [Ziming Luo, Zonglin Yang, Zexin Xu, Wei Yang, Xinya Du]
year: 2025
source_url: https://arxiv.org/abs/2501.04306
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# LLM4SR: A Survey on Large Language Models for Scientific Research

**Authors:** Ziming Luo, Zonglin Yang, Zexin Xu, Wei Yang, Xinya Du  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2501.04306

## One-line
First systematic survey of how LLMs are being used across the full scientific research cycle — hypothesis discovery, experiment planning/execution, paper writing, and peer review.

## Key claim
LLM-driven scientific discovery has consolidated around an identifiable set of reusable "key components" — inspiration retrieval, novelty/validity/clarity feedback checkers, evolutionary search, multi-inspiration composition, hypothesis ranking, and automatic research-question construction — and progress in the field can be tracked by which components a given method incorporates (Table 1).

## Method
Literature review of ~200 works organized along four research-pipeline stages (§2 hypothesis discovery, §3 experiment planning, §4 writing, §5 peer review). For hypothesis discovery, the authors decompose each system (SciMON, MOOSE, MOOSE-Chem, FunSearch, ResearchAgent, AIScientist, SciAgents, Nova, etc.) into the presence/absence of the eight key components above, and trace lineage from classical Literature-Based Discovery (Swanson's "ABC" model) and inductive reasoning to current LLM-driven pipelines.

## Result
Establishes a taxonomy: (1) inspiration retrieval strategies — semantic neighbors (SciMON), concept co-occurrence (ResearchAgent, SciPIP), random-citation-graph (SciAgents), and LLM-selected (MOOSE, MOOSE-Chem, Nova); (2) three feedback checkers — novelty, validity (heuristic except FunSearch/HypoGeniC/LLM-SR/SGA which have real verifiers), clarity; (3) evolutionary algorithms — island-based (FunSearch, LLM-SR), evolutionary search (SGA), evolutionary unit (MOOSE-Chem); (4) Leveraging Multiple Inspirations (introduced by MOOSE-Chem to decompose $P(\text{hypothesis}|\text{background})$ into multi-inspiration composition). FunSearch is highlighted as the rare case with a *real* validity oracle (a code compiler/verifier for math problems).

## Key terms
LLM4SR, scientific hypothesis discovery, literature-based discovery, ABC model, inductive reasoning, FunSearch, MOOSE-Chem, SciMON, evolutionary algorithm, novelty validity clarity checker, multi-inspiration composition, council dispatch, automated peer review, AI scientist, program search with verifier
