<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, bio-drug-discovery]
title: Empowering Biomedical Discovery with AI Agents
authors: [Shanghua Gao, Ada Fang, Yepeng Huang, Valentina Giunchiglia, Ayush Noori, J. Schwarz, Yasha Ektefaie, Jovana Kondic, M. Zitnik]
year: 2024
source_url: https://arxiv.org/abs/2404.02831
drive_file_id: 1M2kDHKIYjiy-gEx8ecFDFUBKp3umuiDO
text_source: paperclip
ingested_by: agent
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

## Key terms
AI agents, multi-agent systems, LLM, RLHF, chain-of-thought, tree-of-thought, tool use, Coscientist, ChemCrow, self-driving laboratory, conformal prediction, uncertainty quantification, hypothesis generation, autonomy levels, biomedical discovery, retrieval-augmented generation, Reconcile, debate agents, round-table
