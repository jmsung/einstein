<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-reasoning]
title: "Towards Scientific Intelligence: A Survey of LLM-based Scientific Agents"
authors: [Shuo Ren, Pu Jian, Zhenjiang Ren, Chunlin Leng, C. Xie, Jiajun Zhang]
year: 2025
source_url: https://arxiv.org/abs/2503.24047
drive_file_id: 1kn4Bs0-ea5Q-FWY3PBhtw3GGgUV-v-Os
text_source: paperclip
ingested_by: agent
---

# Towards Scientific Intelligence: A Survey of LLM-based Scientific Agents

**Authors:** Shuo Ren, Pu Jian, Zhenjiang Ren, Chunlin Leng, C. Xie, Jiajun Zhang  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2503.24047

## One-line
A mechanism-centric survey of LLM-based scientific agents that taxonomizes their architecture into four building blocks — Planner, Memory, Action Space, Verifier — across >120 papers and >40 benchmarks.

## Key claim
Scientific agents are best understood not by lifecycle stage or domain role but by their architectural mechanisms; in particular, planners split into prompt-native (P1 schema-driven, P2 context-augmented, P3 deliberative/reflective, P4 search-based, P5 role-interactive/multi-agent, P6 programmatic) and learned (L1 SFT/domain-trained, L2 RL/preference-optimized) families, which can be mixed-and-matched to fit a target scientific task.

## Method
Literature synthesis: classify >120 representative scientific-agent papers along four mechanism axes (planner, memory, action space, verifier), then index >40 evaluation benchmarks. A running cathode-design example threads through every component to act as a concrete "recipe book" for assembly. Ethics, bias, and reproducibility are framed as architectural constraints embedded in the verifier, not afterthoughts.

## Result
Delivers (i) a mechanism-level taxonomy with sub-types per component; (ii) a curated atlas mapping individual systems — Coscientist, CRISPR-GPT, AI Scientist-v2, AlphaEvolve, ChemReasoner, AI co-scientist, AtomAgents, ResearchAgent, STELLA, VirSci, Biomni, etc. — to their planner/memory/action/verifier signatures; (iii) an explicit contrast vs prior surveys (Luo 2025, Wang 2025c "Hitchhiker's Guide", Wei 2025 "Agentic Science"), positioning this work as design-focused rather than lifecycle- or domain-focused.

## Key terms
LLM-based scientific agent, planner taxonomy, prompt-native planner, ReAct, schema-driven planning, context-augmented retrieval, deliberative reflection, search-based planning, multi-agent role interaction, programmatic DAG planning, verifier, memory module, action space, reproducibility, AlphaEvolve, Coscientist, AI co-scientist, agentic science
