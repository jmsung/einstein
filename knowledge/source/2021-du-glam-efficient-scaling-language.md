---
type: source
kind: paper
title: "GLaM: Efficient Scaling of Language Models with Mixture-of-Experts"
authors: Nan Du, Yanping Huang, Andrew M. Dai, Simon Tong, Dmitry Lepikhin, Yuanzhong Xu, M. Krikun, Yanqi Zhou, Adams Wei Yu, Orhan Firat, Barret Zoph, L. Fedus, Maarten Bosma, Zongwei Zhou, Tao Wang, Yu Emma Wang, Kellie Webster, Marie Pellat, Kevin Robinson, K. Meier-Hellstern, Toju Duke, Lucas Dixon, Kun Zhang, Quoc V. Le, Yonghui Wu, Z. Chen, Claire Cui
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2112.06905
source_local: ../raw/2021-du-glam-efficient-scaling-language.pdf
topic: general-knowledge
cites:
---

# GLaM: Efficient Scaling of Language Models with Mixture-of-Experts

**Authors:** Nan Du, Yanping Huang, Andrew M. Dai, Simon Tong, Dmitry Lepikhin, Yuanzhong Xu, M. Krikun, Yanqi Zhou, Adams Wei Yu, Orhan Firat, Barret Zoph, L. Fedus, Maarten Bosma, Zongwei Zhou, Tao Wang, Yu Emma Wang, Kellie Webster, Marie Pellat, Kevin Robinson, K. Meier-Hellstern, Toju Duke, Lucas Dixon, Kun Zhang, Quoc V. Le, Yonghui Wu, Z. Chen, Claire Cui  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2112.06905

## One-line
Scales a decoder-only language model to 1.2T parameters via sparsely-activated Mixture-of-Experts (MoE), matching/beating GPT-3 at ~1/2 inference FLOPs and ~1/3 training energy.

## Key claim
GLaM (64B/64E) with 1.2T total params but only 96.6B activated per token outperforms GPT-3 (175B dense) on average across 29 NLP benchmarks in zero/one/few-shot settings (zero-shot 62.7 vs 56.9, one-shot 65.5 vs 61.6, few-shot 68.1 vs 65.2), using 180 vs 350 GFLOPs/token and 456 vs 1287 MWh training energy.

## Method
Replace every other Transformer feed-forward sub-layer with an MoE layer of $E=64$ experts; a softmax gating network selects the top-2 experts per token, yielding $O(E^2)$ effective FFN combinations. Adds GShard-style auxiliary load-balancing loss (coef 0.01), GLU + GELU FFNs, per-layer relative positional bias, Adafactor optimizer ($\beta_1=0$, $\beta_2=0.99$, $1-t^{-0.8}$ decay), and 2D-sharded model partitioning (GSPMD) across 1024 TPU-v4 chips.

## Result
Sparsity beats dense at matched activated-FLOPs across the entire $0.1$B–$137$B scaling sweep (Fig. 3a/b); on TriviaQA open-domain, 1-shot GLaM hits 75.0 (test), exceeding GPT-3 64-shot (71.2) and the fine-tuned KG-FiD SOTA (69.8). Data-quality ablation (1.7B/64E): filtered web (143B tok) consistently beats unfiltered (~7T tok), especially on NLG. Closes the WinoGender stereotypical / anti-stereotypical gap.

## Why it matters here
General background; no direct arena tie — this is NLP scaling, not math optimization. Possibly relevant only as meta-evidence for "sparsity + conditional computation > brute dense scaling," which loosely parallels the agent's compute-router principle of routing each workload to its best-fit substrate rather than scaling one monolithic engine.

## Open questions / connections
- Does top-$k$ expert routing have any structural analogue in optimizer ensembles (e.g., gated dispatch among basin-hoppers / CMA-ES / SLSQP per problem class)?
- Filtered-data-beats-bulk mirrors the wiki's `knowledge/source/` distillation discipline — quantitative evidence that curation > volume.
- Extends Shazeer 2017 (sparsely-gated MoE), GShard (Lepikhin 2021), Switch-C (Fedus 2021); leaves open whether MoE works for non-language modalities and reasoning-heavy tasks.

## Key terms
mixture-of-experts, MoE, sparse activation, conditional computation, top-2 gating, GShard, Switch Transformer, decoder-only language model, GPT-3, scaling laws, GSPMD, 2D sharding, Adafactor, GLU activation, load balancing loss
