---
type: source
kind: paper
title: AlphaGo Moment for Model Architecture Discovery
authors: Yixiu Liu, Yang Nan, Weixiang Xu, Xiangkun Hu, Lyumanshan Ye, Zhen Qin, Pengfei Liu
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2507.18074
source_local: ../raw/2025-liu-alphago-moment-model-architecture.pdf
topic: general-knowledge
cites:
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

## Why it matters here
General background; no direct arena tie — but the methodology is directly transferable to einstein's self-improvement loop: composite fitness (quant + LLM-judge) resists reward hacking; iterative debug-and-retry beats AST-discard; cognition-base + seed-pool + on-the-fly summarization parallels einstein's wiki-first + council dispatch pattern. The scaling-law-for-discovery framing legitimizes the cycle-log/skill-library honesty layer as the right measurement substrate.

## Open questions / connections
- Does the linear scaling law hold beyond linear-attention into combinatorial search spaces (e.g., LP/SDP code variants for sphere packing)?
- How to port the "Researcher + Engineer + Analyst + Cognition" decomposition to math-optimizer evolution where the artifact is a parameter configuration, not a forward-pass module?
- Extends AlphaEvolve / Darwin-Gödel-machine line; leaves open whether emergent design patterns generalize across task domains or are linear-attention-specific.
- The novelty-check (embedding sim + LLM judge) and timeout-killing are concrete primitives einstein's autonomous loop currently lacks.

## Key terms
neural architecture search, ASI-ARCH, linear attention, DeltaNet, evolutionary search, multi-agent LLM, composite fitness, reward hacking, LLM-as-judge, scaling law for discovery, self-improving systems, AlphaEvolve, Darwin-Gödel machine, cognition base, autonomous research loop
