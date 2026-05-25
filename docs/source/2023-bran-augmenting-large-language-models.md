---
type: source
kind: paper
title: Augmenting large language models with chemistry tools
authors: Andrés M Bran, Sam Cox, Oliver Schilter, Carlo Baldassari, Andrew D. White, P. Schwaller
year: 2023
author: agent
drafted: 2026-05-24
ingested_at: 2026-05-24
source_type: arxiv
source_url: https://arxiv.org/abs/2304.05376
source_local: ../raw/2023-bran-augmenting-large-language-models.pdf
topic: general-knowledge
cites:
---

# Augmenting large language models with chemistry tools

**Authors:** Andrés M Bran, Sam Cox, Oliver Schilter, Carlo Baldassari, Andrew D. White, P. Schwaller  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2304.05376

## One-line
Builds ChemCrow, a GPT-4 agent wired to 18 expert-designed chemistry tools that plans and executes organic syntheses, drug-discovery loops, and materials-design tasks via a ReAct/MRKL Thought–Action–Observation loop.

## Key claim
Augmenting an LLM with domain tools and a chain-of-thought tool-use loop turns a hallucination-prone generator into a usable chemistry reasoner that outperforms bare GPT-4 on expert-rated factuality/reasoning, and the agent autonomously synthesized DEET, three thiourea organocatalysts (Schreiner, Ricci, Takemoto), and guided discovery of a novel chromophore with measured $\lambda_{\max} \approx 336$ nm vs target 369 nm.

## Method
ReAct-style scaffold (Thought → Action → Action Input → Observation, iterated) implemented via LangChain over GPT-4 (temperature 0.1), with 18 tools spanning web/literature search, molecule tools (Name2SMILES, property predictors, safety/controlled-substance filters), reaction tools (RXN forward/retro prediction, Vaucher procedure inference), and a ReactionExecute hookup to the IBM RoboRXN cloud lab plus an ActionCleaner that iteratively repairs invalid robotic procedures. Evaluation uses both an "EvaluatorGPT" judge and a four-chemist expert panel scoring correctness, reasoning, and task completion across 14 tasks, with response anonymisation and style-masking to remove ReAct fingerprints.

## Result
On expert ratings, ChemCrow dominates bare GPT-4 on harder synthesis, molecular-design, and chemical-logic tasks, while GPT-4 only wins on memorisable easy targets (paracetamol, aspirin, DEET); the random-forest chromophore screen achieved RMSE $\approx 37$ nm. A notable negative finding: GPT-4-as-judge prefers GPT-4's fluent hallucinations to ChemCrow's tool-grounded answers, inverting the expert ranking — LLM self-evaluation fails when factuality matters.

## Why it matters here
General background; no direct arena tie — this is an LLM-agent / tool-use paper, not a math-optimization paper. The transferable lessons are (a) tool-augmented ReAct loops vs bare-model reasoning, (b) the demonstrated failure of LLM-judge evaluators on fact-critical tasks (relevant to any council-dispatch or auto-grading scheme), and (c) safety/guardrail patterns for autonomous agents.

## Open questions / connections
- LLM-as-judge unreliability when ground truth requires domain expertise — argues for the project's expert/triple-verify discipline over agent self-grading.
- Reproducibility of closed-source LLM agents (5 reruns of the same task diverged in interpretation) — relevant to cycle-discipline replay claims.
- Tool quality bounds agent quality: retrosynthesis ceiling = underlying retro tool's ceiling, mirroring the optimizer/evaluator ceiling in arena work.

## Key terms
ChemCrow, LLM agent, GPT-4, ReAct, MRKL, chain-of-thought, tool use, LangChain, retrosynthesis, RoboRXN, organocatalyst, chromophore discovery, LLM-as-judge, hallucination, autonomous synthesis
