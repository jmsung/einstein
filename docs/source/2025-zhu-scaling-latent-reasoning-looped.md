---
type: source
kind: paper
title: Scaling Latent Reasoning via Looped Language Models
authors: Ruiming Zhu, Zixuan Wang, Kai Hua, Tianyu Zhang, Ziniu Li, Haoran Que, Boyi Wei, Zixin Wen, Fan Yin, He Xing, Lu Li, Jiajun Shi, Kaijing Ma, Shanda Li, Taylor Kergan, Andrew K Smith, Xin Qu, Mude Hui, Bohong Wu, Qiyang Min, Hongzhi Huang, Xun Zhou, Wei Ye, Jiaheng Liu, Jian Yang, Yunfeng Shi, Chenghua Lin, Enduo Zhao, Tianle Cai, Ge Zhang, Wenhao Huang, Y. Bengio, Jason K. Eshraghian
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2510.25741
source_local: ../raw/2025-zhu-scaling-latent-reasoning-looped.pdf
topic: general-knowledge
cites: 
---

# Scaling Latent Reasoning via Looped Language Models

**Authors:** Ruiming Zhu, Zixuan Wang, Kai Hua, Tianyu Zhang, Ziniu Li, Haoran Que, Boyi Wei, Zixin Wen, Fan Yin, He Xing, Lu Li, Jiajun Shi, Kaijing Ma, Shanda Li, Taylor Kergan, Andrew K Smith, Xin Qu, Mude Hui, Bohong Wu, Qiyang Min, Hongzhi Huang, Xun Zhou, Wei Ye, Jiaheng Liu, Jian Yang, Yunfeng Shi, Chenghua Lin, Enduo Zhao, Tianle Cai, Ge Zhang, Wenhao Huang, Y. Bengio, Jason K. Eshraghian  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2510.25741

## One-line
Pre-trained looped (weight-tied recurrent-depth) language models with a learned early-exit gate match transformers 2–3× their parameter count by performing latent reasoning iteratively inside a shared layer stack.

## Key claim
Ouro 1.4B and 2.6B LoopLMs, trained on 7.7T tokens with up to $T_{\max}=4$ recurrent steps, match or exceed 4B–12B standard transformers (Qwen3, Gemma3, DeepSeek-Distill) across MMLU, GSM8K, MATH500, AIME24/25, GPQA, HLE; gains come from improved knowledge *manipulation*, not increased storage (both architectures store ≈2 bits/parameter).

## Method
Stack of $N$ transformer layers $M_L$ is applied $t$ times: $F^{(t)} = \text{lmhead} \circ M_L^{\circ t} \circ \text{emb}$. At each step $t$ an exit gate emits $\lambda_t = \sigma(\text{Linear}(h^{(t)}))$, giving an exit-step distribution $p_\phi(t|x) = \lambda_t \prod_{j<t}(1-\lambda_j)$. Stage I trains jointly with entropy-regularized ELBO loss $\sum_t p_\phi(t|x)\mathcal{L}^{(t)} - \beta H(p_\phi)$ under a uniform prior (preventing collapse to $T_{\max}$); Stage II freezes the LM and fine-tunes the gate via BCE against an "ideal continuation" label $w_i^{(t)} = \sigma(k(I_i^{(t)} - \gamma))$ derived from realized per-step loss improvement.

## Result
Total-loss and step-wise-loss scaling laws of the form $\mathcal{L} = E + A/(N+t_1)^\alpha + B/(D+t_2)^\beta + C/(T+t_3)^\gamma$ fit empirically with $R^2 \approx 0.96$ (total) and 0.79–0.89 (step-wise) and generalize to unseen $N$, $D$, $T_{\max}$. Step-wise loss decreases monotonically with recurrent step (positive $\gamma$); for small models, shallow-step loss can *increase* with data as the gate routes mass to deeper steps to minimize expected loss. Safety (HEx-PHI) improves with more loops, and latent traces show greater output-faithfulness than CoT.

## Why it matters here
General background; no direct arena tie. The looped-architecture / adaptive-depth idea is orthogonal to the math-optimizer work — it's an LLM-architecture paper, not a math-optimization result. The most transferable piece is the *entropy-regularized ELBO with uniform prior* as a recipe for adaptive computation budgets, which has a faint analogy to compute-router decisions (when to spend more compute on hard inputs) but is not a math technique applicable to any of the 23 arena problems.

## Open questions / connections
- Does loop depth as a "third scaling axis" continue past $T_{\max}=8$, or saturate? Paper shows monotone gains but caps at 8.
- Connection to Universal Transformer (Dehghani et al.), Geiping et al. "recurrent depth", Coconut continuous-thought, PonderNet ELBO halting, Mixture-of-Recursions — LoopLM unifies these but doesn't isolate which component drives the manipulation-vs-storage gap.
- Whether the knowledge-manipulation advantage transfers to symbolic / numerical reasoning needed for math-olympiad-style problems (the agent's actual setting) — paper reports on AIME/MATH500 but not on optimization-style tasks.

## Key terms
looped language model, LoopLM, Ouro, Universal Transformer, weight tying, recurrent depth, latent reasoning, adaptive computation, early exit, entropy regularization, ELBO, PonderNet, chain-of-thought, parameter efficiency, scaling laws, knowledge manipulation
