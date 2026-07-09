---
type: source
kind: paper
title: Qwen3 Technical Report
authors: An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao, Chengen Huang, Chenxu Lv, Chujie Zheng, Dayiheng Liu, Fan Zhou, Fei Huang, Feng Hu, Hao Ge, Haoran Wei, Huan Lin, Jialong Tang, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin Yang, Jiaxin Yang, Jingren Zhou, Jingren Zhou, Junyan Lin, K. Dang, Keqin Bao, Ke‐Pei Yang, Le Yu, Li-Chun Deng, Mei Li, Min Xue, Mingze Li, Pei Zhang, Peng Wang, Qin Zhu, Rui Men, Ruize Gao, Shi-Qiang Liu, Shuang Luo, Tianhao Li, Tianyi Tang, Wenbiao Yin, Xingzhang Ren, Xinyu Wang, Xinyu Zhang, Xuancheng Ren, Yang Fan, Yang Su, Yi-Chao Zhang, Yinger Zhang, Yu Wan, Yuqiong Liu, Zekun Wang, Zeyu Cui, Zhenru Zhang, Zhipeng Zhou, Zihan Qiu
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2505.09388
source_local: ../raw/2025-yang-qwen3-technical-report.pdf
topic: general-knowledge
cites:
---

# Qwen3 Technical Report

**Authors:** An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao, Chengen Huang, Chenxu Lv, Chujie Zheng, Dayiheng Liu, Fan Zhou, Fei Huang, Feng Hu, Hao Ge, Haoran Wei, Huan Lin, Jialong Tang, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin Yang, Jiaxin Yang, Jingren Zhou, Jingren Zhou, Junyan Lin, K. Dang, Keqin Bao, Ke‐Pei Yang, Le Yu, Li-Chun Deng, Mei Li, Min Xue, Mingze Li, Pei Zhang, Peng Wang, Qin Zhu, Rui Men, Ruize Gao, Shi-Qiang Liu, Shuang Luo, Tianhao Li, Tianyi Tang, Wenbiao Yin, Xingzhang Ren, Xinyu Wang, Xinyu Zhang, Xuancheng Ren, Yang Fan, Yang Su, Yi-Chao Zhang, Yinger Zhang, Yu Wan, Yuqiong Liu, Zekun Wang, Zeyu Cui, Zhenru Zhang, Zhipeng Zhou, Zihan Qiu  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2505.09388

## One-line
Technical report for the Qwen3 LLM family (0.6B–235B params, dense + MoE), introducing a unified thinking / non-thinking mode and a tunable thinking budget.

## Key claim
Qwen3-235B-A22B (MoE, 235B total / 22B activated) matches or beats DeepSeek-V3, Llama-4-Maverick, and Qwen2.5-72B across 14/15 base benchmarks, and in thinking mode reaches 85.7 on AIME'24, 81.5 on AIME'25, 70.7 on LiveCodeBench v5, 2,056 on CodeForces, and 70.8 on BFCL v3 — competitive with o1 / o3-mini / DeepSeek-V3 — while integrating reasoning and chat into a single model whose reasoning depth can be controlled by a user-set thinking-token budget.

## Method
Architecture: GQA + SwiGLU + RoPE (ABF base $10^6$) + RMSNorm pre-norm + QK-Norm (no QKV-bias); MoE variant uses 128 experts / 8 activated, no shared experts, global-batch load-balancing loss. Pre-training: 36T tokens across 119 languages in three stages (general 30T@4k → reasoning 5T@4k STEM/code-heavy → long-context @32k with YARN + Dual Chunk Attention for 4× extension). Post-training: four-stage pipeline — long-CoT cold start → reasoning RL (math/code) → thinking-mode fusion (merging CoT and non-CoT data) → general-domain RL; smaller models trained via strong-to-weak distillation (off-policy + on-policy) from the flagships, reported as outperforming RL in both accuracy and training cost.

## Result
Qwen3-235B-A22B-Base beats DeepSeek-V3-Base on 14/15 benchmarks with ~1/3 total params and 2/3 activated params; Qwen3-32B-Base matches Qwen2.5-72B-Base with <½ the params; Qwen3-30B-A3B (3B active) matches Qwen3-14B-Base at ~1/5 active params. Multilingual coverage expands 29 → 119 languages with strong Belebele, MMMLU, MGSM, INCLUDE, and PolyMath scores. Empirically, increasing the thinking-token budget yields consistent monotone gains across reasoning benchmarks.

## Why it matters here
General background; no direct arena tie — Qwen3 is a frontier open-weight model family, not a math-optimization paper. Relevant only insofar as the autonomous-loop agent might use such models as backbone reasoners (thinking-mode + budget control + Apache-2.0 weights are practical hooks), but it contributes no mathematical technique to sphere packing, kissing, autocorrelation, or any of the 23 Einstein Arena problems.

## Open questions / connections
- How does the thinking-budget scaling curve interact with math-specific verifier feedback (e.g., triple-verify loops) — does more budget on AIME-style tasks actually find better optima, or just longer rationalizations?
- Strong-to-weak distillation reportedly beats RL for small models — does this generalize to distilling a math-solving agent's wiki/findings into a small on-device reasoner?
- Extends the Qwen2.5 / QwQ-32B line; relates to DeepSeek-R1's RL-for-reasoning paradigm but unifies reasoning + chat in a single weight set.

## Key terms
Qwen3, Mixture-of-Experts, MoE, thinking mode, thinking budget, chain-of-thought, long-CoT cold start, reasoning RL, strong-to-weak distillation, GQA, QK-Norm, YARN, Dual Chunk Attention, multilingual LLM, AIME, LiveCodeBench, BFCL, DeepSeek-V3, Llama-4, GPT-4o
