---
type: source
kind: paper
title: Learning to Continually Learn via Meta-learning Agentic Memory Designs
authors: Yiming Xiong, Shengran Hu, Jeff Clune
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2602.07755
source_local: ../raw/2026-xiong-learning-continually-learn-meta-learning.pdf
topic: general-knowledge
cites: 
---

# Learning to Continually Learn via Meta-learning Agentic Memory Designs

**Authors:** Yiming Xiong, Shengran Hu, Jeff Clune  ·  **Year:** 2026  ·  **Source:** https://arxiv.org/abs/2602.07755

## One-line
ALMA uses a Meta Agent to search code-space for agent memory designs (databases + update/retrieve logic), replacing hand-crafted memory modules with learned ones that better support continual learning.

## Key claim
Meta-learned memory designs outperform four state-of-the-art human-crafted baselines (Trajectory Retrieval, ReasoningBank, Dynamic Cheatsheet, G-memory) on all four sequential decision-making benchmarks (ALFWorld, TextWorld, Baba Is AI, MiniHack), and transfer from the GPT-5-nano training agent to a stronger GPT-5-mini deployment agent.

## Method
A Meta Agent (GPT-5) iteratively samples designs from an archive with probability roughly proportional to success rate and inversely proportional to sample count (DGM-style), reflects on logs to ideate, codes a new memory design against a Python abstract-class interface (`general_update`/`general_retrieve` with composable sub-modules holding their own databases), debugs up to 3× on runtime errors, then evaluates via a two-phase protocol: Memory Collection Phase (build memory, no retrieval) followed by Deployment Phase (static or dynamic mode, success-rate scored over 3 runs). Tools provided to designs include GPT-4o-mini, GPT-4.1, and text-embedding-3-small.

## Result
Across 11 learning steps producing 43 designs, learned memory beat all four baselines on every benchmark under both GPT-5-nano and GPT-5-mini deployment agents (relative gains over no-memory baseline color-coded in Table 1, but no-memory itself is e.g. 2.9% ALFWorld / 5.4% TextWorld / 9.5% Baba Is AI / 6.7% MiniHack). Learned designs are also more cost-efficient than most baselines, scale better with memory size, and adapt faster under task-distribution shift. Ablation: open-ended exploration beats greedy top-K selection.

## Why it matters here
General background; no direct arena tie. The closest connection is to einstein's own self-improvement loop (gap→search→ingest→distill→page) and council-dispatch architecture — ALMA is evidence that *code-as-search-space* meta-learning of memory mechanisms outperforms hand-crafted ones, which could inform future automated tuning of the wiki's retrieve/update interfaces (currently qmd + handcrafted rules).

## Open questions / connections
- Extends ADAS (Hu et al. 2025) and DGM (Zhang et al. 2025e) from agentic-system search to memory-specific search; concurrent with Zhang et al. 2025d (which seeds from handcrafted designs rather than searching from scratch).
- All experiments are token-level memory; parametric and latent memory are flagged but unexplored.
- No theoretical analysis of why open-ended > greedy beyond empirical ablation; no transferability test across *domains* (only across FMs within one domain).

## Key terms
meta-learning, agentic memory, continual learning, foundation models, code search space, open-ended exploration, ADAS, DGM, ReasoningBank, G-memory, Dynamic Cheatsheet, ALFWorld, TextWorld, MiniHack, Baba Is AI, Clune AI-generating algorithms
