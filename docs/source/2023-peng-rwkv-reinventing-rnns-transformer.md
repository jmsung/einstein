---
type: source
kind: paper
title: "RWKV: Reinventing RNNs for the Transformer Era"
authors: Bo Peng, Eric Alcaide, Quentin Anthony, Alon Albalak, Samuel Arcadinho, Stella Biderman, Huanqi Cao, Xin Cheng, Michael Chung, Matteo Grella, G. Kranthikiran, Xingjian Du, Xuming He, Haowen Hou, Przemyslaw Kazienko, Jan Kocoń, Jiaming Kong, Bartlomiej Koptyra, Hayden Lau, Krishna Sri Ipsit Mantri, Ferdinand Mom, Atsushi Saito, Xiangru Tang, Bolun Wang, J. S. Wind, Stansilaw Wozniak, Ruichong Zhang, Zhenyuan Zhang, Qihang Zhao, P. Zhou, Jian Zhu, Rui Zhu
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2305.13048
source_local: ../raw/2023-peng-rwkv-reinventing-rnns-transformer.pdf
topic: general-knowledge
cites:
---

# RWKV: Reinventing RNNs for the Transformer Era

**Authors:** Bo Peng, Eric Alcaide, Quentin Anthony, Alon Albalak, Samuel Arcadinho, Stella Biderman, Huanqi Cao, Xin Cheng, Michael Chung, Matteo Grella, G. Kranthikiran, Xingjian Du, Xuming He, Haowen Hou, Przemyslaw Kazienko, Jan Kocoń, Jiaming Kong, Bartlomiej Koptyra, Hayden Lau, Krishna Sri Ipsit Mantri, Ferdinand Mom, Atsushi Saito, Xiangru Tang, Bolun Wang, J. S. Wind, Stansilaw Wozniak, Ruichong Zhang, Zhenyuan Zhang, Qihang Zhao, P. Zhou, Jian Zhu, Rui Zhu  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2305.13048

## One-line
A new sequence architecture (RWKV) that trains like a Transformer in parallel but runs inference like an RNN in linear time and constant memory, scaled to 14B parameters.

## Key claim
RWKV achieves performance on par with similarly-sized Transformers (Pythia, OPT, BLOOM) on standard NLP benchmarks while reducing inference complexity from $O(T^2 d)$ time and $O(T^2 + Td)$ space (Transformer) to $O(Td)$ time and $O(d)$ space — the lowest among compared architectures.

## Method
Replaces dot-product attention $\mathrm{softmax}(QK^\top)V$ with a channel-wise linear-attention variant inspired by AFT: pairwise weights $w_{t,i} = -(t-i)w$ become a channel-wise time-decay vector with $w \in (\mathbb{R}_{\geq 0})^d$, so the attention reduces to a recurrence. Each block has a time-mixing sub-block (R, K, V with token shift and a WKV operator using exponential decay plus a "bonus" term $u$ for the current token) and a channel-mixing sub-block with sigmoid receptance gating $\sigma(r)$ and squared-ReLU activation. This dual formulation supports $O(BTd^2)$ parallel training (time-parallel mode) and $O(Td)$ recurrent inference (time-sequential mode); numerical stability is maintained via an auxiliary state $p_t$ that tracks the max exponent.

## Result
Six pretrained models from 169M to 14B parameters (the largest dense RNN trained at that time) on 330B tokens of the Pile. Loss-vs-compute follows the Transformer scaling law form with $r^2 = 0.994$ on Pareto-optimal points (0.875 extrapolated an order of magnitude). Test loss decreases monotonically with context length up to 8192 after progressive fine-tuning. On Long-Range Arena, RWKV is second to S4 on five of six tasks. Inference time scales linearly with sequence length where Transformers scale quadratically. Gradient stability is proved (Appendix H): bounded inputs yield uniformly bounded $\partial L_T/\partial W_k, \partial L_T/\partial W_v$ for all $T$.

## Why it matters here
General background; no direct arena tie. May inform future infrastructure choices if the agent needs long-context language-model components, but the paper has no bearing on the math-optimization problem families (sphere packing, autocorrelation, kissing numbers, extremal graphs, sieve theory) that drive Einstein Arena work.

## Open questions / connections
- Can the WKV recurrence be parallelized via a parallel scan to reduce training cost to $O(B \log(T) d)$?
- Single-vector recurrent state limits fine-grained "look-back" recall over very long contexts — what tasks does this bottleneck on, and can larger internal states close the gap?
- RWKV shows high sensitivity to prompt ordering (RTE F1 jumped from 44.2% → 74.8% after re-ordering), suggesting RNN-style architectures need different prompting conventions than Transformers.
- Extends the AFT (Attention Free Transformer, Zhai et al. 2021) line and connects to linear-attention work (Katharopoulos et al. 2020, Performer, Linear Transformer) and state-space models (S4).

## Key terms
RWKV, linear attention, RNN, Transformer, AFT (Attention Free Transformer), time-mixing, channel-mixing, channel-wise time decay, receptance gating, token shift, parallel scan, scaling laws, Long-Range Arena, S4, Pile pretraining, gradient stability
