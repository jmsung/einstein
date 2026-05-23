---
type: source
kind: paper
title: Agentic Reinforced Policy Optimization
authors: Guanting Dong, Hangyu Mao, Kai Ma, Licheng Bao, Yifei Chen, Zhongyuan Wang, Zhongxia Chen, Jiazhen Du, Huiyang Wang, Fuzheng Zhang, Guorui Zhou, Yutao Zhu, Ji-Rong Wen, Zhicheng Dou
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2507.19849
source_local: ../raw/2025-dong-agentic-reinforced-policy-optimization.pdf
topic: general-knowledge
cites:
---

# Agentic Reinforced Policy Optimization

**Authors:** Guanting Dong, Hangyu Mao, Kai Ma, Licheng Bao, Yifei Chen, Zhongyuan Wang, Zhongxia Chen, Jiazhen Du, Huiyang Wang, Fuzheng Zhang, Guorui Zhou, Yutao Zhu, Ji-Rong Wen, Zhicheng Dou  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2507.19849

## One-line
Proposes ARPO, an agentic RL algorithm that adaptively branches rollouts at high-entropy steps following tool calls, training LLMs to interleave reasoning with search/code/browser tools more efficiently than trajectory-level RL.

## Key claim
On 13 benchmarks (math, multi-hop QA, deep search including GAIA, HLE, xbench), ARPO outperforms trajectory-level baselines (GRPO, DAPO, REINFORCE++) while using only ~half the tool-call budget; deep-search gains achieved with just 1K RL samples on 8B/14B backbones.

## Method
Pilot analysis shows token entropy spikes sharply in the first 10–50 tokens after each tool-call return (search feedback > Python). ARPO exploits this with: (1) **entropy-based adaptive rollout** — start with $N$ global trajectories, monitor normalized $\Delta H_t = \text{Normalize}(H_t - H_{\text{initial}})$ after each tool call, and branch $Z$ partial rollouts when $P_t = \alpha + \beta \cdot \Delta H_t > \tau$; (2) **advantage attribution estimation** — shared-prefix tokens get averaged advantage (hard) or, by default, soft attribution via GRPO's importance ratio $r_{i,t}(\theta) = \pi_\theta(y_{i,t}|x,y_{i,<t}) / \pi_{\text{ref}}(\cdot)$, which automatically equates ratios on shared prefixes; (3) **Generalized Policy Gradient theorem** for macro-actions $MA_i = \langle OT_m,\ldots,OT_{m+n}\rangle$, proving $\nabla_\theta J(\theta) = \mathbb{E}_\tau[\sum_T \nabla_\theta \log \pi_\theta(MA_T|MS_T) A_T(\tau)]$ as a generalization of the per-token policy gradient.

## Result
Rollout complexity drops from trajectory-level $O(n^2)$ to between $O(n \log n)$ and $O(n^2)$. Hierarchical reward $R = \max(\text{Acc}+r_M, \text{Acc})$ adds a $+0.1$ multi-tool bonus when both `<search>` and `<python>` appear with correct answer + format. Soft advantage estimation yields higher, more stable reward curves than hard. Cold-start SFT (54K Tool-Star + 0.8K STILL) then RL on 10K (reasoning) or 1K (deep search) samples; 7B trained on 8×H800, 14B on 16×H800.

## Why it matters here
General background; no direct arena tie. Relevant only if the einstein agent itself moves to RL-trained tool use — the entropy-spike-after-tool-call observation and macro-action policy gradient could inform how to budget exploration when the agent branches between optimizer calls, mpmath polishes, and wiki queries.

## Open questions / connections
- Does the entropy spike after tool calls reproduce for math-heavy tools (HiGHS LP solves, mpmath polish, basin-hopping returns) the way it does for web search?
- Can the macro-action GPG framing be adapted to reward-shaping over compute-routing decisions (local CPU vs MPS vs Modal) rather than just tool selection?
- Extends GRPO/DAPO/REINFORCE++ trajectory-level RL; leaves open whether entropy-based branching helps when tool feedback is deterministic (Python) vs informative-textual (search) — paper itself notes search introduces more uncertainty (Ob.3).

## Key terms
agentic RL, GRPO, DAPO, REINFORCE++, entropy-based rollout, token entropy, tool-use, macro-action policy gradient, advantage attribution, importance sampling ratio, multi-turn LLM agent, deep search, GAIA, HLE, RLVR
