<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, sci-chem, ai-foundation-models]
title: A review of large language models and autonomous agents in chemistry
authors: [M. C. Ramos, C. Collison, Andrew D. White]
year: 2024
source_url: https://arxiv.org/abs/2407.01603
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
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

## Key terms
large language model, transformer, attention mechanism, encoder-only, decoder-only, encoder-decoder, BERT, RLHF, DPO, PPO, autonomous agent, ChemCrow, Coscientist, SMILES, retrieval-augmented generation, agent memory, agent planning, tool use, property prediction, inverse design, synthesis prediction, hallucination, chemistry automation, Mol-LLM
