---
type: source
kind: paper
title: "Towards Scientific Intelligence: A Survey of LLM-based Scientific Agents"
authors: Shuo Ren, Pu Jian, Zhenjiang Ren, Chunlin Leng, C. Xie, Jiajun Zhang
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2503.24047
source_local: ../raw/2025-ren-towards-scientific-intelligence-survey.pdf
topic: general-knowledge
cites:
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

## Why it matters here
General background for the autonomous-loop's own architecture: the four-component decomposition (planner / memory / action / verifier) and the P1–P6 + L1–L2 planner taxonomy give vocabulary for designing the JSAgent cycle (council dispatch ≈ P5 role-interactive, wiki-first lookup ≈ P2 context-augmented, search-based deep-research ≈ P4, schema-driven cycle-discipline ≈ P1). No direct arena/math tie.

## Open questions / connections
- Which planner type best fits *math-wisdom* compounding — does iterative wiki-grounded P2 dominate P4 tree-search for problems where the bottleneck is conceptual gap-detection rather than candidate enumeration?
- The survey's verifier discussion frames "factual accuracy + empirical consistency" — how does this map onto the triple-verify axiom (fast eval + exact reimpl + cross-check)?
- AlphaEvolve (Novikov 2025) appears under P6 programmatic — direct precedent for code-generating agents on hard math/algorithmic problems; worth ingesting separately.
- Cycle-discipline (cycle-log + skill-library) corresponds to "memory" + "verifier" feedback loop the survey identifies as critical for reproducibility.

## Key terms
LLM-based scientific agent, planner taxonomy, prompt-native planner, ReAct, schema-driven planning, context-augmented retrieval, deliberative reflection, search-based planning, multi-agent role interaction, programmatic DAG planning, verifier, memory module, action space, reproducibility, AlphaEvolve, Coscientist, AI co-scientist, agentic science
