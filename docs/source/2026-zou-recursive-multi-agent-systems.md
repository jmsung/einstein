---
type: source
kind: paper
title: Recursive Multi-Agent Systems (RecursiveMAS)
authors: Jiaru Zou et al.
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2604.25917
source_local: ../raw/2026-zou-recursive-multi-agent-systems.pdf
topic: agentic-harness
cites: 
---

# Recursive Multi-Agent Systems (RecursiveMAS)

**Authors:** Jiaru Zou et al.  ·  **Year:** 2026  ·  **Source:** https://arxiv.org/abs/2604.25917

## One-line
A framework that turns a multi-agent LLM system into a recursive latent-space computation, with heterogeneous agents looped together via lightweight residual projection modules ("RecursiveLink") and trained by an inner-outer loop algorithm.

## Key claim
Across 9 benchmarks (math, science, medicine, search, code), RecursiveMAS averages +8.3% accuracy over single/multi-agent and recursive-LM baselines while delivering 1.2×–2.4× end-to-end inference speedup and 34.6%–75.6% token reduction; theory shows lower runtime complexity and stable gradient flow vs text-mediated MAS.

## Method
Each agent generates "latent thoughts" by feeding its last-layer hidden state $h_t$ back as the next input via an *inner* RecursiveLink $R_{in}(h)=h+W_2\sigma(W_1 h)$ (GELU + residual). Cross-agent transfer uses an *outer* RecursiveLink $R_{out}(h)=W_3 h+W_2\sigma(W_1 h)$ to project source-agent embeddings into the target's input space; agents are chained $A_1\to A_2\to\cdots\to A_N\to A_1$ for $n$ recursion rounds, with only the last round decoding text. Training is inner-loop (per-agent regression warm-start of $R_{in}$) then outer-loop (cross-entropy with gradients backpropagated through all recursion rounds), with base LLMs frozen — only the RecursiveLinks are updated.

## Result
On Distillation-Style MAS the Learner+RecursiveMAS beats the Learner alone by ~+8% (e.g., AIME2026 76.7→83.3, GPQA-D 61.4→70.0, MedQA 77.9→83.0) at ~1.5× the Expert's speed. On Mixture-Style it beats every specialist (e.g., MedQA 48.1→61.7, GPQA-D 37.4→43.0); on Deliberation-Style it beats Reflector+Tool-Caller (AIME2026 90.0, Bamboogle 53.7). Ablation: accuracy improves monotonically with latent-thought length $m$ and saturates near $m\approx 80$.

## Why it matters here
General background; no direct arena tie. Tangential interest only as engineering for the council-dispatch/self-improvement loop — recursive latent collaboration is a possible architecture if the einstein agent ever moves from text-passing subagents to latent-state agents, but it informs no specific arena problem (sphere packing, kissing, autocorrelation, etc.).

## Open questions / connections
- Does latent-space collaboration preserve faithfulness/auditability needed for triple-verify and wiki-attribution? Frozen-base + projection-only training avoids weight drift but hides reasoning from human review.
- Extends recursive/looped LMs (LoopLM, Ouro-2.6B) and latent-interface MAS (Du 2025, Zheng 2025, Zou 2025) — RecursiveLink is a minimal cross-architecture adapter worth noting if heterogeneous-model coordination is ever attempted.
- Open: scaling laws for deeper recursion beyond ~80 latent steps; whether the +8.3% gain holds on harder math (research-level olympiad) where the constituent agents are already near-ceiling.

## Key terms
recursive language model, looped LM, multi-agent system, latent-space reasoning, RecursiveLink, residual projection, inner-outer loop training, chain-of-agents, mixture-of-agents, knowledge distillation, tool-augmented deliberation, heterogeneous LLM agents
