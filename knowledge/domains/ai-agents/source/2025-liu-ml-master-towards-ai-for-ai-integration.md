<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-ml, ai-reasoning]
title: "ML-Master: Towards AI-for-AI via Integration of Exploration and Reasoning"
authors: [Zexi Liu, Yuzhu Cai, Xinyu Zhu, Yujie Zheng, Runkun Chen, Ying Wen, Yanfeng Wang, E. Weinan, Siheng Chen]
year: 2025
source_url: https://arxiv.org/abs/2506.16499
drive_file_id: 1_brl99HIbZ33zO50HT4I7Ixzgo01bsR5
text_source: paperclip
ingested_by: agent
---

# ML-Master: Towards AI-for-AI via Integration of Exploration and Reasoning

**Authors:** Zexi Liu, Yuzhu Cai, Xinyu Zhu, Yujie Zheng, Runkun Chen, Ying Wen, Yanfeng Wang, E. Weinan, Siheng Chen  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2506.16499

## One-line
An LLM-agent framework for automated ML engineering that couples MCTS-style parallel solution exploration with a reasoning model (DeepSeek-R1) via a selectively-scoped memory embedded into the model's "think" channel.

## Key claim
ML-Master achieves a 29.3% average medal rate on MLE-Bench (75 Kaggle-derived ML tasks), beating R&D-Agent (22.4%) and AIDE/o1-preview (16.9%), with 20.2% on medium-difficulty tasks (>2× prior best of 9.0%) — all within a 12-hour budget vs. the 24-hour baseline limit.

## Method
Two coupled modules. (1) *Balanced multi-trajectory exploration*: MCTS over solution nodes with UCT selection $\text{UCT}(v)=Q_v/N_v + C\sqrt{\ln N_{\text{parent}}/N_v}$, three expansion actions (Draft / Debug / Improve), a composite reward $R(v)=r_q+r_d+r_s$ (quality, debug-fix, improvement-stop), and asynchronous branch-parallel workers (parallelism 3). Pruning via $\tau_{\text{improve}}=3$ failed improves at threshold $t=0.001$ and $\tau_{\text{debug}}=20$. (2) *Steerable reasoning*: an adaptive memory $M_t=\{(r_{t-1},f_{t-1})\}\cup\{(r_t^{(s)},f_t^{(s)})\}_{s\in S_t}$ aggregating the immediate parent's extracted insights + execution feedback plus *sibling* nodes' (contrastive) memory, injected into the LLM's `<think>` block rather than the prompt instruction.

## Result
On MLE-Bench with DeepSeek-R1-0120: valid-submission 93.3%, above-median 44.9%, gold 17.3%, silver+ 7.6%, bronze+ 4.4%, any-medal 29.3% (mean of 3 seeds, SEM ≤1.3). Per complexity: Low 48.5%, Medium 20.2%, High 24.4% — outperforming all baselines on every dimension. Solution quality monotonically improves over the 12-hour wall-clock per Figure 7. No formal theorems; empirical ablations are deferred.

## Key terms
AI4AI, MLE-Bench, Monte Carlo Tree Search, UCT, parallel branch search, steerable reasoning, adaptive memory, sibling-contrastive context, DeepSeek-R1, draft-debug-improve actions, LLM agent, autonomous ML engineering
