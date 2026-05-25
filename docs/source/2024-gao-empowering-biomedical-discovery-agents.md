---
type: source
kind: paper
title: Empowering Biomedical Discovery with AI Agents
authors: Shanghua Gao, Ada Fang, Yepeng Huang, Valentina Giunchiglia, Ayush Noori, J. Schwarz, Yasha Ektefaie, Jovana Kondic, M. Zitnik
year: 2024
author: agent
drafted: 2026-05-24
ingested_at: 2026-05-24
source_type: arxiv
source_url: https://arxiv.org/abs/2404.02831
source_local: ../raw/2024-gao-empowering-biomedical-discovery-agents.pdf
topic: general-knowledge
cites:
---

# Empowering Biomedical Discovery with AI Agents

**Authors:** Shanghua Gao, Ada Fang, Yepeng Huang, Valentina Giunchiglia, Ayush Noori, J. Schwarz, Yasha Ektefaie, Jovana Kondic, M. Zitnik  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2404.02831

## One-line
A perspective arguing that "AI scientists" for biomedicine should be realized as compound multi-agent systems combining LLMs, ML tools, experimental platforms, and human experts that can formulate hypotheses, evaluate them, quantify uncertainty, and iteratively refine knowledge.

## Key claim
Single LLM-based agents (mimicry-trained) are insufficient for genuine scientific discovery; instead, multi-agent systems with role specialization (brainstorming, expert consultation, debate, round-table, self-driving lab) plus a four-level autonomy taxonomy (Level 0 no-agent → Level 3 AI-as-scientist) provide the right scaffolding, with current state-of-the-art (e.g., Coscientist, ChemCrow, AutoBa) sitting only at Level 1.

## Method
Perspective/position paper rather than theorem-proving: surveys the evolution from databases → search engines → ML models → interactive learning → AI agents, then categorizes multi-agent collaboration patterns (brainstorm / consult / debate / round-table / self-driving-lab) and defines a level-of-autonomy taxonomy across three axes (Hypothesis, Experiment, Reasoning). Cites tool-use (Toolformer, HuggingGPT), RLHF/DPO, chain/tree/graph-of-thought, conformal prediction, and uncertainty calibration as constituent techniques.

## Result
No numerical theorem; the contributions are conceptual: (i) a taxonomy of five multi-agent collaboration schemes; (ii) a Level 0–3 autonomy ladder requiring an agent to clear all three axes (Hypothesis/Experiment/Reasoning) at the claimed level; (iii) an argument that novel-hypothesis generation is *not* aligned with next-token prediction and requires creativity + grounding beyond pretraining data; (iv) target application areas (virtual cells, programmable phenotypes, cellular circuits, therapeutics).

## Why it matters here
General background; no direct arena tie. The relevant transferable ideas are the multi-agent collaboration patterns (debate, round-table, self-driving lab) and the autonomy levels — these inform how the einstein agent's council-dispatch + self-improvement loop should be structured, and how to honestly grade its own autonomy. Reinforces the wiki-first / failure-is-a-finding stance: agents need structured memory and uncertainty quantification to avoid mimicry collapse.

## Open questions / connections
- How to quantify skepticism / uncertainty in agent-generated hypotheses (conformal prediction, semantic uncertainty) — relevant to triple-verify discipline.
- Whether LLM-based agents can generate *genuinely novel* hypotheses or only interpolate in training distribution (the "embers of autoregression" critique [174,175]).
- Connection to debate/round-table schemes (Reconcile [73]) as templates for the council-dispatch rule with confidence-weighted voting.
- Memory architectures (MemoryBank [151], ChatDB [142]) as analogues for the wiki-as-persistence-layer design.

## Key terms
AI agents, multi-agent systems, LLM, RLHF, chain-of-thought, tree-of-thought, tool use, Coscientist, ChemCrow, self-driving laboratory, conformal prediction, uncertainty quantification, hypothesis generation, autonomy levels, biomedical discovery, retrieval-augmented generation, Reconcile, debate agents, round-table, council dispatch
