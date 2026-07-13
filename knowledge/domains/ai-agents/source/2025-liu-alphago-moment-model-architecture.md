<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-ml]
title: AlphaGo Moment for Model Architecture Discovery
authors: [Yixiu Liu, Yang Nan, Weixiang Xu, Xiangkun Hu, Lyumanshan Ye, Zhen Qin, Pengfei Liu]
year: 2025
source_url: https://arxiv.org/abs/2507.18074
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# AlphaGo Moment for Model Architecture Discovery

**Authors:** Yixiu Liu, Yang Nan, Weixiang Xu, Xiangkun Hu, Lyumanshan Ye, Zhen Qin, Pengfei Liu  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2507.18074

## One-line
A multi-agent LLM system (ASI-ARCH) autonomously hypothesizes, codes, trains, and evaluates neural architectures, discovering 106 SOTA linear-attention variants over 1,773 experiments and 20,000 GPU-hours.

## Key claim
Architectural discovery obeys an empirical scaling law: the cumulative count of discovered SOTA architectures grows linearly with compute hours, shifting AI research from human-bandwidth-bound to compute-bound.

## Method
Closed-loop evolutionary framework with four modules — Researcher (proposes + codes architectures from top-50 seed pool with two-tier sampling), Engineer (trains in a real code env with self-revision and timeout-killing), Analyst (writes ablation-style postmortems), and Cognition Base (distilled human-literature priors). Selection uses a composite fitness $\text{Fitness} = \tfrac{1}{3}[\sigma(\Delta\text{loss}) + \sigma(\Delta\text{benchmark}) + \text{LLM}_{\text{judge}}]$ to resist reward hacking. A two-stage explore-then-verify protocol scales promising small-model candidates to larger validation runs.

## Result
1,773 autonomous experiments produced 106 novel linear-attention architectures (DeltaNet derivatives) that outperform human-designed baselines on reasoning, language-understanding, and structured-extraction benchmarks. Cumulative SOTA-count vs GPU-hours is strikingly linear (Fig. 1). The discovered architectures exhibit emergent design motifs — gated/decay variants, hierarchical/fractal memory, spectral/Fourier mixers, RoPE-state hybrids — clustered into ~5 family branches across 10 generations.

## Key terms
neural architecture search, ASI-ARCH, linear attention, DeltaNet, evolutionary search, multi-agent LLM, composite fitness, reward hacking, LLM-as-judge, scaling law for discovery, self-improving systems, AlphaEvolve, Darwin-Gödel machine, cognition base, autonomous research loop
