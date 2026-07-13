<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, sci-math, ai-reasoning]
title: "LLM-Feynman: Leveraging Large Language Models for Universal Scientific Formula and Theory Discovery"
authors: [Zhilong Song, Qionghua Zhou, Chunjin Ren, Chongyi Ling, Minggang Ju, Jinlan Wang]
year: 2025
source_url: https://arxiv.org/abs/2503.06512
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
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

## Key terms
symbolic regression, large language models, Monte Carlo tree search, Pareto frontier, multi-objective optimization, self-evaluation, Feynman lectures benchmark, AI-Feynman, SISSO, PySR, interpretability score, UCB, mutual information feature selection, formula discovery
