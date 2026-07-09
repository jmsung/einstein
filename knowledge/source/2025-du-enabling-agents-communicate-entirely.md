---
type: source
kind: paper
title: Enabling Agents to Communicate Entirely in Latent Space
authors: Zhuoyun Du, Runze Wang, Huiyu Bai, Zouying Cao, Xiaoyong Zhu, Bo Zheng, Wei Chen, Haochao Ying
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2511.09149
source_local: ../raw/2025-du-enabling-agents-communicate-entirely.pdf
topic: general-knowledge
cites:
---

# Enabling Agents to Communicate Entirely in Latent Space

**Authors:** Zhuoyun Du, Runze Wang, Huiyu Bai, Zouying Cao, Xiaoyong Zhu, Bo Zheng, Wei Chen, Haochao Ying  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2511.09149

## One-line
Interlat lets two LLM agents communicate by directly passing last-layer hidden states (instead of decoded tokens), then compresses those latent messages to as few as 8 vectors while preserving task performance.

## Key claim
Latent-space inter-agent communication beats both fine-tuned CoT and no-communication baselines on ALFWorld (e.g. 70.48% vs 64.29% / 62.14% seen-task success on Qwen2.5-7B) and on MATH Level-5 (15.80% vs 15.05% CoT), and compressed 8-token latents retain ~94% of full-length performance with up to 24× inference speedup.

## Method
Sender's last hidden states $H = [h_1,\dots,h_L] \in \mathbb{R}^{L\times d}$ over its generated message are routed through a light self-attention + projection adapter and spliced into the receiver's embedding sequence between `<bop>`/`<eop>` markers. Training combines (i) task cross-entropy $L_{\text{task}}$, (ii) a Jensen–Shannon **conditional thought separation** loss against mismatched latents from other tasks, and (iii) a KL+cosine **plan-aligned regulation** loss against the language-space CoT plan, with a stochastic token↔latent **curriculum** (replacement rate $r\in\{0,0.1,\dots,1\}$) to stabilize learning. Compression trains a separate reasoning model $M_\phi$ that autoregresses latents end-to-end (feeding $h_i$ back via a projector) under frozen-actor supervision with $L_{\text{task}} + L_{\text{pref}}$ (uncertainty-weighted KL between full- and compressed-latent actor distributions) $+ L_{\text{geom}}$ (cosine alignment of step-averaged actor-side features).

## Result
Across Qwen2.5-7B/0.5B and LLaMA3.1-8B backbones on ALFWorld, Interlat improves seen-task success by ~6–11 points over CoT-full and ~6–14 over no-comm, and crucially **cross-family** (Qwen sender → LLaMA actor) gives the largest gain (70.95% seen / 71.39% unseen). Structured perturbations (CrossTask, covariance-matched Gaussians, random rotations, white noise) all degrade performance, confirming the actor exploits higher-order latent structure rather than first/second moments. Compressed latents at $K=8$ (trained $M_\phi$) hold 66.43% seen / 60.45% unseen vs 70.48% / 65.42% full, with end-to-end message latency dropping from 9.19s → 0.20s (Qwen2.5-7B); a clear "aha" drop in separation loss appears around step ~2.2k.

## Why it matters here
General background; no direct arena tie. Relevant only as infrastructure for the autonomous-loop agent if multi-agent council dispatch is ever moved off natural-language transcripts — latent-channel communication could in principle preserve parallel hypotheses (the paper's claimed mechanism for the MATH Level-5 win) that CoT linearization collapses, which matches our council-dispatch rationale of "questions, not single answers."

## Open questions / connections
- Does the "parallel hypotheses preserved in latent space" claim hold under formal information-theoretic measurement, or is it inferred only from Top-k probability gaps?
- Cross-family transfer (Qwen→LLaMA) works without shared tokenizer — what is the minimal representational alignment needed, and does it survive when sender/receiver disagree on task framing?
- Compression to $K=8$ retains task utility but the paper does not test whether the compressed latents encode the *same* reasoning content or a different sufficient statistic — relevant if used to audit agent reasoning.
- Extends Coconut (Hao et al. 2024), activation grafting (Ramesh & Li 2025), and per-token latent deltas (Tang et al. 2025) by being fully language-free and adapter-trained rather than ad-hoc.

## Key terms
latent space communication, inter-agent communication, hidden state transmission, chain-of-thought compression, multi-agent LLM, Interlat, Jensen-Shannon separation loss, curriculum learning, latent reasoning, ALFWorld, MATH benchmark, parallel hypotheses
