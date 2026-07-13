<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-foundation-models]
title: Enabling Agents to Communicate Entirely in Latent Space
authors: [Zhuoyun Du, Runze Wang, Huiyu Bai, Zouying Cao, Xiaoyong Zhu, Bo Zheng, Wei Chen, Haochao Ying]
year: 2025
source_url: https://arxiv.org/abs/2511.09149
drive_file_id: 1aPkvoLy0jmGqZ6VrhgyiMc-ZjhS45UZ_
text_source: paperclip
ingested_by: agent
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

## Key terms
latent space communication, inter-agent communication, hidden state transmission, chain-of-thought compression, multi-agent LLM, Interlat, Jensen-Shannon separation loss, curriculum learning, latent reasoning, ALFWorld, MATH benchmark, parallel hypotheses
