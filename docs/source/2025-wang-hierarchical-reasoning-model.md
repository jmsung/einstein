---
type: source
kind: paper
title: Hierarchical Reasoning Model
authors: Guan Wang, Jin Li, Yuhao Sun, Xing Chen, Chang-Le Liu, Yue Wu, Meng Lu, Sen Song, Yasin Abbasi-Yadkori
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2506.21734
source_local: ../raw/2025-wang-hierarchical-reasoning-model.pdf
topic: general-knowledge
cites:
---

# Hierarchical Reasoning Model

**Authors:** Guan Wang, Jin Li, Yuhao Sun, Xing Chen, Chang-Le Liu, Yue Wu, Meng Lu, Sen Song, Yasin Abbasi-Yadkori  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2506.21734

## One-line
A brain-inspired recurrent architecture with two coupled modules running at different timescales achieves deep latent reasoning from ~1000 training examples without chain-of-thought.

## Key claim
A 27M-parameter HRM trained from scratch on ~1000 samples reaches 40.3% on ARC-AGI-1 (beating o3-mini-high at 34.5% and Claude 3.7/8K at 21.2%), ~55% on Sudoku-Extreme, and ~74.5% on Maze-Hard (30×30) — tasks where leading CoT LLMs score 0%.

## Method
Two coupled recurrent Transformer modules: a slow high-level module $f_H$ and a fast low-level module $f_L$ that updates $T$ times per H-cycle over $N$ cycles, enabling "hierarchical convergence" — $f_L$ converges to a local fixed point conditioned on $z_H$, which then resets it for a new equilibrium. Training uses a one-step gradient approximation (justified by Deep Equilibrium Models + Implicit Function Theorem, $(I-J_F)^{-1} \approx I$), avoiding BPTT with $O(1)$ memory. Adds deep supervision (segmented forward passes with detached states) and Q-learning–based Adaptive Computation Time for halting.

## Result
Near-perfect accuracy on Sudoku-Extreme Full and 30×30 optimal-path mazes (where standard Transformers saturate even at 256+ depth). Demonstrates inference-time scaling: a model trained with $M_{\max}=8$ continues to improve at $M_{\max}=16$. Post-hoc analysis shows emergent dimensionality hierarchy — participation ratio $z_H/z_L \approx 2.98$, matching mouse cortex (~2.25) — only after training, not in random-init controls.

## Why it matters here
General background; no direct arena tie. Possibly relevant as a meta-architectural pattern for the agent's self-improvement loop (slow planner / fast executor separation, adaptive halting via Q-learning) but doesn't inform any specific math-optimization problem (sphere packing, autocorrelation, kissing, etc.).

## Open questions / connections
- Causal necessity of the emergent $z_H$/$z_L$ dimensionality split — only correlational evidence given; intervention experiments left to future work.
- Whether hierarchical memory mechanisms (Clockwork RNN, Hierarchical Sequential Models) combined with HRM's depth could extend to long-context reasoning.
- Extends Universal Transformers (Dehghani 2018) and Deep Equilibrium Models (Bai et al. 2019) by combining recurrence + IFT-based 1-step gradient + adaptive halt.
- Open: whether HRM's "latent reasoning" generalizes to symbolic-search problem families with no obvious grid/sequence structure.

## Key terms
hierarchical reasoning model, HRM, latent reasoning, deep equilibrium model, implicit function theorem, one-step gradient, BPTT alternative, adaptive computation time, Q-learning halting, recurrent Transformer, hierarchical convergence, ARC-AGI, Sudoku, participation ratio, neural collapse, Universal Transformer
