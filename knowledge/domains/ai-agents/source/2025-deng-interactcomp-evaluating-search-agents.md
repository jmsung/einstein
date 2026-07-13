<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-retrieval, ai-verification]
title: InteractComp: Evaluating Search Agents With Ambiguous Queries
authors: [Mingyi Deng, Lijun Huang, Yan Fan, Jiayi Zhang, Fashen Ren, Jinyi Bai, F. Yang, Dayi Miao, Zhaoyang Yu, Yifan Wu, Yanfei Zhang, Fengwei Teng, Yingjia Wan, Song Hu, Yude Li, Xin Jin, Cong Hu, Haoyu Li, Qirui Fu, Tai Zhong, Xinyu Wang, Xiangru Tang, Nan Tang, Chenglin Wu, Yuyu Luo]
year: 2025
source_url: https://arxiv.org/abs/2510.24668
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# InteractComp: Evaluating Search Agents With Ambiguous Queries

**Authors:** Mingyi Deng, Lijun Huang, Yan Fan, Jiayi Zhang, Fashen Ren, Jinyi Bai, F. Yang, Dayi Miao, Zhaoyang Yu, Yifan Wu, Yanfei Zhang, Fengwei Teng, Yingjia Wan, Song Hu, Yude Li, Xin Jin, Cong Hu, Haoyu Li, Qirui Fu, Tai Zhong, Xinyu Wang, Xiangru Tang, Nan Tang, Chenglin Wu, Yuyu Luo  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2510.24668

## One-line
A benchmark of 210 deliberately-ambiguous search questions showing that current LLM search agents almost never ask clarifying questions even when they need to, and that this failure is overconfidence rather than missing capability.

## Key claim
On INTERACTCOMP, the best model (GPT-5) reaches only 13.73% accuracy in the full interactive setting versus 71.50% when given complete disambiguating context — a ~5× gap — and forced interaction roughly doubles accuracy (e.g. GPT-5: 20% → 40%), while interaction performance has stagnated at 6–14% over 15 months despite BrowseComp scores rising 7×.

## Method
Target–distractor benchmark construction: annotators pair a lesser-known target entity with a popular distractor, build the question from only their *shared* attributes, and reserve the target's *distinctive* attributes as hidden context that a simulated yes/no/I-don't-know responder holds. Agents use a ReAct loop with `search`, `ask`, and `answer` actions; evaluation across 17 models compares answer-only, search-only, with-context, and forced-interaction configurations (minimum $k$ clarifying questions required) and a scaling sweep over 5/10/20 max rounds.

## Result
Ablations: answer-only ≈ 1–8%, search-only ≈ 7–10%, with-context 41–72% — so reasoning/knowledge is present but interaction is the bottleneck. Scaling max rounds 5→20 barely moves interaction count (GPT-5: 1.14 → 1.90 asks) or accuracy (14 → 20%); calibration error drops sharply with interaction (GPT-4o-mini 37 CE vs Doubao-1.6 84 CE). Forced interaction is model-dependent: GPT-5 doubles, Claude-Sonnet-4 gains modestly, GPT-4o-mini degrades.

## Key terms
search agents, query ambiguity, clarification questions, ReAct, overconfidence, calibration error, target-distractor design, forced interaction, BrowseComp, RLVR, simulated user, interaction benchmark
