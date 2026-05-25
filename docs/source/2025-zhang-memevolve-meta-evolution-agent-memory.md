---
type: source
kind: paper
title: MemEvolve: Meta-Evolution of Agent Memory Systems
authors: Guibin Zhang, Haotian Ren, Chong Zhan, Zhen Zhou, Junhao Wang, He Zhu, Wangchunshu Zhou, Shuicheng Yan
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2512.18746
source_local: ../raw/2025-zhang-memevolve-meta-evolution-agent-memory.pdf
topic: general-knowledge
cites:
---

# MemEvolve: Meta-Evolution of Agent Memory Systems

**Authors:** Guibin Zhang, Haotian Ren, Chong Zhan, Zhen Zhou, Junhao Wang, He Zhu, Wangchunshu Zhou, Shuicheng Yan  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2512.18746

## One-line
A meta-evolutionary framework that jointly evolves an LLM agent's experiential memory *and* the underlying memory architecture (encode/store/retrieve/manage modules) rather than treating the memory pipeline as static.

## Key claim
Co-evolving memory architecture with memory contents yields up to **17.06%** task-performance gains over fixed self-improving memory baselines (e.g., SmolAgent, Flash-Searcher) and transfers across benchmarks/backbones with 2.0–9.09% gains on unseen evaluations.

## Method
Bilevel optimization: an **inner loop** (first-order) populates each candidate's experience base from agent trajectories under a fixed memory $\Omega_j^{(k)} = (E_j, U_j, R_j, G_j)$; an **outer loop** (second-order) uses an LLM "meta-evolver" to mutate the programmatic implementations of those four modules, ranking candidates on a Pareto front of (task success, token cost, latency). The memory design space is decomposed modularly — Encode, Store, Retrieve, Manage — instantiated as a unified codebase (EvolveLab) that re-implements 12 prior memory systems (Voyager, ExpeL, AWM, Cheatsheet, SkillWeaver, G-Memory, Agent-KB, Memp, EvolveR, …) behind one `BaseMemoryProvider` ABC.

## Result
On four agentic benchmarks (GAIA, WebWalkerQA, xBench-DS, TaskCraft), MemEvolve beats every static memory baseline. Evolved architectures (Lightweight, Riva, Cerebra) show recurring design motifs the human designers did not seed: hierarchical/multi-level abstraction of trajectories, increased agent involvement in encoding (vs passive logging), JSON→graph storage upgrades, and explicit working-memory maintenance for long-horizon tasks. Cross-task evolution on TaskCraft transfers to GAIA/WebWalker/xBench without retraining the architecture.

## Why it matters here
Directly informs the **self-improvement-loop** rule and `docs/agent/` design layer: this paper formalizes "agent that evolves not just its experience but its learning mechanism," which is exactly the question behind cycle-log + skill-library + promotion-log. The Encode/Store/Retrieve/Manage decomposition is a candidate ontology for refactoring how the einstein agent thinks about its wiki + qmd + failure-finding pipeline. No direct math-content tie (no arena problem), but high methodological relevance to the autonomous-loop branch.

## Open questions / connections
- Can the "12 memory architectures as genotype + meta-evolver" framing be applied to evolve einstein's *wiki schema* (concepts/findings/questions/personas/techniques) rather than a fixed taxonomy?
- The Pareto signal here is (success, tokens, latency) — what is the analogue for a math-wisdom-accumulating agent (top-3 rate, cite-coverage, gap-closure rate)?
- Relation to Darwin-Gödel Machine (Zhang et al. 2025e) and Alita (Qiu et al. 2025b) — both cited as architecture-level self-improvement; is meta-evolving the *protocol* (math-solving-protocol.md) the next step beyond meta-evolving the memory?
- Anti-pattern risk: agent-driven memory churn without honesty constraints (cf. cycle-discipline.md "no cherry-picking") — the paper does not address whether the evolved architectures over-fit to the inner-loop benchmark set.

## Key terms
agent memory, meta-evolution, bilevel optimization, self-improving agents, ExpeL, Voyager, SkillWeaver, AgentKB, Pareto ranking, encode-store-retrieve-manage, LLM agents, EvolveLab, MemEvolve, autonomous loop, architectural evolution
