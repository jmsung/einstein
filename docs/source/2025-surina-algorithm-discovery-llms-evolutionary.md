---
type: source
kind: paper
title: "Algorithm Discovery With LLMs: Evolutionary Search Meets Reinforcement Learning"
authors: Anja Surina, Amin Mansouri, Lars Quaedvlieg, Amal Seddas, Maryna Viazovska, Emmanuel Abbe, Caglar Gulcehre
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2504.05108
source_local: ../raw/2025-surina-algorithm-discovery-llms-evolutionary.pdf
topic: general-knowledge
cites:
---

# Algorithm Discovery With LLMs: Evolutionary Search Meets Reinforcement Learning

**Authors:** Anja Surina, Amin Mansouri, Lars Quaedvlieg, Amal Seddas, Maryna Viazovska, Emmanuel Abbe, Caglar Gulcehre  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2504.05108

## One-line
EvoTune augments FunSearch-style LLM evolutionary program search by RL-fine-tuning the generator LLM in-loop on its own evaluation feedback, accelerating discovery of combinatorial-optimization heuristics.

## Key claim
Tightly coupling evolutionary program search with off-policy DPO updates of the generator LLM (using forward-KL regularization to preserve output diversity) consistently outperforms a static-LLM FunSearch baseline on bin packing, TSP, flatpack, Hash Code, and symbolic regression — e.g. bin-packing optimality gap drops from $5.37$ (best-fit human heuristic) to $2.96$ (FunSearch) to $2.06$ (EvoTune, Phi 3.5), and EvoTune's TSP heuristic at $t_{\max}=1000$ achieves the best average gap ($0.32$) across 29 TSPLib instances vs LEHD $1.92$, KGLS $0.36$, NeuralGLS $0.96$.

## Method
A program database $D_t$ (island-structured, à la FunSearch) is grown by sampling prompts $x_t$ = (best programs $\oplus$ CoT task description), generating $K$ candidates from $\pi_{\theta_{t-1}}$, evaluating them on validation instances, and storing $(x_t, y_{t,k}, r(y_{t,k}))$. Every $f_{RL}$ iterations, preference pairs $(x_t, y^+_n, y^-_n)$ are built by splitting valid outputs at the median reward (plus valid-vs-failed pairs) and threshold-filtered; DPO with **forward**-KL $f'(u)=-1/u$ and high $\beta$ (re-initialized from base $\pi_{\theta_0}$ each round) updates the LLM. Forward KL is chosen over reverse KL to keep mass-covering behavior and avoid mode collapse that would kill evolutionary diversity.

## Result
Across three open LLMs (Llama-3.2-1B, Phi-3.5-Mini, Granite-3.1-2B) and three core tasks, EvoTune lowers top-50 mean optimality gap over FunSearch at every sampling budget (9.6k / 16k / 22.4k programs), with the gap widening as more samples accumulate — e.g. Phi/BP test set $3.99 \to 3.38 \to 2.80$ vs FunSearch $3.99 \to 3.42 \to 3.19$; Granite/TSP validation $2.565 \to 2.504$ vs $2.565 \to 2.534$. EvoTune also produces strictly more uniquely-scoring programs (proxy for search diversity) and shifts the score histogram further into the high-reward tail. An ablation shows forward-KL DPO beats reverse-KL DPO and beats a ReSTEM-style SFT-on-top-percentile alternative across three learning rates.

## Why it matters here
General background for the autonomous-loop agent itself: the Einstein Arena agent is structurally a FunSearch-descendant (program/finding database $\to$ LLM sampler $\to$ evaluator $\to$ wiki feedback). EvoTune is direct evidence that **in-weight RL on the generator** (DPO with forward-KL, off-policy, periodic resets to base) is a strict improvement over a static prompt-only generator, and that **forward KL** is the regularizer of choice when downstream search needs output diversity — both directly relevant to how the agent should self-improve over cycles. No direct math-content tie to the 23 arena problems, but Viazovska is a co-author and the framework is the closest analog in the literature to this repo's compounding-wiki loop.

## Open questions / connections
- Can EvoTune be transplanted to the einstein loop where the "program" is a wiki finding / strategy plan rather than a Python heuristic, with reward = arena verifier or triple-verify agreement?
- Forward-KL DPO with high $\beta$ vs reverse-KL — does diversity preservation generalize beyond combinatorial-heuristic synthesis to mathematical-finding generation?
- Hybrid SFT-then-DPO and full PPO/GRPO comparisons are left open; ReSTEM is sensitive to LR but cheaper than DPO.
- Cross-dimensional / out-of-distribution generalization of evolved heuristics (validation-perturbed and TSPLib results suggest robustness, but the agent's wiki demands generalization across problem families — untested here).
- Connects to: FunSearch (Romera-Paredes 2024), DPO (Rafailov 2024), ReSTEM (Singh 2023), Bitter Lesson (Sutton 2019), AlphaTensor/AlphaGo lineage of search+learning.

## Key terms
EvoTune, FunSearch, LLM evolutionary search, DPO, direct preference optimization, forward KL regularization, reverse KL mode collapse, off-policy RL, island-based program database, Chain-of-Thought prompting, bin packing, traveling salesman problem, flatpack, Guided Local Search, ReSTEM, Viazovska, algorithm discovery, output diversity, optimality gap, Bitter Lesson, self-improving agent loop
