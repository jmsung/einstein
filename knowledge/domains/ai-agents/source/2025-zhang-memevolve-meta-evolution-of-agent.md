<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "MemEvolve: Meta-Evolution of Agent Memory Systems"
authors: [Guibin Zhang, Haotian Ren, Chong Zhan, Zhen Zhou, Junhao Wang, He Zhu, Wangchunshu Zhou, Shuicheng Yan]
year: 2025
doi: 10.48550/arXiv.2512.18746
source_url: https://doi.org/10.48550/arXiv.2512.18746
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# MemEvolve: Meta-Evolution of Agent Memory Systems

## TL;DR
MemEvolve is a meta-evolutionary framework that jointly evolves an LLM agent's experiential knowledge AND the architecture of its memory system itself, treating memory as a "genotype" of four modular components (encode, store, retrieve, manage) that a bilevel optimization loop redesigns based on empirical performance feedback. It improves agent frameworks like SmolAgent and Flash-Searcher by up to 17.06% and generalizes across tasks, backbone LLMs, and frameworks.

## Key findings
- **Core thesis: no universally optimal memory architecture exists.** Memory systems that distill reusable APIs excel at web browsing but fail at math/science reasoning; self-critique memories help reasoning but hurt coding/tool-use. Current systems are *static* — a fixed ingestion/abstraction/retrieval pipeline — making them "skillful" but not "adaptive" learners. MemEvolve targets the transition to an adaptive learner that changes *how* it learns per task domain.
- **Modular design space (the "genotype").** Any memory system Ω is decomposed into four components: **Encode** (E — format raw experiences into structured units), **Store** (U — commit to persistent memory: vector DB, knowledge graph, JSON), **Retrieve** (R — context-aware recall), **Manage** (G — offline consolidation/forgetting). MemEvolve evolves the *programmatic implementations* of these modules.
- **Bilevel (dual) optimization.** *Inner loop* (experience evolution): each candidate memory architecture populates its memory base from a batch of trajectories. *Outer loop* (architectural evolution): a meta-evolution operator F ranks candidates by a 3-D fitness vector (task success, token cost, latency), retains top-K via non-dominated Pareto sorting, and generates new variants.
- **Diagnose-and-Design evolution.** F replays a parent architecture's execution batch to produce a structured *defect profile* (retrieval failures, ineffective abstractions, storage inefficiencies across E/U/R/G), then redesigns only permissible module sites to yield S valid descendant variants.
- **EvolveLab codebase.** Re-implements **twelve** representative memory systems (Voyager, ExpeL, Generative Agents, DILU, AWM, Mobile-E, Dynamic Cheatsheet, SkillWeaver, G-Memory, Agent-KB, Memp, EvolveR) under one `BaseMemoryProvider` ABC enforcing the four-component interface — a fair experimental arena.
- **Performance.** On xBench, Flash-Searcher+GPT-5-Mini rose from 69% to 74% pass@1; SmolAgent pass@1 +6%, pass@3 up to 68%. GAIA pass@3 reached 80.61% with Flash-Searcher, surpassing strong multi-agent systems (OWL-Workforce, CK-Pro). Gains of 3.54–5.0% across all three held-out benchmarks.
- **Generalization without re-evolution.** Memory evolved on TaskCraft transferred to WebWalkerQA and xBench unchanged, yielding 2.0–9.09% gains; cross-LLM transfer to Kimi K2 gave +17.06% on WebWalkerQA, +10.0% on TaskCraft; cross-framework transfer worked across heterogeneous scaffolds.
- **Cost-neutral.** MemEvolve maintained API cost near the No-Memory baseline (GAIA: $0.085 vs $0.086; xBench: $0.136 vs $0.141) — gains came from better architecture, not more spend.
- **Emergent design principles.** Evolved systems (named *Riva*, *Cerebra*, *Lightweight*) trended toward increased agentic decision-making in encode/retrieve, hierarchical/multi-level abstraction, and distilling both textual insights and reusable tools with periodic DB maintenance.

## Methods (brief)
Dual-evolution run for Kmax=3 iterations with survivor budget K=1, each parent expanded to S=3 descendants; inner loop evaluates each candidate on 60 trajectories (40 new + 20 reused for stable comparison). GPT-5-Mini backbones both the agent frameworks and the meta-evolution operator; DeepSeek V3.2 and Kimi K2 used to test cross-LLM transfer. Evaluated on GAIA (165 tasks), WebWalkerQA, xBench-DeepSearch (100 tasks), and TaskCraft, with exact-match and LLM-as-Judge protocols.

## Limitations
Meta-evolution is conducted only within a shared task regime (deep-research / web-search style); the authors explicitly concede transfer would likely fail across fundamentally different task families (e.g. embodied action with different action/tool spaces). Only 3 evolutionary iterations with K=1 survivor and S=3 descendants — a narrow search. Benchmark subsets were sampled (e.g. 170 of 680 WebWalkerQA queries), and gains rely partly on LLM-as-Judge evaluation.

## Citations of interest
- **ExpeL** (Zhao et al., 2024) — contrastive-learning memory distilling insights from success/failure trajectories; a baseline component in EvolveLab.
- **Agent Workflow Memory / AWM** (Wang et al., 2024b) — workflow-as-memory abstraction.
- **Dynamic Cheatsheet** (Suzgun et al., 2025) — test-time learning with adaptive memory via skill condensation.
- **Reflexion** (Shinn et al., 2023) — verbal self-reflection memory, the canonical "skillful learner" prior.
- **Flash-Searcher** (Qin et al., 2025) — DAG-based parallel web agent used as the primary integration framework.
- **GAIA** (Mialon et al., 2023) — general AI assistant benchmark used for evaluation.
- **Darwin Gödel Machine** (Zhang et al., 2025e) — open-ended evolution of self-improving agents, conceptual kin to architectural meta-evolution.
