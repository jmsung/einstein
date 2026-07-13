<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, sci-chem]
title: "LLMatDesign: Autonomous Materials Discovery with Large Language Models"
authors: [Shuyi Jia, Chao Zhang, V. Fung]
year: 2024
source_url: https://arxiv.org/abs/2406.13163
drive_file_id: 1B6yyfwarwj5dXUfNnSVMooM37jISG4wL
text_source: paperclip
ingested_by: agent
---

# LLMatDesign: Autonomous Materials Discovery with Large Language Models

**Authors:** Shuyi Jia, Chao Zhang, V. Fung  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2406.13163

## One-line
An LLM-driven closed-loop agent (GPT-4o / Gemini-1.0-pro) proposes discrete composition edits to crystal structures, evaluates them with ML surrogates, and self-reflects to reach target material properties without task-specific training.

## Key claim
With modification history + self-reflection, GPT-4o reaches a 1.4 eV band-gap target in an average of **10.8 modifications** vs **27.4** for random search, and attains average formation energy **−1.97 eV/atom** vs **−0.05** random (DFT-validated **−2.31 eV/atom** vs **−1.51** random, with 73.3% vs 40.0% DFT job success).

## Method
A loop of: LLM proposes one of four discrete edits (add / remove / substitute / exchange) on an `ase.Atoms` object along with a natural-language hypothesis; a TorchMD-Net MLFF relaxes the structure; a TorchMD-Net MLPP predicts the target property; if outside a 10% tolerance, the LLM writes a self-reflection appended to a history message that conditions the next prompt. Modifications continue up to a budget $N$ (50). The framework is model-agnostic and zero-shot — only the prompt changes per task.

## Result
On 10 random Materials Project starting materials × 30 runs: history variants strictly dominate historyless and random on both tasks; without history, GPT-4o oscillates between repeated modifications (zig-zag band-gap traces) indicating diversity collapse. Element-frequency heatmaps show LLM proposals concentrate on first-four-row chemistries, avoid noble gases (GPT-4o) and actinides — i.e., the LLM enforces chemical-validity priors that uniform random sampling lacks. Self-reflection (only run for GPT-4o) is identified qualitatively as the key driver of convergence speed.

## Key terms
LLM agent, autonomous discovery, self-reflection, in-context history, zero-shot decision-making, discrete action space, surrogate-evaluator loop, materials design, band gap, formation energy, GPT-4o, Gemini-1.0-pro, MLFF, closed-loop optimization
