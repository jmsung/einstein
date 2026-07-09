---
type: source
kind: paper
title: "ProtAgents: protein discovery via large language model multi-agent collaborations combining physics and machine learning"
authors: Alireza Ghafarollahi, Markus J. Buehler
year: 2024
author: agent
drafted: 2026-05-24
ingested_at: 2026-05-24
source_type: arxiv
source_url: https://arxiv.org/abs/2402.04268
source_local: ../raw/2024-ghafarollahi-protagents-protein-discovery-large.pdf
topic: general-knowledge
cites:
---

# ProtAgents: protein discovery via large language model multi-agent collaborations combining physics and machine learning

**Authors:** Alireza Ghafarollahi, Markus J. Buehler  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2402.04268

## One-line
Introduces ProtAgents, a GPT-4-driven multi-agent framework where specialized LLM agents (planner, assistant, critic, user_proxy) collaborate via group chat to solve de novo protein design and analysis tasks by orchestrating physics simulators, generative diffusion models, fine-tuned transformers, and retrieval tools.

## Key claim
A team of role-specialized LLM agents coordinated by a chat manager can autonomously decompose multi-step protein tasks — knowledge retrieval, structure folding (OmegaFold), secondary-structure analysis (DSSP), normal-mode frequency computation (elastic network model via ProDy), and conditional/unconditional protein generation (Chroma diffusion) — into correctly-ordered subtasks, execute the right tools with appropriate parameters, and self-correct via critic feedback, with little human intervention.

## Method
A multi-agent system built on AutoGen-style group chat: four agents (user_proxy, planner, assistant, critic) each with distinct profile prompts share a tool library exposed to the assistant. Tools wrap external models — Chroma denoising diffusion for de novo backbone generation, OmegaFold for sequence→structure, DSSP for secondary structure, an anisotropic elastic network model for vibrational normal modes, a fine-tuned transformer for mechanical property prediction, and a LlamaIndex-based RAG retriever over scientific literature. A chat manager dynamically selects speakers; the planner proposes function calls, the critic audits parameters, the assistant executes.

## Result
Demonstrated on three experiments: (i) retrieving experimentally-studied protein names, fetching PDB ids, then conditionally analyzing secondary structure / first 13 natural frequencies / CATH class for proteins with sequence length < 128 — agents correctly enforce the conditional and produce a CSV summary; (ii) generating de novo sequences with Chroma, folding with OmegaFold, and comparing structural / frequency content between Chroma and OmegaFold outputs; (iii) targeted design with mechanical property constraints integrated via physics simulations. The system shows error recovery (e.g., regenerating malformed JSON for CSV export) and persistent memory across long multi-turn conversations.

## Why it matters here
General background; no direct arena tie. The paper's relevance is methodological — it is a concrete example of an LLM multi-agent loop (planner / assistant / critic / user_proxy) coordinating physics tools and generative models autonomously, which parallels the einstein agent's council-dispatch + self-improvement-loop architecture for math optimization. The math problems themselves (sphere packing, kissing numbers, autocorrelation) are unrelated to protein design.

## Open questions / connections
- Can a planner/assistant/critic role split improve council-dispatch in the einstein agent vs persona-only dispatch, particularly for tool-execution discipline (the "assistant double-checking parameters" pattern)?
- The paper's RAG retriever returned wrong PDB ids without the agents noticing — what verification analog protects the einstein agent when wiki-first-lookup retrieves a hallucinated finding? Connects to triple-verify and wiki-attribution rules.
- Extends prior MechAgents (Ni & Buehler 2023) and MechGPT (Buehler 2023) multi-agent work; suggests the multi-agent pattern generalizes across physics-heavy domains and is worth comparing to single-agent ReAct loops on the same task set.

## Key terms
multi-agent LLM, GPT-4, AutoGen, planner-critic-assistant pattern, retrieval-augmented generation, de novo protein design, Chroma diffusion, OmegaFold, DSSP secondary structure, elastic network model normal modes, ProDy, group chat manager
