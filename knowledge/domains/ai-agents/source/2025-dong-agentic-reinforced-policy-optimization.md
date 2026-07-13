<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: Agentic Reinforced Policy Optimization
authors: [Guanting Dong, Hangyu Mao, Kai Ma, Licheng Bao, Yifei Chen, Zhongyuan Wang, Zhongxia Chen, Jiazhen Du, Huiyang Wang, Fuzheng Zhang, Guorui Zhou, Yutao Zhu, Ji-Rong Wen, Zhicheng Dou]
year: 2025
doi: 10.48550/arXiv.2507.19849
source_url: https://doi.org/10.48550/arXiv.2507.19849
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Agentic Reinforced Policy Optimization

## TL;DR
ARPO is a reinforcement-learning algorithm for training multi-turn, tool-using LLM agents that branches its rollout sampling adaptively at high-entropy steps immediately after tool calls — where the model is most uncertain — yielding better tool-integrated reasoning than trajectory-level RL (GRPO/DAPO/REINFORCE++) while using roughly **half the tool-call budget**.

## Key findings
- **Core empirical observation**: token-generation entropy spikes sharply in the first 10–50 tokens *after* each tool-call return, exceeding the entropy of the original prompt (Fig. 1–2). Search-engine feedback induces more uncertainty than Python-interpreter feedback (informative text vs. deterministic numbers). Trajectory-level RL ignores this step-level uncertainty.
- **Entropy-based adaptive rollout**: given a global rollout budget M, the model first draws N full trajectories (recording initial entropy of the first k tokens), then reserves M−N for *partial* sampling. After each tool call it generates k extra tokens, computes normalized entropy change ΔHₜ, and branches Z partial paths when sampling probability Pₜ = α + β·ΔHₜ exceeds threshold τ. Reduces per-rollout complexity from trajectory-RL's O(n²) to between O(n log n) and O(n²).
- **Advantage Attribution Estimation**: assigns shared advantage to tokens on common reasoning prefixes and distinct advantage to branched tokens. A *soft* setting (leveraging GRPO's importance-sampling ratio, which is identical across shared prefixes) outperforms the *hard* setting, giving higher and more stable rewards (Fig. 5); ARPO defaults to soft.
- **Hierarchical reward** (following Tool-Star): correctness + format + a multi-tool collaboration bonus rₘ = 0.1 when both `<search>` and `<python>` are used correctly.
- **Results across 13 benchmarks** (math, knowledge-intensive QA, deep search):
  - On 10 math/knowledge tasks, ARPO beats all trajectory-level RL baselines, ~**+4% average accuracy** across Qwen2.5-3B/7B and Llama3.1-8B backbones (Table 1).
  - On deep search with only **1K RL training samples**: Qwen3-14B+ARPO reaches **GAIA 43.2%**, **HLE 10.0%**, vs. GPT-4o (HLE 2.0%) and DeepSeek-R1-671B (HLE 8.6%); ~6% gains over GRPO on GAIA and WebWalkerQA (Table 2).
  - Pass@5 scaling: Qwen3-14B+ARPO hits GAIA 61.2%, HLE 24.0%, xbench-DR 59% (Fig. 6).
  - Tool-call efficiency: matches/exceeds GRPO accuracy on Qwen2.5-7B with **half the tool calls** (Fig. 7).
- **Scaling/ablations**: performance peaks at entropy weight ~0.4 (declines at 1.0), initial sampling size N=8 (of M=16; a 1:1 global:partial ratio), and rises with larger global rollout size M. Browser-agent capability strongly correlates with deep-search accuracy — snippet-only is worst; a stronger QWQ-32B browser lifts Qwen3-14B GAIA to 47.6%, HLE 32.3% (Table 3).
- **Theory**: a Generalized Policy Gradient (GPG) theorem shows Transformer-based policies can be optimized over arbitrary-length "macro actions" (partial-rollout segments), generalizing the single-token Policy Gradient theorem.

## Methods (brief)
Cold-start SFT (Tool-Star's 54K samples + 0.8K STILL math data, LLaMA-Factory) followed by RL (VERL framework) on 10K samples for deep-reasoning tasks and only 1K mixed hard search samples for deep-search. Three tools: Bing search engine (top-10 snippets), a browser agent that fetches/summarizes pages (up to 6000 tokens), and a sandboxed Python interpreter. Tool-output tokens are excluded from loss. Evaluated pass@1 (temp 0.6, top-p 0.95) with F1 and LLM-as-judge (Qwen2.5-72B).

## Limitations
Deep-search RL used only 1K training samples and short runs (2–5 epochs on 8–16 H800 GPUs); gains are demonstrated on ≤14B open models, not validated at frontier scale. Entropy benefit is non-monotonic (hurts at high weight), so threshold/weight tuning is required. No biological or chemical task evaluation; transfer to scientific tool-use is untested.

## Citations of interest
- Dong et al. 2025, *Tool-Star* — multi-tool RL reasoner; supplies ARPO's reward design and training data.
- Shao et al. 2024, *DeepSeekMath/GRPO* — the trajectory-level RL baseline ARPO builds on and beats.
- Yu et al. 2025, *DAPO* — strong single-turn RL baseline that underperforms ARPO in multi-turn settings.
- Wang et al. 2025c, "Beyond the 80/20 rule" — high-entropy minority tokens drive effective RL, motivating the entropy lens.
- Mialon et al. 2024, *GAIA* — general AI assistant benchmark used as the headline deep-search evaluation.
- Yao et al. 2022, *ReAct* — reasoning+acting paradigm baseline for tool-using agents.
