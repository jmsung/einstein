---
type: source
kind: paper
title: A review of large language models and autonomous agents in chemistry
authors: M. C. Ramos, C. Collison, Andrew D. White
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2407.01603
source_local: ../raw/2024-ramos-review-large-language-models.pdf
topic: general-knowledge
cites:
---

# A review of large language models and autonomous agents in chemistry

**Authors:** M. C. Ramos, C. Collison, Andrew D. White  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2407.01603

## One-line
Survey of how transformer-based LLMs and LLM-driven autonomous agents are being applied across chemistry — molecule design, property prediction, synthesis planning, and lab automation.

## Key claim
LLMs (encoder-only, decoder-only, encoder-decoder, multi-modal) plus agent scaffolding (memory, planning, profiling, perception, tools) are reshaping cheminformatics; the bottleneck is no longer architecture but data quality, interpretability, standard benchmarks, and safe integration with experiment.

## Method
Narrative review. Section 2 reviews transformer mechanics (attention, positional encoding, tokenization, context window) and training pipeline (self-supervised pretrain → instruct fine-tune → RLHF/DPO/PPO/REINFORCE alignment). Section 3 maps architecture → chemistry task (encoder-only → property prediction; decoder-only → inverse design; encoder-decoder → reaction/synthesis prediction). Sections 4–5 dissect agent module anatomy and survey deployed systems (ChemCrow, Coscientist, ChatMOF, CRISPR-GPT, PaperQA, ChemReasoner, ProtAgents, BioPlanner, CACTUS, etc.).

## Result
No new theorem — taxonomic synthesis. Frames four chemistry challenges (property prediction, property-directed generation, synthesis prediction, automation), estimates the stable-chemical search space at up to $10^{180}$, and categorizes ~150 LLM/agent systems by architecture and task. Identifies that BERT-style bidirectional encoding (MLM + NSP) underpins most property-prediction Mol-LLMs, while RLHF/DPO is the dominant alignment route. Catalogs RL variants (PPO, REINFORCE, RLSF) and reward-free methods (DPO, RRHF, PRO) as active competitors.

## Why it matters here
General background; no direct arena tie. Useful only as scaffolding for the meta-question of how the Einstein Arena agent itself is built — agent module decomposition (memory/planning/profiling/perception/tools), context-window limits, RAG patterns (PaperQA, WikiCrow), and the agent-authored-content honesty problem that motivates the wiki-attribution rule. No content on sphere packing, kissing numbers, autocorrelation, or any math-optimization problem class.

## Open questions / connections
- How to align LLM agents on non-differentiable downstream scientific metrics (Bou et al., Hayes et al.) — relevant to wiring an agent against arena scores.
- Hallucination + safeguarding tradeoff for autonomous scientific agents (Tang et al. 2024, Ruan et al. sandbox) — informs cycle-discipline rule design.
- Benchmark scarcity: no standard "did the agent improve" metric across cycles, paralleling the `docs/agent/cycle-log.md` honesty-check problem.

## Key terms
large language model, transformer, attention mechanism, encoder-only, decoder-only, encoder-decoder, BERT, RLHF, DPO, PPO, autonomous agent, ChemCrow, Coscientist, SMILES, retrieval-augmented generation, agent memory, agent planning, tool use, property prediction, inverse design, synthesis prediction, hallucination, chemistry automation, Mol-LLM
