---
type: source
kind: paper
title: Attention is All you Need
authors: Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, I. Polosukhin
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1706.03762
source_local: ../raw/2017-vaswani-attention-all-you-need.pdf
topic: general-knowledge
cites:
---

# Attention is All you Need

**Authors:** Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, I. Polosukhin  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1706.03762

## One-line
Introduces the Transformer, a sequence transduction architecture built entirely from attention layers, dispensing with recurrence and convolution.

## Key claim
A pure-attention encoder–decoder matches or beats RNN/CNN seq2seq SOTA on machine translation: 28.4 BLEU on WMT'14 EN–DE (+2 over prior best, including ensembles) and 41.8 BLEU on WMT'14 EN–FR (new single-model SOTA) at $\sim$1/4 the training cost, trainable in 3.5 days on 8 P100 GPUs.

## Method
Stacked self-attention + position-wise feed-forward layers (N=6) with residual connections and LayerNorm in both encoder and decoder. The core primitive is *scaled dot-product attention*, $\text{Attention}(Q,K,V)=\text{softmax}(QK^T/\sqrt{d_k})V$, computed in parallel across $h=8$ heads on linearly projected $Q,K,V$ subspaces (multi-head attention). Order is injected by fixed sinusoidal positional encodings $PE_{pos,2i}=\sin(pos/10000^{2i/d_{model}})$, $PE_{pos,2i+1}=\cos(\cdot)$, with $d_{model}=512$, $d_{ff}=2048$.

## Result
Self-attention reduces the maximum signal path length between any two positions to $O(1)$ vs $O(n)$ for RNNs and $O(\log_k n)$ for dilated CNNs, at per-layer complexity $O(n^2 \cdot d)$, which is favorable when $n<d$. Beyond translation, a 4-layer Transformer reaches WSJ-23 F1 = 91.3 (WSJ-only) / 92.7 (semi-supervised) on English constituency parsing with minimal task-specific tuning. Ablations show that $h=8$ heads and key dimension $d_k=64$ are near-optimal; learned vs sinusoidal positional encodings are essentially equivalent.

## Why it matters here
General background; no direct arena tie — Transformer architecture is the substrate of the LLM agent itself (its reasoning capacity, scaled dot-product attention, positional encoding) rather than a math technique for sphere packing / autocorrelation. Useful as the foundational citation when discussing why the agent can do anything at all, or when reasoning about attention-based representations in any future neural ansatz for an arena problem.

## Open questions / connections
- Restricted/local attention with neighborhood size $r$ (path length $O(n/r)$) — relevant if ever applying attention to long structured math objects.
- Why scaling by $\sqrt{d_k}$: dot products of independent unit-variance vectors have variance $d_k$, pushing softmax into low-gradient regions — a precision/conditioning intuition applicable beyond NLP.
- Extends prior attention work (Bahdanau, ConvS2S, ByteNet, end-to-end memory networks); leaves open extensions to non-text modalities and less-sequential generation.

## Key terms
Transformer, self-attention, scaled dot-product attention, multi-head attention, encoder-decoder, sinusoidal positional encoding, layer normalization, residual connection, sequence transduction, machine translation, BLEU, softmax saturation, Vaswani
