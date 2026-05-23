---
type: source
kind: paper
title: "LLM-Feynman: Leveraging Large Language Models for Universal Scientific Formula and Theory Discovery"
authors: Zhilong Song, Qionghua Zhou, Chunjin Ren, Chongyi Ling, Minggang Ju, Jinlan Wang
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2503.06512
source_local: ../raw/2025-song-llm-feynman-leveraging-large-language.pdf
topic: general-knowledge
cites:
---

# LLM-Feynman: Leveraging Large Language Models for Universal Scientific Formula and Theory Discovery

**Authors:** Zhilong Song, Qionghua Zhou, Chunjin Ren, Chongyi Ling, Minggang Ju, Jinlan Wang  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2503.06512

## One-line
A framework that couples LLM-driven symbolic regression with self-evaluation and Monte Carlo tree search to extract concise, interpretable formulas from data plus domain knowledge.

## Key claim
LLM-Feynman rediscovers >90% of 120 formulas from Feynman's Lectures (100% on simple/no-noise, 86% at $10^{-2}$ noise on simple, 90% at $10^{-2}$ noise on the 20-formula hard set), outperforming AI-Feynman (85→67→55%), and surpasses SISSO/PySR in $R^2$/MAE at comparable complexity on materials tasks.

## Method
Three-module pipeline: (1) automated feature engineering via Automatminer + mutual-information screening, with LLM-suggested physically meaningful descriptors; (2) LLM-based symbolic regression generating Python-function candidates iteratively, scored by a loss $L = \alpha N(E) + \beta N(C) + \gamma S$ combining error $E$, complexity $C$, and an LLM self-evaluation interpretability score $S \in [0,1]$, with Pareto-frontier selection over ~500 iterations; (3) MCTS over LLM-generated interpretive hypotheses, scored by UCB, to refine formula explanations. Tested with Falcon-Mamba-7B, ChemLLM-20B, LLaMA3-8B.

## Result
On Feynman benchmarks: 100/100 simple and 18/20 hard formulas recovered at moderate noise. On materials applications: 2D-material synthesizability classification at acc=0.93, F1=0.94 (vs 0.60/0.57 using $E_\text{hull}$ alone); perovskite synthesizability at perfect 1.00 on test set; ionic conductivity regression $R^2=0.855$, MAE=0.673 (in $\log_{10}\sigma$); GW bandgap of 2D materials $R^2=0.80$, MAE=0.429 eV. Ablations show domain-knowledge embedding cuts complexity, and self-evaluation lifts accuracy without complexity inflation.

## Why it matters here
General background; no direct arena tie. The relevant transferable idea for the Einstein Arena loop is the multi-objective Pareto scoring (error + complexity + LLM-judged interpretability) plus MCTS-guided explanation refinement — a template for how an LLM council could propose, score, and iterate candidate ansätze for closed-form bounds in problems like P15/P16 equioscillation, Cohn–Elkies magic functions, or autocorrelation kernels.

## Open questions / connections
- Can the loss-function self-evaluation $S$ be replaced or augmented by a *verifier*-grounded signal (analogous to triple-verify) to avoid LLM sycophancy on interpretability?
- LLM-from-scratch feature engineering underperforms Automatminer+MI — suggests human-curated descriptor libraries remain essential; analogue for arena: persona-curated parameterization libraries beat free-form LLM ansatz generation.
- Token-length bottleneck limits to ~$10^4$ samples; hierarchical / RLHF extensions proposed but unimplemented.

## Key terms
symbolic regression, large language models, Monte Carlo tree search, Pareto frontier, multi-objective optimization, self-evaluation, Feynman lectures benchmark, AI-Feynman, SISSO, PySR, interpretability score, UCB, mutual information feature selection, formula discovery
