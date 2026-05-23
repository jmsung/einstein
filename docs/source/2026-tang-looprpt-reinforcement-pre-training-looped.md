---
type: source
kind: paper
title: LoopRPT: Reinforcement Pre-Training for Looped Language Models
authors: Guo Tang, Shixin Jiang, Heng Chang, Nuo Chen, Yuhan Li, Huiming Fan, Jia Li, Ming Liu, Bing Qin
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2603.19714
source_local: ../raw/2026-tang-looprpt-reinforcement-pre-training-looped.pdf
topic: general-knowledge
cites: 
---

# LoopRPT: Reinforcement Pre-Training for Looped Language Models

**Authors:** Guo Tang, Shixin Jiang, Heng Chang, Nuo Chen, Yuhan Li, Huiming Fan, Jia Li, Ming Liu, Bing Qin  ·  **Year:** 2026  ·  **Source:** https://arxiv.org/abs/2603.19714

## One-line
Applies reinforcement pre-training (RPT) to Looped Language Models (LoopLMs), assigning dense step-wise RL rewards to latent recurrent iterations instead of output tokens, so the model compresses multi-step reasoning into fewer latent loops.

## Key claim
On Ouro-2.6B over OMNI-MATH, LoopRPT raises hard-token next-token accuracy by +3.58 (Peak, K=4) and +2.89 (Adaptive) while cutting average inference steps from 3.51 to 2.28 — Pareto-dominant accuracy/compute trade-off vs. vanilla Ouro and Qwen3-1.7B+CoT, with downstream gains on GSM8K (81.76 → 85.36), MBPP+ (+2.91), and HumanEval+.

## Method
A LoopLM ($h^{(k+1)} = f_\theta(h^{(k)}, x_{<t})$ with per-step exit-gate $\lambda^{(k)} = \sigma(a^{(k)})$ and survival $s^{(k+1)} = s^{(k)}(1-\lambda^{(k)})$) is trained via RPT with: (i) entropy-based top-$\rho\%$ hard-token selection using an EMA teacher ($\phi=0.995$); (ii) step-wise reward $R(k) = \Delta_{\text{acc}}(k) - C(k)$ where $\Delta_{\text{acc}}(k) = \ell(\theta_k) - \ell(\bar\theta_{t_{\text{ref}}})$ vs. teacher reference step $t_{\text{ref}} = \min\{k : \Pi_{\bar\theta}(k) \geq \tau\}$ and $C(k) = \lambda_t(k - t_{\text{ref}})$ with difficulty-aware $\lambda_t = \lambda_{\text{base}}(1 + \lambda_{\text{scale}}(1-d_t))$; (iii) Gaussian-noisy latent rollouts $h^{(k)} \leftarrow h^{(k)} + \epsilon$, $\epsilon \sim \mathcal{N}(0, \sigma^2 I)$ for GRPO-style policy gradient on the exit gate, combined with step-weighted NTP loss $L_{\text{rep}} = -\sum_k \pi_\theta(k)(1 + \text{ReLU}(\hat A(k)))\ell(\theta_k)$ plus entropy bonus and K3-surrogate KL to teacher.

## Result
On Ouro-1.4B and 2.6B: peak next-token accuracy improves uniformly across easy/medium/hard splits while adaptive-exit average steps drop ~1.2 steps. Exit distribution shifts mass to step 3 (early exit) while preserving step-4 dominance on truly hard tokens (Fig. 3). Ablations show $L_{\text{rep}}+L_{\text{ent}}$ is the largest contributor; removing Gaussian latent noise, KL stabilizer, hard-token filter, or time penalty each degrades accuracy or step-efficiency. Theoretical results: EMA teacher reference step is invariant under small drift (Prop. A.9), and noisy-rollout objective is $L\sigma\sqrt{d}$-close to deterministic via Lipschitz smoothing (Prop. A.6).

## Why it matters here
General background; no direct arena tie. Closest connection is the autonomous-loop agent design itself — the EMA-teacher reference + dense step-wise reward + noisy rollout pattern is a reusable template for any latent-iterative solver where credit assignment over internal steps matters. Not relevant to current math-optimizer problems (sphere packing, autocorrelation, kissing numbers).

## Open questions / connections
- Does the entropy-based "hard-token" filter transfer to non-text iterative computations (e.g., iterative LP refinement, basin-hopping inner loops) where "uncertainty" must be redefined?
- Can a difficulty-aware time penalty $\lambda_t \propto (1 - d_t)$ inform adaptive compute routing (compute-router rule) — spending more wall-clock on high-entropy / unverified score regions?
- Extends Ouro (Zhu et al. 2025) early-exit; relates to broader RPT line (Dong et al. 2025, Hatamizadeh et al. 2025) and high-entropy-minority token selection (Wang et al. 2025).

## Key terms
LoopRPT, reinforcement pre-training, RPT, looped language models, LoopLM, Ouro, latent reasoning, early exit, EMA teacher, GRPO, noisy latent rollout, step-wise reward, credit assignment, entropy-based token selection, KL surrogate, chain-of-thought, next-token reasoning
